# Commodity Overlay

这个 overlay 用于判断商品价格、实物供需、库存、期货曲线、成本曲线或资源政策是否是当前股票或资产的核心定价变量。

它不替代 `micro-small`、`mid-cap` 或 `large-mega` 主框架。它只回答：

> 商品周期是否通过 realized price、成本、利润率、现金流、资本开支、风险溢价或仓位，改变了这个资产的定价链？

## Use When

- 目标公司或 ETF 对原油、天然气、金属、贵金属、农产品、化工品、煤炭、铀、锂、铁矿、钢材或其他大宗商品有直接暴露。
- 公司收入、毛利、FCF、资本开支、资产减值、分红/回购或信用风险明显受商品价格影响。
- 当前股价或行业表现明显由商品价格、库存、期货曲线、政策/地缘冲击或资源供需解释。
- 需要区分 `commodity beta` 与 `company alpha`。
- 需要判断商品 ETF、资源股、能源股、材料股、化工、航运、消费或通胀敏感资产的传导链。

## Avoid When

- 商品只是一项小成本或背景变量，不改变 thesis。
- 公司特定事件、融资、生存性、监管审批、订单或技术验证完全主导价格。
- 没有可用的商品价格、库存、曲线、成本或公司暴露数据。
- 研究问题本质是宏观 regime，而不需要拆具体商品供需。

## Selection Questions

启用前至少回答：

- 当前价格主要交易公司变量、商品变量、宏观变量，还是仓位/流动性变量？
- 商品价格通过哪条链影响收入、成本、利润率、FCF、资本开支、估值、融资或催化剂？
- 目标资产的 `commodity_beta` 是 `low`、`medium` 还是 `high`？
- 这次商品变化来自供需、库存、曲线、成本、政策/地缘、金融条件还是定位 squeeze？
- 公司有多少暴露被 hedges、合同价、区域基差、成本通胀或项目执行抵消？
- 市场已经 price in 的商品路径是什么？
- 如果商品判断错了，最可能导致哪类投资误判？

## Commodity Weight

每次使用时必须给出 `commodity_weight`：

- `none`
  商品不是当前有效变量。
- `context`
  商品只提供背景，不进入核心结论。
- `secondary`
  商品会影响利润、估值或风险偏好，但公司/行业变量仍是主导。
- `primary`
  商品是核心定价变量，必须进入 memo 主结论和刷新条件。

## Required Fields

启用 commodity overlay 后，在 memo 或 case notes 中写明：

- `selected_overlays: commodity`
- `commodity_weight`
- `commodity_overlay_basis`
- `dominant_commodity_driver`
  one of `physical_balance`, `inventory_cycle`, `curve_structure`, `cost_curve`, `policy_geopolitics`, `financial_conditions`, `positioning`, `mixed`
- `commodity_transmission_chain`
- `market_pricing`
- `what_is_already_priced`
- `company_alpha_separation`
- `commodity_mismatch_risk`
- `commodity_refresh_triggers`

## Checklist

### Exposure

- 收入、成本、利润率、FCF、capex 或资产价值对哪个商品最敏感？
- 公司披露的 realized price、hedges、contract structure 和 regional basis 是否会削弱 spot price 传导？

### Physical Balance

- 当前供需是短缺、均衡还是过剩？
- 变化来自需求、供应、库存、贸易流、天气、停产、政策还是季节性？

### Inventory And Curve

- 库存方向是否支持价格信号？
- 期货曲线是 contango 还是 backwardation？
- 曲线变化是持续紧张、短期 squeeze，还是融资/仓储因素？

### Cost Curve

- 当前价格是否高于边际供应或 incentive price？
- 是否足以改变关停、复产、资本开支或项目批准？

### Policy And Geopolitics

- 政策或地缘事件影响的是实际量、区域基差、运输路线还是市场情绪？
- 验证路径和反证信号是什么？

### Market Pricing

- 股票、ETF、信用或估值是否已经反映商品价格变化？
- 收益或风险来自 commodity price revision、margin revision、multiple rerating、risk premium change 还是 positioning unwind？

## Primary Output

`commodity` overlay 通常应补充：

- commodity exposure map
- commodity transmission chain
- inventory and curve snapshot
- cost-curve / margin-sensitivity note
- hedging and contract adjustment
- market-pricing map
- refresh triggers
- falsification conditions

## Regime-Specific Notes

### With `large-mega`

常见用途：

- 判断能源、矿业、材料或化工大票的 commodity beta 是否已经主导盈利 revision。
- 区分周期上行中的 beta、资本纪律、资产质量和分红/回购能力。
- 检查实际利率、美元、政策和仓位是否通过商品再影响估值倍数。

### With `mid-cap`

常见用途：

- 判断资源中型股的项目弹性、成本曲线位置、资本开支和再融资风险。
- 检查商品涨价是否能穿透 hedges、区域基差和成本通胀。

### With `micro-small`

常见用途：

- 通常只作为 secondary 或 context，除非单一资源项目、矿权、offtake 或商品价格直接决定生存性。
- 如果融资、许可、项目建设或单一客户完全主导，不应强行启用 commodity overlay。

## Failure Mode

- 商品价格方向判断正确，但公司有 hedges、成本膨胀、项目风险或政治风险，股权没有同等受益。
- 商品现货紧张只是短期物流或合约 squeeze，被误判成长周期短缺。
- 曲线和库存不支持价格叙事。
- 市场已经充分 price in 商品路径，剩余 upside 主要取决于更高阶 surprise。
- 把 commodity beta 当作 company alpha，误判管理层执行或资产质量。

## Source Quality Guidance

- 官方、交易所和行业数据用于事实：产量、库存、贸易流、库存、合约规则和官方预测。
- 市场数据用于价格、曲线、仓位和 ETF 结构。
- 公司披露用于 realized price、hedges、成本、储量、产量、capex 和项目风险。
- 券商、专家和 practitioner 材料用于解释分歧，不作为唯一事实来源。
