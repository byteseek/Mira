# Mira Analysis Routing

这个文档定义 Mira 在正式研究前的总路由。

目标是先判断“这是什么类型的研究任务”，再决定进入哪个 loop / skill。不要一开始就把所有问题都塞进单票 `framework-routing`。

## Core Rule

按以下顺序路由：

1. `task_mode`
2. `research_object`
3. `time_boundary`
4. `quant_dependency`
5. `primary_skill_or_loop`
6. `equity_route`
7. `overlays_and_lenses`
8. `output_package`

如果前面步骤已经说明任务不是单票公司研究，就不要强行进入 `equity-research-core`。

## Required Routing Output

每次正式研究前先记录：

- `task_mode`
- `research_object`
- `market_scope`
- `time_boundary`
- `quant_dependency`
- `calculation_gate`
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

### `sec_supplement`

用于在单票研究、财报分析、monitoring 或事件分析中补充 SEC 事实核验。

默认不独立成完整报告，而是补到当前研究包：

- `templates/sec-supplement-source-note.csv`
- 当前 case 的 `evidence-log.csv`
- 当前 case 的 financial snapshot / case notes

使用边界：

- 适合查 CIK、最新 filing timeline、10-K/10-Q/8-K/proxy 是否存在、companyfacts 指标、share count、SBC、debt、cash flow、inventory、RPO/backlog 等事实。
- 不做完整 filing 解剖。
- 如果 filing 与 release、管理层口径或聚合数据冲突，升级为 `sec_filing_deep_dive`。

### `sec_filing_deep_dive`

用于专项分析 SEC 文件本身，例如 10-K、10-Q、S-1、8-K exhibit、DEF 14A 或 13F / Form 4。

默认进入：

- `skills/sec-filing-analysis/SKILL.md`

使用边界：

- 用户明确要求“拆 filing / 年报 / 10-K / 10-Q / S-1 / proxy / 8-K exhibit”。
- 或核心 thesis/actionability 依赖 filing 细节、会计质量、风险因素、股权结构、客户集中度、债务/流动性、相关方交易、segment 口径。
- 输出 filing-level 结论后，再决定是否更新 research package、earnings package 或 thesis system。

### `thesis_system_update`

用于已有研究对象的 thesis 更新、预期差判断、事件 delta、状态变更或复盘。

默认进入：

- `loops/thesis-update-loop.md`

如果触发点是明确事件，例如财报、FOMC、产品发布、监管决定或同业 read-through，先进入：

- `loops/event-delta-loop.md`

如果事件 delta 改变核心前提，再升级回：

- `loops/research-loop.md`

### `position_review`

用于用户明确要求 review 自己的头寸、某个持仓、仓位是否匹配 thesis、是否需要加证据/降风险/退出复盘。

默认进入：

- `loops/position-review-loop.md`

如果没有提供真实持仓、权重、成本、约束或组合语境，只能输出 `research_only` 或 `no_position_data`，不能做 position-size 结论。

### `portfolio_construction_review`

用于真实投资组合或多头寸结构复盘，例如主题集中、因子暴露、重复 bet、催化剂拥挤、流动性风险、风险预算或组合层 thesis 冲突。

默认进入：

- `loops/portfolio-construction-review-loop.md`

如果只是多 thesis 维护、没有真实持仓或权重，保留在：

- `loops/portfolio-review-loop.md`

### `decision_quality_review`

用于复盘过去的研究判断、头寸动作或组合决策质量。

默认进入：

- `loops/decision-quality-review-loop.md`

如果只是在更新 thesis state 或记录事件 delta，使用 `thesis_system_update`，不要升级成完整决策质量复盘。

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

### `commodity_or_resource_cycle`

对象是具体大宗商品、商品期货曲线、库存、供需平衡、成本曲线、资源周期、资源股商品 beta 或商品 ETF。

默认进入：

- `skills/commodity-cycle-analysis/SKILL.md`

如果最终落到具体公司，再作为 `commodity` overlay 交给单票研究；如果商品冲击改变通胀、利率、财政、外部账户或风险偏好，再同步启用 `macro` overlay。

### `etf_or_product_listing`

对象是 ETF、新产品、上市结构、持仓暴露或 ETF 发行趋势。

默认进入：

- `skills/etf-listing-discovery/SKILL.md`
- `skills/etf-listing-analysis/SKILL.md`

### `methodology`

对象是研究方法、框架、指标、信号或分析流程。

默认进入：

- `loops/methodology-research-loop.md`

### `filing_or_disclosure`

对象是具体 SEC 文件、监管披露、招股书、proxy、8-K exhibit 或一组 filing 差异。

默认按问题深度路由：

- 只为其他研究补事实：`sec_supplement`
- 研究 filing 本身：`sec_filing_deep_dive`

### `thesis_object`

对象是已有 thesis、预期差地图、事件影响、研究动作或复盘记录。

默认进入：

- `loops/thesis-update-loop.md`

如果问题明确围绕事件前后变化，进入：

- `loops/event-delta-loop.md`

### `position_or_portfolio`

对象是用户提供的真实头寸、持仓清单、组合、watchlist + holdings 混合表，或一组需要从 PM 角度复盘的 thesis。

默认按数据可得性分流：

- 单一真实头寸：`loops/position-review-loop.md`
- 多个真实头寸或组合结构：`loops/portfolio-construction-review-loop.md`
- 多 thesis 但无真实持仓：`loops/portfolio-review-loop.md`
- 过去决策质量复盘：`loops/decision-quality-review-loop.md`

真实头寸或组合结论必须先记录 `position_data_status` 或 `portfolio_review_scope`。

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

If `time_boundary = gt_1y` and the question depends on multiple operating variables, hot-theme-to-company handoff, product monetization, pull-forward demand, or valuation expectations, route to:

- `loops/long-term-thesis-loop.md`

This loop is currently `candidate_internal_release`, not final external-grade.

单票时间跨度规则见：

- `skills/equity-research-core/references/thesis-horizon-routing.md`

## Step 3.5: Quant Dependency Check

在选择最终输出包之前，判断研究结论是否依赖数量型判断。

如果触发以下任一条件，必须运行：

- `skills/data-analysis-quality-gate/SKILL.md`

触发条件：

- 同比、环比、CAGR、run-rate、margin bridge
- peer comparison、peer ranking、相对估值或相对财务质量
- valuation implied expectation、base / bull / bear scenario math
- 市场规模、渗透率、份额、TAM / SAM / SOM
- 财报三表交叉校验、现金流质量、营运资本异常
- 宏观、商品、价格、库存、利率、就业或通胀时间序列
- 多来源数字冲突或口径不一致
- 任何会影响 `thesis_impact`、`research_action`、`actionability_bridge` 或 durable conclusion 的数量判断

路由输出必须记录：

- `quant_dependency`: `none` / `low` / `medium` / `high`
- `calculation_gate`: `not_required` / `required` / `waived`
- `calculation_gate_basis`
- `tool_consent_required`: `yes` / `no`

如果 `calculation_gate = required` 但用户选择不计算，或当前来源不足以计算，必须把相关结论降级为 `calculation_gap`、`source_gap`、`watch_only`、`needs_refresh` 或 `no_action`。

## Step 4: Single-Equity Route

如果 `research_object = single_equity`，按以下顺序继续：

1. 运行 `thesis-horizon-routing`
2. 运行 `framework-routing`
3. 运行 `overlay-routing`
4. 判断是否使用 `variant-perception` 或 `long-term-multibagger` lens
5. 选择输出包和刷新条件

单票主框架只回答“当前主要由什么变量定价”，不回答任务是不是财报、产业、宏观或方法论。

## Step 5: Overlays And Lenses

### Overlays

overlay 是额外证据路径，不替代主框架。

当前默认：

- `supply-chain`
- `macro`
- `commodity`

选择规则见：

- `skills/equity-research-core/references/overlay-routing.md`

### Lenses

lens 是对 thesis 的约束视角，不是额外研究对象。

当前可用：

- `variant-perception`
  用于判断市场预期、分歧点和重定价路径。
- `long-term-multibagger`
  用于长期右尾 / 多倍股候选，强制检查 5 年收入空间、10 年终局、5x upside path、市场误解、文化适应性、证据阶梯和错过赢家风险。

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

### SEC Supplement Package

用于当前研究包中的补充型 SEC 核验：

- `sec-supplement-source-note.csv`
- 当前 case 的 `evidence-log.csv`
- 当前 case 的 financial snapshot / case notes 更新
- 如有缺口，追加 `source-gap-refresh.md` 触发条件

### SEC Filing Deep Dive Package

用于专项 SEC 文件分析：

- `filing-analysis.md`
- `filing-metric-table.csv`
- `filing-risk-delta.csv`
- `accounting-quality-check.csv`
- `evidence-log.csv`
- 如影响 thesis，追加 `thesis-impact.md`、`event-delta.md` 或 research package 更新

### Industry Package

用于产业概念：

- `industry-map.md`
- `company-map.csv`
- `evidence-log.csv`

### Commodity Package

用于大宗商品、商品期货曲线、库存、供需平衡、成本曲线或商品 beta 分析：

- `commodity-cycle-note.md`
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

### Thesis System Package

用于 thesis 更新、预期差、事件 delta 或复盘：

- `thesis-ledger.md`
- `expectation-map.csv`
- `event-delta.md`，如有事件
- `decision-log.csv`，如有研究动作
- `postmortem.md`，如为复盘任务

### Position Review Package

用于单一真实或拟议头寸复盘：

- `position-review.md`
- `position-register.csv`，如维护组合文件
- updated `decision-log.csv`，如研究动作变化
- required follow-up and refresh triggers

输出必须使用 `position_data_status`、`position_sizing_context` 和 `position_review_action` token。

### Portfolio Construction Review Package

用于真实组合或 mixed book 复盘：

- `portfolio-construction-review.md`
- `portfolio-exposure-review.csv`
- position-review queue
- stale thesis list
- catalyst calendar
- concentration and duplicate-bet notes

如果没有真实持仓或权重，降级为 `research_book`，不要输出仓位大小判断。

### Decision Quality Review Package

用于研究判断、头寸动作或组合决策的事后质量复盘：

- `decision-quality-review.md`
- updated `postmortem.md`，如属于 thesis object
- updated `thesis-scorecard.csv`，如 confidence calibration 改变
- methodology update candidate，如发现流程错误

### Calculation Artifacts

可附加到任意 output package：

- `data-requirement-brief.md`
- `calculation-ledger.csv`

当 `calculation_gate = required`，且结论包含派生数量判断时，必须输出 calculation artifact，或显式写明 `calculation_gap` / `calculation_waived_by_speed` 和结论降级方式。

## Mismatch Risks

每次 routing 都要写明最可能的错配：

- 把财报事件误当成长期首次覆盖
- 把产业概念误当成单票研究
- 把宏观背景误当成宏观主导
- 把 monitoring 小更新误升级为完整 thesis 重写
- 把长期产业 thesis 写成短期交易结论
- 把单票框架错配成错误的市值/流动性/机构持仓 regime
- 把 research book review 误写成真实组合建议
- 在没有持仓、权重、mandate 或风险预算时输出仓位大小判断
- 把 position review action 误写成已执行交易或具体订单

## Stop Rules

- 如果研究对象不清楚，先输出 `routing_unclear`，只做定义澄清，不进入结论。
- 如果时间边界不清楚，默认按用户问题最近的显性时间词判断，并写 `horizon_uncertainty`。
- 如果来源不足以支撑 durable conclusion，只能输出低置信判断和刷新条件。
- 如果总路由与用户明确要求冲突，遵循用户要求，但记录 `routing_override`。
