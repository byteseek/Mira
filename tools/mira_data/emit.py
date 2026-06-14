"""Emit the ingestion / evidence / ledger artifacts the spec demands.

Turns a list of :class:`~tools.mira_data.canonical.CanonicalRecord` into:

- ``dataset-manifest.json``        (templates/ingestion-layer/dataset-manifest.json shape)
- ``ingestion-log.csv`` row        (25 cols)
- ``evidence-log.csv`` rows        (v1.2, 22 cols, pre-tagged)
- ``calculation-ledger.csv`` rows  (14 cols) — only for ``derived`` records (§8)

Everything is stdlib (csv/json). The emitter never invents an evidence tier; it
reads it off each record's posture.
"""

from __future__ import annotations

import csv
import datetime as _dt
import json
import os
from typing import Iterable

from .canonical import CanonicalRecord

EVIDENCE_COLUMNS = [
    "source_id", "claim_area", "claim_type", "claim_text", "source_speaker",
    "verification_status", "authority_level", "source_date", "as_of_date",
    "url_or_path", "used_by_agent", "used_by_skill", "confidence",
    "upstream_sources", "notes", "evidence_category", "freshness_status",
    "conflict_status", "treatment", "readiness_impact", "source_language",
    "translation_basis",
]

LEDGER_COLUMNS = [
    "calculation_id", "research_object", "question", "metric", "formula",
    "input_sources", "period", "unit", "result", "cross_check", "tool_used",
    "verification_status", "limitations", "evidence_log_ref",
]

INGESTION_COLUMNS = [
    "ingestion_id", "ingestion_route", "research_object", "market_scope",
    "provider_or_submitter", "source_id", "source_class", "access_method",
    "acquisition_mode", "license_scope", "storage_scope", "redistribution_allowed",
    "received_at", "source_date", "as_of_date", "retrieved_at", "dataset_location",
    "field_coverage", "row_count", "quality_status", "evidence_log_mapping",
    "calculation_ledger_required", "readiness_impact", "must_refresh_if", "notes",
]

# Per-source distribution policy (kept out of Posture, which is evidence-tier only).
SOURCE_POLICY = {
    "sec_companyfacts_api": dict(
        provider="U.S. Securities and Exchange Commission", speaker="issuer",
        license_scope="public_domain_official", storage_scope="tracked_allowed",
        redistribution_allowed="yes", readiness_impact="supports_durable_conclusion",
        freshness_status="acceptable_for_period", confidence="high",
    ),
    "bls_public_data_api": dict(
        provider="U.S. Bureau of Labor Statistics", speaker="BLS",
        license_scope="public_domain_official", storage_scope="tracked_allowed",
        redistribution_allowed="yes", readiness_impact="supports_durable_conclusion",
        freshness_status="acceptable_for_period", confidence="high",
    ),
    "yahoo_chart_api_v8": dict(
        provider="Yahoo Finance", speaker="market",
        license_scope="public_market_data_personal_use", storage_scope="tracked_allowed",
        redistribution_allowed="derived_only", readiness_impact="supports_working_view",
        freshness_status="acceptable_for_period", confidence="medium",
    ),
    "ibkr_gateway_local": dict(
        provider="Interactive Brokers local Gateway", speaker="broker_gateway",
        license_scope="user_authorized_brokerage_session", storage_scope="private",
        redistribution_allowed="no", readiness_impact="supports_working_view",
        freshness_status="current", confidence="medium",
    ),
}

_DEFAULT_POLICY = dict(
    provider="unknown", speaker="provider", license_scope="unknown", storage_scope="private",
    redistribution_allowed="unknown", readiness_impact="supports_working_view",
    freshness_status="unknown", confidence="medium",
)


def emit_bundle(
    records: list[CanonicalRecord],
    *,
    out_dir: str,
    research_object: str,
    market_scope: str,
    endpoint: str,
    params: str = "",
    ingestion_route: str = "public_on_demand",
    must_refresh_if: str = "",
    used_by_agent: str = "mira_data",
    used_by_skill: str = "data-acquisition",
    series: dict | None = None,
) -> dict:
    """Write the artifacts to ``out_dir`` and return their paths.

    ``series`` (optional ``{"name","columns","rows"}``) is a bulk time-series
    dataset written as a side CSV; when present the manifest points at it and
    its row count, while the evidence rows still come from ``records``.
    """
    if not records:
        raise ValueError("no records to emit")
    os.makedirs(out_dir, exist_ok=True)
    retrieved_at = _dt.date.today().isoformat()
    source_id = records[0].posture.source_id
    policy = SOURCE_POLICY.get(source_id, _DEFAULT_POLICY)
    ingestion_id = f"{source_id}__{research_object}__{retrieved_at}".lower()

    evidence_rows = [_evidence_row(r, policy, used_by_agent, used_by_skill) for r in records]
    ledger_rows = [_ledger_row(r) for r in records if r.derived]

    manifest_path = os.path.join(out_dir, "dataset-manifest.json")
    evidence_path = os.path.join(out_dir, "evidence-log.csv")
    ledger_path = os.path.join(out_dir, "calculation-ledger.csv")
    ingestion_path = os.path.join(out_dir, "ingestion-log.csv")

    series_path = None
    if series:
        series_path = os.path.join(out_dir, f"{series['name']}.csv")
        _append_csv(series_path, series["columns"], series["rows"])
        dataset_location = os.path.relpath(series_path)
        row_count = len(series["rows"])
        field_coverage = _series_field_coverage(series, records[0])
    else:
        dataset_location = os.path.relpath(manifest_path)
        row_count = len(records)
        field_coverage = _record_field_coverage(records)

    _write_manifest(
        manifest_path, records=records, ingestion_id=ingestion_id,
        ingestion_route=ingestion_route, research_object=research_object,
        market_scope=market_scope, endpoint=endpoint, params=params,
        policy=policy, retrieved_at=retrieved_at, ledgered=bool(ledger_rows),
        must_refresh_if=must_refresh_if, dataset_location=dataset_location,
        row_count=row_count, field_coverage=field_coverage,
    )
    _append_csv(evidence_path, EVIDENCE_COLUMNS, evidence_rows)
    if ledger_rows:
        _append_csv(ledger_path, LEDGER_COLUMNS, ledger_rows)
    _append_csv(ingestion_path, INGESTION_COLUMNS, [_ingestion_row(
        records, ingestion_id=ingestion_id, ingestion_route=ingestion_route,
        research_object=research_object, market_scope=market_scope, policy=policy,
        source_id=source_id, retrieved_at=retrieved_at, ledgered=bool(ledger_rows),
        dataset_location=dataset_location, row_count=row_count,
        must_refresh_if=must_refresh_if,
    )])

    return {
        "manifest": manifest_path, "evidence_log": evidence_path,
        "ingestion_log": ingestion_path,
        "calculation_ledger": ledger_path if ledger_rows else None,
        "series": series_path,
        "n_records": len(records), "n_ledgered": len(ledger_rows),
        "n_series_rows": len(series["rows"]) if series else 0,
    }


def _record_field_coverage(records: list[CanonicalRecord]) -> list[dict]:
    return [
        {"field": r.metric, "definition": r.provenance.get("tag", r.metric),
         "unit": r.unit, "currency": r.currency or "not_applicable",
         "period": r.period, "canonical_family": r.family}
        for r in records
    ]


def _series_field_coverage(series: dict, sample: CanonicalRecord) -> list[dict]:
    cur = sample.currency or "USD"
    units = {"date": "date", "volume": "shares"}
    cov = []
    for col in series["columns"]:
        unit = units.get(col, cur)
        cov.append({"field": col, "definition": f"{col} ({sample.family})",
                    "unit": unit, "currency": cur if unit == cur else "not_applicable",
                    "period": "series", "canonical_family": sample.family})
    return cov


def _evidence_row(r: CanonicalRecord, policy, used_by_agent, used_by_skill) -> dict:
    cat = r.posture.evidence_category
    verification = "verified" if cat in {"reported_fact", "market_pricing", "verified_fact"} else "unverified"
    if r.derived:
        # ledger carries the reproducibility; the row points to its ledger via source_id.
        ev_source_id = _calc_id(r)
        notes = f"Formula: {r.formula}" if r.formula else "Formula: derived"
        upstream = r.upstream_sources or r.posture.source_id
    else:
        ev_source_id = r.posture.source_id
        notes = _provenance_note(r)
        upstream = r.upstream_sources or "not_applicable"
    return {
        "source_id": ev_source_id,
        "claim_area": r.metric,
        "claim_type": r.posture.claim_type,
        "claim_text": r.claim_text,
        "source_speaker": "mira_calc" if r.derived else policy["speaker"],
        "verification_status": verification,
        "authority_level": r.posture.authority_level,
        "source_date": r.source_date,
        "as_of_date": r.as_of_date,
        "url_or_path": r.url_or_path,
        "used_by_agent": used_by_agent,
        "used_by_skill": used_by_skill,
        "confidence": r.confidence if r.confidence != "medium" else policy["confidence"],
        "upstream_sources": upstream,
        "notes": notes,
        "evidence_category": cat,
        "freshness_status": r.freshness_status if r.freshness_status != "current" else policy["freshness_status"],
        "conflict_status": "not_checked",
        "treatment": "use_normally",
        "readiness_impact": policy["readiness_impact"],
        "source_language": "en",
        "translation_basis": "not_translated",
    }


def _calc_id(r: CanonicalRecord) -> str:
    # research_object is part of the id: a multi-object bundle (e.g. a screen)
    # must not collide two tickers' identical metric/period into one ledger ref.
    return f"mira_calc__{r.research_object}__{r.metric}__{r.period}".lower().replace(" ", "_")


def _ledger_row(r: CanonicalRecord) -> dict:
    ev_source_id = _calc_id(r)
    return {
        "calculation_id": ev_source_id,
        "research_object": r.research_object,
        "question": f"What is {r.research_object} {r.metric} ({r.period})?",
        "metric": r.metric,
        "formula": r.formula or "derived",
        "input_sources": r.upstream_sources or r.posture.source_id,
        "period": r.period,
        "unit": r.unit,
        "result": r.value,
        "cross_check": r.cross_check or "single_source",
        "tool_used": "tools/mira_data",
        "verification_status": "modeled",
        "limitations": "Derived by Mira; inputs are delayed/period data — verify before durable use.",
        "evidence_log_ref": ev_source_id,
    }


def _ingestion_row(records, *, ingestion_id, ingestion_route, research_object,
                   market_scope, policy, source_id, retrieved_at, ledgered,
                   dataset_location, row_count, must_refresh_if) -> dict:
    families = sorted({r.family for r in records})
    metrics = ";".join(sorted({r.metric for r in records}))
    p0 = records[0].posture
    return {
        "ingestion_id": ingestion_id, "ingestion_route": ingestion_route,
        "research_object": research_object, "market_scope": market_scope,
        "provider_or_submitter": policy["provider"], "source_id": source_id,
        "source_class": p0.source_class, "access_method": p0.access_method,
        "acquisition_mode": p0.acquisition_mode, "license_scope": policy["license_scope"],
        "storage_scope": policy["storage_scope"],
        "redistribution_allowed": policy["redistribution_allowed"],
        "received_at": retrieved_at, "source_date": records[0].source_date,
        "as_of_date": records[0].as_of_date, "retrieved_at": retrieved_at,
        "dataset_location": dataset_location, "field_coverage": metrics,
        "row_count": row_count, "quality_status": "ok",
        "evidence_log_mapping": ";".join(f"{f}->{p0.claim_type}/{p0.evidence_category}" for f in families),
        "calculation_ledger_required": "yes" if ledgered else "no",
        "readiness_impact": policy["readiness_impact"],
        "must_refresh_if": must_refresh_if or "new filing/observation supersedes period",
        "notes": "Emitted by tools/mira_data; on-demand read, not a standing subscription.",
    }


def _write_manifest(path, *, records, ingestion_id, ingestion_route, research_object,
                    market_scope, endpoint, params, policy, retrieved_at, ledgered,
                    must_refresh_if, dataset_location, row_count, field_coverage) -> None:
    p0 = records[0].posture
    manifest = {
        "manifest_version": 1,
        "ingestion_id": ingestion_id,
        "ingestion_route": ingestion_route,
        "research_object": research_object,
        "market_scope": market_scope,
        "prepared_at": retrieved_at,
        "prepared_by": "Mira",
        "provider_or_submitter": policy["provider"],
        "source_id": p0.source_id,
        "source_class": p0.source_class,
        "authority_level": p0.authority_level,
        "access_method": p0.access_method,
        "acquisition_mode": p0.acquisition_mode,
        "license_scope": policy["license_scope"],
        "storage_scope": policy["storage_scope"],
        "redistribution_allowed": policy["redistribution_allowed"],
        "source_date": records[0].source_date,
        "as_of_date": records[0].as_of_date,
        "retrieved_at": retrieved_at,
        "dataset_location": dataset_location,
        "query": {"endpoint_or_file": endpoint, "parameters": params,
                  "coverage": f"{row_count} rows / {len(records)} claims for {research_object}"},
        "field_coverage": field_coverage,
        "transformations": [
            {"step": "select_and_normalize",
             "description": "Adapter selected period-correct observations and mapped vendor fields to the canonical family.",
             "upstream_fields": ["provider_fields"], "output_fields": ["value"]}
        ],
        "quality_checks": {
            "row_count": row_count,
            "missing_field_summary": "none",
            "conflict_status": "not_checked",
            "known_failure_modes": ["issuer tag drift", "restatements", "delayed aggregator data"],
        },
        "evidence_log_mapping": [
            {"claim_area": r.metric, "claim_type": p0.claim_type,
             "evidence_category": p0.evidence_category,
             "readiness_impact": policy["readiness_impact"]}
            for r in records
        ],
        "calculation_ledger_required": "yes" if ledgered else "no",
        "readiness_impact": policy["readiness_impact"],
        "must_refresh_if": must_refresh_if or "new filing/observation supersedes period",
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False, default=str)
        fh.write("\n")


def _provenance_note(r: CanonicalRecord) -> str:
    p = r.provenance
    bits = [f"{k}={p[k]}" for k in ("tag", "form", "fy", "fp", "accn") if p.get(k)]
    return "; ".join(bits) if bits else "reported metric"


def _append_csv(path: str, columns: list[str], rows: Iterable[dict]) -> None:
    exists = os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        if not exists:
            writer.writeheader()
        for row in rows:
            writer.writerow(row)
