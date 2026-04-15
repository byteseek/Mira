# Research Loop

`research-loop` 是这个仓库中一次股票研究任务的最小执行循环。

它不是自动化抓取流程，也不是多 agent 编排系统，而是单一 `research-orchestrator` 在一次研究中应遵循的标准工作方式。

## 1. Loop Input

每次进入 loop，至少要明确以下输入：

- `company_name`
- `ticker`
- `market`
- `research_question`
- `research_cutoff_date`
- `thesis_horizon`

可选输入：

- `focus`
  例如：基本面、财务、技术面、事件面
- `known_sources`
  用户已提供的材料或链接
- `refresh_reason`
  如果这不是首次研究，说明为什么重新进入 loop

## 2. Loop States

### `define`

明确研究问题、时效边界和本轮目标。

输出：

- 当前研究问题
- 研究截止时间
- 预期研究包范围

### `collect`

收集来源并登记 metadata。

输出：

- 候选来源列表
- 已确认来源列表
- 缺失来源或低质量来源提示

### `scan`

基于当前来源做首轮快速研究，覆盖以下视角中的至少三个：

- business and industry
- financial quality
- technical context
- events and sentiment

输出：

- 四视角初判
- 事实清单
- 初步推断

### `gap-check`

识别缺口、冲突和弱证据结论。

输出：

- 证据缺口
- 冲突结论
- 需要补充的来源类型

### `refine`

补充来源并修正判断。

输出：

- 修正后的判断
- 被降级的结论
- 已关闭和未关闭的证据缺口

### `package`

生成统一研究包。

输出：

- `investment-memo.md`
- `evidence-log.csv`
- `case-notes.md`

### `refresh`

当触发条件出现时，重新进入 loop，但不是从零开始，而是基于已有 case 更新。

## 3. Loop Memory

`research-loop` 只保留两层记忆，不做更复杂的长期记忆系统。

### Task Memory

只属于当前这一轮 loop：

- 当前研究问题
- 已看过的来源
- 当前初判与证据缺口
- 当前迭代次数

这层记忆在本轮结束后可以丢弃，不作为长期事实存储。

### Case Memory

属于该标的案例，可以跨多轮复用：

- 上一版 `investment memo`
- 上一版 `evidence log`
- 长期跟踪指标
- 历史核心分歧点
- 历史证伪点和刷新触发条件

### Memory Rules

- 事实不能因为重复出现就自动升级可信度，仍以来源等级为准。
- 推断不能直接写入长期事实。
- 新闻与舆情默认只作为短期 case memory，不自动沉淀为长期结论。
- 没有日期的信息不能进入 case memory 的正式结论区。

## 4. Loop Exit Criteria

满足以下条件时，当前 loop 可以结束：

- 核心结论已有足够来源支撑
- `investment memo`、`evidence log`、`case notes` 已生成
- 事实与推断已明确分离
- 时效字段完整
- 主要风险与跟踪指标已写清

## 5. Loop Stop Rules

为了避免无休止迭代，MVP 默认：

- `max_iterations = 3`
- 如果关键结论只能依赖 `L4` 或 `L6`，则降级结论，不继续脑补
- 如果关键来源缺失且无法补齐，允许输出“证据不足”的 memo

## 6. Loop Refresh Triggers

以下情况会触发重新进入 `research-loop`：

- 新财报、年报或正式指引发布
- 重大产品延期、上线或取消
- 并购、回购、分红等资本配置动作显著变化
- 价格突破关键技术位
- 关税、监管、政策出现重大变化
- 用户主动要求重跑案例

## 7. MVP Intention

MVP 的 `research-loop` 追求的是：

- 让研究过程稳定可重复
- 让来源、时效、结论保持一致
- 让 agent 不因上下文过长而失控

它不追求：

- 自动抓取所有数据
- 无限迭代直到“完美结论”
- 一次性替代专业研究团队的全部流程

