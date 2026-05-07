# Source Policy

这个文件定义来源分组、优先级、可信度、使用边界和引用规则。

## Source Groups

默认按以下四类外部来源 + 一类派生来源组织：

1. `official_and_industry`
2. `market_data`
3. `sellside_research`
4. `social_and_community`
5. `derived_analysis`

## Priority

默认优先级从高到低：

1. `L1` 原始披露
2. `L2` 官方/监管/行业机构
3. `L3` 高质量二手研究
4. `L4` 新闻与访谈
5. `L5` 市场数据
6. `L6` 派生判断

默认研究优先级从高到低：

1. `official_and_industry`
2. `market_data`
3. `sellside_research`
4. `social_and_community`
5. `derived_analysis`

## Credibility And Role Rules

- `A` 级来源可作为 `primary` 或 `secondary`。
- `B` 级来源通常作为 `secondary`，部分可作为补充性 `primary`。
- `C` 级来源默认作为 `signal`，只有证据链清晰时才可升为 `secondary`。
- `D` 级来源默认不高于 `signal`，其中 `rumor` 必须为 `blocked`。

## Content-Type Rules

- `fact` 与 `evidence` 权重高于 `opinion` 与 `sentiment`。
- 有上游来源可复核的 `logic` 高于纯观点式 `opinion`。
- `sentiment` 适合观察叙事变化，不直接支撑核心 thesis。
- `rumor` 只可用于线索发现，不得写入正式 memo。

## Usage Rules

### Facts

- 公司财务、业务结构、资本配置、管理层原话，优先使用 `L1`。
- 政策、监管、行业统计，优先使用 `L2`。
- 价格、估值、52 周区间、成交量，允许使用 `L5`。
- 核心事实默认优先使用 `official_and_industry`。

### Interpretation

- `L3` 和 `L4` 可以帮助解释行业变化、事件影响和市场情绪。
- `L3` 和 `L4` 不能单独支撑核心投资结论。
- `L6` 只能写成推断、情景或派生结果，不能伪装成事实。
- `sellside_research` 可用于补行业框架、竞争格局和估值讨论，但不应替代原始披露。
- `social_and_community` 只应用于发现线索、观察情绪或辅助判断叙事变化。

### Web Sources

- `web_search` 不是例外路径，而是正式来源输入方式。
- 通过网页取得的材料，也必须补齐 `source_id`、日期、适用场景和权重说明。
- 引用网页材料时，应优先选择原始页面，其次是高质量转载或聚合页。

### Public On-Demand Sources

- `web_read` 用于已知 URL 的按需读取和解析；`web_search` 用于先搜索发现来源再读取。
- `web_search`、`web_read` 和 `public_api` 都是按需读取入口，不代表后台订阅、定时采集、批量抓取或本地落库。
- `public_api` 用于 SEC、FRED、BLS、BEA 等公开 JSON/API 页面入口；只在具体研究需要时请求。
- `free_with_key` 表示免费但需要申请 API key、注册账号或遵守明确限流。
- Yahoo Finance、StockAnalysis、MacroTrends、Stooq 等市场数据源默认是 `L5`，用于价格、估值、量价、快照和交叉核验。
- Yahoo Finance 的新闻、分析师预期和 profile 不是原始披露：新闻必须追到原始媒体或公告；分析师预期只用于共识、修正和情绪；profile 只用于快速定位业务描述。
- SEC EDGAR、公司 IR、监管和官方统计仍优先于聚合站。若 Yahoo/StockAnalysis 与 SEC 或公司披露冲突，以原始披露为准。
- 可复用 target 模板可进入 `source-registry.csv`，但正式案例必须写明具体 ticker、CIK、series id、读取日期和数据时点。

### Paid Research

- `sellside_research` 中的 `paid` 来源不自动购买。
- 标准流程应为：`scan -> recommend -> approve -> ingest`。
- 未完成购买确认的付费来源，不能假设其内容存在。

### Social Sources

- 大V长文、长视频、播客和访谈可作为 `C` 级观点源。
- X、论坛、短视频和社区帖子默认作为 `signal`。
- 只有当观点源给出明确证据链和可验证逻辑时，才可从 `signal` 升级到 `secondary`。

## Citation Rules For Cases

每个案例中的核心结论至少满足以下约束：

- 至少一个 `L1` 或 `L2` 来源支撑核心事实
- 至少一个 `L5` 来源支撑价格或市场背景
- 如果写事件催化剂，至少一个 `L4` 或 `L1` 来源支撑
- 如果出现推断或情景分析，必须写明其上游来源
- 如果使用 `sellside_research` 或 `social_and_community`，应明确其 `research_role`

## Explicitly Disallowed

- 只凭新闻写业务质量结论
- 只凭股价走势写基本面结论
- 把没有日期的数据写入正式 memo
- 用没有登记到 `evidence log` 的来源支撑投资结论
- 把 X、短视频、匿名论坛帖子直接写成核心事实
- 把观点型来源当作原始证据引用
- 在未确认购买前假设付费研报已可用
