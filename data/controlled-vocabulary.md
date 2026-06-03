# Mira Controlled Vocabulary

This file is the canonical vocabulary source for Mira research state and action fields.

Human-readable explanation can be written in `basis`, `notes`, `risk`, `required_followup` or prose sections. Machine-facing fields should use the tokens below so outputs can be aggregated across cases, memory and PM registers.

## Thesis State

Use in `thesis-ledger.md`, `event-delta.md`, portfolio registers and [memory/research/INDEX.md](../memory/research/INDEX.md).

- `draft`: first-pass research; evidence chain incomplete.
- `active`: evidence trail, refresh condition and disconfirming path are present.
- `watch`: directional view exists, but evidence is not strong enough for active thesis.
- `upgrade_watch`: new evidence is strengthening the thesis, pending confirmation.
- `downgrade_watch`: new evidence weakens the thesis, but does not yet retire it.
- `narrative_watch`: narrative/catalyst exists, but evidence quality is weak or market-pricing-led.
- `stale`: past refresh boundary or event boundary; must refresh before live use.
- `retired`: core assumption was falsified or object left coverage scope.

## Research Action / Decision Type

Use the same token set for `research_action` and `decision_type`.

- `watch_only`: keep on research watchlist; no stronger actionability.
- `upgrade_watch`: increase research priority after confirming evidence.
- `downgrade_watch`: reduce research priority after weakening evidence.
- `add_to_research_queue`: add to future research queue.
- `reduce_research_priority`: deprioritize without retiring.
- `hedge_context`: record as risk or hedge context for a broader book.
- `event_setup`: prepare for an upcoming event delta.
- `post_event_follow_through`: follow up after event delta.
- `valuation_reset_watch`: monitor for valuation or multiple reset.
- `risk_reduction_context`: record as risk-reduction context only.
- `needs_refresh`: conclusion is stale or source-gapped before live use.
- `no_action`: no research action beyond recordkeeping.
- `retire_thesis`: retire the thesis.

## Setup Type

Use in `actionability-bridge.md`.

- `watch_only`
- `upgrade_watch`
- `event_setup`
- `post_event_follow_through`
- `valuation_reset_watch`
- `risk_reduction_context`
- `needs_refresh`
- `no_action`

## Position Sizing Implication

Research-only qualitative sizing language. These are not trade instructions.

- `not_applicable`
- `watchlist_only`
- `small_if_confirmed`
- `normal_only_after_confirmation`
- `reduce_risk_context`

## Position Data Status

Use in position and portfolio review templates before drawing position-level conclusions.

- `no_position_data`: no real holding, weight, cost basis or mandate was provided.
- `partial_position_data`: some position information exists, but key fields are missing.
- `position_data_provided`: user provided enough position context for a position-level review.
- `research_only`: the review is intentionally limited to thesis exposure, not real portfolio holdings.

## Position Review Action

Use in `position-review.md`, `position-register.csv`, portfolio exposure reviews and decision logs when a real or proposed position is discussed. These are review actions, not executed trades.

- `research_only`: return thesis or exposure implications without position-level conclusion.
- `hold_review`: current position remains reviewable if thesis, evidence and refresh conditions still support it.
- `add_only_if_confirmed`: adding exposure would require specified confirming evidence first.
- `trim_review`: position size appears high relative to evidence, risk, stale status or constraints; review risk reduction.
- `exit_review`: thesis or risk evidence is weak enough that an exit review is required.
- `risk_cap_review`: review whether a cap, hedge context or concentration limit is needed.
- `needs_refresh`: thesis, source, valuation or position data is stale or incomplete before stronger review action.
- `no_action`: no position-management implication beyond recordkeeping.

## Position Sizing Context

Use in position and portfolio reviews. These are qualitative context labels, not target weights.

- `not_applicable`
- `watchlist_only`
- `starter_only`
- `normal_if_confirmed`
- `too_large_for_evidence`
- `too_small_for_conviction`
- `reduce_risk_context`
- `source_gap`

## Instrument Strategy Family

Use in instrument strategy gates. These are research routes, not trade
instructions. See [instrument-strategy-gate.md](instrument-strategy-gate.md).

- `cash_equity`
- `listed_option_long_premium`
- `listed_option_spread`
- `protective_option`
- `collar_or_overlay`
- `income_overlay`
- `short_sale`
- `pair_or_relative_value`
- `portfolio_hedge`
- `no_instrument_route`

## Instrument Data Status

Use in instrument strategy gates to explain whether structure-specific data is
usable. Human-readable details belong in `notes`, `basis` or the required-data
table.

- `available`
- `partial`
- `missing`
- `stale`
- `not_applicable`
- `source_gap`

## Portfolio Review Scope

Use when a task discusses multiple holdings or theses.

- `research_book`: thesis/watchlist review only; real position weights are absent.
- `real_portfolio`: holdings, weights or mandate are provided.
- `mixed`: real holdings plus research-only watchlist objects.

## Technical / Market Pricing State

Use in [../templates/technical-analysis-check.csv](../templates/technical-analysis-check.csv) and memo `technical_context` fields.

`trend_state`:

- `uptrend_confirmed`
- `uptrend_extended`
- `range_constructive`
- `range_neutral`
- `range_distribution`
- `downtrend_confirmed`
- `reversal_attempt`
- `technical_source_gap`

`event_reaction_quality`:

- `positive_follow_through`
- `negative_follow_through`
- `reversal_against_news`
- `gap_and_hold`
- `gap_fill`
- `range_digesting`
- `no_clear_signal`
- `source_gap`

`positioning_risk`:

- `low`
- `medium`
- `high`
- `source_gap`

Technical state tokens are market-pricing descriptors only. They must not be used as proof of company execution, fundamental quality or long-term thesis durability.

## Top / Bottom Risk Overlay Tokens

Use when `top-bottom-risk` overlay is selected. These labels describe risk state, not trade instructions.

`risk_regime`:

- `trend_confirmation`: fundamentals, expectations and reaction quality still align.
- `fragile_upside`: fundamentals are strong, but price requires continued upside surprise.
- `distribution_risk`: good news fades or relative strength weakens after a large move.
- `capitulation_watch`: downside may be forced or exhausted, but thesis repair is not yet proven.
- `base_building`: bad news is being absorbed and evidence is stabilizing.
- `bear_trap_risk`: weak fundamentals coexist with crowded short exposure or removable left-tail assumptions.
- `no_clear_extreme`: no reliable top / bottom risk state can be assigned.

`fundamental_slope`:

- `accelerating`
- `positive_but_decelerating`
- `stable_high_level`
- `deteriorating`
- `mixed`
- `source_gap`

`expectation_burden`:

- `low`
- `medium`
- `high`
- `extreme`
- `source_gap`

`positioning_liquidity`:

- `clean_revision`
- `crowded_long`
- `crowded_short`
- `squeeze_or_forced_flow`
- `liquidity_gap`
- `source_gap`

`next_catalyst_burden`:

- `needs_upside_surprise`
- `needs_confirmation`
- `can_digest`
- `needs_reset`
- `waiting_for_capitulation`
- `source_gap`

## Strategic Data Dependency

Institutional expectation work is constrained without reliable consensus and estimate data.

When Mira cannot access a consensus/estimate source, write `source_gap` in the relevant variable and avoid pretending that price action, media narrative or company guidance is the same as sell-side consensus.

Strategic data candidates:

- sell-side consensus revenue, EPS, margin and target-price estimates
- estimate revision history
- segment-level consensus where available
- options-implied move and skew data
- institutional ownership / positioning and short interest

## Evidence And Calculation Gap Tokens

Use these tokens in notes, expectation maps, delivery checks and gate outputs when a conclusion cannot be fully supported.

- `source_gap`: required source is missing, stale, inaccessible or below the evidence quality needed for the conclusion.
- `calculation_gap`: required calculation, formula, peer comparison, time-series check or numeric cross-check is missing or not reproducible.
- `calculation_waived_by_speed`: user accepted a faster read without full calculation; related conclusions must remain preliminary.
- `verified_calculation`: derived number has a recorded formula, upstream sources and calculation ledger or explicit formula note.

## Language Field

Formal outputs may include `output_language`.

Recommended values:

- `zh-CN`: Chinese output.
- `en`: English output.
- `mixed`: intentionally bilingual or case-source-driven output.

Default rule: use the user's language for new outputs unless the source package or target audience requires otherwise.
