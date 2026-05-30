# Stablecoin Regulatory Plumbing Trial

- as_of: 2026-05-30
- task_mode: `methodology_review` + `macro_asset_or_regime`
- research_object: stablecoins / tokenized money
- market_scope: US payment stablecoin framework and US-listed public-market proxies
- time_boundary: post-GENIUS Act regime setup through 2026 implementation window
- primary_skill_or_loop: `macro-regime-analysis` with regulatory evidence classification
- workflows_under_test: `analysis-routing`, `macro-regime-analysis`, `llm-claim-classification`, `institutional-research-quality-gate`
- source_boundary: evidence rows in `evidence-log.csv`; no issuer valuation model yet
- output_status: regulatory plumbing trial, not a company investment memo
- not_investment_advice: true

## Routing Result

This should not start as a CRCL, COIN or payment-network memo. The right first pass is regulatory plumbing because the key question is how law and implementation rules change issuance rights, reserve economics, distribution access and compliance costs.

## Core Question

Which parts of the stablecoin theme are legal/regulatory facts, which are implementation variables, and which are issuer-economics assumptions?

## Plumbing Map

See [stablecoin-regulatory-plumbing-map.csv](stablecoin-regulatory-plumbing-map.csv).

The critical chain is:

`law enacted -> eligible issuer rules -> reserve requirements -> distribution access -> circulation growth -> reserve yield / revenue share / compliance costs -> issuer cash flow`

## Facts

- The GENIUS Act is a regime-change event for US payment stablecoins.
- Agency implementation and supervision are still live variables.
- Issuer economics require company-level reserve income, distribution-cost and rate-sensitivity evidence.

## Inferences

- Regulatory clarity can expand the addressable market, but it can also compress economics by increasing compliance, reserve constraints and competition.
- Public-market handoff should split direct issuers, distribution partners, payment networks and banks.
- The first-order variable is not "stablecoins become legal." It is whether regulated circulation converts into durable, profitable issuer or platform economics.

## Trial Judgment

The theme passes reality basis at the policy level but does not pass stock-level decision readiness.

Current state should be `regulatory_map_first`. The right next step is a CRCL issuer-economics snapshot or a payment-network exposure check, not a broad stablecoin thesis.

## Quality Gate

| gate | result |
| --- | --- |
| `reality_basis` | pass for legal/regulatory regime change |
| `first_order_variable` | pass after compression: issuer economics and distribution access, not legalization alone |
| `decision_increment` | partial pass: supports company handoff segmentation, not actionability |
| `disconfirmation_path` | partial pass: needs final rules, issuer applications, circulation growth, reserve yield and revenue-share evidence |

## Workflow Review

### What Worked

- `analysis-routing` prevented premature single-company work.
- Claim classification separated law, policy, issuer metrics, assumptions and market-pricing gaps.
- The quality gate downgraded the broad theme from "regulatory clarity = winner" to "regulatory plumbing map first."

### What Failed Or Is Missing

- The current package lacks final-rule implementation detail, issuer applications and company-level economics.
- It lacks independent market-pricing evidence for CRCL, COIN, V/MA or banks.
- The current macro workflow needs a compact "regulation-to-economics bridge" for financial plumbing themes.

## Proposed Workflow Patch Candidate

Name: `regulatory_economics_bridge`

Use when a financial or fintech theme depends on law, licensing, reserve rules, capital rules, distribution access or compliance cost.

Required fields:

- legal event
- implementing authority
- eligible actors
- permitted economics
- prohibited economics
- adoption channel
- compliance / capital / reserve cost
- company exposure path
- disconfirmation metric

Do not adopt yet. Trial it first on stablecoins, then on another regulatory-financial theme.

## Next Work

1. Build CRCL issuer-economics snapshot: circulation, reserve income, distribution costs, rate sensitivity and valuation.
2. Compare payment-network exposure for V/MA versus direct issuer economics.
3. Decide whether stablecoins should become a thesis-system update case or remain a regulatory map.

## Refresh Policy

- stale_after: 2026-06-30
- must_refresh_if:
  - final agency rules differ from proposed requirements
  - major issuers receive or lose approval
  - reserve requirements, interest-rate path or revenue-share agreements change materially
  - USDC circulation or stablecoin payment volumes diverge from issuer commentary
  - market pricing changes enough to alter the expectation map

