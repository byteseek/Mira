# Mira Analysis Routing

这个文档定义 Mira 在正式研究前的总路由。

目标是先判断“这是什么类型的研究任务”，再决定进入哪个 loop / skill。不要一开始就把所有问题都塞进单票 `framework-routing`。

## Core Rule

按以下顺序路由：

1. `task_mode`
2. `research_object`
3. `time_boundary`
4. `primary_skill_or_loop`
5. `equity_route`
6. `overlays_and_lenses`
7. `output_package`

如果前面步骤已经说明任务不是单票公司研究，就不要强行进入 `equity-research-core`。

## Required Routing Output

每次正式研究前先记录：

- `task_mode`
- `research_object`
- `market_scope`
- `time_boundary`
- `primary_skill_or_loop`
- `routing_basis`
- `routing_mismatch_risk`
- `expected_output_package`

如果进入单票研究，还要继续记录：

- `horizon_bucket`
- `selected_framework`
- `selected_overlays`
- `selected_lenses`

## Step 1: Task Mode

### `first_pass_research`

用于首次覆盖、重建 thesis、从零建立研究包。

默认进入：

- `loops/research-loop.md`

### `monitoring_update`

用于已有 thesis 的增量更新。

默认进入：

- `loops/monitoring-loop.md`

如果新增信息改变核心前提，再升级回 `research-loop`。

### `earnings_event`

用于新财报、业绩会、指引或财报后市场反应。

默认先进入：

- `skills/earnings-report-analysis/SKILL.md`

如果财报改变长期 thesis，再同步更新：

- `templates/research-package/`

### `methodology_review`

用于研究方法本身、框架质量、方法是否值得纳入 Mira。

默认进入：

- `loops/methodology-research-loop.md`

### `discovery_or_screening`

用于找候选、发现新 ETF、发现产业链标的或建立 watchlist。

默认进入相应 discovery skill，而不是直接写投资 memo。

## Step 2: Research Object

### `single_equity`

对象是具体公司或 ticker。

默认进入：

- `skills/equity-research-core/SKILL.md`

如果任务是财报事件，先走 `earnings-report-analysis`，再判断是否更新单票研究包。

### `industry_concept`

对象是产业、技术、材料、工艺、设备、供应链概念或主题。

默认进入：

- `skills/industry-concept-analysis/SKILL.md`

完成后用 `stock_research_handoff` 决定哪些公司进入单票研究。

### `macro_asset_or_regime`

对象是宏观状态、利率、通胀、美元、信用、流动性、指数、周期资产或宏观敏感资产。

默认进入：

- `skills/macro-economic-analysis/SKILL.md`

如果最终落到具体公司，再作为 `macro` overlay 交给单票研究。

### `etf_or_product_listing`

对象是 ETF、新产品、上市结构、持仓暴露或 ETF 发行趋势。

默认进入：

- `skills/etf-listing-discovery/SKILL.md`
- `skills/etf-listing-analysis/SKILL.md`

### `methodology`

对象是研究方法、框架、指标、信号或分析流程。

默认进入：

- `loops/methodology-research-loop.md`

## Step 3: Time Boundary

时间边界先于单票框架选择。

- `intraday_to_days`
  只适合 monitoring、technical context 或事件跟踪，不输出长期 thesis。
- `1Q_2Q`
  进入 `near_term_execution`。
- `2Q_8Q_or_FY1_FY2`
  进入 `medium_term_revision`。
- `gt_1y`
  进入 `long_term_thesis`。
- `transition`
  短期证据可能改变长期 thesis，进入 `regime_transition`。

单票时间跨度规则见：

- `skills/equity-research-core/references/thesis-horizon-routing.md`

## Step 4: Single-Equity Route

如果 `research_object = single_equity`，按以下顺序继续：

1. 运行 `thesis-horizon-routing`
2. 运行 `framework-routing`
3. 运行 `overlay-routing`
4. 判断是否使用 `variant-perception` lens
5. 选择输出包和刷新条件

单票主框架只回答“当前主要由什么变量定价”，不回答任务是不是财报、产业、宏观或方法论。

## Step 5: Overlays And Lenses

### Overlays

overlay 是额外证据路径，不替代主框架。

当前默认：

- `supply-chain`
- `macro`

选择规则见：

- `skills/equity-research-core/references/overlay-routing.md`

### Lenses

lens 是对 thesis 的约束视角，不是额外研究对象。

当前可用：

- `variant-perception`
  用于判断市场预期、分歧点和重定价路径。

使用 lens 时必须写：

- `selected_lenses`
- `lens_basis`
- `what_it_forces_us_to_check`

## Output Package Routing

### Research Package

用于单票首次覆盖或重建 thesis：

- `investment-memo.md`
- `case-notes.md`
- `evidence-log.csv`

### Earnings Package

用于财报事件：

- `earnings-analysis.md`
- `financial-snapshot.csv`
- `peer-comparison.csv`
- `evidence-log.csv`

如果财报改变 thesis，再更新 research package。

### Industry Package

用于产业概念：

- `industry-map.md`
- `company-map.csv`
- `evidence-log.csv`

### Methodology Package

用于方法论：

- `methodology-card.md`
- `methodology-search-log.csv`
- `methodology-review-log.csv`
- methodology queue update

### Monitor Summary

用于增量更新：

- `monitor summary`
- `impact assessment`
- `escalation decision`
- `framework still valid?`
- `overlay still valid?`

## Mismatch Risks

每次 routing 都要写明最可能的错配：

- 把财报事件误当成长期首次覆盖
- 把产业概念误当成单票研究
- 把宏观背景误当成宏观主导
- 把 monitoring 小更新误升级为完整 thesis 重写
- 把长期产业 thesis 写成短期交易结论
- 把单票框架错配成错误的市值/流动性/机构持仓 regime

## Stop Rules

- 如果研究对象不清楚，先输出 `routing_unclear`，只做定义澄清，不进入结论。
- 如果时间边界不清楚，默认按用户问题最近的显性时间词判断，并写 `horizon_uncertainty`。
- 如果来源不足以支撑 durable conclusion，只能输出低置信判断和刷新条件。
- 如果总路由与用户明确要求冲突，遵循用户要求，但记录 `routing_override`。
