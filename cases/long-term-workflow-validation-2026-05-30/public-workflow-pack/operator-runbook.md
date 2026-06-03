# Operator Runbook

- methodology: `long-term-integrated-thesis`
- pack_status: candidate_internal_release
- external_release_status: not_ready_external_release
- objective_complete: false
- prepared_date: 2026-05-30
- stale_after: 2026-06-30
- must_refresh_if: G04 or G06 status changes, a live validation case has a later material event, reviewer findings arrive, or release gate status changes

## Current Boundary

Use this runbook to execute the internal candidate workflow, assign external review and prepare a future release packet.

Do not distribute a final institutional release package while:

- `G04` true follow-through refresh is incomplete;
- `G06` external independent review is incomplete;
- `python3 scripts/validate_long_term_release.py --require-external-ready` exits nonzero;
- `python3 scripts/validate_objective_readiness.py` reports `objective_complete: false`.

## Standard Analyst Case

1. Confirm research object, market scope, time boundary and thesis horizon.
2. Route through `loops/analysis-routing.md`.
3. For a long-term thesis, use `loops/long-term-thesis-loop.md`.
4. Create the required case files:

- `investment-memo.md`
- `case-notes.md`
- `evidence-log.csv`
- `expectation-map.csv`
- `workflow-scorecard.csv`
- triggered overlay templates

5. Run case validation:

```bash
python3 scripts/validate_repo.py cases/CASE_FOLDER --as-of 2026-05-30
```

## G04 Follow-Through Execution

Before a later event, check the trigger tracker and dry-run the packet:

```bash
python3 scripts/validate_follow_through_trigger_tracker.py
python3 scripts/validate_g04_later_event_candidate_screen.py
python3 scripts/validate_follow_through_execution_tracker.py
python3 scripts/build_follow_through_packet.py --dry-run
python3 scripts/validate_follow_through_packet_matrix.py
```

After a later material event and source collection, update `g04-later-event-candidate-screen.csv`. Draft a refresh only if `validate_g04_later_event_candidate_screen.py` exits 0 and the selected case shows `later_event_available`, `selected_for_refresh: yes` and `refresh_allowed: yes`.

Then export the packet:

```bash
python3 scripts/build_follow_through_packet.py --output exports/mira-follow-through-packet
```

For a non-default live case after a qualifying later event:

```bash
python3 scripts/build_follow_through_packet.py --case-id ETN_2026 --output exports/mira-follow-through-packet-etn
python3 scripts/build_follow_through_packet.py --case-id VRT_2026 --output exports/mira-follow-through-packet-vrt
python3 scripts/build_follow_through_packet.py --case-id LLY_2026 --output exports/mira-follow-through-packet-lly
```

After writing the refresh, validate it:

```bash
python3 scripts/validate_follow_through_refresh.py \
  --refresh cases/crm-2026-05-product-workflow-trial/follow-through-refresh-YYYY-MM-DD.md \
  --original-cutoff 2026-05-30 \
  --evidence-log cases/crm-2026-05-product-workflow-trial/evidence-log.csv \
  --intake cases/long-term-workflow-validation-2026-05-30/g04-follow-through-intake-checklist.csv
```

The packet alone does not clear G04.

## G06 External Review Execution

Before assignment:

```bash
python3 scripts/validate_external_review_packet.py
python3 scripts/validate_external_review_assignment_tracker.py
python3 scripts/validate_g06_reviewer_independence_screen.py
python3 scripts/build_external_review_packet.py --dry-run
python3 scripts/validate_external_review_dispatch_packet.py
python3 scripts/validate_g06_dispatch_readiness.py
```

To create the reviewer packet:

```bash
python3 scripts/build_external_review_packet.py --output exports/mira-external-reviewer-packet
```

After the reviewer returns materials:

```bash
python3 scripts/validate_external_review_return.py \
  --scorecard PATH/TO/completed-external-reviewer-scorecard.csv \
  --results PATH/TO/external-review-results-YYYY-MM-DD.md \
  --intake PATH/TO/completed-external-review-intake-checklist.csv \
  --assignment-tracker cases/long-term-workflow-validation-2026-05-30/g06-reviewer-assignment-tracker.csv \
  --independence-screen cases/long-term-workflow-validation-2026-05-30/g06-reviewer-independence-screen.csv
```

The packet alone does not clear G06.

The returned materials must include explicit reviewer decisions for:

- `g01_method_source_decision`
- `theme_selection_freshness`
- `practice_falsification`
- `methodology_iteration_traceability`
- `g04_follow_through_readiness`
- `g04_false_completion_control`
- `g05_source_decision`
- `historical_consensus_exception_decision`

## Release Owner Checks

Run the full QA suite after any gate, pack, case, reviewer or release-decision change:

```bash
python3 scripts/run_long_term_release_checks.py
python3 scripts/validate_long_term_release.py
python3 scripts/validate_public_release_freshness.py --as-of 2026-05-30
python3 scripts/validate_go_no_go_evidence_coverage.py
python3 scripts/validate_final_release_cutover.py
python3 scripts/validate_institutional_colleague_acceptance.py
python3 scripts/validate_institutional_colleague_acceptance_return.py --checklist path/to/completed-checklist.csv --memo path/to/institutional-colleague-acceptance-YYYY-MM-DD.md
python3 scripts/validate_objective_readiness.py
python3 scripts/validate_goal_completion_audit.py
python3 scripts/validate_release_verification_command_manifest.py
python3 scripts/validate_external_release_action_queue.py
python3 scripts/validate_g06_reviewer_selection_rubric.py
```

The machine-readable command list is `release-verification-command-manifest.csv`; it records the current expected exit code for each release verification command.
The machine-readable external action list is `external-release-action-queue.csv`; it records the real G04/G06 actions that must happen outside internal preparation before external release.
The reviewer selection rubric is `g06-reviewer-selection-rubric.csv`; it maps required release decisions to reviewer profiles, scorecard dimensions and evidence paths before assignment.

After any monthly theme review or market-leadership change, run:

```bash
python3 scripts/validate_recent_theme_selection.py --as-of 2026-05-30
```

The current expected final-release check is failure:

```bash
python3 scripts/validate_long_term_release.py --require-external-ready
```

Expected current result:

- exit_code: 2
- `external_ready: false`
- `hard_blocking_gates: G04,G06`

## Final Release Packet

The final institutional release packet builder must refuse export until external-ready gates clear:

```bash
python3 scripts/validate_institutional_release_bundle.py
python3 scripts/validate_institutional_colleague_acceptance.py
python3 scripts/validate_institutional_colleague_acceptance_return.py --checklist path/to/completed-checklist.csv --memo path/to/institutional-colleague-acceptance-YYYY-MM-DD.md
python3 scripts/build_institutional_release_packet.py --dry-run
```

Expected current result:

- exit_code: 2
- `export_ready: false`

The colleague acceptance check must also remain incomplete until a real institutional colleague pilot is completed:

- `acceptance_ready: false`
- `pending: 8`

Only after G04/G06 clear and `--require-external-ready` exits 0 should the release owner run:

```bash
python3 scripts/build_institutional_release_packet.py --output exports/mira-institutional-release-packet
```

## Evidence Discipline

- Facts, inferences and judgments must remain separate.
- Durable conclusions require evidence-log rows.
- Source gaps must remain visible.
- Stop rules and action labels must not be softened for presentation.
- `stale_after` and `must_refresh_if` must remain populated.
