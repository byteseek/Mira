# {{ research_object }} Instrument Strategy Gate

- research_object: {{ research_object }}
- date: {{ date }}
- source_actionability_ref: {{ source_actionability_ref }}
- action_boundary: research_framework_only_not_trade_instruction
- gate_policy: ../../data/instrument-strategy-gate.md

## User Objective

| field | value |
| --- | --- |
| objective | {{ objective }} |
| time_window | {{ time_window }} |
| risk_budget_status | {{ risk_budget_status }} |
| instrument_access | {{ instrument_access }} |
| position_context | {{ position_context }} |
| data_status | {{ data_status }} |

## Route Decision

| item | value |
| --- | --- |
| instrument_route | {{ instrument_route }} |
| route_basis | {{ route_basis }} |
| suitable_families | {{ suitable_families }} |
| unsuitable_families | {{ unsuitable_families }} |
| downgraded_to | {{ downgraded_to }} |
| downgrade_reason | {{ downgrade_reason }} |

Use [../../data/controlled-vocabulary.md](../../data/controlled-vocabulary.md)
`instrument_strategy_family` labels for `instrument_route`,
`suitable_families` and `unsuitable_families`.

## Required Data

| data_item | status | why_it_matters |
| --- | --- | --- |
| {{ data_item }} | {{ status }} | {{ why_it_matters }} |

## Risk And Failure Modes

| risk | applies_to | mitigation_or_stop |
| --- | --- | --- |
| {{ risk }} | {{ applies_to }} | {{ mitigation_or_stop }} |

## Next Calculation

{{ next_calculation }}

## Required Follow-Up

{{ required_followup }}
