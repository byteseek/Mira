# Mira Controlled Vocabulary

This file is the canonical vocabulary source for Mira research state and action fields.

Human-readable explanation can be written in `basis`, `notes`, `risk`, `required_followup` or prose sections. Machine-facing fields should use the tokens below so outputs can be aggregated across cases, memory and PM registers.

## Interaction Mode

Use in routing intake (analysis-routing Step 0).

<!-- vocab:interaction_mode start (tokens bound to schemas/vocab.json) -->
- `quick_answer`: user wants a one-line direction or fact; no full package.
- `routed_research`: normal entry into a routed loop / skill.
- `decision_support`: near actionability / position / portfolio; must run the decision pressure gate (Step 0.5).
- `routing_unclear`: research object or time boundary is fully unclear; clarify definition only.
<!-- vocab:interaction_mode end -->

## Task Mode

Step 1 task classification. Per-mode routing and boundaries live in
[../loops/analysis-routing.md](../loops/analysis-routing.md) Step 1; the token set
is bound to `schemas/vocab.json`. `position_review` and
`portfolio_construction_review` (and any `decision_support` interaction) must emit
`decision_pressure` via Step 0.5.

<!-- vocab:task_mode start (tokens bound to schemas/vocab.json) -->
- `first_pass_research`
- `monitoring_update`
- `market_briefing`
- `earnings_event`
- `research_report_interpretation`
- `methodology_review`
- `sec_supplement`
- `sec_filing_deep_dive`
- `thesis_system_update`
- `view_continuity`
- `position_review`
- `portfolio_construction_review`
- `decision_quality_review`
- `discovery_or_screening`
<!-- vocab:task_mode end -->

## Decision Pressure And Framing Risk

Use in routing intake (analysis-routing Step 0.5). These are transient, per-turn routing signals. They describe the structure of the question, not the user's psychology, and must never be written to preference memory or private state.

`decision_pressure`:

<!-- vocab:decision_pressure start (tokens bound to schemas/vocab.json) -->
- `none`
- `low`
- `medium`
- `high`
<!-- vocab:decision_pressure end -->

`framing_risk` (describe the question structure, not the user):

<!-- vocab:framing_risk start (tokens bound to schemas/vocab.json) -->
- `confirmation_seeking`: question is shaped to confirm an existing view.
- `fomo`: question is driven by a recent move or fear of missing it.
- `anchoring`: question anchors on a prior price, cost basis or target.
- `loss_aversion`: question is shaped around avoiding a realized loss.
- `position_defense`: question is shaped to justify keeping an existing exposure.
- `none`
<!-- vocab:framing_risk end -->

`disconfirmation_required`:

<!-- vocab:disconfirmation_required start (tokens bound to schemas/vocab.json) -->
- `yes`
- `no`
<!-- vocab:disconfirmation_required end -->

## Routing Carryover

Use in routing intake (analysis-routing Step 3.2). Carryover is valid within a single session only; cross-session continuity must go through view-continuity-loop or private state.

`routing_carryover`:

- `none`
- `inherit`
- `reset`

Carryover whitelist (may inherit within a session): `market_scope`, `time_boundary`, `research_object`, `depth_mode`, `output_language`.

Never inherit: `decision_pressure`, `framing_risk`, `disconfirmation_required`, or any inferred user motive.

## Information Value And Knowability

Use in routing intake (analysis-routing Step 3.3), after `depth_mode` is selected. This gate can override the depth choice downward.

`information_value`:

<!-- vocab:information_value start (tokens bound to schemas/vocab.json) -->
- `low`: another research round is unlikely to change the conclusion or decision.
- `medium`: more research would sharpen but not flip the conclusion.
- `high`: more research can change the conclusion or the decision at stake.
<!-- vocab:information_value end -->

`knowability_status`:

<!-- vocab:knowability_status start (tokens bound to schemas/vocab.json) -->
- `knowable`: key variables can be settled with available sources or reasonable research.
- `partially_knowable`: some variables are knowable; core uncertainty remains.
- `unknowable_now`: key variables cannot be known yet; awaits an event, disclosure or time.
- `irreducible_uncertainty`: the conclusion is dominated by an inherently unknowable variable; deeper research will not improve quality. A legitimate honest terminal — pair with `watch_only` / `needs_refresh` and an observable refresh trigger.
<!-- vocab:knowability_status end -->

`depth_override_reason`: free-text basis when this gate changes the depth selected in Step 3.25.

## Question Expansion Lenses

Use in routing intake (analysis-routing Step 3.27), after `depth_mode` is
selected and before information-value / knowability is finalized. Lens details
live in [question-expansion-lenses.md](question-expansion-lenses.md).

`question_expansion_lens`:

<!-- vocab:question_expansion_lens start (tokens bound to schemas/vocab.json) -->
- `none`: no question-expansion lens materially improves this route.
- `comparison_association`: sharpen the question through peer, factor, macro, customer, supplier or variable association, while separating correlation from causality.
- `scale_shift`: move the question up or down the evidence scale, such as event -> thesis, theme -> measurable variable, or company -> segment.
- `trend_dynamics`: test level, direction, acceleration, persistence or regime change over time.
- `anomaly_detection`: test whether an observation is unusual versus a defined baseline, and whether it is data error, one-time noise, cyclicality or structural signal.
<!-- vocab:question_expansion_lens end -->

## Depth, Quant And Scope (Routing Intake)

Routing-intake tokens used in analysis-routing Steps 3.25 / 3.5 / 0. Token sets are
bound to `schemas/vocab.json` (the single source) and to
[../schemas/routing.schema.json](../schemas/routing.schema.json).

`depth_mode` (Step 3.25; the information-value/knowability gate above can override it downward):

<!-- vocab:depth_mode start (tokens bound to schemas/vocab.json) -->
- `quick_map`: fast read, early triage, or unclear source boundary.
- `standard`: normal research / earnings / monitoring package.
- `deep_dive`: long-term thesis, complex valuation, SEC deep dive or methodology review.
<!-- vocab:depth_mode end -->

`quant_dependency` (Step 3.5; how much the conclusion rests on derived numbers):

<!-- vocab:quant_dependency start (tokens bound to schemas/vocab.json) -->
- `none`
- `low`
- `medium`
- `high`
<!-- vocab:quant_dependency end -->

`calculation_gate` (Step 3.5; required whenever `quant_dependency` is not `none`):

<!-- vocab:calculation_gate start (tokens bound to schemas/vocab.json) -->
- `not_required`: no derived number gates the conclusion.
- `required`: a calculation gate must be satisfied before the conclusion stands.
- `waived`: user accepted a faster read; related conclusions stay preliminary.
<!-- vocab:calculation_gate end -->

`scope_confirmation_required` (Step 0; set when a compound prompt needs scope confirmation before formal analysis):

<!-- vocab:scope_confirmation_required start (tokens bound to schemas/vocab.json) -->
- `yes`
- `no`
<!-- vocab:scope_confirmation_required end -->

`followup_prompt_mode` (Step 4.5; `light` / `standard` / `decision_grade` must carry 1-3 route-bound questions, `none` must carry a `followup_waiver_reason`):

<!-- vocab:followup_prompt_mode start (tokens bound to schemas/vocab.json) -->
- `none`: no follow-up is useful; pair with an explicit `followup_waiver_reason`.
- `light`: a single sharpening question.
- `standard`: 1-3 route-bound questions.
- `decision_grade`: near actionability / position / portfolio / instrument / PM handoff / durable thesis; 2-3 questions, each naming the next loop / skill.
<!-- vocab:followup_prompt_mode end -->

## Live Data Freshness

Use in analysis-routing Step 3.35 and live market source notes. These tokens
describe whether a same-day market answer has current enough data to support the
visible judgment.

`live_data_gate`:

<!-- vocab:live_data_gate start (tokens bound to schemas/vocab.json) -->
- `required_quote_time`: the prompt depends on current or same-day market quote data and fresh lookup with `quote_time` is required.
- `required_publish_time`: the prompt depends on same-day published event data and fresh lookup with `publish_time` is required.
- `waived_definition`: the prompt uses live-market language but asks only for a stable definition or method.
- `not_applicable`: the prompt does not depend on live or same-day data.
<!-- vocab:live_data_gate end -->

`live_freshness_status`:

<!-- vocab:live_freshness_status start (tokens bound to schemas/vocab.json) -->
- `live`: source claims real-time or near-real-time data and has a usable quote/publish time.
- `delayed`: source is delayed or likely delayed, but still usable for a bounded quick map.
- `stale`: source timestamp is outside the stated live-use window.
- `unavailable`: no usable fresh source was obtained.
<!-- vocab:live_freshness_status end -->

`cross_check_status`:

<!-- vocab:cross_check_status start (tokens bound to schemas/vocab.json) -->
- `passed`: two independent sources align, or one official/primary market source is sufficient for the bounded claim.
- `partial`: only one usable source, delayed source, or source boundary caveat remains.
- `failed`: sources conflict materially or the timestamp cannot support the judgment.
<!-- vocab:cross_check_status end -->

Mapping note:

- `live_freshness_status` is a routing/source-note field for same-day market
  acquisition quality. It is intentionally separate from evidence-log
  `freshness_status`, whose allowed values remain `current`,
  `acceptable_for_period`, `preliminary`, `stale`, and `unknown`.
- `cross_check_status` records whether the live-source lookup was corroborated.
  Evidence-log `conflict_status` still records whether claim-level evidence rows
  conflict after evidence is logged.

## Data / Tool Ingestion

Use in analysis-routing Step 3.4 and ingestion artifacts. These tokens describe
how new material enters Mira before it becomes evidence or calculation input.

`ingestion_route`:

- `public_on_demand`: public API or public page read for a specific task.
- `user_material`: user-provided files, notes, models, screenshots,
  transcripts or exported tables.
- `authorized_provider`: licensed third-party provider or institution-approved
  connector.
- `portfolio_private`: holdings, weights, risk reports, mandates or
  constraints provided by the user.
- `derived_dataset`: retained normalized table, peer table, model output or
  scenario dataset created by Mira or a researcher.
- `none`: no new retained material or dataset enters the workflow.

`ingestion_artifacts`:

- `dataset_manifest`
- `user_material_intake`
- `restricted_source_note`
- `connector_registry`
- `field_map`
- `ingestion_log`
- `waived`

`source_registry_action`:

- `reuse`: existing source record is sufficient.
- `case_local_note`: use an explicit case-local source note.
- `add_source`: add or propose a source registry row.
- `waive`: no retained source record is needed because the material was not
  used for evidence or calculation.

`storage_scope`:

- `tracked_allowed`: may be committed to tracked Mira files.
- `private`: keep under gitignored private state.
- `transient_only`: do not retain raw material after the task.

`redistribution_allowed`:

- `yes`
- `no`
- `derived_only`
- `unknown`

## Judgment Confidence

Use at the delivery layer for any material judgment (see MIRA.md Required Output Discipline and the delivery checklist). These are calibrated bands, not pseudo-precise probabilities.

`judgment_confidence`:

- `low`: directional lean only; evidence is thin or conflicting.
- `medium`: supported by evidence but with material open variables.
- `high`: multiple high-weight, cross-checked claims support it.

Companion fields:

- `confidence_basis`: the evidence and reasoning the band rests on.
- `base_rate_anchor`: the reference class or base rate the judgment is anchored against, when applicable.
- `reversal_condition`: the evidence that would flip or downgrade the judgment.

`judgment_confidence` is about Mira's confidence in a judgment, not about source verification (`verification_status`) or evidence posture. A judgment that rests mainly on `forecast`, `assumption`, `opinion` or `sentiment` inputs cannot be `high`; downgrade it and state the `reversal_condition`.

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

Mira separates three independent language axes. A user may ask in one language, request a deliverable in another, and rely on sources in several — these do not collapse into one field.

`interaction_language`: the language the user is asking in, and the default language Mira answers in.

- Recommended values: `zh-CN`, `en`, `ja`, or other BCP-47-style tags.
- **Determination**: derived from the language of the **current user message**. Do NOT inherit it from the workspace, memory, instruction files, or prior-case language — those are mostly Chinese here, but an English message is `interaction_language=en` and must yield `output_language=en` unless the user overrides.
- Default rule: answer in the user's language. For mixed-language input, keep the dominant language and gloss key terms bilingually once.

`output_language`: the language of a formal deliverable (memo, package, evidence summary).

- Recommended values: `zh-CN`, `en`, `ja`, `mixed` (intentionally bilingual or case-source-driven).
- Scope: required on every formal Mira research output; defaults to `interaction_language` and may be explicitly overridden. `quick_answer` and casual replies inherit `interaction_language` implicitly and need not emit it.

`evidence_languages`: output-level set of the languages the evidence in this output is drawn from, e.g. `[zh-CN, en]`.

- Distinct from the row-level `source_language` in `evidence-log.csv` (one source's original language). The row-level `source_language` and `translation_basis` columns are introduced in the evidence-log v1.2 schema bump; see [../docs/i18n-plan.md](../docs/i18n-plan.md) Phase 1.

Machine tokens, schema field names and file names stay language-invariant regardless of these fields. Only human-readable rendering localizes, via [localization-glossary.csv](localization-glossary.csv).

## Localization Rendering

How outputs render in `output_language` without forking templates or drifting the protocol:

- **Render, don't fork.** Human-facing headings, labels, explanations and follow-up prompts are rendered into `output_language` at delivery time, using [localization-glossary.csv](localization-glossary.csv) for term consistency. Do NOT maintain per-language copies of templates, loops or skills.
- **Never translate the machine layer.** Machine tokens (`quick_map`, `no_action`, `judgment_confidence`, …), schema field names / CSV headers (`research_object`, `claim_text`, `source_language`, …) and file names (`evidence-log.csv`, `investment-memo.md`) stay in their canonical English form in every output language.
- **Token values vs prose.** A controlled-vocabulary token written as a field value stays canonical; only surrounding prose and labels localize. When a token first appears, gloss it once via the glossary, e.g. `快速侦察 (quick_map)`.
- **Glossary is the lookup.** Resolve any domain term or protocol-token display string through `localization-glossary.csv` rather than translating ad hoc, so the same concept renders consistently across cases.
