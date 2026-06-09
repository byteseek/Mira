#!/usr/bin/env python3
"""Migrate Mira evidence-log.csv files from v1 to v1.1.

The migration appends evidence posture fields using conservative defaults based
on existing claim classification. It does not overwrite existing v1.1 files.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


V1_COLUMNS = [
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

POSTURE_COLUMNS = [
    "evidence_category",
    "freshness_status",
    "conflict_status",
    "treatment",
    "readiness_impact",
]

V1_1_COLUMNS = V1_COLUMNS + POSTURE_COLUMNS


def lower(row: dict[str, str], field: str) -> str:
    return row.get(field, "").strip().lower()


def infer_evidence_category(row: dict[str, str]) -> str:
    claim_type = lower(row, "claim_type")
    verification = lower(row, "verification_status")
    notes = lower(row, "notes")

    if "stale" in notes:
        return "stale"
    if "contradict" in notes:
        return "contradicted"
    if claim_type in {"rumor_signal", "sentiment"}:
        return "weak_signal"
    if claim_type == "market_pricing":
        return "market_pricing"
    if claim_type == "guidance":
        return "management_guidance"
    if claim_type in {"company_claim", "target", "commitment"}:
        return "company_statement"
    if claim_type == "fact" and verification == "verified":
        return "verified_fact"
    if claim_type in {"fact", "reported_metric"}:
        return "reported_fact"
    if claim_type in {"assumption", "forecast"}:
        return "assumption"
    if claim_type == "derived_calculation":
        return "estimate"
    if claim_type in {"interpretation", "opinion"}:
        return "inference"
    return "unknown"


def infer_freshness_status(row: dict[str, str], evidence_category: str) -> str:
    notes = lower(row, "notes")
    claim_type = lower(row, "claim_type")

    if evidence_category == "stale" or "stale" in notes:
        return "stale"
    if claim_type == "rumor_signal":
        return "preliminary"
    if not row.get("source_date", "").strip() or not row.get("as_of_date", "").strip():
        return "unknown"
    return "acceptable_for_period"


def infer_conflict_status(row: dict[str, str], evidence_category: str) -> str:
    notes = lower(row, "notes")
    claim_type = lower(row, "claim_type")

    if evidence_category == "contradicted" or "contradict" in notes:
        return "contradicted"
    if "conflict" in notes:
        return "unresolved"
    if claim_type in {"company_claim", "rumor_signal", "opinion", "interpretation"}:
        return "not_checked"
    return "none"


def infer_treatment(row: dict[str, str], evidence_category: str) -> str:
    claim_type = lower(row, "claim_type")
    notes = lower(row, "notes")

    if evidence_category in {"stale", "contradicted", "unknown"}:
        return "source_gap"
    if "source gap" in notes or "source_gap" in notes:
        return "source_gap"
    if claim_type in {"rumor_signal", "sentiment"}:
        return "monitor"
    if claim_type == "market_pricing":
        return "monitor"
    if claim_type in {"company_claim", "guidance", "target", "commitment", "opinion"}:
        return "attribute"
    if claim_type in {"assumption", "forecast", "interpretation", "derived_calculation"}:
        return "sensitize"
    return "use_normally"


def infer_readiness_impact(row: dict[str, str], evidence_category: str) -> str:
    claim_type = lower(row, "claim_type")
    authority = row.get("authority_level", "").strip()
    confidence = lower(row, "confidence")
    notes = lower(row, "notes")

    if evidence_category in {"stale", "contradicted"}:
        return "blocks_actionability"
    if evidence_category in {"weak_signal", "unknown"} or claim_type == "rumor_signal":
        return "monitoring_only"
    if "source gap" in notes or "source_gap" in notes:
        return "blocks_actionability"
    if claim_type == "market_pricing":
        return "supports_working_view"
    if evidence_category in {"verified_fact", "reported_fact"} and authority in {"L1", "L2"} and confidence == "high":
        return "supports_durable_conclusion"
    return "supports_working_view"


def infer_posture(row: dict[str, str]) -> dict[str, str]:
    evidence_category = infer_evidence_category(row)
    return {
        "evidence_category": evidence_category,
        "freshness_status": infer_freshness_status(row, evidence_category),
        "conflict_status": infer_conflict_status(row, evidence_category),
        "treatment": infer_treatment(row, evidence_category),
        "readiness_impact": infer_readiness_impact(row, evidence_category),
    }


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], [dict(row) for row in reader]


def migrate_file(path: Path, dry_run: bool) -> str:
    header, rows = read_csv(path)
    if header == V1_1_COLUMNS:
        return "already_v1_1"
    if header != V1_COLUMNS:
        return "skipped_non_v1"

    migrated_rows = []
    for row in rows:
        migrated = {column: row.get(column, "") for column in V1_COLUMNS}
        migrated.update(infer_posture(row))
        migrated_rows.append(migrated)

    if not dry_run:
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=V1_1_COLUMNS)
            writer.writeheader()
            writer.writerows(migrated_rows)
    return f"migrated_rows={len(migrated_rows)}"


def discover(root: Path) -> list[Path]:
    return [
        path
        for path in sorted(root.glob("**/evidence-log.csv"))
        if ".git" not in path.parts and "templates" not in path.parts
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="specific evidence-log.csv files to migrate")
    parser.add_argument("--root", type=Path, default=Path("."), help="repository root for --all")
    parser.add_argument("--all", action="store_true", help="migrate all non-template evidence logs under root")
    parser.add_argument("--dry-run", action="store_true", help="print planned migrations without writing files")
    args = parser.parse_args()

    if args.all:
        paths = discover(args.root)
    else:
        paths = args.paths

    if not paths:
        parser.error("provide paths or --all")

    for path in paths:
        print(f"{path}: {migrate_file(path, args.dry_run)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
