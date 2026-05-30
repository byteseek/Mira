# CRCL Issuer Economics Snapshot

- as_of: 2026-05-30
- task_mode: `methodology_review` + `single_equity_sample`
- research_object: Circle Internet Group (`CRCL`)
- market_scope: US-listed stablecoin issuer
- time_boundary: Q1 2026 issuer economics and market snapshot as of 2026-05-30
- primary_skill_or_loop: stablecoin company handoff from `stablecoin-regulatory-plumbing-trial.md`
- workflows_under_test: `analysis-routing`, `regulatory_economics_bridge`, `institutional-research-quality-gate`, `variant-perception`
- source_boundary: Q1 2026 10-Q / issuer disclosures, statutory/regulatory sources and a market-data snapshot; no consensus model
- output_status: single-equity validation sample, not a full investment memo
- not_investment_advice: true

## Routing Result

This is the first single-equity handoff from the workflow-validation package. It should not be a full stock recommendation. The correct output is an issuer-economics snapshot that tests whether the stablecoin regulatory map can produce company-level variables.

## Core Question

Does regulatory clarity translate into durable CRCL economics after accounting for reserve yield, USDC circulation, distribution costs, compliance and valuation?

## Issuer Economics Bridge

See [crcl-issuer-economics-bridge.csv](crcl-issuer-economics-bridge.csv).

The working chain is:

`USDC circulation -> reserve balance -> reserve yield -> revenue/reserve income -> distribution and transaction costs -> GAAP net income / adjusted EBITDA -> valuation expectations`

## Facts

- Circle reported Q1 2026 revenue and reserve income of `$694.1M`.
- Circle reported Q1 2026 distribution and transaction costs of `$431.4M`.
- Circle reported Q1 2026 net income of `$55.3M` and adjusted EBITDA of `$151.0M`.
- Circle reported USDC in circulation of `$61.3B` at 2026-03-31 and approximately 27% stablecoin circulation share.
- A market snapshot source showed CRCL market cap of `$25.51B` at a `$102.64` share price as of 2026-05-27.

## Inferences

- The issuer model has real current scale, but distribution and transaction costs absorb a large share of revenue/reserve income.
- CRCL is not just a stablecoin-volume story; it is also a rates, partner-economics and compliance-cost story.
- Regulatory clarity may expand access, but it can also raise compliance burden and invite more regulated competition.
- Market expectations appear demanding relative to annualized Q1 GAAP net income and adjusted EBITDA, but this package lacks consensus estimates and live valuation refresh.

## Simple Run-Rate Check

This is not a valuation model. It is a sanity check to prevent theme-to-stock overreach.

| item | rough Q1 annualized value | note |
| --- | --- | --- |
| revenue and reserve income | `$2.78B` | Q1 `$694.1M` x 4 |
| distribution and transaction costs | `$1.73B` | Q1 `$431.4M` x 4 |
| net income | `$221M` | Q1 `$55.3M` x 4 |
| adjusted EBITDA | `$604M` | Q1 `$151.0M` x 4, company non-GAAP |
| market cap snapshot | `$25.51B` | StockAnalysis as of 2026-05-27 |

Implication: current market cap embeds material growth, margin expansion and/or rate/circulation durability. The package cannot yet prove a variant long thesis.

## Quality Gate

| gate | result |
| --- | --- |
| `reality_basis` | pass: issuer metrics and market snapshot are source-traced |
| `first_order_variable` | pass: reserve income less distribution/compliance costs, not just regulatory clarity |
| `decision_increment` | partial pass: supports watchlist priority and required model work; not a research-action upgrade |
| `disconfirmation_path` | partial pass: needs rate sensitivity, partner terms, consensus revisions and live valuation |

## Trial Judgment

CRCL moves the stablecoin workflow from `regulatory_map_first` to `issuer_economics_watch`.

Do not upgrade to thesis. The evidence supports a focused next research action:

- build a rate/circulation/distribution-cost scenario table
- refresh live market cap and consensus estimates
- compare CRCL economics against COIN distribution exposure and payment-network indirect exposure

## Workflow Review

### What Worked

- The stablecoin handoff avoided a broad fintech basket and selected the direct issuer first.
- `regulatory_economics_bridge` forced the analysis to connect law to actual issuer P&L drivers.
- The quality gate prevented "stablecoin regulation is good" from becoming a CRCL thesis.

### What Failed Or Is Missing

- No consensus or sell-side estimate table.
- No live EV/share-count reconciliation beyond market-cap snapshot.
- No scenario model for rate path, USDC circulation and distribution-cost percentage.
- No peer comparison against COIN, PYPL or payment networks.

## Next Work

1. Build CRCL scenario table across USDC circulation, reserve yield and distribution-cost ratio.
2. Refresh valuation using current share price, diluted shares, cash and consensus estimates.
3. Compare CRCL direct issuer economics against COIN revenue-share exposure.

## Refresh Policy

- stale_after: 2026-06-30
- must_refresh_if:
  - USDC circulation, reserve yield or distribution costs materially change
  - final stablecoin implementation rules differ from current expectations
  - market cap or share price moves materially from the 2026-05-27 snapshot
  - Circle changes partnership economics or reserve disclosure
  - consensus estimates become available or revise materially

