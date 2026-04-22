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
- `known_sources`
  可选

## States

### `define`

明确主题、问题、时间边界和首版输出目标。

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

### `scan`

从公司、财务、技术面、事件四个统一视角快速建立初判，但要按已选框架调整权重，并用 overlay 补充验证关键传导链。

### `gap-check`

识别缺口、冲突、低可信结论，以及框架错配风险。

### `refine`

补足关键来源，修正判断。

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

### `write-memory`

把首版研究中相对稳定的内容沉淀到 `memory/`。

## Exit Criteria

- 核心结论已有足够来源支撑
- `research package` 已生成
- 事实与推断已分离
- 已写出后续刷新条件
- 已完成框架选择并说明适配原因
- 如启用 overlay，已写明其增量价值

## Stop Rules

- `max_iterations = 3`
- 如果关键问题只能依赖 `L4/L6`，降级结论
- 如果关键来源缺失，允许输出“证据不足”
- 如果无法稳定判断框架，允许输出“框架暂定”，但必须写明歧义来源
- 如果 overlay 只能增加噪音而不能提升判断，允许显式不启用
