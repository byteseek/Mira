# Instrument Strategy Gate

Mira may discuss trading instruments only as a research and risk-structure
framework. It must not become an execution engine or a strategy recommender
that bypasses user constraints.

Use this gate only when the user explicitly asks about instruments or structures
such as options, calls, puts, spreads, collars, covered calls, cash-secured puts,
short selling, pair trades, hedges, futures, margin, leverage or other
derivatives.

If the user only asks whether an equity is attractive, load
[actionability-risk-control.md](actionability-risk-control.md) and stop at the
participation posture unless an instrument route is clearly requested.

## Boundary

Instrument work can describe:

- which instrument family best matches the stated objective
- what extra data is required before comparing structures
- instrument-specific risks and failure modes
- limited-loss versus open-ended-risk differences
- what would make an instrument unsuitable
- follow-up calculations needed before implementation

Instrument work must not describe:

- exact contract, strike, expiry or share quantity as an executable order
- naked option selling or leveraged shorting as a default response
- a hedge as risk-free
- a spread, collar or pair trade without naming the risk it actually hedges
- instrument advice without checking user eligibility, liquidity and risk budget

## Trigger Rule

Load this gate when the user asks:

- "用期权怎么玩"
- "可以买 call / put 吗"
- "怎么对冲"
- "能不能做空 / 卖空"
- "有没有结构化一点的买法"
- "pair trade 怎么做"
- "怎么控制回撤但保留上行"

Do not load this gate for ordinary valuation, target price, memo or earnings
analysis unless the output asks for a trading instrument.

## Required Inputs

Before giving instrument-specific framing, identify:

- `objective`: directional upside, downside protection, income, event
  participation, volatility expression, hedge, relative value or risk reduction
- `time_window`: intraday, event date, 1-4 weeks, 1-3 months, 3-12 months or
  long-term
- `risk_budget`: maximum acceptable loss, drawdown tolerance, margin tolerance
  or explicit unknown
- `instrument_access`: cash equity only, listed options, short sale, margin,
  futures or unknown
- `position_context`: no position, proposed position, existing long, existing
  short, concentrated holding or portfolio hedge
- `data_status`: option chain, implied volatility, expected move, bid/ask,
  volume/open interest, borrow, correlation or beta data status

If these inputs are missing, keep the output at route-level and list the missing
inputs. Do not choose a specific contract or structure.

## Instrument Families

Use the family that matches the objective. These are research routes, not trade
instructions.

| family | use when | main risk |
| --- | --- | --- |
| `cash_equity` | thesis exposure is desired without derivative complexity | full downside to equity drawdown |
| `listed_option_long_premium` | limited-loss upside or downside exposure is desired | premium decay, IV crush, timing error |
| `listed_option_spread` | limited-loss exposure with lower premium outlay | capped upside/downside, execution spread, strike selection |
| `protective_option` | existing position needs defined downside protection | hedge cost, basis mismatch, expiry mismatch |
| `collar_or_overlay` | existing long needs downside control with accepted upside sacrifice | upside cap, assignment/exercise complexity |
| `income_overlay` | user owns/accepts underlying exposure and wants yield | upside called away, hidden short-vol exposure |
| `short_sale` | bearish thesis is strong and borrow/margin risk is acceptable | unlimited loss, squeeze, borrow recall/cost |
| `pair_or_relative_value` | thesis is relative mispricing, not broad market direction | leg mismatch, beta/factor residual, borrow/liquidity |
| `portfolio_hedge` | goal is book-level drawdown or factor risk reduction | hedge basis risk, cost, false diversification |
| `no_instrument_route` | inputs are missing or the structure would add more risk than it solves | false precision |

## Stop And Downgrade Rules

Return `no_instrument_route`, `watch_only`, `needs_refresh` or `source_gap`
when:

- objective is unclear
- risk budget is unknown and the structure can lose more than premium paid
- option chain, IV, expected move or liquidity data is required but missing
- short-sale borrow, margin or squeeze risk is unknown
- hedge correlation, beta or exposure mapping is missing
- the proposed instrument does not match the thesis risk
- user eligibility or instrument access is unknown for a complex structure
- the request would require exact execution details without user confirmation

## Option-Specific Gate

For listed options, do not compare structures without at least:

- event date or holding window
- option chain freshness
- implied volatility or expected move
- bid/ask and liquidity context
- maximum premium loss or margin exposure
- thesis variable that must happen before expiry

Before events, state IV-crush risk explicitly. A strong fundamental view does
not automatically make long calls attractive if the required move is already
priced into implied volatility.

## Short-Sale Gate

For short selling, do not move beyond route-level without:

- borrow availability and borrow cost
- margin constraint
- catalyst or invalidation window
- squeeze risk and crowdedness proxy if available
- upside loss path

If these are missing, return `no_instrument_route` or `risk_cap_review`.

## Hedge Gate

For hedges, identify the exposure being hedged:

- single-name drawdown
- market beta
- sector/theme exposure
- factor exposure
- event risk
- currency, rate or commodity exposure

If the hedge does not match the exposure, mark `basis_risk`. A hedge that only
feels safe but does not reduce the named risk should not upgrade actionability.

## Minimum Output

For a quick instrument answer, include:

- `instrument_route`
- `objective`
- `time_window`
- `risk_budget_status`
- `data_required`
- `suitable_families`
- `unsuitable_families`
- `main_failure_modes`
- `next_calculation`
- `action_boundary`

For a formal output, use
[../templates/actionability-system/instrument-strategy-gate.md](../templates/actionability-system/instrument-strategy-gate.md).
