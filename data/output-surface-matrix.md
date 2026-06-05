# Mira Output Surface Matrix

This matrix controls how much of Mira's internal research discipline should be
shown to the user at each output depth. It is meant to reduce visible ceremony
without weakening the protocol.

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

| discipline | quick_answer | quick_map | standard | deep_dive |
| --- | --- | --- | --- | --- |
| Intent intake and route | `internal_check` | `brief_visible` | `full_visible` | `full_visible` |
| `research_object`, `market_scope`, `time_boundary` | `brief_visible` when ambiguous | `brief_visible` | `full_visible` | `full_visible` |
| Source boundary | `brief_visible` when source quality matters | `brief_visible` | `full_visible` | `full_visible` |
| Facts / inferences / judgments separation | `internal_check`, visible if risk of confusion | `brief_visible` | `full_visible` | `full_visible` |
| Material judgment confidence and reversal condition | `brief_visible` for the main judgment | `brief_visible` | `full_visible` | `full_visible` |
| Evidence log or source note | `brief_visible` source note | `brief_visible` source note | `full_visible` evidence/source notes | `full_visible` evidence artifacts |
| Readiness level and blocking gaps | `internal_check` | `brief_visible` if not decision-ready | `full_visible` | `full_visible` |
| Refresh condition: `stale_after` / `must_refresh_if` | `brief_visible` | `brief_visible` | `full_visible` | `full_visible` |
| Progressive follow-up | `brief_visible` or `waive_with_reason` | `brief_visible` light follow-up or `waive_with_reason` | `full_visible` standard follow-up | `full_visible` decision-grade follow-up when relevant |
| Non-investment-advice / research boundary | `internal_check`, visible if action language appears | `brief_visible` when action language appears | `full_visible` | `full_visible` |

## Triggered Gates

| gate | trigger | quick_answer | quick_map | standard | deep_dive |
| --- | --- | --- | --- | --- | --- |
| Decision pressure | actionability, position, portfolio or instrument language | `triggered_visible` | `triggered_visible` | `full_visible` | `full_visible` |
| Disconfirmation | `decision_pressure` medium/high or framing risk not `none` | `brief_visible` | `brief_visible` | `full_visible` | `full_visible` |
| Quant / calculation gate | derived numbers, valuation, peer rank, trend or model-dependent conclusion | `brief_visible` if it changes confidence | `brief_visible` source/calculation gap | `full_visible` | `full_visible` with ledger when retained |
| Ingestion gate | newly supplied files, API pulls, vendor exports, portfolio data or retained derived datasets | `triggered_visible` | `triggered_visible` | `full_visible` | `full_visible` |
| Private state boundary | user-specific views, watchlists, holdings, weights or preferences | `triggered_visible` | `triggered_visible` | `full_visible` | `full_visible` |
| Single-equity framework routing | single-equity research | `internal_check` unless framework drives answer | `brief_visible` | `full_visible` | `full_visible` |
| Instrument strategy gate | options, shorting, hedging, pair trades, margin or leverage | `triggered_visible` | `triggered_visible` | `full_visible` | `full_visible` |

## Artifact Surface

| artifact | quick_answer | quick_map | standard | deep_dive |
| --- | --- | --- | --- | --- |
| Evidence log | `not_required` | source notes only | required when creating or updating a package | required |
| Calculation ledger | `not_required` | formula note or gap only | triggered by quant dependency | required when calculations drive conclusions |
| Thesis ledger / expectation map | `not_required` | `not_required` unless continuing a thesis | triggered by thesis/update/actionability route | required for durable thesis work |
| Decision log | `not_required` | `not_required` | triggered by actionability or thesis-state change | required when thesis/actionability changes |
| Case notes / package manifest | `not_required` | `not_required` | required for package work | required |

## Minimum Surface Contracts

### `quick_answer`

Use for narrow questions or user requests for a short answer. Minimum visible
surface:

- answer the question directly
- state the key source boundary or uncertainty when it matters
- include the main refresh or reversal condition when the claim is time-sensitive
- include follow-up only if it would materially improve the next step, otherwise
  `followup_prompt_mode=none` may be waived in prose

### `quick_map`

Use for "看一下", early triage or unclear source boundary. Minimum visible
surface:

- object / market / time boundary in one line when useful
- core judgment
- key facts versus inferences, at least in prose
- largest `source_gap` or `calculation_gap`
- `stale_after` or `must_refresh_if`
- one route-bound, object-specific light follow-up, unless explicitly waived

### `standard`

Use for normal research, updates, earnings packages and first-pass company
coverage. Minimum visible surface:

- routed task card and source boundary
- facts / inferences / judgments
- evidence log or source notes
- triggered gates and named gaps
- readiness level
- refresh condition
- standard follow-up

### `deep_dive`

Use for long-horizon thesis, complex valuation, SEC deep dive, methodology work,
PM review or portfolio construction. Minimum visible surface:

- full routing and evidence posture
- complete triggered artifacts
- explicit calculations or ledgers when conclusions depend on numbers
- thesis, expectation, decision or postmortem artifacts when applicable
- decision-grade follow-up or explicit waiver

## Failure Modes This Matrix Prevents

- treating `quick_map` as a casual answer with no follow-up
- turning every quick answer into a full compliance template
- hiding triggered risks such as quant dependency or actionability pressure
- showing package-only artifacts before they improve the answer
- omitting refresh conditions because the answer is short
