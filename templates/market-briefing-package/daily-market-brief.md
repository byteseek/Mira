# Daily Market Brief: {{ market_scope }}

- briefing_type: daily_market_brief
- as_of: {{ as_of_datetime_with_timezone }}
- market_scope: {{ market_scope }}
- time_boundary: {{ time_boundary }}
- source_boundary: {{ source_boundary }}
- live_data_gate: {{ live_data_gate }}
- quote_time: {{ quote_time_or_source_gap }}
- publish_time: {{ publish_time_or_source_gap }}
- stale_after: {{ stale_after }}
- must_refresh_if: {{ must_refresh_if }}

## Market Snapshot

{{ index_rates_fx_commodities_credit_snapshot }}

## Key Moves

| asset_or_theme | move | source_time | likely_driver | attribution_quality | notes |
| --- | ---: | --- | --- | --- | --- |
| {{ asset_or_theme }} | {{ move }} | {{ source_time }} | {{ likely_driver }} | {{ confirmed_driver_or_plausible_driver_or_contested_driver_or_unexplained_move }} | {{ notes }} |

## Driver Map

### Facts

{{ dated_facts }}

### Inferences

{{ market_inferences }}

### Judgments

{{ judgments_with_confidence_and_reversal_condition }}

## Today Calendar

| time | event | expected_variable | market_relevance | source |
| --- | --- | --- | --- | --- |
| {{ time }} | {{ event }} | {{ expected_variable }} | {{ market_relevance }} | {{ source }} |

## Watchlist Changes

{{ watchlist_changes }}

## Research Escalation Queue

| object | trigger | suggested_route | urgency | source_note | refresh_condition |
| --- | --- | --- | --- | --- | --- |
| {{ object }} | {{ trigger }} | {{ quick_map_or_monitoring_update_or_earnings_event_or_first_pass_research }} | {{ urgency }} | {{ source_note }} | {{ refresh_condition }} |

## Source Notes

{{ source_notes_with_urls_and_as_of_times }}
