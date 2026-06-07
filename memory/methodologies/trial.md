# Methodology Queue: Trial

- last_updated: 2026-06-07

## Purpose

记录准备在真实案例里验证的方法。

## Entry Format

- `method_name`
- `target_case`
- `expected_increment`
- `falsification_condition`

## Current Items

- `framework-routing`
  target_case: `3-5 single-equity cases across micro-small, mid-cap, and large-mega`
  expected_increment: 根据主导定价变量选择研究框架，避免所有股票套同一模板。
  falsification_condition: 如果它不能减少框架错配，或只是增加路由字段而不改善结论质量，就不升级到 `adopted`。

- `supply-chain`
  target_case: `AI hardware`, `customer-concentrated small caps`, and `industrial component cases`
  expected_increment: 用上下游和同层级证据验证需求、客户集中度、收入确定性和竞争替代，而不是只听公司口径。
  falsification_condition: 如果它不能比普通公司披露带来增量验证，或无法稳定区分行业 beta 与公司 alpha，就不升级到 `adopted`。

- `llm-claim-classification`
  target_case: `earnings package`, `standard equity research package`, and `monitoring update`
  expected_increment: 把来源中的具体信息拆成事实、公司口径、承诺、指引、目标、预测、假设、观点、市场定价和弱信号，减少把不同性质信息混写成结论。
  falsification_condition: 如果 claim 分类不能改善 evidence quality、refresh trigger 和 fact-vs-inference 边界，或显著拖慢研究流程，就不升级到 `adopted`。

- `channel-check-scuttlebutt`
  target_case: `AAPL-like large-mega with supply-chain overlay` and `customer-concentrated micro-small`
  expected_increment: 用一线渠道、客户、供应商和竞品反馈去验证需求、库存、切换成本和竞争位置，而不是只看公司口径。
  falsification_condition: 如果 primary research 不能提供超出公开披露的有效增量，或大部分反馈无法交叉验证，就不升级到 `adopted`。

- `variant-perception`
  target_case: `AAPL large-mega` and `HIMS mid-cap`
  expected_increment: 强制研究先写出 consensus proxy、真正分歧点和价格重估路径，避免把公司分析误当成投资机会分析。
  falsification_condition: 如果它不能稳定提升 thesis 的可交易性、催化剂定义和失效条件清晰度，就不升级到 `adopted`。

- `industry-concept-analysis`
  target_case: `GPU`, `ABF`, `HBM`, `存储`
  expected_increment: 把模糊产业概念拆成概念边界、产业链地图、供需/定价/放量机制、利润池排序和候选标的池，帮助更快进入单票研究。
  falsification_condition: 如果它不能比普通主题搜索更快定位关键瓶颈、利润池和标的候选，或核心判断无法回溯到来源，就不升级到 `adopted`。

- `macro-regime-analysis`
  target_case: `AI high-duration / AI capex`, `banks / real estate`, `cyclical / commodity`, `gold / Treasury-sensitive assets`, and `export chain`
  expected_increment: 把增长、通胀、政策、利率、美元、信用、流动性和风险偏好转成 market pricing 与 macro-to-asset transmission chain，避免宏观分析停留在背景介绍。
  falsification_condition: 如果它不能稳定提升 thesis 的解释力、refresh trigger 和 falsification condition，或经常把公司/行业主导问题误判成宏观主导，就不升级到 `adopted`。

- `commodity-cycle-analysis`
  target_case: `crude oil / oil equities`, `copper / miners`, `gold / gold miners`, and optional `lithium / battery materials`
  expected_increment: 把商品研究从泛宏观或单纯价格图，拆成供需平衡、库存、期货曲线、成本曲线、政策/地缘、仓位和资产传导，区分 commodity beta 与 company alpha。
  falsification_condition: 如果它只是重复 `macro-regime-analysis`，不能稳定区分库存/曲线紧张与长期供需变化，或无法改善资源股、商品 ETF 和商品本身的刷新条件，就不升级到 `adopted`。

- `macro-data-release-triage`
  target_case: `PPI/CPI/PCE`, `NFP`, `ISM/PMI`, `retail sales`, and `FOMC-adjacent data`
  expected_increment: 把单次宏观数据发布拆成 headline surprise、子项目定位、历史类比、上游条件、市场定价和后续刷新触发，避免只用 headline 解释行情。
  falsification_condition: 如果它不能稳定区分一次性噪音与可持续传导，或只是重复 `macro-regime-analysis`，就不升级到 `adopted`。

- `etf-listing-analysis`
  target_case: `new thematic ETF`, `crypto/commodity ETF`, `covered-call/buffer ETF`, and `single-stock/leveraged ETF`
  expected_increment: 把 ETF 新上市拆成发行意图、结构与可达性、持仓暴露地图、管理/权重机制和上市后跟踪，用于识别真实配置趋势、交易工具需求、资产可达性变化和主题尾声包装。
  falsification_condition: 如果它不能稳定区分真实新增需求与同类产品迁移，或经常把发行人营销噪音误判成投资信号，就不升级到 `adopted`。

- `etf-listing-discovery`
  target_case: `monthly US new ETF discovery run`
  expected_increment: 把交易所、发行人、监管文件、ETF 行业媒体和市场数据统一成结构化新 ETF watchlist，给 ETF 上市分析提供候选池。
  falsification_condition: 如果经常漏掉交易所已确认的新 ETF，或把 filed/announced/dual listing 误判成 listed，就不升级到 `adopted`。

- `thesis-horizon-routing`
  target_case: `3-5 earnings cases` and `2 first-coverage company cases`
  expected_increment: 强制区分短期财报影响、FY1/FY2 盈利修正、一年以上长期 thesis 和短期证据触发的 regime transition，避免把单季财报自动外推成长逻辑。
  falsification_condition: 如果它只增加模板字段，不能改善证据权重、thesis impact、refresh trigger 和 falsification condition，就不升级到 `adopted`。

- `analysis-routing`
  target_case: `single-equity`, `earnings-event`, `industry-concept`, `macro-regime`, `ETF`, and `methodology` requests
  expected_increment: 先判断任务入口、研究对象、时间边界、应使用的 loop / skill 和输出包，避免把所有请求都误塞进单票 framework routing。
  falsification_condition: 如果它没有减少入口错配，或让简单任务明显变慢，就不升级到 `adopted`。

- `long-term-multibagger-research`
  target_case: `2-3 historical 10x/100x or failed-growth cases` and `2 live long-term candidate equities`
  expected_increment: 把长期倍数股研究从“好公司/大故事”改成目标收益路径、5 年收入测试、10 年终局、5x upside path、market misunderstanding、culture/adaptability、right to win、再投资 runway、稀释/生存性、证据阶梯、missed-winner risk 和 kill criteria 的组合判断。
  falsification_condition: 如果它不能比普通 `long_term_thesis` 更早暴露失败样本风险，不能稳定写出市场误解变量和重定价证据，或无法形成明确的 return-path math 与退出条件，就不升级到 `adopted`。

- `institutional-thesis-system`
  target_case: `AAPL thesis ledger`, `CRWV event delta`, `WOLF expectation map`, and next live earnings event
  expected_increment: 把一次性 research package 升级为可维护的 thesis ledger、expectation map、event delta、decision log 和 postmortem，让新增信息能明确映射到预期变量和 thesis state。
  falsification_condition: 如果它不能比普通 memo 更清楚地区分预期差、证据强度、状态变化和复盘结论，或维护成本明显拖慢研究，就不升级到 `adopted`。

- `long-term-integrated-thesis`
  target_case: `AAPL-like mega-cap platform`, `consumer/product-led mid-cap`, `failed growth story`, and `macro-sensitive cyclical or financial company`
  expected_increment: 把长期研究从单一好故事拆成 `consumer_demand`、`product_reality`、`macro_economy`、`industry_structure`、`company_execution` 和 `valuation_expectations` 六个互相校验的 lens，强制写出最弱假设、市场隐含预期、刷新触发和证伪条件。
  falsification_condition: 如果它不能比普通 `long_term_thesis` 更早暴露 demand/product/industry/company/valuation 冲突，或只是增加模板字段而不改变结论质量，就不升级到 `adopted`。
  notes: 初始方法论包见 `cases/long-term-methodology-2026-05-30/`。当前已完成 ETN、VRT、CRM、LLY 四个 live/contrast/dry-run trials，以及 TDOC、PTON 两个 historical failure backtests；candidate public workflow pack 已存在并在 LLY 做过 fresh-case dry run。仍需 true follow-through refresh、独立 reviewer dry run、完整 public-grade expectation map 和历史案例 source cleanup 后才能考虑升级。

- `market-structure-policy`
  target_case: `2 Hong Kong cheap-but-no-rerating cases`, `2 A-share policy/flow/share-supply cases`, `1 A/H or ADR dual-listing case`, and `1 Japan/Korea/Taiwan/Europe control case`
  expected_increment: 把上市地、价格发现地、投资者结构、资金通道、政策监管、治理折价、share supply 和估值锚有效性显式纳入 overlay，避免把美股式公司 / valuation / revision 框架无差别套到 A 股和港股。
  falsification_condition: 如果它不能改变 dominant price setter、估值锚质量、证据优先级、刷新条件或结论降级，或经常把政策 / 流量叙事事后包装成解释，就不升级到 `adopted`。
  notes: 方法论卡见 `memory/methodologies/market-structure-policy.md`，填写模板见 `templates/market-structure-policy-check.csv`。A 股和港股先作为 mandatory gate，其他国际市场按触发条件启用。

- `institutional-research-quality-gate`
  target_case: `next 3-5 formal Mira outputs with thesis-level judgments`
  expected_increment: 用四问压缩质量控制：现实依据、一阶变量、决策增量、可被打脸。目标是减少低质量结论和背景堆砌，而不是增加新流程。
  falsification_condition: 如果它只是重复 delivery checklist、让简单任务变慢，或不能在至少两个真实 case 中改善结论降级/刷新条件/一阶变量清晰度，就不升级到 `adopted`。

- `roadmap-to-bottleneck-recursion`
  target_case: `CPO / silicon photonics`, `AI power / grid bottleneck`, and one historical failed-bottleneck backtest
  expected_increment: 从已确认路线图出发，沿物理、工艺、材料、产能、认证和集成约束递归上游，找到比普通产业链图更窄、更可验证、更可映射到股票代理的下一层瓶颈。
  falsification_condition: 如果它不能比普通 `industry-concept-analysis` 和 `supply-chain` 更好地改变瓶颈排序、公司 handoff、source-gap map 或 refresh trigger，或反复把技术节点误判成可投资价值捕获，就不升级到 `adopted`。

- `technical-market-pricing-context`
  target_case: `2 earnings/event cases`, `1 failed-breakout or failed-breakdown monitoring case`, `1 high-volatility / high-short-interest case`, and `1 ETF or product-liquidity case`
  expected_increment: 把技术面从主观图形评论升级为可复现的 market-pricing 层，记录趋势、相对强弱、量能、事件反应、波动、期权/空头/流动性和触发/失效位，用来改善 actionability、refresh trigger 和风险窗口。
  falsification_condition: 如果它只是增加描述性 K 线语言，不能改变研究动作、刷新条件或风险判断，或经常把价格反应误写成基本面验证，就不升级到 `adopted`。
  notes: 方法论卡见 `memory/methodologies/technical-market-pricing-context.md`，填写模板见 `templates/technical-analysis-check.csv`。

- `flow-intent-inference`
  target_case: `1 isolated unusual-options clue without full dataset support`, `1 block trade / secondary / lock-up case`, `1 Form 4 insider cluster`, `1 A-share / HK public-flow disclosure case`, and `1 false-positive visible-flow case`
  expected_increment: 把大单、零散异常期权、block / ATS、龙虎榜、大宗交易、Form 4、13F、ETF / 指数、short / borrow 从“smart money 叙事”降级为可验证的 counterparty-intent hypothesis，改善 evidence priority、risk window、refresh trigger 和 false-positive control。
  falsification_condition: 如果它只能产出合理故事，不能区分信息交易、对冲、被动流、dealer / gamma 机械流、融资供给或 routine filing，或经常把 market-pricing 证据误写成基本面验证，就不升级到 `adopted`。
  notes: 方法论卡见 `memory/methodologies/flow-intent-inference.md`，填写模板见 `templates/flow-intent-inference-check.csv`。

- `options-flow-analysis`
  target_case: `user options-flow dataset quality audit`, `pre-earnings / event-window validation`, `non-event directional-flow validation`, `volatility / skew / gamma state validation`, and `false-positive high-options-activity cases`
  expected_increment: 把系统性期权流从 UOA 叙事升级为可回测的 market-pricing framework，默认按 `rational_prior_position_enhancement` 分析机构级大单，先重构此前理性既有仓位和既有 thesis，再判断新交易是增强、保护、重构、融资、变现还是新增暴露，用历史样本改善 risk window、refresh trigger、event delta 和 false-positive control。
  falsification_condition: 如果数据质量不足、classification 需要未来信息、不能稳定区分新仓/平仓/spread/roll/hedge，或回测不能优于简单 event calendar / stock volume / IV rank baseline，就不升级到 `adopted`。
  notes: 方法论卡见 `memory/methodologies/options-flow-analysis.md`，填写模板见 `templates/options-flow-analysis-check.csv` 和 `templates/options-flow-data-quality-check.csv`。

- `top-bottom-risk-overlay`
  target_case: `AI semis / opticals / memory 2026`, `CPO optical suppliers`, `commodity squeeze`, `macro index drawdown`, `failed growth top`, and `capitulation bottom`
  expected_increment: 把“顶部 / 底部 / 过热 / 洗出”问题拆成 fundamental_slope、expectation_burden、positioning_liquidity、reaction_quality 和 next_catalyst_burden，避免把强基本面误判成好风险收益，或把大跌误判成底部。
  falsification_condition: 如果它只是重复 valuation / technical / macro 检查，不能改变 action label、refresh trigger 或 evidence gap，或系统性过早叫顶 / 抄底，就不升级到 `adopted`。
  notes: 方法论卡见 `memory/methodologies/top-bottom-risk-overlay.md`，填写模板见 `templates/top-bottom-risk-check.csv`。

- `autoresearch-agent-loop`
  target_case: `one methodology-card upgrade`, `one long-form research package`, and `one quant or evidence-classification experiment`
  expected_increment: 把可复用研究产物从一次性 drafting 升级为有 baseline、冻结评价指标、iteration log、rollback rule 和 reviewer-routing 的受控改进循环。
  falsification_condition: 如果它只是增加流程负担、诱发 metric hacking / self-review inflation，或不能比一次认真人工修订更好地改善 evidence quality、source coverage、unsupported-claim count 和 refresh conditions，就不升级到 `adopted`。
  notes: 方法论卡见 `memory/methodologies/autoresearch-agent-loop.md`，搜索日志见 `memory/methodologies/autoresearch-agent-loop-search-log.csv`。
