# Overlay Routing

这个文档定义主框架选定后，哪些专题研究路径值得叠加为 `overlay`。

overlay 不是新的主框架，而是额外的验证视角。

## Core Rule

先回答“这只票怎么被定价”，再回答“哪条补充研究链条最值得沿着挖”。

如果某条专题路径同时满足以下条件，可以启用 overlay：

- 能显著提升 thesis 可解释性
- 能帮助发现新的证据链或对手盘假设
- 不会取代主框架本身

## Current Overlay

### `supply-chain`

适用于以下情形：

- 上游成本、产能、交付瓶颈会明显影响利润率或出货
- 下游客户、渠道、终端需求会明显影响收入确定性
- 需要沿上下游核验景气传导是否真实
- 需要通过同层级公司比对验证竞争位置
- 需要从客户、供应商、竞品三端交叉印证公司叙事

### `macro`

适用于以下情形：

- 增长、通胀、政策、利率、美元、信用、流动性或风险偏好明显主导当前定价
- 目标资产是指数、金融、地产、周期、资源、出口链、高估值成长股、AI capex 链、黄金、美债、美元或其他宏观敏感资产
- 市场正在交易 `soft landing`、`growth scare`、`reflation`、`stagflation`、`policy pivot`、`liquidity rally` 或 `AI productivity boom`
- 单看公司本体不足以解释估值倍数、行业轮动、资金流或风险溢价变化
- 需要判断新宏观数据或政策口径是否改变 thesis

## Selection Questions

判断是否启用 `supply-chain` overlay 时，至少回答：

- 这只票的收入驱动更受客户需求还是供给约束影响？
- 成本、产能、良率、交付、库存是否是核心变量？
- 单看公司本体是否不足以解释盈利弹性？
- 同层级可比公司是否能帮助验证份额变化或叙事真假？
- 顺着 upstream / downstream 继续挖，是否能显著提升研究质量？

判断是否启用 `macro` overlay 时，至少回答：

- 当前价格主要交易公司变量、行业变量、宏观变量，还是仓位/流动性变量？
- 哪个宏观变量的边际变化最可能改变 thesis？
- 宏观变量通过哪条链影响收入、利润率、估值、融资、仓位或催化剂？
- 市场已经 price in 的宏观路径是什么？
- 新数据或政策口径相对预期是 surprise 还是 confirmation？
- 如果宏观判断错了，最可能导致哪类投资误判？

## Usage Rule

启用 overlay 后，必须记录：

- `selected_overlays`
- `overlay_basis`
- `expected_incremental_insight`

如果启用 `macro` overlay，还必须记录：

- `macro_weight`
  one of `none`, `context`, `secondary`, `primary`
- `dominant_macro_variable`
- `dominant_macro_chain`
- `market_pricing`
- `what_is_already_priced`
- `macro_refresh_triggers`

如果不启用，也允许明确写：

- `selected_overlays: none`

## Primary Output

`supply-chain` overlay 通常应补充以下内容：

- upstream map
- downstream map
- same-layer peer set
- transmission logic
- what would falsify the chain

`macro` overlay 通常应补充以下内容：

- macro regime classification
- market-pricing map
- macro-to-asset transmission chain
- asset impact table
- refresh triggers
- falsification conditions

## Regime-Specific Notes

### With `large-mega`

常见用途：

- 从消费端和宏观需求看终端拉动
- 从核心供应链看哪些公司受益或受损
- 判断单一产品或周期变化对更大产业链的影响
- 用 `macro` overlay 判断实际利率、美元、流动性、财政、AI capex、机构配置和风险偏好是否主导估值倍数

这里更像在看：

- 宏观需求传导
- 大客户拉动
- 产业链利润分配
- 贴现率和配置权重

### With `micro-small`

常见用途：

- 从客户集中度判断收入确定性
- 从单一供应商、单一订单或单一产能约束判断脆弱点
- 从竞品和同层级公司看公司叙事是不是伪稀缺
- `macro` 通常只作为背景，除非融资环境、流动性或风险偏好直接影响融资生存性

这里更像在看：

- 收入确定性
- 成本弹性
- 生存性和兑现风险

### With `mid-cap`

常见用途：

- 用 `supply-chain` 判断景气和业绩兑现是否真实
- 用 `macro` 判断板块轮动来自行业 alpha，还是来自利率、信用、政策和风险偏好扩张
- 检查宏观变量是否改变估值修复空间、盈利 revision 或催化剂窗口
