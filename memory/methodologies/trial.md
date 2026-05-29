# Methodology Queue: Trial

- last_updated: 2026-05-29

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
  expected_increment: 把长期倍数股研究从“好公司/大故事”改成目标收益路径、right to win、再投资 runway、稀释/生存性、证据阶梯和 kill criteria 的组合判断。
  falsification_condition: 如果它不能比普通 `long_term_thesis` 更早暴露失败样本风险，或无法形成明确的 return-path math 与退出条件，就不升级到 `adopted`。

- `institutional-thesis-system`
  target_case: `AAPL thesis ledger`, `CRWV event delta`, `WOLF expectation map`, and next live earnings event
  expected_increment: 把一次性 research package 升级为可维护的 thesis ledger、expectation map、event delta、decision log 和 postmortem，让新增信息能明确映射到预期变量和 thesis state。
  falsification_condition: 如果它不能比普通 memo 更清楚地区分预期差、证据强度、状态变化和复盘结论，或维护成本明显拖慢研究，就不升级到 `adopted`。
