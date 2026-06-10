# Market Briefing Loop

`market-briefing-loop` 用于生成固定频率或用户触发的市场观察产品：
daily brief、market close wrap、weekly market review、sector/theme weekly 和
risk/positioning watch。

它不是后台监控承诺，也不是完整 research package。它从 `market_scope` 出发，
把价格行为、宏观变量、事件日历、新闻流、行业/风格轮动和研究升级线索组织成
可刷新、可追溯的 market briefing。

## Objective

- 在盘前、盘中、收盘后或周度窗口内总结市场状态
- 区分事实、市场定价、推断和判断
- 识别主导变量、异常移动和高信息量事件
- 给出需要升级到 `quick_map`、`monitoring_update`、`earnings_event` 或
  `first_pass_research` 的 research escalation queue
- 写清 source freshness、quote/publish time、`stale_after` 和
  `must_refresh_if`

## Loop Input

- `briefing_type`: `daily_market_brief` / `market_close_wrap` /
  `weekly_market_review` / `sector_theme_weekly` / `risk_positioning_watch`
- `market_scope`: 例如 `US equities`、`A shares`、`HK equities`、`global macro`
  或特定行业/主题
- `time_boundary`: 盘前、收盘后、过去 1 个交易日、本周、下周预览等
- `source_boundary`: 公开来源、本地数据、指定链接、vendor export 或用户材料
- `watchlist_scope`: 可选；用户给定的 ticker、行业、主题、宏观变量或已有 thesis
- `output_depth`: `quick_map` / `standard` / `deep_dive`

## Briefing Types

### `daily_market_brief`

盘前或当天市场简报。默认问题：

- 隔夜或盘前哪些资产、行业、主题和宏观变量移动最大？
- 哪些移动有清晰催化剂，哪些只是噪音或流动性？
- 今天有哪些宏观数据、央行、财报、政策或公司事件可能改变判断？
- 哪些对象需要刷新 quote、source 或 thesis？

默认输出：

- `market snapshot`
- `key overnight / premarket moves`
- `driver map`
- `today calendar`
- `watchlist changes`
- `research escalation queue`
- `stale_after = next market session or next major scheduled release`

### `market_close_wrap`

收盘后复盘。默认问题：

- 当天涨跌、风格/行业/主题轮动和广度是否一致？
- 市场叙事是否解释了价格行为，还是存在未解释的 divergence？
- 哪些 move 改变了短期 risk window 或已有 thesis 的刷新条件？

默认输出：

- `close snapshot`
- `move attribution`
- `sector / theme / factor rotation`
- `breadth and reaction quality`
- `unexplained moves`
- `next-session watchpoints`

### `weekly_market_review`

周度市场复盘和下周预览。默认问题：

- 本周主导变量是什么：盈利、利率、通胀、政策、流动性、仓位、主题叙事还是事件？
- 哪些变化只是价格噪音，哪些进入 thesis / watchlist / risk register？
- 下周哪些事件最可能改变市场状态？

默认输出：

- `week in review`
- `dominant market variables`
- `asset / sector / theme rotation`
- `earnings / macro / policy calendar`
- `thesis impact queue`
- `next-week watchpoints`
- `stale_after = next weekly review or major intervening event`

### `sector_theme_weekly`

特定行业、主题或市场段周报。默认问题：

- 主题内谁在领涨/领跌，是否符合基本面或事件差异？
- 主题叙事、订单、价格、供需、政策、竞争和估值变量是否变化？
- 哪些公司需要进入单票 `quick_map` 或正式研究？

默认输出：

- `theme snapshot`
- `leader / laggard map`
- `fundamental signal map`
- `narrative and positioning change`
- `company handoff queue`

### `risk_positioning_watch`

PM 或交易台风格的风险观察。默认问题：

- 哪些 crowded trades、vol、rates、FX、credit、liquidity、earnings 或 policy
  variables 可能改变风险承受度？
- 风险是 price-only、positioning、fundamental、macro 还是 liquidity driven？
- 哪些风险需要升级为 `position_review`、`portfolio_construction_review` 或
  `actionability` 检查？

默认输出：

- `risk dashboard`
- `positioning and crowding notes`
- `macro and liquidity stress map`
- `portfolio relevance`
- `escalation triggers`

## States

### `define-brief`

确认 `briefing_type`、`market_scope`、`time_boundary`、source boundary 和
用户指定 watchlist。没有指定市场时，先用用户上下文推断一个最小市场范围；不确定
时声明假设。

### `run-live-data-gate`

日报、盘前、盘中、收盘复盘和“最新/今天/本周”问题默认触发
[../data/live-data-source-policy.md](../data/live-data-source-policy.md)。
必须记录 quote time、publish time、as-of time 或明确 source gap。

### `collect-snapshot`

按市场范围收集最小可用 source pack：

- broad index / benchmark
- rates / FX / commodities / credit proxy when relevant
- sector / theme / factor movers
- macro / policy / earnings calendar
- company or theme watchlist items
- official / primary source for material claims where practical

### `classify-moves-and-claims`

把输入分为：

- `reported_fact`
- `market_pricing`
- `company_or_policy_claim`
- `macro_release`
- `sellside_or_expert_view`
- `weak_signal`
- `mira_inference`

不得把价格反应直接写成基本面验证。

### `build-driver-map`

对主要移动给出 driver attribution：

- `confirmed_driver`: 有明确事件、数据或披露支持
- `plausible_driver`: 与价格行为和来源一致，但缺少直接证明
- `contested_driver`: 存在多个解释或来源冲突
- `unexplained_move`: 暂无高质量解释，只能进入 watchlist

### `separate-signal-from-noise`

按信息价值排序：

- 影响多资产或多行业的变量优先
- 改变预期、贴现率、盈利、流动性或风险溢价的变量优先
- 有 follow-through 可能的异常移动优先
- 单日 price-only 且无来源支持的解释降级为 `watch_only`

### `write-briefing`

使用匹配模板输出 brief。`quick_map` 可只输出简版；`standard` 和 `deep_dive`
必须写清 source notes、refresh boundary 和 escalation queue。

### `escalate-or-close`

把高信息量条目路由到下一步：

- 单票新问题 -> `first_pass_research` 或 `quick_map`
- 已有 thesis 增量 -> `monitoring_update`
- 财报/指引/业绩会 -> `earnings_event`
- 研报或 rating/target change -> `research_report_interpretation`
- 宏观数据发布 -> macro data release triage / macro overlay
- 真实持仓或组合风险 -> `position_review` / `portfolio_construction_review`
- 仅价格异动且来源弱 -> `watch_only`

## Source Handling Rules

- 日报和收盘复盘必须优先使用带时间戳的市场数据、官方日历、公司 IR、监管、交易所、
  央行、统计机构或高质量市场媒体。
- 周报可以使用机构周度评论、策略 note、公开研究和图表，但必须标注 publish date。
- 使用付费研报、vendor export、用户文件或截图时，先走
  [../data/ingestion-layer.md](../data/ingestion-layer.md)。
- 弱信号、社媒和传闻只能进入 `weak_signal` 或 `watch_only`，不能支撑 durable
  conclusion。
- 任何实时或接近实时的结论都必须写清 `stale_after`；盘前简报通常在开盘后失效，
  收盘复盘通常在下一交易日前或重大隔夜事件后失效。

## Output

- `briefing header`
- `market snapshot`
- `key moves`
- `driver map`
- `calendar / catalyst watch`
- `facts / inferences / judgments`
- `research escalation queue`
- `source notes`
- `stale_after`
- `must_refresh_if`

## Boundaries

- 不输出交易指令、仓位大小或自动执行建议。
- 不声称 Mira 在后台持续盯盘；除非用户显式创建 automation，否则 brief 只在用户触发
  或当前任务内运行。
- 不把日报/周报替代完整 thesis research；brief 的核心价值是 triage、refresh 和
  escalation。
