# ETF Discovery Run: 2026-05-09

本目录记录 2026-05-09 对美国市场近期新上市 ETF 的一轮 discovery。

## Open Source Notice

- case_status: historical_example
- not_investment_advice: true
- historical_status: stale_since 2026-05-16 for listed-product status; refresh before reuse
- refresh policy: refresh before any live trading or portfolio decision

## Files

- `new-etf-watchlist.csv`
  结构化候选列表，供后续 `etf-listing-analysis` 使用。
- `discovery-log.md`
  本轮搜索路径、筛选判断、优先级和缺口。
- `evidence-log.csv`
  本轮使用的 claim-level evidence records。

## Next Suggested Analyses

优先进入深度分析：

1. `BUYB`
   ProShares S&P 500 Buyback Aristocrats ETF。
2. `EUV`
   Corgi Lithography & Semiconductor Photonics ETF，先补发行人/交易所 primary confirmation。
3. `JOUL` / `GASZ`
   Corgi 高压电网设备、天然气电力与涡轮主题，先补 primary confirmation 和持仓。

## Status

- discovery_status: `completed_initial`
- next_step: `run etf-listing-analysis on BUYB; confirm Corgi product primary sources`
- research_cutoff_date: `2026-05-09`
