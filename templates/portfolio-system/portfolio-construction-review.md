# Portfolio Construction Review

- portfolio_id: {{ portfolio_id }}
- book_scope: {{ book_scope }}
- review_scope: {{ review_scope }}
- review_date: {{ review_date }}
- market_scope: {{ market_scope }}
- output_boundary: not_investment_advice; not_trade_instruction
- stale_after: {{ stale_after }}
- must_refresh_if: {{ must_refresh_if }}

## Scope

- holdings_source: {{ holdings_source }}
- thesis_index_ref: {{ thesis_index_ref }}
- constraints: {{ constraints }}
- calculation_gate: {{ calculation_gate }}

## Facts

{{ facts }}

## Exposure Map

{{ exposure_map }}

## Concentration And Duplicate Bets

{{ concentration_and_duplicate_bets }}

## Thesis Conflicts

{{ thesis_conflicts }}

## Stale Or Weak-Evidence Positions

{{ stale_or_weak_evidence_positions }}

## Position Review Queue

{{ position_review_queue }}

## Judgments

{{ judgments }}

## Source Notes

{{ source_notes }}
