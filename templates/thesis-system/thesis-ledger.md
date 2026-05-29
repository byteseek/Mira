# {{ research_object }} Thesis Ledger

- ticker: {{ ticker }}
- market: {{ market }}
- owner_agent: {{ owner_agent }}
- last_updated: {{ last_updated }}
- based_on_cases: {{ based_on_cases }}
- state: {{ state }}
- thesis_horizon: {{ thesis_horizon }}
- selected_framework: {{ selected_framework }}
- selected_overlays: {{ selected_overlays }}
- stale_after: {{ stale_after }}

## Current Thesis

{{ current_thesis }}

## Supporting Claims

| claim_id_or_source | claim_type | evidence_status | why_it_matters |
| --- | --- | --- | --- |
| {{ claim_id_or_source_1 }} | {{ claim_type_1 }} | {{ evidence_status_1 }} | {{ why_it_matters_1 }} |

## Key Assumptions

{{ key_assumptions }}

## Variant View

{{ variant_view }}

## Disconfirming Evidence

{{ disconfirming_evidence }}

## State Change Log

| date | from_state | to_state | trigger | evidence_ref |
| --- | --- | --- | --- | --- |
| {{ date }} | {{ from_state }} | {{ to_state }} | {{ trigger }} | {{ evidence_ref }} |

## Must Refresh If

{{ must_refresh_if }}
