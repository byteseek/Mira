# Framework Routing

这个文档定义 `equity-research-core` 在正式分析前如何选择主研究框架。

目标不是把股票机械地分成大中小盘，而是识别这只票在当前阶段主要由什么变量定价。

## Core Rule

先判断 `pricing regime`，再选择主分析框架。

优先级高于单纯市值分桶的信号：

- 流动性与自由流通盘
- 收益稳定性与盈利可锚定程度
- 机构持仓和配置属性
- 当前市场是否围绕单一催化剂交易
- 叙事是否足以压过静态估值
- 宏观贴现和行业周期是否主导定价

如果 `macro_sensitivity` 很强，不要直接把它当成主框架。先选 `micro-small`、`mid-cap` 或 `large-mega`，再判断是否启用 `macro` overlay。

## Required Routing Inputs

至少要对以下维度做定性判断：

- `market_cap_bucket`
- `avg_dollar_volume`
- `float_quality`
- `ownership_structure`
- `business_maturity`
- `earnings_stability`
- `primary_catalyst`
- `valuation_anchor_usefulness`
- `macro_sensitivity`

## Default Frameworks

### `micro-small`

适用于以下组合特征占主导时：

- 小微盘或低流动性
- 自由流通盘薄
- 盈利不稳定、尚未形成可靠估值锚
- 单一事件、订单、产品、融资、监管变化即可显著改写预期
- 管理层可信度、融资能力、生存性对股价影响大

### `mid-cap`

适用于以下组合特征占主导时：

- 中盘且流动性尚可
- 价格更常受板块轮动、行业景气、公司叙事和业绩兑现共同影响
- 估值有参考意义，但往往不是唯一核心变量
- 机构覆盖和市场标签都在形成或强化过程中

### `large-mega`

适用于以下组合特征占主导时：

- 大盘或超大盘
- 机构持仓和资产配置逻辑影响大
- 盈利预期、估值贴现、宏观利率和行业大周期决定中期方向
- 单个产品或事件通常只影响边际预期，除非能改写中期盈利曲线

## Decision Order

按以下顺序判断：

1. 这只票有没有可靠估值锚。
2. 单一催化剂能不能重写中期预期。
3. 价格主导者更像短缺流动性、板块动量，还是机构配置。
4. 宏观贴现和行业周期对价格波动的解释力有多强。
5. 当前研究问题要求的是事件判断、叙事判断，还是盈利贴现判断。

## Practical Routing Rules

满足以下情形时，优先路由到 `micro-small`：

- `valuation_anchor_usefulness` 很弱
- 公司仍处于融资、生存或单项目验证阶段
- 市场对单一订单、产品、监管结果反应可能极端
- 成交承接弱，价格容易被预期变化放大

满足以下情形时，优先路由到 `large-mega`：

- `macro_sensitivity` 很强
- 盈利预测、贴现率、资本开支或机构再配置主导定价
- 市场更关心未来多个季度的盈利路径而不是单次事件
- 单个事件除非改变长期曲线，否则不足以独立解释股价

其余多数情形，默认先进入 `mid-cap`，再检查是否存在明显偏向。

## Mixed Cases

允许混合判断，但必须明确：

- `selected_framework`
- `secondary_regime`
- `why_not_other_framework`

示例：

- 表面是中盘，但流通盘偏薄且被单一事件主导，可选 `micro-small`
- 表面是大盘，但若正处于重大转型并且事件直接重写长期盈利，可保留 `large-mega` 主框架，同时显式抬高事件分析权重

## Output Requirements

在 `investment memo` 和 `case notes` 中都要留下：

- `selected_framework`
- `framework_basis`
- `framework_mismatch_risk`

`framework_mismatch_risk` 用于回答一个问题：

如果这个框架选错，最可能导致哪类误判。

如果还需要专题研究路径，再继续参考 [overlay-routing.md](overlay-routing.md)。

如果宏观变量可能主导当前定价，优先参考 [macro-overlay.md](macro-overlay.md)，并写明 `macro_weight`。
