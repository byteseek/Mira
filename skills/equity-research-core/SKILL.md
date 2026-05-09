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
- 一个 framework router
- 一个 overlay selector
- 多个可切换研究框架

也就是说，输出仍然统一，但研究顺序、证据权重和结论重心会随标的的定价主导变量变化。

在主框架之外，还允许叠加专题 `overlay`，用于补充特定研究路径。

## Use When

- 需要对单一股票做首次覆盖或阶段性复核
- 需要把多源数据整理成一个可追溯的研究包
- 需要在同一份输出里同时包含公司、财务、宏观、价格、事件等视角
- 需要根据标的特征切换研究框架，而不是默认用同一套分析权重

## Required Inputs

- company_name
- ticker
- market
- research_question
- research_cutoff_date
- thesis_horizon
- `framework_hint`
  可选，用户已有明确框架偏好时使用
- `overlay_hint`
  可选，用户已有明确研究视角时使用

## Framework Routing

在正式分析前，必须先完成 `framework selection`。

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

当前默认支持：

- [supply-chain-overlay](references/supply-chain-overlay.md)
- [macro-overlay](references/macro-overlay.md)

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

## Required Source Types

- `L1` 公司披露或官方材料
- `L5` 市场数据
- `L4` 事件/新闻材料可选但建议使用
- 如果启用 `macro` overlay，至少补充官方宏观数据、政策材料或市场定价数据中的两类

## Output Package

这个 skill 必须输出统一的 `research package`：

- `investment-memo.md`
- `evidence-log.csv`
- `case-notes.md`

研究包里必须显式写明：

- `selected_framework`
- `framework_basis`
- `framework_mismatch_risk`
- `selected_overlays`
- `overlay_basis`

如果研究问题明显属于“预期差判断”，建议额外使用：

- [../../templates/variant-perception-checklist.md](../../templates/variant-perception-checklist.md)

这个 checklist 不替代 memo，只用于把 thesis 压缩成：

- `consensus proxy`
- `what is mispriced`
- `why market may be wrong`
- `what changes the price`
- `what falsifies the view`

## Required Sections In Case Notes

- business and industry
- financial quality
- macro and financial conditions
- technical context
- events and sentiment
- overlays
- fact vs inference

## Boundaries

- 它只定义研究组织方式，不承诺自动抓取。
- 它不把每个框架拆成完全独立的报告系统。
- 它允许写技术面和事件面，但它们服务于 thesis，不单独形成交易系统。
- 它不允许跳过 framework selection 直接套模板。
- 它不允许用 overlay 替代主框架。

## Quality Bar

- 核心结论必须可回溯到来源
- 事实与推断必须显式区分
- 每份 memo 必须有时效边界
- 至少覆盖公司、财务、宏观、价格、事件五类视角中的三个
- 必须解释为什么当前框架适配这只票
- 必须指出如果框架错配，最可能错在哪里
- 如果启用 overlay，必须解释它补充验证了什么
- 如果使用 `variant perception`，必须给出可观察的 `consensus proxy` 和 `falsification condition`
- 如果启用 `macro` overlay，必须写明 `macro_weight`、`dominant_macro_chain`、`market_pricing` 和 `macro_refresh_triggers`
