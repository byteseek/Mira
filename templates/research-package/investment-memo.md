# {{ company_name }} ({{ ticker }}) Investment Memo

- market: {{ market }}
- research_question: {{ research_question }}
- research_cutoff_date: {{ research_cutoff_date }}
- task_mode: {{ task_mode }}
- research_object: {{ research_object }}
- routing_basis: {{ routing_basis }}
- selected_framework: {{ selected_framework }}
- framework_basis: {{ framework_basis }}
- selected_overlays: {{ selected_overlays }}
- overlay_basis: {{ overlay_basis }}
- selected_lenses: {{ selected_lenses }}
- lens_basis: {{ lens_basis }}
- financial_data_through: {{ financial_data_through }}
- price_date: {{ price_date }}
- thesis_horizon: {{ thesis_horizon }}
- horizon_bucket: {{ horizon_bucket }}
- horizon_basis: {{ horizon_basis }}
- stale_after: {{ stale_after }}

## Core Conclusion

{{ core_conclusion }}

## Bull Case

{{ bull_case }}

## Bear Case

{{ bear_case }}

## Key Debate

{{ key_debate }}

## Framework Mismatch Risk

{{ framework_mismatch_risk }}

## Thesis Horizon

- routing_mismatch_risk: {{ routing_mismatch_risk }}
- horizon_mismatch_risk: {{ horizon_mismatch_risk }}
- earnings_to_thesis_bridge: {{ earnings_to_thesis_bridge }}

Use `earnings_to_thesis_bridge: not_applicable` when the memo is not driven by an earnings event.

## Overlay Takeaways

{{ overlay_takeaways }}

## Major Risks

{{ major_risks }}

## Tracking Metrics

{{ tracking_metrics }}

## Must Refresh If

{{ must_refresh_if }}
