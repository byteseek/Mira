# Monitoring Loop

`monitoring-loop` 用于对一个已建立 thesis 的研究主题做持续更新。

它不是重新研究全案，而是增量扫描、增量记录、增量判断。

## Objective

- 每天或每周扫描新增信号
- 按主题 monitor 更新内容
- 判断是否需要升级回 `research-loop`

## Loop Input

- `theme`
- `watch_scope`
- `last_research_package`
- `memory_refs`

## Monitoring Roles

- `technical-monitor`
  关注趋势、关键位、量价、相对强弱
- `market-data-monitor`
  扫描 Yahoo 等市场数据源，更新价格、估值、量价和技术面快照
- `sellside-research-monitor`
  扫描研报来源，筛选值得进一步获取的研报，并生成购买建议或已读摘要
- `official-and-industry-monitor`
  扫描官网、IR、监管、行业协会和大型行业站
- `social-sentiment-monitor`
  扫描 X、论坛、访谈、花边、短视频与市场叙事变化
- `filing-and-news-monitor`
  扫描公告、财报、新闻、管理层表态
- `research-orchestrator`
  汇总更新并判断是否触发升级

## States

### `scan-updates`

扫描增量信息，不重写整份研究。

### `filter-noise`

对低价值、重复、无日期、无来源的信息降噪，并按 `credibility_level`、`content_type`、`research_role` 做分层。

### `write-monitor-log`

把有效增量写入当期监控记录。

### `assess-impact`

判断增量是否改变 thesis、风险、节奏或跟踪指标。

### `escalate-or-close`

- 小更新：结束本轮 monitoring
- 核心前提变化：升级回 `research-loop`

## Escalation Rules

- 财报、指引、重大公告改变核心判断
- 原 thesis 的关键证据被削弱
- 重大事件改变公司、行业或估值叙事
- 长期跟踪指标连续恶化
- 用户要求重做完整研究

## Source Handling Rules

- `official_and_industry` 优先进入核心更新检查。
- `market_data` 用于价格、估值、技术面和市场背景更新。
- `sellside_research` 先做 `scan -> recommend -> approve -> ingest`，不默认自动购买。
- `social_and_community` 默认作为 `signal`，除非其内容具备明确证据链和可验证逻辑。
- `rumor` 与 `blocked` 内容不进入正式 monitoring 结论。

## Output

- `monitor summary`
- `impact assessment`
- `escalation decision`
