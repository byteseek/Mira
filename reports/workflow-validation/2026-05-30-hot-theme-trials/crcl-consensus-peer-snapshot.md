# CRCL Consensus / Peer Snapshot

- as_of: 2026-05-30
- task_mode: `methodology_review` + `single_equity_sample`
- research_object: Circle Internet Group (`CRCL`)
- market_scope: US-listed stablecoin issuer and adjacent peer `COIN`
- time_boundary: current public market/peer data as of 2026-05-30
- primary_skill_or_loop: follow-up to `crcl-scenario-valuation-check.md`
- workflows_under_test: `variant-perception`, `regulatory_economics_bridge`, `institutional-research-quality-gate`
- source_boundary: public forecast/financial summary pages, CRCL Q1 2026 filing metrics, Coinbase Q1 2026 shareholder materials
- output_status: consensus/peer proxy snapshot, not a full investment memo
- not_investment_advice: true

## Purpose

This closes the readiness gap that the CRCL sample lacked any consensus or peer proxy. It still does not create a full valuation model. It adds enough market-expectation context to decide whether a stock-level thesis would be premature.

## Snapshot Map

See [crcl-consensus-peer-snapshot.csv](crcl-consensus-peer-snapshot.csv).

## What Changed

Before this step, CRCL had:

- company-reported issuer economics
- a scenario table
- a market-cap sanity check

After this step, CRCL also has:

- a public analyst-forecast / price-target proxy
- a public market/financial summary proxy
- an adjacent peer comparison against COIN stablecoin-related economics

## Peer Logic

`CRCL` is the cleaner direct issuer exposure. The core economics are USDC circulation, reserve yield and distribution cost.

`COIN` is not a clean issuer comp. It is a distribution/ecosystem peer with exchange and crypto-market beta. It is useful because stablecoin economics can show up through partner and platform revenue, but it cannot be used as a simple valuation comp without separating crypto trading activity and subscription/services revenue.

## Variant View

The variant view is still not strong enough for a thesis upgrade.

Facts supporting interest:

- CRCL has direct issuer economics and real USDC circulation scale.
- Stablecoin regulation creates a clearer operating framework.
- COIN comparison helps separate issuer economics from distribution exposure.

Facts limiting actionability:

- market cap and simple run-rate multiples already imply substantial growth and margin improvement
- consensus/forecast sources are secondary, not a full institutional estimate set
- EV, diluted share count and long-term estimate bridge remain missing
- COIN is an imperfect peer because crypto beta can dominate stablecoin economics

## Quality Gate

| gate | result |
| --- | --- |
| `reality_basis` | pass: source-traced filings, market data proxy and peer source |
| `first_order_variable` | pass: issuer economics and valuation expectations, not just regulation |
| `decision_increment` | pass for workflow: market-pricing gap moves from missing to partial |
| `disconfirmation_path` | partial: needs full consensus, peer multiples and partner-economics detail |

## Trial Judgment

CRCL remains `issuer_economics_watch`.

This snapshot improves the validation package because it demonstrates the right behavior: when market-pricing evidence is incomplete, Mira should name the gap and stop short of an actionability claim.

## Workflow Review

### What Worked

- `variant-perception` can now run at a weak/proxy level instead of being fully blocked.
- `regulatory_economics_bridge` held up through law, issuer metrics, scenario analysis and peer comparison.
- The readiness checklist can move market-pricing sanity check from partial-with-missing-proxy toward pass-with-residual-gaps.

### What Is Still Missing

- primary consensus dataset
- explicit EV and diluted share count reconciliation
- CRCL long-term revenue / EBITDA / EPS forecast bridge
- COIN stablecoin revenue-share contract detail
- valuation comp table with normalized growth/margins

## Next Work

1. Decide whether `regulatory_economics_bridge` can be tested on a second regulatory-financial case.
2. If the package is being prepared for colleague review, keep CRCL as a workflow sample rather than a full investment memo.
3. Finalize publication language after source-link QA.

## Refresh Policy

- stale_after: 2026-06-30
- must_refresh_if:
  - CRCL price, market cap or analyst forecast changes materially
  - Circle reports updated USDC circulation, reserve income or distribution cost
  - Coinbase reports materially different stablecoin revenue economics
  - final stablecoin rules change issuer economics

