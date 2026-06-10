# Market Close Wrap: {{ market_scope }}

- briefing_type: market_close_wrap
- as_of: {{ close_datetime_with_timezone }}
- market_scope: {{ market_scope }}
- session: {{ session_date }}
- source_boundary: {{ source_boundary }}
- live_data_gate: {{ live_data_gate }}
- quote_time: {{ quote_time_or_source_gap }}
- stale_after: {{ stale_after }}
- must_refresh_if: {{ must_refresh_if }}

## Close Snapshot

{{ close_snapshot }}

## Move Attribution

| market_segment | close_move | intraday_pattern | likely_driver | attribution_quality | evidence |
| --- | ---: | --- | --- | --- | --- |
| {{ market_segment }} | {{ close_move }} | {{ intraday_pattern }} | {{ likely_driver }} | {{ confirmed_driver_or_plausible_driver_or_contested_driver_or_unexplained_move }} | {{ evidence }} |

## Rotation And Breadth

{{ sector_theme_factor_breadth_summary }}

## Reaction Quality

{{ reaction_quality_assessment }}

## Unexplained Moves

{{ unexplained_moves_and_watch_only_items }}

## Next-Session Watchpoints

{{ next_session_watchpoints }}

## Research Escalation Queue

| object | trigger | suggested_route | urgency | source_note | refresh_condition |
| --- | --- | --- | --- | --- | --- |
| {{ object }} | {{ trigger }} | {{ route }} | {{ urgency }} | {{ source_note }} | {{ refresh_condition }} |

## Source Notes

{{ source_notes_with_urls_and_as_of_times }}
