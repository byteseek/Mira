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

判断该标的当前的 `pricing regime`，选择研究框架，并记录：

- `selected_framework`
- `framework_basis`
- `why_not_other_framework`

### `select-overlays`

判断是否需要专题 `overlay`，并记录：

- `selected_overlays`
- `overlay_basis`
- `expected_incremental_insight`

### `collect`

按选定框架和已选 overlay 收集并登记首版研究需要的来源。

如果处于 `industry-concept` 分支，来源至少覆盖公司披露/IR、行业或官方材料、专业研究和市场数据，不能只依赖主题文章或二手产业图。

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

### `package`

输出首版 `research package`：

- `investment memo`
- `evidence log`
- `case notes`

并显式写入：

- `selected_framework`
- `framework_basis`
- `framework_mismatch_risk`
- `selected_overlays`
- `overlay_basis`

如果处于 `industry-concept` 分支，则输出 `industry-analysis-package`：

- `industry-map.md`
- `company-map.csv`
- `evidence-log.csv`

### `write-memory`

把首版研究中相对稳定的内容沉淀到 `memory/`。

## Exit Criteria

- 核心结论已有足够来源支撑
- `research package` 已生成
- 事实与推断已分离
- 已写出后续刷新条件
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
