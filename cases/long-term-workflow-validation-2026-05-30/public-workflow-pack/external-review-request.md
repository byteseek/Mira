# External Review Request

- request_type: independent methodology dry run
- methodology: `long-term-integrated-thesis`
- pack_status: internal_candidate_release
- final_external_release: no
- requested_return_by: set_on_assignment

## Request

Please review the attached long-term equity research workflow as an independent institutional analyst.

The goal is not to agree with the original analyst. The goal is to test whether another analyst can reproduce, challenge and improve the workflow without access to internal chat history or live explanation.

## What To Review

Use the attached bundle manifest:

- `../external-reviewer-bundle-manifest.csv`

Packet build command:

```bash
python3 scripts/build_external_review_packet.py --output exports/mira-external-reviewer-packet
```

Only files listed as `send_to_reviewer=yes` in the manifest should be included.

Core files:

- `README.md`
- `workflow.md`
- `fill-guide.md`
- `template-inventory.md`
- `source-appendix.md`
- `analyst-checklist.csv`
- `external-reviewer-brief.md`
- `external-reviewer-scorecard.csv`
- `blind-review-assignment.md`
- `external-review-results-template.md`
- `external-review-intake-checklist.csv`
- `../g06-reviewer-selection-rubric.csv`

Assigned case folder will be one of:

- LLY GLP-1 workflow dry run
- humanoid robotics value-capture screen
- PTON historical failure backtest

Also review the recent-theme selection, G01 method-source, G04 follow-through readiness and CRM G05 source packages:

- `../trial-theme-matrix.csv`
- `../theme-selection-refresh-audit.csv`
- `../g06-reviewer-selection-rubric.csv`
- `../../../scripts/validate_recent_theme_selection.py`
- `../practice-falsification-audit.csv`
- `../methodology-iteration-trace-audit.csv`
- `../multi-lens-coverage-audit.csv`
- `../g01-external-method-source-audit.csv`
- `../g01-external-method-source-upgrade-2026-05-30.md`
- `../follow-through-trigger-tracker.csv`
- `../g04-follow-through-event-watch-calendar.csv`
- `../g04-later-event-candidate-screen.csv`
- `../g04-follow-through-execution-tracker.csv`
- `../g04-follow-through-handoff-2026-05-30.md`
- `../../../scripts/validate_g04_later_event_candidate_screen.py`
- `../g05-fy2-fcf-source-upgrade-2026-05-30.md`
- `../g05-crm-source-attempts.csv`
- CRM expectation map
- CRM evidence log

## What Not To Use

Do not use:

- internal chat transcript
- unpublished reasoning notes
- methodology development logs
- prior answers from the original analyst
- live explanation from the author

If a conclusion cannot be reproduced from the supplied files and public sources, mark it as a finding.

## Required Return

Please return:

1. completed `external-reviewer-scorecard.csv`
2. completed `external-review-results-YYYY-MM-DD.md` based on the template
3. completed `external-review-intake-checklist.csv` or equivalent confirmations
4. P0/P1 blocker list
5. release recommendation

Allowed release recommendations:

- `release_external`
- `release_with_caveats`
- `release_internal_only`
- `reject`

## Release Standard

The workflow cannot be treated as external-release methodology unless:

- reviewer independence is confirmed;
- no P0 finding is returned;
- average score is at least 4;
- every P1 has a named fix;
- recent theme selection freshness result is `pass` or `accepted_with_caveats`;
- `methodology_iteration_traceability` result is `pass` or `accepted_with_caveats`;
- G01 method-source decision is `accept_basis` or `accept_with_caveats`;
- CRM G05 source decision is `accept_source` or `accept_with_caveats`;
- release recommendation is `release_external` or `release_with_caveats`;
- G04 true follow-through refresh is later completed.

## Known Current Limits

These are known and should not be treated as hidden defects:

- G04 true follow-through refresh has not been completed yet.
- Recent theme selection has source-linked freshness and replacement controls; score `theme_selection_freshness`, and do not accept narrative heat without observable refresh/drop rules.
- Practice-falsification audit maps methodology claims to cases and rejection tests; score `practice_falsification`, and do not accept theory-only or stale-theory claims without case evidence.
- Methodology iteration trace audit maps workflow patches to case failure modes, patch artifacts, validators and decision effects; challenge any patch that looks document-only, memory-based or overfit to one case.
- Multi-lens coverage audit maps consumer/product/economy/industry/company/valuation lenses to case evidence; challenge lens routing if any dimension is document-only rather than case-grounded.
- G04 follow-through readiness controls are included for review; score `g04_follow_through_readiness` and `g04_false_completion_control`, but do not treat packet readiness, scheduled future events or candidate-screen rows without `refresh_allowed: yes` as completed G04 evidence.
- A valid G04 refresh requires `validate_g04_later_event_candidate_screen.py` to pass after the later-event candidate screen shows `later_event_available`, `selected_for_refresh: yes` and `refresh_allowed: yes` for the selected case.
- G01 method-source coverage includes public Asian/Chinese practitioner sources, but private buyside execution detail remains undercovered and requires `g01_method_source_decision`: `accept_basis`, `accept_with_caveats`, `require_private_material` or `reject_basis`.
- Historical backtests still have consensus exception caveats and require `historical_consensus_exception_decision`: `accept_exception`, `accept_with_caveats`, `require_export` or `reject_exception`.
- CRM G05 uses MarketScreener FY2028 FCF forecast; please challenge source methodology.
- This is an internal candidate pack, not final external-release methodology.

## Questions To Answer

1. Can you reproduce the action label from the supplied evidence?
2. Which lens is weakest?
3. Which source gap most affects actionability?
4. Does the workflow improve on an ordinary memo enough to justify its cost?
5. Would you allow this workflow to be shared with other institutional analysts, and under what caveats?

## Refresh Conditions

- stale_after: 2026-06-30
- must_refresh_if: reviewer assignment changes, bundle manifest changes, G04 follow-through completes, G05 source is rejected, or release recommendation changes.
