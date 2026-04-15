# Source Schema

所有进入正式研究包的来源，都必须登记为一个 source record。

## Required Fields

| field | required | description |
| --- | --- | --- |
| `source_id` | yes | 全仓库唯一标识，例如 `apple_q1_2026_pr` |
| `source_name` | yes | 来源名称 |
| `source_type` | yes | `text` / `structured` / `derived` |
| `content_mode` | yes | `filing` / `press_release` / `news` / `market_data` / `transcript` / `note` / `dataset` |
| `authority_level` | yes | `L1` 到 `L6` |
| `market_scope` | yes | `US` / `CN` / `global` / `multi` |
| `access_method` | yes | `repo_local` / `web_search` / `manual_attach` / `derived` |
| `update_frequency` | yes | `real_time` / `daily` / `quarterly` / `event_driven` / `irregular` |
| `latency_class` | yes | `live` / `delayed` / `filing_cycle` / `archival` |
| `as_of_date_required` | yes | `yes` / `no` |
| `usable_for` | yes | 该来源适用的研究任务，使用 `;` 分隔 |
| `url_or_path` | yes | 原始链接或本地路径 |
| `last_checked_date` | yes | 最后核验日期，格式 `YYYY-MM-DD` |

## Optional Fields

| field | description |
| --- | --- |
| `publisher` | 发布方 |
| `notes` | 对数据质量、滞后性、使用限制的说明 |
| `coverage` | 该来源覆盖的公司、市场、时间范围 |

## Authority Levels

| level | meaning | examples |
| --- | --- | --- |
| `L1` | 原始披露 | 年报、季报、公告、业绩会、招股书 |
| `L2` | 官方/监管/行业机构 | SEC、交易所、统计局、行业协会 |
| `L3` | 高质量二手研究 | 券商深度、专业行业研究 |
| `L4` | 新闻与访谈 | Reuters、Bloomberg、主流财经媒体 |
| `L5` | 市场数据 | 价格、估值、量能、分析师预期 |
| `L6` | 派生判断 | agent 估算、模型推导、中间结论 |

## Source Type Rules

- `text`：可直接阅读的文本源，例如公告、新闻、访谈。
- `structured`：表格或时间序列数据，例如价格、财务、估值。
- `derived`：从原始来源加工出的模型表或分析结论。

## Validation Rules

- 没有 `source_id` 的材料不能进入 `evidence log`。
- `L6` 必须指向至少一个上游 `L1` 到 `L5` 来源。
- `web_search` 来源与 `repo_local` 来源字段完全一致，不另开口径。
- 没有 `last_checked_date` 的来源不能支撑正式结论。

