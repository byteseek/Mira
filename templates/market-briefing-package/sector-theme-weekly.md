# Sector / Theme Weekly: {{ theme_or_sector }}

- briefing_type: sector_theme_weekly
- as_of: {{ as_of_datetime_with_timezone }}
- market_scope: {{ market_scope }}
- theme_or_sector: {{ theme_or_sector }}
- week_covered: {{ week_covered }}
- source_boundary: {{ source_boundary }}
- stale_after: {{ stale_after }}
- must_refresh_if: {{ must_refresh_if }}

## Theme Snapshot

{{ theme_snapshot }}

## Leader / Laggard Map

| company_or_asset | role_in_theme | weekly_move | likely_driver | source_note | research_handoff |
| --- | --- | ---: | --- | --- | --- |
| {{ company_or_asset }} | {{ role_in_theme }} | {{ weekly_move }} | {{ likely_driver }} | {{ source_note }} | {{ research_handoff }} |

## Fundamental Signal Map

{{ demand_supply_pricing_policy_competition_signal_map }}

## Narrative And Positioning Change

{{ narrative_positioning_change }}

## Company Handoff Queue

| company | handoff_reason | suggested_route | required_sources | refresh_condition |
| --- | --- | --- | --- | --- |
| {{ company }} | {{ handoff_reason }} | {{ route }} | {{ required_sources }} | {{ refresh_condition }} |

## Source Notes

{{ source_notes_with_urls_and_as_of_times }}
