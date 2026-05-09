# Methodology Card: ETF Listing Discovery

- status: trial
- role: discovery-engine
- last_updated: 2026-05-09
- source_bucket: mixed (`official_and_industry`, `market_data`, `ETF industry media`, `derived_internal`)
- source_quality: medium
- credibility_score: medium
- credibility_basis: 新 ETF 发现可以通过交易所、发行人、监管文件和 ETF 行业媒体交叉验证，但来源分散且上市、申请、公告状态容易混淆
- search_coverage: low-medium
- search_gaps: 还需要为 US 以外市场补本地交易所和监管来源；部分 ETF flow/AUM 数据可能需要付费或延迟数据
- comparison_baseline: `manual web search for new ETFs`
- empirical_validation_mode: trial -> live discovery runs + missed-listing review
- follow_through_plan: 用 30 天 discovery window 定期试跑，记录漏掉的 ETF、误收的非新产品、以及 priority_score 是否能筛出值得分析的候选

## Core Idea

ETF 新发发现不是简单搜“new ETF”。必须把交易所通知、发行人产品页、监管文件、ETF 行业媒体和市场数据放在同一张候选表里，并区分 `filed / approved / announced / listed / trading`。

## Use When

- 需要找最近新上市或即将上市 ETF
- 需要为 `etf-listing-analysis` 准备候选池
- 需要监控某个主题是否正在被多家 issuer 产品化
- 需要观察 ETF 产品供给是否代表市场偏好变化

## Avoid When

- 只想分析一个已知 ETF
- 时间窗口或市场范围无法定义
- 没有能力确认候选产品是否真的上市
- 只拿媒体报道，不回到交易所、发行人或监管来源

## Core Question

最近有哪些 ETF/ETP 新上市、申请或宣布推出，其中哪些值得进入 ETF 上市分析？

## Required Inputs

- market_scope
- discovery_window
- discovery_mode
- theme_filter
- source coverage
- research_cutoff_date

## Primary Signal

- 交易所新上市通知确认 first trade date
- 发行人产品页或新闻稿确认策略、费用、指数或主动管理方式
- 监管文件确认申请状态
- 行业媒体用于补充发现线索和主题语境
- AUM/成交用于初步判断是否进入 T1 watch

## Failure Mode

- 把申请误当上市
- 把 dual listing 或 share class conversion 当新产品
- 只搜媒体，漏掉交易所或监管来源
- 只搜英文，漏掉本地市场 ETF
- 过度收集低质量新发，造成分析队列噪音

## Evidence Cost

medium

快速发现可以先搜行业媒体，但高质量 watchlist 必须回补交易所、发行人或监管来源。

## Speed Vs Depth

- `speed`: 媒体/交易所快速扫，输出候选列表
- `medium`: 加发行人页面和监管文件确认状态
- `depth`: 补首日/5日 AUM、成交、价差和同类 ETF 对比

## Comparison To Existing Methods

相对 `etf-listing-analysis`：

- `discovery` 负责找候选、去重、排序
- `analysis` 负责解释 T0/T1 信号和投资 read-through

相对普通新闻扫描：

- 它强制区分上市状态和来源权重
- 它输出结构化 watchlist，而不是一组链接

## Trial Design

- 每月做一次 US ETF discovery run，记录候选、来源和 next_action
- 对 priority_score >= 4 的产品进入 `etf-listing-analysis`
- 30 至 60 天后复盘是否漏掉重要 ETF，或是否把噪音误判为高优先级

## Falsification Conditions

- 经常漏掉交易所已确认的新 ETF
- 经常把 filed/announced 误写成 listed
- priority_score 无法筛出后续真实流入或高讨论度产品
- watchlist 噪音过高，导致分析队列不可用

## Adoption Decision

当前判断：`trial`

原因：

- 发现层是 ETF 上市分析闭环的必要前置
- 但数据源覆盖和误差率必须经过真实 discovery run 检验

