# Data and Source Policy

Mira is designed for evidence-tracked research. Open-source use should preserve
source attribution without redistributing material that should remain private,
paid, or restricted.

## Public Examples

Public case packages should be treated as historical examples of the workflow.
They are not live recommendations and may be stale after their stated cutoff or
refresh boundary.

Each public case should include:

- `research_cutoff_date`, `analysis_cutoff_date`, `case_date`, or equivalent.
- `stale_after`, `must_refresh_if`, `Next Refresh`, or equivalent.
- `not_investment_advice: true`.
- An `evidence-log.csv` for source traceability.

## Allowed Source Material

- Public company filings, issuer pages, exchange pages, regulator releases, and
  official datasets.
- Public market-data pages, with the provider and as-of date recorded.
- Short summaries of public articles, research notes, and commentary, with
  source metadata and links.
- Derived calculations when inputs, formulas, and assumptions are visible.
- User-provided files, notes, models, screenshots, transcripts or exports when
  their permission, date, source and storage boundary are recorded.
- Third-party authorized datasets when the user or institution confirms access
  rights and Mira records license scope, storage scope and redistribution
  boundary.

## Ingestion Boundary

Public API pulls, uploaded files, local spreadsheets, vendor exports and
portfolio/risk reports must enter Mira through the ingestion layer before they
support formal conclusions.

Use [data/ingestion-layer.md](data/ingestion-layer.md) and
[templates/ingestion-layer/](templates/ingestion-layer/) to record:

- ingestion route and source posture
- provider or submitter
- license, storage and redistribution scope
- as-of date, source date and refresh rule
- canonical field mapping
- evidence log and calculation ledger mapping

Tools and connectors are acquisition paths, not evidence. A browser result,
API response, file parse or vendor adapter output still needs a source record
or case-local source note and claim-level evidence rows.

Model summaries, model memory and agent-written interpretations are processing
artifacts, not source evidence. They may help identify claims, gaps or next
checks, but they cannot support a durable conclusion until the underlying source
metadata, claim mapping and calculation support are recorded.

## Restricted Source Material

Do not commit:

- Full paid research reports or substantial excerpts from paywalled content.
- Licensed datasets, raw data dumps, or scraped archives that cannot be
  redistributed.
- Private call notes, expert-network transcripts, or confidential materials.
- Personal, brokerage, or account-level data.
- API keys, cookies, tokens, account identifiers or entitlement details.

If a restricted source informs a workflow, record only compliant metadata and a
brief note about how it affected the analysis. Label the source as restricted,
secondary, or low-confidence when appropriate.

Restricted materials should default to `private/` or transient local storage.
Tracked cases may include only compliant metadata, short effect notes and
derived claims that the license permits.

## Source Quality

Use `data/source-policy.md`, `data/source-schema.md`,
`data/source-taxonomy.md`, `data/source-class-map.csv`, and
`data/claim-taxonomy.md` when adding new source records. Facts should prefer
primary sources. Sell-side, social, and community sources can inform framing but
should not replace primary evidence.

When evidence is weak, the conclusion should say so.
