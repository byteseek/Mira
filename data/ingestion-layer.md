# Data And Tool Ingestion Layer

Mira can use public data, user-provided material and authorized third-party
datasets, but every input must enter the research system through a traceable
ingestion contract.

This layer sits before evidence logging. It answers:

1. What material or dataset entered the workflow?
2. Who is allowed to use it, summarize it or store derived fields?
3. Which canonical Mira fields does it populate?
4. Which claims can it support, and which conclusions must be downgraded?
5. When must it be refreshed or discarded?

Do not let a tool response, uploaded file, API payload or vendor export bypass
the source registry, evidence log or calculation ledger.

## Ingestion Routes

| route | use when | default location | required artifact |
| --- | --- | --- | --- |
| `public_on_demand` | SEC, FRED, BLS, BEA, exchange pages or other public APIs/pages are read for one task | case package or source note | `dataset-manifest.json` when structured data is retained |
| `user_material` | user provides files, notes, models, screenshots, transcripts or exported tables | `private/` by default | `user-material-intake.md` |
| `authorized_provider` | user or institution has a licensed vendor connection such as FactSet, Bloomberg, Visible Alpha, Capital IQ, LSEG or Nasdaq Data Link | private/local adapter output | `connector-registry.yaml` and `dataset-manifest.json` |
| `portfolio_private` | holdings, weights, risk reports, mandate or constraints are provided | `private/portfolio/` | position or portfolio register plus intake note |
| `derived_dataset` | Mira or a researcher creates model outputs, peer tables, valuation scenarios or normalized data | case package or `private/` depending on source rights | `calculation-ledger.csv` or formula note |

If a route is unclear, treat it as `user_material` and keep it private until the
permissions and source posture are explicit.

## Core Principle

Tools are acquisition paths, not evidence. A tool can fetch, parse, normalize or
calculate data, but the research output still needs a source record and a claim
record.

Minimum chain:

```text
tool_or_file -> ingestion artifact -> source record/source note -> evidence log -> calculation ledger when needed -> research conclusion
```

## Required Ingestion Fields

Every retained data input should record:

- `ingestion_id`
- `ingestion_route`
- `research_object`
- `market_scope`
- `received_at`
- `as_of_date`
- `source_date`
- `provider_or_submitter`
- `access_method`
- `acquisition_mode`
- `license_scope`
- `storage_scope`
- `redistribution_allowed`
- `permitted_use`
- `source_class`
- `authority_level`
- `field_coverage`
- `known_failure_modes`
- `refresh_frequency`
- `must_refresh_if`
- `evidence_log_mapping`
- `calculation_ledger_required`

Use `source_gap` when any material field is missing.

## User-Provided Material

User files are first-class inputs, but they are not automatically true,
complete, current or redistributable.

Default rules:

- Store user-specific material under `private/` unless the user explicitly asks
  to promote a de-identified example or product method.
- Record the file name, submitter, provided date, stated source, stated
  permissions and whether the material is complete.
- Extract claim-level records instead of copying long text into tracked cases.
- If the file is paid, confidential, account-level, expert-network, sell-side or
  otherwise restricted, keep only compliant metadata and a brief effect note in
  tracked artifacts.
- If a file lacks date, source or permission context, it can support discovery
  or a working view, not a durable conclusion.

Use [../templates/ingestion-layer/user-material-intake.md](../templates/ingestion-layer/user-material-intake.md).

## Authorized Third-Party Data

Licensed datasets should be connected through adapters, not hard-coded into
research loops.

Adapter design:

```text
provider adapter -> canonical data contract -> Mira evidence/calculation layer
```

The provider adapter handles authentication, rate limits, vendor fields,
entitlements and local caching. Mira consumes canonical fields such as:

- `company_financials`
- `market_price`
- `valuation_snapshot`
- `consensus_estimate`
- `estimate_revision`
- `transcript_claim`
- `ownership_short_interest`
- `options_surface`
- `portfolio_position`
- `macro_series`

Every adapter must state:

- what the license allows
- whether raw data may be stored
- whether derived fields may be stored
- whether provider names or values may be cited
- refresh frequency and latency
- field definitions and known vendor quirks
- fallback source path when the adapter is unavailable

Use [../templates/ingestion-layer/connector-registry.yaml](../templates/ingestion-layer/connector-registry.yaml)
and [../templates/ingestion-layer/field-map.yaml](../templates/ingestion-layer/field-map.yaml).

## Public API Data

Public APIs are preferred over ad hoc scraping when they provide stable fields.

Public API records still need:

- endpoint or dataset name
- query parameters
- retrieval timestamp
- as-of date and period
- units and currency
- transformation notes
- rate-limit or revision caveats

Examples: SEC companyfacts, FRED series observations, BLS series, BEA tables,
Treasury FiscalData, EIA series, CFTC COT.

## Restricted Source Handling

Restricted sources may inform private research, but they cannot be committed as
raw content.

Allowed tracked record:

- source metadata
- permission scope
- short compliant effect note
- claim category and evidence posture
- whether the source blocks publication or actionability

Disallowed tracked record:

- full paid reports
- substantial paywalled excerpts
- private call notes or expert-network transcripts
- account-level holdings unless explicitly de-identified and approved
- vendor raw datasets or bulk exports

Use [../templates/ingestion-layer/restricted-source-note.md](../templates/ingestion-layer/restricted-source-note.md).

## Evidence Mapping

Ingestion artifacts do not replace `evidence-log.csv`.

Mapping rules:

- Reported company metrics from filings or issuer disclosures become
  `reported_metric` or `fact`.
- Vendor consensus values become `forecast`, not facts.
- Price, volume, options and valuation fields become `market_pricing`.
- User notes become `interpretation`, `opinion`, `assumption` or
  `company_claim` unless independently verified.
- Mira-normalized fields become `derived_calculation` and need upstream sources.

If a dataset powers valuation, peer ranking, event reaction, exposure or
portfolio risk claims, create or update `calculation-ledger.csv`.

## Readiness Impact

Data ingestion can upgrade readiness only when it resolves the named gap. It can
also downgrade readiness.

Default downgrades:

- missing source date -> `working_view` or lower
- missing permission scope -> blocks publication
- missing as-of date for market data -> blocks actionability
- missing consensus provider -> `source_gap` for expectation baseline
- restricted source only -> private use, not public package support
- calculation without reproducible inputs -> `calculation_gap`

## Tool Selection Rules

Prefer the narrowest tool that can supply source-backed structured data.

Use:

- browser/search for discovery and public page reading
- public API clients for official structured data
- document/spreadsheet parsers for user-provided files
- provider adapters for licensed datasets
- calculation tools for reproducible derived outputs

Do not use a broad scraping tool when an official API, local file or authorized
adapter is available.

## Required Output When Ingestion Matters

When a formal task depends on newly ingested material, include:

- `ingestion_route`
- `ingestion_artifacts`
- `source_registry_action`: `reuse` / `case_local_note` / `add_source` / `waive`
- `license_scope`
- `storage_scope`
- `evidence_log_mapping`
- `calculation_ledger_required`
- `readiness_impact`
- `must_refresh_if`
