# Long-Term Thesis Loop

`long-term-thesis-loop` is the operating loop for 3-5 year equity theses, hot-theme-to-company handoffs, and multi-lens long-term research where ordinary first-pass research is not enough.

It is based on the `long-term-integrated-thesis` validation program. Current status is `candidate_internal_release`, not final external release.

Use this loop when the research question depends on several linked variables:

- consumer or end-demand durability
- product reality and monetization
- macro or capital-cycle transmission
- industry structure and value migration
- company execution and capital allocation
- valuation expectations and what is already priced
- long-term right-tail / multibagger potential

Do not use this loop for same-day earnings reaction, narrow fact checking, pure macro views, or catalyst-only trades.

## Loop Input

- `research_object`
- `company_or_theme`
- `market_scope`
- `research_cutoff_date`
- `thesis_horizon`
- `current_market_label`
- `expected_decision_use`
- `source_availability`
- `known_sources`
- `prior_thesis_ref`, optional
- `theme_context`, optional

## Required Routing

Before starting, run `loops/analysis-routing.md`.

If the task is:

- an earnings event, start with earnings analysis or `event-delta-loop`
- a monitoring update, use `monitoring-loop`
- a methodology review, use `methodology-research-loop`
- a pure industry concept, run industry concept analysis before single-equity research

Use this loop only when routing confirms a long-term thesis or regime-transition question.

## States

### `setup`

Define research object, market scope, time boundary, thesis horizon, current market narrative, source availability and expected decision use.

### `theme-to-company-handoff`

Use this when a hot theme is being converted into a stock idea.

Required fields:

- theme definition
- value-chain nodes
- public company expressions
- investable purity
- value-capture path
- why this company and not only the theme
- read-through type
- theme purity score
- expectation burden score
- evidence maturity score
- valuation heat score
- handoff decision

If public-company value capture is unclear, run `theme-value-capture-screen.csv` before any single-company memo.

Stop rules:

- unclear value capture -> `industry_map_first`
- mostly private, pre-revenue or enabling-layer exposure -> `industry_map_first`
- high theme purity plus high expectation burden -> no actionability without expectation map

### `six-lens-test`

Run all six lenses and name the weakest lens:

1. consumer demand
2. product reality
3. macro economy
4. industry structure
5. company execution
6. valuation expectations

Keep facts, inferences and judgments separate.

### `right-tail-gate`

Use this gate when the case is framed as a long-term growth winner, platform compounder, multibagger, outlier company or 5-10 year right-tail candidate.

This is a lens, not a primary framework and not an actionability shortcut. It borrows from institutional long-term growth practice, including Baillie Gifford LTGG, but must stay inside Mira's source-trail and expectation-map discipline.

Required fields:

- five-year sales test
- ten-year outcome
- five-times-upside path
- market misunderstanding
- culture and adaptability
- probability-weighted upside
- missed-winner risk
- evidence ladder
- kill criteria

Stop rules:

- no 5x path -> do not label as long-term multibagger
- no market misunderstanding -> downgrade to ordinary quality company analysis
- no expectation map when valuation is material -> watch-only
- no evidence ladder -> no durable conclusion
- thesis depends on multiple heroic assumptions with no interim refresh variables -> reject or watch-only
- weak balance sheet or severe dilution can block shareholder upside even if the company survives

### `trigger-overlays`

Select overlays based on the evidence path:

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

Each triggered overlay is either completed, explicitly waived, or blocks actionability.

### `build-evidence-log`

Every durable conclusion must map to a source.

Use `evidence-log.csv` with source id, claim area, claim type, source date, URL/path, confidence and notes.

`L6` Mira-derived calculations can support interpretation, but cannot be the only evidence for a durable conclusion.

### `expectation-map`

Create or update `expectation-map.csv`.

Unavailable-data rule:

- keep unavailable fields as `source_gap`
- label modeled values as `modeled`, not consensus
- do not replace FY2 FCF or historical EV/FCF with easier metrics without a false-precision warning
- if valuation is a gating lens, keep the case watch-only unless data is obtained or reviewer accepts the exception

### `ordinary-vs-workflow-delta`

Record whether this loop changed the research result versus ordinary research:

- ordinary likely conclusion
- workflow conclusion
- actionability change
- new stop rule
- source gap exposed
- whether the workflow changed the decision enough to justify its cost

If the workflow changes nothing, mark the case as a methodology or cost-efficiency failure.

### `decision`

Use explicit labels:

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

If a case needs a case-specific label, define it in the memo header and map it to the closest stop rule.

### `refresh-plan`

Every case must include:

- `stale_after`
- `must_refresh_if`
- next event
- affected thesis variable
- expected state change if trigger fires

If a source gap is later closed, use `source-gap-refresh.md`.

If a later material event occurs after the original memo cutoff, use `follow-through-refresh.md`.

Do not count source-gap refresh as true follow-through unless the triggering evidence occurred after the original memo was completed.

### `reviewability`

Before using the case as methodology evidence, check whether another analyst can reproduce the action label, challenge the weakest lens, trace source gaps and understand the expectation map.

## Standard Output

For a single-equity case:

- `investment-memo.md`
- `case-notes.md`
- `evidence-log.csv`
- `expectation-map.csv`
- `long-term-multibagger-checklist.md`, if `right-tail-gate` is triggered
- `workflow-scorecard.csv`
- triggered overlay files
- `methodology-delta.md`

For a hot-theme screen:

- `value-capture-screen.md`
- `value-capture-map.csv`
- `evidence-log.csv`
- `workflow-scorecard.csv`
- `methodology-delta.md`

For a follow-through refresh:

- `follow-through-refresh-YYYY-MM-DD.md`
- updated evidence log
- updated expectation map if valuation changed
- updated workflow scorecard
- review-log entry

Every standard output also includes Step 4.5 critical interaction: one natural-language next question tied to the highest-value evidence gap, workflow handoff, or explicit waiver.

## Release Status

This loop is approved for internal candidate use.

It is not externally release-grade until:

- one true post-memo follow-through refresh is completed
- an external independent reviewer completes the scorecard
- expectation-map gate is resolved by data or accepted unavailable-data exception

Use `cases/long-term-workflow-validation-2026-05-30/public-release-gate-tracker.csv` for release status.

## Stop Rules

- No source trail -> no durable conclusion.
- No expectation map -> no actionability when valuation is material.
- Product usage without monetization bridge -> watch-only.
- Clinical demand without payer/access and net-price evidence -> watch-only.
- Shock-era demand without normalized demand evidence -> watch-only.
- Hardware-linked subscription thesis without normalized hardware demand and hardware margin -> watch-only.
- Acquired exposure without purchase price, integration and ROIC path -> watch-only.
- Power or nuclear exposure without contract economics, regulatory status, interconnection and COD evidence -> watch-only.
- Stablecoin or tokenized-cash exposure without reserve economics, distribution costs, redemption liquidity, regulatory status and payment usage evidence -> watch-only.
- Defense or government-procurement exposure without funded program status, contract quality, delivery evidence, compliance requirements and margin risk -> watch-only.
- Hot theme with unclear public-company value capture -> `industry_map_first`.
- No ordinary-vs-workflow delta -> methodology value not proven.
