# Methodology Card: Technical Market Pricing Context

- status: trial
- role: market-pricing, event-reaction and risk-window layer
- last_updated: 2026-06-03
- source_bucket: derived_internal; practitioner; market_data
- source_quality: medium
- credibility_score: 3
- credibility_basis: Public price, volume, options and positioning data are reproducible, but the interpretation layer can easily become narrative or hindsight-biased.
- search_coverage: internal-methodology-only
- search_gaps: Needs future external methodology review across institutional technical analysis, event studies and market microstructure sources before adoption.
- comparison_baseline: Current `memory/skills/technical-analysis.md` only checked trend, levels, volume and event reaction at a high level.
- empirical_validation_mode: case backtest plus live trial
- follow_through_plan: Test in at least three earnings/event cases and two first-pass single-equity memos before considering adoption.

## Core Idea

Technical analysis should be treated as a structured `market_pricing` layer. It helps Mira describe how the market is reacting, where risk and invalidation are changing, and whether a setup has post-event follow-through. It does not validate fundamentals.

## Reverse-Engineered From

- Existing Mira source taxonomy for `market_price_and_trading`.
- Existing technical-analysis memory item dated 2026-04-15.
- Existing actionability bridge need for trigger levels, invalidation and event follow-through.

## Search Paths Used

- repo search for technical-analysis, price, volume, market reaction and valuation references
- internal source taxonomy review
- internal actionability bridge review

## Use When

- A research action depends on current market setup, event reaction or follow-through.
- A thesis update needs to distinguish fundamental evidence from market reaction.
- A stock has high volatility, crowded positioning, low liquidity or event-driven gaps.
- The user asks whether a name can be acted on now, watched, refreshed or deprioritized.

## Avoid When

- The case lacks date-stamped price data.
- The object is not tradeable or market data is too thin.
- The user is asking only for long-term business quality and actionability is explicitly out of scope.
- The analysis would rely only on chart pattern labels without benchmark, volume and event context.

## Applies To

- single-equity research
- earnings and event deltas
- monitoring updates
- ETF and thematic product checks when liquidity / spread / AUM matters
- portfolio reviews where crowding or drawdown risk affects research priority

## Core Question

What does current price, volume, volatility and positioning say about market pricing, follow-through quality and research-action risk?

## Required Inputs

- 252 trading days of OHLCV when available
- benchmark and sector / peer price series
- event date and event source
- price snapshot with `as_of_date`
- optional options chain, short interest, holder and liquidity data

## Primary Signal

The primary signal is not a single indicator. It is alignment or conflict across:

- trend state
- relative strength
- volume participation
- event reaction
- volatility / liquidity
- positioning and crowdedness

## Why It Works

Market data is the fastest observable record of expectation adjustment. When combined with event timing and benchmark-relative returns, it can show whether new information is being accepted, rejected or digested by the market.

## Failure Mode

- confuses price reaction with fundamental proof
- overfits levels after the fact
- ignores sector beta and market regime
- over-reads low-liquidity moves
- treats options or short-interest data as directional truth without expiry, quote time and liquidity context

## Evidence Cost

Low for daily price / volume, medium for benchmark-relative and event calculations, medium-high for options and positioning because quote time, expiry and liquidity must be recorded.

## Speed Vs Depth

- speed mode: trend, levels, relative strength, volume and event reaction
- depth mode: abnormal returns, realized volatility, options, short interest, liquidity and peer basket comparison

## Comparison To Existing Methods

This method extends the prior technical-analysis checklist by adding data fields, benchmark-relative context, event reaction metrics, volatility, options / short-interest positioning and explicit evidence boundaries.

## Follow-Through Criteria

- Technical context changes the research action only when it changes setup quality, invalidation, refresh priority or risk window.
- It must not upgrade a thesis whose fundamental evidence remains weak.
- It should produce a clear refresh condition, not a vague chart comment.

## Trial Design

Use [../../templates/technical-analysis-check.csv](../../templates/technical-analysis-check.csv) in:

- two earnings-event cases with visible post-event price reaction
- one failed-breakout or failed-breakdown monitoring case
- one high-volatility / high-short-interest case
- one ETF or product-liquidity case

## Falsification Conditions

- It repeatedly adds descriptive chart commentary without changing decision quality.
- It produces false confidence because evidence is low-liquidity, stale or not benchmark-adjusted.
- It encourages thesis upgrades unsupported by fundamental evidence.
- It cannot be reproduced from the recorded public data.

## Adoption Decision

Keep in `trial`. It can be used in formal outputs as a market-pricing layer, but it is not yet an adopted Mira method until case follow-through proves that it improves actionability, refresh triggers and risk framing.
