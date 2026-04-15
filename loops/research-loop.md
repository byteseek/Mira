# Research Loop

`research-loop` 用于建立一个研究主题的初始认知和首版研究包。

它服务于“首次覆盖”或“需要重建 thesis”的场景，不负责每日更新。

## Loop Input

- `theme`
- `research_question`
- `market_scope`
- `research_cutoff_date`
- `thesis_horizon`
- `known_sources`
  可选

## States

### `define`

明确主题、问题、时间边界和首版输出目标。

### `collect`

收集并登记首版研究需要的来源。

### `scan`

从公司、财务、技术面、事件四个视角快速建立初判。

### `gap-check`

识别缺口、冲突和低可信结论。

### `refine`

补足关键来源，修正判断。

### `package`

输出首版 `research package`：

- `investment memo`
- `evidence log`
- `case notes`

### `write-memory`

把首版研究中相对稳定的内容沉淀到 `memory/`。

## Exit Criteria

- 核心结论已有足够来源支撑
- `research package` 已生成
- 事实与推断已分离
- 已写出后续刷新条件

## Stop Rules

- `max_iterations = 3`
- 如果关键问题只能依赖 `L4/L6`，降级结论
- 如果关键来源缺失，允许输出“证据不足”

