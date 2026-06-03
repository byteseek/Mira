#!/usr/bin/env python3
"""Regression tests for long-term release validators.

The positive fixtures are synthetic and written to a temporary directory.
They must not be used as release evidence.
"""

from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_cmd(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


def assert_code(name: str, result: subprocess.CompletedProcess[str], expected: int) -> None:
    if result.returncode != expected:
        print(f"FAIL: {name}: expected exit {expected}, got {result.returncode}")
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(1)
    print(f"ok {name}")


def assert_contains(name: str, text: str, marker: str) -> None:
    if marker not in text:
        print(f"FAIL: {name}: missing marker `{marker}`")
        print(text)
        raise SystemExit(1)
    print(f"ok {name}")


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv_rows(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("rows must not be empty")
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_scorecard(path: Path) -> None:
    dimensions = [
        ("LLY_reproduction", "source_quality", "source trails reproduced", "No fix required."),
        ("LLY_reproduction", "lens_routing", "lens selection reproduced", "No fix required."),
        ("LLY_reproduction", "action_label_reproducibility", "action label reproduced", "No fix required."),
        ("LLY_reproduction", "valuation_discipline", "expectation map discipline accepted", "No fix required."),
        ("LLY_reproduction", "refresh_conditions", "refresh triggers are specific", "No fix required."),
        ("G04_follow_through", "g04_follow_through_readiness", "follow-through readiness controls are reviewable", "No fix required."),
        ("G04_follow_through", "g04_false_completion_control", "G04 readiness is not confused with completed refresh evidence", "No fix required."),
        ("recent_theme_selection", "theme_selection_freshness", "recent theme selection and refresh controls are reviewable", "No fix required."),
        ("practice_validation", "practice_falsification", "practice-falsification claims are case-grounded", "No fix required."),
        ("practice_validation", "methodology_iteration_traceability", "methodology iteration trace is case-grounded", "No fix required."),
        ("humanoid_handoff", "theme_to_company_handoff", "industry_map_first reproduced", "No fix required."),
        ("historical_backtest", "downgrade_timing", "downgrade timing caveated correctly", "No fix required."),
        ("overall", "workflow_cost_efficiency", "workflow value justifies added effort", "No fix required."),
        ("overall", "reviewer_release_recommendation", "release_with_caveats", "release_with_caveats"),
        ("G01_method_source", "g01_method_source_sufficiency", "public method-source basis accepted with caveats", "No fix required."),
        ("G01_method_source", "g01_private_buyside_gap_control", "private buyside gap is caveated", "No fix required."),
        ("G01_method_source", "g01_method_source_decision", "accept_with_caveats", "accept_with_caveats"),
        ("CRM_G05_source", "g05_source_sufficiency", "MarketScreener source accepted with caveats", "No fix required."),
        ("CRM_G05_source", "g05_false_precision_control", "modeled values stay separate", "No fix required."),
        ("CRM_G05_source", "g05_source_decision", "accept_with_caveats", "accept_with_caveats"),
        (
            "historical_consensus_exception",
            "historical_consensus_exception_sufficiency",
            "historical consensus exception accepted with caveats",
            "No fix required.",
        ),
        (
            "historical_consensus_exception",
            "historical_consensus_false_precision_control",
            "partial snippets are not labeled consensus",
            "No fix required.",
        ),
        (
            "historical_consensus_exception",
            "historical_consensus_exception_decision",
            "accept_with_caveats",
            "accept_with_caveats",
        ),
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "review_id",
                "reviewer",
                "review_date",
                "case_or_task",
                "dimension",
                "score_1_to_5",
                "minimum_release_score",
                "finding_severity",
                "evidence",
                "required_fix",
                "release_impact",
            ]
        )
        for idx, (case_or_task, dimension, evidence, required_fix) in enumerate(dimensions, start=1):
            writer.writerow(
                [
                    f"synthetic_{idx:02d}",
                    "synthetic_independent_reviewer_do_not_use",
                    "2026-06-15",
                    case_or_task,
                    dimension,
                    "4",
                    "4",
                    "P2",
                    evidence,
                    required_fix,
                    "caveat" if "caveat" in evidence else "none",
                ]
            )


def write_review_results(path: Path) -> None:
    path.write_text(
        """# External Review Results

- review_date: 2026-06-15
- reviewer_id: synthetic_independent_reviewer_do_not_use
- reviewer_independence_confirmed: true
- reviewed_pack_version_date: 2026-05-30
- review_status: complete
- release_recommendation: release_with_caveats

## Scorecard Summary

- average_score: 4
- minimum_score: 4
- p0_findings_count: 0
- p1_findings_count: 0
- g01_method_source_decision: accept_with_caveats
- g04_follow_through_readiness: accepted_with_caveats
- g04_false_completion_control: accepted_with_caveats
- theme_selection_freshness: accepted_with_caveats
- practice_falsification: accepted_with_caveats
- methodology_iteration_traceability: accepted_with_caveats
- g05_source_decision: accept_with_caveats
- historical_consensus_exception_decision: accept_with_caveats
- action_label_reproducibility: pass
- release_blockers_remaining: G04 still requires real follow-through evidence

## Findings

| severity | case_or_task | finding | evidence | required_fix | release_impact |
| --- | --- | --- | --- | --- | --- |
| P2 | CRM_G05_source | Use caveat for MarketScreener definition | scorecard | preserve caveat | caveat |

## Refresh Conditions

- stale_after: 2026-06-30
- must_refresh_if: actual reviewer return differs or G04 completes.
""",
        encoding="utf-8",
    )


def write_inconsistent_review_results(path: Path) -> None:
    write_review_results(path)
    text = path.read_text(encoding="utf-8")
    text = text.replace("- p1_findings_count: 0", "- p1_findings_count: 1")
    path.write_text(text, encoding="utf-8")


def write_intake(path: Path, prefix: str) -> None:
    rows = [
        ("01", "independence_confirmed", "Required condition met.", "pass", "Synthetic fixture."),
        ("02", "scorecard_completed", "Required condition met.", "pass", "Synthetic fixture."),
        ("03", "no_p0_findings", "Required condition met.", "pass", "Synthetic fixture."),
        ("04", "p1_fix_plan", "Required condition met.", "accepted", "Synthetic fixture."),
        ("05", "g01_method_source_decision", "Required condition met.", "pass", "Synthetic fixture."),
        ("06", "theme_selection_freshness", "Required condition met.", "pass", "Synthetic fixture."),
        ("07", "practice_falsification", "Required condition met.", "pass", "Synthetic fixture."),
        ("08", "methodology_iteration_traceability", "Required condition met.", "pass", "Synthetic fixture."),
        ("09", "g04_follow_through_results", "Required condition met.", "pass", "Synthetic fixture."),
        ("10", "g05_source_decision", "Required condition met.", "pass", "Synthetic fixture."),
        ("11", "historical_consensus_exception_decision", "Required condition met.", "pass", "Synthetic fixture."),
        ("12", "action_label_reproducibility", "Required condition met.", "pass", "Synthetic fixture."),
        ("13", "release_recommendation", "Required condition met.", "pass", "Synthetic fixture."),
        ("14", "results_memo_complete", "Required condition met.", "pass", "Synthetic fixture."),
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["check_id", "requirement", "pass_condition", "status", "notes"])
        for suffix, requirement, condition, status, notes in rows:
            writer.writerow([f"{prefix}_{suffix}", requirement, condition, status, notes])


def write_g06_assignment_tracker(path: Path, reviewer: str = "synthetic_independent_reviewer_do_not_use") -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "assignment_id",
                "gate_id",
                "packet_status",
                "reviewer_status",
                "independence_required",
                "assigned_reviewer",
                "assigned_date",
                "due_date",
                "packet_command",
                "return_validator_command",
                "current_status",
                "release_impact",
                "evidence_path",
                "next_action",
            ]
        )
        writer.writerow(
            [
                "G06_ASSIGN_SYNTHETIC",
                "G06",
                "packet_sent",
                "returned",
                "yes",
                reviewer,
                "2026-06-01",
                "2026-06-20",
                "python3 scripts/build_external_review_packet.py --output exports/mira-external-reviewer-packet",
                "python3 scripts/validate_external_review_return.py --scorecard PATH/TO/completed-external-reviewer-scorecard.csv --results PATH/TO/external-review-results-YYYY-MM-DD.md --intake PATH/TO/completed-external-review-intake-checklist.csv --assignment-tracker PATH/TO/g06-reviewer-assignment-tracker.csv --independence-screen PATH/TO/g06-reviewer-independence-screen.csv",
                "returned_not_validated",
                "blocks_external_release",
                "cases/long-term-workflow-validation-2026-05-30/g06-external-review-handoff-2026-05-30.md",
                "Validate returned materials.",
            ]
        )


def write_g06_independence_screen(path: Path) -> None:
    rows = [
        ("screen_01", "independence_boundary_defined", "independent Reviewer boundary disclosed.", "pass", "supports_assignment_ready"),
        ("screen_02", "conflict_screen_required", "Reviewer has no conflict.", "pass", "supports_assignment_ready"),
        ("screen_03", "capability_screen_required", "Reviewer can challenge workflow.", "pass", "supports_assignment_ready"),
        ("screen_04", "source_boundary_required", "Reviewer source boundary accepted.", "pass", "supports_assignment_ready"),
        ("screen_05", "reviewer_named_after_screen", "independent Reviewer is named after screen.", "pass", "blocks_external_release"),
        ("screen_06", "reviewer_attestation_returned", "independent Reviewer returned attestation.", "accepted", "blocks_external_release"),
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["check_id", "control", "pass_condition", "status", "evidence_path", "validator", "release_impact", "notes"])
        for check_id, control, pass_condition, status, release_impact in rows:
            writer.writerow(
                [
                    check_id,
                    control,
                    pass_condition,
                    status,
                    "synthetic",
                    "synthetic",
                    release_impact,
                    "Synthetic fixture.",
                ]
            )


def external_review_return_command(
    scorecard: Path,
    results: Path,
    intake: Path,
    assignment_tracker: Path,
    independence_screen: Path,
) -> list[str]:
    return [
        sys.executable,
        "scripts/validate_external_review_return.py",
        "--scorecard",
        str(scorecard),
        "--results",
        str(results),
        "--intake",
        str(intake),
        "--assignment-tracker",
        str(assignment_tracker),
        "--independence-screen",
        str(independence_screen),
    ]


def write_colleague_acceptance_checklist(path: Path) -> None:
    rows = [
        ("acceptance_01", "colleague_named", "Required condition met.", "pass", "colleague memo", "Synthetic fixture."),
        (
            "acceptance_02",
            "packet_used_without_live_author_context",
            "Required condition met.",
            "pass",
            "operator runbook",
            "Synthetic fixture.",
        ),
        ("acceptance_03", "one_case_reproduced", "Required condition met.", "pass", "case memo", "Synthetic fixture."),
        (
            "acceptance_04",
            "one_new_or_refresh_case_started",
            "Required condition met.",
            "accepted",
            "case memo",
            "Synthetic fixture.",
        ),
        (
            "acceptance_05",
            "source_gap_visibility_confirmed",
            "Required condition met.",
            "pass",
            "source appendix",
            "Synthetic fixture.",
        ),
        (
            "acceptance_06",
            "action_label_and_stop_rule_understood",
            "Required condition met.",
            "pass",
            "analyst checklist",
            "Synthetic fixture.",
        ),
        (
            "acceptance_07",
            "practice_falsification_understood",
            "Required condition met.",
            "pass",
            "practice audit",
            "Synthetic fixture.",
        ),
        (
            "acceptance_08",
            "methodology_iteration_traceability_understood",
            "Required condition met.",
            "pass",
            "iteration audit",
            "Synthetic fixture.",
        ),
        (
            "acceptance_09",
            "acceptance_memo_signed",
            "Required condition met.",
            "accepted",
            "colleague memo",
            "Synthetic fixture.",
        ),
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["check_id", "requirement", "pass_condition", "status", "evidence_path", "notes"])
        writer.writerows(rows)


def write_colleague_acceptance_memo(path: Path) -> None:
    path.write_text(
        """# Institutional Colleague Acceptance Memo

- acceptance_date: 2026-06-20
- colleague_id: synthetic_colleague_do_not_use
- colleague_role: institutional_equity_analyst
- used_live_author_context: false
- packet_version_date: 2026-05-30
- reproduced_case_id: LLY_2026
- reproduced_action_label: watch_only_pending_payer_access_and_expectation_map_refresh
- new_or_refresh_case_id: synthetic_new_case_started
- source_gap_visibility: accepted_with_caveats
- action_label_stop_rule_understood: accepted_with_caveats
- practice_falsification_understood: accepted_with_caveats
- methodology_iteration_traceability: accepted_with_caveats
- release_recommendation: release_with_caveats

## Evidence Used

- packet files used: workflow, fill guide, source appendix, analyst checklist
- reproduced case evidence: LLY evidence log and expectation map
- new or refresh case started: synthetic new case fixture
- source-gap evidence: source appendix and source-gap refresh template
- stop-rule evidence: analyst checklist

## Residual Caveats

Keep G04/G06 caveats visible until the actual release gates clear.

## Required Fixes

owner: release owner; fix: preserve residual caveats in final release notes.

## Refresh Conditions

- stale_after: 2026-07-20
- must_refresh_if: colleague disputes action label, G04 refresh changes, reviewer return changes or source definitions change.
""",
        encoding="utf-8",
    )


def write_g04_intake(path: Path) -> None:
    rows = [
        ("01", "later_event", "Required condition met.", "pass", "Synthetic fixture."),
        ("02", "material_variable", "Required condition met.", "pass", "Synthetic fixture."),
        ("03", "new_source_evidence", "Required condition met.", "pass", "Synthetic fixture."),
        ("04", "before_after_action_label", "Required condition met.", "pass", "Synthetic fixture."),
        ("05", "trigger_quality_evaluated", "Required condition met.", "pass", "Synthetic fixture."),
        ("06", "result_label_valid", "Required condition met.", "pass", "Synthetic fixture."),
        ("07", "public_grade_impact", "Required condition met.", "pass", "Synthetic fixture."),
        ("08", "downstream_logs_updated", "Required condition met.", "accepted", "Synthetic fixture."),
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["check_id", "requirement", "pass_condition", "status", "notes"])
        for suffix, requirement, condition, status, notes in rows:
            writer.writerow([f"g04_{suffix}", requirement, condition, status, notes])


def write_follow_through(path: Path) -> None:
    path.write_text(
        """# Follow-Through Refresh

- case_id: SYNTHETIC_CRM_2026_DO_NOT_USE
- ticker: CRM
- refresh_date: 2026-08-28
- original_memo_date: 2026-05-30
- original_action_label: watch_only_pending_product_monetization_map
- refreshed_action_label: watch_only_pending_product_monetization_map
- qualifies_as_true_follow_through: yes

## Qualification Check

| requirement | answer | evidence |
| --- | --- | --- |
| Event occurred after original memo cutoff | yes | Synthetic event dated 2026-08-28. |
| Event is material to named thesis variable | yes | Product monetization and valuation expectations. |
| New source evidence added | yes | synthetic_crm_q2_2027_release. |
| Before/after action label stated | yes | Labels appear in header. |
| Original refresh trigger evaluated | yes | Trigger was specific enough. |

## Original Thesis State

- weakest_lens: product_monetization
- strongest_evidence: Agentforce ARR
- biggest_source_gap: total-company monetization bridge
- valuation_burden: material
- stop_rule: watch-only until product monetization bridge improves

## New Event Evidence

| source_id | source_type | source_date | claim_supported | link_or_path | confidence |
| --- | --- | --- | --- | --- | --- |
| synthetic_crm_q2_2027_release | company_release | 2026-08-28 | Product metric update | synthetic fixture | high |

## Before / After

| thesis_variable | before | after | change | actionability_impact |
| --- | --- | --- | --- | --- |
| product_monetization | source_gap | partial_evidence | improved | action unchanged |

## Refresh Trigger Quality

Was the original `must_refresh_if`:

- specific enough

Explanation:

Synthetic fixture says the original trigger was specific enough.

## Decision

Refresh result label:

- `thesis_strengthened_action_unchanged`

## Public-Grade Impact

- follow_through_gate_status: pass
- reviewer_needed: yes
- remaining_source_gaps: external reviewer still required

## Next Refresh Conditions

- stale_after: 2026-09-30
- must_refresh_if: next material product monetization update occurs.
""",
        encoding="utf-8",
    )


def write_evidence_log(path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["source_id", "source_date", "claim_text"])
        writer.writerow(["synthetic_crm_q2_2027_release", "2026-08-28", "Synthetic later-event source."])


def write_mismatched_evidence_log(path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["source_id", "source_date", "claim_text"])
        writer.writerow(["different_later_source", "2026-08-28", "Synthetic later-event source."])


def write_g04_gate_tracker(path: Path, refresh: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "gate_id",
                "gate",
                "required_for_external_release",
                "current_status",
                "evidence_path",
                "remaining_blocker",
                "next_action",
                "owner_type",
            ]
        )
        writer.writerow(
            [
                "G04",
                "true_follow_through_refresh",
                "yes",
                "pass_external",
                str(refresh),
                "Synthetic fixture only.",
                "Continue external validation.",
                "event_dependent",
            ]
        )


def write_g04_public_readiness(path: Path, refresh: Path) -> None:
    path.write_text(
        f"""# Synthetic Public Readiness Audit

- case_id: SYNTHETIC_CRM_2026_DO_NOT_USE
- refresh_file: {refresh.name}
- follow_through_gate_status: pass
- refresh_result: thesis_strengthened_action_unchanged
""",
        encoding="utf-8",
    )


def write_g04_review_log(path: Path, refresh: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "method_name",
                "review_date",
                "validation_mode",
                "case_or_scope",
                "result",
                "what_worked",
                "what_failed",
                "keep_change_or_retire",
                "notes",
            ]
        )
        writer.writerow(
            [
                "long-term-integrated-thesis",
                "2026-08-28",
                "g04_follow_through_refresh",
                "SYNTHETIC_CRM_2026_DO_NOT_USE",
                "positive_partial",
                "Synthetic G04 true follow-through row.",
                "External reviewer still required.",
                "keep_under_trial",
                f"G04 true follow-through refresh {refresh.name} selected thesis_strengthened_action_unchanged.",
            ]
        )


def run_positive_fixtures(tmp: Path) -> None:
    scorecard = tmp / "scorecard.csv"
    results = tmp / "results.md"
    review_intake = tmp / "review-intake.csv"
    refresh = tmp / "follow-through-refresh.md"
    evidence_log = tmp / "evidence-log.csv"
    g04_intake = tmp / "g04-intake.csv"
    g04_gate_tracker = tmp / "public-release-gate-tracker.csv"
    g04_public_readiness = tmp / "public-readiness-audit.md"
    g04_review_log = tmp / "review-log.csv"
    g06_assignment_tracker = tmp / "g06-reviewer-assignment-tracker.csv"
    g06_independence_screen = tmp / "g06-reviewer-independence-screen.csv"

    write_scorecard(scorecard)
    write_review_results(results)
    write_intake(review_intake, "intake")
    write_follow_through(refresh)
    write_evidence_log(evidence_log)
    write_g04_intake(g04_intake)
    write_g04_gate_tracker(g04_gate_tracker, refresh)
    write_g04_public_readiness(g04_public_readiness, refresh)
    write_g04_review_log(g04_review_log, refresh)
    write_g06_assignment_tracker(g06_assignment_tracker)
    write_g06_independence_screen(g06_independence_screen)

    clean_review_return = run_cmd(
        external_review_return_command(scorecard, results, review_intake, g06_assignment_tracker, g06_independence_screen)
    )
    assert_code("synthetic external review return clears validator", clean_review_return, 0)
    assert_contains(
        "synthetic external review return checks selection rubric",
        clean_review_return.stdout,
        "rubric_decisions_checked: 11",
    )
    assert_contains(
        "synthetic external review return checks reviewer assignment chain",
        clean_review_return.stdout,
        "assignment_independence_checked: 2",
    )

    mismatched_assignment = tmp / "mismatched-g06-reviewer-assignment-tracker.csv"
    write_g06_assignment_tracker(mismatched_assignment, reviewer="different_reviewer")
    reviewer_mismatch = run_cmd(
        external_review_return_command(scorecard, results, review_intake, mismatched_assignment, g06_independence_screen)
    )
    assert_code("external review return rejects assignment reviewer mismatch", reviewer_mismatch, 1)
    assert_contains(
        "external review return names assignment reviewer mismatch",
        reviewer_mismatch.stdout,
        "assigned_reviewer does not match completed scorecard reviewer",
    )

    selection_rubric_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-selection-rubric.csv"
    original_selection_rubric = selection_rubric_path.read_text(encoding="utf-8")
    try:
        selection_rubric_path.write_text(
            original_selection_rubric.replace(",workflow_cost_efficiency,", ",missing_workflow_cost_efficiency,", 1),
            encoding="utf-8",
        )
        invalid_rubric_return = run_cmd(
            external_review_return_command(scorecard, results, review_intake, g06_assignment_tracker, g06_independence_screen)
        )
        assert_code("external review return rejects rubric scorecard gap", invalid_rubric_return, 1)
        assert_contains(
            "external review return names rubric scorecard gap",
            invalid_rubric_return.stdout,
            "scorecard_dimension missing from completed scorecard",
        )
    finally:
        selection_rubric_path.write_text(original_selection_rubric, encoding="utf-8")
    missing_iteration_results = tmp / "missing-iteration-results.md"
    write_review_results(missing_iteration_results)
    missing_iteration_text = missing_iteration_results.read_text(encoding="utf-8")
    missing_iteration_text = missing_iteration_text.replace(
        "- methodology_iteration_traceability: accepted_with_caveats\n",
        "",
    )
    missing_iteration_results.write_text(missing_iteration_text, encoding="utf-8")
    missing_iteration = run_cmd(
        external_review_return_command(
            scorecard,
            missing_iteration_results,
            review_intake,
            g06_assignment_tracker,
            g06_independence_screen,
        )
    )
    assert_code("synthetic external review return rejects missing iteration trace result", missing_iteration, 1)
    assert_contains(
        "external review missing iteration trace result is named",
        missing_iteration.stdout,
        "methodology_iteration_traceability does not clear G06",
    )

    p1_scorecard = tmp / "p1-scorecard.csv"
    write_scorecard(p1_scorecard)
    p1_scorecard_rows = read_csv_rows(p1_scorecard)
    p1_scorecard_rows[0]["finding_severity"] = "P1"
    p1_scorecard_rows[0]["required_fix"] = "owner: methodology owner; fix: strengthen source trail."
    p1_scorecard_rows[0]["release_impact"] = "caveat"
    write_csv_rows(p1_scorecard, p1_scorecard_rows)

    p1_results = tmp / "p1-results.md"
    write_review_results(p1_results)
    p1_results_text = p1_results.read_text(encoding="utf-8")
    p1_results_text = p1_results_text.replace("- p1_findings_count: 0", "- p1_findings_count: 1")
    p1_results_text = p1_results_text.replace(
        "| P2 | CRM_G05_source | Use caveat for MarketScreener definition | scorecard | preserve caveat | caveat |",
        (
            "| P1 | LLY_reproduction | Source trail needs clearer owner | scorecard row synthetic_01 | "
            "owner: methodology owner; fix: strengthen source trail. | caveat |\n"
            "| P2 | CRM_G05_source | Use caveat for MarketScreener definition | scorecard | preserve caveat | caveat |"
        ),
    )
    p1_results.write_text(p1_results_text, encoding="utf-8")
    assert_code(
        "synthetic external review return allows P1 with owner fix",
        run_cmd(
            external_review_return_command(
                p1_scorecard,
                p1_results,
                review_intake,
                g06_assignment_tracker,
                g06_independence_screen,
            )
        ),
        0,
    )

    hidden_p1_results = tmp / "hidden-p1-results.md"
    write_review_results(hidden_p1_results)
    hidden_p1_text = hidden_p1_results.read_text(encoding="utf-8")
    hidden_p1_text = hidden_p1_text.replace("- p1_findings_count: 0", "- p1_findings_count: 1")
    hidden_p1_results.write_text(hidden_p1_text, encoding="utf-8")
    hidden_p1 = run_cmd(
        external_review_return_command(
            p1_scorecard,
            hidden_p1_results,
            review_intake,
            g06_assignment_tracker,
            g06_independence_screen,
        )
    )
    assert_code("synthetic external review return rejects memo hiding P1 finding", hidden_p1, 1)
    assert_contains(
        "external review memo P1 count mismatch is named",
        hidden_p1.stdout,
        "findings table P1 count does not match summary",
    )

    vague_p1_results = tmp / "vague-p1-results.md"
    write_review_results(vague_p1_results)
    vague_p1_results_text = vague_p1_results.read_text(encoding="utf-8")
    vague_p1_results_text = vague_p1_results_text.replace("- p1_findings_count: 0", "- p1_findings_count: 1")
    vague_p1_results_text = vague_p1_results_text.replace(
        "| P2 | CRM_G05_source | Use caveat for MarketScreener definition | scorecard | preserve caveat | caveat |",
        (
            "| P1 | LLY_reproduction | Source trail needs clearer owner | scorecard row synthetic_01 | "
            "Needs fix | caveat |\n"
            "| P2 | CRM_G05_source | Use caveat for MarketScreener definition | scorecard | preserve caveat | caveat |"
        ),
    )
    vague_p1_results.write_text(vague_p1_results_text, encoding="utf-8")
    vague_p1_memo = run_cmd(
        external_review_return_command(
            p1_scorecard,
            vague_p1_results,
            review_intake,
            g06_assignment_tracker,
            g06_independence_screen,
        )
    )
    assert_code("synthetic external review return rejects vague P1 memo fix", vague_p1_memo, 1)
    assert_contains(
        "external review memo P1 owner requirement is named",
        vague_p1_memo.stdout,
        "findings row 1 P1 required_fix missing owner:",
    )
    assert_contains(
        "external review memo P1 fix requirement is named",
        vague_p1_memo.stdout,
        "findings row 1 P1 required_fix missing fix:",
    )

    invalid_severity_scorecard = tmp / "invalid-severity-scorecard.csv"
    write_scorecard(invalid_severity_scorecard)
    invalid_rows = invalid_severity_scorecard.read_text(encoding="utf-8")
    invalid_rows = invalid_rows.replace(",P2,", ",P9,", 1)
    invalid_severity_scorecard.write_text(invalid_rows, encoding="utf-8")
    invalid_severity = run_cmd(
        external_review_return_command(
            invalid_severity_scorecard,
            results,
            review_intake,
            g06_assignment_tracker,
            g06_independence_screen,
        )
    )
    assert_code("synthetic external review return rejects invalid severity", invalid_severity, 1)
    assert_contains(
        "external review invalid severity is named",
        invalid_severity.stdout,
        "invalid finding_severity",
    )

    vague_p1_scorecard = tmp / "vague-p1-scorecard.csv"
    write_scorecard(vague_p1_scorecard)
    vague_rows = vague_p1_scorecard.read_text(encoding="utf-8")
    vague_rows = vague_rows.replace(
        ",P2,source trails reproduced,No fix required.,none",
        ",P1,source trails reproduced,Needs fix,caveat",
        1,
    )
    vague_p1_scorecard.write_text(vague_rows, encoding="utf-8")
    vague_p1 = run_cmd(
        external_review_return_command(
            vague_p1_scorecard,
            results,
            review_intake,
            g06_assignment_tracker,
            g06_independence_screen,
        )
    )
    assert_code("synthetic external review return rejects P1 without owner fix", vague_p1, 1)
    assert_contains(
        "external review P1 owner requirement is named",
        vague_p1.stdout,
        "P1 finding required_fix missing owner:",
    )
    assert_contains(
        "external review P1 fix requirement is named",
        vague_p1.stdout,
        "P1 finding required_fix missing fix:",
    )

    mismatched_reviewer_results = tmp / "mismatched-reviewer-results.md"
    write_review_results(mismatched_reviewer_results)
    mismatched_text = mismatched_reviewer_results.read_text(encoding="utf-8")
    mismatched_text = mismatched_text.replace(
        "- reviewer_id: synthetic_independent_reviewer_do_not_use",
        "- reviewer_id: different_reviewer",
    )
    mismatched_reviewer_results.write_text(mismatched_text, encoding="utf-8")
    mismatched_reviewer = run_cmd(
        external_review_return_command(
            scorecard,
            mismatched_reviewer_results,
            review_intake,
            g06_assignment_tracker,
            g06_independence_screen,
        )
    )
    assert_code("synthetic external review return rejects reviewer mismatch", mismatched_reviewer, 1)
    assert_contains(
        "external review reviewer mismatch names inconsistent field",
        mismatched_reviewer.stdout,
        "reviewer_id does not match scorecard reviewer",
    )

    incomplete_intake = tmp / "incomplete-intake.csv"
    with incomplete_intake.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["check_id", "requirement", "pass_condition", "status", "notes"])
        writer.writerow(["intake_01", "independence_confirmed", "Required condition met.", "pass", "Synthetic fixture."])
    incomplete = run_cmd(
        external_review_return_command(
            scorecard,
            results,
            incomplete_intake,
            g06_assignment_tracker,
            g06_independence_screen,
        )
    )
    assert_code("synthetic external review return rejects incomplete intake", incomplete, 1)
    assert_contains(
        "external review incomplete intake names missing requirements",
        incomplete.stdout,
        "missing requirements",
    )

    inconsistent_results = tmp / "inconsistent-results.md"
    write_inconsistent_review_results(inconsistent_results)
    inconsistent = run_cmd(
        external_review_return_command(
            scorecard,
            inconsistent_results,
            review_intake,
            g06_assignment_tracker,
            g06_independence_screen,
        )
    )
    assert_code("synthetic external review return rejects memo-scorecard mismatch", inconsistent, 1)
    assert_contains(
        "external review mismatch names inconsistent field",
        inconsistent.stdout,
        "p1_findings_count does not match scorecard",
    )
    clean_follow_through = run_cmd(
        [
            sys.executable,
            "scripts/validate_follow_through_refresh.py",
            "--refresh",
            str(refresh),
            "--original-cutoff",
            "2026-05-30",
            "--evidence-log",
            str(evidence_log),
            "--intake",
            str(g04_intake),
            "--gate-tracker",
            str(g04_gate_tracker),
            "--public-readiness-audit",
            str(g04_public_readiness),
            "--review-log",
            str(g04_review_log),
        ]
    )
    assert_code(
        "synthetic follow-through refresh clears validator",
        clean_follow_through,
        0,
    )
    assert_contains(
        "synthetic follow-through checks downstream release updates",
        clean_follow_through.stdout,
        "downstream_updates_checked: 3",
    )

    stale_public_readiness = tmp / "stale-public-readiness-audit.md"
    stale_public_readiness.write_text(
        "# Synthetic Public Readiness Audit\n\n- case_id: SYNTHETIC_CRM_2026_DO_NOT_USE\n",
        encoding="utf-8",
    )
    missing_downstream = run_cmd(
        [
            sys.executable,
            "scripts/validate_follow_through_refresh.py",
            "--refresh",
            str(refresh),
            "--original-cutoff",
            "2026-05-30",
            "--evidence-log",
            str(evidence_log),
            "--intake",
            str(g04_intake),
            "--gate-tracker",
            str(g04_gate_tracker),
            "--public-readiness-audit",
            str(stale_public_readiness),
            "--review-log",
            str(g04_review_log),
        ]
    )
    assert_code("synthetic follow-through rejects stale downstream audit", missing_downstream, 1)
    assert_contains(
        "follow-through downstream audit gap is named",
        missing_downstream.stdout,
        "public readiness audit missing",
    )
    mismatched_evidence_log = tmp / "mismatched-evidence-log.csv"
    write_mismatched_evidence_log(mismatched_evidence_log)
    mismatched_follow = run_cmd(
        [
            sys.executable,
            "scripts/validate_follow_through_refresh.py",
            "--refresh",
            str(refresh),
            "--original-cutoff",
            "2026-05-30",
            "--evidence-log",
            str(mismatched_evidence_log),
            "--intake",
            str(g04_intake),
        ]
    )
    assert_code("synthetic follow-through rejects missing evidence-log source id", mismatched_follow, 1)
    assert_contains(
        "follow-through mismatch names missing source ids",
        mismatched_follow.stdout,
        "refresh source_ids missing from evidence log later-event rows",
    )

    weak_refresh = tmp / "weak-follow-through-refresh.md"
    write_follow_through(weak_refresh)
    weak_text = weak_refresh.read_text(encoding="utf-8").replace(
        "| Event is material to named thesis variable | yes | Product monetization and valuation expectations. |",
        "| Event is material to named thesis variable | no | Product monetization and valuation expectations. |",
    )
    weak_refresh.write_text(weak_text, encoding="utf-8")
    weak_follow = run_cmd(
        [
            sys.executable,
            "scripts/validate_follow_through_refresh.py",
            "--refresh",
            str(weak_refresh),
            "--original-cutoff",
            "2026-05-30",
            "--evidence-log",
            str(evidence_log),
            "--intake",
            str(g04_intake),
        ]
    )
    assert_code("synthetic follow-through rejects non-material qualification", weak_follow, 1)
    assert_contains(
        "follow-through non-material qualification is named",
        weak_follow.stdout,
        "must answer yes",
    )

    multi_label_refresh = tmp / "multi-label-follow-through-refresh.md"
    write_follow_through(multi_label_refresh)
    multi_label_text = multi_label_refresh.read_text(encoding="utf-8").replace(
        "- `thesis_strengthened_action_unchanged`",
        "- `thesis_strengthened_action_unchanged`\n- `thesis_weakened_action_downgraded`",
    )
    multi_label_refresh.write_text(multi_label_text, encoding="utf-8")
    multi_label = run_cmd(
        [
            sys.executable,
            "scripts/validate_follow_through_refresh.py",
            "--refresh",
            str(multi_label_refresh),
            "--original-cutoff",
            "2026-05-30",
            "--evidence-log",
            str(evidence_log),
            "--intake",
            str(g04_intake),
        ]
    )
    assert_code("synthetic follow-through rejects multiple result labels", multi_label, 1)
    assert_contains(
        "follow-through multiple result labels are named",
        multi_label.stdout,
        "must select exactly one approved refresh result label",
    )

    wrong_cutoff_refresh = tmp / "wrong-cutoff-follow-through-refresh.md"
    write_follow_through(wrong_cutoff_refresh)
    wrong_cutoff_text = wrong_cutoff_refresh.read_text(encoding="utf-8").replace(
        "- original_memo_date: 2026-05-30",
        "- original_memo_date: 2026-05-31",
    )
    wrong_cutoff_refresh.write_text(wrong_cutoff_text, encoding="utf-8")
    wrong_cutoff = run_cmd(
        [
            sys.executable,
            "scripts/validate_follow_through_refresh.py",
            "--refresh",
            str(wrong_cutoff_refresh),
            "--original-cutoff",
            "2026-05-30",
            "--evidence-log",
            str(evidence_log),
            "--intake",
            str(g04_intake),
        ]
    )
    assert_code("synthetic follow-through rejects original cutoff mismatch", wrong_cutoff, 1)
    assert_contains(
        "follow-through cutoff mismatch is named",
        wrong_cutoff.stdout,
        "does not match cutoff",
    )

    stale_window_refresh = tmp / "stale-window-follow-through-refresh.md"
    write_follow_through(stale_window_refresh)
    stale_window_text = stale_window_refresh.read_text(encoding="utf-8").replace(
        "- stale_after: 2026-09-30",
        "- stale_after: 2026-08-28",
    )
    stale_window_refresh.write_text(stale_window_text, encoding="utf-8")
    stale_window = run_cmd(
        [
            sys.executable,
            "scripts/validate_follow_through_refresh.py",
            "--refresh",
            str(stale_window_refresh),
            "--original-cutoff",
            "2026-05-30",
            "--evidence-log",
            str(evidence_log),
            "--intake",
            str(g04_intake),
        ]
    )
    assert_code("synthetic follow-through rejects stale window at refresh date", stale_window, 1)
    assert_contains(
        "follow-through stale window is named",
        stale_window.stdout,
        "stale_after 2026-08-28 is not after refresh_date 2026-08-28",
    )

    incomplete_g04_intake = tmp / "incomplete-g04-intake.csv"
    with incomplete_g04_intake.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["check_id", "requirement", "pass_condition", "status", "notes"])
        writer.writerow(["g04_01", "later_event", "Required condition met.", "pass", "Synthetic fixture."])
    incomplete_g04 = run_cmd(
        [
            sys.executable,
            "scripts/validate_follow_through_refresh.py",
            "--refresh",
            str(refresh),
            "--original-cutoff",
            "2026-05-30",
            "--evidence-log",
            str(evidence_log),
            "--intake",
            str(incomplete_g04_intake),
        ]
    )
    assert_code("synthetic follow-through rejects incomplete G04 intake", incomplete_g04, 1)
    assert_contains(
        "follow-through incomplete G04 intake names missing requirements",
        incomplete_g04.stdout,
        "missing requirements",
    )


def run_packet_builder_fixtures(tmp: Path) -> None:
    external_output = tmp / "external-reviewer-packet"
    external_result = run_cmd(
        [
            sys.executable,
            "scripts/build_external_review_packet.py",
            "--output",
            str(external_output),
        ]
    )
    assert_code("external reviewer packet builder exports", external_result, 0)
    assert_contains("external reviewer packet builder reports send count", external_result.stdout, "send_items: 37")
    external_manifest = external_output / "reviewer-packet-export-manifest.csv"
    if not external_manifest.exists():
        print("FAIL: external reviewer packet export manifest missing")
        raise SystemExit(1)
    external_rows = read_csv_rows(external_manifest)
    blocked_fragments = [
        "public-readiness-audit.md",
        "public-release-gate-tracker.csv",
        "public-release-decision.md",
        "ordinary-vs-workflow-comparison.md",
        "long-term-methodology-2026-05-30/methodology-card.md",
    ]
    exported_sources = "\n".join(row.get("source_path", "") for row in external_rows)
    exported_manifest_paths = "\n".join(row.get("manifest_path", "") for row in external_rows)
    assert_contains(
        "external reviewer packet includes G04 later-event candidate screen",
        exported_manifest_paths,
        "g04-later-event-candidate-screen.csv",
    )
    assert_contains(
        "external reviewer packet includes G04 later-event validator",
        exported_manifest_paths,
        "validate_g04_later_event_candidate_screen.py",
    )
    assert_contains(
        "external reviewer packet includes recent theme selection validator",
        exported_manifest_paths,
        "validate_recent_theme_selection.py",
    )
    assert_contains(
        "external reviewer packet includes G06 selection rubric",
        exported_manifest_paths,
        "g06-reviewer-selection-rubric.csv",
    )
    for fragment in blocked_fragments:
        if fragment in exported_sources:
            print(f"FAIL: external reviewer packet exported internal file: {fragment}")
            raise SystemExit(1)
    print("ok external reviewer packet excludes internal files")

    dirty_external_output = tmp / "dirty-external-output"
    dirty_external_output.mkdir()
    (dirty_external_output / "existing.txt").write_text("occupied", encoding="utf-8")
    assert_code(
        "external reviewer packet builder rejects non-empty output",
        run_cmd(
            [
                sys.executable,
                "scripts/build_external_review_packet.py",
                "--output",
                str(dirty_external_output),
            ]
        ),
        1,
    )

    follow_output = tmp / "follow-through-packet"
    follow_result = run_cmd(
        [
            sys.executable,
            "scripts/build_follow_through_packet.py",
            "--output",
            str(follow_output),
        ]
    )
    assert_code("follow-through packet builder exports", follow_result, 0)
    assert_contains("follow-through packet defaults to CRM", follow_result.stdout, "selected_case: CRM_2026")
    follow_summary = follow_output / "follow-through-packet-summary.md"
    if not follow_summary.exists():
        print("FAIL: follow-through packet summary missing")
        raise SystemExit(1)
    summary_text = follow_summary.read_text(encoding="utf-8")
    assert_contains("follow-through packet preserves G04 boundary", summary_text, "This packet does not clear G04 by itself.")
    assert_contains(
        "follow-through packet summary requires later-event screen validator",
        summary_text,
        "validate_g04_later_event_candidate_screen.py",
    )
    assert_contains(
        "follow-through packet summary requires refresh allowed boundary",
        summary_text,
        "refresh_allowed: yes",
    )
    assert_contains(
        "follow-through packet summary requires downstream release updates",
        summary_text,
        "--public-readiness-audit",
    )
    follow_manifest = follow_output / "follow-through-packet-export-manifest.csv"
    follow_rows = read_csv_rows(follow_manifest)
    if len(follow_rows) != 19:
        print("FAIL: follow-through packet manifest should contain 19 rows")
        raise SystemExit(1)
    print("ok follow-through packet manifest row count")
    exported_follow_sources = "\n".join(row.get("source_path", "") for row in follow_rows)
    assert_contains(
        "follow-through packet includes event watch calendar",
        exported_follow_sources,
        "g04-follow-through-event-watch-calendar.csv",
    )
    assert_contains(
        "follow-through packet includes later-event candidate screen",
        exported_follow_sources,
        "g04-later-event-candidate-screen.csv",
    )
    assert_contains(
        "follow-through packet includes later-event candidate validator",
        exported_follow_sources,
        "validate_g04_later_event_candidate_screen.py",
    )

    explicit_vrt_output = tmp / "follow-through-packet-vrt"
    explicit_vrt_result = run_cmd(
        [
            sys.executable,
            "scripts/build_follow_through_packet.py",
            "--case-id",
            "VRT_2026",
            "--output",
            str(explicit_vrt_output),
        ]
    )
    assert_code("follow-through packet supports explicit VRT override", explicit_vrt_result, 0)
    assert_contains("follow-through packet explicit VRT selected", explicit_vrt_result.stdout, "selected_case: VRT_2026")

    dirty_follow_output = tmp / "dirty-follow-output"
    dirty_follow_output.mkdir()
    (dirty_follow_output / "existing.txt").write_text("occupied", encoding="utf-8")
    assert_code(
        "follow-through packet builder rejects non-empty output",
        run_cmd(
            [
                sys.executable,
                "scripts/build_follow_through_packet.py",
                "--output",
                str(dirty_follow_output),
            ]
        ),
        1,
    )

    institutional_dry_run = run_cmd(
        [
            sys.executable,
            "scripts/build_institutional_release_packet.py",
            "--dry-run",
        ]
    )
    assert_code("institutional release packet builder refuses while external-ready is false", institutional_dry_run, 2)
    assert_contains("institutional release packet dry-run counts release items", institutional_dry_run.stdout, "release_items: 40")
    assert_contains(
        "institutional release packet dry-run checks required exports",
        institutional_dry_run.stdout,
        "required_export_paths_checked: 40",
    )

    institutional_manifest = ROOT / "cases/long-term-workflow-validation-2026-05-30/institutional-release-bundle-manifest.csv"
    original_manifest = institutional_manifest.read_text(encoding="utf-8")
    try:
        institutional_manifest.write_text(
            original_manifest
            + "core_pack,../long-term-methodology-2026-05-30/methodology-card.md,yes,yes,external_release_only,"
            + '"malicious path escape fixture."\n',
            encoding="utf-8",
        )
        escaped_manifest = run_cmd([sys.executable, "scripts/validate_institutional_release_bundle.py"])
        assert_code("institutional release bundle rejects included path escape", escaped_manifest, 1)
        assert_contains(
            "institutional release bundle path escape is named",
            escaped_manifest.stdout,
            "included path escapes validation directory",
        )
    finally:
        institutional_manifest.write_text(original_manifest, encoding="utf-8")


def run_negative_fixtures() -> None:
    assert_code(
        "blank external review template is rejected",
        run_cmd(
            [
                sys.executable,
                "scripts/validate_external_review_return.py",
                "--scorecard",
                "cases/long-term-workflow-validation-2026-05-30/public-workflow-pack/external-reviewer-scorecard.csv",
                "--results",
                "cases/long-term-workflow-validation-2026-05-30/public-workflow-pack/external-review-results-template.md",
                "--intake",
                "cases/long-term-workflow-validation-2026-05-30/public-workflow-pack/external-review-intake-checklist.csv",
                "--assignment-tracker",
                "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-assignment-tracker.csv",
                "--independence-screen",
                "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-independence-screen.csv",
            ]
        ),
        1,
    )
    assert_code(
        "blank follow-through template is rejected",
        run_cmd(
            [
                sys.executable,
                "scripts/validate_follow_through_refresh.py",
                "--refresh",
                "templates/follow-through-refresh.md",
                "--original-cutoff",
                "2026-05-30",
                "--intake",
                "cases/long-term-workflow-validation-2026-05-30/g04-follow-through-intake-checklist.csv",
            ]
        ),
        1,
    )


def run_current_state_guardrails() -> None:
    dispatch = run_cmd([sys.executable, "scripts/validate_external_review_dispatch_packet.py"])
    assert_code("external review dispatch packet is ready but not clear", dispatch, 0)
    assert_contains("external review dispatch does not clear G06", dispatch.stdout, "clears_g06: false")
    assert_contains("external review dispatch has no assigned reviewer", dispatch.stdout, "reviewer_assigned: false")

    g06_dispatch = run_cmd([sys.executable, "scripts/validate_g06_dispatch_readiness.py"])
    assert_code("G06 dispatch readiness passes but stays incomplete", g06_dispatch, 0)
    assert_contains("G06 dispatch readiness has pending external blockers", g06_dispatch.stdout, "pending_external: 2")
    assert_contains("G06 dispatch readiness does not clear G06", g06_dispatch.stdout, "clears_g06: false")

    g06_screen = run_cmd([sys.executable, "scripts/validate_g06_reviewer_independence_screen.py"])
    assert_code("G06 reviewer independence screen passes but stays incomplete", g06_screen, 0)
    assert_contains("G06 reviewer independence screen has pending external blockers", g06_screen.stdout, "pending_external: 2")
    assert_contains("G06 reviewer independence screen does not clear G06", g06_screen.stdout, "clears_g06: false")

    candidate_screen = run_cmd([sys.executable, "scripts/validate_g06_reviewer_candidate_screen.py"])
    assert_code("G06 reviewer candidate screen passes but stays incomplete", candidate_screen, 0)
    assert_contains("G06 reviewer candidate screen has pending candidate", candidate_screen.stdout, "pending_candidate_selection: 3")
    assert_contains("G06 reviewer candidate screen checks profiles", candidate_screen.stdout, "candidate_profiles_checked: 3")
    assert_contains("G06 reviewer candidate screen has no selected reviewer", candidate_screen.stdout, "selected_assigned: 0")
    assert_contains("G06 reviewer candidate screen does not clear G06", candidate_screen.stdout, "clears_g06: false")

    selection_rubric = run_cmd([sys.executable, "scripts/validate_g06_reviewer_selection_rubric.py"])
    assert_code("G06 reviewer selection rubric passes but does not clear G06", selection_rubric, 0)
    assert_contains("G06 reviewer selection rubric checks decisions", selection_rubric.stdout, "decisions_checked: 11")
    assert_contains("G06 reviewer selection rubric checks profiles", selection_rubric.stdout, "profiles_checked: 11")
    assert_contains(
        "G06 reviewer selection rubric checks scorecard dimensions",
        selection_rubric.stdout,
        "scorecard_dimensions_checked: 11",
    )
    assert_contains("G06 reviewer selection rubric does not clear G06", selection_rubric.stdout, "clears_g06: false")

    candidate_screen_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-candidate-screen.csv"
    original_candidate_screen = candidate_screen_path.read_text(encoding="utf-8")
    try:
        candidate_screen_path.write_text(
            original_candidate_screen.replace("pending_candidate_selection", "selected_assigned", 1),
            encoding="utf-8",
        )
        premature_candidate = run_cmd([sys.executable, "scripts/validate_g06_reviewer_candidate_screen.py"])
        assert_code("G06 reviewer candidate screen rejects premature selected candidate", premature_candidate, 1)
        assert_contains(
            "G06 reviewer candidate screen names missing reviewer",
            premature_candidate.stdout,
            "selected_assigned requires named reviewer",
        )
    finally:
        candidate_screen_path.write_text(original_candidate_screen, encoding="utf-8")

    try:
        candidate_screen_path.write_text(
            original_candidate_screen.replace("source_quality_valuation_reviewer", "unsupported_reviewer", 1),
            encoding="utf-8",
        )
        missing_profile_candidate = run_cmd([sys.executable, "scripts/validate_g06_reviewer_candidate_screen.py"])
        assert_code("G06 reviewer candidate screen rejects missing required profile", missing_profile_candidate, 1)
        assert_contains(
            "G06 reviewer candidate screen names missing required profile",
            missing_profile_candidate.stdout,
            "missing required candidate profiles",
        )
    finally:
        candidate_screen_path.write_text(original_candidate_screen, encoding="utf-8")

    selection_rubric_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-selection-rubric.csv"
    original_selection_rubric = selection_rubric_path.read_text(encoding="utf-8")
    try:
        selection_rubric_path.write_text(
            original_selection_rubric.replace("methodology_iteration_traceability", "missing_iteration_traceability", 1),
            encoding="utf-8",
        )
        invalid_selection_rubric = run_cmd([sys.executable, "scripts/validate_g06_reviewer_selection_rubric.py"])
        assert_code("G06 reviewer selection rubric rejects missing required decision", invalid_selection_rubric, 1)
        assert_contains(
            "G06 reviewer selection rubric names missing decision",
            invalid_selection_rubric.stdout,
            "missing required decisions",
        )
    finally:
        selection_rubric_path.write_text(original_selection_rubric, encoding="utf-8")

    assignment_tracker = run_cmd([sys.executable, "scripts/validate_external_review_assignment_tracker.py"])
    assert_code("G06 assignment tracker passes with screen-row cross-checks", assignment_tracker, 0)
    assert_contains("G06 assignment tracker checks screen rows", assignment_tracker.stdout, "screen_rows_checked: 2")
    assert_contains("G06 assignment tracker checks candidate rows", assignment_tracker.stdout, "candidate_rows_checked: 3")

    independence_screen_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-independence-screen.csv"
    original_independence_screen = independence_screen_path.read_text(encoding="utf-8")
    try:
        independence_screen_path.write_text(
            original_independence_screen.replace(
                "screen_05,reviewer_named_after_screen,"
                '"A specific independent Reviewer is named with assigned_date and due_date only after the independence screen is accepted.",pending_external,',
                "screen_05,reviewer_named_after_screen,"
                '"A specific independent Reviewer is named with assigned_date and due_date only after the independence screen is accepted.",pass,',
            ),
            encoding="utf-8",
        )
        conflicting_assignment = run_cmd([sys.executable, "scripts/validate_external_review_assignment_tracker.py"])
        assert_code("G06 assignment tracker rejects premature screen_05 pass", conflicting_assignment, 1)
        assert_contains(
            "G06 assignment tracker names premature screen_05",
            conflicting_assignment.stdout,
            "ready assignment requires screen_05 pending_external",
        )
    finally:
        independence_screen_path.write_text(original_independence_screen, encoding="utf-8")

    assignment_tracker_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-assignment-tracker.csv"
    candidate_screen_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/g06-reviewer-candidate-screen.csv"
    original_assignment_tracker = assignment_tracker_path.read_text(encoding="utf-8")
    original_candidate_screen = candidate_screen_path.read_text(encoding="utf-8")
    try:
        assignment_rows = read_csv_rows(assignment_tracker_path)
        assignment_rows[0]["packet_status"] = "packet_sent"
        assignment_rows[0]["reviewer_status"] = "validated"
        assignment_rows[0]["assigned_reviewer"] = "synthetic_reviewer"
        assignment_rows[0]["assigned_date"] = "2026-06-01"
        assignment_rows[0]["due_date"] = "2026-06-20"
        assignment_rows[0]["current_status"] = "validated_completed"
        assignment_rows[0]["release_impact"] = "supports_external_release"
        write_csv_rows(assignment_tracker_path, assignment_rows)

        independence_rows = read_csv_rows(independence_screen_path)
        for row in independence_rows:
            if row["check_id"] == "screen_05":
                row["status"] = "pass"
            if row["check_id"] == "screen_06":
                row["status"] = "accepted"
        write_csv_rows(independence_screen_path, independence_rows)

        candidate_rows = read_csv_rows(candidate_screen_path)
        candidate_rows[0]["candidate_status"] = "selected_assigned"
        candidate_rows[0]["reviewer_name"] = "synthetic_reviewer"
        candidate_rows[0]["conflict_check"] = "pass"
        candidate_rows[0]["authorship_check"] = "pass"
        candidate_rows[0]["incentive_check"] = "pass"
        candidate_rows[0]["capability_check"] = "pass"
        candidate_rows[0]["source_boundary_ack"] = "pass"
        candidate_rows[0]["assigned_in_tracker"] = "yes"
        write_csv_rows(candidate_screen_path, candidate_rows)

        invalid_completed_assignment = run_cmd([sys.executable, "scripts/validate_external_review_assignment_tracker.py"])
        assert_code("G06 assignment tracker rejects completed state without results memo", invalid_completed_assignment, 1)
        assert_contains(
            "G06 assignment tracker names missing results memo",
            invalid_completed_assignment.stdout,
            "completed state must point to external review results memo",
        )
    finally:
        assignment_tracker_path.write_text(original_assignment_tracker, encoding="utf-8")
        independence_screen_path.write_text(original_independence_screen, encoding="utf-8")
        candidate_screen_path.write_text(original_candidate_screen, encoding="utf-8")

    packet_matrix = run_cmd([sys.executable, "scripts/validate_follow_through_packet_matrix.py"])
    assert_code("G04 packet matrix validates all tracked live cases", packet_matrix, 0)
    assert_contains("G04 packet matrix checks four cases", packet_matrix.stdout, "packet_ready_cases: 4")
    assert_contains("G04 packet matrix checks default case", packet_matrix.stdout, "default_case_checked: true")

    execution_tracker = run_cmd([sys.executable, "scripts/validate_follow_through_execution_tracker.py"])
    assert_code("G04 execution tracker passes with support-row cross-checks", execution_tracker, 0)
    assert_contains("G04 execution tracker checks support rows", execution_tracker.stdout, "support_rows_checked: 4")
    assert_contains("G04 execution tracker checks candidate rows", execution_tracker.stdout, "candidate_rows_checked: 4")

    later_event_screen = run_cmd([sys.executable, "scripts/validate_g04_later_event_candidate_screen.py"])
    assert_code("G04 later-event candidate screen passes current not-ready state", later_event_screen, 0)
    assert_contains("G04 later-event screen checks scheduled event", later_event_screen.stdout, "scheduled_future_events: 1")
    assert_contains("G04 later-event screen has no available event", later_event_screen.stdout, "later_event_available: 0")
    assert_contains("G04 later-event screen does not clear G04", later_event_screen.stdout, "clears_g04: false")

    later_event_screen_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/g04-later-event-candidate-screen.csv"
    original_later_event_screen = later_event_screen_path.read_text(encoding="utf-8")
    try:
        later_event_screen_path.write_text(
            original_later_event_screen.replace(
                "LLY_2026,LLY,2026-05-30,Q2 2026 earnings,2026-08-05,scheduled_future_event,yes,scheduled_official_ir,pending_event_materials,no,no,ready_to_execute_waiting_event,",
                "LLY_2026,LLY,2026-05-30,Q2 2026 earnings,2026-08-05,scheduled_future_event,yes,scheduled_official_ir,pending_event_materials,yes,yes,ready_to_execute_waiting_event,",
                1,
            ),
            encoding="utf-8",
        )
        premature_event = run_cmd([sys.executable, "scripts/validate_g04_later_event_candidate_screen.py"])
        assert_code("G04 later-event screen rejects scheduled event selected for refresh", premature_event, 1)
        assert_contains(
            "G04 later-event screen names scheduled-event violation",
            premature_event.stdout,
            "scheduled future event cannot be selected before materials publish",
        )
    finally:
        later_event_screen_path.write_text(original_later_event_screen, encoding="utf-8")

    trigger_tracker_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/follow-through-trigger-tracker.csv"
    original_trigger_tracker = trigger_tracker_path.read_text(encoding="utf-8")
    try:
        trigger_tracker_path.write_text(
            original_trigger_tracker.replace(",high,waiting_for_later_event,", ",high,refresh_completed,", 1),
            encoding="utf-8",
        )
        conflicting_execution = run_cmd([sys.executable, "scripts/validate_follow_through_execution_tracker.py"])
        assert_code("G04 execution tracker rejects trigger status conflict", conflicting_execution, 1)
        assert_contains(
            "G04 execution tracker names trigger conflict",
            conflicting_execution.stdout,
            "trigger tracker status conflicts with waiting execution",
        )
    finally:
        trigger_tracker_path.write_text(original_trigger_tracker, encoding="utf-8")

    case_set = run_cmd([sys.executable, "scripts/validate_validation_case_set.py"])
    assert_code("validation case set passes non-recursive validator", case_set, 0)
    assert_contains("validation case set checks ten cases", case_set.stdout, "checked_cases: 10")

    theme_matrix = run_cmd([sys.executable, "scripts/validate_trial_theme_matrix.py", "--as-of", "2026-05-30"])
    assert_code("trial theme matrix passes source-linked validator", theme_matrix, 0)
    assert_contains("trial theme matrix checks seven themes", theme_matrix.stdout, "themes: 7")
    assert_contains("trial theme matrix checks source ids", theme_matrix.stdout, "source_ids_checked:")

    theme_refresh = run_cmd([sys.executable, "scripts/validate_theme_selection_refresh_audit.py", "--as-of", "2026-05-30"])
    assert_code("theme selection refresh audit passes freshness validator", theme_refresh, 0)
    assert_contains("theme selection refresh audit checks seven themes", theme_refresh.stdout, "themes: 7")
    assert_contains(
        "theme selection refresh audit checks replacement rules",
        theme_refresh.stdout,
        "replacement_rules_checked: 7",
    )

    release_freshness = run_cmd([sys.executable, "scripts/validate_public_release_freshness.py", "--as-of", "2026-05-30"])
    assert_code("public release freshness validator passes current materials", release_freshness, 0)
    assert_contains("public release freshness checks concrete docs", release_freshness.stdout, "concrete_documents_checked: 15")
    assert_contains("public release freshness checks templates", release_freshness.stdout, "template_documents_checked: 4")

    source_appendix_freshness_path = (
        ROOT / "cases/long-term-workflow-validation-2026-05-30/public-workflow-pack/source-appendix.md"
    )
    original_source_appendix_for_freshness = source_appendix_freshness_path.read_text(encoding="utf-8")
    try:
        source_appendix_freshness_path.write_text(
            original_source_appendix_for_freshness.replace("- stale_after: 2026-06-30", "- stale_after: 2026-05-30", 1),
            encoding="utf-8",
        )
        stale_release_freshness = run_cmd(
            [sys.executable, "scripts/validate_public_release_freshness.py", "--as-of", "2026-05-30"]
        )
        assert_code("public release freshness rejects stale public appendix", stale_release_freshness, 1)
        assert_contains(
            "public release freshness names stale public appendix",
            stale_release_freshness.stdout,
            "stale_after must be after as_of 2026-05-30",
        )
    finally:
        source_appendix_freshness_path.write_text(original_source_appendix_for_freshness, encoding="utf-8")

    theme_refresh_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/theme-selection-refresh-audit.csv"
    original_theme_refresh = theme_refresh_path.read_text(encoding="utf-8")
    try:
        theme_refresh_path.write_text(
            original_theme_refresh.replace("2026-06-30,etn_2026q1_8k_ex99", "2026-05-30,etn_2026q1_8k_ex99", 1),
            encoding="utf-8",
        )
        stale_theme_refresh = run_cmd([sys.executable, "scripts/validate_theme_selection_refresh_audit.py", "--as-of", "2026-05-30"])
        assert_code("theme selection refresh audit rejects stale-after boundary", stale_theme_refresh, 1)
        assert_contains(
            "theme selection refresh audit names stale_after boundary",
            stale_theme_refresh.stdout,
            "stale_after must be after selection_date",
        )
    finally:
        theme_refresh_path.write_text(original_theme_refresh, encoding="utf-8")

    recent_theme = run_cmd([sys.executable, "scripts/validate_recent_theme_selection.py", "--as-of", "2026-05-30"])
    assert_code("recent theme selection composite validator passes", recent_theme, 0)
    assert_contains("recent theme selection composite checks component count", recent_theme.stdout, "component_checks: 2")
    assert_contains("recent theme selection composite checks replacement rules", recent_theme.stdout, "replacement_rules_checked: 7")

    practice_audit = run_cmd([sys.executable, "scripts/validate_practice_falsification_audit.py", "--as-of", "2026-05-30"])
    assert_code("practice falsification audit passes case-grounded validator", practice_audit, 0)
    assert_contains("practice falsification audit checks eight claims", practice_audit.stdout, "claims: 8")
    assert_contains("practice falsification audit checks case links", practice_audit.stdout, "case_links_checked: 39")

    iteration_trace = run_cmd(
        [sys.executable, "scripts/validate_methodology_iteration_trace_audit.py", "--as-of", "2026-05-30"]
    )
    assert_code("methodology iteration trace audit passes case-grounded validator", iteration_trace, 0)
    assert_contains("methodology iteration trace audit checks twelve iterations", iteration_trace.stdout, "iterations: 12")
    assert_contains(
        "methodology iteration trace audit checks patch artifacts",
        iteration_trace.stdout,
        "patch_artifacts_checked: 21",
    )

    lens_audit = run_cmd([sys.executable, "scripts/validate_multi_lens_coverage_audit.py", "--as-of", "2026-05-30"])
    assert_code("multi-lens coverage audit passes case-grounded validator", lens_audit, 0)
    assert_contains("multi-lens coverage audit checks six lenses", lens_audit.stdout, "lenses: 6")
    assert_contains("multi-lens coverage audit checks case links", lens_audit.stdout, "case_links_checked: 26")

    iteration_trace_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/methodology-iteration-trace-audit.csv"
    original_iteration_trace = iteration_trace_path.read_text(encoding="utf-8")
    try:
        iteration_trace_path.write_text(
            original_iteration_trace.replace(
                "downgraded_from_broad_bullish_to_watch_only",
                "observed_broad_bullish_watch_only",
                1,
            ),
            encoding="utf-8",
        )
        weak_iteration_trace = run_cmd(
            [sys.executable, "scripts/validate_methodology_iteration_trace_audit.py", "--as-of", "2026-05-30"]
        )
        assert_code("methodology iteration trace audit rejects weak decision effect", weak_iteration_trace, 1)
        assert_contains(
            "methodology iteration trace audit names actionability impact",
            weak_iteration_trace.stdout,
            "decision_effect must show actionability impact",
        )
    finally:
        iteration_trace_path.write_text(original_iteration_trace, encoding="utf-8")

    lens_audit_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/multi-lens-coverage-audit.csv"
    original_lens_audit = lens_audit_path.read_text(encoding="utf-8")
    try:
        lens_audit_path.write_text(
            original_lens_audit.replace(
                "payer_access_pull_forward_and_hardware_demand_changed_actionability",
                "payer_access_pull_forward_and_hardware_demand_observed",
                1,
            ),
            encoding="utf-8",
        )
        weak_lens_audit = run_cmd([sys.executable, "scripts/validate_multi_lens_coverage_audit.py", "--as-of", "2026-05-30"])
        assert_code("multi-lens coverage audit rejects missing decision delta", weak_lens_audit, 1)
        assert_contains(
            "multi-lens coverage audit names decision delta",
            weak_lens_audit.stdout,
            "decision_delta must show actionability or stop-rule change",
        )
    finally:
        lens_audit_path.write_text(original_lens_audit, encoding="utf-8")

    practice_audit_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/practice-falsification-audit.csv"
    original_practice_audit = practice_audit_path.read_text(encoding="utf-8")
    try:
        practice_audit_path.write_text(
            original_practice_audit.replace(
                "Reject the claim if case validation fails",
                "Accept the claim if case validation fails",
                1,
            ),
            encoding="utf-8",
        )
        weak_practice_audit = run_cmd(
            [sys.executable, "scripts/validate_practice_falsification_audit.py", "--as-of", "2026-05-30"]
        )
        assert_code("practice falsification audit rejects non-falsifiable claim", weak_practice_audit, 1)
        assert_contains(
            "practice falsification audit names missing rejection condition",
            weak_practice_audit.stdout,
            "falsification_test must state a rejection condition",
        )
    finally:
        practice_audit_path.write_text(original_practice_audit, encoding="utf-8")

    public_pack = run_cmd([sys.executable, "scripts/validate_public_workflow_pack.py"])
    assert_code("public workflow pack passes overlay validator", public_pack, 0)
    assert_contains("public workflow pack checks overlays", public_pack.stdout, "overlays_checked: 11")
    assert_contains("public workflow pack checks source sections", public_pack.stdout, "source_sections_checked: 10")

    pack_readme_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/public-workflow-pack/README.md"
    original_pack_readme = pack_readme_path.read_text(encoding="utf-8")
    try:
        pack_readme_path.write_text(
            original_pack_readme.replace("Seven-theme direction scan", "Four-theme direction scan", 1),
            encoding="utf-8",
        )
        stale_pack = run_cmd([sys.executable, "scripts/validate_public_workflow_pack.py"])
        assert_code("public workflow pack rejects stale theme count", stale_pack, 1)
        assert_contains(
            "public workflow pack names stale four-theme wording",
            stale_pack.stdout,
            "README still says Four-theme direction scan",
        )
    finally:
        pack_readme_path.write_text(original_pack_readme, encoding="utf-8")

    source_appendix_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/public-workflow-pack/source-appendix.md"
    original_source_appendix = source_appendix_path.read_text(encoding="utf-8")
    try:
        source_appendix_path.write_text(
            original_source_appendix.replace("### Stablecoin Payments", "### Stablecoin Payments Removed", 1),
            encoding="utf-8",
        )
        missing_source_section = run_cmd([sys.executable, "scripts/validate_public_workflow_pack.py"])
        assert_code("public workflow pack rejects missing source trail section", missing_source_section, 1)
        assert_contains(
            "public workflow pack names missing stablecoin source section",
            missing_source_section.stdout,
            "missing source-trail section `### Stablecoin Payments`",
        )
    finally:
        source_appendix_path.write_text(original_source_appendix, encoding="utf-8")

    cutover = run_cmd([sys.executable, "scripts/validate_final_release_cutover.py"])
    assert_code("final cutover validator passes current not-ready state", cutover, 0)
    assert_contains("final cutover remains not ready", cutover.stdout, "cutover_ready: false")
    assert_contains("final cutover checks thirteen rows", cutover.stdout, "checks: 13")
    assert_contains("final cutover has no signed go memo", cutover.stdout, "go_memo_present: false")

    coverage = run_cmd([sys.executable, "scripts/validate_go_no_go_evidence_coverage.py"])
    assert_code("go/no-go evidence coverage validator passes current mapping", coverage, 0)
    assert_contains("go/no-go coverage checks all required gates", coverage.stdout, "required_gates_checked: 11")
    assert_contains("go/no-go coverage checks all evidence rows", coverage.stdout, "evidence_rows_checked: 15")

    go_no_go_template_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/external-release-go-no-go-template.md"
    original_go_no_go_template = go_no_go_template_path.read_text(encoding="utf-8")
    try:
        go_no_go_template_path.write_text(
            original_go_no_go_template.replace(
                "| ordinary-vs-workflow delta | reviewer accepts or caveats actionability delta versus ordinary memo | pending | replace |",
                "| ordinary-vs-workflow delta removed | reviewer accepts or caveats actionability delta versus ordinary memo | pending | replace |",
                1,
            ),
            encoding="utf-8",
        )
        stale_coverage = run_cmd([sys.executable, "scripts/validate_go_no_go_evidence_coverage.py"])
        assert_code("go/no-go evidence coverage rejects missing required row", stale_coverage, 1)
        assert_contains(
            "go/no-go coverage names missing ordinary-vs-workflow row",
            stale_coverage.stdout,
            "missing go/no-go evidence row: | ordinary-vs-workflow delta |",
        )
    finally:
        go_no_go_template_path.write_text(original_go_no_go_template, encoding="utf-8")

    colleague_acceptance = run_cmd([sys.executable, "scripts/validate_institutional_colleague_acceptance.py"])
    assert_code("institutional colleague acceptance passes current pending state", colleague_acceptance, 0)
    assert_contains("institutional colleague acceptance remains not ready", colleague_acceptance.stdout, "acceptance_ready: false")
    assert_contains("institutional colleague acceptance checks nine rows", colleague_acceptance.stdout, "checks: 9")
    assert_contains(
        "institutional colleague acceptance checks no return memos in pending state",
        colleague_acceptance.stdout,
        "return_memos_checked: 0",
    )

    colleague_acceptance_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/institutional-colleague-acceptance-checklist.csv"
    original_colleague_acceptance = colleague_acceptance_path.read_text(encoding="utf-8")
    try:
        colleague_acceptance_path.write_text(
            original_colleague_acceptance.replace(",pending,", ",pass,", 9),
            encoding="utf-8",
        )
        premature_acceptance = run_cmd([sys.executable, "scripts/validate_institutional_colleague_acceptance.py"])
        assert_code("institutional colleague acceptance rejects premature all-pass", premature_acceptance, 1)
        assert_contains(
            "institutional colleague acceptance names external-ready conflict",
            premature_acceptance.stdout,
            "all acceptance checks pass while external-ready validator fails",
        )
    finally:
        colleague_acceptance_path.write_text(original_colleague_acceptance, encoding="utf-8")

    premature_colleague_memo_path = (
        ROOT
        / "cases/long-term-workflow-validation-2026-05-30/institutional-colleague-acceptance-2099-12-30.md"
    )
    original_premature_colleague_memo = (
        premature_colleague_memo_path.read_text(encoding="utf-8") if premature_colleague_memo_path.exists() else None
    )
    try:
        write_colleague_acceptance_memo(premature_colleague_memo_path)
        premature_colleague_memo_text = premature_colleague_memo_path.read_text(encoding="utf-8")
        premature_colleague_memo_text = premature_colleague_memo_text.replace(
            "- methodology_iteration_traceability: accepted_with_caveats",
            "- methodology_iteration_traceability: fail",
        )
        premature_colleague_memo_path.write_text(premature_colleague_memo_text, encoding="utf-8")
        weak_colleague_acceptance = run_cmd([sys.executable, "scripts/validate_institutional_colleague_acceptance.py"])
        assert_code("institutional colleague acceptance rejects weak dated memo", weak_colleague_acceptance, 1)
        assert_contains(
            "institutional colleague acceptance chains to return validator",
            weak_colleague_acceptance.stdout,
            "acceptance return validator failed",
        )
        assert_contains(
            "institutional colleague acceptance surfaces weak traceability",
            weak_colleague_acceptance.stdout,
            "methodology_iteration_traceability does not clear acceptance",
        )
        assert_contains(
            "institutional colleague acceptance counts checked return memo",
            weak_colleague_acceptance.stdout,
            "return_memos_checked: 1",
        )
    finally:
        if original_premature_colleague_memo is None:
            premature_colleague_memo_path.unlink(missing_ok=True)
        else:
            premature_colleague_memo_path.write_text(original_premature_colleague_memo, encoding="utf-8")

    with tempfile.TemporaryDirectory(prefix="mira-colleague-return-") as colleague_tmp:
        colleague_tmp_path = Path(colleague_tmp)
        colleague_return_checklist = colleague_tmp_path / "colleague-acceptance-checklist.csv"
        colleague_return_memo = colleague_tmp_path / "institutional-colleague-acceptance-2026-06-20.md"
        write_colleague_acceptance_checklist(colleague_return_checklist)
        write_colleague_acceptance_memo(colleague_return_memo)
        colleague_return = run_cmd(
            [
                sys.executable,
                "scripts/validate_institutional_colleague_acceptance_return.py",
                "--checklist",
                str(colleague_return_checklist),
                "--memo",
                str(colleague_return_memo),
            ]
        )
        assert_code("synthetic colleague acceptance return clears validator", colleague_return, 0)
        assert_contains("colleague return checks nine rows", colleague_return.stdout, "checks: 9")
        assert_contains(
            "colleague return reports methodology traceability",
            colleague_return.stdout,
            "methodology_iteration_traceability: accepted_with_caveats",
        )

        weak_colleague_memo = colleague_tmp_path / "institutional-colleague-acceptance-2026-06-21.md"
        write_colleague_acceptance_memo(weak_colleague_memo)
        weak_colleague_text = weak_colleague_memo.read_text(encoding="utf-8")
        weak_colleague_text = weak_colleague_text.replace(
            "- methodology_iteration_traceability: accepted_with_caveats",
            "- methodology_iteration_traceability: fail",
        )
        weak_colleague_memo.write_text(weak_colleague_text, encoding="utf-8")
        weak_colleague_return = run_cmd(
            [
                sys.executable,
                "scripts/validate_institutional_colleague_acceptance_return.py",
                "--checklist",
                str(colleague_return_checklist),
                "--memo",
                str(weak_colleague_memo),
            ]
        )
        assert_code("colleague acceptance return rejects failed iteration traceability", weak_colleague_return, 1)
        assert_contains(
            "colleague return names methodology traceability failure",
            weak_colleague_return.stdout,
            "methodology_iteration_traceability does not clear acceptance",
        )

    go_memo_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/external-release-go-no-go-2099-12-31.md"
    original_go_memo = go_memo_path.read_text(encoding="utf-8") if go_memo_path.exists() else None
    try:
        go_memo_path.write_text(
            """# External Release Go/No-Go Memo

- decision_date: 2099-12-31
- methodology: `long-term-integrated-thesis`
- release_status: ready_external_release
- release_owner: replace
- decision: go

## Required Evidence

| gate | required evidence | status | evidence path |
| --- | --- | --- | --- |
| G04 true follow-through | completed qualifying later-event refresh | pending | replace |
| G06 external reviewer | completed scorecard, results memo and intake checklist | pending | replace |

## Validator Output

```text
paste final validator output here
```

## Refresh Conditions

- stale_after: YYYY-MM-DD
- must_refresh_if: replace
""",
            encoding="utf-8",
        )
        premature_go = run_cmd([sys.executable, "scripts/validate_final_release_cutover.py"])
        assert_code("final cutover rejects premature go memo", premature_go, 1)
        assert_contains(
            "final cutover names premature go decision",
            premature_go.stdout,
            "go/no-go memo says go while external-ready validator fails",
        )
        assert_contains(
            "final cutover rejects placeholder owner",
            premature_go.stdout,
            "release_owner is placeholder",
        )
        assert_contains(
            "final cutover requires colleague acceptance evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed institutional colleague acceptance evidence row",
        )
        assert_contains(
            "final cutover requires live case evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed live case evidence row",
        )
        assert_contains(
            "final cutover requires G01 evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed G01 evidence row",
        )
        assert_contains(
            "final cutover requires theme selection evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed theme selection evidence row",
        )
        assert_contains(
            "final cutover requires practice falsification evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed practice falsification evidence row",
        )
        assert_contains(
            "final cutover requires methodology iteration evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed methodology iteration evidence row",
        )
        assert_contains(
            "final cutover requires ordinary-vs-workflow evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed ordinary-vs-workflow evidence row",
        )
        assert_contains(
            "final cutover requires template completeness evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed template completeness evidence row",
        )
        assert_contains(
            "final cutover requires G05 evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed G05 evidence row",
        )
        assert_contains(
            "final cutover requires public source-quality evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed public source-quality evidence row",
        )
        assert_contains(
            "final cutover requires historical consensus evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed historical consensus evidence row",
        )
        assert_contains(
            "final cutover requires operational loop evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed operational loop evidence row",
        )
        assert_contains(
            "final cutover requires release validator evidence row",
            premature_go.stdout,
            "go/no-go memo missing passed release validator evidence row",
        )
    finally:
        if original_go_memo is None:
            go_memo_path.unlink(missing_ok=True)
        else:
            go_memo_path.write_text(original_go_memo, encoding="utf-8")

    objective = run_cmd([sys.executable, "scripts/validate_objective_readiness.py"])
    assert_code("objective readiness validator passes current incomplete state", objective, 0)
    assert_contains("objective remains incomplete", objective.stdout, "objective_complete: false")
    assert_contains("objective has three blockers", objective.stdout, "blocking: 3")
    assert_contains("objective executes all verification commands", objective.stdout, "verification_commands_checked: 10")
    assert_contains(
        "objective checks institutional required export paths",
        objective.stdout,
        "institutional_export_paths_checked: 40",
    )

    goal = run_cmd([sys.executable, "scripts/validate_goal_completion_audit.py"])
    assert_code("goal completion audit passes current incomplete state", goal, 0)
    assert_contains("goal remains incomplete", goal.stdout, "goal_complete: false")
    assert_contains("goal has three external blockers", goal.stdout, "blocked_external: 3")
    assert_contains("goal executes all verification commands", goal.stdout, "verification_commands_checked: 10")
    assert_contains(
        "goal checks institutional required export paths",
        goal.stdout,
        "institutional_export_paths_checked: 40",
    )

    command_manifest = run_cmd([sys.executable, "scripts/validate_release_verification_command_manifest.py"])
    assert_code("release verification command manifest passes current expected exits", command_manifest, 0)
    assert_contains("release verification command manifest reports external-ready false", command_manifest.stdout, "external_ready: false")
    assert_contains("release verification command manifest executes commands", command_manifest.stdout, "commands_executed: 12")
    assert_contains("release verification command manifest checks runbook coverage", command_manifest.stdout, "runbook_commands_checked: 12")
    assert_contains(
        "release verification command manifest checks expected failures",
        command_manifest.stdout,
        "expected_failures_checked: 2",
    )

    operator_runbook_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/public-workflow-pack/operator-runbook.md"
    original_operator_runbook = operator_runbook_path.read_text(encoding="utf-8")
    try:
        operator_runbook_path.write_text(
            original_operator_runbook.replace("python3 scripts/validate_go_no_go_evidence_coverage.py", "", 1),
            encoding="utf-8",
        )
        stale_command_manifest = run_cmd([sys.executable, "scripts/validate_release_verification_command_manifest.py"])
        assert_code("release verification command manifest rejects runbook drift", stale_command_manifest, 1)
        assert_contains(
            "release verification command manifest names missing runbook command",
            stale_command_manifest.stdout,
            "runbook missing manifest command `python3 scripts/validate_go_no_go_evidence_coverage.py`",
        )
    finally:
        operator_runbook_path.write_text(original_operator_runbook, encoding="utf-8")

    command_manifest_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/release-verification-command-manifest.csv"
    original_command_manifest = command_manifest_path.read_text(encoding="utf-8")
    try:
        command_manifest_path.write_text(
            original_command_manifest.replace(
                "cmd_02,python3 scripts/validate_long_term_release.py --require-external-ready,2,",
                "cmd_02,python3 scripts/validate_long_term_release.py --require-external-ready,0,",
                1,
            ),
            encoding="utf-8",
        )
        invalid_expected_exit = run_cmd([sys.executable, "scripts/validate_release_verification_command_manifest.py"])
        assert_code("release verification command manifest rejects premature external-ready expected exit", invalid_expected_exit, 1)
        assert_contains(
            "release verification command manifest names premature expected exit",
            invalid_expected_exit.stdout,
            "external blocker command must currently have nonzero expected exit while external_ready is false",
        )
    finally:
        command_manifest_path.write_text(original_command_manifest, encoding="utf-8")

    action_queue = run_cmd([sys.executable, "scripts/validate_external_release_action_queue.py"])
    assert_code("external release action queue passes current blocker state", action_queue, 0)
    assert_contains("external release action queue reports external-ready false", action_queue.stdout, "external_ready: false")
    assert_contains("external release action queue checks six actions", action_queue.stdout, "actions: 6")
    assert_contains("external release action queue checks G04 actions", action_queue.stdout, "g04_actions: 4")
    assert_contains("external release action queue checks G06 actions", action_queue.stdout, "g06_actions: 2")
    assert_contains("external release action queue executes commands", action_queue.stdout, "commands_executed: 6")
    assert_contains(
        "external release action queue checks completion commands",
        action_queue.stdout,
        "completion_commands_checked: 6",
    )

    action_queue_path = ROOT / "cases/long-term-workflow-validation-2026-05-30/external-release-action-queue.csv"
    original_action_queue = action_queue_path.read_text(encoding="utf-8")
    try:
        action_queue_path.write_text(
            original_action_queue.replace(",no,blocks_external_release,", ",yes,blocks_external_release,", 1),
            encoding="utf-8",
        )
        invalid_action_queue = run_cmd([sys.executable, "scripts/validate_external_release_action_queue.py"])
        assert_code("external release action queue rejects internal completion", invalid_action_queue, 1)
        assert_contains(
            "external release action queue names internal completion violation",
            invalid_action_queue.stdout,
            "external blocker cannot be internally completed",
        )
    finally:
        action_queue_path.write_text(original_action_queue, encoding="utf-8")

    try:
        action_queue_path.write_text(
            original_action_queue.replace("scripts/validate_follow_through_refresh.py", "scripts/validate_g04_event_watch_calendar.py", 1),
            encoding="utf-8",
        )
        invalid_completion_queue = run_cmd([sys.executable, "scripts/validate_external_release_action_queue.py"])
        assert_code("external release action queue rejects weak G04 completion command", invalid_completion_queue, 1)
        assert_contains(
            "external release action queue names weak G04 completion command",
            invalid_completion_queue.stdout,
            "G04 completion must use validate_follow_through_refresh.py",
        )
    finally:
        action_queue_path.write_text(original_action_queue, encoding="utf-8")


def main() -> int:
    assert_code(
        "release validator internal candidate",
        run_cmd([sys.executable, "scripts/validate_long_term_release.py"]),
        0,
    )
    assert_code(
        "external-ready check fails while gates are open",
        run_cmd([sys.executable, "scripts/validate_long_term_release.py", "--require-external-ready"]),
        2,
    )
    run_current_state_guardrails()
    run_negative_fixtures()
    with tempfile.TemporaryDirectory(prefix="mira-validator-fixtures-") as tmp_dir:
        tmp = Path(tmp_dir)
        run_positive_fixtures(tmp)
        run_packet_builder_fixtures(tmp)
    print("validator_regression_tests: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
