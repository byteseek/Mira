#!/usr/bin/env python3
"""Validate Mira repository readiness and research discipline.

Default mode is strict and exits non-zero on errors. Use --report-only to
surface current legacy drift without failing the run.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


REQUIRED_ROOT_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "DATA_POLICY.md",
    ".gitignore",
]

DATE_MARKERS = (
    "research_cutoff_date",
    "analysis_cutoff_date",
    "case_date",
    "release_date",
    "as_of",
)
REFRESH_MARKERS = (
    "stale_after",
    "must_refresh_if",
    "next refresh",
    "refresh after",
    "refresh policy",
    "refresh triggers",
)
DISCLAIMER_MARKERS = (
    "not_investment_advice",
    "not investment advice",
    "does not constitute investment advice",
    "不构成投资建议",
)

CANONICAL_EVIDENCE_COLUMNS_V1 = [
    "source_id",
    "claim_area",
    "claim_type",
    "claim_text",
    "source_speaker",
    "verification_status",
    "authority_level",
    "source_date",
    "as_of_date",
    "url_or_path",
    "used_by_agent",
    "used_by_skill",
    "confidence",
    "upstream_sources",
    "notes",
]

EVIDENCE_POSTURE_COLUMNS = [
    "evidence_category",
    "freshness_status",
    "conflict_status",
    "treatment",
    "readiness_impact",
]

CANONICAL_EVIDENCE_COLUMNS = CANONICAL_EVIDENCE_COLUMNS_V1 + EVIDENCE_POSTURE_COLUMNS

EVIDENCE_LANGUAGE_COLUMNS = [
    "source_language",
    "translation_basis",
]

# v1.2 appends the two i18n columns. v1 / v1.1 headers stay tolerated.
CANONICAL_EVIDENCE_COLUMNS_V1_2 = CANONICAL_EVIDENCE_COLUMNS + EVIDENCE_LANGUAGE_COLUMNS

TRANSLATION_BASES = {
    "not_translated",
    "mira_translation",
    "provider_translation",
    "official_translation",
    "bilingual_source",
    "not_applicable",
}

# Only judgment-bearing claims must retain a verbatim original excerpt when
# translated (management wording is itself the signal). Background/aggregated
# claims may carry just a translated summary — matches the rule documented in
# data/evidence-log-schema.md, so legitimate background translations don't WARN.
JUDGMENT_BEARING_CLAIM_TYPES = {
    "guidance",
    "company_claim",
    "commitment",
    "target",
}

CLAIM_TYPES = {
    "fact",
    "reported_metric",
    "company_claim",
    "guidance",
    "target",
    "commitment",
    "forecast",
    "assumption",
    "interpretation",
    "opinion",
    "market_pricing",
    "sentiment",
    "rumor_signal",
    "derived_calculation",
}

VERIFICATION_STATUSES = {
    "verified",
    "disclosed",
    "claimed",
    "estimated",
    "modeled",
    "unverified",
    "contradicted",
}

AUTHORITY_LEVELS = {"L1", "L2", "L3", "L4", "L5", "L6"}
CONFIDENCE_LEVELS = {"high", "medium", "low"}
EVIDENCE_CATEGORIES = {
    "verified_fact",
    "reported_fact",
    "company_statement",
    "management_guidance",
    "market_pricing",
    "assumption",
    "inference",
    "estimate",
    "weak_signal",
    "stale",
    "contradicted",
    "unknown",
}
FRESHNESS_STATUSES = {
    "current",
    "acceptable_for_period",
    "preliminary",
    "stale",
    "unknown",
}
CONFLICT_STATUSES = {"none", "unresolved", "contradicted", "not_checked"}
EVIDENCE_TREATMENTS = {
    "use_normally",
    "attribute",
    "sensitize",
    "haircut",
    "source_gap",
    "monitor",
    "exclude",
    "open_item",
}
READINESS_IMPACTS = {
    "supports_durable_conclusion",
    "supports_working_view",
    "monitoring_only",
    "blocks_actionability",
    "blocks_publication",
    "not_material",
}
READINESS_LEVELS = {
    "draft",
    "working_view",
    "research_ready",
    "actionable_with_caveats",
    "watch_only",
    "not_actionable",
    "needs_refresh",
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_IN_TEXT_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
STALE_AFTER_RE = re.compile(r"stale_after:\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
FIELD_RE = re.compile(r"^-\s*(state|research_action):\s*(.+?)\s*$")
ROUTING_PROMPT_RE = re.compile(r"^Prompt:\s*`(.+?)`\s*$")
ROUTING_FIELD_RE = re.compile(r"^-\s*`([^`]+)`:\s*(.+?)\s*$")
ROUTING_BASIS_RE = re.compile(r"^-\s*routing_basis:\s*(.+?)\s*$")
LOCAL_ABSOLUTE_PATH_RE = re.compile(
    r"(/" r"Users/[^)\s,]+|/" r"private/(?:tmp|var)/[^)\s,]+)"
)

THESIS_STATES = {
    "draft",
    "active",
    "watch",
    "upgrade_watch",
    "downgrade_watch",
    "narrative_watch",
    "stale",
    "retired",
}

RESEARCH_ACTIONS = {
    "watch_only",
    "upgrade_watch",
    "downgrade_watch",
    "add_to_research_queue",
    "reduce_research_priority",
    "hedge_context",
    "event_setup",
    "post_event_follow_through",
    "valuation_reset_watch",
    "risk_reduction_context",
    "needs_refresh",
    "no_action",
    "retire_thesis",
}

SETUP_TYPES = {
    "watch_only",
    "upgrade_watch",
    "event_setup",
    "post_event_follow_through",
    "valuation_reset_watch",
    "risk_reduction_context",
    "needs_refresh",
    "no_action",
}

POSITION_SIZING = {
    "not_applicable",
    "watchlist_only",
    "small_if_confirmed",
    "normal_only_after_confirmation",
    "reduce_risk_context",
}

SOURCE_RECORD_COLUMNS = {
    "source_name",
    "source_type",
    "source_group",
    "content_mode",
    "credibility_level",
    "content_type",
    "research_role",
    "market_scope",
    "access_method",
    "acquisition_mode",
    "update_frequency",
    "latency_class",
    "as_of_date_required",
    "usable_for",
    "last_checked_date",
}

SOURCE_CLASSES = {
    "issuer_primary_disclosure",
    "regulatory_and_exchange",
    "official_macro_and_industry",
    "market_price_and_trading",
    "aggregated_financial_data",
    "consensus_and_estimates",
    "sellside_and_expert_research",
    "professional_media",
    "industry_and_supply_chain_signal",
    "social_and_community_signal",
    "local_user_material",
    "mira_derived_analysis",
}

SOURCE_CLASS_MAP_COLUMNS = [
    "source_id",
    "source_class",
    "classification_basis",
    "review_status",
    "notes",
]

SOURCE_REVIEW_STATUSES = {"reviewed", "needs_review", "deprecated"}

SOURCE_COVERAGE_MATRIX_COLUMNS = [
    "workflow",
    "required_inputs",
    "minimum_coverage",
    "preferred_inputs",
    "source_gap_action",
    "refresh_rule",
    "notes",
]

# Routing controlled vocabulary lives in schemas/vocab.json (single source of
# truth, also $ref'd by schemas/routing.schema.json). These sets are BUILT from
# it — do not re-hardcode the values here. INVARIANT: each routing enum lives in
# vocab.json only. Evidence/source/readiness/claim enums above stay hardcoded
# until a later vocab migration (round-1 scope is routing-only).
SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schemas"
_VOCAB = json.loads((SCHEMA_DIR / "vocab.json").read_text(encoding="utf-8"))


def _vocab_set(key: str) -> set[str]:
    return set(_VOCAB[key]["enum"])


INTERACTION_MODES = _vocab_set("interaction_mode")
DECISION_PRESSURES = _vocab_set("decision_pressure")
FRAMING_RISKS = _vocab_set("framing_risk")
DISCONFIRMATION_REQUIRED = _vocab_set("disconfirmation_required")
DEPTH_MODES = _vocab_set("depth_mode")
QUANT_DEPENDENCIES = _vocab_set("quant_dependency")
CALCULATION_GATES = _vocab_set("calculation_gate")
INFORMATION_VALUES = _vocab_set("information_value")
KNOWABILITY_STATUSES = _vocab_set("knowability_status")
SCOPE_CONFIRMATION_REQUIRED = _vocab_set("scope_confirmation_required")

ROUTING_EXAMPLE_TOKEN_FIELDS = {
    "interaction_mode": INTERACTION_MODES,
    "decision_pressure": DECISION_PRESSURES,
    "framing_risk": FRAMING_RISKS,
    "disconfirmation_required": DISCONFIRMATION_REQUIRED,
    "depth_mode": DEPTH_MODES,
    "quant_dependency": QUANT_DEPENDENCIES,
    "calculation_gate": CALCULATION_GATES,
    "information_value": INFORMATION_VALUES,
    "knowability_status": KNOWABILITY_STATUSES,
    "scope_confirmation_required": SCOPE_CONFIRMATION_REQUIRED,
}

ROUTING_EXAMPLE_EXPECTATIONS = {
    "Mira, NVDA 的预期差在哪？": {
        "interaction_mode": "routed_research",
        "task_mode": "thesis_system_update",
        "research_object": "single_equity",
        "selected_lenses": "variant-perception",
        "decision_pressure": "none",
        "framing_risk": "none",
        "disconfirmation_required": "no",
    },
    "Mira, NVDA 预期差兑现了，现在还能不能加？": {
        "interaction_mode": "decision_support",
        "task_mode": "thesis_system_update",
        "decision_pressure": "medium",
        "framing_risk": "position_defense",
        "disconfirmation_required": "yes",
    },
    "Mira, 看一下 AAPL 方向就行": {
        "interaction_mode": "quick_answer",
        "depth_mode": "quick_map",
        "user_visible_routing_card": "一行假设条",
    },
    "Mira, 一句话告诉我 CRWV 现在贵不贵": {
        "interaction_mode": "quick_answer",
        "depth_mode": "deep_dive",
        "quant_dependency": "high",
        "calculation_gate": "required",
    },
    "Mira, 下个月 CPI 会不会超预期？": {
        "interaction_mode": "quick_answer",
        "information_value": "low",
        "knowability_status": "unknowable_now",
    },
    "Mira, 看 NVDA 这次财报，顺便对比 AMD，这俩我都重仓了": {
        "primary_intent": "NVDA earnings event",
        "secondary_intents": "[AMD peer / industry compare, position review of both]",
        "execution_order": "earnings → peer compare → position review",
        "scope_confirmation_required": "yes",
        "decision_pressure": "low",
    },
}

RESEARCH_PACKAGE_MANIFEST_REQUIRED_FIELDS = [
    "manifest_version",
    "case_id",
    "research_object",
    "market_scope",
    "time_boundary",
    "research_cutoff_date",
    "package_type",
    "readiness_level",
    "readiness_basis",
    "blocking_gaps",
    "hero_artifacts",
    "support_artifacts",
    "source_scope",
    "evidence_log_status",
    "quant_gate_status",
    "stale_after",
    "must_refresh_if",
]


@dataclass
class Issue:
    severity: str
    path: Path
    line: int
    message: str

    def render(self) -> str:
        loc = f"{self.path}:{self.line}" if self.line else str(self.path)
        return f"{self.severity}: {loc}: {self.message}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_any(text: str, markers: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in markers)


def is_template(path: Path) -> bool:
    return "templates" in path.parts


def normalize_token(value: str) -> str:
    return value.strip().strip("`").strip()


def is_placeholder(value: str) -> bool:
    stripped = value.strip()
    return stripped.startswith("{{") and stripped.endswith("}}")


def is_legacy_evidence_schema(path: Path) -> bool:
    """Allow archived historical cases to keep old evidence schema explicitly."""
    readme = path.parent / "README.md"
    if not readme.exists():
        return False
    return "legacy_evidence_schema: true" in read_text(readme).lower()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]], list[Issue]]:
    issues: list[Issue] = []
    try:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames or []
            rows = [dict(row) for row in reader]
    except Exception as exc:  # pragma: no cover - diagnostic path
        issues.append(Issue("ERROR", path, 0, f"could not read CSV: {exc}"))
        return [], [], issues

    if not header:
        issues.append(Issue("ERROR", path, 1, "missing CSV header"))
    return header, rows, issues


def validate_evidence_log(path: Path) -> list[Issue]:
    if is_legacy_evidence_schema(path):
        return [
            Issue(
                "WARN",
                path,
                1,
                "legacy_evidence_schema=true; canonical claim-level evidence validation skipped",
            )
        ]

    header, rows, issues = read_csv(path)
    if not header:
        return issues

    header_set = set(header)
    is_v1 = header == CANONICAL_EVIDENCE_COLUMNS_V1
    is_v1_1 = header == CANONICAL_EVIDENCE_COLUMNS
    is_v1_2 = header == CANONICAL_EVIDENCE_COLUMNS_V1_2
    has_posture = is_v1_1 or is_v1_2
    if not (is_v1 or is_v1_1 or is_v1_2):
        missing = [c for c in CANONICAL_EVIDENCE_COLUMNS_V1_2 if c not in header_set]
        extra = [c for c in header if c not in CANONICAL_EVIDENCE_COLUMNS_V1_2]
        if SOURCE_RECORD_COLUMNS & header_set:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    1,
                    "evidence-log.csv appears to use source-record schema; use claim-level canonical evidence schema",
                )
            )
        issues.append(
            Issue(
                "ERROR",
                path,
                1,
                f"non-canonical evidence-log header; missing={missing}; extra={extra}",
            )
        )
        return issues

    if is_template(path):
        return issues

    for i, row in enumerate(rows, start=2):
        if is_v1_2:
            required_fields = CANONICAL_EVIDENCE_COLUMNS_V1_2
        elif is_v1_1:
            required_fields = CANONICAL_EVIDENCE_COLUMNS
        else:
            required_fields = CANONICAL_EVIDENCE_COLUMNS_V1
        for field in required_fields:
            if not (row.get(field) or "").strip():
                issues.append(Issue("ERROR", path, i, f"missing required field `{field}`"))

        claim_type = row.get("claim_type", "").strip()
        if claim_type and claim_type not in CLAIM_TYPES:
            issues.append(Issue("ERROR", path, i, f"invalid claim_type `{claim_type}`"))

        verification_status = row.get("verification_status", "").strip()
        if verification_status and verification_status not in VERIFICATION_STATUSES:
            issues.append(
                Issue("ERROR", path, i, f"invalid verification_status `{verification_status}`")
            )

        authority_level = row.get("authority_level", "").strip()
        if authority_level and authority_level not in AUTHORITY_LEVELS:
            issues.append(Issue("ERROR", path, i, f"invalid authority_level `{authority_level}`"))

        confidence = row.get("confidence", "").strip()
        if confidence and confidence not in CONFIDENCE_LEVELS:
            issues.append(Issue("ERROR", path, i, f"invalid confidence `{confidence}`"))

        evidence_category = row.get("evidence_category", "").strip()
        freshness_status = row.get("freshness_status", "").strip()
        conflict_status = row.get("conflict_status", "").strip()
        treatment = row.get("treatment", "").strip()
        readiness_impact = row.get("readiness_impact", "").strip()

        if is_v1_2:
            translation_basis = row.get("translation_basis", "").strip()
            if translation_basis and translation_basis not in TRANSLATION_BASES:
                issues.append(Issue("ERROR", path, i, f"invalid translation_basis `{translation_basis}`"))
            # Translation provenance: a judgment-bearing translated claim must keep
            # the verbatim original snippet (background claims are exempt).
            if (
                claim_type in JUDGMENT_BEARING_CLAIM_TYPES
                and translation_basis in {"mira_translation", "provider_translation"}
                and "original_excerpt" not in row.get("notes", "")
            ):
                issues.append(
                    Issue(
                        "WARN",
                        path,
                        i,
                        "translated claim should keep `original_excerpt=` in notes (translation provenance)",
                    )
                )

        if has_posture:
            if evidence_category and evidence_category not in EVIDENCE_CATEGORIES:
                issues.append(
                    Issue("ERROR", path, i, f"invalid evidence_category `{evidence_category}`")
                )
            if freshness_status and freshness_status not in FRESHNESS_STATUSES:
                issues.append(
                    Issue("ERROR", path, i, f"invalid freshness_status `{freshness_status}`")
                )
            if conflict_status and conflict_status not in CONFLICT_STATUSES:
                issues.append(
                    Issue("ERROR", path, i, f"invalid conflict_status `{conflict_status}`")
                )
            if treatment and treatment not in EVIDENCE_TREATMENTS:
                issues.append(Issue("ERROR", path, i, f"invalid treatment `{treatment}`"))
            if readiness_impact and readiness_impact not in READINESS_IMPACTS:
                issues.append(
                    Issue("ERROR", path, i, f"invalid readiness_impact `{readiness_impact}`")
                )

        for field in ("source_date", "as_of_date"):
            value = row.get(field, "").strip()
            if value and not DATE_RE.match(value):
                issues.append(Issue("ERROR", path, i, f"`{field}` must be YYYY-MM-DD"))

        upstream = row.get("upstream_sources", "").strip()
        if (claim_type == "derived_calculation" or authority_level == "L6") and upstream in {
            "",
            "not_applicable",
            "na",
            "n/a",
        }:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    i,
                    "derived_calculation or L6 claim requires upstream_sources",
                )
            )

        if claim_type == "rumor_signal" and confidence == "high":
            issues.append(Issue("ERROR", path, i, "rumor_signal cannot have high confidence"))

        if claim_type in {"sentiment", "opinion", "rumor_signal"} and verification_status == "verified":
            issues.append(
                Issue(
                    "WARN",
                    path,
                    i,
                    f"{claim_type} with verification_status=verified is usually a classification smell",
                )
            )

        if has_posture:
            if evidence_category == "verified_fact" and (
                verification_status == "unverified"
                or claim_type in {"assumption", "opinion", "sentiment", "rumor_signal"}
            ):
                issues.append(
                    Issue(
                        "ERROR",
                        path,
                        i,
                        "verified_fact posture conflicts with weak/unverified claim classification",
                    )
                )
            if evidence_category == "market_pricing" and claim_type != "market_pricing":
                issues.append(
                    Issue(
                        "WARN",
                        path,
                        i,
                        "evidence_category=market_pricing usually pairs with claim_type=market_pricing",
                    )
                )
            if readiness_impact == "supports_durable_conclusion" and evidence_category in {
                "unknown",
                "weak_signal",
                "stale",
                "contradicted",
            }:
                issues.append(
                    Issue(
                        "ERROR",
                        path,
                        i,
                        f"{evidence_category} cannot directly support a durable conclusion",
                    )
                )
            if freshness_status == "stale" and evidence_category not in {"stale", "unknown"}:
                issues.append(
                    Issue(
                        "WARN",
                        path,
                        i,
                        "freshness_status=stale should normally downgrade evidence_category",
                    )
                )
            if conflict_status in {"unresolved", "contradicted"} and evidence_category != "contradicted":
                issues.append(
                    Issue(
                        "WARN",
                        path,
                        i,
                        "unresolved or contradicted conflict_status should normally downgrade evidence_category",
                    )
                )

    if not rows:
        issues.append(Issue("ERROR", path, 1, "evidence-log.csv has no claim rows"))

    return issues


def validate_research_package_manifest(path: Path) -> list[Issue]:
    issues: list[Issue] = []
    try:
        data = json.loads(read_text(path))
    except Exception as exc:
        return [Issue("ERROR", path, 0, f"could not parse JSON manifest: {exc}")]

    for field in RESEARCH_PACKAGE_MANIFEST_REQUIRED_FIELDS:
        if field not in data:
            issues.append(Issue("ERROR", path, 0, f"missing manifest field `{field}`"))

    readiness = str(data.get("readiness_level", "")).strip()
    if readiness and not is_placeholder(readiness) and readiness not in READINESS_LEVELS:
        issues.append(Issue("ERROR", path, 0, f"invalid readiness_level `{readiness}`"))

    for field in ("research_cutoff_date", "stale_after"):
        value = str(data.get(field, "")).strip()
        if value and not is_placeholder(value) and not DATE_RE.match(value):
            issues.append(Issue("ERROR", path, 0, f"`{field}` must be YYYY-MM-DD"))

    for field in ("blocking_gaps", "hero_artifacts", "support_artifacts", "must_refresh_if"):
        if field in data and not isinstance(data.get(field), list):
            issues.append(Issue("ERROR", path, 0, f"`{field}` must be a list"))

    if not data.get("hero_artifacts"):
        issues.append(Issue("ERROR", path, 0, "manifest must name at least one hero artifact"))
    if not data.get("support_artifacts"):
        issues.append(Issue("ERROR", path, 0, "manifest must name support artifacts"))

    package_type = str(data.get("package_type", "")).strip()
    if package_type and package_type != "research_package":
        issues.append(Issue("WARN", path, 0, f"unexpected package_type `{package_type}`"))

    return issues


def validate_decision_log(path: Path) -> list[Issue]:
    if is_template(path):
        return []

    header, rows, issues = read_csv(path)
    if issues:
        return issues
    if "decision_type" not in header:
        issues.append(Issue("ERROR", path, 1, "decision-log.csv missing `decision_type` column"))
        return issues

    for i, row in enumerate(rows, start=2):
        decision_type = normalize_token(row.get("decision_type", ""))
        if decision_type and not is_placeholder(decision_type) and decision_type not in RESEARCH_ACTIONS:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    i,
                    f"invalid decision_type `{decision_type}`; use data/controlled-vocabulary.md",
                )
            )
    return issues


def validate_case_readme(case_dir: Path) -> list[Issue]:
    readme = case_dir / "README.md"
    if not readme.exists():
        return [Issue("ERROR", case_dir, 0, "missing README.md")]

    issues: list[Issue] = []
    text = read_text(readme)
    if not has_any(text, DATE_MARKERS):
        issues.append(Issue("ERROR", readme, 0, "missing cutoff/as-of metadata"))
    if not has_any(text, REFRESH_MARKERS):
        issues.append(Issue("ERROR", readme, 0, "missing refresh/staleness policy"))
    if not has_any(text, DISCLAIMER_MARKERS):
        issues.append(Issue("ERROR", readme, 0, "missing not-investment-advice disclaimer"))
    return issues


def validate_staleness(path: Path, as_of: date) -> list[Issue]:
    if not path.exists() or path.is_dir():
        return []

    issues: list[Issue] = []
    for i, line in enumerate(read_text(path).splitlines(), start=1):
        match = STALE_AFTER_RE.search(line)
        if not match:
            continue
        stale_after = date.fromisoformat(match.group(1))
        if stale_after < as_of:
            issues.append(
                Issue(
                    "WARN",
                    path,
                    i,
                    f"stale_after {stale_after.isoformat()} is before validation date {as_of.isoformat()}",
                )
            )
    return issues


def first_token_after_heading(lines: list[str], heading: str) -> tuple[int, str] | None:
    for i, line in enumerate(lines):
        if line.strip() != heading:
            continue
        for j in range(i + 1, len(lines)):
            candidate = lines[j].strip()
            if not candidate:
                continue
            if candidate.startswith("## "):
                return None
            return j + 1, normalize_token(candidate)
    return None


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def validate_markdown_vocabulary(path: Path) -> list[Issue]:
    if is_template(path) or path.name == "controlled-vocabulary.md":
        return []

    issues: list[Issue] = []
    lines = read_text(path).splitlines()
    for i, line in enumerate(lines, start=1):
        match = FIELD_RE.match(line.strip())
        if not match:
            continue
        field, raw_value = match.groups()
        value = normalize_token(raw_value)
        if is_placeholder(value):
            continue
        allowed = THESIS_STATES if field == "state" else RESEARCH_ACTIONS
        if value not in allowed:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    i,
                    f"invalid {field} `{value}`; use data/controlled-vocabulary.md",
                )
            )

    setup = first_token_after_heading(lines, "## Setup Type")
    if setup:
        line_no, value = setup
        if not is_placeholder(value) and value not in SETUP_TYPES:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    line_no,
                    f"invalid setup_type `{value}`; use data/controlled-vocabulary.md",
                )
            )

    sizing = first_token_after_heading(lines, "## Position Sizing Implication")
    if sizing:
        line_no, value = sizing
        if not is_placeholder(value) and value not in POSITION_SIZING:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    line_no,
                    f"invalid position_sizing_implication `{value}`; use data/controlled-vocabulary.md",
                )
            )
    return issues


def validate_no_local_absolute_paths(path: Path) -> list[Issue]:
    """Prevent local workstation paths from leaking into portable docs."""
    if path.is_dir() or ".git" in path.parts:
        return []
    if path.suffix.lower() not in {".md", ".csv", ".py"}:
        return []

    issues: list[Issue] = []
    for i, line in enumerate(read_text(path).splitlines(), start=1):
        match = LOCAL_ABSOLUTE_PATH_RE.search(line)
        if match:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    i,
                    f"local absolute path `{match.group(1)}`; use a repo-relative path",
                )
            )
    return issues


def validate_research_index(path: Path, as_of: date) -> list[Issue]:
    if not path.exists():
        return []

    issues: list[Issue] = []
    lines = read_text(path).splitlines()
    for i, line in enumerate(lines, start=1):
        if not line.startswith("| ") or "research_object" in line or line.startswith("| ---"):
            continue
        cells = split_markdown_row(line)
        if len(cells) < 8:
            continue
        research_object, state, _, _, stale_after, _, actionability, _ = cells[:8]
        state_token = normalize_token(state)
        if state_token not in THESIS_STATES:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    i,
                    f"{research_object} has invalid state `{state_token}`; use data/controlled-vocabulary.md",
                )
            )

        action_tokens = [
            normalize_token(token)
            for token in re.split(r"[/,;]", actionability)
            if normalize_token(token)
        ]
        allowed_actions = RESEARCH_ACTIONS | POSITION_SIZING
        for token in action_tokens:
            if token not in allowed_actions:
                issues.append(
                    Issue(
                        "ERROR",
                        path,
                        i,
                        f"{research_object} has invalid actionability token `{token}`; use data/controlled-vocabulary.md",
                    )
                )

        for date_match in DATE_IN_TEXT_RE.finditer(stale_after):
            stale_date = date.fromisoformat(date_match.group(1))
            if stale_date < as_of:
                issues.append(
                    Issue(
                        "WARN",
                        path,
                        i,
                        f"{research_object} index stale_after {stale_date.isoformat()} is before validation date {as_of.isoformat()}",
                    )
                )
    return issues


def validate_methodology_adoption(root: Path) -> list[Issue]:
    path = root / "memory" / "methodologies" / "adopted.md"
    if not path.exists():
        return []

    issues: list[Issue] = []
    lines = path.read_text().splitlines()
    current_method = None
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("- `") and stripped.endswith("`"):
            current_method = stripped.strip("- `")
        if stripped.startswith("based_on_cases:") and current_method:
            value = stripped.split(":", 1)[1].strip().lower()
            weak_markers = {"design iteration", "sample", "routed design iteration"}
            if any(marker in value for marker in weak_markers):
                issues.append(
                    Issue(
                        "WARN",
                        path,
                        i,
                        f"`{current_method}` adoption is based on design/sample rather than outcome-reviewed cases",
                    )
                )
    return issues


def validate_root_readiness(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for rel_path in REQUIRED_ROOT_FILES:
        if not (root / rel_path).exists():
            issues.append(Issue("ERROR", root / rel_path, 0, "missing required root file"))

    readme = root / "README.md"
    if readme.exists():
        readme_text = read_text(readme)
        if not has_any(readme_text, DISCLAIMER_MARKERS):
            issues.append(Issue("ERROR", readme, 0, "missing investment disclaimer"))
        if "Quickstart" not in readme_text:
            issues.append(Issue("ERROR", readme, 0, "missing Quickstart section"))
    return issues


def validate_source_class_map(root: Path) -> list[Issue]:
    registry_path = root / "data" / "source-registry.csv"
    map_path = root / "data" / "source-class-map.csv"
    issues: list[Issue] = []

    registry_header, registry_rows, registry_issues = read_csv(registry_path)
    map_header, map_rows, map_issues = read_csv(map_path)
    issues.extend(registry_issues)
    issues.extend(map_issues)
    if registry_issues or map_issues:
        return issues

    if "source_id" not in registry_header:
        issues.append(Issue("ERROR", registry_path, 1, "missing `source_id` column"))
        return issues

    if map_header != SOURCE_CLASS_MAP_COLUMNS:
        missing = [c for c in SOURCE_CLASS_MAP_COLUMNS if c not in set(map_header)]
        extra = [c for c in map_header if c not in SOURCE_CLASS_MAP_COLUMNS]
        issues.append(
            Issue(
                "ERROR",
                map_path,
                1,
                f"non-canonical source-class-map header; missing={missing}; extra={extra}",
            )
        )
        return issues

    registry_ids = [row.get("source_id", "").strip() for row in registry_rows]
    map_ids = [row.get("source_id", "").strip() for row in map_rows]
    registry_set = set(registry_ids)
    map_set = set(map_ids)

    duplicate_map_ids = sorted(source_id for source_id in map_set if map_ids.count(source_id) > 1)
    for source_id in duplicate_map_ids:
        issues.append(Issue("ERROR", map_path, 0, f"duplicate source_id `{source_id}`"))

    for source_id in sorted(registry_set - map_set):
        issues.append(Issue("ERROR", map_path, 0, f"missing source_class mapping for `{source_id}`"))

    for source_id in sorted(map_set - registry_set):
        issues.append(Issue("ERROR", map_path, 0, f"source_class mapping for unknown `{source_id}`"))

    for i, row in enumerate(map_rows, start=2):
        for field in SOURCE_CLASS_MAP_COLUMNS:
            if not (row.get(field) or "").strip():
                issues.append(Issue("ERROR", map_path, i, f"missing required field `{field}`"))

        source_class = row.get("source_class", "").strip()
        if source_class and source_class not in SOURCE_CLASSES:
            issues.append(Issue("ERROR", map_path, i, f"invalid source_class `{source_class}`"))

        review_status = row.get("review_status", "").strip()
        if review_status and review_status not in SOURCE_REVIEW_STATUSES:
            issues.append(Issue("ERROR", map_path, i, f"invalid review_status `{review_status}`"))

    return issues


def validate_source_coverage_matrix(root: Path) -> list[Issue]:
    path = root / "data" / "source-coverage-matrix.csv"
    header, rows, issues = read_csv(path)
    if issues:
        return issues

    if header != SOURCE_COVERAGE_MATRIX_COLUMNS:
        missing = [c for c in SOURCE_COVERAGE_MATRIX_COLUMNS if c not in set(header)]
        extra = [c for c in header if c not in SOURCE_COVERAGE_MATRIX_COLUMNS]
        issues.append(
            Issue(
                "ERROR",
                path,
                1,
                f"non-canonical source-coverage-matrix header; missing={missing}; extra={extra}",
            )
        )
        return issues

    if not rows:
        issues.append(Issue("ERROR", path, 1, "source-coverage-matrix.csv has no workflow rows"))
        return issues

    workflow_ids = [row.get("workflow", "").strip() for row in rows]
    duplicate_workflows = sorted(workflow for workflow in set(workflow_ids) if workflow_ids.count(workflow) > 1)
    for workflow in duplicate_workflows:
        issues.append(Issue("ERROR", path, 0, f"duplicate workflow `{workflow}`"))

    for i, row in enumerate(rows, start=2):
        for field in SOURCE_COVERAGE_MATRIX_COLUMNS:
            if not (row.get(field) or "").strip():
                issues.append(Issue("ERROR", path, i, f"missing required field `{field}`"))

    return issues


def routing_field_value(raw: str) -> str:
    """Normalize a routing example value while preserving free-text fields."""
    value = raw.strip()
    backticked = re.match(r"`([^`]+)`", value)
    if backticked:
        return backticked.group(1).strip()
    return value


def validate_routing_examples(root: Path) -> list[Issue]:
    path = root / "examples" / "routing-examples.md"
    if not path.exists():
        return [Issue("ERROR", path, 0, "missing routing examples fixture")]

    lines = read_text(path).splitlines()
    issues: list[Issue] = []
    text = "\n".join(lines)

    if "not_investment_advice: true" not in text:
        issues.append(Issue("ERROR", path, 1, "routing examples must state not_investment_advice: true"))

    examples: dict[str, dict[str, object]] = {}
    current_prompt: str | None = None
    for line_no, line in enumerate(lines, start=1):
        prompt_match = ROUTING_PROMPT_RE.match(line)
        if prompt_match:
            current_prompt = prompt_match.group(1)
            if current_prompt in examples:
                issues.append(Issue("ERROR", path, line_no, f"duplicate routing prompt `{current_prompt}`"))
            examples[current_prompt] = {"line": line_no, "fields": {}, "has_basis": False}
            continue

        if current_prompt is None:
            continue

        field_match = ROUTING_FIELD_RE.match(line)
        if field_match:
            field = field_match.group(1)
            value = routing_field_value(field_match.group(2))
            fields = examples[current_prompt]["fields"]
            assert isinstance(fields, dict)
            fields[field] = value
            allowed_values = ROUTING_EXAMPLE_TOKEN_FIELDS.get(field)
            if allowed_values is not None and value not in allowed_values:
                issues.append(Issue("ERROR", path, line_no, f"`{field}` has non-canonical token `{value}`"))
            continue

        if ROUTING_BASIS_RE.match(line):
            examples[current_prompt]["has_basis"] = True

    for prompt, expected_fields in ROUTING_EXAMPLE_EXPECTATIONS.items():
        example = examples.get(prompt)
        if example is None:
            issues.append(Issue("ERROR", path, 0, f"missing golden routing prompt `{prompt}`"))
            continue

        line_no = int(example["line"])
        fields = example["fields"]
        assert isinstance(fields, dict)
        if not example["has_basis"]:
            issues.append(Issue("ERROR", path, line_no, "routing example is missing routing_basis"))

        for field, expected_value in expected_fields.items():
            actual_value = fields.get(field)
            if actual_value is None:
                issues.append(Issue("ERROR", path, line_no, f"routing example missing `{field}`"))
            elif actual_value != expected_value:
                issues.append(
                    Issue(
                        "ERROR",
                        path,
                        line_no,
                        f"`{field}` expected `{expected_value}` but found `{actual_value}`",
                    )
                )

    for prompt, example in examples.items():
        if prompt not in ROUTING_EXAMPLE_EXPECTATIONS:
            issues.append(
                Issue(
                    "WARN",
                    path,
                    int(example["line"]),
                    "routing prompt is documented but not locked in ROUTING_EXAMPLE_EXPECTATIONS",
                )
            )

    return issues


def _doc_backtick_token(line: str) -> str | None:
    match = re.match(r"-\s*`([^`]+)`", line.strip())
    return match.group(1) if match else None


def validate_vocab_doc_consistency(root: Path) -> list[Issue]:
    """Bind controlled-vocabulary.md routing token lists to schemas/vocab.json.

    vocab.json is the single source for the routing token SET; the doc prose is
    human-only. Each `<!-- vocab:FIELD start --> ... <!-- vocab:FIELD end -->`
    region must enumerate exactly the vocab.json enum for that field, so the doc
    cannot drift from the machine vocabulary (no second hand-maintained token
    source).
    """
    doc = root / "data" / "controlled-vocabulary.md"
    if not doc.exists():
        return [Issue("ERROR", doc, 0, "missing data/controlled-vocabulary.md")]

    start_re = re.compile(r"<!--\s*vocab:([a-z_]+)\s+start")
    end_re = re.compile(r"<!--\s*vocab:([a-z_]+)\s+end")
    regions: dict[str, set[str]] = {}
    current: str | None = None
    for line in read_text(doc).splitlines():
        start = start_re.search(line)
        if start:
            current = start.group(1)
            regions.setdefault(current, set())
            continue
        if end_re.search(line):
            current = None
            continue
        if current is not None:
            token = _doc_backtick_token(line)
            if token:
                regions[current].add(token)

    issues: list[Issue] = []
    for field, fragment in _VOCAB.items():
        if not isinstance(fragment, dict) or "enum" not in fragment:
            continue
        expected = set(fragment["enum"])
        documented = regions.get(field)
        if documented is None:
            issues.append(
                Issue(
                    "ERROR",
                    doc,
                    0,
                    f"routing field `{field}` has no `<!-- vocab:{field} -->` token "
                    "list; schemas/vocab.json is the source",
                )
            )
            continue
        missing = sorted(expected - documented)
        extra = sorted(documented - expected)
        if missing:
            issues.append(Issue("ERROR", doc, 0, f"`{field}`: in vocab.json but undocumented: {missing}"))
        if extra:
            issues.append(Issue("ERROR", doc, 0, f"`{field}`: documented but not in vocab.json: {extra}"))
    return issues


# --- Routing card schema (stdlib subset checker) ---------------------------
# Implements only the JSON Schema subset that schemas/routing.schema.json uses:
# type, enum, const, required, properties, minLength, minItems, allOf, if/then,
# and $ref to schemas/vocab.json. No third-party dependency, so the repo stays
# clone-and-run. Staying inside this keyword subset keeps a standard JSON Schema
# engine a drop-in replacement later.

_SCHEMA_DOC_CACHE: dict[Path, dict] = {}


def _load_schema_doc(path: Path) -> dict:
    doc = _SCHEMA_DOC_CACHE.get(path)
    if doc is None:
        doc = json.loads(path.read_text(encoding="utf-8"))
        _SCHEMA_DOC_CACHE[path] = doc
    return doc


def _resolve_ref(ref: str) -> dict:
    file_part, _, fragment = ref.partition("#")
    node: object = _load_schema_doc(SCHEMA_DIR / file_part)
    for segment in fragment.split("/"):
        if segment:
            node = node[segment]  # type: ignore[index]
    return node  # type: ignore[return-value]


def schema_errors(instance: object, schema: dict) -> list[str]:
    """Return human-readable validation errors for the supported subset."""
    if "$ref" in schema:
        merged = {key: value for key, value in schema.items() if key != "$ref"}
        merged.update(_resolve_ref(schema["$ref"]))
        schema = merged

    errors: list[str] = []
    expected_type = schema.get("type")
    if expected_type == "object" and not isinstance(instance, dict):
        return ["expected an object"]
    if expected_type == "string" and not isinstance(instance, str):
        return ["expected a string"]
    if expected_type == "array" and not isinstance(instance, list):
        return ["expected an array"]

    if "const" in schema and instance != schema["const"]:
        errors.append(f"must equal {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{instance!r} is not one of {sorted(schema['enum'])}")
    if "minLength" in schema and isinstance(instance, str):
        if len(instance.strip()) < schema["minLength"]:
            errors.append("must not be empty")
    if "minItems" in schema and isinstance(instance, list):
        if len(instance) < schema["minItems"]:
            errors.append(f"needs at least {schema['minItems']} item(s)")

    if isinstance(instance, dict):
        for field_name in schema.get("required", []):
            value = instance.get(field_name)
            missing = (
                field_name not in instance
                or (isinstance(value, str) and not value.strip())
                or (isinstance(value, list) and not value)
            )
            if missing:
                errors.append(f"missing required field `{field_name}`")
        for field_name, subschema in schema.get("properties", {}).items():
            if field_name in instance:
                for message in schema_errors(instance[field_name], subschema):
                    errors.append(f"`{field_name}`: {message}")

    for subschema in schema.get("allOf", []):
        errors.extend(schema_errors(instance, subschema))

    if "if" in schema and not schema_errors(instance, schema["if"]):
        errors.extend(schema_errors(instance, schema["then"]))

    return errors


def validate_routing_json(path: Path) -> list[Issue]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [Issue("ERROR", path, 0, f"invalid routing.json: {exc}")]
    schema = _load_schema_doc(SCHEMA_DIR / "routing.schema.json")
    return [Issue("ERROR", path, 0, message) for message in schema_errors(data, schema)]


def load_routing_exempt(root: Path) -> set[str]:
    exempt_file = root / "cases" / "legacy-routing-exempt.txt"
    if not exempt_file.exists():
        return set()
    names: set[str] = set()
    for line in exempt_file.read_text(encoding="utf-8").splitlines():
        name = line.split("#", 1)[0].strip()
        if name:
            names.add(name)
    return names


def validate_case_routing(case_dir: Path, exempt: set[str]) -> list[Issue]:
    has_research = (case_dir / "investment-memo.md").exists() or (
        case_dir / "evidence-log.csv"
    ).exists()
    if not has_research or case_dir.name in exempt:
        return []
    if (case_dir / "routing.json").exists():
        return []
    return [
        Issue(
            "ERROR",
            case_dir,
            0,
            "case has investment-memo.md or evidence-log.csv but no routing.json; "
            "add routing.json per schemas/routing.schema.json, or list the case in "
            "cases/legacy-routing-exempt.txt",
        )
    ]


def validate_repo(root: Path, as_of: date) -> list[Issue]:
    issues = validate_root_readiness(root)
    issues.extend(validate_source_class_map(root))
    issues.extend(validate_source_coverage_matrix(root))
    issues.extend(validate_routing_examples(root))
    issues.extend(validate_vocab_doc_consistency(root))
    issues.extend(validate_localization_glossary(root))
    for path in sorted(root.glob("**/routing.json")):
        if ".git" in path.parts:
            continue
        issues.extend(validate_routing_json(path))
    for path in sorted(root.glob("**/evidence-log.csv")):
        if ".git" in path.parts:
            continue
        issues.extend(validate_evidence_log(path))
    for path in sorted(root.glob("**/decision-log.csv")):
        if ".git" in path.parts:
            continue
        issues.extend(validate_decision_log(path))
    for path in sorted(root.glob("**/research-package-manifest.json")):
        if ".git" in path.parts:
            continue
        issues.extend(validate_research_package_manifest(path))
    for path in sorted(root.glob("**/*.md")):
        if ".git" in path.parts:
            continue
        issues.extend(validate_no_local_absolute_paths(path))
        issues.extend(validate_staleness(path, as_of))
        issues.extend(validate_markdown_vocabulary(path))
    for path in sorted(root.glob("**/*.csv")):
        if ".git" in path.parts:
            continue
        issues.extend(validate_no_local_absolute_paths(path))
    for path in sorted(root.glob("**/*.py")):
        if ".git" in path.parts:
            continue
        issues.extend(validate_no_local_absolute_paths(path))
    issues.extend(validate_research_index(root / "memory" / "research" / "INDEX.md", as_of))
    cases_dir = root / "cases"
    if cases_dir.exists():
        routing_exempt = load_routing_exempt(root)
        for case_dir in sorted(path for path in cases_dir.iterdir() if path.is_dir()):
            issues.extend(validate_case_readme(case_dir))
            issues.extend(validate_case_routing(case_dir, routing_exempt))
    issues.extend(validate_methodology_adoption(root))
    return issues


def validate_paths(paths: list[Path], as_of: date) -> list[Issue]:
    issues: list[Issue] = []
    for path in paths:
        if path.is_dir():
            evidence = path / "evidence-log.csv"
            if evidence.exists():
                issues.extend(validate_evidence_log(evidence))
            else:
                issues.append(Issue("ERROR", path, 0, "directory has no evidence-log.csv"))
            readme = path / "README.md"
            if readme.exists():
                issues.extend(validate_no_local_absolute_paths(readme))
                issues.extend(validate_case_readme(path))
                issues.extend(validate_staleness(readme, as_of))
            for md_path in sorted(path.glob("*.md")):
                if md_path != readme:
                    issues.extend(validate_no_local_absolute_paths(md_path))
                    issues.extend(validate_staleness(md_path, as_of))
                    issues.extend(validate_markdown_vocabulary(md_path))
            decision_log = path / "decision-log.csv"
            if decision_log.exists():
                issues.extend(validate_no_local_absolute_paths(decision_log))
                issues.extend(validate_decision_log(decision_log))
            manifest = path / "research-package-manifest.json"
            if manifest.exists():
                issues.extend(validate_research_package_manifest(manifest))
            routing = path / "routing.json"
            if routing.exists():
                issues.extend(validate_routing_json(routing))
            issues.extend(
                validate_case_routing(path, load_routing_exempt(path.parent.parent))
            )
        elif path.name == "routing.json":
            issues.extend(validate_routing_json(path))
        elif path.name == "evidence-log.csv":
            issues.extend(validate_no_local_absolute_paths(path))
            issues.extend(validate_evidence_log(path))
        elif path.name == "decision-log.csv":
            issues.extend(validate_no_local_absolute_paths(path))
            issues.extend(validate_decision_log(path))
        elif path.name == "research-package-manifest.json":
            issues.extend(validate_research_package_manifest(path))
        elif path.as_posix().endswith("examples/routing-examples.md"):
            issues.extend(validate_routing_examples(path.parent.parent))
        else:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    0,
                    "expected evidence-log.csv, decision-log.csv, research-package-manifest.json or case directory",
                )
            )
    return issues


def validate_localization_glossary(root: Path) -> list[Issue]:
    """Structure + anti-drift check for data/localization-glossary.csv.

    Each `kind=protocol_token` row's `canonical_token` must exist in a known
    token source (schemas/vocab.json routing enums, the hardcoded
    evidence/state/action enum sets, or the documented language field names), so
    the glossary cannot silently drift from the controlled vocabulary.
    """
    path = root / "data" / "localization-glossary.csv"
    if not path.exists():
        return []

    header, rows, issues = read_csv(path)
    if not header:
        return issues

    required_cols = {"key", "kind", "en", "canonical_token"}
    missing_cols = sorted(required_cols - set(header))
    if missing_cols:
        issues.append(Issue("ERROR", path, 1, f"glossary missing columns: {missing_cols}"))
        return issues

    valid_kinds = {"protocol_token", "field_label", "domain_term"}
    documented_field_tokens = {
        "output_language",
        "interaction_language",
        "evidence_languages",
        "source_language",
        "translation_basis",
    }
    known_tokens: set[str] = set(documented_field_tokens)
    for fragment in _VOCAB.values():
        if isinstance(fragment, dict) and "enum" in fragment:
            known_tokens.update(fragment["enum"])
    for enum_set in (
        THESIS_STATES,
        RESEARCH_ACTIONS,
        SETUP_TYPES,
        POSITION_SIZING,
        CLAIM_TYPES,
        VERIFICATION_STATUSES,
        AUTHORITY_LEVELS,
        CONFIDENCE_LEVELS,
        EVIDENCE_CATEGORIES,
        FRESHNESS_STATUSES,
        CONFLICT_STATUSES,
        EVIDENCE_TREATMENTS,
        READINESS_IMPACTS,
        READINESS_LEVELS,
        TRANSLATION_BASES,
    ):
        known_tokens.update(enum_set)

    seen_keys: set[str] = set()
    for i, row in enumerate(rows, start=2):
        key = (row.get("key") or "").strip()
        kind = (row.get("kind") or "").strip()
        if not key:
            issues.append(Issue("ERROR", path, i, "glossary row missing `key`"))
            continue
        if key in seen_keys:
            issues.append(Issue("ERROR", path, i, f"duplicate glossary key `{key}`"))
        seen_keys.add(key)
        if kind not in valid_kinds:
            issues.append(Issue("ERROR", path, i, f"invalid kind `{kind}`; use {sorted(valid_kinds)}"))
        if not (row.get("en") or "").strip():
            issues.append(Issue("ERROR", path, i, f"glossary `{key}` missing `en` display string"))
        if kind == "protocol_token":
            canonical = (row.get("canonical_token") or "").strip()
            if not canonical:
                issues.append(Issue("ERROR", path, i, f"protocol_token `{key}` missing `canonical_token`"))
            elif canonical not in known_tokens:
                issues.append(
                    Issue(
                        "ERROR",
                        path,
                        i,
                        f"protocol_token `{key}` canonical_token `{canonical}` not found in any "
                        "controlled vocabulary source (vocab.json, hardcoded enums, or documented field tokens)",
                    )
                )
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument(
        "paths",
        nargs="*",
        help="optional evidence-log.csv files or case directories to validate instead of full repo",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="print issues but exit 0; useful while migrating legacy cases",
    )
    parser.add_argument(
        "--as-of",
        default=date.today().isoformat(),
        help="validation date for stale_after checks, in YYYY-MM-DD format",
    )
    args = parser.parse_args()

    root = Path(args.root)
    as_of = date.fromisoformat(args.as_of)
    if args.paths:
        issues = validate_paths([root / path for path in args.paths], as_of)
    else:
        issues = validate_repo(root, as_of)
    errors = [issue for issue in issues if issue.severity == "ERROR"]
    warnings = [issue for issue in issues if issue.severity == "WARN"]

    for issue in issues:
        print(issue.render())

    print(f"summary: {len(errors)} errors, {len(warnings)} warnings")

    if args.report_only:
        return 0
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
