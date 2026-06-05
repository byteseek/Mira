# AAPL Case

这是首个单票 golden case，用于展示当前 Mira 单票研究脚手架如何在真实公司上跑通：memo、canonical evidence log、expectation map、thesis ledger、decision log 和 actionability bridge 在同一 case 包内闭环。

## Open Source Notice

- case_status: historical_example
- not_investment_advice: true
- stale_after: next quarterly results release or 2026-07-13, whichever comes first
- refresh_policy: refresh before any live trading or portfolio decision

## Case Metadata

- company: Apple Inc.
- ticker: AAPL
- market: US
- output_language: zh-CN
- research_cutoff_date: 2026-04-14
- financial_data_through: fiscal Q1 2026 ended 2025-12-27
- price_date: 2026-04-13
- thesis_horizon: 12-24 months

## Why This Case

- 公开资料丰富，适合作为多源数据案例
- 同时具备公司、财务、技术面和事件面材料
- 可清楚演示 `L1`、`L4`、`L5` 三类以上来源如何并存
- 可用单一 skill + 单一 orchestrator 跑出完整研究包
- 可作为 agent few-shot 样例；不要模仿 legacy case 的旧 evidence-log schema

## Package Files

- `investment-memo.md`
- `research-package-manifest.json`
- `evidence-log.csv`
- `case-notes.md`
- `expectation-map.csv`
- `thesis-ledger.md`
- `decision-log.csv`
- `actionability-bridge.md`
