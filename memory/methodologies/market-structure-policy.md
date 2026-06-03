# Methodology Card: Market Structure Policy Overlay

- status: trial
- role: market-structure, policy-regime and local-price-setter overlay
- last_updated: 2026-06-03
- source_bucket: derived_internal; official_market_structure_sources; first_principles
- source_quality: medium
- credibility_score: 3
- credibility_basis: The logic is internally coherent and supported by observable market-structure facts such as Stock Connect channels, quotas and regulatory rules, but it still needs case backtests and follow-through before adoption.
- search_coverage: limited_official_sources_plus_internal_methodology
- search_gaps: Needs broader institutional and practitioner review across A-share, Hong Kong, Japan, Korea, Taiwan and Europe cases; needs contrary cases where local-market overlay added no value.
- comparison_baseline: Existing `framework-routing` plus `macro`, `supply-chain`, `commodity`, `strategic-catalyst` and `valuation-expectation` overlays.
- empirical_validation_mode: case backtest plus live trial
- follow_through_plan: Test in at least four A-share / Hong Kong cases, one A/H or ADR dual-listing case, and two non-China international cases before considering adoption.

## Core Idea

Some international equities fail under a pure company / valuation / revision framework because the main price setter is not the company variable. The overlay asks whether listing venue, investor base, capital-flow channel, policy regime, governance discount, share supply or local trading structure is impairing or amplifying the valuation anchor.

This is an overlay, not a replacement for the main equity framework. The main framework still asks whether the stock is best analyzed as `micro-small`, `mid-cap` or `large-mega`; this overlay asks whether local market structure changes how evidence should be weighted.

## Reverse-Engineered From

- User observation that current Mira equity frameworks work reasonably well for US, Japan, Korea, Taiwan and Europe, but often feel less reliable for A-shares and Hong Kong.
- Existing Mira `framework-routing` rule that first identifies the dominant price setter.
- Existing `valuation-expectation` need to explain what is already priced in and what would cause rerating.
- Official Stock Connect materials from HKEX and SSE showing formal cross-market trading channels.
- CSRC public materials on shareholder reduction rules, which illustrate that local rules can directly affect share supply and risk premium.

## Search Paths Used

- `HKEX Stock Connect Southbound Northbound official overview`
- `Shanghai Stock Exchange Stock Connect official overview`
- `CSRC official shares reduction rules listed companies 2024`
- repo search for `overlay-routing`, `framework-routing`, `analysis-routing` and `technical-market-pricing-context`

## Use When

- The stock is listed in A-share, Hong Kong, A/H, H-share, red chip, China ADR or another market where local price setters may dominate company fundamentals.
- A stock is fundamentally cheap or expensive but the rerating path depends on who can buy, who is forced to sell, or what local policy changes.
- Governance, controller behavior, related-party risk, disclosure quality, buyback, dividend or shareholder-return credibility changes the valuation discount.
- A market structure variable such as Stock Connect eligibility, Southbound / Northbound flow, index inclusion, ETF flow, float, lock-up, share reduction, refinancing or trading restrictions changes the supply-demand balance.
- The research question asks why company fundamentals and price action diverge.

## Avoid When

- The listed market has deep institutional price discovery and no clear local-structure distortion in the current case.
- The user only needs operating due diligence and explicitly waives market-pricing or actionability.
- The only support is broad country stereotyping without date-stamped market, regulatory or ownership evidence.
- The overlay would duplicate `macro` because the real driver is rates, credit, FX, growth, inflation or broad risk appetite rather than market structure.

## Applies To

- single-equity research
- earnings and monitoring updates where price reaction diverges from fundamental evidence
- A/H or ADR dual-listed companies
- portfolio reviews where local market liquidity, governance or policy exposure can create hidden correlated risk
- valuation-expectation work where rerating depends on the buyer base

## Core Question

Is this stock being priced mainly by company fundamentals, or by a local market-structure / policy / investor-base variable that changes the valuation anchor and rerating path?

## Required Inputs

- listing market, primary trading venue and likely price discovery venue
- market access path for relevant investors
- investor-base and flow clues such as Southbound / Northbound, ETF, passive, foreign ownership, local funds or retail activity
- policy and regulatory items relevant to the company, sector or share supply
- share supply and float items: lock-ups, reductions, refinancing, buyback, dividend, dilution and major-holder behavior
- governance and shareholder-return evidence
- valuation anchor and evidence for whether the market currently respects it
- refresh source list for exchange, regulator, company and market-flow data

## Primary Signal

The primary signal is a mismatch between company-level evidence and the current price-setting mechanism.

Examples:

- Fundamentals improve but rerating requires foreign inflow, Southbound buying, governance repair or policy confirmation.
- Valuation is optically cheap but the market is pricing controller risk, low payout, geopolitical risk, disclosure weakness or permanent foreign-exit risk.
- A theme rallies before earnings because local policy and liquidity are the price setter.
- Share supply, refinancing, lock-up expiry or reduction rules matter more than reported earnings for near-term risk.

## Why It Works

The same company-level evidence can have different pricing power in different market structures. A strong earnings revision in a market dominated by institutional forecasting may reprice quickly; the same revision in a market dominated by policy themes, flow constraints, governance discount or offshore risk premium may require a different catalyst path.

## Failure Mode

- Turns into country-level stereotypes rather than specific price-setter evidence.
- Overweights policy headlines and underweights actual company economics.
- Confuses broad macro with market structure.
- Treats Southbound / Northbound or ETF flow as directional truth without checking scale, persistence and stock-level relevance.
- Explains every underperformance as governance or policy discount after the fact.

## Evidence Cost

Low to medium for listing venue, public regulation, company buyback / dividend / share-supply history and exchange eligibility. Medium to high for investor-base, flow, ownership and policy-transmission evidence because the data may be delayed, partial or noisy.

## Speed Vs Depth

- speed mode: listing / price-discovery map, dominant price setter, key policy or flow variable, valuation-anchor impairment and refresh trigger
- depth mode: flow history, investor-base map, governance / shareholder-return review, A/H or ADR spread analysis, share-supply calendar, policy timeline and contrary evidence

## Comparison To Existing Methods

- Compared with `macro`, this overlay focuses on market access, price setters, governance, local regulation and share supply rather than growth, rates, FX, credit or liquidity regime.
- Compared with `valuation-expectation`, this overlay explains why the valuation anchor may or may not work in a specific market.
- Compared with `technical-market-pricing-context`, this overlay explains structural price-setting conditions rather than the current chart / event reaction.
- Compared with `supply-chain`, it does not validate operating demand or margin transmission; it validates whether operating evidence can actually be priced.

## Follow-Through Criteria

- It should change at least one of: selected overlays, evidence priority, valuation-anchor quality, rerating path, refresh triggers or conclusion confidence.
- It should produce a named structure variable, not a generic claim that a market is policy-driven or flow-driven.
- It should make stale conditions explicit, especially for regulatory changes, flow regime changes, buyback / dividend actions, index inclusion and policy confirmation.

## Trial Design

Run this overlay in:

- two Hong Kong cases where the stock is optically cheap but rerating is uncertain
- two A-share cases where policy theme, local flow, share supply or governance may dominate price
- one A/H or ADR dual-listing case where price discovery venue and spread matter
- one Japan / Korea / Taiwan / Europe control case where the overlay should stay `context` or be waived

For each case, record whether the overlay improved:

- dominant price-setter identification
- valuation-anchor quality
- thesis confidence downgrade / upgrade
- refresh trigger quality
- post-event follow-through explanation

## Falsification Conditions

- It does not change research conclusions, evidence priority or refresh conditions in real cases.
- It repeatedly explains outcomes only after the fact.
- It causes Mira to over-focus on policy / flow and miss company-level earnings, cash flow or competitive evidence.
- It cannot name the specific investor-base, policy, governance, flow, access or share-supply variable driving the conclusion.
- Non-China international control cases show the same issues can be handled by existing `macro`, `valuation-expectation` or `technical-market-pricing-context` overlays.

## Adoption Decision

Keep in `trial`. Use it as a mandatory gate for A-share and Hong Kong single-equity work, but do not mark it `adopted` until it passes case backtests and at least one follow-through review.
