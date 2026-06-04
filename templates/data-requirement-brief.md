# Data Requirement Brief

- research_object: {{ research_object }}
- research_question: {{ research_question }}
- market_scope: {{ market_scope }}
- time_boundary: {{ time_boundary }}
- prepared_at: {{ prepared_at }}
- prepared_by: Mira

## Numeric Question

{{ numeric_question }}

## Required Variables

| variable | definition | source_priority | required_or_optional | notes |
| --- | --- | --- | --- | --- |
| {{ variable }} | {{ definition }} | {{ source_priority }} | {{ required_or_optional }} | {{ notes }} |

## Method

- metric: {{ metric }}
- formula_or_method: {{ formula_or_method }}
- period: {{ period }}
- unit: {{ unit }}
- currency: {{ currency }}
- peer_set: {{ peer_set }}
- comparison_basis: {{ comparison_basis }}

## Source Plan

| priority | source_type | expected_source | use_for | fallback |
| --- | --- | --- | --- | --- |
| {{ priority }} | {{ source_type }} | {{ expected_source }} | {{ use_for }} | {{ fallback }} |

## Missing Data Rules

- missing_data_fallback: {{ missing_data_fallback }}
- downgrade_if_missing: {{ downgrade_if_missing }}
- calculation_gap_condition: {{ calculation_gap_condition }}

## Tool Path

- calculation_required: {{ calculation_required }}
- tool_consent_required: {{ tool_consent_required }}
- recommended_tool_path: {{ recommended_tool_path }}
- ingestion_route: {{ ingestion_route }}
- ingestion_artifacts_required: {{ ingestion_artifacts_required }}
- source_registry_action: {{ source_registry_action }}
- calculation_ledger_required: {{ calculation_ledger_required }}

## Refresh Condition

{{ refresh_condition }}
