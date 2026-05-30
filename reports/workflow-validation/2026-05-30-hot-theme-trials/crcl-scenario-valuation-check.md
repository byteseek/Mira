# CRCL Scenario / Valuation Sanity Check

- as_of: 2026-05-30
- task_mode: `methodology_review` + `single_equity_sample`
- research_object: Circle Internet Group (`CRCL`)
- market_scope: US-listed stablecoin issuer
- time_boundary: Q1 2026 run-rate and market snapshot as of 2026-05-30
- primary_skill_or_loop: follow-up to `crcl-issuer-economics-snapshot.md`
- workflows_under_test: `regulatory_economics_bridge`, `variant-perception`, `institutional-research-quality-gate`
- source_boundary: Q1 2026 company filing metrics + public market-cap snapshot; no consensus estimate table
- output_status: valuation sanity check, not a full investment memo
- not_investment_advice: true

## Purpose

This file closes one validation gap: the CRCL single-equity sample needs at least a basic market-pricing check. The goal is not a full valuation model. The goal is to test whether the workflow can stop a real operating story from becoming an unpriced stock thesis.

## Source Inputs

| input | value | source |
| --- | --- | --- |
| Q1 2026 revenue and reserve income | `$694.1M` | CRCL Q1 2026 10-Q |
| Q1 2026 distribution and transaction costs | `$431.4M` | CRCL Q1 2026 10-Q |
| Q1 2026 net income | `$55.3M` | CRCL Q1 2026 10-Q |
| Q1 2026 adjusted EBITDA | `$151.0M` | CRCL Q1 2026 10-Q, company non-GAAP |
| USDC in circulation | `$61.3B` at 2026-03-31 | CRCL Q1 2026 10-Q |
| market cap working snapshot | `$28.56B` | public market-data snapshot, refresh before live use |

## Q1 Run-Rate

| item | annualized value | market-cap multiple at `$28.56B` |
| --- | --- | --- |
| revenue and reserve income | `$2.78B` | `10.3x` |
| adjusted EBITDA | `$604M` | `47.3x` |
| net income | `$221M` | `129x` |

This does not prove overvaluation. It proves that the stock requires material growth, improved economics, durable rates, or some combination of the three.

## Scenario Table

See [crcl-scenario-table.csv](crcl-scenario-table.csv).

The table uses three simple variables:

- USDC circulation
- annual revenue yield on circulation
- distribution-cost ratio and adjusted EBITDA margin

It intentionally avoids false precision. It is a pressure test, not a DCF.

## Interpretation

### Bear

If USDC circulation weakens or grows slowly, rates compress and partner/distribution economics stay heavy, the market cap becomes hard to support on near-term profitability.

### Base

If USDC grows to `$75B`, revenue yield stays around `4%` and adjusted EBITDA margin resembles Q1 run-rate economics, the stock still trades at roughly `43x` adjusted EBITDA in the simple table.

### Bull

The bull case requires multiple things to go right: USDC circulation around `$120B`, favorable yield, improved cost leverage and better adjusted EBITDA margin. Under that setup, the market cap is closer to `18x` adjusted EBITDA.

## Quality Gate

| gate | result |
| --- | --- |
| `reality_basis` | pass: source-traced Q1 numbers and explicit market-cap snapshot |
| `first_order_variable` | pass: USDC circulation, revenue yield, distribution cost and margin |
| `decision_increment` | pass for workflow: it changes CRCL from issuer snapshot to valuation-sensitive watch |
| `disconfirmation_path` | pass at first level: rate cuts, USDC stagnation, worse revenue share or lower margins weaken the case; stronger circulation and cost leverage strengthen it |

## Trial Judgment

CRCL remains `issuer_economics_watch`, not thesis upgrade.

The scenario check improves the workflow because it shows why a real regulatory/operating story can still be a difficult stock setup. The issue is not whether CRCL is a real business. The issue is whether current market value already prices a large share of the positive scenario.

## Workflow Review

### What Worked

- `regulatory_economics_bridge` carried from law to issuer metrics to valuation variables.
- `variant-perception` correctly stopped at `source_gap` because no consensus estimates were included.
- The quality gate forced a disconfirmation path instead of a directional call.

### What Is Still Missing

- live diluted share count and enterprise value
- consensus revenue/EPS/EBITDA estimates
- partner revenue-share contract detail
- rate-sensitivity bridge from reserve portfolio yield to revenue
- peer comparison with COIN and payment networks

## Next Work

1. Add consensus estimates and valuation comp table.
2. Add rate/circulation sensitivity with explicit reserve-yield assumptions.
3. Decide whether CRCL should become a full investment memo or remain a workflow validation sample.

## Refresh Policy

- stale_after: 2026-06-30
- must_refresh_if:
  - market cap or share price materially changes from the working snapshot
  - USDC circulation or reserve yield changes materially
  - Circle discloses new partner economics or distribution-cost ratio
  - consensus estimates become available or revise materially
  - final stablecoin rules alter reserve or compliance economics

