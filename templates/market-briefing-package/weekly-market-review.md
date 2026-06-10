# Weekly Market Review: {{ market_scope }}

- briefing_type: weekly_market_review
- as_of: {{ as_of_datetime_with_timezone }}
- week_covered: {{ week_covered }}
- market_scope: {{ market_scope }}
- source_boundary: {{ source_boundary }}
- live_data_gate: {{ live_data_gate }}
- quote_time: {{ quote_time_or_source_gap }}
- publish_time: {{ publish_time_or_source_gap }}
- stale_after: {{ stale_after }}
- must_refresh_if: {{ must_refresh_if }}

## Week In Review

{{ week_in_review }}

## Dominant Market Variables

| variable | evidence | affected_assets | information_value | next_check |
| --- | --- | --- | --- | --- |
| {{ variable }} | {{ evidence }} | {{ affected_assets }} | {{ low_medium_high }} | {{ next_check }} |

## Rotation

{{ asset_sector_theme_factor_rotation }}

## Calendar And Catalyst Watch

| date | event | expected_variable | market_relevance | source |
| --- | --- | --- | --- | --- |
| {{ date }} | {{ event }} | {{ expected_variable }} | {{ market_relevance }} | {{ source }} |

## Thesis Impact Queue

| object | existing_view_or_gap | weekly_delta | suggested_route | priority | must_refresh_if |
| --- | --- | --- | --- | --- | --- |
| {{ object }} | {{ existing_view_or_gap }} | {{ weekly_delta }} | {{ route }} | {{ priority }} | {{ must_refresh_if }} |

## Facts / Inferences / Judgments

### Facts

{{ facts }}

### Inferences

{{ inferences }}

### Judgments

{{ judgments_with_confidence_and_reversal_condition }}

## Source Notes

{{ source_notes_with_urls_and_as_of_times }}
