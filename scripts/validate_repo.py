#!/usr/bin/env python3
"""Validate Mira repository readiness and research discipline.

Default mode is strict and exits non-zero on errors. Use --report-only to
surface current legacy drift without failing the run.
"""

from __future__ import annotations

import argparse
import csv
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

CANONICAL_EVIDENCE_COLUMNS = [
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
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_IN_TEXT_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
STALE_AFTER_RE = re.compile(r"stale_after:\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
FIELD_RE = re.compile(r"^-\s*(state|research_action):\s*(.+?)\s*$")
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
    if header != CANONICAL_EVIDENCE_COLUMNS:
        missing = [c for c in CANONICAL_EVIDENCE_COLUMNS if c not in header_set]
        extra = [c for c in header if c not in CANONICAL_EVIDENCE_COLUMNS]
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
        for field in CANONICAL_EVIDENCE_COLUMNS:
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

    if not rows:
        issues.append(Issue("ERROR", path, 1, "evidence-log.csv has no claim rows"))

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


def validate_repo(root: Path, as_of: date) -> list[Issue]:
    issues = validate_root_readiness(root)
    issues.extend(validate_source_class_map(root))
    issues.extend(validate_source_coverage_matrix(root))
    for path in sorted(root.glob("**/evidence-log.csv")):
        if ".git" in path.parts:
            continue
        issues.extend(validate_evidence_log(path))
    for path in sorted(root.glob("**/decision-log.csv")):
        if ".git" in path.parts:
            continue
        issues.extend(validate_decision_log(path))
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
        for case_dir in sorted(path for path in cases_dir.iterdir() if path.is_dir()):
            issues.extend(validate_case_readme(case_dir))
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
        elif path.name == "evidence-log.csv":
            issues.extend(validate_no_local_absolute_paths(path))
            issues.extend(validate_evidence_log(path))
        elif path.name == "decision-log.csv":
            issues.extend(validate_no_local_absolute_paths(path))
            issues.extend(validate_decision_log(path))
        else:
            issues.append(Issue("ERROR", path, 0, "expected evidence-log.csv or case directory"))
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
