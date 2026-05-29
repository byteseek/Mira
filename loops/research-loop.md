# Research Loop

`research-loop` 用于建立一个研究主题的初始认知和首版研究包。

它服务于“首次覆盖”或“需要重建 thesis”的场景，不负责每日更新。

## Loop Input

- `theme`
- `research_question`
- `market_scope`
- `research_cutoff_date`
- `thesis_horizon`
- `framework_hint`
  可选
- `overlay_hint`
  可选
- `concept_mode`
  可选；当主题是产业、技术、材料、设备、工艺或供应链概念时设为 `true`
- `known_sources`
  可选

## States

### `define`

明确主题、问题、时间边界和首版输出目标。

### `route-analysis`

先运行 `analysis-routing`，明确：

- `task_mode`
- `research_object`
- `market_scope`
- `time_boundary`
- `primary_skill_or_loop`
- `routing_basis`
- `routing_mismatch_risk`
- `expected_output_package`

如果总路由显示任务应进入 `earnings_event`、`monitoring_update`、`methodology_review`、`macro_asset_or_regime` 或 `etf_or_product_listing`，不要继续强行走普通单票 research loop。

如果主题是 `存储`、`CPU`、`GPU`、`ABF`、`HBM`、`CPO`、`液冷`、`先进封装` 这类产业概念，先进入 `industry-concept` 分支。

### `industry-concept`

当 `concept_mode = true` 时，运行 `industry-concept-analysis`，并先输出：

- `one_page_industry_map`
- `concept_boundary`
- `value_chain_map`
- `demand_map`
- `supply_map`
- `pricing_mechanics`
- `volume_mechanics`
- `tightness_and_profit_pool_ranking`
- `company_shortlist`
- `stock_research_handoff`

完成后再决定是否对 shortlist 里的公司进入 `route-framework` 和 `equity-research-core`。

### `route-framework`

仅当 `research_object = single_equity` 时进入本步骤。

先判断研究结论的 `thesis_horizon`，再判断该标的当前的 `pricing regime`，选择研究框架，并记录：

- `horizon_bucket`
- `horizon_basis`
- `horizon_mismatch_risk`

- `selected_framework`
- `framework_basis`
- `secondary_regime`
- `why_not_other_framework`

### `select-overlays`

判断是否需要专题 `overlay`，并记录：

- `selected_overlays`
- `overlay_basis`
- `expected_incremental_insight`

如果研究问题本质是预期差，还要判断是否启用 `variant-perception` lens，并记录：

- `selected_lenses`
- `lens_basis`
- `what_it_forces_us_to_check`

### `collect`

按选定框架和已选 overlay 收集并登记首版研究需要的来源。

如果处于 `industry-concept` 分支，来源至少覆盖公司披露/IR、行业或官方材料、专业研究和市场数据，不能只依赖主题文章或二手产业图。

### `classify-claims`

把已收集来源中会被用于研究结论的具体信息拆成 claim，并按 [../data/claim-taxonomy.md](../data/claim-taxonomy.md) 标注：

- `claim_type`
- `claim_text`
- `source_speaker`
- `verification_status`
- `as_of_date`
- `confidence`

必须特别区分：

- 事实 vs 观点
- 承诺 vs 预测
- 指引 vs 长期目标
- 假设 vs 结论
- 弱信号 vs 可用证据
- 价格反应 vs 基本面验证

### `scan`

从公司、财务、技术面、事件四个统一视角快速建立初判，但要按已选框架调整权重，并用 overlay 补充验证关键传导链。

如果处于 `industry-concept` 分支，scan 的重点改为：

- 一页版结论是否足够清楚，可以先读后查
- 概念边界是否清楚
- 上下游公司是否分层
- 定价和放量机制是否分开
- 紧供需和利润池是否排序
- 候选标的是否能交接给单票研究

如果研究对象适合做预期差分析，允许在这里插入 `variant perception checklist`，用于把初判转成：

- `consensus proxy`
- `what is mispriced`
- `why market may be wrong`
- `what changes the price`
- `what falsifies the view`

如果研究对象适合做长期 10x / 100x / multibagger 分析，允许在这里插入 `long-term-multibagger checklist`，用于把初判转成：

- `target_return_path`
- `return_path_math`
- `market_expansion`
- `right_to_win`
- `reinvestment_runway`
- `dilution_risk`
- `evidence_ladder`
- `kill_criteria`

如果研究对象需要进入持续跟踪、用户关心可执行性，或 key debate 涉及估值是否已 price in，必须插入 `valuation-expectation overlay`，用于把初判转成：

- `current_valuation`
- `what_is_priced_in`
- `base_bull_bear`
- `revision_path`
- `downside_path`
- `valuation_anchor_quality`

### `gap-check`

识别缺口、冲突、低可信结论，以及框架错配风险。

如果使用了 `variant perception checklist`，这里还要额外检查：

- 共识是不是被清晰刻画
- 分歧是不是具体到变量层
- 是否只是“想和市场不同”而不是有可验证 edge

### `refine`

补足关键来源，修正判断。

如果 `variant perception` 仍停留在概念层，必须继续补：

- 共识代理
- 证据链
- 失效条件

如果 `long-term-multibagger` 仍停留在故事层，必须继续补：

- 目标倍数、年限和隐含 CAGR
- 收入、利润、现金流和估值结果要求
- 生存性和稀释风险
- 证据阶梯
- kill criteria

如果 `valuation-expectation` 无法给出 valuation anchor 或 base/bull/bear，必须标记 `source_gap`，并把 `actionability_bridge` 降级为 `watch_only` 或 `no_action`。

### `package`

输出首版 `research package`：

- `investment memo`
- `evidence log`
- `case notes`

并显式写入：

- `task_mode`
- `research_object`
- `routing_basis`
- `routing_mismatch_risk`
- `horizon_bucket`
- `horizon_basis`
- `horizon_mismatch_risk`
- `selected_framework`
- `framework_basis`
- `framework_mismatch_risk`
- `selected_overlays`
- `overlay_basis`
- `selected_lenses`
- `lens_basis`

如果处于 `industry-concept` 分支，则输出 `industry-analysis-package`：

- `industry-map.md`
- `company-map.csv`
- `evidence-log.csv`

### `write-thesis-ledger`

如果研究结论已经足够稳定，写入或更新 Thesis System 对象：

- `thesis-ledger.md`
- `expectation-map.csv`
- `decision-log.csv`，如需要记录研究动作

写入前必须检查：

- 核心 thesis 是否能回溯到 evidence log 或 explicit source note
- supporting claims 是否区分事实、指引、预测、假设、公司口径、市场定价和情绪
- expectation map 是否有真实 consensus proxy；没有则标记 `source_gap`
- thesis state 是否为 `draft`、`active`、`watch`、`upgrade_watch`、`downgrade_watch`、`stale` 或 `retired`
- `stale_after` 和 `must_refresh_if` 是否完整

### `write-memory`

把首版研究中相对稳定的内容沉淀到 `memory/`。

## Exit Criteria

- 核心结论已有足够来源支撑
- `research package` 已生成
- 若结论进入持续跟踪，`thesis-ledger` 与 `expectation-map` 已生成或明确 waived
- 若结论进入行动跟踪，`valuation_and_expectation_quant` 与 `actionability_bridge` 已生成或明确 waived
- 事实、公司口径、承诺、指引、预测、假设、观点和市场定价已分离
- 已写出后续刷新条件
- 已完成总分析路由并说明为什么进入当前 loop / skill
- 已完成框架选择并说明适配原因
- 如启用 overlay，已写明其增量价值
- 如果是产业概念研究，已完成概念边界、产业链地图、供需/定价/放量机制、利润池排序和单票研究交接
- 如果是产业概念研究，报告最前面已给出可快速阅读的 `one_page_industry_map`

## Stop Rules

- `max_iterations = 3`
- 如果关键问题只能依赖 `L4/L6`，降级结论
- 如果关键来源缺失，允许输出“证据不足”
- 如果无法稳定判断框架，允许输出“框架暂定”，但必须写明歧义来源
- 如果 overlay 只能增加噪音而不能提升判断，允许显式不启用
