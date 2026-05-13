# Methodology Card: Macro Data Release Triage

- status: trial
- role: playbook / macro-overlay input layer
- last_updated: 2026-05-13
- source_bucket: mixed (`institutional`, `official`, `practitioner`, `derived_internal`, `reverse_engineered`)
- source_quality: medium-high
- credibility_score: medium-high
- credibility_basis: 官方数据发布本身天然按 headline、core、component 和 special grouping 组织；央行和机构框架长期把通胀、增长、金融条件和市场预期结合起来看；本方法的增量来自把单次数据发布拆成可复现的定位、类比、传导和刷新触发流程。
- search_coverage: medium
- search_gaps: 还缺更多 buy-side 实盘 desk notes、中文宏观卖方模板、失败案例复盘，以及对 CPI/PPI/NFP/retail sales/ISM 以外数据的跨品类验证。
- comparison_baseline: `macro-regime-analysis`
- empirical_validation_mode: live trial + forward watch
- follow_through_plan: 先用 PPI/CPI/NFP/FOMC/retail sales/ISM 的实际发布做 6-10 次试跑，验证是否能更快定位 surprise、区分噪音与二轮传导、并定义清楚刷新条件。

## Core Idea

`macro-data-release-triage` 用于分析单次宏观数据发布。

它不是完整宏观 regime 框架，而是进入 `macro-regime-analysis` 之前的输入层。核心流程是：

1. 从 headline 到子项目定位具体问题。
2. 判断 surprise 来自 level、change、revision、breadth 还是 composition。
3. 与历史相似阶段类比，但必须写出相似点和不同点。
4. 推演数据继续恶化或转好的上游条件。
5. 映射到市场已经 price in 的路径和资产传导链。
6. 写出 `stale_after` 与 `must_refresh_if`。

## Reverse-Engineered From

- BLS PPI/CPI 发布稿的结构：headline、core、goods/services、food/energy、trade services、transportation、intermediate demand 等分层。
- Federal Reserve 的政策框架：通胀、就业、金融条件和风险是否改变政策反应函数。
- IMF/BIS/J.P. Morgan/BlackRock 等宏观框架：把增长、通胀、政策、金融条件、地缘和市场定价放在同一张 regime map 里。
- Mira 对 2026-05 美国 PPI 的实战拆解：先定位能源、运输仓储、贸易利润率和中间需求，再类比 2021-2022 成本推动再通胀，最后推演油价、霍尔木兹、CPI/PCE、就业和企业利润率的刷新条件。

## Search Paths Used

- 方法名/功能搜索
  `macro data surprise framework`, `economic data release market reaction components`, `inflation data subcomponents market pricing`
- 官方来源搜索
  `BLS PPI final demand intermediate demand components`, `Federal Reserve Monetary Policy Report inflation financial conditions`, `IMF WEO oil price inflation risks`, `BIS financial conditions macro shocks`
- 机构/实务搜索
  `J.P. Morgan Guide to the Markets inflation rates asset allocation`, `BlackRock macro regime investment outlook`, `economic surprise index methodology`
- 反面问题搜索
  `already priced in macro data`, `macro data revisions market reaction`, `headline inflation noise core components`
- 内部反推
  `macro-regime-analysis`, `macro-overlay`, `fomc-language-decoder`, `PPI 2026-05 conversation`

## Use When

- 用户问“最新 CPI/PPI/NFP/ISM/retail sales/GDP 怎么了”。
- 单次数据可能改变通胀、增长、政策、流动性、信用或风险偏好判断。
- 需要判断市场短期反应是否只是第一轮冲击，还是会影响中期 thesis。
- 数据内部结构明显分化，headline 不足以解释资产价格。
- 需要把宏观事件转成后续 watchlist。

## Avoid When

- 用户只需要查一个数字或发布时间。
- 数据本身不是市场主导变量，或目标资产对该数据传导很弱。
- 没有官方数据表和市场预期基准，无法判断 surprise。
- 历史类比只有标签相似，缺乏传导链相似。

## Applies To

- inflation releases: CPI、PPI、PCE、wage data、import/export prices
- growth releases: GDP、retail sales、industrial production、PMI/ISM
- labor releases: payrolls、unemployment、participation、wages、hours
- policy events: FOMC、Treasury refunding、fiscal package
- commodity/geopolitical macro shocks: oil、gas、shipping lanes、sanctions

## Core Question

这次数据发布的 surprise 到底在哪里，它是否改变市场定价的宏观路径、政策反应函数或资产传导链？

## Required Inputs

- official_release
  官方新闻稿、表格、历史修正说明和系列定义。
- consensus_or_market_pricing
  经济学家预期、Fed funds futures、收益率、通胀 breakeven、美元、油价、信用利差、指数/行业反应。
- component_breakdown
  headline、core、主要分项、权重/贡献、扩散度、修正项。
- historical_context
  同类数据的历史分位、上次类似组合、当时政策和市场背景。
- upstream_conditions
  能源、运费、工资、租金、库存、信贷、地缘、财政、汇率、供应链。
- transmission_target
  目标资产或市场需要被影响的路径：盈利、利润率、贴现率、风险溢价、仓位或流动性。

## Primary Signal

主信号不是 headline 好坏，而是：

- surprise 是否集中在高噪音项目，还是扩散到核心与粘性项目。
- 子项是否有二轮传导风险。
- 历史类比是否对应相同的上游条件和政策环境。
- 市场是否已经 price in 这条路径。
- 后续数据需要什么条件才能确认或证伪。

## Why It Works

宏观数据影响市场时，通常不是因为单个数字本身，而是因为它改变了投资者对未来路径的条件概率。

把数据拆成子项目可以区分：

- 一次性噪音 vs 持续压力。
- headline shock vs core trend。
- level problem vs acceleration problem。
- 价格冲击 vs 数量/需求冲击。
- 数据事实 vs 市场 surprise。

历史类比只有在传导链相似时才有用；上游条件和刷新触发能防止分析退化成事后叙事。

## Failure Mode

- 过度解读一个月数据。
- 用 headline 替代子项和贡献分析。
- 找一个历史年份贴标签，但忽略政策、估值、仓位和资产负债表背景不同。
- 只判断“利好/利空”，不写市场已经 price in 什么。
- 没有后续刷新条件，导致观点无法被证伪。
- 把官方事实、机构解释和 Mira 推断混在一起。

## Evidence Cost

medium

快速版只需要官方 release、市场预期和关键资产价格。完整版本需要历史序列、分项贡献、机构解释、市场定价和上游变量跟踪。

## Speed Vs Depth

- `speed`
  10-20 分钟内完成：headline surprise、top components、market pricing、one-line implication、must_refresh_if。
- `depth`
  1-2 小时完成：完整分项、历史类比、传导链、资产影响表、机构分歧、watchlist。

## Comparison To Existing Methods

相对 `macro-regime-analysis`：

- `macro-regime-analysis` 回答“当前宏观状态是否改变资产定价链”。
- `macro-data-release-triage` 回答“单次数据发布里到底哪里变了，是否足以进入宏观 regime 或资产 thesis”。

它应该作为 `macro-regime-analysis` 的前置 playbook，而不是替代它。

相对 `fomc-language-decoder`：

- `fomc-language-decoder` 解读政策语言和点阵图。
- `macro-data-release-triage` 解读经济数据和分项传导。

## Follow-Through Criteria

- 是否能比 headline commentary 更快定位真正问题项。
- 是否能区分一次性噪音和可持续传导。
- 是否能明确市场已计价路径和剩余尾部风险。
- 是否能形成后续 watchlist，而不是只解释当天行情。
- 是否能在不同数据类型上复用。

## Trial Design

首批试跑：

- `PPI 2026-05`
  验证能源、运输仓储、贸易利润率和中间需求的再通胀传导判断。
- `CPI/PCE follow-through`
  验证 PPI 问题项是否进入消费者价格或核心服务。
- `NFP`
  验证就业 surprise 是 payroll level、revision、wage、hours、participation 还是 sector breadth。
- `ISM / PMI`
  验证 growth scare 或 reflation 是订单、价格、就业、库存还是供应商交付驱动。
- `FOMC`
  与 `fomc-language-decoder` 联用，验证数据是否改变政策反应函数。

## Falsification Conditions

- 如果 6-10 次试跑后，它只是重复 `macro-regime-analysis`，不保留独立方法卡。
- 如果无法稳定写出 component problem、historical analogue 和 upstream conditions，降级为普通 checklist。
- 如果经常把单月噪音误判为 regime change，收紧使用条件。
- 如果不能提升 `must_refresh_if` 的清晰度，不升级到 `adopted`。

## Adoption Decision

当前判断：`trial`

原因：

- 与机构/实务分析习惯一致：先看 surprise 和 composition，再看历史、传导和市场定价。
- 与 Mira 现有宏观 overlay 互补，填补了“单次数据发布如何拆解”的空白。
- 但需要多个真实数据发布验证，尤其要防止过度解读单月数据。

## Source Notes

- BLS Producer Price Index release structure and final demand / intermediate demand breakdown: https://www.bls.gov/news.release/ppi.htm
- BLS CPI release structure and major component breakdown: https://www.bls.gov/news.release/cpi.nr0.htm
- Federal Reserve Monetary Policy Report framing for inflation, labor markets, financial conditions and policy reaction: https://www.federalreserve.gov/monetarypolicy/mpr_default.htm
- IMF World Economic Outlook risk scenario framing for inflation, oil, growth and policy: https://www.imf.org/en/publications/weo
- BIS work on financial conditions and macro-financial transmission: https://www.bis.org/publ/arpdf/ar2025e2.htm
- J.P. Morgan Asset Management Guide to the Markets as institutional macro chartbook pattern: https://am.jpmorgan.com/wr/en/asset-management/liq/insights/market-insights/guide-to-the-markets/
- BlackRock Investment Institute outlook as asset-manager macro regime and asset-allocation pattern: https://www.blackrock.com/americas-offshore/insights/blackrock-investment-institute/global-macro-outlook
