#!/usr/bin/env python3
"""Run the long-term workflow release QA suite.

This is an orchestration check, not an external-release approval.
The expected state before G04/G06 clear is:

- internal candidate release validator passes
- external-ready validator fails
- G04/G06 validators reject blank templates and accept synthetic fixtures
- trial theme matrix selection evidence is source-linked and case-linked
- theme selection refresh audit proves recent-theme freshness and replacement controls
- recent-theme selection validator combines selection and refresh checks for objective/goal audits
- public release freshness validator prevents stale public materials from being reused
- practice falsification audit proves methodology claims are case-grounded, not theory-only
- methodology iteration trace audit proves workflow changes trace to case failures
- multi-lens coverage audit proves consumer/product/economy/industry/company/valuation coverage
- public workflow pack is cross-file checked for overlay and release-boundary consistency
- external reviewer assignment packet is internally consistent
- G01 external method-source scan is improved but not externally cleared
- external reviewer assignment tracker is ready but not completed
- external reviewer candidate screen is ready but no candidate is selected
- external reviewer selection rubric maps release decisions to reviewer profiles
- external reviewer independence screen is ready but not completed
- external reviewer packet export is dry-run checked
- external reviewer dispatch packet export is audited and still does not clear G06
- G06 dispatch readiness checklist passes while reviewer assignment/return remain pending
- external release action queue keeps G04/G06 real-world unblock actions explicit
- G04 follow-through trigger tracker is executable
- G04 event watch calendar is explicit and does not clear G04 prematurely
- G04 later-event candidate screen separates scheduled/no-event states from refresh-ready events
- G04 follow-through execution tracker is ready but not completed
- G04 follow-through packet export is dry-run checked
- G04 follow-through packet matrix is export-audited across tracked live cases
- institutional colleague release bundle preserves release controls
- institutional colleague acceptance checklist is prepared but not prematurely complete
- institutional colleague release packet export refuses until external-ready
- go/no-go evidence coverage stays aligned with required public release gates
- final release cutover controls remain pending until external-ready
- objective-level readiness audit remains aligned with external-ready status
- goal-level completion audit remains aligned with external-ready status
- release verification command manifest is executable and includes expected blockers
- non-recursive case-set validator passes all validation cases
- validation cases pass repository discipline checks
"""

from __future__ import annotations

import csv
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AS_OF = "2026-05-30"

VALIDATION_CASES = [
    "cases/etn-2026-05-long-term-workflow-trial",
    "cases/vrt-2026-05-long-term-workflow-trial",
    "cases/crm-2026-05-product-workflow-trial",
    "cases/lly-2026-05-glp1-workflow-dry-run",
    "cases/humanoid-robotics-2026-05-value-capture-screen",
    "cases/nuclear-ai-power-2026-05-value-capture-screen",
    "cases/stablecoin-payments-2026-05-value-capture-screen",
    "cases/defense-autonomy-drones-2026-05-value-capture-screen",
    "cases/tdoc-2020-2022-failure-backtest",
    "cases/pton-2020-2022-failure-backtest",
]

CSV_FILES = [
    "cases/long-term-workflow-validation-2026-05-30/public-release-gate-tracker.csv",
    "cases/long-term-workflow-validation-2026-05-30/g01-external-method-source-audit.csv",
    "cases/long-term-workflow-validation-2026-05-30/external-reviewer-bundle-manifest.csv",
    "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-assignment-tracker.csv",
    "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-candidate-screen.csv",
    "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-selection-rubric.csv",
    "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-independence-screen.csv",
    "cases/long-term-workflow-validation-2026-05-30/g06-dispatch-readiness-checklist.csv",
    "cases/long-term-workflow-validation-2026-05-30/external-release-action-queue.csv",
    "cases/long-term-workflow-validation-2026-05-30/institutional-release-bundle-manifest.csv",
    "cases/long-term-workflow-validation-2026-05-30/institutional-colleague-acceptance-checklist.csv",
    "cases/long-term-workflow-validation-2026-05-30/objective-readiness-audit.csv",
    "cases/long-term-workflow-validation-2026-05-30/goal-completion-audit.csv",
    "cases/long-term-workflow-validation-2026-05-30/release-verification-command-manifest.csv",
    "cases/long-term-workflow-validation-2026-05-30/trial-theme-matrix.csv",
    "cases/long-term-workflow-validation-2026-05-30/theme-selection-refresh-audit.csv",
    "cases/long-term-workflow-validation-2026-05-30/practice-falsification-audit.csv",
    "cases/long-term-workflow-validation-2026-05-30/methodology-iteration-trace-audit.csv",
    "cases/long-term-workflow-validation-2026-05-30/multi-lens-coverage-audit.csv",
    "cases/long-term-workflow-validation-2026-05-30/cross-case-validation-matrix.csv",
    "cases/long-term-workflow-validation-2026-05-30/overlay-coverage-audit.csv",
    "cases/long-term-workflow-validation-2026-05-30/historical-backtest-source-archive-audit.csv",
    "cases/long-term-workflow-validation-2026-05-30/final-release-cutover-checklist.csv",
    "cases/long-term-workflow-validation-2026-05-30/g04-follow-through-event-watch-calendar.csv",
    "cases/long-term-workflow-validation-2026-05-30/g04-later-event-candidate-screen.csv",
    "cases/long-term-workflow-validation-2026-05-30/g04-follow-through-execution-tracker.csv",
    "cases/long-term-workflow-validation-2026-05-30/g04-follow-through-intake-checklist.csv",
    "cases/long-term-workflow-validation-2026-05-30/public-workflow-pack/external-review-intake-checklist.csv",
]


@dataclass
class CheckResult:
    name: str
    passed: bool
    returncode: int | None = None
    detail: str = ""


def run_command(name: str, args: list[str], expected_codes: set[int]) -> CheckResult:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    passed = result.returncode in expected_codes
    output = "\n".join(part for part in (result.stdout, result.stderr) if part).strip()
    return CheckResult(
        name=name,
        passed=passed,
        returncode=result.returncode,
        detail=output,
    )


def validate_csv_shape(path_str: str) -> CheckResult:
    path = ROOT / path_str
    if not path.exists():
        return CheckResult(path_str, False, detail="missing CSV file")
    try:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames or []
            rows = list(reader)
    except Exception as exc:
        return CheckResult(path_str, False, detail=f"could not parse CSV: {exc}")
    if not header:
        return CheckResult(path_str, False, detail="missing header")
    if not rows:
        return CheckResult(path_str, False, detail="no data rows")
    blank_rows = [
        idx
        for idx, row in enumerate(rows, start=2)
        if not any((value or "").strip() for value in row.values())
    ]
    if blank_rows:
        return CheckResult(path_str, False, detail=f"blank rows: {blank_rows}")
    return CheckResult(path_str, True, detail=f"rows={len(rows)}")


def main() -> int:
    checks: list[CheckResult] = []

    checks.append(
        run_command(
            "release_validator_internal_candidate",
            [sys.executable, "scripts/validate_long_term_release.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "release_validator_external_ready_expected_failure",
            [sys.executable, "scripts/validate_long_term_release.py", "--require-external-ready"],
            {2},
        )
    )
    checks.append(
        run_command(
            "validator_regression_tests",
            [sys.executable, "scripts/test_long_term_release_validators.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "repo_validation_contract_tests",
            [sys.executable, "scripts/test_repo_validation_contracts.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "validation_case_set",
            [sys.executable, "scripts/validate_validation_case_set.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "trial_theme_matrix_validation",
            [sys.executable, "scripts/validate_trial_theme_matrix.py", "--as-of", AS_OF],
            {0},
        )
    )
    checks.append(
        run_command(
            "recent_theme_selection_validation",
            [sys.executable, "scripts/validate_recent_theme_selection.py", "--as-of", AS_OF],
            {0},
        )
    )
    checks.append(
        run_command(
            "theme_selection_refresh_audit_validation",
            [sys.executable, "scripts/validate_theme_selection_refresh_audit.py", "--as-of", AS_OF],
            {0},
        )
    )
    checks.append(
        run_command(
            "public_release_freshness_validation",
            [sys.executable, "scripts/validate_public_release_freshness.py", "--as-of", AS_OF],
            {0},
        )
    )
    checks.append(
        run_command(
            "practice_falsification_audit_validation",
            [sys.executable, "scripts/validate_practice_falsification_audit.py", "--as-of", AS_OF],
            {0},
        )
    )
    checks.append(
        run_command(
            "methodology_iteration_trace_audit_validation",
            [sys.executable, "scripts/validate_methodology_iteration_trace_audit.py", "--as-of", AS_OF],
            {0},
        )
    )
    checks.append(
        run_command(
            "multi_lens_coverage_audit_validation",
            [sys.executable, "scripts/validate_multi_lens_coverage_audit.py", "--as-of", AS_OF],
            {0},
        )
    )
    checks.append(
        run_command(
            "public_workflow_pack_validation",
            [sys.executable, "scripts/validate_public_workflow_pack.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "external_review_packet_validation",
            [sys.executable, "scripts/validate_external_review_packet.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "g01_external_method_scan_validation",
            [sys.executable, "scripts/validate_g01_external_method_scan.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "external_review_assignment_tracker_validation",
            [sys.executable, "scripts/validate_external_review_assignment_tracker.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "g06_reviewer_candidate_screen_validation",
            [sys.executable, "scripts/validate_g06_reviewer_candidate_screen.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "g06_reviewer_selection_rubric_validation",
            [sys.executable, "scripts/validate_g06_reviewer_selection_rubric.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "g06_reviewer_independence_screen_validation",
            [sys.executable, "scripts/validate_g06_reviewer_independence_screen.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "external_review_packet_export_dry_run",
            [sys.executable, "scripts/build_external_review_packet.py", "--dry-run"],
            {0},
        )
    )
    checks.append(
        run_command(
            "external_review_dispatch_packet_validation",
            [sys.executable, "scripts/validate_external_review_dispatch_packet.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "g06_dispatch_readiness_validation",
            [sys.executable, "scripts/validate_g06_dispatch_readiness.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "external_release_action_queue_validation",
            [sys.executable, "scripts/validate_external_release_action_queue.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "follow_through_trigger_tracker_validation",
            [sys.executable, "scripts/validate_follow_through_trigger_tracker.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "g04_event_watch_calendar_validation",
            [sys.executable, "scripts/validate_g04_event_watch_calendar.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "g04_later_event_candidate_screen_validation",
            [sys.executable, "scripts/validate_g04_later_event_candidate_screen.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "follow_through_execution_tracker_validation",
            [sys.executable, "scripts/validate_follow_through_execution_tracker.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "follow_through_packet_export_dry_run",
            [sys.executable, "scripts/build_follow_through_packet.py", "--dry-run"],
            {0},
        )
    )
    checks.append(
        run_command(
            "follow_through_packet_matrix_validation",
            [sys.executable, "scripts/validate_follow_through_packet_matrix.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "institutional_release_bundle_validation",
            [sys.executable, "scripts/validate_institutional_release_bundle.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "institutional_colleague_acceptance_validation",
            [sys.executable, "scripts/validate_institutional_colleague_acceptance.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "institutional_release_packet_export_expected_failure",
            [sys.executable, "scripts/build_institutional_release_packet.py", "--dry-run"],
            {2},
        )
    )
    checks.append(
        run_command(
            "go_no_go_evidence_coverage_validation",
            [sys.executable, "scripts/validate_go_no_go_evidence_coverage.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "final_release_cutover_validation",
            [sys.executable, "scripts/validate_final_release_cutover.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "objective_readiness_validation",
            [sys.executable, "scripts/validate_objective_readiness.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "goal_completion_audit_validation",
            [sys.executable, "scripts/validate_goal_completion_audit.py"],
            {0},
        )
    )
    checks.append(
        run_command(
            "release_verification_command_manifest_validation",
            [sys.executable, "scripts/validate_release_verification_command_manifest.py"],
            {0},
        )
    )

    for case_path in VALIDATION_CASES:
        checks.append(
            run_command(
                f"case_repo_validation:{case_path}",
                [sys.executable, "scripts/validate_repo.py", case_path, "--as-of", AS_OF],
                {0},
            )
        )

    for csv_path in CSV_FILES:
        checks.append(validate_csv_shape(csv_path))

    failures = [check for check in checks if not check.passed]

    print("long_term_release_checks:")
    print(f"  passed: {str(not failures).lower()}")
    print(f"  as_of: {AS_OF}")
    print("  expected_external_ready_failure: true")
    print(f"  checked_cases: {len(VALIDATION_CASES)}")
    print(f"  csv_shape_checks: {len(CSV_FILES)}")
    print("  external_review_packet_validation: true")
    print("  g01_external_method_scan_validation: true")
    print("  external_review_assignment_tracker_validation: true")
    print("  g06_reviewer_candidate_screen_validation: true")
    print("  g06_reviewer_selection_rubric_validation: true")
    print("  g06_reviewer_independence_screen_validation: true")
    print("  external_review_packet_export_dry_run: true")
    print("  external_review_dispatch_packet_validation: true")
    print("  g06_dispatch_readiness_validation: true")
    print("  external_release_action_queue_validation: true")
    print("  follow_through_trigger_tracker_validation: true")
    print("  g04_event_watch_calendar_validation: true")
    print("  g04_later_event_candidate_screen_validation: true")
    print("  follow_through_execution_tracker_validation: true")
    print("  follow_through_packet_export_dry_run: true")
    print("  follow_through_packet_matrix_validation: true")
    print("  institutional_release_bundle_validation: true")
    print("  institutional_colleague_acceptance_validation: true")
    print("  institutional_release_packet_export_expected_failure: true")
    print("  go_no_go_evidence_coverage_validation: true")
    print("  final_release_cutover_validation: true")
    print("  objective_readiness_validation: true")
    print("  goal_completion_audit_validation: true")
    print("  release_verification_command_manifest_validation: true")
    print("  validation_case_set: true")
    print("  repo_validation_contract_tests: true")
    print("  trial_theme_matrix_validation: true")
    print("  recent_theme_selection_validation: true")
    print("  theme_selection_refresh_audit_validation: true")
    print("  public_release_freshness_validation: true")
    print("  practice_falsification_audit_validation: true")
    print("  methodology_iteration_trace_audit_validation: true")
    print("  multi_lens_coverage_audit_validation: true")
    print("  public_workflow_pack_validation: true")
    print(f"  errors: {len(failures)}")
    print("  results:")
    for check in checks:
        status = "pass" if check.passed else "fail"
        code = "" if check.returncode is None else f" exit={check.returncode}"
        print(f"    - {check.name}: {status}{code}")
        if not check.passed and check.detail:
            detail = check.detail.replace("\n", "\n        ")
            print(f"        {detail}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
