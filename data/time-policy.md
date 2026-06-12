# Time Policy

这个文件定义回看窗口、前瞻窗口和结论失效规则。

## Market-Date Resolution

当用户使用 `今天`、`现在`、`目前`、`latest`、`盘前`、`盘后`、`收盘`、
`本周` 等相对时间词，先确定 `market_scope`，再把相对日期投影到该市场的
主交易时区。不要用用户所在地日期或运行环境日期覆盖市场日期。

默认主交易时区：

| market_scope | market_timezone | market date basis |
| --- | --- | --- |
| US equities / US index / US options | `America/New_York` | 美东交易日，含盘前/盘后 session |
| CN A-share | `Asia/Shanghai` | 中国交易日 |
| HK equities | `Asia/Hong_Kong` | 香港交易日 |
| JP equities | `Asia/Tokyo` | 日本交易日 |
| TW equities | `Asia/Taipei` | 台湾交易日 |
| KR equities | `Asia/Seoul` | 韩国交易日 |
| EU equities | issuer primary venue timezone | 先确认主要上市地/交易场所 |
| FX / crypto / commodity | venue or instrument convention | 记录具体 venue / convention |

必须记录或可追溯：

- `user_local_datetime` when known, especially across midnight.
- `market_timezone`.
- `market_session_date`: 用于行情、K 线、日内涨跌和“今天”的交易日。
- `as_of_date`: 必须等于来源实际 quote / close / publication 所属日期。
- `quote_time` / `publish_time`: 带时区偏移或明确时区名称。

跨时区硬规则：

- 美股问题里，中文用户说“今天”时，默认解释为美东市场的今天，而不是中国、
  新加坡或系统本地的日期。例：用户所在地是 `Asia/Shanghai` 的 6 月 12 日
  早晨，但纽约仍是 6 月 11 日盘后，则美股 `market_session_date` 是
  `YYYY-06-11`，不能抓取或引用中国 6 月 12 日的“今日行情”来回答美股。
- 反向也成立：用户在美国且本地仍是 6 月 11 日时，如果研究对象是中/韩/日、
  港股、台股或其他东亚市场，`今天` 默认按该市场本地交易日解释，而不是美国
  本地日期。例：纽约仍是 6 月 11 日晚间，但上海、首尔或东京已是 6 月 12 日
  交易时段，则对应市场分别使用 `Asia/Shanghai`、`Asia/Seoul` 或
  `Asia/Tokyo`，`market_session_date=YYYY-06-12`。
- 如果市场已休市，说明是 regular close、premarket、after-hours 还是下一交易日
  尚未开盘；不要把盘后报价和下一交易日 regular session 混成一个日期。
- 如果无法确认市场时区或来源时点，输出 `source_gap` / `needs_refresh`，不要用
  相对日期做正式结论。

## Default Windows

| task | default_window | purpose |
| --- | --- | --- |
| 结构性基本面 | 过去 `3-5 年` | 判断商业质量、资本配置、盈利稳定性 |
| 经营趋势 | 过去 `4-6 个季度` | 观察拐点、库存、产品周期、利润修复 |
| 技术面 | 过去 `3-12 个月` | 观察趋势、区间、相对强弱、关键位置 |
| 事件与舆情 | 过去 `30-180 天` | 观察催化剂、扰动、叙事变化 |
| 投资主判断 | 向前 `12-24 个月` | 构建中长线 thesis |

## Hard Rules

- 超过 `24 个月` 的前瞻只能作为长期情景，不作为高置信结论。
- 超过 `5 年` 的历史只在治理、周期、资本配置回顾时默认使用。
- 没有明确 `as_of_date` 的数据不能进入正式结论。
- 实时市场数据如果延迟，必须在 `notes` 中标明。

## Staleness Rules

每份 `investment memo` 都必须写出：

- `research_cutoff_date`
- `financial_data_through`
- `price_date`
- `stale_after`
- `must_refresh_if`

## Recommended Refresh Triggers

- 新财报或年报发布
- 指引显著变化
- 重大产品延期或上线
- 并购、分拆、回购、分红政策重大调整
- 价格突破关键技术区间
- 政策、关税、监管规则发生重大变化

## Case-Level Defaults

如果案例没有单独说明，默认按以下规则刷新：

- 财务与基本面：下一个财报后刷新
- 技术面：`30` 天内视为有效
- 事件面：`14` 天后默认降级为背景信息
- 完整 research package：`90` 天后视为过期，需要重新审核
