# User Material Intake

- intake_id: {{ intake_id }}
- ingestion_route: user_material
- research_object: {{ research_object }}
- market_scope: {{ market_scope }}
- received_at: {{ YYYY-MM-DD }}
- received_by: Mira
- submitter: {{ submitter }}
- file_or_material_name: {{ file_or_material_name }}
- material_type: {{ filing | model | note | transcript | screenshot | holdings | risk_report | dataset | other }}
- storage_scope: private
- proposed_private_path: private/{{ proposed_path }}
- source_date: {{ YYYY-MM-DD_or_unknown }}
- as_of_date: {{ YYYY-MM-DD_or_unknown }}
- stated_source: {{ stated_source }}
- permission_scope: {{ permission_scope }}
- redistribution_allowed: {{ yes | no | derived_only | unknown }}
- completeness_status: {{ complete | partial | excerpt | unknown }}
- confidentiality_status: {{ public | user_private | paid_restricted | confidential | account_level | unknown }}

## Intake Decision

- accept_for_private_use: {{ yes_or_no }}
- eligible_for_tracked_case: {{ yes_or_no }}
- restricted_source_note_required: {{ yes_or_no }}
- source_registry_action: {{ reuse | case_local_note | add_source | waive }}
- evidence_log_mapping_required: {{ yes_or_no }}
- calculation_ledger_required: {{ yes_or_no }}

## Material Summary

{{ short_summary }}

## Claim Extraction Plan

| claim_area | expected_claim_type | verification_path | allowed_use | readiness_impact |
| --- | --- | --- | --- | --- |
| {{ claim_area }} | {{ claim_type }} | {{ verification_path }} | {{ allowed_use }} | {{ readiness_impact }} |

## Source Gaps

| gap | effect | downgrade |
| --- | --- | --- |
| {{ gap }} | {{ effect }} | {{ downgrade }} |

## Refresh Condition

- stale_after: {{ YYYY-MM-DD_or_not_applicable }}
- must_refresh_if: {{ refresh_condition }}
