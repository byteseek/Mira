# Macro Overlay

这个 overlay 用于判断宏观变量是否是当前股票或资产的核心定价变量。

它不替代 `micro-small`、`mid-cap` 或 `large-mega` 主框架。它只回答：

> 宏观是否通过增长、通胀、政策、流动性、信用、利率、汇率或风险偏好，改变了这个资产的定价链？

## Use When

- 目标资产对利率、通胀、美元、信用、能源、财政或政策路径高度敏感。
- 当前股价或行业表现明显由宏观数据、央行表态、收益率、美元、信用利差或风险偏好驱动。
- 研究对象属于以下类型之一：
  - 指数或 ETF
  - 银行、地产、保险、券商
  - 资源、能源、工业、运输、化工、材料
  - 出口链、跨国收入占比高的公司
  - 高估值成长股、AI capex 链、长久期资产
  - 黄金、美债、美元、加密资产等宏观敏感资产
- 用户明确提出宏观经济、利率、央行、美元、财政、流动性或经济周期。

## Avoid When

- 公司特定事件、融资、生存性、监管审批或单一订单完全主导价格。
- 宏观只能解释背景，但不能改变收入、利润率、贴现率、风险溢价、资金流或仓位。
- 研究者无法说明“市场已经 price in 什么”。
- 只能得到宽泛判断，例如“经济不好所以股票不好”。

## Selection Questions

启用前至少回答：

- 当前价格主要交易的是公司变量、行业变量、宏观变量，还是仓位/流动性变量？
- 哪个宏观变量的边际变化最可能改变 thesis？
- 这个变量通过哪条链传导到收入、利润率、估值、融资、仓位或催化剂？
- 市场已经 price in 的宏观路径是什么？
- 新数据相对预期是 surprise 还是 confirmation？
- 如果宏观判断错了，最可能导致哪类投资误判？

## Macro Weight

每次使用时必须给出 `macro_weight`：

- `none`
  宏观不是当前有效变量。
- `context`
  宏观只提供背景，不进入核心结论。
- `secondary`
  宏观会影响估值或风险偏好，但公司/行业变量仍是主导。
- `primary`
  宏观是核心定价变量，必须进入 memo 主结论和刷新条件。

## Required Fields

启用 macro overlay 后，在 memo 或 case notes 中写明：

- `selected_overlays: macro`
- `macro_weight`
- `macro_overlay_basis`
- `dominant_macro_variable`
- `dominant_macro_chain`
- `market_pricing`
- `what_is_already_priced`
- `macro_mismatch_risk`
- `macro_refresh_triggers`

## Regime Checklist

### Growth

- 增长是加速、减速、韧性还是断裂？
- 影响收入 beta、盈利弹性、信用质量还是风险偏好？

### Inflation

- 通胀是需求、供给、工资、租金、商品、关税、汇率还是能源驱动？
- 它影响央行路径、实际利率、利润率还是估值倍数？

### Policy

- 政策反应函数是否改变？
- 市场预期路径与政策口径是否偏离？

### Liquidity And Financial Conditions

- 利率、信用、股价、美元、融资成本是否同向收紧或出现分裂？
- 金融条件是支持 risk-taking，还是压缩估值和融资能力？

### Credit

- 利差、银行贷款、违约率、再融资压力是否改变企业风险溢价？

### FX And Rates

- 汇率和利率变化是否影响收入换算、进口成本、资本流向、外债压力或估值贴现？

### Risk Appetite And Positioning

- 价格变化来自 earnings revision，还是来自仓位、波动率、杠杆或风险预算？

### Market Pricing

- 市场当前隐含的是 soft landing、recession、reflation、stagflation、liquidity rally，还是 productivity boom？
- 关键数据或政策是否足以推翻这个隐含路径？

## Primary Output

`macro` overlay 应补充：

- regime classification
- transmission chain
- market-pricing map
- asset impact table
- refresh triggers
- falsification conditions

## Regime-Specific Notes

### With `large-mega`

常见用途：

- 判断利率和实际利率对估值倍数的影响。
- 判断机构配置、美元和风险偏好是否主导价格。
- 判断 AI capex、财政、流动性或全球增长是否正在变成大票核心变量。

### With `mid-cap`

常见用途：

- 判断板块轮动是行业景气改善，还是宏观风险偏好扩张。
- 判断盈利兑现和估值修复是否依赖利率、信用或政策窗口。

### With `micro-small`

常见用途：

- 通常只作为背景，除非利率、融资环境、流动性或风险偏好直接影响融资生存性。
- 如果单一催化剂完全主导，不应强行启用 macro overlay。

## Failure Mode

- 宏观判断正确，但传导到目标资产的链条太弱。
- 宏观数据方向正确，但市场已经充分 price in。
- 用滞后数据解释已经发生的价格。
- 忽略仓位和流动性，误把 squeeze 或 de-risking 当成基本面变化。
