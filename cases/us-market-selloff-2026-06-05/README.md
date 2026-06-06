# 2026-06-05 US Market Selloff Case

这是一个美股大盘下跌解释案例，用于展示 Mira 如何处理时间敏感的市场问题：先过 live-data gate，再把价格行为、宏观触发、板块集中度和判断边界分开。

## Open Source Notice

- case_status: public_example
- not_investment_advice: true
- stale_after: 2026-06-08 US premarket
- refresh_policy: refresh before any live trading, portfolio, or actionability decision

## Case Metadata

- research_object: US major indices and AI/semiconductor-led selloff
- market_scope: US equities
- output_language: zh-CN
- research_cutoff_date: 2026-06-06
- market_data_as_of: 2026-06-05 US regular-session close
- depth_mode: standard
- readiness_level: working_view

## Why This Case

- Demonstrates the live-data-source policy on a same-session market question.
- Separates official macro facts from market-pricing evidence and media interpretation.
- Shows why a sharp Nasdaq/semiconductor selloff is not automatically a confirmed systemic crash.
- Preserves refresh triggers before any actionability or portfolio review.

## Package Files

- `investment-memo.md`
- `evidence-log.csv`
- `case-notes.md`
- `research-package-manifest.json`
