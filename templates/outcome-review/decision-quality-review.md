# Decision Quality Review

- decision_id: {{ decision_id }}
- research_object: {{ research_object }}
- review_date: {{ review_date }}
- original_decision_date: {{ original_decision_date }}
- outcome_window: {{ outcome_window }}
- market_scope: {{ market_scope }}
- output_boundary: not_investment_advice; not_trade_instruction
- stale_after: {{ stale_after }}
- must_refresh_if: {{ must_refresh_if }}

## Original Record

- original_thesis_ref: {{ original_thesis_ref }}
- original_expectation_map_ref: {{ original_expectation_map_ref }}
- original_decision_log_ref: {{ original_decision_log_ref }}
- original_evidence_log_ref: {{ original_evidence_log_ref }}
- position_context_available: {{ position_context_available }}

## Outcome Window

- start_date: {{ start_date }}
- end_date: {{ end_date }}
- expected_validation_event: {{ expected_validation_event }}
- benchmark_or_peer_set: {{ benchmark_or_peer_set }}
- outcome_data_status: {{ outcome_data_status }}

## Facts Available Then

{{ facts_available_then }}

## Facts Known Now

{{ facts_known_now }}

## Outcome Attribution

- thesis_variable_realization: {{ thesis_variable_realization }}
- market_beta: {{ market_beta }}
- sector_or_factor_move: {{ sector_or_factor_move }}
- multiple_change: {{ multiple_change }}
- estimate_revision: {{ estimate_revision }}
- timing: {{ timing }}
- execution_constraint: {{ execution_constraint }}
- unrelated_luck: {{ unrelated_luck }}
- calculation_gate: {{ calculation_gate }}

## Decision Quality Assessment

- evidence_quality_at_decision: {{ evidence_quality_at_decision }}
- reasoning_quality: {{ reasoning_quality }}
- claim_weighting: {{ claim_weighting }}
- time_horizon_match: {{ time_horizon_match }}
- valuation_expectation_anchor: {{ valuation_expectation_anchor }}
- disconfirming_evidence_handling: {{ disconfirming_evidence_handling }}
- sizing_discipline_if_applicable: {{ sizing_discipline_if_applicable }}
- refresh_discipline: {{ refresh_discipline }}

## Error Classification

{{ error_classification }}

## Methodology Implication

{{ methodology_implication }}

## Required Research Follow-Up

{{ required_research_followup }}

## Source Notes

{{ source_notes }}
