# Methodology Queue: Trial

- last_updated: 2026-05-18

## Purpose

记录准备在真实案例里验证的方法。

## Entry Format

- `method_name`
- `target_case`
- `expected_increment`
- `falsification_condition`

## Current Items

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
