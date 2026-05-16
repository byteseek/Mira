# Methodology Card: LLM Claim Classification

- status: trial
- role: llm-native-research-layer
- last_updated: 2026-05-16
- source_bucket: derived_internal + first_principles
- source_quality: internal_design
- credibility_score: provisional
- credibility_basis: Mira 已经要求 evidence log、fact vs inference 和 source quality；本方法把这些要求推进到 claim-level，适合由 LLM 执行初筛，再由研究者复核。
- search_coverage: not_started
- search_gaps: 需要后续用真实 research package、earnings package 和 monitoring case 验证分类是否稳定，尤其是公司口径、承诺、指引、长期目标、预测和假设的边界。
- comparison_baseline: source-level evidence logging
- empirical_validation_mode: live trial + case review
- follow_through_plan: 先在新研究包和财报分析包中试用，记录是否减少事实、观点、承诺、预测和假设混写。

## Core Idea

LLM 不只负责总结来源，而要把来源中的具体句子拆成 claim，并标注它们是事实、公司口径、承诺、指引、目标、预测、假设、观点、市场定价还是弱信号。

这个方法的核心是：

> source quality tells us who said it; claim classification tells us what kind of information it is.

## Reverse-Engineered From

- Mira 现有 `source-schema` 和 `source-policy` 对来源质量的要求。
- Mira 现有 research package 中 `fact vs inference` 的输出要求。
- 财报分析中反复出现的误差来源：把管理层解释、公司指引、sell-side consensus、市场反应和 Mira 倒推计算混写。
- LLM 擅长长文本抽取、句子级分类、结构化表格和一致性检查。

## Search Paths Used

当前为内部方法设计，尚未完成外部方法论搜索。

后续搜索路径：

- `claim extraction evidence classification investment research`
- `fact opinion distinction financial analysis`
- `management guidance vs long term target investment research`
- `LLM information extraction claim verification`
- `source credibility claim taxonomy research workflow`

## Use When

- 任意正式 research package、earnings package、industry package 或 monitoring update。
- 来源中同时包含事实、管理层说法、预测、目标、承诺和解释性判断。
- 研究对象依赖管理层兑现、订单、backlog、capex、指引、长期目标或市场预期差。
- 用户要求判断一条信息到底是事实、观点、承诺、预测还是假设。

## Avoid When

- 只有极少量明确事实，分类成本高于收益。
- 没有原始来源，只剩二手转述，无法可靠拆 claim。
- 研究只是在做临时方向感扫描，不进入正式 memory 或 research package。

## Applies To

- `research-loop`
  在 `collect` 后、`scan` 前运行，避免初判被未分类信息污染。
- `monitoring-loop`
  对新增信息做 diff，判断新 claim 是验证、削弱、替代旧 claim，还是噪音。
- `earnings-report-analysis`
  区分财务事实、管理层解释、正式指引、长期目标、consensus、Mira implied bridge。
- `methodology-research-loop`
  区分方法事实、作者观点、事后解释、真实可复用流程。

## Core Question

这条被用来支撑研究判断的信息，本质上是什么，是否足以支撑它被用到的结论？

## Required Inputs

- 原始来源或可追溯二手来源
- source record
- 要被用于研究判断的具体句子、指标或表述
- claim taxonomy
- 研究输出中该 claim 的使用位置

## Primary Signal

- 高权重结论是否由高权重 claim 支撑
- 关键假设是否仍被标记为假设
- 公司口径是否被误写成事实
- 指引、目标、承诺和预测是否被混淆
- 市场定价是否被误写成基本面验证

## Why It Works

投资研究错误常来自信息性质混淆，而不只是来源不够多。

LLM 在这里的优势不是预测能力，而是：

- 快速从长文本中抽取 claim
- 对 claim 做一致分类
- 发现同一段文字里的事实和观点混写
- 在监控时比较旧 claim 与新 claim 的状态变化
- 强制 memo 保留事实、推断、判断和假设之间的边界

## Failure Mode

- 分类看起来精细，但没有改变最终 memo 的证据纪律。
- LLM 把语气强的观点误判为事实。
- 研究者没有复核，导致分类错误被系统性放大。
- 过度分类低价值信息，增加流程负担。
- `claim_type` 被机械填写，实际结论仍然混写。

## Evidence Cost

low to medium

对已有来源做 claim 分类成本较低，但要做好需要读原文、保留上下文并复核边界。

## Speed Vs Depth

- `speed`
  对新来源快速标注事实、公司口径、指引、预测和观点。
- `depth`
  对核心 memo 结论逐条回溯 claim，检查是否有结论越权。

## Comparison To Existing Methods

相对 source-level evidence log：

- 旧方法说明来源是谁、可信度如何。
- 新方法说明被使用的信息本质上是什么。

相对 `fact vs inference`：

- `fact vs inference` 是输出层检查。
- `llm-claim-classification` 是输入层和 evidence log 层约束。

## Follow-Through Criteria

- 是否减少把管理层说法写成事实。
- 是否减少把预测、假设和长期目标写成结论。
- 是否让 `must_refresh_if` 更具体。
- 是否帮助 monitoring 判断旧 thesis 的关键 claim 是否被验证或证伪。
- 是否能在不显著拖慢研究速度的情况下提高 memo 质量。

## Trial Design

先在三类 case 试用：

- earnings case
  区分财务事实、管理层解释、guidance、consensus 和 Mira 倒推。
- standard equity research package
  检查核心结论是否由高权重 claim 支撑。
- monitoring update
  判断新增信息改变旧 claim 的哪一部分。

## Falsification Conditions

- 如果分类不能改变 memo 的证据质量，只是增加表格字段，应降级。
- 如果研究者经常需要大量返工修正 LLM 分类，说明 taxonomy 需要简化。
- 如果 claim 分类无法改善 refresh trigger 和 falsification condition，不升级到 `adopted`。

## Adoption Decision

当前判断：`trial`

原因：

- 与 Mira 的 evidence log、source schema、research loop 和 monitoring loop 高度兼容。
- LLM 执行优势明确。
- 但仍需要真实案例验证分类粒度是否合适，以及是否会增加过多流程成本。
