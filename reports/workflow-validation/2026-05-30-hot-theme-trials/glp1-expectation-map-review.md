# GLP-1 Expectation Map Review

- as_of: 2026-05-30
- reviewed_case: `glp1-claim-classification-trial.md` + `glp1-expectation-map.csv`
- status: second practical iteration complete
- review_type: reverse assessment of Mira workflow

## What The Iteration Changed

The first GLP-1 pass separated claims. The expectation-map pass added a second guardrail: even when the facts are real, the workflow still cannot infer variant opportunity without market-expectation evidence.

The resulting sequence is:

1. classify claims
2. map each claim to an expectation variable
3. identify which variables are already visible in company guidance and reported metrics
4. mark missing market-pricing and payer/prescription evidence as `source_gap`
5. decide whether a thesis-system update is justified

## Current Decision

GLP-1 should stay at `watch / expectation_map_needed`, not thesis upgrade.

Reason:

- reported product momentum is real
- regulatory approval and label constraints are real
- oral GLP-1 can be a major category variable
- but the package lacks independent payer, prescription, net-price and market-expectation evidence

The right next output is not a full investment memo. It is a focused LLY/NVO expectation-map update with consensus/valuation inputs.

## Method Scores

| workflow | score | evidence from trial | change needed |
| --- | --- | --- | --- |
| `analysis-routing` | positive | avoided single-company memo before claim and expectation mapping | no change |
| `llm-claim-classification` | positive | prevented approval/guidance/assumption collapse | keep under trial |
| `institutional-research-quality-gate` | positive | downgraded oral GLP-1 market expansion from thesis to scenario variable | keep under trial |
| `institutional-thesis-system` | mixed | expectation map is useful, but thesis state update is premature without pricing/consensus evidence | use only after consensus/valuation snapshot |
| `variant-perception` | not ready | explicit market expectation gap remains | do not use for actionability yet |

## Workflow Patch Candidate Assessment

`clinical_commercial_bridge` looks useful after this trial because claim classification alone was not enough. The bridge forced a commercial chain:

`approval -> label -> access -> adoption -> persistence -> net price -> margin / cash flow`

However, it should remain a patch candidate. It needs at least one more healthcare or medtech case before adoption.

## Failure Evidence

The package still lacks:

- third-party prescription data
- payer/formulary evidence
- gross-to-net or realized-price bridge
- independent consensus estimate revisions
- valuation or market-pricing snapshot

Because these are missing, any strong LLY/NVO stock-level conclusion would violate Mira's quality gate.

## Proposed Next Trial

Use one of two paths:

- continue GLP-1 into LLY/NVO consensus and valuation snapshot
- switch to stablecoins to test regulatory plumbing and issuer-economics workflow

## Refresh Conditions

- stale_after: 2026-06-30
- must_refresh_if:
  - Lilly or Novo updates product guidance, supply, label, launch timing or pricing commentary
  - third-party prescription or payer evidence becomes available
  - consensus estimates or valuation moves enough to change priced-in status
  - safety or comparative efficacy data changes the standard-of-care map

