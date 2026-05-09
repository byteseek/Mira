# {{ company_name }} ({{ ticker }}) Earnings Analysis

- market: {{ market }}
- report_period: {{ report_period }}
- report_type: {{ report_type }}
- fiscal_period_end: {{ fiscal_period_end }}
- release_date: {{ release_date }}
- analysis_cutoff_date: {{ analysis_cutoff_date }}
- thesis_horizon: {{ thesis_horizon }}
- stale_after: {{ stale_after }}

## Setup

{{ setup }}

## Headline Result

{{ headline_result }}

## Source Map

{{ source_map }}

## Core Business Map

- core_business: {{ core_business }}
- core_growth: {{ core_growth }}
- core_drag: {{ core_drag }}
- thesis_driver: {{ thesis_driver }}
- non_core_noise: {{ non_core_noise }}

## Price / Volume Bridge

### Pricing

{{ pricing_analysis }}

### Volume

{{ volume_analysis }}

### Growth Attribution

| driver | classification | evidence | durability |
| --- | --- | --- | --- |
| {{ growth_driver_1 }} | {{ growth_driver_1_classification }} | {{ growth_driver_1_evidence }} | {{ growth_driver_1_durability }} |
| {{ growth_driver_2 }} | {{ growth_driver_2_classification }} | {{ growth_driver_2_evidence }} | {{ growth_driver_2_durability }} |

## Financial Snapshot

{{ financial_snapshot_summary }}

## Three-Statement Analysis

### Income Statement

{{ income_statement_analysis }}

### Balance Sheet

{{ balance_sheet_analysis }}

### Cash Flow

{{ cash_flow_analysis }}

## Forward Outlook / Guidance Bridge

| item | analysis |
| --- | --- |
| reported_vs_consensus | {{ reported_vs_consensus }} |
| next_quarter_guidance | {{ next_quarter_guidance }} |
| full_year_guidance | {{ full_year_guidance }} |
| implied_bridge | {{ implied_bridge }} |
| guide_vs_consensus | {{ guide_vs_consensus }} |
| guidance_drivers | {{ guidance_drivers }} |
| guidance_quality | {{ guidance_quality }} |
| estimate_revision_impact | {{ estimate_revision_impact }} |
| guidance_risks | {{ guidance_risks }} |
| transcript_QA_delta | {{ transcript_QA_delta }} |

## Driver Bridge

{{ driver_bridge }}

## Durability Test

{{ durability_test }}

## Peer Earnings Cross-Check

- peer_company: {{ peer_company_name }}
- peer_ticker: {{ peer_ticker }}
- peer_report_period: {{ peer_report_period }}
- peer_selection_reason: {{ peer_selection_reason }}

{{ peer_earnings_cross_check }}

## Management Commentary

{{ management_commentary }}

## Market Expectation And Reaction

{{ market_expectation_and_reaction }}

## Quality Scorecard

| dimension | score | rationale |
| --- | --- | --- |
| growth_quality | {{ growth_quality_score }} | {{ growth_quality_rationale }} |
| pricing_power | {{ pricing_power_score }} | {{ pricing_power_rationale }} |
| volume_durability | {{ volume_durability_score }} | {{ volume_durability_rationale }} |
| margin_quality | {{ margin_quality_score }} | {{ margin_quality_rationale }} |
| cash_conversion | {{ cash_conversion_score }} | {{ cash_conversion_rationale }} |
| balance_sheet_risk | {{ balance_sheet_risk_score }} | {{ balance_sheet_risk_rationale }} |
| guidance_credibility | {{ guidance_credibility_score }} | {{ guidance_credibility_rationale }} |
| guidance_market_delta | {{ guidance_market_delta_score }} | {{ guidance_market_delta_rationale }} |
| peer_relative_quality | {{ peer_relative_quality_score }} | {{ peer_relative_quality_rationale }} |
| thesis_impact | {{ thesis_impact_score }} | {{ thesis_impact_rationale }} |

## Thesis Impact

{{ thesis_impact }}

## Risks And Watch Items

{{ risks_and_watch_items }}

## Fact Vs Inference

{{ fact_vs_inference }}

## Refresh Triggers

{{ refresh_triggers }}
