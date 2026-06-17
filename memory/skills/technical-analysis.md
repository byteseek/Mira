# Skill Knowledge: Technical Analysis

- last_updated: 2026-06-09
- status: trial
- role: market-pricing and risk-context layer, not a standalone trade signal
- executor: reproducible computation via `tools/mira_data technical <ticker>` (stdlib, delayed L5 daily); derived indicators are ledgered; options / short-interest / intraday = `source_gap`

## Scope

Use technical analysis to answer:

- how the market is currently pricing the research object
- whether price, volume and volatility confirm or reject recent event interpretation
- where the thesis or setup would need refresh because the market reaction changed
- whether positioning, crowdedness or volatility make the research action lower quality

Do not use technical analysis to prove fundamental execution, demand, margin, moat, valuation or long-term thesis durability.

## Required Inputs

- OHLCV daily history, normally at least 252 trading days
- sector or benchmark ETF history
- 2-5 close peers when available
- event dates for earnings, guidance, product, regulatory or macro catalysts
- current valuation / price snapshot with `as_of_date`
- optional: options chain, implied move, short interest, borrow/float and holder data

## Default Checks

### Trend And Structure

- 20 / 50 / 100 / 200 day moving-average stack
- price location vs 52-week high / low
- 1M / 3M / 6M / 12M absolute return
- 1M / 3M / 6M / 12M relative return vs benchmark and sector ETF
- maximum drawdown from recent high
- support, resistance and failed breakout / failed breakdown levels
- MA20 extension, current-entry reward/risk and pullback-entry reward/risk when
  the user asks whether a move is buyable, chaseable or worth waiting for
- chase-risk state and preferred wait zone as price-discipline fields only

### Volume And Participation

- volume vs 20D / 60D average
- volume z-score around event dates
- accumulation / distribution pattern only if it is tied to price levels and evidence date
- liquidity quality: average daily value traded and bid/ask proxy where available

### Volatility And Risk Window

- 20D / 60D realized volatility
- ATR / normalized ATR
- gap size and whether the gap was filled
- event-day and post-event abnormal return
- volatility compression / expansion before catalysts

### Event Reaction

- 1D / 5D / 20D post-event return
- 1D / 5D / 20D relative return vs benchmark / sector / peer basket
- "good news not up" and "bad news not down" as market-pricing signals only
- follow-through quality: sustained move, reversal, failed retest or range-bound digestion

### Positioning And Crowding

- options implied move, IV rank / term structure and skew when public data is available
- put/call and open interest changes when public data is available
- short interest, days to cover and short-interest change
- ownership / float constraints if relevant
- social or media attention only as `sentiment`, never as core evidence

## Output Standard

- trend_state
- relative_strength_state
- volume_state
- volatility_state
- event_reaction_quality
- positioning_risk
- key_levels
- invalidation_level
- trigger_level
- technical_context_score
- extension_from_ma20_pct
- current_entry_rr
- pullback_entry_rr
- chase_risk_state
- preferred_wait_zone
- evidence_limitations
- stale_after
- must_refresh_if

## State Tokens

Use these values in `trend_state`:

- `uptrend_confirmed`
- `uptrend_extended`
- `range_constructive`
- `range_neutral`
- `range_distribution`
- `downtrend_confirmed`
- `reversal_attempt`
- `technical_source_gap`

Use these values in `event_reaction_quality`:

- `positive_follow_through`
- `negative_follow_through`
- `reversal_against_news`
- `gap_and_hold`
- `gap_fill`
- `range_digesting`
- `no_clear_signal`
- `source_gap`

Use these values in `positioning_risk`:

- `low`
- `medium`
- `high`
- `source_gap`

## Evidence Rules

- Price, volume, options and positioning data are `market_pricing` claims.
- Derived levels, z-scores and abnormal returns are `derived_calculation` claims and must list upstream market-data sources.
- A technical conclusion is stale for live use after 30 calendar days unless refreshed.
- Event-reaction checks are stale after the next material event or 20 trading days, whichever comes first.
- Options and intraday conclusions require quote time and are stale same day for live use.

## Failure Modes

- treating price action as proof of fundamental truth
- ignoring benchmark / sector beta
- fitting levels after the fact without a date-stamped price source
- over-weighting low-liquidity moves
- reading options flow without expiry, quote time, open interest and liquidity context
- using technical confirmation to override stale or weak fundamental evidence

## Actionability Boundary

The reward/risk fields are a technical-price overlay for actionability
questions. They can downgrade a buy/chase posture when the current price is
extended or the current-entry reward/risk is poor. They cannot upgrade a thesis
whose marginal buyer, payoff source, repricing trigger, valuation anchor or
fundamental evidence remains weak.

Use these fields after the marginal-buyer / payoff bridge, not instead of it.
They describe whether the market-pricing setup is stretched, not whether the
company is fundamentally attractive.
