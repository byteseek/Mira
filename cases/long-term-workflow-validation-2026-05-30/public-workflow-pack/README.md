# Long-Term Integrated Thesis Workflow Pack

- methodology: `long-term-integrated-thesis`
- pack_status: candidate_internal_release
- last_updated: 2026-05-30
- intended_users: institutional equity analysts, PMs, and research reviewers
- current_limit: not final public-grade until one true follow-through refresh and external reviewer completion
- external_review_status: ready_to_run_not_completed

## Purpose

This pack converts the internal Mira long-term workflow trials into a reproducible analyst workflow.

The canonical operating loop for internal use is `../../../loops/long-term-thesis-loop.md`.

Use it to test whether a 3-5 year equity thesis survives six linked lenses:

1. consumer demand
2. product reality
3. macro economy
4. industry structure
5. company execution
6. valuation expectations

The workflow is intentionally designed to block attractive narratives when the evidence bridge is incomplete.

## When To Use

Use this workflow when:

- the thesis horizon is longer than one year
- the conclusion depends on multiple operating variables
- a hot theme is being translated into a single company
- product usage, ARR, backlog, AI adoption, consumer behavior, acquisition logic, or demand pull-forward are central to the thesis
- valuation already embeds a meaningful growth, margin, ROIC or duration assumption

Do not use it as the primary workflow for:

- same-day earnings reaction
- single data-release triage
- pure macro view
- narrow fact verification
- catalyst-only trades

## Required Output For A Standard Case

- `investment-memo.md`
- `case-notes.md`
- `evidence-log.csv`
- `expectation-map.csv`
- `workflow-scorecard.csv`
- one or more overlay maps when triggered:
  - `theme-value-capture-screen.csv`
  - `product-monetization-map.csv`
  - `pull-forward-check.csv`
  - `payer-access-net-price-check.csv`
  - `hardware-subscription-mix-check.csv`
  - `backlog-quality-check.csv`
  - `acquisition-value-capture-check.csv`
  - `cash-flow-quality-check.csv`
  - `power-contract-regulatory-check.csv`
  - `stablecoin-reserve-regulatory-check.csv`
  - `government-procurement-program-check.csv`
- `source-gap-refresh.md` when a blocking source gap is closed after the initial memo
- `follow-through-refresh.md` when a later material event refreshes the original thesis

## Decision Labels

Use these labels rather than vague conviction language:

- `actionable`
- `watch_only_pending_expectation_map`
- `watch_only_pending_product_monetization_map`
- `watch_only_pending_payer_access`
- `watch_only_pending_expectation_map_and_realized_price_refresh`
- `watch_only_pending_normalized_demand`
- `watch_only_pending_normalized_hardware_demand`
- `watch_only_pending_backlog_quality`
- `watch_only_pending_acquisition_value_capture`
- `industry_map_first`
- `reject_for_now`

If a case needs a more specific label, define it in the memo header and map it to the closest standard stop rule.

## Current Validation Base

Live / current-market trials:

- ETN: AI power infrastructure value-capture and expectation-map discipline
- VRT: high-purity AI infrastructure versus expectation burden
- CRM: enterprise AI product evidence and monetization bridge
- LLY: GLP-1 direct exposure, payer access / net price and high expectation burden
- Humanoid robotics: value-capture screen and `industry_map_first` discipline
- Nuclear / SMR / AI power: power-contract and regulatory value-capture discipline
- Stablecoin / tokenized payments: reserve, regulatory and payment-network value-capture discipline
- Defense autonomy / drones / counter-UAS: government procurement and program-quality discipline
- Seven-theme direction scan: AI power, enterprise AI agents, GLP-1 read-through, humanoid robotics, nuclear / AI power, stablecoin payments and defense autonomy

Historical failure backtests:

- TDOC 2020-2022: COVID demand pull-forward and acquisition value capture
- PTON 2020-2022: hardware/subscription mix, inventory commitment and normalized demand

## Current Public-Grade Gaps

This pack is usable internally but not final public-grade because:

- no true follow-through refresh has occurred after a later live-case event
- reviewer dry run is still internal/simulated, not an external independent analyst test
- CRM expectation map now has broader peer support, historical ratio support and MarketScreener FY2028 FCF forecast; reviewer still needs to challenge source definitions under G06
- historical cases need transcript, price and consensus reconstruction before external distribution
- public Asian/Chinese practitioner source coverage has improved, but private buyside execution detail remains undercovered and needs G06 reviewer acceptance
- LLY now has FDA/CVS/CMS source-gap support, but still needs transcript, all-PBM confirmation, plan-level payer evidence and realized-price follow-through before external use

## External Reviewer Dry Run

Prepared but not completed:

- `external-reviewer-brief.md`
- `external-review-request.md`
- `external-reviewer-scorecard.csv`
- `blind-review-assignment.md`
- `external-review-results-template.md`
- `external-review-intake-checklist.csv`
- `../g06-external-review-handoff-2026-05-30.md`
- `../g05-crm-unavailable-data-exception-review.md`
- `../g05-crm-source-attempts.csv`
- `../g05-fy2-fcf-source-upgrade-2026-05-30.md`

These files make the pack ready to send to an external reviewer, including a specific G05 source-sufficiency challenge. They do not count as independent review evidence until a reviewer completes the assignment and returns findings.

Before sending, build or dry-run the reviewer packet from the manifest:

```bash
python3 scripts/build_external_review_packet.py --dry-run
python3 scripts/validate_g06_reviewer_independence_screen.py
python3 scripts/validate_external_review_dispatch_packet.py
python3 scripts/validate_g06_dispatch_readiness.py
python3 scripts/build_external_review_packet.py --output exports/mira-external-reviewer-packet
```

The builder copies only `send_to_reviewer=yes` rows from `../external-reviewer-bundle-manifest.csv` and excludes internal do-not-send rows. The dispatch validator performs a temporary real export and confirms the packet is ready to assign while still not clearing G06.

## Follow-Through Refresh

Prepared but not completed:

- `../follow-through-refresh-playbook.md`
- `../follow-through-trigger-tracker.csv`
- `../g04-follow-through-execution-tracker.csv`
- `../../../templates/follow-through-refresh.md`
- `../../../scripts/build_follow_through_packet.py`
- `../../../scripts/validate_follow_through_packet_matrix.py`

The first valid refresh should use a later event after the original memo cutoff. `CRM_2026` is the preferred default candidate because Q2 FY2027 should directly test the product-to-company monetization bridge, but ETN_2026, VRT_2026 and LLY_2026 are also packet-ready if their later events arrive first.

Before execution, update and validate the later-event candidate screen. Do not draft a G04 refresh unless the selected case shows `later_event_available`, `selected_for_refresh: yes` and `refresh_allowed: yes`:

```bash
python3 scripts/validate_g04_later_event_candidate_screen.py
python3 scripts/build_follow_through_packet.py --dry-run
python3 scripts/validate_follow_through_packet_matrix.py
python3 scripts/build_follow_through_packet.py --output exports/mira-follow-through-packet
```

## Release QA

One-screen execution runbook:

- `operator-runbook.md`

Run after any gate, pack or release-decision change:

```bash
python3 scripts/run_long_term_release_checks.py
python3 scripts/validate_long_term_release.py
python3 scripts/validate_final_release_cutover.py
python3 scripts/validate_objective_readiness.py
python3 scripts/validate_goal_completion_audit.py
python3 scripts/validate_external_review_dispatch_packet.py
python3 scripts/validate_g06_reviewer_independence_screen.py
python3 scripts/validate_g06_dispatch_readiness.py
python3 scripts/build_external_review_packet.py --dry-run
python3 scripts/build_follow_through_packet.py --dry-run
python3 scripts/validate_follow_through_packet_matrix.py
python3 scripts/build_institutional_release_packet.py --dry-run
```

Current report:

- `../release-qa-report-2026-05-30.md`

The QA runner should pass while the external-ready subcheck fails as expected. The release validator should show zero errors and `hard_blocking_gates: G04,G06` until the remaining external-release gates are actually resolved. The objective-readiness validator should keep `objective_complete: false` until G04, G06 and final external release clear.

The G06 assignment packet can also be checked directly:

```bash
python3 scripts/validate_external_review_packet.py
python3 scripts/validate_external_review_assignment_tracker.py
python3 scripts/validate_g06_reviewer_independence_screen.py
python3 scripts/build_external_review_packet.py --dry-run
python3 scripts/validate_external_review_dispatch_packet.py
python3 scripts/validate_g06_dispatch_readiness.py
```

The G04 trigger tracker can also be checked directly:

```bash
python3 scripts/validate_follow_through_trigger_tracker.py
python3 scripts/validate_g04_event_watch_calendar.py
python3 scripts/validate_g04_later_event_candidate_screen.py
python3 scripts/build_follow_through_packet.py --dry-run
```

The recent-theme selection and refresh audit can also be checked directly:

```bash
python3 scripts/validate_recent_theme_selection.py --as-of 2026-05-30
```

The future institutional colleague release bundle can also be checked directly:

```bash
python3 scripts/validate_institutional_release_bundle.py
python3 scripts/validate_institutional_colleague_acceptance.py
python3 scripts/validate_institutional_colleague_acceptance_return.py --checklist path/to/completed-checklist.csv --memo path/to/institutional-colleague-acceptance-YYYY-MM-DD.md
python3 scripts/build_institutional_release_packet.py --dry-run
```

## Institutional Colleague Release Package

Prepared but not released:

- `institutional-colleague-release-notes-template.md`
- `institutional-colleague-acceptance-memo-template.md`
- `institutional-use-boundaries.md`
- `institutional-adoption-faq.md`
- `../institutional-colleague-acceptance-checklist.csv`
- `../institutional-release-bundle-manifest.csv`

These files define what an eventual institutional colleague release must say, what caveats must remain visible, what colleague acceptance must prove and which internal development notes should not be sent by default.

They do not change the current status. The package remains `candidate_internal_release` until G04 and G06 clear, colleague acceptance is validated and `python3 scripts/validate_long_term_release.py --require-external-ready` exits 0.

The final institutional release packet builder should refuse export in the current state:

```bash
python3 scripts/build_institutional_release_packet.py --dry-run
```

Expected current result: exit 2 with `export_ready: false`.

## Refresh Conditions

- stale_after: 2026-06-30
- must_refresh_if: any live case reports a material new quarter, product metric or guidance change; valuation data changes enough to alter the expectation map; or another analyst cannot reproduce a case conclusion from the evidence log.
