# ETF Listing Analysis Framework

这个框架把 ETF 新上市视为 `product signal`，而不是直接视为 `flow signal`。

首轮分析关注三件事：

- 发行人为什么现在推出这个产品
- 这个产品真实暴露在哪里，权重机制如何传导
- 它比已有 ETF 多提供了什么：更纯、更便宜、更主动、更容易交易，还是只是追热点

上市后的 AUM、净流入、成交和价差用于后续复盘，不是首轮结论成立的前提。

## Core Principle

ETF 上市是 `revealed product intent`，不是 `confirmed asset demand`。

发行人愿意推一个 ETF，通常说明某类资产或主题具备产品化理由；但首轮分析最重要的是识别这个理由的性质：长期配置、用户偏好、平台战略、资产可达性、主题纯度、费率竞争，还是热点营销。

## First-Pass Checklist

### 1. Issuer Intent

先判断发行人为什么现在推这个产品。允许多标签，但必须给主判断：

| intent | meaning | evidence to check |
| --- | --- | --- |
| hype-capture | 追热点、抢主题名字、承接媒体和散户热度 | 主题已大涨、竞品密集、营销话术强于方法论 |
| long-term-allocation | 建长期配置货架 | 宽渠道适配、低费率、规则稳定、同类成功产品 |
| user-preference | 响应客户或渠道已经存在的需求 | RIA/机构/交易者使用场景清晰 |
| strategic-direction | 代表发行人平台方向 | 产品线连续扩张、管理人资源投入 |
| access-innovation | 把难配置资产变成可交易证券 | 加密、商品、跨境、复杂收益或衍生品结构 |
| theme-purity | 试图比现有 ETF 更纯地表达主题 | 持仓筛选、收入暴露、权重规则更聚焦 |
| fee-lineup-competition | 货架补全、费率竞争、防守客户流失 | 同质化高、费率或品牌差异是核心卖点 |

判断标准：不要只问“这个主题热不热”，而要问“发行人认为谁会买，为什么现有产品不够”。

### 2. Product Structure

不同结构的信号含义不同：

| product type | primary signal | common trap |
| --- | --- | --- |
| passive thematic equity | 主题被产品化 | 主题纯度低或成分股已拥挤 |
| active ETF | 管理人判断和分销能力 | 持仓不透明或风格漂移 |
| broad/sector index | 配置需求或费率竞争 | 只是低费率复制 |
| leveraged/inverse | 交易需求和波动需求 | 不能代表长期配置需求 |
| covered call / income | 收益需求和波动率货币化 | 用高分红包装弱上行 |
| buffer / defined outcome | 防守和结构化需求 | 复杂 payoff 掩盖真实风险 |
| single-stock ETF | 单股交易工具化 | 反映交易热度而非基本面确认 |
| commodity / crypto | 资产可达性变化 | 初期流入可能只是替代原有敞口 |
| bond / duration | 久期、信用或收益偏好 | 受利率环境主导，主题解释力弱 |

### 3. Exposure And Constituent Map

ETF 名字不能替代持仓。必须拆到以下层级：

- `holdings_status`
  已披露、部分披露、未披露/推断
- `selection_universe`
  从哪个资产池选：S&P 500、全球股票、特定行业、管理人自选池等
- `selection_rules`
  进入持仓的规则：财务指标、收入占比、主题相关性、管理人判断等
- `top_holdings`
  前十大或最可能核心暴露
- `top10_weight`
  集中度，未披露则写 unknown
- `exposure_purity`
  标的是否真实贡献目标主题收入、利润、资产或现金流
- `transmission_targets`
  ETF 叙事和资金最可能影响的股票、行业、国家或链条
- `liquidity_sensitivity`
  小市值、低流动性、高权重或低自由流通盘成分股是否更敏感

若持仓尚未披露，只能写 `inferred exposure`，不能写成 confirmed holdings。

### 4. Management And Weighting Mechanics

管理模式和权重模式决定信号强弱：

| mode / weighting | read-through | risk |
| --- | --- | --- |
| market-cap weighted | 常是龙头 beta 或大盘 wrapper | 对中小成分股传导弱 |
| equal-weighted | 主题传导更分散，可能强化中小成分股 | 再平衡和流动性压力更高 |
| modified cap / capped | 兼顾龙头和分散度 | cap 规则可能掩盖实际集中度 |
| theme-revenue / factor weighted | 可能提高主题纯度 | 方法论可能过拟合或样本不稳定 |
| liquidity-weighted | 更能承载交易 | 可能牺牲主题纯度 |
| active discretionary | 代表管理人判断和渠道意图 | 持仓漂移、披露滞后、风格漂移 |
| leveraged / inverse / single-stock | 交易需求强 | 不能外推为长期配置需求 |

必须记录：

- management_mode
- weighting_mode
- rebalance_frequency
- single_name_cap
- sector/country caps
- derivative_usage
- turnover_expectation
- index_or_manager_discretion

### 5. Peer And Timing Context

同类比较用于解释新 ETF 的边际意义：

- 它是否比竞品更纯、更便宜、更主动、更高收益或更容易交易
- 发行人是否有把类似产品做大的历史
- 上市时点处在主题早期、扩散期、拥挤期，还是回撤后的再包装期
- 多家发行人是否同时推出类似产品，说明进入产品竞赛
- 若竞品都很小，可能代表主题表达困难或真实用户需求不足

## Practical Output

一份 ETF 上市分析必须最后落到五类结论之一：

- `actionable-theme`
  可以继续研究主题内股票、行业链条或相邻资产。
- `exposure-watch`
  方向可能重要，但要等持仓/权重披露确认。
- `issuer-intent-watch`
  产品本身说明发行人或渠道方向值得跟踪。
- `liquidity-tool`
  ETF 主要是交易工具，重点是流动性和结构，不是成分股机会。
- `ignore-noise`
  产品信号不足，暂不纳入研究队列。

## Post-Listing Tracking

资金验证不应阻塞首轮分析，但要用于复盘首轮判断：

- 上市后 5、20、60 个交易日 AUM 和净流入
- 成交量、买卖价差、折溢价
- 首次持仓披露是否确认暴露地图
- 同类 ETF 是否出现新增需求或只是 cannibalization
- 再平衡和持仓变化是否带来成分股传导
- 发行人营销、媒体叙事、卖方讨论和期权生态是否扩散

## Failure Modes

- 把 ETF 名字当成真实暴露
- 把上市当成趋势早期，忽略它可能是周期尾声
- 把资金验证当成新 ETF 首轮分析的硬前提
- 忽略管理模式和权重模式
- 忽略同类 ETF 产品线扩张和费率竞争
- 忽略底层资产流动性，夸大 ETF 对成分股价格影响
- 把杠杆、反向、covered call、buffer ETF 的交易需求误读成长期配置需求
- 忽略发行人营销动机

## Falsification Conditions

一个 ETF 上市信号应被降级的条件：

- 持仓披露后主题纯度明显低于产品叙事
- 管理模式或权重规则显示它只是宽基/龙头 wrapper
- 上市后 20 至 60 个交易日无持续关注、成交和渠道讨论
- 成交量低、价差大、折溢价不稳定，产品难以实际交易
- 同类老 ETF 流出完全抵消新 ETF 流入
- 成分股价格和成交没有任何可观察传导
- 发行人快速降低营销力度或产品进入清盘风险
- 主题本身被后续政策、财报或价格行为证伪
