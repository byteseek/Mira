# Marginal Buyer / Payoff Bridge

This bridge is the actionability analysis core for "can I buy?", "should I
sell?", "can I add?", "can I chase?", "can I buy the dip?" and similar
participation questions.

It is not a trade signal module. It answers the research question that must
come before actionability risk control:

- who is the next marginal buyer or seller
- why that marginal participant has not fully acted yet
- what variable can force repricing from the current price
- how much of that payoff appears already priced in
- what evidence would confirm or invalidate the bridge

After this bridge, apply [actionability-risk-control.md](actionability-risk-control.md).
If the user provides a real position, route through the position or portfolio
loop before making position-level implications.

## Trigger

Load this bridge when the prompt asks whether to buy, sell, add, trim, chase,
buy a dip, exit, hold after a move, or participate around an event.

Examples:

- "can I buy X now?"
- "should I sell X now?"
- "can I add after the print?"
- "is this dip buyable?"
- "can I still chase after this move?"
- "target price reached; still buyable?"

If the prompt is time-sensitive (`now`, `today`, `latest`, intraday,
premarket, after-hours), run the live-data policy before judging price context.

## Routing Position

Use this bridge as a lens, not as a standalone heavy loop.

```text
actionability prompt
-> intent intake and decision pressure gate
-> live-data gate when time-sensitive
-> current thesis / source notes / event context
-> marginal buyer / payoff bridge
-> actionability risk-control
-> position-review or portfolio loop if real holdings are provided
```

Default route mapping:

| context | route |
| --- | --- |
| no real position data | `thesis_system_update` or current research route, then actionability bridge |
| real single-position data | `position_review` with this bridge as a required lens |
| real portfolio or risk-budget context | `portfolio_construction_review` with this bridge for object-level actionability |
| options, shorting, hedges, pair trades, margin or leverage | also load `instrument-strategy-gate.md` |

## Payoff Source Taxonomy

Use these labels as research descriptors. Do not invent machine-facing action
tokens.

| payoff_source | meaning |
| --- | --- |
| `earnings_revision` | revenue, margin, EPS, FCF or unit economics expectations can move |
| `guidance_revision` | company or consensus guidance can reset expectations |
| `macro_discount_rate` | rate, dollar, credit spread or risk premium changes drive valuation |
| `macro_growth_liquidity` | growth, liquidity, inflation or policy regime changes drive flows |
| `value_mean_reversion` | asset is priced below a defensible normalized value anchor |
| `multiple_rerating` | market may assign a higher or lower multiple to the same fundamentals |
| `event_probability_repricing` | regulatory, legal, M&A, product, trial or policy probability changes |
| `positioning_short_cover` | short interest, underweight, crowding or forced cover drives demand |
| `flow_rebalance_passive` | index, ETF, benchmark, factor or systematic flow changes |
| `capital_return_carry` | dividends, buybacks, yield or carry become material to return |
| `balance_sheet_risk_repricing` | liquidity, leverage, covenant or solvency risk changes |
| `asset_value_repricing` | owned assets, reserves, IP, real estate or sum-of-parts value resets |
| `technical_liquidity_only` | price action or liquidity can move price, but thesis evidence is weak |
| `unknown_source_gap` | payoff source cannot be stated from current evidence |

Multiple payoff sources are allowed, but state whether they are independent or
the same variable expressed twice.

## Buy / Add / Chase Questions

For buy-side actionability, answer these before assigning participation posture:

| field | question |
| --- | --- |
| `marginal_buyer` | Who is the next likely buyer: fundamental, growth, value, macro, event, passive, short-cover, retail, or systematic flow? |
| `payoff_source` | What is the marginal return source from here? |
| `repricing_trigger` | What evidence, event or price behavior forces that buyer to reprice? |
| `buyer_not_in_yet` | Why has that buyer not already fully bought? |
| `priced_in_status` | How much of the upside appears already priced in? |
| `seller_error` | What must the current seller be wrong about? |
| `confirmation_required` | What must be confirmed before posture strengthens? |
| `invalidation` | What would show the payoff bridge is wrong? |
| `failure_mode` | Most likely way the buy/add/chase thesis fails. |

If `marginal_buyer`, `payoff_source` or `repricing_trigger` cannot be named,
downgrade toward `watch_only`, `needs_refresh` or `research_only`.

## Sell / Trim / Exit Questions

For sell-side actionability, use the mirror logic:

| field | question |
| --- | --- |
| `remaining_marginal_buyer` | Who still has a reason to buy above the current price? |
| `residual_payoff_source` | What return source remains if the user keeps holding? |
| `buyer_exhaustion` | Has the original marginal buyer already completed repricing? |
| `marginal_seller` | Who could become the next seller: thesis owners, event traders, crowded longs, risk managers, passive/systematic flow, or balance-sheet sellers? |
| `downside_repricing_trigger` | What evidence or event could make selling pressure dominant? |
| `priced_in_status` | Is the prior upside priced in, over-priced, or still under-recognized? |
| `buyer_error` | What must the current buyer or holder be wrong about? |
| `hold_confirmation_required` | What must be confirmed to justify holding rather than trimming? |
| `invalidation` | What would show the sell/trim thesis is wrong? |
| `failure_mode` | Most likely way selling is premature. |

If remaining payoff is small, hard to evidence, or already priced in while
downside triggers are nearer or more knowable, downgrade toward `trim_review`,
`risk_cap_review` or `exit_review` only after applying position-data rules.
Without real position data, keep the implication research-bound.

## Minimum Output

For `quick_map`, show this bridge in natural language:

- "the next buyer/seller is probably..."
- "the payoff source is..."
- "this strengthens only if..."
- "this fails if..."

For `standard` or durable actionability work, include a structured bridge in
`actionability-bridge.md` and tie material claims to source notes or an
evidence log.

## Stop Rules

- No identifiable marginal buyer or remaining buyer: do not upgrade
  actionability.
- No payoff source beyond price momentum: mark `technical_liquidity_only` and
  downgrade unless the task is explicitly a short-term market-structure read.
- No valuation, expectation or event anchor when price matters: downgrade to
  `source_gap`, `calculation_gap`, `needs_refresh` or `watch_only`.
- Time-sensitive price context without current quote or publish time cannot
  support live-use actionability.
- Real position-size, trim or exit conclusions require holdings, weights,
  mandate and risk budget.
