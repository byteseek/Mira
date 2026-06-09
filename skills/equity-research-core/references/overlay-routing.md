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

### `market-structure-policy`

适用于以下情形：

- 研究对象上市地、主要交易地、资金通道、投资者结构或监管政策明显影响当前定价
- A 股、港股、中概 / ADR / H 股 / A+H 两地上市公司，或其他本地市场结构可能削弱通用估值锚的股票
- 政策、监管、减持 / 再融资、回购 / 分红、指数纳入、互联互通、外资风险偏好、南向 / 北向资金、ETF / 被动资金或本地散户主题交易可能主导价格
- 公司基本面结论与价格表现长期背离，需要解释“谁会买、为什么现在买、什么条件下重估”
- 治理、控股股东、国企 / 民企属性、关联交易、披露质量或会计可信度会改变 shareholder return、风险溢价或估值折价

### `flow-intent-inference`

适用于以下情形：

- 大单、异常期权、block trade、ATS / dark pool、龙虎榜、大宗交易、Form 4、13F、ETF / 指数资金流、short interest、borrow 或 open interest 变化成为研究问题本身
- 用户明确问“谁在买 / 卖”“这是 smart money 还是 hedge”“交易意图是什么”“这笔 flow 是否改变 thesis”
- 当前价格变化可能来自信息交易、对冲、dealer / gamma 机械流、指数 / ETF 被动流、融资 / 减持 / lock-up、short squeeze、liquidation 或流动性真空
- 基本面证据与价格反应不一致，需要判断可见 flow 是否只改变风险窗口 / refresh trigger，而不是改变 fundamental thesis

默认只作为 `market_pricing` 和 `weak_signal` 路径使用。除非有独立事实或事件证据确认，不得用它升级收入、利润率、现金流、产品、客户或 moat 结论。

### `options-flow-analysis`

适用于以下情形：

- 用户提供或引用系统性期权流数据，而不是单条 unusual-options alert
- 研究问题依赖 options volume、OI / OI change、IV、skew、term structure、gamma / pin risk、option-to-stock volume、event implied move 或期权成交分类
- 需要判断期权市场正在定价方向、波动、尾部风险、对冲、dealer 机械流、event lottery 还是 noise
- 需要用历史样本验证期权状态对 1d / 5d / 20d return、realized vol、IV crush、event gap、post-event drift 或 false positive rate 的解释力

如果期权数据是主要输入，优先用 `options-flow-analysis`；如果只是把期权作为可见 flow 的一类零散线索，再用 `flow-intent-inference`。

### `commodity`

适用于以下情形：

- 商品价格、库存、期货曲线、成本曲线、政策/地缘或贸易流明显影响收入、成本、利润率、FCF、资本开支、资产价值或风险溢价
- 目标资产是资源股、能源股、材料股、化工、航运、商品 ETF、商品期货或其他商品 beta 明显的资产
- 需要区分 `commodity beta` 与 `company alpha`
- 单看公司本体或泛宏观不足以解释盈利 revision、估值倍数、行业轮动或资金流
- 需要判断商品变化来自实物供需、库存、曲线、成本、政策/地缘、金融条件还是仓位 squeeze

### `strategic-catalyst`

适用于以下情形：

- 小盘股或事件驱动标的可能因为巨头合作、投资、并购、客户认证、独家授权、平台接入或供应链导入而重估
- 关键线索可能先出现在社交平台、行业聊天、异常量价、招聘、专利、会议纪要或非正式渠道
- 市场正在交易“谁会合作 / 谁会收购 / 谁会投资 / 谁会成为大客户”
- 单一战略关系足以改变收入确定性、融资能力、生存风险或估值锚
- 需要把已确认事实、媒体报道、社交信号和未确认传闻分层输出

### `valuation-expectation`

适用于以下情形：

- key debate 是估值是否已经反映质量、成长、风险或主题热度
- 用户问“是不是已经 price in”“有没有风险收益比”“能不能做”
- 需要把 thesis 写入 `thesis-ledger` 或 `actionability_bridge`
- 标的已有可用估值锚，或者必须明确估值锚不可用

### `top-bottom-risk`

适用于以下情形：

- 用户问是否顶部、底部、涨疯了、跌惨了、过热、拥挤、泡沫、capitulation 或“有问题吗”
- 标的、板块、行业或宏观资产刚经历大幅上涨 / 下跌，核心问题是风险状态而不是首次覆盖
- 基本面和价格都很强，但下一步需要判断是否已经进入 `fragile_upside` 或 `distribution_risk`
- 基本面和价格都很弱，但下一步需要判断是否进入 `capitulation_watch` 或 `base_building`
- 单看估值、技术面、宏观或供应链都不足以解释风险，因为价格、预期、仓位和事件路径必须同时看

### `technical-context`

适用于以下情形：

- 研究动作依赖当前市场定价、事件反应或 follow-through 质量
- thesis 更新需要把基本面证据与市场反应明确分开
- 标的处于高波动、拥挤仓位、低流动性或事件驱动跳空
- 用户问某只票现在能不能行动、观察、刷新还是降优先级

这是市场定价与风险上下文层，不用于证明基本面执行、需求、利润率、护城河或长期 thesis 持久性（见 [../../../memory/skills/technical-analysis.md](../../../memory/skills/technical-analysis.md)）。

可复现计算由 `tools/mira_data technical <ticker>`（stdlib、延迟 L5 日线）产出 trend / relative strength / volume / volatility / 关键位 / `technical_context_score`，自算指标进 calculation-ledger；options、short interest、intraday 无免费源，必须保持 `source_gap`，不得伪造。

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

判断是否启用 `market-structure-policy` overlay 时，至少回答：

- 这只股票的主要上市地、交易地和价格发现地在哪里？
- 当前价格设定者更像本地散户、公募 / 私募、外资、南向 / 北向、ETF / 被动资金、量化、产业资本、政策资金，还是混合？
- 市场正在交易公司基本面、行业景气、政策主题、资金流、风险溢价、治理折价，还是估值锚修复？
- 本地制度变量是否会改变供给、流动性、估值锚或 shareholder return，例如减持、再融资、限售、回购、分红、退市、指数纳入、互联互通资格或交易限制？
- 公司是否存在 A/H/ADR 多地上市、同股不同价、外资可达性或本地投资者偏好差异？
- 如果基本面判断正确但股票不重估，最可能卡在哪个市场结构变量？
- 下一步最直接的确认或证伪来源是什么：交易所数据、监管公告、持仓 / 资金流、公司治理动作、指数公告、回购 / 分红记录还是政策文件？

判断是否启用 `flow-intent-inference` overlay 时，至少回答：

- 可见 flow 是什么：股票大单、异常期权、block / ATS、龙虎榜、大宗交易、Form 4、13F、ETF / 指数、short / borrow 还是 open interest？
- 这个 flow 相对自身历史、ADV、OI、float、spread、event window 和同业是否真的异常？
- 是否能区分 opening / closing、方向、hedge leg、spread / roll、dealer inventory 或被动调仓？
- 可能的交易意图假设有哪些：信息交易、对冲、套利、被动流、融资 / 减持消化、short squeeze、liquidation、buyback / insider alignment 还是 routine compensation / tax / diversification？
- 最强机械解释是什么？如果机械解释成立，结论应如何降级？
- 这个 flow 影响的是 thesis 变量、催化剂、风险窗口、refresh trigger、evidence priority，还是只是噪音？
- 下一步最直接的确认或证伪来源是什么：OI 次日变化、filing、事件结果、重复 flow、borrow / short data、交易所公开信息、公司公告还是价格跟随失败？

判断是否启用 `options-flow-analysis` 时，至少回答：

- 是否有结构化期权流数据，而不是截图、社媒 alert 或单条成交？
- 数据质量层级是什么：timestamp、bid/ask、underlying price、OI、IV、Greeks、trade-side、opening / closing、multi-leg、corporate action 是否可用？
- 这笔大单是否应按 `prior_position_aware` 解读：买方/卖方是否可能已经有股票、期权、convertible、borrow、ETF / index 或 portfolio hedge 仓位？
- 如果像机构大单，是否应按 `rational_prior_position_enhancement` 解读：这笔交易是在增强、保护、重构、融资或变现一个此前理性建立的仓位吗？
- 这笔交易暗示的既有 thesis 或既有风险暴露是什么？
- 这笔交易更像新增方向暴露、对冲、roll、monetize、overwrite、融资、保护尾部、卖波动、转移风险，还是未知的边际调仓？
- 当前期权状态更像 `directional`、`volatility`、`skew_tail`、`dealer_mechanical`、`hedge`、`roll_or_spread`、`closing`、`retail_lottery`、`ambiguous` 还是 `noise`？
- OI 次日变化是否确认新仓，还是成交更可能是平仓、roll、spread、覆盖卖出或对冲？
- IV、skew、term structure、event implied move 和 realized vol 的关系是什么？
- gamma / expiry / pin risk 是否会改变短期价格弹性，而不是基本面预期？
- 历史验证中，相同状态对 return、realized vol、IV crush、event gap 或 false positive control 是否有增量？
- 它改变的是 risk window、refresh trigger、event delta、volatility expectation、evidence priority，还是不改变结论？

判断是否启用 `commodity` overlay 时，至少回答：

- 当前价格主要交易公司变量、商品变量、宏观变量，还是仓位/流动性变量？
- 商品价格通过哪条链影响收入、成本、利润率、FCF、资本开支、估值、融资或催化剂？
- 目标资产的 `commodity_beta` 是 `low`、`medium` 还是 `high`？
- 商品变化来自供需、库存、期货曲线、成本、政策/地缘、金融条件还是仓位 squeeze？
- 公司有多少暴露被 hedges、合同价、区域基差、成本通胀或项目执行抵消？
- 市场已经 price in 的商品路径是什么？
- 如果商品判断错了，最可能导致哪类投资误判？

判断是否启用 `strategic-catalyst` overlay 时，至少回答：

- 这条线索指向什么具体催化剂：合作、订单、认证、投资、并购、授权、平台接入还是供应链导入？
- 交易对手是否是巨头、核心客户、产业链关键节点或潜在收购方？
- 信息状态是 `confirmed`、`reported`、`social_signal` 还是 `unverified_rumor`？
- 如果线索成真，它改变的是收入、融资、生存性、估值锚、市场叙事还是控制权预期？
- 当前市场是否已经 price in，还是仍处于早期扩散？
- 下一步最直接的确认或证伪来源是什么？

判断是否启用 `valuation-expectation` overlay 时，至少回答：

- 当前 valuation anchor 是什么，质量是 `high`、`medium`、`low` 还是 `source_gap`？
- 市场价格已经隐含什么增长、利润率、现金流、风险溢价或催化剂预期？
- Mira 的 base/bull/bear 和市场预期差在哪里？
- 收益或风险来自 revenue revision、margin revision、cash flow revision、multiple rerating、risk premium change 还是 positioning unwind？
- 下行场景和证伪条件是什么？

判断是否启用 `top-bottom-risk` overlay 时，至少回答：

- 研究对象的基本面斜率是继续加速、正但放缓、稳定高位、恶化、混合还是 source-gapped？
- 当前价格隐含的 expectation burden 是 low、medium、high、extreme 还是 source_gap？
- 当前 move 更像 clean revision、crowded long、crowded short、squeeze / forced flow、liquidity gap 还是 source_gap？
- 好消息和坏消息的 reaction quality 如何，是否出现 good-news fade、bad-news absorbed 或 gap fill？
- 下一催化剂需要 upside surprise、confirmation、digest、reset 还是 capitulation？
- 输出应该是 `watch_only`、`valuation_reset_watch`、`risk_reduction_context`、`event_setup` 还是回到主框架？

判断是否启用 `technical-context` overlay 时，至少回答：

- 当前 trend、relative strength、volume 和 volatility 是确认还是否定最近的事件解读？
- 关键 `invalidation_level` 和 `trigger_level` 在哪里，价格相对它们处于什么位置？
- 这个 setup 改变了研究动作（行动 / 观察 / 刷新 / 降优先级），还是只是图形评论？
- 市场反应是否在用“好消息不涨 / 坏消息不跌”反驳基本面叙事？
- 哪些字段必须保持 `source_gap`（options / short interest / intraday），不能伪造？

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

如果启用 `market-structure-policy` overlay，还必须记录：

- `market_structure_weight`
  one of `none`, `context`, `secondary`, `primary`
- `primary_listing_and_price_discovery`
- `dominant_price_setter`
- `dominant_structure_variable`
  one of `policy_regulation`, `capital_flow`, `investor_base`, `index_passive_flow`, `liquidity_float`, `share_supply`, `governance_discount`, `listing_arbitrage`, `disclosure_quality`, `mixed`
- `market_access_and_flow_channels`
- `policy_or_regulatory_chain`
- `governance_and_shareholder_return_check`
- `valuation_anchor_impairment`
- `what_is_already_priced`
- `market_structure_refresh_triggers`

如果启用 `flow-intent-inference` overlay，还必须记录：

- `flow_intent_weight`
  one of `none`, `context`, `secondary`, `primary`
- `visible_flow_object`
  one of `stock_large_print`, `options_uoa`, `block_or_ats`, `insider_filing`, `13f_or_ownership`, `etf_or_index_flow`, `short_or_borrow`, `a_share_public_flow`, `hk_connect_or_ccass`, `mixed`
- `abnormality_basis`
- `possible_counterparties`
- `mechanical_explanations`
- `ranked_intent_hypotheses`
- `intent_confidence`
  one of `low`, `medium`, `high`
- `thesis_variable_affected`
- `what_would_confirm`
- `what_would_disconfirm`
- `flow_refresh_triggers`

如果启用 `options-flow-analysis`，还必须记录：

- `options_flow_weight`
  one of `none`, `context`, `secondary`, `primary`
- `options_data_quality_tier`
  one of `blocked`, `exploratory`, `usable`, `validated`
- `dominant_option_state`
  one of `directional`, `volatility`, `skew_tail`, `dealer_mechanical`, `hedge`, `roll_or_spread`, `closing`, `retail_lottery`, `ambiguous`, `noise`
- `opening_flow_confidence`
  one of `low`, `medium`, `high`
- `counterparty_assumption`
  one of `rational_prior_position_enhancement`, `prior_position_aware`, `blank_slate_directional`, `unknown`
- `prior_position_hypotheses`
- `prior_thesis_hypothesis`
- `enhancement_hypothesis`
- `marginal_action_hypothesis`
  one of `add_exposure`, `reduce_exposure`, `hedge`, `monetize`, `roll`, `finance`, `overwrite`, `tail_protect`, `volatility_trade`, `transfer_risk`, `unknown`
- `oi_confirmation`
- `iv_skew_term_structure_read`
- `gamma_or_expiry_mechanics`
- `historical_base_rate_ref`
- `thesis_variable_affected`
- `options_refresh_triggers`
- `blocked_use_cases`

如果启用 `commodity` overlay，还必须记录：

- `commodity_weight`
  one of `none`, `context`, `secondary`, `primary`
- `dominant_commodity_driver`
  one of `physical_balance`, `inventory_cycle`, `curve_structure`, `cost_curve`, `policy_geopolitics`, `financial_conditions`, `positioning`, `mixed`
- `commodity_transmission_chain`
- `market_pricing`
- `what_is_already_priced`
- `company_alpha_separation`
- `commodity_refresh_triggers`

如果启用 `strategic-catalyst` overlay，还必须记录：

- `catalyst_status`
  one of `confirmed`, `reported`, `social_signal`, `unverified_rumor`
- `counterparty_quality`
- `economic_materiality`
- `expected_timeline`
- `verification_path`
- `what_would_confirm`
- `what_would_disconfirm`
- `next_refresh_trigger`

如果启用 `valuation-expectation` overlay，还必须记录：

- `current_valuation`
- `historical_or_peer_range`
- `what_is_priced_in`
- `base_bull_bear`
- `revision_path`
- `valuation_anchor_quality`

如果启用 `top-bottom-risk` overlay，还必须记录：

- `risk_regime`
  one of `trend_confirmation`, `fragile_upside`, `distribution_risk`, `capitulation_watch`, `base_building`, `bear_trap_risk`, `no_clear_extreme`
- `fundamental_slope`
- `expectation_burden`
- `positioning_liquidity`
- `reaction_quality`
- `next_catalyst_burden`
- `research_action`
- `must_refresh_if`

如果启用 `technical-context` overlay，还必须记录：

- `technical_context_weight`
  one of `none`, `context`, `secondary`, `primary`
- `trend_state`
- `relative_strength_state`
- `volume_state`
- `volatility_state`
- `event_reaction_quality`
- `positioning_risk`
- `key_levels`
- `invalidation_level`
- `trigger_level`
- `technical_context_score`
- `evidence_limitations`
- `stale_after`
- `must_refresh_if`

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

`market-structure-policy` overlay 通常应补充以下内容：

- listing / trading venue map
- price discovery and investor-base map
- capital-flow channel check
- policy / regulatory transmission chain
- share supply, float, dilution, buyback and dividend check
- governance / controller / shareholder-return note
- valuation discount or premium explanation
- refresh triggers
- falsification conditions

`flow-intent-inference` overlay 通常应补充以下内容：

- visible-flow map
- abnormality and liquidity baseline
- possible counterparty map
- mechanical-explanation check
- ranked intent hypotheses
- thesis-variable impact
- confirmation / falsification path
- refresh triggers

`options-flow-analysis` 通常应补充以下内容：

- options data-quality gate
- options state map
- flow classification
- prior-position hypothesis map
- rational prior-position enhancement map
- marginal-action classification
- OI confirmation check
- IV / skew / term-structure map
- gamma / expiry mechanics note
- event-window or historical base-rate check
- false-positive downgrade
- refresh triggers

`commodity` overlay 通常应补充以下内容：

- commodity exposure map
- commodity transmission chain
- inventory and curve snapshot
- cost-curve / margin-sensitivity note
- hedging and contract adjustment
- market-pricing map
- refresh triggers
- falsification conditions

`strategic-catalyst` overlay 通常应补充以下内容：

- catalyst map
- counterparty map
- signal quality table
- market-pricing status
- confirmation path
- falsification conditions

`valuation-expectation` overlay 通常应补充以下内容：

- valuation snapshot
- base/bull/bear scenario table
- revision path
- downside path
- actionability bridge input

`top-bottom-risk` overlay 通常应补充以下内容：

- top / bottom risk check
- fundamental slope and expectation burden
- positioning / liquidity posture
- event reaction quality
- next catalyst burden
- research action and refresh trigger

`technical-context` overlay 通常应补充以下内容：

- trend / relative-strength / volume / volatility 状态
- event-reaction quality 和 follow-through
- key levels、trigger 和 invalidation
- positioning / crowding 检查（无免费源时为 `source_gap`）
- `technical_context_score` 和刷新条件

## Regime-Specific Notes

### With `large-mega`

常见用途：

- 从消费端和宏观需求看终端拉动
- 从核心供应链看哪些公司受益或受损
- 判断单一产品或周期变化对更大产业链的影响
- 用 `macro` overlay 判断实际利率、美元、流动性、财政、AI capex、机构配置和风险偏好是否主导估值倍数
- 用 `market-structure-policy` 判断指数权重、外资配置、本地政策、回购分红、国企 / 民企属性和治理折价是否主导估值倍数
- 用 `options-flow-analysis` 判断系统性期权流是否改变 event-risk、volatility、gamma、skew 或 refresh priority
- 用 `flow-intent-inference` 判断大额期权、block、13F / Form 4、buyback、被动资金或 short / borrow 是否只改变风险窗口与刷新优先级，而不是改变基本面结论
- 用 `commodity` overlay 判断资源、能源、材料或化工大票的商品 beta 是否主导盈利 revision

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
- 用 `strategic-catalyst` 捕捉巨头合作、投资、并购、客户认证和供应链导入的早期 alpha 线索
- 用 `options-flow-analysis` 判断小票期权异动是否只是 event lottery、retail flow、short squeeze 或 dealer 机械流
- 用 `flow-intent-inference` 捕捉异常量价、期权、Form 4、融资 / 减持、lock-up、short squeeze 或 liquidation 对催化剂窗口和生存性风险的影响
- `macro` 通常只作为背景，除非融资环境、流动性或风险偏好直接影响融资生存性
- `market-structure-policy` 用于检查流通盘、限售 / 减持、再融资、壳价值、交易制度、政策题材和监管风险是否比公司经营更能解释价格
- `commodity` 通常只作为 secondary 或 context，除非单一资源项目、矿权、offtake 或商品价格直接决定生存性

这里更像在看：

- 收入确定性
- 成本弹性
- 生存性和兑现风险
- 战略关系是否能重写估值锚

### With `mid-cap`

常见用途：

- 用 `supply-chain` 判断景气和业绩兑现是否真实
- 用 `macro` 判断板块轮动来自行业 alpha，还是来自利率、信用、政策和风险偏好扩张
- 用 `market-structure-policy` 判断板块轮动来自真实盈利 revision，还是来自政策主题、资金流、互联互通、指数 / ETF、再融资 / 减持或治理折价修复
- 用 `options-flow-analysis` 判断期权市场在交易方向、波动、skew、gamma、event-risk 还是噪音
- 用 `flow-intent-inference` 判断板块或单票异动来自信息流、对冲、被动资金、期权 / dealer 机械流、融资供给还是仓位 unwind
- 检查宏观变量是否改变估值修复空间、盈利 revision 或催化剂窗口
- 用 `commodity` 判断商品 beta、成本曲线位置、项目弹性、hedges 和区域基差是否改变盈利 revision

## Market-Specific Defaults

### A 股

默认先运行 `market-structure-policy` gate。若无明显触发，可记录为 `market_structure_weight: context`；若政策、主题、资金流、限售 / 减持、再融资、国企改革、指数 / ETF 或交易制度正在主导价格，升为 `secondary` 或 `primary`。

常见检查重点：

- 政策主题与监管窗口
- 本地散户、公募、量化、ETF、北向和产业资本的价格设定权
- 限售、减持、再融资、股权质押、回购和分红
- 国企 / 民企属性、控股股东和关联交易
- 披露质量、会计质量和产业数据可验证性
- 估值锚是否被主题拥挤、风险偏好或政策溢价削弱

### 港股

默认先运行 `market-structure-policy` gate。若基本面便宜但缺少重估买家，至少记录为 `market_structure_weight: secondary`；若中国政策、外资配置、美元 / HKD 流动性、南向资金、地缘风险、治理折价或回购分红主导定价，升为 `primary`。

常见检查重点：

- 中国基本面与离岸风险溢价的分离
- 外资、南向、ETF / 被动资金和本地资金的边际买盘
- A/H/ADR 多地上市、同股不同价和价格发现地
- 回购、分红、控股股东、治理和关联交易
- 美元 / HKD 流动性、港股市场成交和风险偏好
- “便宜但不重估”的触发条件与证伪条件

### 其他国际市场

美股、日股、韩股、台股和欧股不默认升为 `secondary`，但如果交易制度、外资可达性、财阀 / 控股结构、治理改革、指数纳入、货币流动性或政策补贴显著主导价格，应启用 `market-structure-policy`。
