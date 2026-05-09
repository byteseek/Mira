# ETF Listing Analysis Skill

这个 skill 用于分析新上市 ETF、即将上市 ETF、ETF 申请文件和 ETF 产品线扩张。

它不把 ETF 新上市直接等同于买入信号，也不要求新 ETF 在首轮分析中已经完成资金验证。新上市本身首先是一个 `product signal`：发行人为什么现在愿意把某类暴露做成产品，想卖给谁，底层持仓和权重机制会把这个信号传导到哪里。

核心目标是回答：

新 ETF 上市到底代表真实配置方向、交易工具需求、资产可达性变化、用户偏好，还是主题营销和周期尾声包装？

## Use When

- 用户要求分析一个新上市 ETF 或即将上市 ETF
- 用户想从 ETF 新发看市场偏好、配置方向、主题热度或成分股机会
- 研究对象是 ETF 申请、上市公告、招募说明书、指数方法论或主动 ETF 组合
- 需要判断某个主题是否开始进入机构可配置产品货架
- 需要把 ETF 暴露传导到股票、行业、国家、债券、商品或加密资产

## Avoid When

- ETF 只是已有宽基产品的低费率复制，且没有新的配置含义
- 上市主要是基金转换、税务结构调整或发行人内部产品整理
- 底层资产极度不透明，无法确认持仓、指数规则或管理方式
- 研究问题本质是单家公司财报、基本面或事件，ETF 只是背景噪音

## Required Inputs

- etf_name
- ticker
- market
- issuer
- listing_date
- product_type
  例如 passive index、active ETF、rules-based active、leveraged/inverse、covered call、buffer、single-stock、commodity、crypto、bond、thematic equity
- management_mode
  例如 passive index、active discretionary、rules-based active、quantitative active、synthetic/derivative based
- weighting_mode
  例如 market-cap weighted、equal-weighted、modified market-cap、liquidity-weighted、factor-weighted、theme-revenue-weighted、active discretionary
- underlying_exposure
  例如国家、行业、主题、因子、期限、商品、币种或单股
- holdings_status
  `confirmed`、`partial` 或 `unavailable/inferred`
- research_cutoff_date
- thesis_horizon

建议补充：

- fee、index_provider、index_methodology、holdings、weighting_rules、rebalance_frequency
- top holdings、top10_weight、single_name_cap、sector/country caps、theme revenue purity
- peer ETF set、category products、issuer product history、distribution channel
- seed capital、AUM、volume、bid-ask spread、creation/redemption unit
- authorized participants、market makers、options listing status
- underlying holdings liquidity、float、short interest、ownership and crowding

## Framework

首轮分析必须分成四个核心判断和一个后续跟踪层：

1. `issuer intent`
2. `structure and access`
3. `exposure and constituent map`
4. `mode and weighting mechanics`
5. `post-listing tracking`

`post-listing tracking` 是后续验证层，不是新 ETF 首轮结论的前置条件。

### 1. Issuer Intent

先判断发行人为什么现在推这个产品。允许多标签，但必须给主判断：

- `hype-capture`
  追热点、抢主题名字、承接媒体和散户热度。
- `long-term-allocation`
  建立长期配置货架，服务模型组合、顾问、机构或长期主题配置。
- `user-preference`
  响应客户、RIA、交易员、机构或零售用户已经存在的表达需求。
- `strategic-direction`
  代表发行人产品线或平台方向，例如主动 ETF 化、加密资产、能源转型、期权收益。
- `access-innovation`
  把难直接买、难托管、难税务处理或难跨境配置的资产包装成普通账户可交易产品。
- `theme-purity`
  试图比现有 ETF 更纯粹地表达某个主题、产业链或因子。
- `fee-lineup-competition`
  补全产品线、降低费率、替代竞品或防止客户流失。

必须区分：这是发行人想卖的故事，还是投资者已经需要的工具。

### 2. Structure And Access

产品结构决定 ETF 上市信号的含义：

| product type | primary signal | common trap |
| --- | --- | --- |
| passive thematic equity | 主题被产品化 | 名字热但主题纯度低 |
| active ETF | 管理人判断、渠道需求和组合表达 | 持仓漂移或披露滞后 |
| broad/sector index | 配置需求或费率竞争 | 只是低费率复制 |
| leveraged/inverse | 交易需求和波动需求 | 不能代表长期配置需求 |
| covered call / income | 收益需求和波动率货币化 | 用高分红包装弱上行 |
| buffer / defined outcome | 防守和结构化需求 | payoff 复杂，真实风险被隐藏 |
| single-stock ETF | 单股交易工具化 | 反映交易热度而非基本面确认 |
| commodity / crypto | 资产可达性变化 | 初期需求可能是替代原有敞口 |
| bond / duration | 久期、信用或收益偏好 | 宏观利率解释力可能高于产品信号 |

### 3. Exposure And Constituent Map

必须拆持仓或指数方法论。若持仓尚未披露，必须明确标注 `inferred`，不得把推断写成事实。

必填字段：

- `holdings_status`
  confirmed、partial、unavailable/inferred
- `selection_universe`
  成分股从哪里来：S&P 500、全球股票、特定行业、交易所上市资产、管理人自选池等
- `selection_rules`
  进入持仓的定量或定性规则
- `top_holdings`
  前十大或预期核心暴露
- `top10_weight`
  前十大集中度，未披露则写 unknown
- `exposure_purity`
  标的是否真有目标主题收入、资产、利润或现金流暴露
- `constituent_transmission`
  ETF 资金和叙事最可能传导到哪些股票、行业、国家或链条
- `liquidity_sensitivity`
  哪些低流动性、小市值或高权重标的更容易受 ETF 影响

### 4. Mode And Weighting Mechanics

管理模式和权重模式是 ETF 上市分析的核心，不是附录。

| mode / weighting | read-through | risk |
| --- | --- | --- |
| market-cap weighted | 更像大市值 beta 或龙头 wrapper | 成分股机会可能已高度拥挤 |
| equal-weighted | 更容易把主题传导到中小权重公司 | 再平衡交易和低流动性风险更高 |
| modified cap / capped | 兼顾龙头和分散度 | cap 规则可能掩盖真实集中度 |
| theme-revenue / factor weighted | 可能提高主题纯度 | methodology 可能过拟合或样本不稳定 |
| liquidity-weighted | 更适合交易和大资金承载 | 牺牲主题纯度 |
| active discretionary | 代表管理人判断和分销意图 | 持仓漂移、风格漂移和披露滞后 |
| leveraged / inverse / single-stock | 代表交易和波动需求 | 不能外推为长期配置需求 |

必须检查：

- `rebalance_frequency`
- `single_name_cap`
- `sector/country caps`
- `derivative_usage`
- `turnover_expectation`
- `index_or_manager_discretion`

### 5. Peer And Timing Context

同类产品比较用于解释产品定位，不用于机械否定新 ETF：

- 新 ETF 是否比竞品更纯、更便宜、更主动、更高收益或更容易交易
- 发行人是否有分销优势或过往同类成功经验
- 主题处在早期产品化、主升扩散、拥挤尾声，还是回撤后再包装
- 若多个发行人同时推类似 ETF，说明主题进入产品竞赛
- 若竞品很多但都很小，可能是用户需求弱或主题表达困难

### 6. Post-Listing Tracking

上市后资金、成交和价差用于复盘，不是首轮分析的必要门槛。

跟踪重点：

- 5、20、60 个交易日 AUM 和净流入
- 成交量、买卖价差、折溢价
- 持仓披露是否确认首轮暴露判断
- 同类 ETF 是否出现新增需求或只是 cannibalization
- 再平衡和持仓变化是否带来成分股传导
- 发行人营销、媒体叙事、卖方讨论和期权生态是否扩散

## Output Package

默认输出一份 `etf-listing-analysis`，至少包含：

- analysis setup
- core conclusion
- product anatomy
- issuer intent
- structure and access
- exposure and constituent map
- mode and weighting mechanics
- peer and category comparison
- bull interpretation
- bear interpretation
- practical trade/read-through
- post-listing tracking plan
- falsification conditions
- evidence log notes

如果 ETF 分析指向具体股票机会，再进入 `equity-research-core`：

- 先选成分股或受益链条
- 再执行 `framework selection`
- 必要时叠加 `supply-chain` 或 `variant-perception`

## Signal Interpretation

ETF 新上市通常可以有六种解释：

- `early-institutionalization`
  主题开始从故事变成可配置产品，值得继续跟踪。
- `confirmed-user-demand`
  产品设计明显回应了用户、顾问或机构的现有需求。
- `strategic-platform-move`
  发行人通过新 ETF 表达自身业务方向或产品线迁移。
- `late-cycle-packaging`
  产品在主题拥挤、估值极高或散户热度很高时推出，更多是兑现情绪。
- `synthetic-access-signal`
  ETF 解决了准入、托管、税务、监管、期限、杠杆或收益结构问题，重点在资产可达性变化。
- `low-signal-lineup-fill`
  主要是补货架、费率竞争或产品线防守，投资含义有限。

## Quality Bar

- 不允许只凭 ETF 名字判断主题暴露
- 必须核对招募说明书、持仓、指数方法论或主动管理披露
- 必须明确 `management_mode` 和 `weighting_mode`
- 必须区分 confirmed holdings 和 inferred holdings
- 必须解释发行人意图，不只复述产品介绍
- 必须比较同类 ETF，避免把普通产品线扩张误读成趋势信号
- 必须说明底层资产流动性是否足以让 ETF 持仓或再平衡产生价格影响
- 必须给出 `what would falsify this listing signal`
- 如果持仓或方法论数据不足，只能输出 `watchlist / needs-holdings-confirmation`，不能升级为投资结论

## Source Requirements

优先来源：

- `L1` ETF 招募说明书、issuer product page、持仓披露、公告
- `L2` 交易所、监管文件、指数提供商方法论
- `L5` AUM、净流入、成交量、价差、折溢价、成分股市场数据
- `L3/L4` ETF 行业研究、财经媒体、发行人访谈、策略评论

`L3/L4` 只能帮助解释产品语境和市场叙事，不能替代持仓、结构、权重机制和方法论。

## Refresh Triggers

必须刷新分析的情况：

- 上市后 5、20、60 个交易日
- 持仓首次披露或发生大幅变化
- AUM 或净流入突破同类产品显著分位
- 成交量和价差明显改善或恶化
- 期权上市或衍生品使用明显增加
- 同主题出现多个竞品 ETF 或发行人撤回/清盘
- 底层主题出现政策、财报、监管或价格冲击
