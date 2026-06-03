# Methodology Card: Options Flow Analysis Framework

- status: trial
- role: options market-pricing, event-risk and positioning framework / overlay
- last_updated: 2026-06-03
- source_bucket: user_dataset; official_market_data; academic_market_microstructure; derived_internal
- source_quality: medium
- credibility_score: 3
- credibility_basis: The method can become more credible than generic unusual-options commentary because the user has a large options-flow dataset and can run repeatable validation. Credibility remains capped until the dataset quality gate, classification labels and false-positive backtests are documented.
- search_coverage: initial_external_sources_plus_user_dataset_pending
- search_gaps: Needs the user's dataset schema, vendor/source provenance, trade-signing method, opening/closing inference method, survivorship controls, corporate-action adjustments, and historical validation results before adoption.
- comparison_baseline: `technical-market-pricing-context`, `flow-intent-inference`, and ad hoc unusual-options alerts
- empirical_validation_mode: dataset audit, historical backtest, event-window study, false-positive review, and forward watch
- follow_through_plan: Start with a data dictionary and 3 validation notebooks or ledgers: pre-earnings/event windows, non-event directional flow, and false-positive/noise cases.

## Core Idea

Options flow deserves a separate framework when Mira has a large, repeatable dataset rather than isolated unusual-options screenshots. The framework asks what the options market is pricing across direction, volatility, skew, term structure, gamma, open interest and event risk, then tests whether those states have historical follow-through.

This is still a market-pricing framework. It can upgrade or downgrade event-risk, positioning, volatility and refresh-priority conclusions. It cannot independently prove revenue, margin, cash flow, customer demand, product quality or moat.

## Default Counterparty Assumption

For large options trades, the default assumption should be `prior_position_aware`, not `blank_slate_directional`.

Assume the aggressive side and liquidity provider are both likely to be familiar with the underlying stock, and at least one side may already have a stock, option, convertible, financing, borrow, index, ETF or portfolio-risk position. The observed option trade is therefore a marginal book adjustment unless evidence shows it is a clean new directional position.

When the trade size, structure and liquidity profile suggest institutional participation, use a stricter working prior: `rational_prior_position_enhancement`. This means Mira should first assume the institution's earlier position was intentional, informed and risk-managed, and the new trade is an enhancement, hedge, roll, monetization, financing action or convexity adjustment to that prior book.

This is an interpretation prior, not a truth claim. It should make the analysis more coherent by forcing Mira to reconstruct the likely existing book before interpreting the new print. It must not become blind deference to institutions. If the trade is inconsistent with rational enhancement, or if OI / bid-ask / IV / subsequent behavior contradicts it, downgrade to `unknown` or `noise`.

This improves interpretation because many large option prints are not a simple "buyer is bullish / seller is bearish" signal. They may be:

- adding convexity to an existing long or short stock position
- hedging borrow, financing, convertible or event exposure
- rolling, monetizing or re-striking an existing option position
- selling volatility against stock or another option leg
- creating defined-risk upside/downside participation
- transferring risk from a portfolio or market-maker book

The framework should analyze `initiator_intent`, `book_context_hypotheses`, `prior_thesis_hypothesis` and `enhancement_hypothesis`. If prior-position context is unknown, keep the conclusion at `market_pricing` / `positioning_hypothesis` and do not upgrade to strong directional intent.

## Reverse-Engineered From

- User has a large options-flow dataset and has already done initial analysis.
- Prior `flow-intent-inference` method treated unusual options as one visible-flow subtype, but that is too shallow for a systematic options dataset.
- Existing `technical-market-pricing-context` includes options fields but does not classify flow, validate predictive value, or separate volatility/directional/dealer mechanics.
- Academic work suggests some buyer-initiated opening option volume can contain information, while newer contradiction work and practitioner experience show high options activity can also be noise, retail speculation, hedging or expensive event lottery demand.

## Search Paths Used

- inherited from `flow-intent-inference-search-log.csv`: SEC / FINRA / OCC source checks, Pan and Poteshman option volume paper, options-and-earnings studies, order-imbalance literature and contradiction sources
- repo search for `technical-market-pricing-context`, `flow-intent-inference`, `options`, `positioning`, `overlay-routing`
- next required search path: user dataset schema and prior analysis outputs

## Use When

- The research question depends on options flow, implied volatility, skew, term structure, gamma concentration, open-interest build/decay, event implied move or option-to-stock activity.
- The user provides or references a structured options-flow dataset rather than a one-off UOA alert.
- Mira needs to test whether options data improves event-window prediction, risk-window definition, refresh triggers, false-positive control or thesis-system event deltas.
- A single-equity case has meaningful option liquidity and current market pricing may be dominated by volatility supply/demand, hedging, event lottery, dealer/gamma effects or directional positioning.

## Avoid When

- Option liquidity is too thin, bid/ask spreads are wide, OI is stale or corporate-action adjustments are not handled.
- The only input is a screenshot, social alert or vendor label without raw fields.
- The framework would be used to assert fundamental truth without independent company, industry or event evidence.
- The event window is unclear and realized-vol / return labels cannot be constructed.
- The dataset cannot distinguish at least quote-time, contract, price, size, bid/ask, expiry, strike, option type, underlying price and source timestamp.

## Applies To

- single-equity research
- earnings-event and catalyst-event analysis
- monitoring updates
- valuation-expectation and strategic-catalyst overlays
- flow-intent-inference handoff when the visible flow is specifically options-heavy
- portfolio review only as a crowding, event-risk or hedging-risk input, not as an autonomous position-size rule

## Core Question

What is the options market pricing about direction, volatility, skew, event risk and positioning, and has this option state historically improved Mira's refresh triggers, risk-window judgments or false-positive control?

## Required Inputs

- dataset identity, vendor/source, coverage universe, date range and survivorship policy
- raw contract fields: timestamp, ticker, expiry, strike, call/put, trade price, trade size, bid, ask, mid, underlying price, exchange/venue if available
- derived fields: moneyness, delta bucket, notional premium, volume z-score, OI, OI change next session, IV, IV rank, skew, term structure, bid/ask spread, option-to-stock volume, event distance
- flow labels: trade-side estimate, aggressor side, opening/closing inference, spread/roll detection, sweep/block flag, multi-leg linkage where available
- event labels: earnings, guidance, product, FDA/regulatory, M&A, financing, macro, index rebalance, lock-up, ex-dividend and no-event control windows
- outcome labels: 1d/5d/20d underlying return, abnormal return, realized volatility, IV crush/expansion, max adverse move, event gap, post-event drift and payoff proxy
- data-quality ledger and missing-field downgrade rule
- prior-position hypotheses: long stock, short stock, existing option spread, covered call, protective put, collar, convertible/arb, borrow/short-interest exposure, ETF/index/portfolio hedge, dealer inventory, unknown
- marginal-action classification: add exposure, reduce exposure, hedge, monetize, roll, finance, overwrite, tail-protect, volatility trade, transfer risk, unknown
- prior-thesis hypothesis: what existing view or exposure the trade is likely enhancing, protecting, monetizing or restructuring
- enhancement hypothesis: why this trade now improves the prior book's payoff, convexity, risk budget, financing, downside protection or event exposure

## Primary Signal

The signal is a state vector, not a single unusual-options alert:

- directional pressure: call/put buyer-initiated opening flow, delta-adjusted notional and OI build
- volatility demand: IV expansion, term-structure kink, event implied move, straddle/strangle demand
- skew / tail risk: put skew, call skew, wing concentration and crash/upside-tail demand
- positioning mechanics: gamma concentration, pin risk, expiry clustering, dealer-hedging sensitivity and OI decay
- liquidity / credibility: spread, depth proxy, premium size versus ADV/market cap, repeat flow and post-session OI confirmation
- prior-position fit: whether the trade makes more sense as new exposure, hedge, roll, overwrite, monetization, financing or portfolio-risk transfer
- enhancement fit: whether the trade improves an existing book's payoff shape, risk window, capital efficiency or event convexity

## Why It Works

Options can concentrate demand for leverage, event convexity, hedging and volatility transfer. When raw flow is classified and validated against later returns and realized volatility, it can reveal whether the market is buying information, hedging a known risk, selling volatility, chasing lottery payoff, or forcing dealer hedging. The edge, if any, should appear in calibrated event windows, asymmetric payoff distributions, volatility forecasts, false-positive filters or better refresh triggers.

## Failure Mode

- treats volume as new positioning when OI does not confirm
- reads a spread, roll, overwrite, hedge or closing trade as a directional bet
- assumes the buyer or seller has no prior stock/options exposure
- assumes institutional flow is automatically correct instead of treating rational-prior enhancement as a falsifiable prior
- ignores that a bullish-looking call buy can hedge short stock, and a bearish-looking put buy can protect long stock
- ignores that option selling can be volatility supply, covered overwrite, monetization or financing rather than the opposite directional view
- ignores bid/ask width, stale quotes, low-liquidity contracts and adjusted options
- overfits to rare payoff tails while ignoring base-rate losses
- confuses retail event lottery demand with informed trading
- treats IV expansion as bullish/bearish instead of volatility demand
- ignores dealer/gamma mechanics and expiry effects
- leaks future information through OI updates, event labels or survivorship-biased universe construction
- upgrades fundamental thesis without independent evidence

## Evidence Cost

High upfront because the framework requires data cleaning, classification and validation. Medium once the dataset schema, quality gates and reusable labels are stable.

## Speed Vs Depth

- speed mode: run data-quality gate, summarize option state, classify dominant flow type, state confidence and refresh trigger
- standard mode: add event-window comparison, OI confirmation, IV/skew/term-structure map and historical base-rate context
- deep mode: run backtest by flow class, event type, liquidity bucket, moneyness, expiry, premium size, OI confirmation and regime

## Comparison To Existing Methods

- Compared with `technical-market-pricing-context`, this framework is deeper and dataset-backed; it does not merely record options snapshot fields.
- Compared with `flow-intent-inference`, this framework is specialized for options and should be used first when options data is the main input.
- Compared with `valuation-expectation`, it can show what volatility, event risk or directional pressure is priced, but valuation still determines whether the underlying expectation is attractive.
- Compared with ad hoc UOA alerts, it requires data-quality checks, base rates, false-positive controls and explicit failure modes.

## Follow-Through Criteria

- It must improve at least one of: event-risk classification, risk window, refresh trigger, volatility expectation, catalyst priority, false-positive downgrade or thesis-system event delta.
- Every output should label whether the option state is `directional`, `volatility`, `skew_tail`, `dealer_mechanical`, `hedge`, `roll_or_spread`, `closing`, `retail_lottery`, `ambiguous` or `noise`.
- Every large-trade output should include at least two prior-position hypotheses and one prior-thesis / enhancement hypothesis unless raw data proves a clean new position.
- No conclusion may exceed the data-quality tier.
- If validation does not beat a simple baseline such as stock volume / realized-vol / event calendar, the framework stays `watch_only`.

## Trial Design

1. Build `options-flow-data-quality-check.csv` for the user's dataset.
2. Create a data dictionary with raw fields, derived labels and known vendor limitations.
3. Run three validation slices:
   - pre-earnings and other named event windows
   - non-event directional flow
   - false-positive high-volume / high-premium option activity
4. Compare against baselines:
   - no-options event calendar baseline
   - stock volume / abnormal return baseline
   - simple IV rank / implied move baseline
   - generic `flow-intent-inference` hypothesis output
5. Record whether the method changes Mira's refresh trigger or downgrade decision in at least five real cases.

## Falsification Conditions

- Backtests show no improvement over simple event and stock-volume baselines after costs, liquidity and false positives.
- Predictive value only appears in labels unavailable at decision time.
- The framework cannot reliably separate opening flow from closing, spreads, rolls or hedges.
- Prior-position-aware hypotheses do not improve classification quality versus blank-slate directional labels.
- Rational-prior enhancement hypotheses become unfalsifiable stories that explain every institutional trade after the fact.
- It repeatedly encourages bullish/bearish conclusions where the true signal is volatility demand.
- It improves hit rate only by excluding failed cases after the fact.

## Adoption Decision

Keep in `trial`. Promote toward `adopted` only after the user's dataset passes quality gates and at least three validation slices show repeatable improvement in refresh triggers, risk-window definition or false-positive control. Until then, use it as a specialist market-pricing framework, not a standalone investment decision engine.

## Source Notes

- Inherits source notes from `memory/methodologies/flow-intent-inference.md` and `memory/methodologies/flow-intent-inference-search-log.csv`.
- Next source required: user-provided options-flow dataset schema, prior analysis notes and validation outputs.
