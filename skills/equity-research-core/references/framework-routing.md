# Framework Routing

这个文档定义 `equity-research-core` 如何为单票公司研究选择主研究框架。

它不是 Mira 的总入口路由。总入口先由 `loops/analysis-routing.md` 判断任务是单票、财报、产业概念、宏观、ETF、监控还是方法论。只有当任务进入 `single_equity` 后，才使用本文件。

## Core Rule

先判断 `thesis_horizon`，再判断 `pricing regime`，最后选择主分析框架。

`thesis_horizon` 用于避免把单季财报、未来几个季度的盈利修正和一年以上的长期产业/公司趋势混在一起。规则见 [thesis-horizon-routing.md](thesis-horizon-routing.md)。

`pricing regime` 用于回答：

> 这只股票当前主要由什么变量定价？

## Required Routing Inputs

至少要对以下维度做定性判断：

- `research_question`
- `thesis_horizon`
- `horizon_bucket`
- `horizon_basis`
- `market_cap_bucket`
- `avg_dollar_volume`
- `float_quality`
- `ownership_structure`
- `business_maturity`
- `earnings_stability`
- `primary_catalyst`
- `valuation_anchor_usefulness`
- `macro_sensitivity`
- `institutional_ownership_or_coverage`
- `current_market_label`

## Decision Tree

### 1. Time Boundary

先确认结论时间跨度：

- `near_term_execution`
- `medium_term_revision`
- `long_term_thesis`
- `regime_transition`

如果时间跨度不清楚，先写 `horizon_uncertainty`，不要直接进入结论。

### 2. Valuation Anchor

判断这家公司有没有可靠估值锚：

- 盈利、现金流、收入倍数、资产价值或订单是否能约束估值？
- 市场是否真的用这些锚定价，还是只交易故事、事件和流动性？

如果估值锚很弱，优先考虑 `micro-small` 或事件/生存性框架。

### 3. Dominant Price Setter

判断当前价格主导者更像：

- `scarce_liquidity`
  流通盘、融资、生存性、换手和事件驱动。
- `narrative_and_revision`
  板块标签、行业景气、盈利修正和叙事强化。
- `institutional_allocation`
  机构持仓、贴现率、资本配置、长期盈利曲线和大周期。

### 4. Catalyst Power

判断单一催化剂能否重写中期预期：

- 如果一个订单、监管、产品、融资或客户变化就能改变生存性或估值锚，偏 `micro-small`。
- 如果催化剂需要通过多个季度业绩兑现才能改变市场，偏 `mid-cap`。
- 如果单个事件只有在改变多年现金流曲线时才重要，偏 `large-mega`。

### 5. Macro And Cycle Weight

宏观敏感度强时，不直接把宏观当主框架。

先选：

- `micro-small`
- `mid-cap`
- `large-mega`

再判断是否启用 `macro` overlay，并写 `macro_weight`。

## Default Frameworks

### `micro-small`

适用于以下组合特征占主导时：

- 小微盘或低流动性
- 自由流通盘薄
- 盈利不稳定、尚未形成可靠估值锚
- 单一事件、订单、产品、融资、监管变化即可显著改写预期
- 管理层可信度、融资能力、生存性对股价影响大

研究重点通常是：

- 生存性
- 稀释和融资
- 单一催化剂兑现
- float / liquidity
- 管理层可信度
- 叙事真假和兑现路径

### `mid-cap`

适用于以下组合特征占主导时：

- 中盘且流动性尚可
- 价格更常受板块轮动、行业景气、公司叙事和业绩兑现共同影响
- 估值有参考意义，但往往不是唯一核心变量
- 机构覆盖和市场标签都在形成或强化过程中

研究重点通常是：

- 行业景气
- 盈利修正
- 叙事强化或降温
- 板块相对强弱
- 估值修复空间
- 公司 alpha vs 行业 beta

### `large-mega`

适用于以下组合特征占主导时：

- 大盘或超大盘
- 机构持仓和资产配置逻辑影响大
- 盈利预期、估值贴现、宏观利率和行业大周期决定中期方向
- 单个产品或事件通常只影响边际预期，除非能改写中期或长期盈利曲线

研究重点通常是：

- 多季度盈利路径
- 长期现金流曲线
- 资本开支和股东回报
- 机构仓位和配置属性
- 贴现率和宏观敏感度
- 长周期行业位置

## Horizon X Framework Matrix

### `near_term_execution`

- `micro-small`
  看单一事件是否改变融资、生存性、订单或叙事。
- `mid-cap`
  看财报、指引和催化剂是否改变未来 1-2 个季度盈利修正。
- `large-mega`
  看本期结果是否改变全年路径、机构预期或资本配置节奏。

### `medium_term_revision`

- `micro-small`
  看事件兑现后是否能形成可持续收入、现金流或估值锚。
- `mid-cap`
  看 FY1/FY2 revision、行业景气和叙事是否同向。
- `large-mega`
  看未来多个季度收入、利润率、capex、FCF 和 buyback 路径。

### `long_term_thesis`

- `micro-small`
  谨慎使用。必须证明公司能从事件资产转成可持续经营资产。
- `mid-cap`
  看公司能否从板块弹性变成长期份额、利润池或商业模式赢家。
- `large-mega`
  看长期现金流曲线、护城河、资本配置、平台价值和产业周期。

### `regime_transition`

- `micro-small`
  事件可能把公司从生存/验证阶段推入可估值阶段，或反向证伪。
- `mid-cap`
  多季度证据可能把板块叙事升级为长期公司 alpha，或暴露伪成长。
- `large-mega`
  新产品、capex、监管、AI/技术周期或资本配置可能改写长期曲线。

## Practical Routing Rules

优先路由到 `micro-small`，如果：

- `valuation_anchor_usefulness` 很弱
- 公司仍处于融资、生存或单项目验证阶段
- 市场对单一订单、产品、监管结果反应可能极端
- 成交承接弱，价格容易被预期变化放大

优先路由到 `mid-cap`，如果：

- 公司已有业务基础，但市场仍在给它定义主标签
- 盈利修正、行业景气和叙事变化共同主导价格
- 估值锚存在但不稳定
- 板块轮动和相对强弱对定价很重要

优先路由到 `large-mega`，如果：

- 盈利预测、贴现率、资本开支或机构再配置主导定价
- 市场更关心未来多个季度的盈利路径而不是单次事件
- 单个事件除非改变长期曲线，否则不足以独立解释股价
- 公司更像配置型、平台型或周期型权重资产

## Mixed Cases

允许混合判断，但必须明确：

- `selected_framework`
- `secondary_regime`
- `why_not_other_framework`
- `framework_mismatch_risk`

示例：

- 表面是中盘，但流通盘偏薄且被单一事件主导，可选 `micro-small`。
- 表面是大盘，但若正处于重大转型并且事件直接重写长期盈利，可保留 `large-mega` 主框架，同时显式抬高事件分析权重。
- 表面是小票，但已经有稳定盈利和机构覆盖，且价格主要跟随行业景气和盈利修正，可升到 `mid-cap`。

## Overlay And Lens Handoff

主框架选完后，再判断：

- 是否启用 `supply-chain` overlay
- 是否启用 `macro` overlay
- 是否启用 `market-structure-policy` overlay
- 是否启用 `variant-perception` lens

规则：

- overlay 负责补证据链，不替代主框架
- lens 负责约束 thesis 写法，不替代主框架
- 如果宏观变量可能主导当前定价，优先参考 [macro-overlay.md](macro-overlay.md)，并写明 `macro_weight`
- 如果上市地、交易地、资金通道、政策监管、治理折价或 A/H/ADR 多地上市可能主导当前定价，优先参考 [overlay-routing.md](overlay-routing.md) 的 `market-structure-policy`，并写明 `market_structure_weight`
- 如果研究问题本质是“市场预期错在哪里”，使用 `variant-perception` checklist

## Output Requirements

在 `investment memo` 和 `case notes` 中都要留下：

- `horizon_bucket`
- `horizon_basis`
- `horizon_mismatch_risk`
- `selected_framework`
- `framework_basis`
- `secondary_regime`
- `why_not_other_framework`
- `framework_mismatch_risk`
- `selected_overlays`
- `selected_lenses`

`framework_mismatch_risk` 用于回答：

如果这个框架选错，最可能导致哪类误判。

## Stop Rules

- 如果无法判断 `thesis_horizon`，不要直接选公司框架。
- 如果无法判断当前主导定价变量，允许写 `selected_framework: provisional`。
- 如果 macro 只是背景，不要让它吞掉公司框架。
- 如果一个 overlay 只是增加材料但不能改变证据质量，不启用。
- 如果一个 lens 只是让 memo 更复杂但不能提高可证伪性，不启用。
