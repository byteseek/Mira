# Restricted Source Note

- source_note_id: {{ source_note_id }}
- ingestion_id: {{ ingestion_id }}
- research_object: {{ research_object }}
- market_scope: {{ market_scope }}
- prepared_at: {{ YYYY-MM-DD }}
- prepared_by: Mira
- source_class: {{ source_class }}
- authority_level: {{ L1-L6 }}
- provider_or_submitter: {{ provider_or_submitter }}
- source_date: {{ YYYY-MM-DD }}
- as_of_date: {{ YYYY-MM-DD }}
- access_method: {{ access_method }}
- acquisition_mode: {{ acquisition_mode }}
- license_scope: {{ license_scope }}
- storage_scope: {{ tracked_allowed | private | transient_only }}
- redistribution_allowed: {{ yes | no | derived_only | unknown }}
- public_case_use: {{ allowed | metadata_only | blocked }}

## Material Description

{{ short_description_without_restricted_content }}

## Permitted Use

- allowed_use: {{ allowed_use }}
- blocked_use: {{ blocked_use }}
- quote_limit: {{ quote_limit_or_none }}
- raw_storage_allowed: {{ yes_or_no }}
- derived_storage_allowed: {{ yes_or_no }}

## Research Effect

{{ brief_compliant_effect_note }}

## Evidence Mapping

| claim_area | claim_type | evidence_category | treatment | readiness_impact | notes |
| --- | --- | --- | --- | --- | --- |
| {{ claim_area }} | {{ claim_type }} | {{ evidence_category }} | {{ treatment }} | {{ readiness_impact }} | {{ notes }} |

## Refresh / Invalidation

- stale_after: {{ YYYY-MM-DD_or_not_applicable }}
- must_refresh_if: {{ refresh_condition }}

## Publication Boundary

{{ what_can_and_cannot_be_used_in_tracked_or_public_outputs }}
