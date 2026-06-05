#!/usr/bin/env python3
"""Regression tests for Mira repository validation contracts.

The fixtures are synthetic and only exercise validator behavior.
"""

from __future__ import annotations

import csv
import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import generate_case_manifests  # noqa: E402
import validate_repo  # noqa: E402


def assert_no_issues(name: str, issues: list[validate_repo.Issue]) -> None:
    if issues:
        print(f"FAIL: {name}: expected no issues")
        for issue in issues:
            print(issue.render())
        raise SystemExit(1)
    print(f"ok {name}")


def assert_issue_contains(name: str, issues: list[validate_repo.Issue], marker: str) -> None:
    rendered = "\n".join(issue.render() for issue in issues)
    if marker not in rendered:
        print(f"FAIL: {name}: missing marker `{marker}`")
        print(rendered)
        raise SystemExit(1)
    print(f"ok {name}")


def write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def evidence_row(source_id: str, *, notes: str = "Synthetic fixture note.") -> dict[str, str]:
    return {
        "source_id": source_id,
        "claim_area": "unit_test",
        "claim_type": "derived_calculation",
        "claim_text": "Synthetic modeled metric used only for validator regression tests.",
        "source_speaker": "synthetic_fixture",
        "verification_status": "modeled",
        "authority_level": "L6",
        "source_date": "2026-06-01",
        "as_of_date": "2026-06-01",
        "url_or_path": "synthetic_fixture",
        "used_by_agent": "validator_regression_test",
        "used_by_skill": "validator_regression_test",
        "confidence": "medium",
        "upstream_sources": "synthetic_input_a; synthetic_input_b",
        "notes": notes,
        "evidence_category": "estimate",
        "freshness_status": "current",
        "conflict_status": "none",
        "treatment": "sensitize",
        "readiness_impact": "supports_working_view",
    }


def ledger_row(calculation_id: str, evidence_log_ref: str) -> dict[str, str]:
    return {
        "calculation_id": calculation_id,
        "research_object": "SYNTHETIC",
        "question": "Can derived calculations be traced?",
        "metric": "synthetic_metric",
        "formula": "input_a + input_b",
        "input_sources": "synthetic_input_a; synthetic_input_b",
        "period": "2026-06-01",
        "unit": "units",
        "result": "42",
        "cross_check": "manual recomputation matched",
        "tool_used": "python",
        "verification_status": "modeled",
        "limitations": "Synthetic fixture only.",
        "evidence_log_ref": evidence_log_ref,
    }


def write_evidence_log(path: Path, rows: list[dict[str, str]]) -> None:
    write_csv(path, validate_repo.CANONICAL_EVIDENCE_COLUMNS, rows)


def write_calculation_ledger(path: Path, rows: list[dict[str, str]]) -> None:
    write_csv(path, validate_repo.CALCULATION_LEDGER_COLUMNS, rows)


def write_case_readme(path: Path) -> None:
    path.write_text(
        """# Synthetic Case

- research_cutoff_date: 2026-06-01
- stale_after: 2026-07-01
- must_refresh_if: material new information appears.
- not_investment_advice: true
""",
        encoding="utf-8",
    )


def test_derived_calculation_requires_formula_or_ledger(tmp: Path) -> None:
    evidence_path = tmp / "evidence-log.csv"
    write_evidence_log(evidence_path, [evidence_row("calc_missing_trace")])
    assert_issue_contains(
        "derived calculation without trace is rejected",
        validate_repo.validate_evidence_log(evidence_path),
        "derived_calculation requires a Formula: note or calculation-ledger.csv row",
    )

    write_calculation_ledger(tmp / "calculation-ledger.csv", [ledger_row("calc_001", "calc_missing_trace")])
    assert_no_issues(
        "derived calculation can be traced through calculation ledger",
        validate_repo.validate_evidence_log(evidence_path),
    )

    write_evidence_log(
        evidence_path,
        [evidence_row("calc_formula_trace", notes="Formula: input_a + input_b. Synthetic fixture.")],
    )
    assert_no_issues(
        "derived calculation can be traced through formula note",
        validate_repo.validate_evidence_log(evidence_path),
    )


def test_calculation_ledger_refs_sibling_evidence_log(tmp: Path) -> None:
    write_evidence_log(tmp / "evidence-log.csv", [evidence_row("known_calc_ref", notes="Formula: input_a + input_b.")])
    ledger_path = tmp / "calculation-ledger.csv"
    write_calculation_ledger(ledger_path, [ledger_row("calc_001", "missing_calc_ref")])

    assert_issue_contains(
        "calculation ledger rejects unknown evidence refs",
        validate_repo.validate_calculation_ledger(ledger_path),
        "evidence_log_ref `missing_calc_ref` not found in sibling evidence-log.csv",
    )


def manifest_payload(package_type: str, hero_artifacts: list[str], support_artifacts: list[str]) -> dict[str, object]:
    return {
        "manifest_version": "mira_package_manifest_v1",
        "case_id": "synthetic-case",
        "research_object": "SYNTHETIC",
        "market_scope": "US equity",
        "time_boundary": "synthetic through 2026-06-01",
        "research_cutoff_date": "2026-06-01",
        "package_type": package_type,
        "readiness_level": "working_view",
        "readiness_basis": "Synthetic fixture.",
        "blocking_gaps": [],
        "hero_artifacts": hero_artifacts,
        "support_artifacts": support_artifacts,
        "source_scope": "Synthetic fixture.",
        "evidence_log_status": "canonical_v1_1",
        "quant_gate_status": "not_required_or_not_recorded",
        "stale_after": "2026-07-01",
        "must_refresh_if": ["material new information appears"],
    }


def test_manifest_artifacts_and_package_types(tmp: Path) -> None:
    (tmp / "earnings-analysis.md").write_text("# Earnings Analysis\n", encoding="utf-8")
    (tmp / "evidence-log.csv").write_text("source_id\n", encoding="utf-8")
    manifest_path = tmp / "research-package-manifest.json"

    manifest_path.write_text(
        json.dumps(manifest_payload("earnings_package", ["earnings-analysis.md"], ["evidence-log.csv"])),
        encoding="utf-8",
    )
    assert_no_issues(
        "manifest accepts non-research package type",
        validate_repo.validate_research_package_manifest(manifest_path),
    )

    manifest_path.write_text(
        json.dumps(manifest_payload("earnings_package", ["missing.md"], ["evidence-log.csv"])),
        encoding="utf-8",
    )
    assert_issue_contains(
        "manifest rejects missing hero artifact",
        validate_repo.validate_research_package_manifest(manifest_path),
        "`hero_artifacts` references missing artifact `missing.md`",
    )


def test_case_with_evidence_log_requires_manifest(tmp: Path) -> None:
    write_case_readme(tmp / "README.md")
    write_evidence_log(
        tmp / "evidence-log.csv",
        [evidence_row("calc_formula_trace", notes="Formula: input_a + input_b. Synthetic fixture.")],
    )

    assert_issue_contains(
        "case readme requires manifest when evidence log exists",
        validate_repo.validate_case_readme(tmp),
        "case with evidence-log.csv must include research-package-manifest.json",
    )


def test_generated_manifest_classifies_earnings_and_calculation_artifacts(tmp: Path) -> None:
    write_case_readme(tmp / "README.md")
    (tmp / "earnings-analysis.md").write_text("# Earnings Analysis\n", encoding="utf-8")
    write_evidence_log(tmp / "evidence-log.csv", [evidence_row("calc_earnings_ref", notes="Formula: a + b.")])
    write_calculation_ledger(tmp / "calculation-ledger.csv", [ledger_row("calc_earnings", "calc_earnings_ref")])

    manifest = generate_case_manifests.build_manifest(tmp)

    if manifest["package_type"] != "earnings_package":
        print(f"FAIL: generated manifest package_type={manifest['package_type']}")
        raise SystemExit(1)
    if manifest["hero_artifacts"] != ["earnings-analysis.md"]:
        print(f"FAIL: generated manifest hero_artifacts={manifest['hero_artifacts']}")
        raise SystemExit(1)
    if "evidence-log.csv" not in manifest["support_artifacts"]:
        print(f"FAIL: generated manifest support_artifacts={manifest['support_artifacts']}")
        raise SystemExit(1)
    if "calculation-ledger.csv" not in manifest["calculation_artifacts"]:
        print(f"FAIL: generated manifest calculation_artifacts={manifest['calculation_artifacts']}")
        raise SystemExit(1)
    print("ok generated manifest classifies earnings and calculation artifacts")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="mira-repo-contracts-") as tmp_dir:
        tmp = Path(tmp_dir)
        test_derived_calculation_requires_formula_or_ledger(tmp)
    with tempfile.TemporaryDirectory(prefix="mira-repo-contracts-") as tmp_dir:
        test_calculation_ledger_refs_sibling_evidence_log(Path(tmp_dir))
    with tempfile.TemporaryDirectory(prefix="mira-repo-contracts-") as tmp_dir:
        test_manifest_artifacts_and_package_types(Path(tmp_dir))
    with tempfile.TemporaryDirectory(prefix="mira-repo-contracts-") as tmp_dir:
        test_case_with_evidence_log_requires_manifest(Path(tmp_dir))
    with tempfile.TemporaryDirectory(prefix="mira-repo-contracts-") as tmp_dir:
        test_generated_manifest_classifies_earnings_and_calculation_artifacts(Path(tmp_dir))
    print("repo_validation_contract_tests: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
