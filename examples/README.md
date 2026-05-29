# Mira Examples

The `cases/` directory contains historical examples that demonstrate how Mira
packages research outputs. They are examples of workflow structure, not live
investment recommendations.

- not_investment_advice: true
- default_case_status: historical_example
- refresh_required_before_use: true

## Recommended Reading Order

1. `cases/aapl-2026-04/`
   Standard single-equity research package. Start here to understand the basic
   `investment-memo.md`, `case-notes.md`, and `evidence-log.csv` structure.

2. `cases/cohr-2026-05/`
   Earnings event package. Use this to understand `earnings-analysis.md`,
   `financial-snapshot.csv`, `peer-comparison.csv`, and thesis-impact handling.

3. `cases/abf-2026-05/`
   Industry concept package. Use this to understand one-page industry maps,
   value-chain mapping, company shortlists, and source-backed industry claims.

4. `cases/etf-discovery-2026-05-09/`
   ETF listing discovery package. Use this for screening and prioritizing new
   product launches before deeper analysis.

5. `cases/etf-listing-analysis-2026-05-09/`
   ETF listing analysis package. Use this for issuer-intent, exposure-map,
   mechanism, and follow-through analysis.

6. `cases/wolf-2026-05/`
   Event-driven micro/small-cap package. Use this to see strategic-catalyst and
   macro overlays combined with stricter evidence downgrades.

7. `cases/a-share-etf-options-underlyings-2026-05-26/`
   Cross-ETF underlying map for A-share option underlyings.

## How To Reuse A Case Pattern

1. Pick the closest package type from `templates/`.
2. Copy the template files into a new `cases/<slug>-<yyyy-mm>/` directory.
3. Fill out metadata first: market, research object, cutoff date, thesis
   horizon, source boundary, and refresh condition.
4. Build the evidence log before treating a conclusion as durable.
5. Write facts, inferences, and judgments as separate sections or clearly
   labeled paragraphs.
6. Add `not_investment_advice: true` to the case README.

Run validation before publishing:

```sh
python3 scripts/validate_repo.py
```
