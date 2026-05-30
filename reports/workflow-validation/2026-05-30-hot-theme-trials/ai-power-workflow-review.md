# AI Power Workflow Review

- as_of: 2026-05-30
- reviewed_case: `ai-power-grid-trial.md` + `ai-power-regional-bottleneck-map.csv`
- status: first practical iteration complete
- review_type: reverse assessment of Mira workflow

## What The Practical Trial Changed

The workflow moved the topic from broad theme enthusiasm to a map-first research sequence:

1. identify geography of the constraint
2. identify whether the constraint is power, interconnection, transmission, generation, cooling or regulation
3. identify who gets paid and under what approval mechanism
4. only then hand off to single-equity research

This is a better sequence than starting with a basket of "AI power winners."

## Method Scores

| workflow | score | evidence from trial | change needed |
| --- | --- | --- | --- |
| `analysis-routing` | positive | prevented premature single-equity memo | no change |
| `industry-concept-analysis` | positive but incomplete | forced value-chain and profit-pool mapping | add infrastructure-specific regional bottleneck fields |
| `macro-regime-analysis` | mixed | kept power demand tied to grid/resource adequacy | needs a clearer load-to-asset transmission mini-template |
| `institutional-research-quality-gate` | positive | downgraded stock-level conclusion to `map_first` | keep in trial; do not adopt yet |
| `variant-perception` | not yet tested | no consensus proxy built for individual stocks | use only after company-level handoff |

## Proposed Workflow Patch Candidate

Name: `regional_bottleneck_check`

Use when a theme depends on physical infrastructure, local regulation, permitting, grid capacity, logistics or constrained resources.

Fields:

- region
- demand source
- bottleneck type
- bottleneck owner or regulator
- funding / cost recovery mechanism
- public-market exposure path
- evidence status
- disconfirmation metric

This should probably be an overlay inside `industry-concept-analysis`, not a standalone loop.

## Failure Evidence

The current workflow still under-specifies the handoff from theme map to single-name work. The new `company-handoff.csv` helps, but it is not enough to support a stock-level thesis. Each candidate still needs:

- source-traced company filings
- valuation / expectations snapshot
- regulatory and customer concentration review
- refresh and disconfirmation metrics

## Decision

Keep `institutional-research-quality-gate` under trial. Add `regional_bottleneck_check` as a patch candidate, not adopted.

Next validation should either:

- deepen AI power into one single-equity sample, likely `D`, `SO`, `ETN`, `PWR` or `VRT`; or
- run a contrasting hot theme such as GLP-1 to test whether the same quality gate works outside infrastructure.

## Refresh Conditions

- stale_after: 2026-06-30
- must_refresh_if:
  - new PJM/ERCOT/PSC/ACC load forecast or rate-case evidence changes regional priority
  - hyperscaler capex guidance changes materially
  - a company candidate reports earnings that changes exposure purity or backlog evidence
  - `regional_bottleneck_check` fails on another infrastructure theme

