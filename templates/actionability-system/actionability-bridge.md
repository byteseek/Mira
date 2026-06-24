# {{ research_object }} Actionability Bridge

- research_object: {{ research_object }}
- date: {{ date }}
- source_thesis_ref: {{ source_thesis_ref }}
- price_date: {{ price_date }}
- research_action: {{ research_action }}
- action_boundary: research_action_only_not_trade_instruction
- risk_control_policy: ../../data/actionability-risk-control.md
- instrument_gate_policy: ../../data/instrument-strategy-gate.md

## Setup Type

{{ setup_type }}

Allowed values:

Use [../../data/controlled-vocabulary.md](../../data/controlled-vocabulary.md) `setup_type` tokens.

## Participation Stage

Use [../../data/actionability-risk-control.md](../../data/actionability-risk-control.md)
to separate "worth watching" from "left-side candidate" and "confirmed
participation" before assigning posture.

| item | value |
| --- | --- |
| participation_stage | {{ participation_stage }} |
| stage_basis | {{ stage_basis }} |
| left_side_check_ref | {{ left_side_check_ref }} |
| confirmation_status | {{ confirmation_status }} |

Allowed `participation_stage` values: `watch_only`, `left_side_candidate`,
`confirmed_participation`.

If `participation_stage = left_side_candidate`, attach
[left-side-participation-check.md](left-side-participation-check.md) or state
why it was waived and downgrade the posture.

## Valuation / Expectation Frame

| item | value |
| --- | --- |
| current_price_or_level | {{ current_price_or_level }} |
| valuation_anchor | {{ valuation_anchor }} |
| what_is_priced_in | {{ what_is_priced_in }} |
| mira_variant | {{ mira_variant }} |
| revision_path | {{ revision_path }} |
| implied_risk_reward | {{ implied_risk_reward }} |

## Marginal Buyer / Payoff Bridge

Use [../../data/marginal-buyer-payoff-bridge.md](../../data/marginal-buyer-payoff-bridge.md)
before assigning the participation posture.

| item | value |
| --- | --- |
| decision_direction | {{ decision_direction }} |
| marginal_buyer | {{ marginal_buyer }} |
| remaining_marginal_buyer | {{ remaining_marginal_buyer }} |
| marginal_seller | {{ marginal_seller }} |
| payoff_source | {{ payoff_source }} |
| repricing_trigger | {{ repricing_trigger }} |
| priced_in_status | {{ priced_in_status }} |
| seller_or_buyer_error | {{ seller_or_buyer_error }} |
| failure_mode | {{ failure_mode }} |

## Path Fit / Cycle Burden

| item | value |
| --- | --- |
| thesis_requires_cycle_endurance | {{ thesis_requires_cycle_endurance }} |
| expected_pain_path | {{ expected_pain_path }} |
| evidence_for_waiting_through_cycle | {{ evidence_for_waiting_through_cycle }} |
| alternative_waiting_condition | {{ alternative_waiting_condition }} |
| path_fit_control_status | {{ path_fit_control_status }} |

Do not infer personal tolerance without position data, mandate and risk budget.
This section states the research path burden and whether a non-cycle-enduring
waiting condition exists.

## Scenario And Risk

| scenario | key_assumption | valuation_or_level | implication |
| --- | --- | --- | --- |
| bear | {{ bear_assumption }} | {{ bear_level }} | {{ bear_implication }} |
| base | {{ base_assumption }} | {{ base_level }} | {{ base_implication }} |
| bull | {{ bull_assumption }} | {{ bull_level }} | {{ bull_implication }} |

## Invalidation

{{ invalidation_conditions }}

## Catalyst Calendar

| date_or_window | catalyst | expected_variable | evidence_needed |
| --- | --- | --- | --- |
| {{ date_or_window }} | {{ catalyst }} | {{ expected_variable }} | {{ evidence_needed }} |

## Position Sizing Implication

{{ position_sizing_implication }}

Use qualitative sizing language only:

Use [../../data/controlled-vocabulary.md](../../data/controlled-vocabulary.md) `position_sizing_implication` tokens.

## Participation Risk Control

| control | status | note |
| --- | --- | --- |
| source_control | {{ source_control_status }} | {{ source_control_note }} |
| valuation_control | {{ valuation_control_status }} | {{ valuation_control_note }} |
| payoff_control | {{ payoff_control_status }} | {{ payoff_control_note }} |
| event_control | {{ event_control_status }} | {{ event_control_note }} |
| confirmation_control | {{ confirmation_control_status }} | {{ confirmation_control_note }} |
| path_fit_control | {{ path_fit_control_status }} | {{ path_fit_control_note }} |
| invalidation_control | {{ invalidation_control_status }} | {{ invalidation_control_note }} |
| position_data_control | {{ position_data_control_status }} | {{ position_data_control_note }} |
| refresh_control | {{ refresh_control_status }} | {{ refresh_control_note }} |

If any material control fails, downgrade to `watch_only`, `needs_refresh`,
`research_only`, `small_if_confirmed` or
`normal_only_after_confirmation` rather than forcing a stronger actionability
claim.

## Required Research Follow-Up

{{ required_research_followup }}

If the user explicitly asks about options, short selling, hedges, pair trades,
margin, leverage or other instruments, attach
[instrument-strategy-gate.md](instrument-strategy-gate.md). Otherwise stop at
the participation posture.
