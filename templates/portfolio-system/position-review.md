# Position Review

- position_id: {{ position_id }}
- research_object: {{ research_object }}
- review_date: {{ review_date }}
- market_scope: {{ market_scope }}
- time_boundary: {{ time_boundary }}
- position_data_status: {{ position_data_status }}
- output_boundary: not_investment_advice; not_trade_instruction
- stale_after: {{ stale_after }}
- must_refresh_if: {{ must_refresh_if }}

## Position Context

- current_weight: {{ current_weight }}
- cost_basis: {{ cost_basis }}
- entry_date: {{ entry_date }}
- entry_thesis_ref: {{ entry_thesis_ref }}
- constraints: {{ constraints }}

## Current Thesis Status

- thesis_state: {{ thesis_state }}
- evidence_quality: {{ evidence_quality }}
- latest_thesis_ref: {{ latest_thesis_ref }}
- key_supporting_claims: {{ key_supporting_claims }}
- disconfirming_evidence: {{ disconfirming_evidence }}

## Facts

{{ facts }}

## Inferences

{{ inferences }}

## Judgments

{{ judgments }}

## Size Vs Evidence Check

- position_sizing_context: {{ position_sizing_context }}
- sizing_basis: {{ sizing_basis }}
- downside_path: {{ downside_path }}
- invalidation_conditions: {{ invalidation_conditions }}
- concentration_or_duplicate_exposure: {{ concentration_or_duplicate_exposure }}

## Review Action

- position_review_action: {{ position_review_action }}
- action_basis: {{ action_basis }}
- required_research_followup: {{ required_research_followup }}

## Source Notes

{{ source_notes }}
