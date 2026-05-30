# Mira Hot Theme Workflow Validation

- as_of: 2026-05-30
- status: ready for colleague workflow review
- audience: institutional research colleagues reviewing Mira's workflow design
- scope: workflow validation, not investment recommendation
- stale_after: 2026-06-30
- not_investment_advice: true

## Purpose

This package tests whether Mira's research workflow can handle current, popular market themes without turning them into unsupported investment theses.

The goal is not to prove that any theme or stock is attractive. The goal is to test whether the workflow:

- routes the research correctly before analysis starts
- separates facts, guidance, assumptions, forecasts and market pricing
- downgrades weak conclusions instead of forcing a thesis
- identifies the first-order variable that would actually matter for investment work
- records what evidence would change the view

## What Was Tested

| area | practical test | result |
| --- | --- | --- |
| AI power / data centers | regional bottleneck map and company handoff | broad AI-power basket was downgraded to `map_first` |
| GLP-1 / metabolic drugs | claim classification and expectation map | approval and product growth were separated from adoption economics |
| stablecoins / tokenized money | regulatory plumbing map and issuer handoff | legal/regulatory facts were separated from issuer economics |
| CRCL | issuer economics and valuation sanity check | real business momentum was tested against market-pricing pressure |

## Main Workflow Lessons

### 1. Start With The Bottleneck

Hot themes often start with a broad beneficiary basket. The AI power trial showed that the better first question is narrower:

Where is the actual constraint, who controls it, who pays to fix it, and who earns economically?

### 2. Classify Claims Before Writing Thesis

The GLP-1 trial showed why claim classification matters. FDA approval, label constraints, company guidance, payer access, patient persistence and margin conversion are different claim types. Treating them as one bullish fact would be a process error.

### 3. Law Is Not Economics

The stablecoin trial showed that regulatory clarity does not automatically identify public-market winners. The investable chain runs through eligible issuers, reserves, rates, distribution, compliance costs and adoption.

### 4. Real Business Does Not Mean Cheap Stock

The CRCL trial showed that company-level evidence still needs market-pricing pressure. A real operating story can still require demanding growth, margin and rate assumptions.

## Current Patch Candidates

| patch | use case | status |
| --- | --- | --- |
| `regional_bottleneck_check` | physical infrastructure themes | trial candidate |
| `clinical_commercial_bridge` | healthcare / clinical-to-commercial themes | trial candidate |
| `regulatory_economics_bridge` | financial-regulatory themes | trial candidate |

None are adopted yet. They need more live cases before becoming formal Mira workflow.

## What This Package Can Be Used For

- reviewing Mira's workflow discipline
- pressure-testing whether hot-theme research stays evidence-bound
- selecting the next case for deeper research
- deciding which workflow patch candidates deserve another trial

## What This Package Should Not Be Used For

- investment recommendations
- live trading or portfolio decisions
- final valuation conclusions
- proof that any workflow patch should be adopted
- proof that CRCL, LLY, NVO, utility or AI-power names are attractive or unattractive

## Publication Readiness

This is ready for institutional colleague workflow review.

Remaining limits:

- not an investment recommendation package
- some source links require manual refresh because automated checks can be blocked
- secondary market/forecast proxies should be replaced before investment use
- decision on whether CRCL remains a workflow sample or becomes a full investment memo

See [publication-readiness-checklist.csv](publication-readiness-checklist.csv).

## File Map

Start here:

- [validation-summary.md](validation-summary.md)
- [workflow-patch-candidates.csv](workflow-patch-candidates.csv)
- [evidence-log.csv](evidence-log.csv)
- [source-link-qa-log.csv](source-link-qa-log.csv)

Theme trials:

- [ai-power-grid-trial.md](ai-power-grid-trial.md)
- [glp1-claim-classification-trial.md](glp1-claim-classification-trial.md)
- [stablecoin-regulatory-plumbing-trial.md](stablecoin-regulatory-plumbing-trial.md)
- [prediction-market-regulatory-economics-trial.md](prediction-market-regulatory-economics-trial.md)

Single-equity sample:

- [crcl-issuer-economics-snapshot.md](crcl-issuer-economics-snapshot.md)
- [crcl-scenario-valuation-check.md](crcl-scenario-valuation-check.md)
- [crcl-consensus-peer-snapshot.md](crcl-consensus-peer-snapshot.md)

## Refresh Conditions

Refresh before relying on the package if:

- hyperscaler capex or AI power-demand evidence changes materially
- GLP-1 label, guidance, payer or prescription evidence changes
- stablecoin implementation rules or issuer economics change
- CRCL market cap, USDC circulation, rates or distribution costs move materially
- any patch candidate fails in another live case
