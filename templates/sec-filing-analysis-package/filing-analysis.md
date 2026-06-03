# {{ company_name }} {{ filing_type }} Filing Analysis

- task_mode: `sec_filing_deep_dive`
- research_object: `filing_or_disclosure`
- company_name: {{ company_name }}
- ticker: {{ ticker }}
- market_scope: {{ market_scope }}
- CIK: {{ cik }}
- accession_number: {{ accession_number }}
- filing_type: {{ filing_type }}
- filing_date: {{ filing_date }}
- report_period_or_event_date: {{ report_period_or_event_date }}
- source_url: {{ source_url }}
- analysis_cutoff_date: {{ analysis_cutoff_date }}
- stale_after: {{ stale_after }}

## Research Question

{{ research_question }}

## Filing Identity And Completeness

- amendment_status: {{ amendment_status }}
- sections_checked: {{ sections_checked }}
- unavailable_sections: {{ unavailable_sections }}
- source_gap_summary: {{ source_gap_summary }}

## Answer First

{{ answer_first }}

## Source Map

| source_id | role | authority_level | source_date | as_of_date | link_or_path |
| --- | --- | --- | --- | --- | --- |
| {{ source_id }} | {{ role }} | {{ authority_level }} | {{ source_date }} | {{ as_of_date }} | {{ link_or_path }} |

## Filing Delta

### Facts

- {{ filing_fact }}

### Management Claims

- {{ management_claim }}

### Inferences

- {{ inference }}

### Judgments

- {{ judgment }}

## Metric Extraction Summary

See `filing-metric-table.csv`.

Key metrics:

- {{ key_metric_1 }}
- {{ key_metric_2 }}
- {{ key_metric_3 }}

## Accounting Quality

See `accounting-quality-check.csv`.

- cash_conversion: {{ cash_conversion }}
- working_capital: {{ working_capital }}
- debt_and_liquidity: {{ debt_and_liquidity }}
- non_gaap_quality: {{ non_gaap_quality }}
- dilution_or_sbc: {{ dilution_or_sbc }}

## Risk-Factor And Language Delta

See `filing-risk-delta.csv`.

- new_or_expanded_risks: {{ new_or_expanded_risks }}
- removed_or_softened_risks: {{ removed_or_softened_risks }}
- thesis_relevant_delta: {{ thesis_relevant_delta }}

## Conflict Check

- release_or_management_conflict: {{ release_or_management_conflict }}
- market_data_conflict: {{ market_data_conflict }}
- prior_mira_conflict: {{ prior_mira_conflict }}
- resolution: {{ conflict_resolution }}

## Thesis Impact

- impact_classification: {{ impact_classification }}
- affected_thesis_variable: {{ affected_thesis_variable }}
- decision_impact: {{ decision_impact }}
- followup_required: {{ followup_required }}

## Refresh Conditions

- stale_after: {{ stale_after }}
- must_refresh_if: {{ must_refresh_if }}
