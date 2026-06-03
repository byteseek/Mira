# Equity Research Core Skill

这是当前主 research skill，用于在单次研究中统一处理：

- 基本面
- 财务质量
- 宏观经济与金融条件
- 技术面节奏
- 事件与舆情

它不是多个独立 skill 的简单拼接，而是一个面向 `research package` 的主 skill。

这个 skill 现在采用：

- 一个统一输出骨架
- 一个 upstream analysis router
- 一个 thesis horizon router
- 一个 framework router
- 一个 overlay selector
- 多个可切换研究框架

也就是说，输出仍然统一，但研究顺序、证据权重和结论重心会随时间跨度和标的的定价主导变量变化。

在主框架之外，还允许叠加专题 `overlay`，用于补充特定研究路径。

## Upstream Analysis Routing

进入本 skill 前，应先通过总路由确认任务确实是 `single_equity`。

总路由见：

- [../../loops/analysis-routing.md](../../loops/analysis-routing.md)

如果任务本质是财报事件、产业概念、宏观 regime、ETF 产品或方法论研究，应优先进入对应 loop / skill，再决定是否 handoff 到单票研究。

## Use When

- 需要对单一股票做首次覆盖或阶段性复核
- 需要把多源数据整理成一个可追溯的研究包
- 需要在同一份输出里同时包含公司、财务、宏观、价格、事件等视角
- 需要根据标的特征切换研究框架，而不是默认用同一套分析权重
- 需要区分财报/短中期执行判断和一年以上的长期公司或产业 thesis
- 已通过 `industry-concept-analysis` 识别出某个产业概念中的候选标的，需要进入单票研究

## Required Inputs

- company_name
- ticker
- market
- research_question
- research_cutoff_date
- thesis_horizon
- `depth_mode`
  可选；默认由 `analysis-routing` 推断
- `framework_hint`
  可选，用户已有明确框架偏好时使用
- `overlay_hint`
  可选，用户已有明确研究视角时使用

## Thesis Horizon Routing

在正式分析前，必须先完成 `thesis horizon selection`。

默认不要把最新财报、未来几个季度盈利修正和长期产业趋势写成同一种结论。先判断：

- `thesis_horizon`
- `horizon_bucket`
- `horizon_basis`
- `horizon_mismatch_risk`

时间跨度选择规则见：

- [references/thesis-horizon-routing.md](references/thesis-horizon-routing.md)

当前默认支持四种 horizon bucket：

- `near_term_execution`
- `medium_term_revision`
- `long_term_thesis`
- `regime_transition`

## Framework Routing

完成 `thesis horizon selection` 后，必须继续完成 `framework selection`。

默认不要只按市值机械分类，而要优先判断：

- `market_cap_bucket`
- `liquidity_and_float`
- `ownership_structure`
- `business_maturity`
- `catalyst_type`
- `valuation_anchor_usefulness`

框架选择规则见：

- [references/framework-routing.md](references/framework-routing.md)

当前默认支持三个主框架：

- [micro-small](references/micro-small.md)
- [mid-cap](references/mid-cap.md)
- [large-mega](references/large-mega.md)

如果标的存在明显混合特征，允许声明：

- 主框架
- 次要干扰变量
- 为什么不采用另一个看起来相近的框架

## Overlay Selection

完成主框架选择后，可以继续判断是否需要专题 `overlay`。

overlay 不改变主框架，只补充一条高价值研究路径。

当前可用 overlay 以 [references/overlay-routing.md](references/overlay-routing.md) 为单一来源，常用包括：

- [supply-chain-overlay](references/supply-chain-overlay.md)
- [macro-overlay](references/macro-overlay.md)
- [commodity-overlay](references/commodity-overlay.md)
- [strategic-catalyst-overlay](references/strategic-catalyst-overlay.md)
- [valuation-expectation-overlay](references/valuation-expectation-overlay.md)
- `flow-intent-inference` in [references/overlay-routing.md](references/overlay-routing.md)
- `options-flow-analysis` in [references/overlay-routing.md](references/overlay-routing.md)

overlay 选择规则见：

- [references/overlay-routing.md](references/overlay-routing.md)

`supply-chain` overlay 适用于以下问题：

- 上下游传导是否决定盈利弹性
- 客户集中度是否决定收入确定性
- 哪一层供应链更受益或更受损
- 同层级可比公司对照能否帮助验证叙事

`macro` overlay 适用于以下问题：

- 增长、通胀、政策、利率、美元、信用、流动性或风险偏好是否主导当前定价
- 市场已经 price in 的宏观路径是什么
- 宏观变量通过哪条链影响收入、利润率、估值、融资、仓位或催化剂
- 新数据或政策口径是否会改变 thesis

`strategic-catalyst` overlay 适用于以下问题：

- 巨头合作、投资、并购、客户认证、独家授权、平台接入或供应链导入是否会重写小盘股预期
- 社交传闻、行业聊天、异常量价或非正式线索是否值得纳入 alpha signal 监控
- 线索应如何区分为 `confirmed`、`reported`、`social_signal` 或 `unverified_rumor`
- 下一步确认或证伪路径是什么

## Required Source Types

- `L1` 公司披露或官方材料
- `L5` 市场数据
- `L4` 事件/新闻材料可选但建议使用
- 如果启用 `macro` overlay，至少补充官方宏观数据、政策材料或市场定价数据中的两类
- 如果启用 `strategic-catalyst` overlay，允许使用 `social_and_community` 作为 alpha signal，但必须降级标记并写入验证路径

## SEC Filing Boundary

单票研究默认把 SEC 作为事实底座和冲突校验，走 `sec_supplement`：

- 查 CIK、最新 filing timeline、10-K/10-Q/8-K/proxy 是否覆盖研究 cutoff。
- 抽取 thesis-critical 指标，例如 cash flow、debt、share count、SBC、inventory、RPO/backlog、segment、customer concentration 或 risk-factor facts。
- 在 `evidence-log.csv`、financial snapshot 或 case notes 中记录 SEC provenance。

只有在以下情况升级为 `sec_filing_deep_dive`：

- 用户明确要求拆 SEC 文件。
- 核心 thesis 依赖 accounting quality、risk factor delta、debt/liquidity、related-party、ownership/control、dilution 或 segment 细节。
- filing 与 release、management commentary、market-data page 或 prior Mira case 冲突。
- 缺失 filing 阻断 actionability，需要 source-gap refresh 后再复核。

## Output Package

这个 skill 默认输出统一的 `research package`，但受 `depth_mode` 约束：

- `quick_map`: 可以只输出 routing card、core judgment、source notes、source gaps、refresh triggers 和升级条件；不默认写完整 case artifacts。
- `standard`: 输出完整 `research package`。
- `deep_dive`: 在完整 package 外，按 gate 触发 expectation map、calculation artifacts、workflow scorecard 或专题 overlay 文件。

标准 `research package` 包括：

- `investment-memo.md`
- `evidence-log.csv`
- `case-notes.md`

研究包里必须显式写明：

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
- `readiness_level`
- `readiness_basis`
- `blocking_gaps`
- `evidence_log_status`
- `quant_gate_status`

新的 `evidence-log.csv` 应使用 [../../data/evidence-posture-taxonomy.md](../../data/evidence-posture-taxonomy.md)
中的 evidence posture 字段。不要因为来源层级高就自动把 claim 升级成
`verified_fact`；必须匹配 claim、期间、口径、单位和当前研究用途。

研究包还应包含或更新 `research-package-manifest.json`，用于记录 hero artifacts、
support artifacts、readiness、handoffs、source scope、quant gate 和 refresh
条件。

如果研究问题明显属于“预期差判断”，建议额外使用：

- [../../templates/variant-perception-checklist.md](../../templates/variant-perception-checklist.md)

这个 checklist 不替代 memo，只用于把 thesis 压缩成：

- `consensus proxy`
- `what is mispriced`
- `why market may be wrong`
- `what changes the price`
- `what falsifies the view`

如果研究问题明显属于“长期 10x / 100x / multibagger 候选”，建议额外使用：

- [../../templates/long-term-multibagger-checklist.md](../../templates/long-term-multibagger-checklist.md)

这个 checklist 不替代 memo，只用于把长期 thesis 压缩成：

- `target_return_path`
- `return_path_math`
- `market_expansion`
- `right_to_win`
- `reinvestment_runway`
- `dilution_risk`
- `evidence_ladder`
- `kill_criteria`

## Required Sections In Case Notes

- business and industry
- financial quality
- macro and financial conditions
- technical context
- events and sentiment
- overlays
- fact vs inference
- claim classification notes

## Boundaries

- 它只定义研究组织方式，不承诺自动抓取。
- 它不把每个框架拆成完全独立的报告系统。
- 它不是 Mira 的总入口路由；总入口由 `loops/analysis-routing.md` 处理。
- 它不负责从零解释产业概念；如果输入是 `GPU`、`ABF`、`HBM`、`存储` 这类概念，先使用 `industry-concept-analysis`。
- 它允许写技术面和事件面，但它们服务于 thesis，不单独形成交易系统。
- 它不允许跳过 framework selection 直接套模板。
- 它不允许用 overlay 替代主框架。

## Quality Bar

- 核心结论必须可回溯到来源
- 事实、公司口径、承诺、指引、目标、预测、假设、观点和市场定价必须显式区分
- evidence log 必须记录 `claim_type`、`claim_text`、`source_speaker` 和 `verification_status`
- 每份 memo 必须有时效边界
- 必须说明结论对应的时间跨度，且不能把短期财报信号自动外推成长期 thesis
- 至少覆盖公司、财务、宏观、价格、事件五类视角中的三个
- 必须解释为什么当前框架适配这只票
- 必须指出如果框架错配，最可能错在哪里
- 如果启用 overlay，必须解释它补充验证了什么
- 如果使用 `variant perception`，必须给出可观察的 `consensus proxy` 和 `falsification condition`
- 如果使用 `long-term-multibagger`，必须给出 `target_return_path`、`implied_cagr`、`evidence_ladder`、`dilution_risk` 和 `kill_criteria`
- 如果启用 `macro` overlay，必须写明 `macro_weight`、`dominant_macro_chain`、`market_pricing` 和 `macro_refresh_triggers`
- 如果启用 `strategic-catalyst` overlay，必须写明 `catalyst_status`、`verification_path`、`what_would_confirm` 和 `what_would_disconfirm`
