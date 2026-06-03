# {{ company_name }} ({{ ticker }}) Investment Memo

- market: {{ market }}
- output_language: {{ output_language }}
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
- quant_dependency: {{ quant_dependency }}
- calculation_gate: {{ calculation_gate }}
- calculation_status: {{ calculation_status }}
- not_investment_advice: true

## Decision Header

| field | value |
| --- | --- |
| research_action | {{ research_action }} |
| conviction | {{ conviction }} |
| horizon | {{ horizon }} |
| what_is_priced_in | {{ what_is_priced_in }} |
| invalidation_level_or_condition | {{ invalidation_level_or_condition }} |
| implied_risk_reward | {{ implied_risk_reward }} |
| next_catalyst_date | {{ next_catalyst_date }} |

## Core Conclusion

{{ core_conclusion }}

## Bull Case

{{ bull_case }}

## Bear Case

{{ bear_case }}

## Key Debate

{{ key_debate }}

## Valuation And Expectation Quant

{{ valuation_and_expectation_quant }}

At minimum, include current valuation anchor, what is priced in, base/bull/bear scenario assumptions, downside path, and whether the valuation anchor quality is `high`, `medium`, `low`, or `source_gap`.

If this section relies on derived numbers, include `calculation-ledger` refs or explicit formula notes. If calculation was waived, state `calculation_gap` or `calculation_waived_by_speed` and downgrade actionability.

## Actionability Bridge

{{ actionability_bridge }}

Use this as a research-action bridge only. Do not write autonomous trade instructions. If evidence is insufficient, set `research_action: watch_only` or `no_action`.

## Evidence Quality

{{ evidence_quality }}

## Framework Mismatch Risk

{{ framework_mismatch_risk }}

## Thesis Horizon

- routing_mismatch_risk: {{ routing_mismatch_risk }}
- horizon_mismatch_risk: {{ horizon_mismatch_risk }}
- earnings_to_thesis_bridge: {{ earnings_to_thesis_bridge }}

Use `earnings_to_thesis_bridge: not_applicable` when the memo is not driven by an earnings event.

## Overlay Takeaways

{{ overlay_takeaways }}

## Alpha Signals / Rumor Watch

{{ alpha_signals }}

## Major Risks

{{ major_risks }}

## Tracking Metrics

{{ tracking_metrics }}

## Must Refresh If

{{ must_refresh_if }}
