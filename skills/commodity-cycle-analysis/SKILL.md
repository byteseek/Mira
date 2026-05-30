# Commodity Cycle Analysis Skill

这个 skill 用于研究实物大宗商品、商品期货曲线、资源周期和商品价格对资产的传导。

它不是泛宏观综述，也不是资源股单票模板。它服务于一个核心问题：

> 当前商品价格到底由供需平衡、库存、成本曲线、政策/地缘风险、金融条件还是仓位驱动？这个驱动是否足以改变目标资产的盈利、估值、风险溢价或交易节奏？

## Use When

- 研究对象是原油、成品油、天然气、LNG、煤炭、铜、铝、镍、锂、铀、铁矿、钢、黄金、白银、农产品或其他商品。
- 用户问商品价格、期货曲线、库存、供需平衡、成本曲线、OPEC、制裁、出口限制、矿山供给、天气、WASDE、EIA、IEA、LME、CFTC 或商品 ETF。
- 单票、ETF 或产业研究的主变量是商品 beta，而不是公司自身执行、技术路线或普通宏观风险偏好。
- 需要判断资源股、能源股、材料股、化工、航运、消费或通胀资产受到商品冲击的方向和幅度。

## Avoid When

- 目标资产的主要变量是公司订单、融资、生存性、监管审批、技术验证或并购催化剂。
- 商品价格只是背景，不能改变收入、利润率、资本开支、估值、资金流或仓位。
- 没有可用的供需、库存、曲线或成本数据，只能复述价格走势。
- 研究对象是泛宏观 regime，且不需要拆具体商品的物理平衡表。

## Required Inputs

- `commodity_or_asset`
- `market_scope`
  例如 `global` / `US` / `China` / `Europe` / `multi`
- `research_question`
- `research_cutoff_date`
- `thesis_horizon`
  例如 `days_weeks` / `1Q_2Q` / `2Q_8Q` / `cycle`
- `current_market_pricing`
  至少包括现货、近月、远月、曲线形态或相关 ETF/股票表现中的两项。
- `commodity_sources`
  至少覆盖官方/行业数据、市场价格或仓位数据、公司/行业披露、机构或 practitioner 解释中的两类。

## Core Principle

先拆物理平衡，再拆金融定价；先问价格在反映什么，再问这个反映能不能持续。

商品研究不能只看价格涨跌。必须把结论落到至少一条可证伪链条：

- `demand shock -> inventory draw -> curve backwardation -> producer cash flow revision`
- `supply disruption -> spot premium -> cost passthrough -> downstream margin compression`
- `cost curve reset -> marginal supply discipline -> long-dated price support`
- `policy/geopolitics -> trade flow rerouting -> regional basis widening -> asset impact`
- `real rates / dollar -> investment demand -> precious metal price -> miner multiple`
- `weather / crop condition -> yield revision -> stock-to-use ratio -> futures curve`
- `positioning squeeze -> price overshoot -> roll yield / equity beta risk`

If no credible chain exists, commodity stays as context and should not enter the core thesis.

## Analysis Sequence

### 0. Routing Snapshot

Start every formal note with:

- `task_mode`
- `commodity_or_asset`
- `market_scope`
- `time_boundary`
- `dominant_driver`
  one of `physical_balance`, `inventory_cycle`, `cost_curve`, `policy_geopolitics`, `financial_conditions`, `positioning`, `mixed`
- `commodity_weight`
  one of `none`, `context`, `secondary`, `primary`
- `routing_mismatch_risk`
- `expected_output_package`

### 1. Commodity Identity And Contract Map

Define what is being studied:

- physical commodity, benchmark, grade, geography and delivery point
- main traded instruments: spot benchmark, futures contract, ETF, equity proxy or spread
- substitutes and adjacent commodities
- most relevant consuming sectors
- most relevant producing regions or companies

Avoid mixing benchmarks without saying so. WTI is not Brent; Henry Hub is not JKM; LME copper is not every copper concentrate or regional premium; gold bullion is not gold miners.

### 2. Physical Balance

Build the balance in levels and deltas:

- production / supply
- consumption / demand
- imports / exports and trade flows
- inventories and stock changes
- spare capacity or shut-in / restart capacity
- seasonal pattern
- bottlenecks: logistics, refining, smelting, grid, shipping, storage or permitting

Separate:

- `level`
- `change`
- `surprise_vs_expectation`
- `breadth`
- `sustainability`

### 3. Inventory And Curve Structure

Always inspect inventory together with curve structure.

Required checks:

- exchange or official inventory level and direction
- commercial / strategic / visible vs invisible inventory when available
- days of cover or stock-to-use ratio when relevant
- spot vs front-month vs deferred prices
- contango / backwardation and spread movement
- roll yield implication for ETFs and futures-based exposure

Interpretation guardrail:

- Falling inventory with backwardation usually signals tightness, but can be distorted by logistics, sanctions, financing cost, storage constraints or contract-specific squeezes.
- Rising inventory with contango usually signals slack, but can coexist with future supply risk or seasonal builds.

### 4. Cost Curve And Supply Response

For producers and resource equities, connect price to marginal economics:

- cash cost, all-in sustaining cost, marginal cost or incentive price
- capex cycle and project lead time
- depletion, decline rate or reserve quality
- shut-in, restart and substitution thresholds
- cost inflation in labor, energy, freight, reagents, equipment or financing
- producer discipline versus growth capex

Core question:

> Is price above the level that changes behavior, or merely moving within noise?

### 5. Demand Map

Split demand by end market and sensitivity:

- cyclical industrial demand
- transport / mobility
- power generation
- construction / property
- manufacturing / electronics
- agriculture / food / feed
- investment and reserve demand
- policy-driven or energy-transition demand

For each demand bucket:

- leading indicators
- lag to commodity consumption
- substitution risk
- price elasticity
- reliability of available data

### 6. Policy, Geopolitics And Trade Flow

Do not treat policy and geopolitics as generic risk labels.

Map the concrete mechanism:

- production quota
- export ban or license
- sanctions and enforcement
- tariffs or trade restrictions
- strategic reserve purchase / release
- environmental permit, mine license or pipeline approval
- shipping route disruption
- local subsidy or demand mandate

Then state:

- affected volume
- affected region or benchmark
- expected duration
- verification path
- what would confirm
- what would disconfirm

### 7. Financial Conditions And Positioning

Use this layer only after physical balance is clear, unless the commodity is primarily financialized in the current setup.

Check:

- dollar and real rates
- inflation expectations
- CFTC COT or exchange positioning where available
- ETF flows and open interest
- volatility, skew and CTA trend risk when available
- roll yield and funding cost

Do not confuse a positioning squeeze with a durable supply-demand deficit.

### 8. Asset Transmission

Map commodity move to the target asset:

- producers: realized price, hedges, cost inflation, volume, capex, FCF, buybacks/dividends
- consumers: input cost, pass-through ability, gross margin, working capital, demand destruction
- ETFs/futures: roll yield, benchmark tracking, liquidity, tax/structure risk
- macro assets: inflation, fiscal/external balance, rates, currency and risk premium
- resource equities: commodity beta, company alpha, balance sheet, project execution and political risk

For single-equity handoff, state:

- `commodity_beta`
  one of `low`, `medium`, `high`
- `commodity_driver_quality`
  one of `high`, `medium`, `low`, `source_gap`
- `company_alpha_separation`
  what can be explained by commodity price versus company-specific execution.

### 9. Market Pricing And Variant Perception

Commodity work must include what is already priced:

- current spot / curve shape
- consensus or public forecast range when available
- equity or ETF relative performance
- inventory and curve signals already visible to market
- key debate and opposing view

Then define:

- base case
- bull case
- bear case
- surprise needed for repricing
- what would make the view stale

## Required Source Types

Minimum coverage depends on the commodity, but every durable conclusion should try to include:

- `L2` official or industry data:
  EIA, IEA, OPEC, USDA WASDE, USGS, LME, exchange data, customs data, national statistics, industry associations.
- `L5` market data:
  spot/futures prices, curve spreads, ETF performance, open interest, CFTC COT or exchange positioning.
- `L1` company disclosures when mapping to equities:
  producer reports, reserves, cost guidance, hedges, capex and operating metrics.
- `L3` institutional or specialist research:
  used for interpretation, not as primary fact.
- `L4` news and practitioner commentary:
  useful for disruptions and trade-flow color, but must be cross-checked.

Source-quality rule:

- Official data supports facts.
- Market data supports pricing and positioning.
- Company disclosure supports company exposure.
- Institutional/practitioner sources support interpretation only unless independently verifiable.

## Output Package

For standalone commodity work, output a `commodity-analysis-package`:

- `commodity-cycle-note.md`
- `evidence-log.csv`

`commodity-cycle-note.md` must contain:

- routing snapshot
- one-page view
- contract / benchmark map
- physical balance
- inventory and curve structure
- cost curve and supply response
- demand map
- policy / geopolitics / trade flow
- financial conditions and positioning
- asset transmission
- market pricing and variant perception
- monitoring dashboard
- stale_after
- must_refresh_if

For equity research, add commodity fields to memo or case notes:

- `selected_overlays: commodity`
- `commodity_weight`
- `commodity_overlay_basis`
- `dominant_commodity_driver`
- `commodity_transmission_chain`
- `what_is_already_priced`
- `commodity_mismatch_risk`
- `commodity_refresh_triggers`

## Monitoring Dashboard

Every commodity view needs a small dashboard:

- price: spot, front-month and key deferred contract
- curve: nearest relevant spread
- inventory: level and direction
- supply: production / outage / quota / project update
- demand: high-frequency proxy or official demand update
- cost: marginal or incentive-cost proxy if available
- policy/geopolitics: active event and verification path
- positioning: COT / ETF flow / open interest where relevant

## Failure Modes

- Treating every commodity move as macro when the true driver is inventory or trade flow.
- Treating every inventory draw as durable demand without checking seasonality and logistics.
- Ignoring curve structure and roll yield when analyzing futures or commodity ETFs.
- Using producer equities as pure commodity proxies without separating hedges, costs, balance sheet and project risk.
- Confusing spot tightness with long-cycle incentive pricing.
- Ignoring policy quota, sanctions, export bans or strategic reserve actions.
- Explaining price action after the fact without predefining refresh and falsification triggers.

## Current Status

- methodology_status: `trial`
- related_methodology_card: `memory/methodologies/commodity-cycle-analysis.md`
- related_overlay: `skills/equity-research-core/references/commodity-overlay.md`
