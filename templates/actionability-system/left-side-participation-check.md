# {{ research_object }} Left-Side Participation Check

- research_object: {{ research_object }}
- date: {{ date }}
- price_date: {{ price_date }}
- source_thesis_ref: {{ source_thesis_ref }}
- action_boundary: research_action_only_not_trade_instruction
- status: {{ status }}

Use this check only when participation is being considered before the main
confirmation variable has arrived. It does not produce a trade instruction. It
decides whether the setup can move from `watch_only` to a research-bound
`left_side_candidate`.

## Setup Classification

| field | value |
| --- | --- |
| current_stage | {{ current_stage }} |
| proposed_stage | {{ proposed_stage }} |
| drawdown_type | {{ drawdown_type }} |
| cycle_type | {{ cycle_type }} |
| thesis_damage_status | {{ thesis_damage_status }} |
| valuation_anchor_quality | {{ valuation_anchor_quality }} |

Allowed `drawdown_type` examples: valuation_compression, cycle_pressure,
sentiment_liquidity_pressure, event_uncertainty, thesis_damage, unknown.

## Reversal Variable

| item | value |
| --- | --- |
| reversal_variable | {{ reversal_variable }} |
| observation_window | {{ observation_window }} |
| evidence_needed | {{ evidence_needed }} |
| next_marginal_buyer | {{ next_marginal_buyer }} |
| buyer_not_in_yet | {{ buyer_not_in_yet }} |
| payoff_source | {{ payoff_source }} |
| repricing_trigger | {{ repricing_trigger }} |

## Further Drawdown Test

If price keeps falling, what does that mean for the thesis?

| path | interpretation | actionability impact |
| --- | --- | --- |
| drawdown_strengthens | {{ drawdown_strengthens_interpretation }} | {{ drawdown_strengthens_impact }} |
| drawdown_neutral | {{ drawdown_neutral_interpretation }} | {{ drawdown_neutral_impact }} |
| drawdown_falsifies | {{ drawdown_falsifies_interpretation }} | {{ drawdown_falsifies_impact }} |

Price falling can improve risk/reward only when the thesis evidence is intact
and the valuation or expectation anchor is credible. If falling price coincides
with weakening evidence, treat it as possible thesis damage, not a better
left-side setup.

## Path Fit And Cycle Burden

| item | value |
| --- | --- |
| required_holding_path | {{ required_holding_path }} |
| likely_pain_path | {{ likely_pain_path }} |
| cycle_duration_risk | {{ cycle_duration_risk }} |
| opportunity_cost_risk | {{ opportunity_cost_risk }} |
| alternative_waiting_condition | {{ alternative_waiting_condition }} |
| position_context_status | {{ position_context_status }} |

Without user-provided holdings, weights, mandate and risk budget, do not infer
whether the path is personally acceptable. State only whether the research setup
requires enduring a full or partial cycle.

## Decision

| field | value |
| --- | --- |
| left_side_check_result | {{ left_side_check_result }} |
| readiness_level | {{ readiness_level }} |
| participation_posture | {{ participation_posture }} |
| confirmation_required | {{ confirmation_required }} |
| invalidation | {{ invalidation }} |
| must_refresh_if | {{ must_refresh_if }} |

Allowed `left_side_check_result` values:

- `pass_as_left_side_candidate`
- `watch_only_until_confirmation`
- `needs_refresh`
- `reject_left_side_setup`

