# Methodology Card: Industry Concept Analysis

- status: trial
- role: standalone-skill
- last_updated: 2026-05-09
- source_bucket: practitioner + institutional + first-principles
- source_quality: mixed
- credibility_score: provisional
- credibility_basis: 由现有 `framework-routing` 和 `supply-chain` overlay 扩展而来，尚需用 GPU / ABF / HBM / 存储等真实案例验证。
- search_coverage: not_started
- search_gaps: 需要后续通过产业深度报告、公司披露、行业协会、技术标准和财报电话会验证写法。
- comparison_baseline: 单票 research package + supply-chain overlay
- empirical_validation_mode: 用 2-3 个热门概念生成产业包，再检查是否能更快收敛到关键环节和候选标的。
- follow_through_plan: 先进入 `trial`，形成案例后再决定是否升级到 `adopted`。

## Core Idea

把一个模糊产业概念拆成概念边界、产业链位置、需求拉动、供给瓶颈、定价机制、放量机制、利润池和可投标的映射。

## Use When

- 先研究概念，再决定研究哪些公司。
- 市场叙事围绕技术、材料、设备、零部件或产业链瓶颈展开。
- 用户需要快速理解某个概念在产业链里到底卡在哪里。

## Avoid When

- 用户已经明确指定单一公司并只需要单票结论。
- 概念过宽，无法在一次研究中形成可验证产业边界。
- 缺少任何可追溯来源，只剩情绪或传闻。

## Core Question

这个概念对应的产业链中，哪一层真正拥有定价权、放量确定性和利润留存能力，哪些上市公司是最好的研究代理。

## Required Inputs

- concept_name
- research_question
- market_scope
- research_cutoff_date
- thesis_horizon
- depth
- focus

## Primary Signal

环节层面的供需紧张度、定价权、放量可见度、利润留存和股票代理质量。

## Why It Works

产业概念容易被市场叙事压扁成单一标签。把概念拆回产业链和商业机制，可以区分：

- 概念正确但股票代理很差
- 需求增长但利润池不在该公司
- 放量确定但价格被压
- 短期紧缺但长期供给扩张过快
- 龙头有优势但估值已透支

## Failure Mode

- 只画产业链，不排序利润池和瓶颈。
- 把券商产业图谱当作事实结论。
- 把高增长赛道等同于高收益股票。
- 没有区分定价权和放量能力。
- 忽略客户认证、良率、设备交期、库存和 capex 周期。

## Evidence Cost

中等到高。quick map 可以先用公开材料，但正式结论需要公司披露、行业来源、专业研究和市场数据交叉验证。

## Speed Vs Depth

- `quick_map`: 适合建立概念边界和候选公司池。
- `standard`: 适合形成可用产业包和跟踪指标。
- `deep_dive`: 适合进入单票研究、估值和交易计划之前。

## Comparison To Existing Methods

相比 `supply-chain` overlay，它不是从某家公司出发沿上下游验证，而是从产业概念出发建立完整地图，再筛选值得进入 `equity-research-core` 的公司。

## Trial Design

优先选择：

- `GPU`
- `ABF`
- `HBM`
- `存储`

每个案例检查：

- 是否能在 30-60 分钟内形成清晰产业链地图
- 是否能明确 3-5 个关键环节
- 是否能筛出 5-10 个候选公司并说明暴露度
- 是否能给出供需、定价和放量监控指标

## Falsification Conditions

如果生成的产业包不能比普通搜索更快定位关键瓶颈、利润池和标的候选，或核心判断无法回溯到来源，则不升级到 `adopted`。

## Adoption Decision

pending
