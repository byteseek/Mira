# Monitoring Loop

`monitoring-loop` 用于对一个已建立 thesis 的研究主题做持续更新。

它不是后台采集任务，也不是重新研究全案；它只在用户触发或研究需要时按需读取、增量记录、增量判断。

## Objective

- 在用户触发、研究刷新或明确监控窗口内检查新增信号
- 按主题 monitor 更新内容
- 判断是否需要升级回 `research-loop`
- 判断当前 `selected_framework` 是否仍然成立
- 判断当前 overlay 是否仍然值得保留

## Loop Input

- `theme`
- `watch_scope`
- `last_research_package`
- `memory_refs`

## Monitoring Roles

- `technical-monitor`
  关注趋势、关键位、量价、相对强弱
- `market-data-monitor`
  按需读取 Yahoo Finance、StockAnalysis、MacroTrends、Stooq 等市场数据页面，更新价格、估值、量价和技术面快照
- `sellside-research-monitor`
  扫描研报来源，筛选值得进一步获取的研报，并生成购买建议或已读摘要
- `official-and-industry-monitor`
  扫描官网、IR、监管、行业协会和大型行业站
- `social-sentiment-monitor`
  扫描 X、论坛、访谈、花边、短视频与市场叙事变化
- `filing-and-news-monitor`
  扫描公告、财报、新闻、管理层表态
- `macro-data-monitor`
  按需读取 FRED、BLS、BEA 等公开宏观页面或端点，更新利率、通胀、就业、GDP 和行业周期背景
- `research-orchestrator`
  汇总更新并判断是否触发升级

## States

### `scan-updates`

扫描增量信息，不重写整份研究。

### `filter-noise`

对低价值、重复、无日期、无来源的信息降噪，并按 `credibility_level`、`content_type`、`research_role` 做分层。

### `classify-incremental-claims`

把有效增量拆成 claim，并按 [../data/claim-taxonomy.md](../data/claim-taxonomy.md) 标注 `claim_type`、`source_speaker` 和 `verification_status`。

监控时必须回答：

- 新信息是事实、公司口径、承诺、指引、预测、假设、观点、弱信号，还是市场定价？
- 它是验证旧 thesis、削弱旧 thesis、替代旧假设，还是只是噪音？
- 它是否改变了旧 evidence log 中某条 claim 的 `verification_status`？
- 它是否触发 `stale_after`、`must_refresh_if` 或完整重研？

### `write-monitor-log`

把有效增量写入当期监控记录。

### `assess-impact`

判断增量是否改变 thesis、风险、节奏、跟踪指标、当前框架或已选 overlay。

### `update-expectation-map`

把有效增量映射到具体预期变量：

- revenue
- margin
- cash flow
- capex
- balance sheet risk
- valuation multiple
- risk premium
- positioning
- catalyst timing

如果无法定位到变量，只能作为 watch item，不能升级 thesis。

### `thesis-state-change`

判断是否更新 `thesis-ledger` 状态：

- `active -> upgrade_watch`
- `active -> downgrade_watch`
- `active -> stale`
- `watch -> active`
- `watch -> retired`
- `downgrade_watch -> retired`
- `stale -> active`

所有状态变化必须指向 evidence log 或 explicit source note。

### `escalate-or-close`

- 小更新：结束本轮 monitoring
- 核心前提变化：升级回 `research-loop`

## Escalation Rules

- 财报、指引、重大公告改变核心判断
- 原 thesis 的关键证据被削弱
- 原 thesis 的关键承诺没有兑现，或公司口径与已验证事实出现冲突
- 原本只是 `assumption`、`forecast` 或 `company_claim` 的关键输入被新证据证实或证伪
- 重大事件改变公司、行业或估值叙事
- 长期跟踪指标连续恶化
- 标的的主导定价变量发生变化，导致原框架可能失效
- 原 overlay 的关键传导链被证伪或失去增量价值
- 用户要求重做完整研究

## Source Handling Rules

- `official_and_industry` 优先进入核心更新检查。
- `market_data` 用于价格、估值、技术面和市场背景更新。
- `web_read`、`web_search` 与 `public_api` 都是按需读取；必须记录 ticker、series id、CIK、参数、读取日期和 as-of date。
- `sellside_research` 先做 `scan -> recommend -> approve -> ingest`，不默认自动购买。
- `social_and_community` 默认作为 `signal`，除非其内容具备明确证据链和可验证逻辑。
- `rumor` 与 `blocked` 内容不进入正式 monitoring 结论。
- `market_pricing` 可用于判断市场反应和预期变化，但不能替代基本面 claim。

## Output

- `monitor summary`
- `impact assessment`
- `expectation map update`
- `thesis state change decision`
- `escalation decision`
- `framework still valid?`
- `overlay still valid?`
- Step 4.5 critical interaction: ask one natural-language next question that either confirms the escalation path, closes the most important source gap, or waives follow-up with a reason.
