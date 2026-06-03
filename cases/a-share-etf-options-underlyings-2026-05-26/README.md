# A股 ETF 期权标的底层属性手册

This case maps the ETF underlyings available in the user's ETF option menu to their actual index exposures and dominant trading factors.

## Open Source Notice

- case_status: historical_example
- not_investment_advice: true
- refresh_policy: refresh before any live trading or portfolio decision

- market: `CN A-share`
- research_question: 可交易期权的 ETF 标的，内部成分分别对应什么市场属性？
- research_cutoff_date: `2026-05-26`
- primary_weight_data_as_of: `2026-05-25; 深证100采用国证指数2026年04月指数单张`
- output_language: `zh-CN`

## Files

- `investment-memo.md`
  Main cross-ETF exposure map, trading-factor interpretation, refresh conditions, and comparison tables.
- `case-notes.md`
  Routing notes, source quality notes, and open issues for future refresh.
- `evidence-log.csv`
  Claim-level evidence records used in this run.

## Next Refresh

Refresh after:

- ETF.run or index providers update monthly constituent and sector weights.
- Exchanges add, suspend, or change ETF option underlyings.
- Major index rebalances for CSI, SSE, SZSE, or CNI indexes.
- One of the dominant sectors moves enough to materially alter weights: semiconductors, CPO/communication, power equipment, financials, consumer staples, or nonferrous metals.
