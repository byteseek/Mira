# {{ research_object }} Actionability Bridge

- research_object: {{ research_object }}
- date: {{ date }}
- source_thesis_ref: {{ source_thesis_ref }}
- price_date: {{ price_date }}
- research_action: {{ research_action }}
- action_boundary: research_action_only_not_trade_instruction

## Setup Type

{{ setup_type }}

Allowed values:

- `watch_only`
- `upgrade_watch`
- `event_setup`
- `post_event_follow_through`
- `valuation_reset_watch`
- `risk_reduction_context`
- `no_action`

## Valuation / Expectation Frame

| item | value |
| --- | --- |
| current_price_or_level | {{ current_price_or_level }} |
| valuation_anchor | {{ valuation_anchor }} |
| what_is_priced_in | {{ what_is_priced_in }} |
| mira_variant | {{ mira_variant }} |
| revision_path | {{ revision_path }} |

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

- `not_applicable`
- `watchlist_only`
- `small_if_confirmed`
- `normal_only_after_confirmation`
- `reduce_risk_context`

## Required Follow-Up

{{ required_followup }}
