# Time Policy

这个文件定义回看窗口、前瞻窗口和结论失效规则。

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

