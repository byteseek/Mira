# Research Artifacts

This document keeps the artifact and validation details that do not need to live in the root README.

Use the root [README.md](../README.md) for orientation, [OPERATING_CONTRACT.md](../OPERATING_CONTRACT.md) for the agent loading contract, and [AGENT_QUICKSTART.md](../AGENT_QUICKSTART.md) for prompt-level usage.

## Standard Research Package

A standard research package has three core files:

- `investment memo`: investment judgment, key evidence, source limits, refresh conditions and disconfirmation conditions.
- `evidence log`: source, claim area, claim type, use location, as-of date, confidence and notes.
- `case notes`: intermediate observations, conflicts, gaps and fact/inference separation.
- `research-package-manifest.json`: machine handoff metadata for package type, hero artifacts, support artifacts, readiness, source scope, quant status and refresh conditions.

Every standard package should also state:

- `selected_framework`
- `framework_basis`
- `framework_mismatch_risk`
- `selected_overlays`
- `overlay_basis`
- `stale_after`
- `must_refresh_if`

Templates: [templates/research-package/](../templates/research-package/).

Generate manifests for existing cases with:

```sh
python3 scripts/generate_case_manifests.py cases/<case-id>
python3 scripts/generate_case_manifests.py --all
```

The repository validator checks manifest shape, allowed package types, date fields,
list fields, referenced artifacts and whether every case with an `evidence-log.csv`
has a manifest.

## Thesis System Package

Durable monitored theses can use:

- `thesis-ledger.md`
- `expectation-map.csv`
- `event-delta.md`
- `decision-log.csv`
- `postmortem.md`
- `actionability-bridge.md`
- `thesis-scorecard.csv`

Templates and references:

- [templates/thesis-system/](../templates/thesis-system/)
- [templates/actionability-system/](../templates/actionability-system/)
- [templates/outcome-review/](../templates/outcome-review/)
- [architecture/thesis-system.md](../architecture/thesis-system.md)

## Position And Portfolio Review Package

Position and portfolio review artifacts can include:

- `position-review.md`
- `position-register.csv`
- `portfolio-construction-review.md`
- `portfolio-exposure-review.csv`
- `portfolio-register.csv`

Templates: [templates/portfolio-system/](../templates/portfolio-system/).

These artifacts may describe research actions, sizing context, risk semantics and follow-up queues. They must not be written as executed trades, autonomous orders or portfolio instructions without user-provided holdings, mandate, weights and risk constraints.

## Event And Specialty Packages

### Earnings Analysis

Use [skills/earnings-report-analysis/](../skills/earnings-report-analysis/) for earnings, call, guidance and peer-report events.

Typical package:

- `earnings-analysis`
- `financial-snapshot`
- `peer-comparison`
- `evidence-log`

Template: [templates/earnings-analysis-package/](../templates/earnings-analysis-package/).

### Industry Analysis

Use [skills/industry-concept-analysis/](../skills/industry-concept-analysis/) for technology, supply-chain or industry-concept work before single-stock handoff.

Typical package:

- `industry-map`: one-page industry map plus diligence notes.
- `company-map`: industry-chain position, exposure, pricing power, volume visibility and stock proxy quality.
- `evidence-log`: source trail for concept boundaries, supply/demand, pricing, volume ramp and company mapping.

Template: [templates/industry-analysis-package/](../templates/industry-analysis-package/).

### Macro Analysis

Use [skills/macro-economic-analysis/](../skills/macro-economic-analysis/) for growth, inflation, policy, rates, dollar, credit, liquidity and risk-appetite work.

Macro analysis should state the transmission chain into the relevant asset, sector, thesis or portfolio object. Methodology notes live in [memory/methodologies/macro-regime-analysis.md](../memory/methodologies/macro-regime-analysis.md).

### SEC Filing Analysis

Use [skills/sec-filing-analysis/](../skills/sec-filing-analysis/) for SEC supplements or filing deep dives.

SEC work should preserve filing provenance such as CIK, accession, form, filing date, report period, tag or section and source gaps.

Template: [templates/sec-filing-analysis-package/](../templates/sec-filing-analysis-package/).

### ETF Discovery And Listing Analysis

ETF discovery can use a lightweight package:

- `new-etf-watchlist`
- `discovery-log`
- `evidence-log`

ETF listing analysis can use:

- `etf-listing-analysis`
- `evidence-log`

Use [skills/etf-listing-discovery/](../skills/etf-listing-discovery/) and [skills/etf-listing-analysis/](../skills/etf-listing-analysis/). When ETF analysis points to specific stocks, industries or assets, route into the standard research package or the relevant specialty package.

### Methodology Research

Methodology work uses:

- [templates/methodology-card.md](../templates/methodology-card.md)
- [templates/methodology-queue.csv](../templates/methodology-queue.csv)
- [templates/methodology-review-log.csv](../templates/methodology-review-log.csv)
- [templates/methodology-search-log.csv](../templates/methodology-search-log.csv)
- [templates/variant-perception-checklist.md](../templates/variant-perception-checklist.md)

Use [loops/methodology-research-loop.md](../loops/methodology-research-loop.md).

## Evidence Log And Claim Classification

Formal cases should use the canonical evidence log schema:

- [data/evidence-log-schema.md](../data/evidence-log-schema.md)
- [data/source-taxonomy.md](../data/source-taxonomy.md)
- [data/source-policy.md](../data/source-policy.md)
- [data/evidence-posture-taxonomy.md](../data/evidence-posture-taxonomy.md)

Mira evidence logs classify the information used in conclusions, not only the source itself.

Claim taxonomy: [data/claim-taxonomy.md](../data/claim-taxonomy.md).

Core `claim_type` values include:

- `fact`
- `reported_metric`
- `company_claim`
- `guidance`
- `target`
- `commitment`
- `forecast`
- `assumption`
- `interpretation`
- `opinion`
- `market_pricing`
- `sentiment`
- `rumor_signal`
- `derived_calculation`

LLMs may extract, classify and label long-text claims. The researcher or agent still has to verify whether the claims are sufficient to support the memo conclusion.

## Data And Tool Ingestion Artifacts

When formal research depends on a newly supplied file, public API pull,
authorized provider export, portfolio/risk report or derived dataset, route it
through [data/ingestion-layer.md](../data/ingestion-layer.md) before treating it
as evidence.

Reusable ingestion templates:

- [connector-registry.yaml](../templates/ingestion-layer/connector-registry.yaml):
  authorized data connectors and public API adapters.
- [dataset-manifest.json](../templates/ingestion-layer/dataset-manifest.json):
  retained structured data snapshots.
- [field-map.yaml](../templates/ingestion-layer/field-map.yaml): provider-field
  to Mira canonical-field mapping.
- [ingestion-log.csv](../templates/ingestion-layer/ingestion-log.csv): case or
  private ingestion audit trail.
- [user-material-intake.md](../templates/ingestion-layer/user-material-intake.md):
  user-provided files, models and notes.
- [restricted-source-note.md](../templates/ingestion-layer/restricted-source-note.md):
  metadata-only record for paid, confidential or non-redistributable sources.

Ingestion artifacts do not replace `evidence-log.csv`. They document how data
entered the workflow and what it is allowed to support. Claim-level use still
belongs in the evidence log, and material derived numbers still need
`calculation-ledger.csv` or an explicit formula note.

## Calculation Ledger And Quant Gate

When a number is calculated by Mira or the researcher and affects thesis,
event delta, valuation, peer comparison or actionability, it must not only
appear as `claim_type=derived_calculation` in `evidence-log.csv`.

Derived calculations need one of:

- a `Formula:` note in the evidence row
- a case-local `calculation-ledger.csv` row whose `evidence_log_ref` points back
  to that evidence row

The repository validator checks:

- canonical `calculation-ledger.csv` headers and required fields
- `evidence_log_ref` values against sibling `evidence-log.csv` source IDs
- derived-calculation rows for either a formula note or ledger reference
- manifest `calculation_artifacts` entries for referenced file existence

## Validation

Run the full local quality gate:

```sh
python3 scripts/run_quality_gate.py
```

Validate a formal case:

```sh
python3 scripts/validate_repo.py cases/<case-id>
```

Run a report-only migration check for older cases:

```sh
python3 scripts/validate_repo.py --report-only
```

Current evidence-log drift baseline: [reports/validation/evidence-log-2026-05-29.md](../reports/validation/evidence-log-2026-05-29.md).

SEC supplement or filing package validation:

```sh
python3 scripts/validate_sec_filing_package.py path/to/sec-supplement-source-note.csv
python3 scripts/validate_sec_filing_package.py path/to/sec-filing-package-dir
```

Release-gate validation for a case directory (objective readiness, goal
completion, go/no-go gate coverage, freshness):

```sh
python3 scripts/validate_release.py cases/<case-dir>
# for a real external-release go decision:
python3 scripts/validate_release.py cases/<case-dir> --require-external-ready
```

Long-term workflow release QA evidence is a release snapshot, not a stable product claim. See [cases/long-term-workflow-validation-2026-05-30/release-qa-report-2026-05-30.md](../cases/long-term-workflow-validation-2026-05-30/release-qa-report-2026-05-30.md). The original multi-stage release pipeline (~39 scripts) was removed on 2026-06-10 in favor of `validate_release.py`; it remains recoverable from git history.
