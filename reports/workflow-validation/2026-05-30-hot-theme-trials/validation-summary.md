# Hot Theme Workflow Validation Summary

- as_of: 2026-05-30
- status: colleague-review ready workflow validation package
- publication_state: ready_for_colleague_workflow_review
- market_scope: US/global public-market themes
- trials_completed: 5
- themes: AI power / GLP-1 / stablecoins / CRCL issuer sample
- not_investment_advice: true

## Executive Readout

The practical trials now support sharing this package with institutional colleagues for workflow review. It is not an investment recommendation package and should not be used for live portfolio decisions.

What is working:

- Routing is preventing premature single-stock memos.
- Claim classification is preventing fact/guidance/assumption collapse.
- The institutional quality gate is downgrading broad hot-theme claims into map-first or expectation-map-first research actions.
- Each theme produced at least one concrete workflow patch candidate.
- The first single-equity handoff produced a company economics snapshot instead of a theme-driven stock thesis.
- The first valuation sanity check showed how to pressure-test a real operating story against market pricing.
- A public-facing README now exists, with explicit use limits and stale-after conditions.
- The CRCL sample now includes a consensus/peer proxy, not just company filings and a market-cap snapshot.
- `regulatory_economics_bridge` has a second independent regulatory-financial validation case.
- Source QA status is documented in `source-link-qa-log.csv`.

What is still not ready for investment use:

- Consensus evidence remains secondary/proxy-based rather than a full institutional estimate set.
- Several source trails still need deeper extraction from filings, rate cases, labels, or company reports.
- The first single-equity sample is a snapshot, not a complete investment memo.
- Patch candidates remain trial candidates, not adopted core workflow.

## Trial Results

| theme | practical output | workflow result | conclusion state | patch candidate |
| --- | --- | --- | --- | --- |
| AI power / data-center grid bottleneck | regional bottleneck map + company handoff | positive | `map_first` | `regional_bottleneck_check` |
| GLP-1 / metabolic drugs | claim classification + expectation map | positive | `watch / expectation_map_needed` | `clinical_commercial_bridge` |
| stablecoins / tokenized money | regulatory plumbing map + issuer handoff | positive | `regulatory_map_first` | `regulatory_economics_bridge` |
| CRCL issuer economics | single-equity issuer snapshot + scenario/valuation check | positive but incomplete | `issuer_economics_watch` | `regulatory_economics_bridge` |
| prediction markets / event contracts | regulatory economics map + company handoff | positive | `regulatory_map_first / source_gap_watch` | `regulatory_economics_bridge` |

## Cross-Case Lessons

### 1. Start With The Bottleneck, Not The Basket

AI power showed that broad beneficiary baskets are dangerous. The first useful question was regional and mechanical: where is power physically deliverable, who funds upgrades, and who earns under regulation?

### 2. Classify Claims Before Building Thesis

GLP-1 showed that strong facts can still produce bad conclusions if the workflow collapses approval, label, guidance, adoption, reimbursement and margin into one thesis.

### 3. Law Is Not Economics

Stablecoins showed that regulatory clarity is only the start. Issuer economics still depend on reserves, rates, distribution, compliance and adoption.

### 4. The Quality Gate Is Useful, But Should Stay Trial

The four-question gate improved all three cases:

- reality basis
- first-order variable
- decision increment
- disconfirmation path

But it should remain under trial because there is not yet enough evidence that it works across completed single-equity memos.

## Workflow Patch Candidates

See [workflow-patch-candidates.csv](workflow-patch-candidates.csv).

Current status:

- `regional_bottleneck_check`: promising for infrastructure themes, not adopted
- `clinical_commercial_bridge`: promising for healthcare themes, not adopted
- `regulatory_economics_bridge`: second-case validated trial for financial-regulatory themes, not adopted

## Publication Gap

This package is ready to share with institutional colleagues as a workflow-validation draft.

Remaining gaps before adopting workflow changes:

1. Convert the strongest patch candidates into concise workflow references or reject them.
2. Review whether the CRCL snapshot should be expanded into a full investment memo or remain a workflow sample.
3. Replace secondary market/forecast proxies with primary institutional data before investment use.
4. Run another non-crypto financial-regulatory case if adopting `regulatory_economics_bridge` into core workflow.

## Next Best Step

The highest-value next step is a single-equity sample, not another theme scan.

Recommended sequence:

1. Share [PUBLIC_README.md](PUBLIC_README.md) and [validation-summary.md](validation-summary.md) for colleague workflow review.
2. Decide whether `regulatory_economics_bridge` should be formalized as a reference or kept under trial.
3. Decide whether CRCL remains a workflow sample or becomes a full memo.

## Refresh Policy

- stale_after: 2026-06-30
- must_refresh_if:
  - hyperscaler capex or power-demand evidence changes materially
  - LLY/NVO guidance, label, payer or prescription evidence changes
  - stablecoin implementation rules or issuer economics change
  - any single-equity trial contradicts current patch-candidate value
