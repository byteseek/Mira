# Prediction Markets Regulatory Economics Trial

- as_of: 2026-05-30
- task_mode: `methodology_review` + `macro_asset_or_regime`
- research_object: prediction markets / event contracts
- market_scope: US regulatory-financial market structure, public proxies first
- time_boundary: current regulatory setup and platform product evidence as of 2026-05-30
- primary_skill_or_loop: `regulatory_economics_bridge` second-case validation
- workflows_under_test: `analysis-routing`, `macro-regime-analysis`, `llm-claim-classification`, `institutional-research-quality-gate`
- source_boundary: CFTC/regulatory materials, Robinhood product/financial materials, public proxy handoff; no company valuation model
- output_status: second-case patch validation, not a company investment memo
- not_investment_advice: true

## Routing Result

This should not start as a HOOD or COIN memo. The right first pass is regulatory economics because the investable question is whether event-contract permission, venue eligibility, product scope and platform economics can turn prediction-market demand into public-company earnings.

## Core Question

Does `regulatory_economics_bridge` work outside stablecoins?

The prediction-market chain is:

`regulatory jurisdiction -> eligible venue -> allowed contract scope -> user adoption / liquidity -> take rate / revenue share -> compliance cost -> public-company exposure`

## Regulatory Economics Map

See [prediction-market-regulatory-economics-map.csv](prediction-market-regulatory-economics-map.csv).

## Facts

- Event contracts and prediction markets are an active regulatory boundary area.
- Public-market exposure is indirect. HOOD is a product/distribution candidate; Kalshi and Polymarket are more direct but private; COIN/IBKR/CME are adjacent screens.
- Current public-company disclosures do not isolate prediction-market economics.

## Inferences

- The first-order variable is not "prediction markets are popular." It is whether permitted products can generate durable volume, take rate and margin inside a regulated venue.
- Product launch evidence is weaker than regulatory permission plus volume/revenue evidence.
- The public-company handoff must distinguish direct venue economics, distribution economics and adjacent market-structure exposure.

## Trial Judgment

This is a successful second-case validation for `regulatory_economics_bridge` at the map-first level.

Current state should be `regulatory_map_first / source_gap_watch`, not stock-level thesis.

## Quality Gate

| gate | result |
| --- | --- |
| `reality_basis` | pass for regulatory and product-surface evidence |
| `first_order_variable` | pass after compression: venue permission, product scope, volume, take rate and compliance cost |
| `decision_increment` | pass for workflow: validates `regulatory_economics_bridge` beyond stablecoins |
| `disconfirmation_path` | partial: needs volume, fee, user retention and enforcement/product-scope evidence |

## Workflow Review

### What Worked

- `regulatory_economics_bridge` generalized from stablecoins to prediction markets.
- Claim classification prevented product availability from being treated as revenue evidence.
- The quality gate downgraded HOOD/COIN/IBKR/CME to handoff/watch candidates instead of forcing a stock conclusion.

### What Failed Or Is Missing

- Source trail needs specific CFTC orders/dockets before any formal memo.
- Public companies do not yet disclose isolated prediction-market economics.
- No market-pricing or consensus estimate proxy for prediction-market contribution.

## Patch Candidate Decision

`regulatory_economics_bridge` now has two case validations:

- stablecoins / CRCL
- prediction markets / event contracts

It should still not be fully adopted, because both cases are financial-regulatory and the second case is map-level rather than full single-equity. But the patch candidate can be upgraded from `trial_candidate` to `second_case_validated_trial`.

## Next Work

1. Pull specific CFTC orders/dockets and product-rule documents.
2. Decide whether HOOD has enough product/revenue disclosure for a company-level snapshot.
3. Compare event-contract economics against stablecoin issuer economics to refine `regulatory_economics_bridge`.

## Refresh Policy

- stale_after: 2026-06-30
- must_refresh_if:
  - CFTC or court decisions materially change event-contract treatment
  - Robinhood, Kalshi, Polymarket, IBKR, CME or another platform discloses material volume/revenue data
  - prediction-market contracts are restricted, delisted or expanded materially
  - public-company revenue contribution becomes separately disclosed

