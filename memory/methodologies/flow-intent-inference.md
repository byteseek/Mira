# Methodology Card: Flow Intent Inference Overlay

- status: trial
- role: market-flow, positioning and counterparty-intent inference overlay
- last_updated: 2026-06-03
- source_bucket: official_market_data; academic_market_microstructure; practitioner; derived_internal
- source_quality: medium
- credibility_score: 3
- credibility_basis: Public order-flow, options, block-trade, ATS, Form 4 and 13F data can anchor observable behavior, and academic work supports that some option and order-flow variables contain information. Credibility is capped because public data often lacks initiator identity, full hedge legs, opening/closing tags, trade intent and real-time position context.
- search_coverage: initial_multi_bucket
- search_gaps: Needs more practitioner failure cases, dealer/gamma-specific institutional sources, China/HK local block-trade and 龙虎榜 source mapping, and Mira case backtests before adoption.
- comparison_baseline: `technical-market-pricing-context` plus `market-structure-policy` plus `valuation-expectation`
- empirical_validation_mode: case backtest plus forward watch
- follow_through_plan: Test in at least five cases: one isolated unusual-options clue without full dataset support, one block/secondary offering case, one insider/Form 4 cluster, one A-share/HK flow-disclosure case, and one false-positive visible-flow case.

## Core Idea

Visible trading records can sometimes reveal pressure, constraints or information asymmetry before fundamentals are fully confirmed. This overlay turns "someone is trading size" into a disciplined intent-inference workflow: identify the observable flow, map possible counterparties and mechanics, rank intent hypotheses, then downgrade or discard the signal unless it changes a named thesis variable, risk window, refresh trigger or evidence priority.

The method does not claim to know a trader's actual motive. It only forms bounded hypotheses from observable behavior and states what would confirm or falsify each hypothesis.

## Reverse-Engineered From

- User observation that research reports, large prints, abnormal stock volume and unusual options activity often reveal market participants acting before the thesis is obvious.
- Existing Mira `technical-market-pricing-context`, which already treats price, volume, options and positioning as `market_pricing` rather than fundamental proof.
- Existing Mira `market-structure-policy`, which asks who the price setter is but does not provide a specific intent-inference workflow for visible trades.
- SEC Form 13F FAQ: 13F discloses institutional manager holdings, but with coverage limits, quarterly timing and possible confidential treatment.
- Investor.gov Form 3/4/5 bulletin: Form 4 reports insider transaction details, while insider sales can have non-informational reasons such as liquidity or diversification.
- FINRA OTC/ATS transparency materials: ATS and non-ATS trading data can show delayed off-exchange and block-size activity, but not the full pre-trade intent.
- OCC and options-market data references: option volume and open interest are observable, but systematic options analysis should be routed to `options-flow-analysis` when raw dataset coverage is available.
- Academic market microstructure and options literature showing both information content and failure/noise channels in option volume and order imbalance.

## Search Paths Used

- `SEC Form 13F limitations confidential treatment`
- `Investor.gov insider transactions Form 4 purchases sales diversification`
- `FINRA ATS transparency block-size trade data`
- `OCC options volume open interest`
- `option volume future stock prices Pan Poteshman`
- `options volume as noise earnings announcements`
- `order imbalance individual stock returns market microstructure`
- repo search for `technical-market-pricing-context`, `market-structure-policy`, `overlay-routing`, `options`, `positioning`

## Use When

- A stock, sector or event shows abnormal stock volume, large block prints, isolated unusual options activity, short-interest pressure, borrow stress, ATS/dark-pool activity, insider transactions, 13F changes, ETF/index flow or A-share/HK public flow disclosures.
- The user asks what other market participants may be doing, whether a move is information-driven or mechanical, or whether visible flow changes the evidence priority.
- A catalyst or event window may create forced hedging, dealer gamma effects, index/passive flow, short squeeze, liquidation, secondary offering digestion, buyback execution or insider/aligned-holder signaling.
- A single-equity thesis has a gap between fundamental evidence and market reaction, and the next useful question is "who is likely setting price right now?"

## Avoid When

- The only evidence is a social-media screenshot, vendor alert or isolated high-volume print without timestamp, venue, price, expiry/strike, OI, spread, underlying move and event context.
- The method would be used to infer exact trade direction or position size without initiator-side, opening/closing and hedge-leg data.
- The conclusion depends on market flow to validate revenue, margin, cash flow, moat or product execution.
- Liquidity is too thin for prints to carry institutional meaning.
- The visible flow is likely routine: scheduled insider grants, tax sales, index rebalance, option expiry roll, market-maker inventory management or systematic ETF creation/redemption.

## Applies To

- single-equity research
- earnings and event deltas
- monitoring updates
- strategic-catalyst and valuation-expectation overlays
- market-structure-policy overlay for A-share, HK, ADR, A/H and Stock Connect cases
- portfolio review only as a research-priority or crowding-risk input, not as a position-sizing rule

## Core Question

What intent hypotheses are consistent with the observable flow, and does any hypothesis materially change the thesis, catalyst path, risk window, refresh trigger or evidence priority?

## Required Inputs

- flow_object: stock, option contract, block trade, insider filing, 13F/ownership, ETF/index flow, ATS/dark-pool data or local disclosure
- as_of_date and quote_time or filing_time
- price, volume, spread and liquidity context
- event calendar: earnings, guidance, FDA/regulatory, M&A, financing, lock-up, index rebalance, macro data or product launch
- option-specific fields when relevant: expiry, strike, moneyness, bid/ask, volume, open interest, implied volatility, skew, put/call, and OI change after the session. If structured options-flow data is available, route to `options-flow-analysis`.
- stock-flow fields when relevant: print size versus ADV, price impact, venue, block/ATS tag, short interest, borrow, float and ownership
- disclosure fields when relevant: Form 4 transaction code, insider role, transaction size versus holdings, 10b5-1 or routine compensation context, 13F report date and reporting-period lag
- competing mechanical explanations and direct falsification checks

## Primary Signal

The primary signal is not "large trade equals smart money." The signal is the alignment of:

- abnormality versus the asset's own baseline
- concentration by strike, expiry, venue, holder, event or time window
- persistence across multiple sessions or disclosures
- price impact relative to liquidity
- consistency with event timing and thesis variables
- evidence that a mechanical explanation is insufficient

## Why It Works

Large or unusual flow can reveal urgency, information asymmetry, hedging demand, liquidity stress or forced rebalancing before the full reason appears in fundamentals. Options can concentrate information because leverage and defined downside make them attractive for informed or event-driven traders. Block and ATS data can identify where large liquidity demand occurred. Insider and institutional filings can show observable alignment, even if with lag and context limits.

## Failure Mode

- infers intent from a print that may be a hedge, spread, roll, closing trade or market-maker inventory transfer
- treats options volume as directional without OI change, trade side, IV/skew and underlying move
- overweights delayed 13F data as current institutional intent
- treats insider sales as bearish without checking diversification, tax, compensation, 10b5-1 and remaining ownership
- ignores dealer hedging, expiry, gamma, liquidity vacuum and index/passive mechanics
- backfills narrative after price movement
- upgrades fundamental confidence from market-pricing evidence

## Evidence Cost

Medium in speed mode because basic price, volume, OI, Form 4, 13F and delayed ATS data are public. High in depth mode because robust inference needs signed flow, opening/closing classification, hedge-leg detection, dealer positioning, borrow, intraday liquidity and event-specific context that may be unavailable or vendor-dependent.

## Speed Vs Depth

- speed mode: classify visible flow, list plausible intent hypotheses, identify mechanical alternatives, state whether it changes refresh priority
- depth mode: reconstruct event window, compare against ADV/OI/float/history, check OI after the session, map possible counterparties, model dealer/hedge mechanics qualitatively, and log confirmation/falsification triggers

## Comparison To Existing Methods

- Compared with `technical-market-pricing-context`, this overlay focuses on who might be trading and why, not whether the chart, volume and event reaction look strong.
- Compared with `options-flow-analysis`, this overlay is broader and shallower; use `options-flow-analysis` first when the primary input is a structured options-flow dataset.
- Compared with `market-structure-policy`, this overlay focuses on discrete visible flow and counterparty hypotheses, not stable listing-venue, investor-base and regulatory structure.
- Compared with `valuation-expectation`, this overlay can reveal whether price movement is driven by expectation revision or positioning unwind, but it cannot replace valuation work.
- Compared with `strategic-catalyst`, it can prioritize a suspicious event path, but rumor or flow alone stays `weak_signal` until independently confirmed.

## Follow-Through Criteria

- The overlay must change at least one of: `selected_overlays`, evidence priority, catalyst watchlist, risk window, refresh trigger, actionability confidence downgrade, or thesis-system event delta.
- Every intent hypothesis must name a falsification check.
- If the best explanation is mechanical or ambiguous, output should be `watch_only`, `needs_refresh` or `source_gap`, not a stronger thesis conclusion.

## Trial Design

Run the check in five validation cases:

1. Isolated unusual options activity without enough raw data for full `options-flow-analysis`.
2. Large block trade, secondary offering, ATM program or lock-up expiry where supply/digestion matters.
3. Insider Form 4 purchase/sale cluster where transaction code and remaining ownership can be checked.
4. A-share/HK flow-disclosure case using 龙虎榜, 大宗交易, southbound/northbound or CCASS-style ownership clues.
5. A false-positive case where visible flow did not map to a thesis-relevant event.

For each case, compare the output against ordinary `technical-market-pricing-context` and record whether this overlay improved refresh triggers or avoided a false conclusion.

## Falsification Conditions

- The overlay repeatedly produces plausible stories but no improved refresh trigger, evidence priority or risk-window decision.
- It cannot separate information-driven flow from routine mechanical flow in backtests.
- It increases confidence from market-pricing evidence without independent fundamental or event evidence.
- It fails false-positive tests where volume was high but OI, spreads, event timing or later disclosures showed no thesis-relevant intent.
- The same work can be handled by `technical-market-pricing-context`, `market-structure-policy` or `valuation-expectation` without loss of clarity.

## Adoption Decision

Keep in `trial`. Use as an optional overlay when visible flow is central to the research question, and as a mandatory downgrade gate when a user or source claims that large trades reveal "smart money." Do not mark `adopted` until case backtests show repeatable improvement in evidence priority, refresh triggers and false-positive control.

## Source Notes

- SEC Form 13F FAQ: https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f
- Investor.gov insider transactions bulletin: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-69
- FINRA OTC / ATS transparency: https://www.finra.org/filing-reporting/otc-transparency
- OCC volume and open interest query page: https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/volume-query
- Pan and Poteshman, `The Information in Option Volume for Future Stock Prices`: https://www.nber.org/papers/w10925 and https://www.mit.edu/~junpan/volume.pdf
- Chordia and Subrahmanyam, `Order imbalance and individual stock returns`: https://www.sciencedirect.com/science/article/abs/pii/S0304405X03001752
- Donders, Kouwenberg and Vorst, `Options and earnings announcements`: https://ideas.repec.org/a/bla/eufman/v6y2000i2p149-171.html
- Contradiction seed, options volume as noise around earnings: https://papers.ssrn.com/sol3/Delivery.cfm/6448100.pdf?abstractid=6448100&mirid=1
