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

## Restricted Source Material

Do not commit:

- Full paid research reports or substantial excerpts from paywalled content.
- Licensed datasets, raw data dumps, or scraped archives that cannot be
  redistributed.
- Private call notes, expert-network transcripts, or confidential materials.
- Personal, brokerage, or account-level data.

If a restricted source informs a workflow, record only compliant metadata and a
brief note about how it affected the analysis. Label the source as restricted,
secondary, or low-confidence when appropriate.

## Source Quality

Use `data/source-policy.md`, `data/source-schema.md`, and
`data/claim-taxonomy.md` when adding new source records. Facts should prefer
primary sources. Sell-side, social, and community sources can inform framing but
should not replace primary evidence.

When evidence is weak, the conclusion should say so.
