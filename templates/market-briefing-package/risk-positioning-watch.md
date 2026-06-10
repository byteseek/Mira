# Risk / Positioning Watch: {{ market_scope }}

- briefing_type: risk_positioning_watch
- as_of: {{ as_of_datetime_with_timezone }}
- market_scope: {{ market_scope }}
- source_boundary: {{ source_boundary }}
- portfolio_context_provided: {{ yes_or_no }}
- stale_after: {{ stale_after }}
- must_refresh_if: {{ must_refresh_if }}

## Risk Dashboard

| risk_variable | current_state | evidence | affected_assets | severity | next_check |
| --- | --- | --- | --- | --- | --- |
| {{ risk_variable }} | {{ current_state }} | {{ evidence }} | {{ affected_assets }} | {{ low_medium_high }} | {{ next_check }} |

## Positioning And Crowding Notes

{{ positioning_crowding_notes }}

## Macro And Liquidity Stress Map

{{ macro_liquidity_stress_map }}

## Portfolio Relevance

{{ research_only_if_no_holdings_or_portfolio_specific_if_context_provided }}

## Escalation Triggers

| trigger | suggested_route | required_context | action_boundary |
| --- | --- | --- | --- |
| {{ trigger }} | {{ route }} | {{ required_context }} | {{ research_only_or_decision_support_gate_required }} |

## Source Notes

{{ source_notes_with_urls_and_as_of_times }}
