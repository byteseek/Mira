# Methodology Card: market-briefing-loop

- status: trial
- role: market briefing, market triage, research escalation
- last_updated: 2026-06-10
- source_bucket: institutional; practitioner; first_principles; derived_internal
- source_quality: medium_high
- credibility_score: 4
- credibility_basis: Public institutional examples consistently show daily market updates, weekly market recaps, weekly commentary and market calendars as recurring products. The method is operationally simple, but its investment value depends on freshness, attribution discipline and escalation quality.
- search_coverage: English institutional public sources plus Mira internal loop comparison
- search_gaps: Did not inspect paid sell-side morning notes, internal buy-side desk notes, Bloomberg terminal templates, or Chinese brokerage daily/weekly products.
- comparison_baseline: `monitoring-loop` for existing thesis updates
- empirical_validation_mode: live_trial
- follow_through_plan: Use on at least three market scopes: US equity daily brief, US equity weekly review, and one sector/theme weekly. Review whether the escalation queue produces useful follow-up research.

## Core Idea

机构常见的日报/周报不是完整研究包，而是固定节奏的 market triage product。它从市场范围和时间窗口出发，把价格行为、宏观变量、事件日历、新闻流、行业/风格轮动、风险信号和研究升级线索组织成可刷新输出。

Mira 应把它作为独立 loop，而不是塞进 `monitoring_update`。`monitoring_update` 的对象是已有 thesis；`market-briefing-loop` 的对象是市场窗口。

## Reverse-Engineered From

- Schwab Market Update: https://www.schwab.com/learn/schwab-market-update
- Schwab Weekly Trader's Outlook: https://www.schwab.com/learn/story/weekly-traders-outlook
- J.P. Morgan Asset Management Market Updates: https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/market-updates/
- BlackRock Weekly Market Commentary: https://www.blackrock.com/us/individual/insights/blackrock-investment-institute/weekly-commentary
- Morningstar Weekly Markets Planner: https://www.morningstar.com/markets/whats-happening-markets-this-week
- UBS Daily Outlook: https://www.ubs.com/global/en/wealthmanagement/insights/chief-investment-office/house-view/daily.html
- Fidelity Weekly Market Update: https://www.fidelity.com/learning-center/trading-investing/weekly-market-update

## Search Paths Used

- `daily market update`, `market open report`, `weekly market recap`
- `weekly market commentary`, `weekly trader outlook`, `markets this week`
- institutional public sites from Schwab, J.P. Morgan Asset Management, BlackRock, Morningstar, UBS and Fidelity
- internal comparison against `loops/monitoring-loop.md`

## Use When

- 用户问“日报 / 周报 / 盘前简报 / 收盘复盘 / 本周市场回顾 / 下周市场怎么看”
- 用户指定某个市场、板块、主题或 watchlist，希望做固定窗口观察
- 用户想知道今天/本周哪些变量需要刷新或升级研究
- 需要把市场新闻流转成 research escalation queue，而不是完整 thesis

## Avoid When

- 用户要完整研究单票、财报、研报解读或组合复盘；应路由到对应 loop/skill
- 用户要求真实仓位、下单、仓位大小或交易执行；必须走 decision/actionability gates
- 数据无法建立 quote/publish time，而用户要求 live-use 判断
- 只有 price-only 叙事，无法做 attribution quality 标注

## Applies To

- US equities, A-shares, HK equities, global macro, commodities, rates-sensitive assets
- sector/theme windows such as AI semiconductors, China internet, power equipment, robotics
- PM/trader risk watch when holdings are provided or when only research-only risk triage is needed

## Core Question

在给定市场范围和时间窗口内，哪些价格行为、事件、宏观变量、行业/主题变化和风险信号具有足够信息量，值得进入 watchlist、刷新已有 thesis 或升级为正式研究？

## Required Inputs

- `briefing_type`
- `market_scope`
- `time_boundary`
- quote/publish/as-of time for live or near-live inputs
- macro/earnings/policy calendar when relevant
- source notes for material claims
- optional watchlist or portfolio context

## Primary Signal

- confirmed or plausible drivers behind major moves
- sector/theme/factor rotation and breadth
- dated catalysts and next checks
- divergence between market pricing and available evidence
- escalation queue quality

## Why It Works

固定频率 brief 的价值不是预测市场，而是压缩信息流、识别主导变量、暴露需要刷新的旧判断，并把“市场发生了什么”转成可执行的研究下一步。机构公开产品普遍包含每日市场更新、周度回顾、下周预览、市场日历和策略评论，说明这种工作流是常见投研表面。

## Failure Mode

- 把日报写成新闻摘要，没有 research escalation
- 用事后叙事解释所有价格波动，缺少 attribution quality
- 忽略数据时间戳，导致 stale market view 被复用
- 把 price reaction 当成基本面验证
- 在没有持仓、mandate 和风险预算时输出仓位或交易建议

## Evidence Cost

中等。`quick_map` 需要少量高质量、带时间戳的市场和事件来源；`standard` 需要补充 calendar、sector/theme rotation、source notes 和 escalation queue；`deep_dive` 才需要更完整的跨资产、仓位、流动性和历史对比。

## Speed Vs Depth

- daily brief: speed > depth，默认短生命周期
- close wrap: speed and attribution balance
- weekly review: depth > daily，强调主导变量和下周事件
- sector/theme weekly: depth depends on theme complexity
- risk/positioning watch: depth depends on portfolio context and data availability

## Comparison To Existing Methods

相对 `monitoring-loop`，本方法不要求已有 thesis，也不从单个研究对象出发。它先观察市场窗口，再决定是否把某个对象送入 `quick_map`、`monitoring_update`、`earnings_event` 或 `first_pass_research`。

相对 `macro-regime-analysis`，本方法不尝试建立宏观 regime，只在 briefing 窗口内识别宏观变量对市场的短期信息价值。

## Follow-Through Criteria

- brief 是否写清了 `stale_after` 和 `must_refresh_if`
- source notes 是否包含 quote/publish/as-of time
- major moves 是否有 attribution quality，而不是单一叙事
- escalation queue 是否能产生后续有效研究
- 被升级对象是否真的改善了 thesis freshness 或 source coverage

## Trial Design

- target_case_1: `US equities daily_market_brief`
- target_case_2: `US equities weekly_market_review`
- target_case_3: `AI semiconductors sector_theme_weekly`
- target_case_4: optional `HK equities weekly_market_review`

每个 case 都要检查：source freshness、driver attribution、facts/inferences/judgments 分离、escalation queue 命中率和下一轮 follow-through。

## Falsification Conditions

- 连续三次 brief 只产出泛泛新闻摘要，不能产生有用 escalation
- 多数 driver attribution 无法被来源支持，或经常把 price-only 移动写成事实判断
- 用户复用 brief 时经常越过 `stale_after` 造成错误结论
- brief 明显重复 `monitoring-loop` 或 `macro-regime-analysis`，没有独立价值

## Adoption Decision

进入 `trial`。理由：机构样本和 Mira 内部缺口都支持新增独立 loop；但还需要真实日报/周报 case 验证是否改善研究升级、刷新边界和用户使用效率，不能直接标记 `adopted`。
