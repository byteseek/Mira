# Mira Output Surface Matrix

This matrix controls how much of Mira's internal research discipline should be
shown to the user at each output depth. It is meant to reduce visible ceremony
without weakening the protocol.

Mira has only three output surfaces: `quick_map`, `standard` and `deep_dive`.
`quick_answer` remains an `interaction_mode`, but it is not a separate surface:
it renders through the selected depth surface, usually `quick_map`, with shorter
prose.

## Surface Tokens

Use these tokens when deciding whether a rule should appear in the answer:

- `internal_check`: run the rule mentally or in notes, but do not show a field
  unless it affects the answer.
- `brief_visible`: show a short natural-language version.
- `full_visible`: show the field, basis and relevant source or artifact link.
- `triggered_visible`: show only if the route or evidence condition triggers it.
- `waive_with_reason`: omit only with an explicit route-specific waiver reason.
- `not_required`: not required for this output surface.

User instructions can override display style, but not evidence quality,
refresh, safety or source-boundary discipline.

## Core Matrix

| discipline | quick_map | standard | deep_dive |
| --- | --- | --- | --- |
| Intent intake and route | `brief_visible` | `full_visible` | `full_visible` |
| `research_object`, `market_scope`, `time_boundary` | `brief_visible` | `full_visible` | `full_visible` |
| Source boundary | `brief_visible` | `full_visible` | `full_visible` |
| Facts / inferences / judgments separation | `brief_visible` | `full_visible` | `full_visible` |
| Material judgment confidence and reversal condition | `brief_visible` | `full_visible` | `full_visible` |
| Evidence log or source note | `brief_visible` source note | `full_visible` evidence/source notes | `full_visible` evidence artifacts |
| Readiness level and blocking gaps | `brief_visible` if not decision-ready | `full_visible` | `full_visible` |
| Refresh condition: `stale_after` / `must_refresh_if` | `brief_visible` | `full_visible` | `full_visible` |
| Critical interaction step | `brief_visible` one high-leverage question, handoff or waiver | `full_visible` follow-up / handoff | `full_visible` decision-grade handoff or waiver |
| Progressive follow-up | `brief_visible` light follow-up or `waive_with_reason` | `full_visible` standard follow-up | `full_visible` decision-grade follow-up when relevant |
| Non-investment-advice / research boundary | `brief_visible` when action language appears | `full_visible` | `full_visible` |

## Triggered Gates

| gate | trigger | quick_map | standard | deep_dive |
| --- | --- | --- | --- | --- |
| Decision pressure | actionability, position, portfolio or instrument language | `triggered_visible` | `full_visible` | `full_visible` |
| Disconfirmation | `decision_pressure` medium/high or framing risk not `none` | `brief_visible` | `full_visible` | `full_visible` |
| Marginal buyer / payoff bridge | buy, sell, add, trim, chase, dip-buying or event participation language | `brief_visible` natural-language buyer/seller + payoff source | `full_visible` | `full_visible` |
| Question expansion lens | comparison, scale shift, trend or anomaly framing materially improves the route | `internal_check` or natural-language follow-up | `triggered_visible` | `full_visible` when it changes evidence path |
| Live data gate | today/now/latest/intraday market or event-reaction question | `brief_visible` time/source/freshness caveat | `full_visible` | `full_visible` |
| Quant / calculation gate | derived numbers, valuation, peer rank, trend or model-dependent conclusion | `brief_visible` source/calculation gap | `full_visible` | `full_visible` with ledger when retained |
| Ingestion gate | newly supplied files, API pulls, vendor exports, portfolio data or retained derived datasets | `triggered_visible` | `full_visible` | `full_visible` |
| Private state boundary | user-specific views, watchlists, holdings, weights or preferences | `triggered_visible` | `full_visible` | `full_visible` |
| Single-equity framework routing | single-equity research | `brief_visible` | `full_visible` | `full_visible` |
| Instrument strategy gate | options, shorting, hedging, pair trades, margin or leverage | `triggered_visible` | `full_visible` | `full_visible` |

## Artifact Surface

| artifact | quick_map | standard | deep_dive |
| --- | --- | --- | --- |
| Evidence log | source notes only | required when creating or updating a package | required |
| Calculation ledger | formula note or gap only | triggered by quant dependency | required when calculations drive conclusions |
| Thesis ledger / expectation map | `not_required` unless continuing a thesis | triggered by thesis/update/actionability route | required for durable thesis work |
| Decision log | `not_required` | triggered by actionability or thesis-state change | required when thesis/actionability changes |
| Actionability bridge | source/posture summary only | triggered by durable actionability route | required when actionability changes a thesis or review |
| Case notes / package manifest | `not_required` | required for package work | required |

## Minimum Surface Contracts

### `quick_map`

Use for "看一下", early triage or unclear source boundary. Minimum visible
surface:

- object / market / time boundary in one line when useful
- core judgment
- if live market data is triggered, quote/publish time and freshness caveat
- key facts versus inferences, at least in prose
- largest `source_gap` or `calculation_gap`
- `stale_after` or `must_refresh_if`
- one route-bound, object-specific critical interaction: a light follow-up,
  workflow handoff or explicit waiver

If `interaction_mode=quick_answer`, keep this surface compact: answer first,
then only show the source boundary, uncertainty, refresh/reversal condition and
critical interaction in the smallest useful form. The critical interaction must
still appear as one brief object-specific follow-up / handoff, or as
`followup_prompt_mode=none` with an explicit waiver reason.

### `standard`

Use for normal research, updates, earnings packages and first-pass company
coverage. Minimum visible surface:

- routed task card and source boundary
- facts / inferences / judgments
- evidence log or source notes
- triggered gates and named gaps
- readiness level
- refresh condition
- critical interaction step: follow-up, handoff or waiver
- standard follow-up with at least one pricing-variable, consensus,
  falsification or next-route question when more than one follow-up is shown

### `deep_dive`

Use for long-horizon thesis, complex valuation, SEC deep dive, methodology work,
PM review or portfolio construction. Minimum visible surface:

- full routing and evidence posture
- complete triggered artifacts
- explicit calculations or ledgers when conclusions depend on numbers
- thesis, expectation, decision or postmortem artifacts when applicable
- decision-grade critical interaction: blocking clarification, workflow
  handoff, follow-up continuation, rung progression or explicit waiver

## Failure Modes This Matrix Prevents

- treating `quick_map` as a casual answer with no follow-up
- treating progressive follow-up as an optional closing line instead of a
  workflow control point
- turning every `quick_answer` interaction into a full compliance template
- hiding triggered risks such as quant dependency or actionability pressure
- showing package-only artifacts before they improve the answer
- omitting refresh conditions because the answer is short
