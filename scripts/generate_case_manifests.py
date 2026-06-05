#!/usr/bin/env python3
"""Generate Mira package manifests for case directories.

The generator is intentionally conservative. It infers package type and artifact
lists from files already present in a case directory, while leaving substantive
research judgments in the underlying package files.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

PACKAGE_RULES = [
    (
        "earnings_package",
        ["earnings-analysis.md"],
        "skills/earnings-report-analysis/SKILL.md",
        "loops/event-delta-loop.md",
    ),
    (
        "industry_package",
        ["industry-map.md"],
        "skills/industry-concept-analysis/SKILL.md",
        "loops/research-loop.md",
    ),
    (
        "etf_discovery_package",
        ["discovery-log.md", "new-etf-watchlist.csv"],
        "skills/etf-listing-discovery/SKILL.md",
        "loops/research-loop.md",
    ),
    (
        "etf_listing_analysis_package",
        ["etf-listing-analysis.md"],
        "skills/etf-listing-analysis/SKILL.md",
        "loops/research-loop.md",
    ),
    (
        "failure_backtest_package",
        ["failure-backtest.md"],
        "loops/decision-quality-review-loop.md",
        "loops/decision-quality-review-loop.md",
    ),
    (
        "value_capture_package",
        ["value-capture-screen.md"],
        "skills/industry-concept-analysis/SKILL.md",
        "loops/research-loop.md",
    ),
    (
        "company_handoff_package",
        ["company-handoff.md"],
        "skills/industry-concept-analysis/SKILL.md",
        "loops/research-loop.md",
    ),
    (
        "watchlist_package",
        ["watchlist.md"],
        "loops/research-loop.md",
        "loops/research-loop.md",
    ),
    (
        "research_package",
        ["investment-memo.md"],
        "skills/equity-research-core/SKILL.md",
        "loops/research-loop.md",
    ),
]

SUPPORT_EXTENSIONS = {".md", ".csv", ".json"}
EXCLUDED_SUPPORT = {"README.md", "research-package-manifest.json"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def metadata_value(readme_text: str, key: str) -> str | None:
    pattern = re.compile(rf"^\s*-\s*{re.escape(key)}\s*:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(readme_text)
    if not match:
        return None
    return match.group(1).strip().strip("`")


def first_date(text: str) -> str | None:
    match = DATE_RE.search(text)
    return match.group(0) if match else None


def infer_research_cutoff(readme_text: str) -> str:
    for key in (
        "research_cutoff_date",
        "analysis_cutoff_date",
        "case_date",
        "release_date",
        "as_of",
        "review_date",
    ):
        value = metadata_value(readme_text, key)
        if value:
            date_value = first_date(value)
            if date_value:
                return date_value
    date_value = first_date(readme_text)
    return date_value or "1970-01-01"


def infer_stale_after(readme_text: str, fallback_date: str) -> tuple[str, list[str]]:
    raw = metadata_value(readme_text, "stale_after")
    must_refresh = metadata_value(readme_text, "must_refresh_if")
    refresh_policy = metadata_value(readme_text, "refresh_policy")
    if raw:
        date_value = first_date(raw) or fallback_date
        if must_refresh:
            return date_value, [must_refresh]
        return date_value, [raw]
    if must_refresh:
        return fallback_date, [must_refresh]
    if refresh_policy:
        return fallback_date, [refresh_policy]
    return fallback_date, ["Refresh before live research, trading, portfolio or publication use."]


def infer_research_object(case_dir: Path, readme_text: str) -> str:
    for key in ("ticker", "concept_name", "company", "case", "theme", "research_object"):
        value = metadata_value(readme_text, key)
        if value:
            return value.split("/")[0].strip()
    return case_dir.name


def infer_market_scope(case_dir: Path, readme_text: str) -> str:
    market = metadata_value(readme_text, "market")
    if market:
        return market
    name = case_dir.name.lower()
    if "a-share" in name:
        return "China A-share"
    if any(token in name for token in ("aapl", "cohr", "crm", "nvts", "pton", "tdoc", "vrt", "wolf")):
        return "US equity"
    return "unspecified"


def existing_files(case_dir: Path) -> set[str]:
    return {path.name for path in case_dir.iterdir() if path.is_file()}


def infer_package_type(case_dir: Path) -> tuple[str, str, str, list[str]]:
    files = existing_files(case_dir)
    for package_type, hero_candidates, lead_skill, primary_loop in PACKAGE_RULES:
        present = [name for name in hero_candidates if name in files]
        if present:
            return package_type, lead_skill, primary_loop, present
    if "evidence-log.csv" in files:
        return "evidence_package", "loops/research-loop.md", "loops/research-loop.md", ["evidence-log.csv"]
    return "case_package", "loops/research-loop.md", "loops/research-loop.md", sorted(files)


def support_artifacts(case_dir: Path, hero_artifacts: list[str]) -> list[str]:
    support = []
    hero_set = set(hero_artifacts)
    for path in sorted(case_dir.iterdir(), key=lambda item: item.name):
        if not path.is_file():
            continue
        if path.name in EXCLUDED_SUPPORT or path.name in hero_set:
            continue
        if path.suffix.lower() in SUPPORT_EXTENSIONS:
            support.append(path.name)
    return support


def evidence_log_status(case_dir: Path) -> str:
    path = case_dir / "evidence-log.csv"
    if not path.exists():
        return "not_present"
    header = path.read_text(encoding="utf-8").splitlines()[0].split(",")
    return "canonical_v1_1" if len(header) == 20 else "legacy_or_noncanonical"


def quant_gate_status(files: set[str]) -> str:
    calculation_markers = (
        "calculation-ledger",
        "valuation",
        "scenario",
        "peer-comparison",
        "financial-snapshot",
        "workflow-scorecard",
        "marketcap",
    )
    if any(any(marker in name for marker in calculation_markers) for name in files):
        return "case_artifacts_present_review_required"
    return "not_required_or_not_recorded"


def build_manifest(case_dir: Path) -> dict[str, Any]:
    readme_path = case_dir / "README.md"
    readme_text = read_text(readme_path) if readme_path.exists() else ""
    package_type, lead_skill, primary_loop, hero_artifacts = infer_package_type(case_dir)
    files = existing_files(case_dir)
    cutoff = infer_research_cutoff(readme_text)
    stale_after, must_refresh_if = infer_stale_after(readme_text, cutoff)
    support = support_artifacts(case_dir, hero_artifacts)
    if "evidence-log.csv" in files and "evidence-log.csv" not in support and "evidence-log.csv" not in hero_artifacts:
        support.insert(0, "evidence-log.csv")

    readiness = "working_view" if "not_investment_advice" in readme_text.lower() else "draft"
    blocking_gaps = []
    if stale_after == cutoff:
        blocking_gaps.append("stale_after was inferred from cutoff date; refresh boundary should be reviewed")
    if evidence_log_status(case_dir) != "canonical_v1_1":
        blocking_gaps.append("evidence log is missing or noncanonical")

    return {
        "manifest_version": "mira_package_manifest_v1",
        "case_id": case_dir.name,
        "research_object": infer_research_object(case_dir, readme_text),
        "market_scope": infer_market_scope(case_dir, readme_text),
        "time_boundary": f"historical case through {cutoff}; refresh before live use",
        "research_cutoff_date": cutoff,
        "package_type": package_type,
        "readiness_level": readiness,
        "readiness_basis": "Generated package manifest for historical Mira case handoff; use underlying artifacts and evidence log for substantive conclusions.",
        "blocking_gaps": blocking_gaps,
        "primary_loop": primary_loop,
        "lead_skill": lead_skill,
        "support_skills": [],
        "hero_artifacts": hero_artifacts,
        "support_artifacts": support,
        "handoffs": [],
        "source_scope": "See evidence-log.csv and case README for source coverage and limitations.",
        "evidence_log_status": evidence_log_status(case_dir),
        "quant_gate_status": quant_gate_status(files),
        "calculation_artifacts": [
            name for name in sorted(files) if any(marker in name for marker in ("calculation-ledger", "valuation", "scenario", "financial-snapshot", "peer-comparison", "scorecard"))
        ],
        "stale_after": stale_after,
        "must_refresh_if": must_refresh_if,
        "notes": "Generated by scripts/generate_case_manifests.py. Historical example; not investment advice.",
    }


def eligible_case_dirs(root: Path) -> list[Path]:
    return [
        path
        for path in sorted((root / "cases").iterdir())
        if path.is_dir() and (path / "README.md").exists() and (path / "evidence-log.csv").exists()
    ]


def is_generated_manifest(target: Path) -> bool:
    if not target.exists():
        return False
    try:
        data = json.loads(target.read_text(encoding="utf-8"))
    except Exception:
        return False
    return data.get("manifest_version") == "mira_package_manifest_v1"


def write_manifest(case_dir: Path, overwrite: bool, overwrite_generated: bool, dry_run: bool) -> str:
    target = case_dir / "research-package-manifest.json"
    if target.exists() and not overwrite and not (overwrite_generated and is_generated_manifest(target)):
        return "exists"
    manifest = build_manifest(case_dir)
    if dry_run:
        return f"would_write package_type={manifest['package_type']}"
    target.write_text(json.dumps(manifest, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    return f"wrote package_type={manifest['package_type']}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_dirs", nargs="*", type=Path, help="case directories to process")
    parser.add_argument("--root", type=Path, default=Path("."), help="repository root")
    parser.add_argument("--all", action="store_true", help="generate manifests for all eligible case directories")
    parser.add_argument("--overwrite", action="store_true", help="overwrite existing manifests")
    parser.add_argument("--overwrite-generated", action="store_true", help="overwrite only manifests previously generated by this script")
    parser.add_argument("--dry-run", action="store_true", help="print planned writes without changing files")
    args = parser.parse_args()

    if args.all:
        case_dirs = eligible_case_dirs(args.root)
    else:
        case_dirs = args.case_dirs
    if not case_dirs:
        parser.error("provide case directories or --all")

    for case_dir in case_dirs:
        print(f"{case_dir}: {write_manifest(case_dir, args.overwrite, args.overwrite_generated, args.dry_run)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
