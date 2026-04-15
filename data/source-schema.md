# Source Schema

所有进入正式研究包的来源，都必须登记为一个 source record。

## Required Fields

| field | required | description |
| --- | --- | --- |
| `source_id` | yes | 全仓库唯一标识，例如 `apple_q1_2026_pr` |
| `source_name` | yes | 来源名称 |
| `source_type` | yes | `text` / `structured` / `derived` |
| `source_group` | yes | `official_and_industry` / `market_data` / `sellside_research` / `social_and_community` / `derived_analysis` |
| `content_mode` | yes | `filing` / `press_release` / `news` / `market_data` / `transcript` / `note` / `dataset` |
| `authority_level` | yes | `L1` 到 `L6` |
| `credibility_level` | yes | `A` / `B` / `C` / `D` |
| `content_type` | yes | `fact` / `evidence` / `logic` / `opinion` / `sentiment` / `rumor` |
| `research_role` | yes | `primary` / `secondary` / `signal` / `blocked` |
| `market_scope` | yes | `US` / `CN` / `global` / `multi` |
| `access_method` | yes | `repo_local` / `web_search` / `manual_attach` / `derived` |
| `acquisition_mode` | yes | `free` / `paid` / `manual` |
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
| `upstream_sources` | 如果该来源是解读或派生内容，记录其上游来源 |

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

## Source Groups

- `official_and_industry`：公司官网、IR、财报、监管、行业协会、官方统计、大型行业站。
- `market_data`：Yahoo、价格、估值、财务快照、技术面数据。
- `sellside_research`：券商研报、付费研究、专家访谈纪要。
- `social_and_community`：X、论坛、社区、自媒体、短视频、花边。
- `derived_analysis`：由 agent 或研究员整理出的中间表、判断和结论。

## Credibility Levels

| level | meaning | examples |
| --- | --- | --- |
| `A` | 高可信原始或官方来源 | 财报、公告、监管、官方统计 |
| `B` | 高质量二手来源 | 券商深度、专业行业站、权威媒体 |
| `C` | 观点型来源 | 大V长文、长视频、播客、访谈解读 |
| `D` | 噪音或低可信来源 | 短视频切片、匿名帖子、未验证传闻 |

## Content Types

- `fact`：直接事实。
- `evidence`：可支撑判断的证据。
- `logic`：可复核的推理链。
- `opinion`：观点或判断。
- `sentiment`：情绪和市场叙事。
- `rumor`：未经验证传闻。

## Research Roles

- `primary`：可直接支撑核心结论。
- `secondary`：可辅助论证，但不单独定结论。
- `signal`：只用于发现线索、观察叙事和情绪。
- `blocked`：不得进入正式研究结论。

## Validation Rules

- 没有 `source_id` 的材料不能进入 `evidence log`。
- `L6` 必须指向至少一个上游 `L1` 到 `L5` 来源。
- `web_search` 来源与 `repo_local` 来源字段完全一致，不另开口径。
- 没有 `last_checked_date` 的来源不能支撑正式结论。
- `social_and_community` 默认不能是 `primary`。
- `rumor` 默认必须标记为 `blocked`。
- `paid` 来源不能自动获取，应先经过购买建议或人工确认。
