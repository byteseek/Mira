# Mira Analysis Routing

这个文档定义 Mira 在正式研究前的总路由。

目标是先判断“这是什么类型的研究任务”，再决定进入哪个 loop / skill。不要一开始就把所有问题都塞进单票 `framework-routing`。

> 机器索引优先：路由决策先读 [../data/routing-index.csv](../data/routing-index.csv)（`task_mode` → 唯一 `primary_loop_or_skill` + 一句话触发条件 + `load_gate`），命中后只加载那一个 loop / skill 正文，**不要前置整篇本文档**。本文档是各 route 的正文与边界细节，按需取用。索引的 `task_mode` 与 [../schemas/vocab.json](../schemas/vocab.json) 同源，`scripts/validate_repo.py` 校验其覆盖完整、路径存在。

## Core Rule

按以下顺序路由（自上而下即执行顺序；括号内为相关正文 Step，编号不一定连续）：

- `intent_intake`（Step 0）
- `decision_pressure_gate`（Step 0.5）
- `task_mode`（Step 1）
- `research_object`（Step 2）
- `time_boundary`（Step 3）
- `private_state_boundary`（Step 3.1）
- `sticky_context_carryover`（Step 3.2）
- `depth_mode_and_budget`（Step 3.25）
- `question_expansion_lens`（Step 3.27）
- `information_value_knowability_gate`（Step 3.3）
- `live_data_gate`（Step 3.35）
- `data_tool_ingestion_gate`（Step 3.4）
- `quant_dependency`（Step 3.5）
- `primary_skill_or_loop`
- `equity_route`（Step 5）
- `overlays_and_lenses`（Step 5）
- `handoff_and_readiness`（Step 4）
- `progressive_followup_prompts`（Step 4.5）
- `output_package`（Output Package Routing）

`intent_intake`（Step 0）先于一切：拆分复合 prompt、声明运行假设、按 depth 缩放入口卡片，再进入 task_mode。它只做拆分和排序，不做任务分类，分类仍由 Step 1 负责。
`decision_pressure_gate`（Step 0.5）只在路由进入 actionability / position / portfolio 时强制输出，禁止静默跳过。
`sticky_context_carryover`（Step 3.2）在同一会话内决定哪些路由字段沿用、哪些在对象切换后重置；跨会话延续必须走 view-continuity 或 private state。
`question_expansion_lens`（Step 3.27）在选定 depth 后、花 source / quant 预算前，选择是否用 comparison、scale shift、trend 或 anomaly lens 改写问题；最多选两个，不触发则 `none`。
`information_value_knowability_gate`（Step 3.3）在选定 depth 后校验问题是否值得深挖、核心变量是否可知，可反向下调 depth，并允许 `irreducible_uncertainty` 作为诚实终态。
`live_data_gate`（Step 3.35）在时间敏感市场问题中强制刷新或搜索同日来源，并记录 `quote_time` / `publish_time`、freshness 和 cross-check 状态。
`data_tool_ingestion_gate`（Step 3.4）在 evidence logging 和 quant dependency 前处理新材料、API、vendor、portfolio export 和 retained derived dataset 的权限、存储、字段映射和证据用途。

如果前面步骤已经说明任务不是单票公司研究，就不要强行进入 `equity-research-core`。

## Internal Routing State

每次正式研究前先记录以下内部路由状态。它是 agent 的工作状态，不是默认
用户可见模板。交付时只按 [../data/output-surface-matrix.md](../data/output-surface-matrix.md)
展示对应 `depth_mode` 需要的字段；短答不得因为本清单而暴露全部机器字段。

Machine-first rule: 当 formal task 需要保留路由结果时，优先生成符合
[../schemas/routing.schema.json](../schemas/routing.schema.json) 的
`routing.json`。用户可见 routing card 是该对象按 depth surface 渲染后的摘要，
不是第二套字段来源。示例见
[../examples/routing-json-examples.md](../examples/routing-json-examples.md)。

每次正式研究前先记录：

- `interaction_mode`
- `primary_intent`
- `secondary_intents`
- `execution_order`
- `scope_confirmation_required`
- `routing_assumptions`
- `assumption_confidence`
- `user_visible_routing_card`
- `task_mode`
- `research_object`
- `market_scope`
- `time_boundary`
- `depth_mode`
- `source_budget`
- `ingestion_route`
- `ingestion_artifacts`
- `source_registry_action`
- `artifact_budget`
- `token_budget_policy`
- `information_value`
- `knowability_status`
- `depth_override_reason`
- `live_data_gate`
- `freshness_status`
- `cross_check_status`
- `quote_time`
- `publish_time`
- `primary_question_lens`
- `selected_question_lenses`
- `lens_selection_basis`
- `lens_data_required`
- `lens_failure_mode`
- `private_state_action`
- `private_state_refs`
- `view_continuity_basis`
- `routing_carryover`
- `carryover_fields`
- `context_reset_trigger`
- `decision_pressure`
- `framing_risk`
- `disconfirmation_required`
- `quant_dependency`
- `calculation_gate`
- `primary_skill_or_loop`
- `routing_basis`
- `routing_mismatch_risk`
- `expected_output_package`
- `expected_handoffs`
- `readiness_level`
- `readiness_basis`
- `followup_prompt_mode`
- `followup_questions`
- `followup_basis`
- `next_route_if_answered`
- `followup_route_binding`
- `followup_object_anchor`
- `followup_decision_impact`

如果进入单票研究，还要继续记录：

- `horizon_bucket`
- `selected_framework`
- `selected_overlays`
- `selected_lenses`

Visible-output rule: `quick_map`, `standard` and `deep_dive` are the only output
surfaces. `quick_answer` is an `interaction_mode`; it controls prose length but
does not create a fourth surface.

## Step 0: Intent + Interaction Intake

在 `task_mode` 之前，先做意图与交互入口处理。目标：复合 prompt 不被压扁成单任务，运行假设对用户显式，且入口本身不浪费 token。

Step 0 只做拆分、排序和假设声明，**不做任务分类**。分类仍由 Step 1 `task_mode` 负责；Step 0 输出的子任务候选逐个进入 Step 1–12，secondary intents 进入队列，不抢 `task_mode`。

### Multi-Intent Decomposition

很多真实 prompt 是复合的，例如“看 NVDA 财报，顺便对比 AMD，这俩我都重仓了”= earnings_event + peer/industry + position/portfolio 三件事。

记录：

- `primary_intent`: 本轮先执行的主任务。
- `secondary_intents`: 其余子任务，进入队列，本轮默认不深做。
- `execution_order`: 子任务执行顺序及理由。
- `scope_confirmation_required`: `yes` / `no`，是否需要先和用户确认范围再花 depth 预算。

规则：

- 如果子任务之间存在 depth 或数据冲突（例如一个要 quick_map、一个要真实持仓 review），先确认范围，不要默认全做。
- secondary intents 在输出末尾用 progressive follow-up 提示是否进入下一轮，不要静默丢弃。

确认即状态（把 `scope_confirmation_required` 从可跳过字段收紧成必经停顿）：

- 触发即必填、不得静默跳过（沿用 Step 0.5 同款纪律）：当 (a) 子任务间 depth / 数据冲突，或 (b) `interaction_mode = decision_support` 且 `decision_pressure ∈ {medium, high}` 时，`scope_confirmation_required = yes` 是**强制**的，不能因为“看起来能直接做”就填 `no`。
- 范围未确认期间冻结预算：当范围确认为 yes 且用户尚未确认、也未明确“别问直接做”时，本轮只按 `quick_map` 给方向、路由卡和运行假设，**不花 `deep_dive` 预算、不产出 durable artifact**，直到用户确认或明确放行。其余情况默认走 Assumption Register（声明假设、先答、邀请修正），不阻塞。

### Interaction Mode

记录 `interaction_mode`：

- `quick_answer`: 用户要一句话方向或事实，不要完整 package。
- `routed_research`: 正常进入 routed loop / skill。
- `decision_support`: 接近 actionability / position / portfolio，必须联动 Step 0.5。
- `routing_unclear`: 研究对象或时间边界完全不清楚，继续会误导；只做定义澄清。

`interaction_mode` 是“答案形状”，与 `depth_mode`（研究力度，Step 3.25）**正交**，不要因为都带 “quick” 就混用：

- `quick_answer` + `quick_map`：看一下方向，浅研究、一句结论。
- `quick_answer` + `deep_dive`：用户只要一句结论，但问题（如“现在贵不贵”）诚实回答需要真估值——答案短、研究深，不能因为是 quick_answer 就跳过 valuation。
- `routed_research` + `quick_map`：早期 triage，仍输出结构化路由卡。

### Assumption Register

Mira 在正式分析前显式声明它正在用的运行假设，先答、同时邀请用户修正，而不是阻塞式追问或静默假设。这是与 Step 4.5 后端 follow-up gate 对称的前端。

记录：

- `routing_assumptions`: 3-4 条本轮假设（真正要判断的问题、market_scope、time_boundary、什么算“答完了”）。
- `assumption_confidence`: `low` / `medium` / `high`。
- `user_visible_routing_card`: 入口卡片的可见形态，随 depth 缩放（见下）。

### Card Verbosity By Depth

入口卡片必须随 `depth_mode` 缩放，安静的入口也是聪明的入口：

- `quick_map`: 只出一行假设条，例如“按美股 / 方向性判断 / 截止今天来看，如不对请说”。
- `standard`: 出简短卡片：`primary_intent`、`market_scope`、`time_boundary`、关键假设、是否需要确认范围。
- `deep_dive`: 出完整卡片：含 `secondary_intents`、`execution_order` 和 `scope_confirmation_required`。

如果 `assumption_confidence = low` 或 `scope_confirmation_required = yes`，即使在 quick_map 也要把最关键的一条假设提到用户可见。

## Step 0.5: Decision Pressure Gate

用于识别 prompt 本身携带的决策压力和框架偏误，并在必要时强制一个 disconfirmation 动作。这是 Mira “证据不被偏好绑架” 身份的前端防线。

### Non-Diagnostic Rule

为了不违反 [../MIRA.md](../MIRA.md) 的 personalization 边界（不得存储对用户动机的推测）：

- 偏误标签锚定到**问题结构**，不是用户心理。不写“用户在死扛仓位”，而写“问题锚定在某个成本价 / 目标价上”。
- `decision_pressure` 和 `framing_risk` 是**每轮重算的瞬时路由信号，永不写入 preference memory 或 private state**。
- 这些字段不进入 Step 3.2 的 carryover 白名单。

### Trigger Rule (No Silent Skip)

触发绑定到确定性的 route，而不是对 prompt 的模糊感知（沿用 Step 4.5 “禁止静默跳过” 的同一纪律）：

- 凡是路由进入 actionability（能不能买 / 加 / 减 / 冲 / 抄底 / 目标价到了还能不能买 / 预期差兑现后能不能加）、position review、portfolio construction review，就**强制输出** `decision_pressure`，哪怕是 `none`。
- 裸 `预期差 / 预期差在哪` 是 variant-perception 研究问题，默认不进 actionability、`decision_pressure=none`；只有叠加动作语（能不能加 / 冲）或持仓语境时才触发本 gate。
- Step 0 若把 `interaction_mode` 标为 `decision_support`，本 gate 先给出初判，待 task_mode / research_object 确定 route 后再终判。
- 不允许因为“没看出压力”而静默跳过本 gate。

记录：

- `decision_pressure`: `none` / `low` / `medium` / `high`。
- `framing_risk`: `confirmation_seeking` / `fomo` / `anchoring` / `loss_aversion` / `position_defense` / `none`（描述问题结构，非用户心理）。
- `disconfirmation_required`: `yes` / `no`。

### Disconfirmation Move

当 `decision_pressure` 为 `medium` 或 `high`，或 `framing_risk` 非 `none` 时，`disconfirmation_required = yes`，输出必须包含一个反向检验：

- “如果你没有这个持仓 / 把问题反过来问，当前证据会得出什么？”
- 反向判断必须带一个 `reversal_condition`（什么证据会翻转它），即使完整的 `judgment_confidence` 阶梯尚未落地。
- 不得用 disconfirmation 把 research-only 输出诱导成交易指令；仍遵守 [../data/actionability-risk-control.md](../data/actionability-risk-control.md) 边界。

### Posture: research_only ↔ decision_support

Mira 的领域安全门——不给交易指令、无持仓不给仓位、instrument gate——不是各自独立的开关，而是同一个 posture 的子条款。这个 posture 由**既有的 `interaction_mode` 充当唯一开关**，不新增 `interaction_posture` 这种同义字段：

- `interaction_mode = decision_support` 即 decision_support posture：才进入 actionability / position / portfolio / instrument 分析框架，且**必经** decision pressure gate（[../schemas/routing.schema.json](../schemas/routing.schema.json) 已强制 `decision_support` → `decision_pressure`）和上面的范围确认。
- 其余 `interaction_mode`（`quick_answer` / `routed_research` / `routing_unclear`）即 research_only posture：默认禁止仓位大小、订单和交易指令输出。

各安全门的规则不变，仍以 [../MIRA.md](../MIRA.md)、[../data/actionability-risk-control.md](../data/actionability-risk-control.md)、[../data/instrument-strategy-gate.md](../data/instrument-strategy-gate.md) 为准；这里只是把它们统一挂到这一个开关下，让模型判断一个 posture 即可，而不必分别记住每个门的触发条件。

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

### `view_continuity`

用于普通问答观点、working view、用户私有 thesis、watchlist note 或“接着上次看”的延续和更新。

默认进入：

- `loops/view-continuity-loop.md`

触发条件：

- 用户要求保存、延续、更新、对比或复盘之前的观点。
- 本次回答形成了可复用但未达到正式 research package 的 working view。
- 用户观点、持仓、watchlist、偏好或私有 thesis 会影响当前边界。
- 输出需要说明 `save_as_working_view`、`private_state_action` 或 promotion / waiver。

边界：

- 用户私有观点默认写入 gitignored `private/`，不写入 tracked `memory/`。
- 只有用户明确要求贡献为 Mira 产品方法、公开样例或脱敏 case，才允许进入 tracked 文件。
- 没有来源或证据不足的观点只能保存为 `working_view`、`hypothesis` 或 `watch_item`，不能升级为正式 thesis。

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

## Step 3.1: Private State Boundary

在选择深度和输出包前，判断本次任务是否涉及用户私有状态。

默认规则：

- Mira 产品状态包括 tracked 的协议、loops、skills、templates、公开样例、默认方法论 memory 和 playbooks。
- 用户状态包括观点、working views、私有 thesis、watchlist、持仓、权重、风险预算、偏好和本地数据。
- 用户状态默认只读写 gitignored `private/` 或 `local/`。
- 不要把用户私有观点、持仓或 watchlist 写入 tracked `memory/`、`cases/` 或 `templates/`。

路由输出必须记录：

- `private_state_action`: `none` / `load` / `save_working_view` / `update` / `promote` / `waive`
- `private_state_refs`: 例如 `private/views/view-register.csv` 或 `private/research/<OBJECT>/working-view.md`
- `view_continuity_basis`: 为什么需要或不需要延续上次观点

动作规则：

- `none`: 纯方法论、公开资料解释、一次性事实查询，且没有可复用观点。
- `load`: 用户说“之前那个观点”“继续看”“更新 X”，或当前任务依赖既有私有 thesis。
- `save_working_view`: quick_map 或普通问答产生了可复用但未达到 durable thesis 的观点。
- `update`: 新证据会改变已有 private working view、expectation map 或 thesis state。
- `promote`: private working view 已满足 evidence、source trail、refresh condition 和 scope 要求，用户也明确希望升级。
- `waive`: 用户明确不要保存，或观点太弱、太临时、无来源，不应进入私有状态。

如果 `private_state_action` 不是 `none` 或 `waive`，先进入或并行使用：

- `loops/view-continuity-loop.md`

## Step 3.2: Sticky Context And Carryover

用于同一会话内的增量路由：哪些字段默认沿用，哪些在对象切换后必须重置。目标是既不反复追问，也不静默漂移。

### Boundary

- carryover 只在**同一会话内**有效。跨会话的观点延续必须走 [view-continuity-loop.md](view-continuity-loop.md) 或 private state，不得用 carryover 变成隐性长期记忆（见 [../MIRA.md](../MIRA.md) 的 private state 边界）。

记录：

- `routing_carryover`: `none` / `inherit` / `reset`。
- `carryover_fields`: 本轮实际沿用的字段。
- `context_reset_trigger`: 触发重置的条件。

### Carryover Whitelist

默认只允许沿用：

- `market_scope`
- `time_boundary`
- `research_object`（同一对象继续深入时）
- `depth_mode`（用户未改变要求时）
- `output_language`

显式排除（每轮重算，禁止沿用）：

- `decision_pressure`
- `framing_risk`
- `disconfirmation_required`
- 任何对用户动机的推测

### Reset Rules

- 研究对象 pivot（换公司 / 换产业 / 换资产）→ `routing_carryover = reset`，重新跑 Step 0–3。
- 时间边界或市场范围被用户改写 → 重置对应字段。
- 从 research-only 转入 actionability / position / portfolio → 不沿用旧结论强度，必须重新跑 Step 0.5 和相应 gate。

## Step 3.25: Depth Mode And Budget

在进入来源收集、quant gate 或模板输出前，先选择 `depth_mode`。目标是“不节约必要证据，也不浪费 token 在低增量模板字段上”。

### `quick_map`

用于：

- 用户说“看一下”“快看”“先判断方向”
- 研究对象或来源边界还不完整
- 目标是决定是否值得进入标准研究，而不是写 durable thesis

预算规则：

- `source_budget`: 只读最高增量来源，通常 3-6 个来源或已有 case 的最相关文件。
- `artifact_budget`: 输出 routing card、核心判断、source notes、source gaps 和 refresh triggers；不默认创建完整 research package。
- `token_budget_policy`: `concise`，先给一页可读结论，保留升级路径。
- quant 处理：可用 formula note 或明确 `calculation_gap`；不得把未复算数字写成高置信 durable conclusion。

### `standard`

用于：

- 首次覆盖、重建 thesis、正式 monitoring update、财报包或普通单票 research package
- 用户需要可追溯、可复核、能写入 case 的输出

预算规则：

- `source_budget`: 覆盖任务所需的 L1/L2/L5 和关键 L3/L4，不追求穷尽。
- `artifact_budget`: 输出 routed package 的必需文件；只生成被 route 或 gate 触发的附加 artifact。
- `token_budget_policy`: `balanced`，完整但避免重复贴模板字段。
- quant 处理：按 data-analysis-quality-gate 决定 formula note、calculation ledger 或 full model。

### `deep_dive`

用于：

- 用户明确要求深挖、专项拆解、方法验证、长期 thesis、多变量定价或外部复核质量
- 结论会进入 durable thesis、PM review、actionability bridge 或 methodology evidence

预算规则：

- `source_budget`: 允许多轮 source gap closure、peer checks、contrary evidence 和 cross-source validation。
- `artifact_budget`: 允许完整 package、calculation artifacts、expectation map、workflow scorecard 或专题 overlay 文件。
- `token_budget_policy`: `full`，但每个附加 artifact 必须说明增量用途。
- quant 处理：若数量判断影响 actionability，默认需要 calculation ledger 或明确降级。

### Upgrade / Downgrade Rules

- `quick_map -> standard`: 发现可行动 thesis、关键 source gap 可关闭、用户要求正式 package。
- `standard -> deep_dive`: 触发长期多变量 thesis、SEC 深拆、复杂 valuation、peer ranking、方法论验证或 PM 复核。
- `deep_dive -> standard`: 额外 lens / overlay 不能改变证据质量、结论强度或刷新条件。
- 不论深度如何，source quality、facts / inferences / judgments、refresh condition 和 downgrade rules 不能被省略。

## Step 3.27: Question Expansion Lens

在选定 `depth_mode` 之后、正式花 source / quant / artifact 预算之前，判断当前
问题是否需要一个轻量“问题变换”lens。目标是让 Mira 先把问题问科学，而不是
把错误粒度的问题直接送进重型 research loop。

只读：

- `data/question-expansion-lenses.md`

记录：

- `primary_question_lens`: `none` / `comparison_association` / `scale_shift` / `trend_dynamics` / `anomaly_detection`
- `selected_question_lenses`: 完整有序列表，包含 `primary_question_lens`，最多两个；`primary_question_lens = none` 时省略或留空
- `lens_selection_basis`: 为什么这个 lens 能改善当前 route
- `lens_data_required`: 需要什么比较组、时间序列、baseline、口径或 source
- `lens_failure_mode`: 如果缺少这些要求，最可能误导在哪里

选择规则：

- 默认 `primary_question_lens = none`。只有 lens 会改善 evidence path、
  falsification path、quant gate 或 progressive follow-up 时才触发。
- 最多选两个 lens；不要把四个 lens 全部套上。若多个 lens 都可用，优先选择
  能改变结论强度、readiness 或下一 route 的那一个。
- `question_lens` 只负责改写或锐化问题；单票路由里的 `selected_lenses`
  负责选择分析框架（如 variant perception），二者不互相替代。
- `comparison_association`: 问题需要“相对谁 / 与什么变量同动 / 是否有机制路径”。
- `scale_shift`: 问题粒度不对，需要由事件上升到 thesis，或由宏大主题下钻到
  可测变量。
- `trend_dynamics`: 当前值不够，需要看方向、一阶变化、二阶变化、持续性或拐点。
- `anomaly_detection`: 结论依赖“这是不是异常”，需要 baseline 和 materiality threshold。

边界规则：

- lens 不新增研究对象，不绕过 task_mode、source quality、private state 或
  actionability 边界。
- lens 默认在当前 route / depth 内锐化问题；如果它暴露出需要更大 scope 或
  更深 package，只能作为显式 upgrade path 或 progressive follow-up，不得静默扩展任务。
- 关联分析必须区分 correlation、mechanism 和 causality；没有机制路径时只能
  写 association，不得写因果。
- 趋势或异常驱动 durable conclusion 时，继续进入 Step 3.5 quant dependency。
- 缺少 comparator、baseline、时间序列或同口径数据时，输出必须降级为
  `source_gap`、`calculation_gap`、`working_view` 或 `needs_refresh`。
- `quick_map` 通常不展示 lens token，只把 lens 变成一句自然语言 source gap
  或 progressive follow-up。

## Step 3.3: Information Value And Knowability Gate

在选定 `depth_mode` 之后、进入来源收集和 quant gate 之前，校验这个问题是否值得当前深度、核心变量是否可知。`depth_mode` 管的是成本，本 gate 管的是“深挖会不会真的提高判断质量”。

它可以**反向下调 depth**：如果主导变量当前不可知，即使 prompt 看起来像 deep_dive，也应降级为更轻的输出 + 诚实的不确定性，而不是制造伪精确结论。

记录：

- `information_value`: `low` / `medium` / `high`——再多一轮研究会改变结论或决策的程度。
- `knowability_status`:
  - `knowable`: 关键变量可由现有来源或合理研究确定。
  - `partially_knowable`: 部分变量可知，核心仍有不可消除的不确定。
  - `unknowable_now`: 关键变量当前不可知，需等事件、披露或时间。
  - `irreducible_uncertainty`: 结论由本质不可知的变量主导，深挖不会提高质量。
- `depth_override_reason`: 若本 gate 改变了 Step 3.25 选定的 depth，说明原因。

规则：

- `information_value = low`，或 `knowability_status` 为 `unknowable_now` / `irreducible_uncertainty` 时，默认下调 depth，并在输出中显式说明“为什么深挖不会改变结论”。
- `irreducible_uncertainty` 是一个**诚实终态**：允许直接输出“这件事当前由不可知变量主导”，并配 `watch_only` / `needs_refresh` 和触发刷新的可观察条件，而不是强行给方向。
- 本 gate 不替代 source quality、facts/inferences/judgments 或刷新条件；它只防止过度研究。

## Step 3.35: Live Data Gate

当 prompt 依赖同日、盘中、最新价格、最新新闻或实时市场反应时，先运行：

- `data/live-data-source-policy.md`

触发词包括但不限于：`today`、`now`、`current`、`latest`、`premarket`、
`after-hours`、`今天`、`现在`、`目前`、`刚刚`、`盘中`、`是不是崩盘`、
`是不是调整`、`市场反应`。

记录：

- `live_data_gate`: `required` / `waived_definition` / `not_applicable`
- `freshness_status`: `live` / `delayed` / `stale` / `unavailable`
- `cross_check_status`: `passed` / `partial` / `failed`
- `quote_time`
- `publish_time`
- `source_boundary`
- `stale_after`
- `must_refresh_if`

规则：

- 时间敏感市场判断必须先搜索或读取 live-source；不能用模型记忆、旧 case note
  或未标注时间的数据回答。
- 对 `崩盘`、`panic`、`squeeze`、`breakout`、`sharp selloff` 这类强标签，
  默认需要两个独立市场数据源，或一个官方/交易所/指数源加明确 source
  boundary。
- 如果只拿到单一延迟聚合源，输出可以给 `quick_map`，但必须标记
  `freshness_status=delayed`、`cross_check_status=partial` 并降低 confidence。
- 新闻或 live blog 可解释 catalyst，但不能替代行情快照；先有
  market-pricing snapshot，再讨论原因。
- 如果问题只是稳定定义或方法论，例如“什么叫崩盘”，可以
  `live_data_gate=waived_definition`。

## Step 3.4: Data / Tool Ingestion Gate

如果本轮任务依赖新上传文件、用户本地材料、公开 API 输出、第三方授权数据、portfolio/risk export 或保留下来的派生数据集，先运行：

- `data/ingestion-layer.md`

本 gate 发生在 evidence logging 和 quant dependency 之前。工具返回值、网页抓取、API payload、用户文件和 vendor export 都只是 acquisition path，不是 evidence 本身。

记录：

- `ingestion_route`: `public_on_demand` / `user_material` / `authorized_provider` / `portfolio_private` / `derived_dataset` / `none`
- `ingestion_artifacts`: `dataset_manifest` / `user_material_intake` / `restricted_source_note` / `connector_registry` / `field_map` / `ingestion_log` / `waived`
- `source_registry_action`: `reuse` / `case_local_note` / `add_source` / `waive`
- `license_scope`
- `storage_scope`
- `evidence_log_mapping`
- `calculation_ledger_required`
- `ingestion_readiness_impact`

规则：

- 用户材料默认进入 `private/`，除非用户明确要求贡献为去标识化 product method 或 public example。
- 付费、保密、账户级、专家访谈或 vendor 原始数据只能记录合规 metadata 和简短 effect note；不得提交原文或原始数据 dump。
- 没有 date、permission、as-of 或 field coverage 的材料只能支持 discovery / working_view，不能支撑 durable conclusion。
- 如果 material 会驱动估值、peer ranking、event reaction、position/portfolio review 或 actionability，继续进入 Step 3.5 quant dependency。

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
- `calculation_depth`: `none` / `formula_note` / `ledger_required` / `full_model_required`
- `tool_consent_required`: `yes` / `no`

如果 `calculation_gate = required` 但用户选择不计算，或当前来源不足以计算，必须把相关结论降级为 `calculation_gap`、`source_gap`、`watch_only`、`needs_refresh` 或 `no_action`。

## Step 4: Handoff And Readiness

在进入具体 loop / skill 前，先判断当前任务是否会把结果交给另一个模块。

如果存在跨模块流转，按 [../data/handoff-contracts.md](../data/handoff-contracts.md)
记录：

- `handoff_type`
- `producer`
- `consumer`
- `required_artifacts`
- `evidence_log_refs`
- `calculation_refs`
- `readiness_level`
- `blocking_gaps`
- `must_refresh_if`

常见 handoff：

- `earnings_to_equity_research`
- `sec_to_research_package`
- `industry_to_single_equity`
- `macro_to_equity_overlay`

同时按 [../data/research-readiness-gate.md](../data/research-readiness-gate.md)
给任务当前输出预设 `readiness_level`。默认不要超过 `working_view`，除非来源、
计算、冲突和刷新条件都能支撑更高等级。

## Step 4.5: Progressive Follow-Up Prompts

progressive follow-up 是研究输出末尾的渐进式反问，用于帮助用户把一个松散问题升级为更科学、更可验证、更机构化的下一步任务。

它不是阻塞性澄清。默认先完成当前 route 能支持的回答，再给 1-3 个高杠杆反问。只有当研究对象、时间边界或数据权限完全不清楚，且继续分析会制造误导时，才把反问提前为 `routing_unclear`。

### Prompt Modes

至少记录：

- `followup_prompt_mode`: `none` / `light` / `standard` / `decision_grade`
- `followup_questions`
- `followup_basis`
- `next_route_if_answered`
- `followup_route_binding`
- `followup_object_anchor`
- `followup_decision_impact`

默认规则：

- `none`: 用户明确要求只要结论、机械更新、格式转换或已有下一步非常明确。必须同时写明 `followup_waiver_reason`；不能静默省略。
- `light`: quick_map、monitoring 小更新或用户只问“看一下”；输出 1 个反问。
- `standard`: 标准研究、产业 / 宏观 / 方法论任务、单票首次覆盖；输出 2-3 个反问。
- `decision_grade`: 任何接近 actionability、position review、portfolio construction、instrument strategy、PM handoff 或 durable thesis 的任务；输出 2-3 个反问，并明确回答后会进入哪个 loop / skill。

### Follow-Up Rungs

progressive follow-up 不是平铺 checklist。先判断当前答案已经爬到哪一层，
再问下一层最有增量的问题。

- `Rung A - boundary_or_data`: 补关键数据、来源权限、时间窗、市场范围、
  研究对象边界或缺失的一手材料。
- `Rung B - pricing_variable_or_consensus`: 暴露真正驱动结论的变量、共识代理、
  估值隐含预期、关键反事实或市场可能误判的位置。
- `Rung C - falsification_or_next_route`: 定义什么证据会翻转判断、降级 thesis、
  触发刷新、进入 actionability bridge、position review、portfolio review、
  quant gate、overlay 或下一个 loop / skill。

接力规则：

- `quick_map` 默认输出 1 个 light follow-up，可停在 Rung A；如果答案已经给出
  明确 source gap，则优先问 Rung B 或 C。
- `standard` / `deep_dive` 的 2-3 个 follow-up 不能全部停在 Rung A；至少 1 个
  必须进入 Rung B 或 Rung C。
- `decision_grade` 至少 1 个 follow-up 必须进入 Rung C，并说明回答后会改变
  `actionability_boundary`、`position_review_scope`、`readiness_level` 或下一个
  route。
- 每个 follow-up 必须引用当前答案里的具体对象、变量、证据缺口、判断或
  readiness 状态；不能只问通用偏好。
- 如果只能提出 Rung A 问题，说明当前对象或来源边界仍不足，并把结论保持在
  `working_view`、`source_gap`、`needs_refresh` 或等价降级状态。

### Final Gate

在交付前检查 progressive follow-up：

- 如果 `followup_prompt_mode` 是 `light`、`standard` 或 `decision_grade`，最终输出必须包含 1-3 个问题，且每个问题都有 `route_binding`、`object_anchor` 和 `decision_impact`，可以用简短自然语言表达。
- 如果 `followup_prompt_mode` 是 `standard` 或 `decision_grade`，最终输出必须
  体现 rung progression：不能全部是刷新、补数据或范围确认；至少一个问题要
  推进到定价变量 / 共识代理 / 证伪条件 / 下一 route。
- 如果最终输出没有任何 follow-up 问题，必须显式写 `followup_prompt_mode=none` 和 `followup_waiver_reason`。
- quick_map 默认不能用空白代替 follow-up；只有用户明确要求不要反问、任务是机械更新/格式转换、或下一步已经由用户命令唯一确定时，才允许 `none`。
- 如果交付时发现遗漏，应在发送前补 1 个最高杠杆、对象锚定的问题，而不是事后解释。

### Generation Gate

每个 progressive follow-up 必须按以下顺序生成。不要先写一个通用问题，再事后贴 route。

1. `rung-select`: 先选 Rung A / B / C。
   - 使用当前答案已经解决和未解决的内容决定下一层，不要把所有问题都停在
     Rung A 的卫生检查。
   - 如果当前答案已经指出 source gap，优先问能关闭共识代理、估值隐含预期、
     关键反事实或证伪条件的问题。
2. `route-bound`: 再从 routing 输出中选择问题类型。
   - 使用 `task_mode`、`research_object`、`time_boundary`、`depth_mode`、`primary_question_lens`、`selected_question_lenses`、`quant_dependency`、`readiness_level`、`selected_framework`、`selected_overlays` 和 `expected_handoffs`。
   - 问题必须能说明它会改变哪个 route 字段，或会触发哪个 loop / skill / gate。
3. `object-specific`: 再把问题内容锚定到当前研究对象。
   - 单票研究必须点名公司、ticker、主业务、当前定价变量、关键客户、主要产品、核心风险或估值锚中的至少一个。
   - 产业 / 宏观 / 商品 / 方法论研究必须点名主题变量、数据口径、市场范围或待验证机制。
   - position / portfolio review 必须点名持仓语境、组合约束、风险预算或 thesis conflict；没有真实持仓数据时必须保持 `research_only`。
4. `decision-impact explicit`: 最后说明用户回答后会改变什么。
   - 可选影响类型：`boundary`、`evidence_path`、`calculation_depth`、`readiness_level`、`thesis_state`、`actionability_boundary`、`position_review_scope`、`output_package`、`refresh_condition`。
   - 如果答案可能把输出从 `working_view` 升级到更高 readiness，必须同时说明还缺哪些来源、计算或持仓数据。

合格标准：

- 每个问题都必须同时有 `route_binding`、`object_anchor` 和 `decision_impact`。
- standard / deep_dive / decision_grade 的问题集合必须至少包含一个 Rung B 或
  Rung C；decision_grade 必须至少包含一个 Rung C。
- 如果无法做到 object-specific，说明当前来源或对象信息不足，并把问题降级为边界澄清。
- 如果问题只适用于任意股票、任意行业或任意组合，视为不合格。

### Question Design Rules

每个反问必须至少满足以下一个目的：

- 缩窄研究边界：明确时间窗口、市场范围、研究对象、输出深度或来源权限。
- 暴露隐含假设：指出结论真正依赖的变量、共识代理、估值隐含预期或关键反事实。
- 推动机构化决策框架：把问题连接到 watchlist、research package、thesis update、position review、portfolio review 或 actionability bridge。
- 明确可证伪条件：要求用户定义什么证据会改变判断、降级 thesis 或触发 refresh。
- 连接下一层证据路径：说明回答后会进入哪个 loop、skill、overlay、quant gate 或 handoff。
- 应用问题变换：通过对比 / 关联、尺度上移或下钻、趋势动态、异常基线，让下一步问题更可验证。

反问必须避免：

- 泛泛问“你还想了解什么？”
- 要求用户重复已经给出的信息。
- 在证据不足时用反问掩盖结论降级。
- 把 research-only 输出诱导成交易建议、订单或仓位大小结论。
- 一次给超过 3 个问题，除非用户明确要求设计完整 research questionnaire。
- 使用只适用于任何对象的通用问题，而没有对象锚点。
- 只写“下一步 route”，但不说明会改变哪类结论或 readiness。

### Route-Specific Prompt Patterns

以下只是问题类型，不是可直接照抄的最终问题。输出时必须用当前研究对象、市场变量和 route 结果改写成 object-specific 问题。

`first_pass_research`:

- 你希望这次覆盖服务于 watchlist、正式 thesis，还是后续 position review？
- 你更关心 1-2 个季度的 revision，还是 2-3 年的竞争格局和终局空间？
- 哪个变量如果被证伪，应该直接降级这个 thesis？

`monitoring_update`:

- 这次增量信息要更新 thesis state、expectation map，还是只放入 watchlist note？
- 你希望我只判断事件影响，还是同步检查原框架是否仍然有效？

`earnings_event`:

- 你更关心业绩是否超预期、指引是否改变 FY1/FY2，还是长期 thesis 是否被改写？
- 是否需要把财报 delta 转成 actionability bridge？如果需要，必须补时间窗口、持仓语境和失效条件。

`methodology_review`:

- 这个方法准备用于生成候选、验证 thesis，还是管理组合风险？
- 你接受它作为辅助 lens，还是需要达到能写入 methodology memory 的证据标准？

`industry_concept`:

- 你要的是产业图谱、可投资标的筛选，还是从主题落到单票 handoff？
- 这个主题真正要验证的是 TAM、渗透率、成本曲线、监管路径，还是竞争格局？

`macro_asset_or_regime`:

- 你要把宏观判断用于指数 / 资产配置，还是作为某类股票的 overlay？
- 哪个变量最可能推翻当前宏观 regime 判断：通胀、就业、利率、信用、美元还是流动性？

`position_review`:

- 这次 review 是检查 thesis 是否变了、仓位是否匹配 thesis，还是是否需要风险降级？
- 如果要讨论仓位动作，需要补持仓、权重、成本、风险预算、时间窗口和 mandate。

`portfolio_construction_review`:

- 你更想检查集中度、重复 bet、因子暴露、催化剂拥挤，还是 thesis stale risk？
- 哪些组合约束是硬约束：最大单票、行业上限、流动性、回撤、杠杆或现金比例？

### Output Shape

默认在输出末尾加入短节：

```md
## Progressive Follow-Up

1. [问题]
   - rung: `Rung A / Rung B / Rung C`
   - route_binding: `[routing_field / loop_or_skill / gate]`
   - object_anchor: `[company / product / customer / variable / position context]`
   - decision_impact: `[boundary / evidence_path / calculation_depth / readiness_level / actionability_boundary]`
2. [问题]
   - rung: `Rung A / Rung B / Rung C`
   - route_binding: `[routing_field / loop_or_skill / gate]`
   - object_anchor: `[company / product / customer / variable / position context]`
   - decision_impact: `[boundary / evidence_path / calculation_depth / readiness_level / actionability_boundary]`
```

如果当前输出非常短，可以压缩为一行：

```md
下一步最有用的问题：围绕 `[object_anchor]`，你更希望验证 `[route-bound choice]` 还是 `[route-bound choice]`？回答后会改变 `[decision_impact]`，并把 route 升级到 `[loop_or_skill]`。
```

## Step 5: Single-Equity Route

如果 `research_object = single_equity`，按以下顺序继续：

1. 运行 `market_scope_gate`
2. 运行 `thesis-horizon-routing`
3. 运行 `framework-routing`
4. 运行 `overlay-routing`
5. 判断是否使用 `variant-perception` 或 `long-term-multibagger` lens
6. 选择输出包和刷新条件

单票主框架只回答“当前主要由什么变量定价”，不回答任务是不是财报、产业、宏观或方法论。

### Market Scope Gate

`market_scope_gate` 用于防止把美股式公司 / 估值 / revision 框架无差别套到其他市场。

至少记录：

- `listing_market`
- `primary_trading_venue`
- `price_discovery_venue`
- `market_access`
- `dominant_investor_base`
- `policy_regulatory_sensitivity`
- `governance_or_controller_risk`
- `market_structure_overlay_default`

默认规则：

- A 股：必须先跑 `market-structure-policy` gate。若无明显触发，记录 `market_structure_weight: context`。
- 港股：必须先跑 `market-structure-policy` gate。若存在“便宜但不重估”、外资 / 南向 / 离岸风险溢价或治理折价问题，至少记录 `market_structure_weight: secondary`。
- A/H/ADR 多地上市：必须判断 `price_discovery_venue` 和多地估值差异是否改变结论。
- 美股、日股、韩股、台股、欧股：不默认升为 `secondary`，但若本地政策、交易制度、治理结构、指数 / 被动资金、货币流动性或外资可达性主导价格，应启用 `market-structure-policy`。

## Step 5: Overlays And Lenses

### Overlays

overlay 是额外证据路径，不替代主框架。

当前默认：

- `supply-chain`
- `macro`
- `market-structure-policy`
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

### Ingestion Artifacts

当新材料或新数据输入影响 formal output 时，按 [../data/ingestion-layer.md](../data/ingestion-layer.md) 附加或引用：

- `dataset-manifest.json`
- `user-material-intake.md`
- `restricted-source-note.md`
- `connector-registry.yaml`
- `field-map.yaml`
- `ingestion-log.csv`

当 `calculation_gate = required`，且结论包含派生数量判断时，必须按 gate 深度输出 formula note、`data-requirement-brief.md`、`calculation-ledger.csv` 或 full model；如果当前深度或来源不支持计算，显式写明 `calculation_gap` / `calculation_waived_by_speed` 和结论降级方式。

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
- 把 progressive follow-up 写成泛泛闲聊，而不是连接边界、证据、readiness 或下一层 route
- 静默遗漏 progressive follow-up，既没有 1-3 个 route-bound 问题，也没有 `followup_prompt_mode=none` 和 waiver reason
- 把复合 prompt 压扁成单任务，漏掉 `secondary_intents` 或不确认范围就花 depth 预算
- 在 actionability / position / portfolio 路由上静默跳过 decision pressure gate，不输出 `decision_pressure`
- 把瞬时偏误读数（`decision_pressure` / `framing_risk`）当成用户长期偏好存入 memory
- 跨会话误用 carryover，把会话内沿用变成隐性长期记忆，或对象 pivot 后不重置
- 在 `information_value=low` 或主导变量不可知时仍强行 deep_dive，制造伪精确结论
- 把判断当作无置信度的“语感”输出，缺 `judgment_confidence` 和 `reversal_condition`

## Stop Rules

- 如果研究对象不清楚，先输出 `routing_unclear`，只做定义澄清，不进入结论。
- 如果时间边界不清楚，默认按用户问题最近的显性时间词判断，并写 `horizon_uncertainty`。
- 如果来源不足以支撑 durable conclusion，只能输出低置信判断和刷新条件。
- 如果总路由与用户明确要求冲突，遵循用户要求，但记录 `routing_override`。
- 如果 progressive follow-up 的答案会改变核心结论等级，先把当前结论标成 preliminary / working_view，不要假装已经 decision-ready。
- 如果核心变量当前不可知，输出 `irreducible_uncertainty` 或 `unknowable_now` + 可观察刷新条件，不要用深挖掩盖不可知。
