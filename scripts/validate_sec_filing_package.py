#!/usr/bin/env python3
"""Validate SEC supplement notes and SEC filing deep-dive packages."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

from validate_repo import validate_evidence_log as validate_canonical_evidence_log


SUPPLEMENT_COLUMNS = [
    "case_id",
    "company_name",
    "ticker",
    "cik",
    "checked_at",
    "route",
    "target_question",
    "sec_source_id",
    "source_class",
    "authority_level",
    "form_type",
    "filing_date",
    "report_period",
    "accession_number",
    "source_url",
    "section_or_exhibit",
    "metric_or_claim",
    "extraction_method",
    "provenance_fields",
    "confirms_or_conflicts",
    "active_case_update",
    "source_gap",
    "refresh_trigger",
    "notes",
]

METRIC_COLUMNS = [
    "metric_id",
    "company_name",
    "ticker",
    "cik",
    "accession_number",
    "form_type",
    "filing_date",
    "report_period",
    "statement_or_section",
    "metric_name",
    "value",
    "unit",
    "period_start",
    "period_end",
    "taxonomy",
    "tag",
    "frame",
    "source_method",
    "source_url",
    "section_or_exhibit",
    "extraction_status",
    "confidence",
    "confirms_or_conflicts",
    "comparison_source_id",
    "notes",
]

RISK_COLUMNS = [
    "risk_id",
    "company_name",
    "ticker",
    "cik",
    "accession_number",
    "form_type",
    "filing_date",
    "report_period",
    "section",
    "prior_source_id",
    "current_source_id",
    "risk_area",
    "delta_type",
    "current_language_summary",
    "prior_language_summary",
    "thesis_variable",
    "materiality",
    "verification_status",
    "confidence",
    "source_url",
    "notes",
]

ACCOUNTING_COLUMNS = [
    "check_id",
    "company_name",
    "ticker",
    "cik",
    "accession_number",
    "form_type",
    "filing_date",
    "report_period",
    "quality_area",
    "metric_or_section",
    "evidence_summary",
    "source_id",
    "source_url",
    "classification",
    "thesis_relevance",
    "source_gap",
    "confidence",
    "followup_required",
    "notes",
]

REQUIRED_PACKAGE_FILES = {
    "filing-metric-table.csv": METRIC_COLUMNS,
    "filing-risk-delta.csv": RISK_COLUMNS,
    "accounting-quality-check.csv": ACCOUNTING_COLUMNS,
    "evidence-log.csv": None,
    "filing-analysis.md": None,
}

CONFIDENCE_LEVELS = {"high", "medium", "low"}
AUTHORITY_LEVELS = {"L1", "L2", "L3", "L4", "L5", "L6"}
SUPPLEMENT_ROUTES = {"sec_supplement"}
SOURCE_GAP_VALUES = {"yes", "no", "partial"}
DELTA_TYPES = {"new", "expanded", "removed", "softened", "unchanged", "source_gap"}
IMPACT_VALUES = {"confirms", "corrects", "conflicts", "source_gap", "no_material_change"}


@dataclass
class Issue:
    severity: str
    path: Path
    line: int
    message: str

    def render(self) -> str:
        loc = f"{self.path}:{self.line}" if self.line else str(self.path)
        return f"{self.severity}: {loc}: {self.message}"


def is_placeholder(value: str) -> bool:
    stripped = value.strip()
    return stripped.startswith("{{") and stripped.endswith("}}")


def is_empty_or_placeholder(value: str) -> bool:
    stripped = value.strip()
    return not stripped or is_placeholder(stripped)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]], list[Issue]]:
    issues: list[Issue] = []
    try:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return reader.fieldnames or [], [dict(row) for row in reader], issues
    except Exception as exc:  # pragma: no cover - diagnostic path
        return [], [], [Issue("ERROR", path, 0, f"could not read CSV: {exc}")]


def validate_header(path: Path, expected: list[str]) -> tuple[list[dict[str, str]], list[Issue]]:
    header, rows, issues = read_csv(path)
    if issues:
        return rows, issues
    if header != expected:
        missing = [column for column in expected if column not in set(header)]
        extra = [column for column in header if column not in expected]
        issues.append(
            Issue(
                "ERROR",
                path,
                1,
                f"non-canonical header; missing={missing}; extra={extra}",
            )
        )
    return rows, issues


def validate_common_sec_fields(path: Path, rows: list[dict[str, str]], required_fields: list[str]) -> list[Issue]:
    issues: list[Issue] = []
    for i, row in enumerate(rows, start=2):
        template_row = all(is_empty_or_placeholder(row.get(field, "")) for field in required_fields)
        if template_row:
            continue
        for field in required_fields:
            if is_empty_or_placeholder(row.get(field, "")):
                issues.append(Issue("ERROR", path, i, f"missing SEC provenance field `{field}`"))
    return issues


def validate_supplement(path: Path) -> list[Issue]:
    rows, issues = validate_header(path, SUPPLEMENT_COLUMNS)
    if issues:
        return issues

    issues.extend(
        validate_common_sec_fields(
            path,
            rows,
            ["company_name", "ticker", "cik", "checked_at", "sec_source_id", "source_url", "metric_or_claim"],
        )
    )
    for i, row in enumerate(rows, start=2):
        if all(is_empty_or_placeholder(value) for value in row.values()):
            continue
        route = row.get("route", "").strip()
        if route and not is_placeholder(route) and route not in SUPPLEMENT_ROUTES:
            issues.append(Issue("ERROR", path, i, f"invalid route `{route}`"))
        authority = row.get("authority_level", "").strip()
        if authority and not is_placeholder(authority) and authority not in AUTHORITY_LEVELS:
            issues.append(Issue("ERROR", path, i, f"invalid authority_level `{authority}`"))
        source_gap = row.get("source_gap", "").strip()
        if source_gap and not is_placeholder(source_gap) and source_gap not in SOURCE_GAP_VALUES:
            issues.append(Issue("ERROR", path, i, f"invalid source_gap `{source_gap}`"))
        impact = row.get("confirms_or_conflicts", "").strip()
        if impact and not is_placeholder(impact) and impact not in IMPACT_VALUES:
            issues.append(Issue("ERROR", path, i, f"invalid confirms_or_conflicts `{impact}`"))
    return issues


def validate_metric_table(path: Path) -> list[Issue]:
    rows, issues = validate_header(path, METRIC_COLUMNS)
    if issues:
        return issues
    issues.extend(
        validate_common_sec_fields(
            path,
            rows,
            ["metric_id", "company_name", "ticker", "cik", "form_type", "filing_date", "source_url", "metric_name"],
        )
    )
    for i, row in enumerate(rows, start=2):
        if all(is_empty_or_placeholder(value) for value in row.values()):
            continue
        confidence = row.get("confidence", "").strip()
        if confidence and not is_placeholder(confidence) and confidence not in CONFIDENCE_LEVELS:
            issues.append(Issue("ERROR", path, i, f"invalid confidence `{confidence}`"))
        impact = row.get("confirms_or_conflicts", "").strip()
        if impact and not is_placeholder(impact) and impact not in IMPACT_VALUES:
            issues.append(Issue("ERROR", path, i, f"invalid confirms_or_conflicts `{impact}`"))
    return issues


def validate_risk_delta(path: Path) -> list[Issue]:
    rows, issues = validate_header(path, RISK_COLUMNS)
    if issues:
        return issues
    issues.extend(
        validate_common_sec_fields(
            path,
            rows,
            ["risk_id", "company_name", "ticker", "cik", "form_type", "filing_date", "section", "risk_area"],
        )
    )
    for i, row in enumerate(rows, start=2):
        if all(is_empty_or_placeholder(value) for value in row.values()):
            continue
        delta_type = row.get("delta_type", "").strip()
        if delta_type and not is_placeholder(delta_type) and delta_type not in DELTA_TYPES:
            issues.append(Issue("ERROR", path, i, f"invalid delta_type `{delta_type}`"))
        confidence = row.get("confidence", "").strip()
        if confidence and not is_placeholder(confidence) and confidence not in CONFIDENCE_LEVELS:
            issues.append(Issue("ERROR", path, i, f"invalid confidence `{confidence}`"))
    return issues


def validate_accounting_check(path: Path) -> list[Issue]:
    rows, issues = validate_header(path, ACCOUNTING_COLUMNS)
    if issues:
        return issues
    issues.extend(
        validate_common_sec_fields(
            path,
            rows,
            ["check_id", "company_name", "ticker", "cik", "form_type", "filing_date", "quality_area", "source_url"],
        )
    )
    for i, row in enumerate(rows, start=2):
        if all(is_empty_or_placeholder(value) for value in row.values()):
            continue
        source_gap = row.get("source_gap", "").strip()
        if source_gap and not is_placeholder(source_gap) and source_gap not in SOURCE_GAP_VALUES:
            issues.append(Issue("ERROR", path, i, f"invalid source_gap `{source_gap}`"))
        confidence = row.get("confidence", "").strip()
        if confidence and not is_placeholder(confidence) and confidence not in CONFIDENCE_LEVELS:
            issues.append(Issue("ERROR", path, i, f"invalid confidence `{confidence}`"))
    return issues


def validate_package(path: Path) -> list[Issue]:
    issues: list[Issue] = []
    for file_name, columns in REQUIRED_PACKAGE_FILES.items():
        file_path = path / file_name
        if not file_path.exists():
            issues.append(Issue("ERROR", file_path, 0, "missing required SEC filing package file"))
            continue
        if file_name == "evidence-log.csv":
            issues.extend(validate_canonical_evidence_log(file_path))
            continue
        if columns is None:
            continue
        if file_name == "filing-metric-table.csv":
            issues.extend(validate_metric_table(file_path))
        elif file_name == "filing-risk-delta.csv":
            issues.extend(validate_risk_delta(file_path))
        elif file_name == "accounting-quality-check.csv":
            issues.extend(validate_accounting_check(file_path))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="SEC supplement CSV files or SEC filing package directories")
    parser.add_argument("--report-only", action="store_true", help="print issues but exit 0")
    args = parser.parse_args()

    issues: list[Issue] = []
    for raw_path in args.paths:
        path = Path(raw_path)
        if path.is_dir():
            issues.extend(validate_package(path))
        elif path.name == "sec-supplement-source-note.csv":
            issues.extend(validate_supplement(path))
        elif path.name == "filing-metric-table.csv":
            issues.extend(validate_metric_table(path))
        elif path.name == "filing-risk-delta.csv":
            issues.extend(validate_risk_delta(path))
        elif path.name == "accounting-quality-check.csv":
            issues.extend(validate_accounting_check(path))
        elif path.name == "evidence-log.csv":
            issues.extend(validate_canonical_evidence_log(path))
        else:
            issues.append(
                Issue(
                    "ERROR",
                    path,
                    0,
                    "expected SEC supplement CSV, SEC package dir, SEC package CSV, or evidence-log.csv",
                )
            )

    errors = [issue for issue in issues if issue.severity == "ERROR"]
    warnings = [issue for issue in issues if issue.severity == "WARN"]
    for issue in issues:
        print(issue.render())
    print(f"summary: {len(errors)} errors, {len(warnings)} warnings")
    if errors and not args.report_only:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
