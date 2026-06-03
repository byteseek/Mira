# Methodology Card: Top / Bottom Risk Overlay

- status: trial
- role: overlay / risk-regime lens
- last_updated: 2026-06-03
- source_bucket: mixed (`institutional`, `academic`, `official_market_data`, `practitioner`, `derived_internal`)
- source_quality: medium-high
- credibility_score: medium
- credibility_basis: The method combines price-implied expectations, market-cycle psychology, official vulnerability frameworks, positioning data and event-reaction research. It is credible as a risk-diagnosis overlay, but not yet validated as an independent timing tool.
- search_coverage: medium
- search_gaps: Buy-side positioning data, dealer options exposure, ETF flow data, China / Hong Kong market microstructure, and historical top / bottom backtests remain incomplete.
- comparison_baseline: `valuation-expectation` + `variant-perception` + `macro-regime-analysis` without an explicit top / bottom risk state
- empirical_validation_mode: live case trial + historical failure backtest + forward watch
- follow_through_plan: Test on AI semis / opticals / memory, one commodity squeeze, one macro index drawdown, one failed growth rerating, and one capitulation bottom.

## Core Idea

`top-bottom-risk-overlay` is not a market-timing model.

It asks whether the research object is in a fragile risk regime where price has moved faster than the evidence base, or in a washed-out regime where price has moved past the current bad news.

The overlay separates four questions that are often mixed together:

- Is the fundamental direction still improving or deteriorating?
- What expectation path is now embedded in price?
- Is positioning / liquidity making the move more fragile?
- What next event would confirm, exhaust, reverse or reset the move?

For high-heat upside moves, the method should prevent:

> strong fundamentals -> therefore still good risk/reward.

For washed-out downside moves, the method should prevent:

> stock is down a lot -> therefore bottom.

## Use When

- User asks whether something is topping, bottoming, overheated, washed out, extended, capitulating, bubble-like or "有问题吗".
- A macro asset, sector, industry or single equity has moved sharply and the key question is risk state rather than first-pass fundamentals.
- The research object is dominated by the same factor across many securities: AI capex, liquidity, rates, commodity squeeze, China reopening, GLP-1, defense, crypto, etc.
- Good news no longer produces clean follow-through, or bad news no longer causes fresh downside.
- A thesis is fundamentally correct but may have become too crowded or too expensive.
- A thesis is fundamentally impaired but may have become too discounted for incremental bad news.

## Avoid When

- The user wants a normal first-pass company memo and price action is not central.
- There is no reliable market-pricing input.
- The asset is illiquid enough that price signals are mostly noise.
- A binary legal, financing or survival event dominates all other variables.
- The output would imply a trading action without position data, mandate, horizon or risk budget.

## Applies To

- `macro_asset_or_regime`: index, rates, FX, gold, credit, liquidity-sensitive baskets.
- `industry_concept`: hot themes, supply-chain bottlenecks, commodities, policy baskets.
- `single_equity`: high-revision names, crowded winners, capitulation candidates, event-driven names.
- `portfolio_review`: theme concentration, same-catalyst crowding, duplicated factor exposure.

## Core Question

Is the object in `trend_confirmation`, `fragile_upside`, `distribution_risk`, `capitulation_watch`, `base_building`, `bear_trap_risk`, or `no_clear_extreme`, and what evidence would move that state?

## Required Inputs

- price and relative performance window
  - 1 day, 5 day, 1 month, 3 month, YTD or case-specific event window.
- fundamental slope
  - revenue revision, margin revision, cash-flow quality, order / backlog quality, supply-demand balance, macro data surprise, or policy path.
- expectation burden
  - price-implied growth / margin / FCF path, consensus or guidance proxy, historical / peer range, or explicit `source_gap`.
- positioning / liquidity
  - ETF flows, short interest, options implied move / skew, CFTC COT for futures, fund exposure, volume, borrow, dealer / vol-control / CTA proxy where available.
- reaction quality
  - stock / asset reaction to good news and bad news, gap hold / fade, post-event follow-through, relative strength versus peers.
- catalyst path
  - next earnings, macro print, guidance, customer capex update, supply / inventory data, pricing update, policy event, refinancing, or lock-up / issuance.
- left-tail / right-tail map
  - customer concentration, leverage, funding, regulatory risk, inventory reversal, technology transition, short squeeze, policy rescue, forced selling.

## Diagnostic Lenses

### 1. Fundamental Slope

Classify the operating or macro evidence:

- `accelerating`
- `positive_but_decelerating`
- `stable_high_level`
- `deteriorating`
- `mixed`
- `source_gap`

The key is slope, not level. A sector can be fundamentally excellent and still face top risk if the second derivative is rolling over against high expectations.

### 2. Expectation Burden

Classify what the current price now requires:

- `low`
- `medium`
- `high`
- `extreme`
- `source_gap`

High burden means future evidence must keep improving merely to support current price. It does not mean the thesis is false.

### 3. Positioning And Liquidity

Classify whether the move is being amplified:

- `clean_revision`
- `crowded_long`
- `crowded_short`
- `squeeze_or_forced_flow`
- `liquidity_gap`
- `source_gap`

Positioning evidence is a market-pricing input only. It cannot verify fundamentals.

### 4. Reaction Quality

Classify the price response:

- `positive_follow_through`
- `good_news_fade`
- `bad_news_absorbed`
- `negative_follow_through`
- `gap_and_hold`
- `gap_fill`
- `range_digesting`
- `source_gap`

Reaction quality helps identify exhaustion or underreaction. It must be tied to a specific event window.

### 5. Catalyst Path

Classify the next event burden:

- `needs_upside_surprise`
- `needs_confirmation`
- `can_digest`
- `needs_reset`
- `waiting_for_capitulation`
- `source_gap`

This is the practical bridge from risk diagnosis to research action.

## Regime Labels

### `trend_confirmation`

Use when fundamentals, expectations and reaction quality still align.

Typical pattern:

- fundamental slope positive
- expectation burden not extreme
- reaction quality positive
- positioning not obviously one-way

Research action: `upgrade_watch` or `event_setup`, if other evidence gates are cleared.

### `fragile_upside`

Use when fundamentals are strong but the price already requires continued upside surprises.

Typical pattern:

- fundamental slope positive
- expectation burden high / extreme
- positioning risk medium / high
- next catalyst needs upside surprise

Research action: `watch_only` or `risk_reduction_context`.

### `distribution_risk`

Use when good news fades, relative strength deteriorates, or leadership narrows after a large move.

Typical pattern:

- fundamental slope positive but decelerating, mixed or source-gapped
- expectation burden high
- reaction quality good-news fade, gap fill or range distribution
- volume / positioning suggests crowded long exposure

Research action: `valuation_reset_watch` or `risk_reduction_context`.

### `capitulation_watch`

Use when downside is violent and positioning / liquidity may be forcing price below current evidence.

Typical pattern:

- fundamental slope deteriorating or mixed
- bad news widely known
- reaction quality starts to absorb bad news
- funding / survival risk is not dominant, or is explicitly bounded

Research action: `event_setup` or `valuation_reset_watch`, not a bottom call.

### `base_building`

Use when bad news is absorbed across multiple events and evidence begins to stabilize.

Typical pattern:

- fundamental slope stabilizing
- expectation burden low
- reaction quality bad-news absorbed or range digesting
- catalysts shift from negative revision to confirmation

Research action: `upgrade_watch` only after evidence confirms the base.

### `bear_trap_risk`

Use when fundamentals are still weak but market positioning is heavily short and the next event can squeeze the asset.

Typical pattern:

- fundamental slope not yet repaired
- crowded short / high short interest / high put skew
- next catalyst can remove a left-tail assumption
- upside move may be squeeze-led rather than thesis-led

Research action: `event_setup` or `hedge_context`.

### `no_clear_extreme`

Use when evidence is mixed or price movement is not extreme enough for this overlay to add value.

Research action: return to the primary framework.

## Output Template

Use `templates/top-bottom-risk-check.csv` for compact cases.

Minimum prose output:

- `risk_regime`
- `fundamental_slope`
- `expectation_burden`
- `positioning_liquidity`
- `reaction_quality`
- `next_catalyst_burden`
- `research_action`
- `confidence`
- `must_refresh_if`

## Stop Rules

- Do not call a top only because price is high.
- Do not call a bottom only because price is down a lot.
- Do not treat market reaction as fundamental validation.
- Do not use price action without an event window.
- Do not convert `risk_reduction_context` into a trade instruction without position data.
- If consensus, valuation or positioning data is missing, cap confidence at medium and mark `source_gap`.
- If the conclusion depends on implied valuation math, run the data-analysis quality gate or mark `calculation_gap`.

## Failure Modes

- Turning every sharp rally into a top warning.
- Turning every sharp selloff into a contrarian bottom setup.
- Overweighting social-media sentiment when actual positioning data is missing.
- Ignoring second derivative: good absolute fundamentals can still be bad versus expectations.
- Ignoring left-tail risk in apparent capitulation.
- Treating a squeeze as durable thesis repair.
- Using the same regime label for macro assets, industry baskets and single equities without mapping transmission.

## Comparison To Existing Methods

Relative to `valuation-expectation`:

- `valuation-expectation` asks what is priced in.
- `top-bottom-risk-overlay` asks whether price, expectations, positioning and next catalysts create an unstable risk regime.

Relative to `variant-perception`:

- `variant-perception` asks where Mira differs from consensus.
- `top-bottom-risk-overlay` asks whether the consensus / price setup is fragile or exhausted.

Relative to `macro-regime-analysis`:

- `macro-regime-analysis` maps macro transmission.
- `top-bottom-risk-overlay` maps whether that macro trade is extended, reversing, confirming or washed out.

Relative to `technical-market-pricing-context`:

- technical context describes market-pricing state.
- top / bottom overlay forces that state to be reconciled with fundamentals, expectations and catalysts.

## Trial Design

Initial live trials:

- `AI semis / opticals / memory 2026`
  Test whether the overlay improves risk-state judgment after extreme upside moves in MRVL, LITE, COHR and memory.
- `CPO optical suppliers`
  Reuse LITE / COHR handoff cases to test fragile upside and valuation reset conditions.
- `commodity squeeze`
  Test whether the method separates physical shortage from positioning squeeze.
- `macro index drawdown`
  Test whether the method distinguishes de-risking from growth scare and liquidity shock.
- `failed growth top`
  Backtest TDOC, PTON or another 2020-2022 high-growth winner.
- `capitulation bottom`
  Choose one case where fundamentals stabilized after a major drawdown.

Adopt only if the overlay changes action labels, refresh triggers or evidence requirements in at least three cases without producing systematic early top calls.

## Source Notes

- Expectations Investing, Mauboussin and Rappaport, official overview: https://www.expectationsinvesting.com/
- Expectations Investing, about page and process summary: https://www.expectationsinvesting.com/about-expectations-investing
- Howard Marks / Oaktree, `Taking the Temperature`: https://www.oaktreecapital.com/insights/memo/taking-the-temperature
- Federal Reserve, Financial Stability Report framework: https://www.federalreserve.gov/publications/2021-november-financial-stability-report-framework.htm
- Federal Reserve, Financial Stability Report May 2026: https://www.federalreserve.gov/publications/2026-may-financial-stability-report-accessibility-tables.htm
- CFTC Commitments of Traders descriptions and methodology: https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm
- A review of the Post-Earnings-Announcement Drift, Journal of Behavioral and Experimental Finance, 2021: https://www.sciencedirect.com/science/article/pii/S2214635020303750
- Crowded Trades, Market Clustering, and Price Instability, PLOS ONE / PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC8000620/

## Must Refresh If

- Three live Mira cases show the overlay does not change conclusions beyond existing valuation or technical checks.
- A high-profile case using this overlay produces a wrong-way top / bottom label because the framework ignored a key variable.
- Better public positioning, options, ETF flow or consensus data sources become available.
- The framework starts to slow down quick triage without improving action labels.
