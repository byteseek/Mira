# Methodology Card: Macro Regime Analysis

- status: trial
- role: overlay / framework-lens
- last_updated: 2026-05-09
- source_bucket: mixed (`institutional`, `practitioner`, `first_principles`, `derived_internal`)
- source_quality: medium-high
- credibility_score: medium-high
- credibility_basis: T0/T1 机构、央行/国际组织和市场实务都长期使用增长、通胀、政策、金融条件、信用和风险偏好来解释资产定价；但宏观分析容易退化成事后叙事，必须通过 market pricing 和 transmission chain 约束。
- search_coverage: medium
- search_gaps: 还缺中文 buy-side 实操写法、更多失败案例、跨资产高频 positioning 数据源、以及 A 股本地宏观变量传导验证。
- comparison_baseline: `equity-research-core without explicit macro overlay`
- empirical_validation_mode: trial -> case backtest + forward watch + live case trial
- follow_through_plan: 用指数、高估值成长股、银行/地产、周期资源、黄金/美债敏感资产和出口链案例验证宏观 overlay 是否提高 thesis 的解释力、刷新条件和可交易性。

## Core Idea

`macro-regime-analysis` 的核心不是判断经济好坏，而是判断宏观变量是否正在改变资产定价链。

Mira 里的宏观分析必须先回答：

- 市场已经 price in 什么宏观路径？
- 哪个宏观变量的边际变化会改变资产定价？
- 它通过哪条链传导到收入、利润率、贴现率、风险溢价、流动性或仓位？
- 如果宏观判断错了，最可能错在哪里？

## Reverse-Engineered From

- J.P. Morgan Asset Management `Guide to the Markets` 这类以图表组织增长、通胀、利率、美元、估值和资产配置的机构框架。
- BIS 对 financial conditions、跨境资本、NBFI、FX swaps 和风险溢价传导的宏观金融分析。
- IMF World Economic Outlook 对增长、通胀、财政、地缘风险和金融市场稳定的情景化写法。
- Federal Reserve Monetary Policy Report 对增长、通胀、劳动力、金融条件、信用和金融稳定的政策框架。
- Goldman Sachs Research 对 GDP、通胀、劳动力、财政、金融条件和 consensus 差异的 forecast-to-market 写法。
- BlackRock Investment Institute 对 macro regime、mega forces、AI capex、leverage 和资产配置含义的写法。
- Mira 现有 `framework-routing` 里对 `macro_sensitivity`、机构配置和宏观贴现的要求。

## Search Paths Used

- 方法名搜索
  `macro regime framework`, `financial conditions macro framework`, `market pricing macro regime`
- 机构搜索
  `J.P. Morgan Guide to the Markets`, `BIS financial conditions`, `IMF World Economic Outlook`, `Federal Reserve Monetary Policy Report`, `Goldman Sachs macro outlook`, `BlackRock Investment Institute outlook`
- 功能描述搜索
  `how macro affects equity valuation`, `growth inflation policy rates equity transmission`, `financial conditions risk assets`
- 反面问题搜索
  `macro forecasts fail investing`, `why macro analysis is not actionable`, `already priced in macro data`
- 内部方法搜索
  `framework-routing macro_sensitivity`, `variant perception consensus proxy`, `supply-chain overlay transmission`

## Use When

- 资产价格由利率、实际利率、美元、信用、流动性、通胀、增长或风险偏好解释力很强。
- 研究对象是指数、周期、金融、地产、资源、出口链、高估值成长股、AI capex 链、黄金、美债或美元敏感资产。
- 研究需要判断宏观数据、政策路径或金融条件是否改变 thesis。
- 公司层面信息不足以解释价格，需要回答市场到底在交易哪条宏观路径。

## Avoid When

- 单一公司事件、融资、生存性或监管审批才是主导变量。
- 宏观变量无法落到明确传导链。
- 市场预期无法被刻画，只能写“宏观利好/利空”。
- 研究者想用宏观故事替代公司和行业研究。

## Applies To

- `large-mega`
  高适配，尤其是受实际利率、机构配置、全球增长、美元和主题 capex 影响的大票。
- `mid-cap`
  中高适配，尤其是板块轮动、行业 beta、信用条件和风险偏好主导时。
- `micro-small`
  低到中适配，通常只在融资环境、流动性、生存性和风险偏好直接影响价格时使用。
- `macro assets`
  高适配，包括指数、利率、黄金、美元、商品和跨资产主题。

## Core Question

当前宏观状态是否正在改变目标资产的盈利路径、贴现率、风险溢价、流动性、仓位或催化剂时间表？

## Required Inputs

- 官方宏观数据
  GDP、就业、CPI/PCE、PPI、PMI、零售、工业生产、收入、财政、贸易。
- 政策材料
  央行声明、纪要、SEP、财政政策、监管与贸易政策。
- 市场定价
  利率曲线、实际利率、通胀预期、美元、信用利差、VIX、股债相关性、行业相对强弱、估值倍数、资金流。
- 机构/实务解释
  T0/T1 sell-side、asset manager、macro strategist、trader commentary。
- 目标资产映射
  收入敏感度、成本敏感度、杠杆、融资需求、估值 duration、海外收入、商品敞口、客户需求 beta。

## Primary Signal

最重要的信号不是某个宏观指标的绝对水平，而是：

- 相对市场预期的 surprise。
- 是否改变政策反应函数。
- 是否改变金融条件。
- 是否改变盈利修正方向。
- 是否改变风险溢价和仓位。
- 是否触发跨资产确认或背离。

## Why It Works

宏观之所以对股票和资产有效，不是因为宏观数据本身神秘，而是因为资产价格本质上折现未来现金流和风险。

宏观变量会通过五条主路径影响价格：

- `earnings path`
  增长、需求、库存、财政和外需改变收入和利润。
- `discount rate`
  名义利率、实际利率和期限溢价改变估值倍数。
- `risk premium`
  信用、波动率、地缘和政策不确定性改变投资者要求回报。
- `liquidity`
  央行资产负债表、美元流动性、融资条件和信用供给改变风险承载能力。
- `positioning`
  拥挤度、CTA/vol-control、期权和资金流改变短期价格弹性。

## Failure Mode

- 宏观判断正确，但目标资产对这条宏观链不敏感。
- 指标方向正确，但市场已经提前 price in。
- 只看经济数据 level，不看 change 和 surprise。
- 把 policy easing 一概视为利好，忽略 growth scare。
- 把高估值成长股简单归因于利率，忽略盈利 revision、主题拥挤和 capex cycle。
- 用滞后数据解释价格，而不是定义下一次刷新触发。

## Evidence Cost

medium-high

基础版本可以快速完成，但高质量版本需要同时看官方数据、政策口径、市场定价和目标资产映射。若要做跨资产确认和仓位判断，成本会升高。

## Speed Vs Depth

- `speed`
  用于快速判断 `macro_weight`，决定是否启用 overlay。
- `depth`
  用于宏观主导资产或重大宏观事件，必须写完整 regime、market pricing 和 transmission chain。

## Comparison To Existing Methods

相对当前 `equity-research-core`：

- 它补足了宏观敏感资产的定价链，而不是只在 `large-mega` 里笼统提到利率和配置。
- 它给 `macro_sensitivity` 一个可执行的判断流程。
- 它与 `variant-perception` 互补：macro overlay 负责判断宏观变量，variant perception 负责判断市场是否已经 price in。
- 它与 `supply-chain` 互补：macro overlay 负责需求、利率、流动性和风险偏好，supply-chain overlay 负责产业链验证。

## Follow-Through Criteria

- 是否减少“泛宏观背景”。
- 是否能更清晰解释 price action 和 earnings revision。
- 是否能提前定义 `must_refresh_if`。
- 是否能帮助识别宏观判断与目标资产价格之间的错配。
- 是否能在不同资产上给出不同传导链，而不是同一个宏观故事套所有票。

## Trial Design

试跑案例：

- `AI high-duration / AI capex`
  验证实际利率、AI capex、信用融资、主题拥挤和 earnings revision 如何共同定价。
- `banks / real estate`
  验证利率曲线、信用、贷款标准和资产质量传导。
- `cyclical / commodity`
  验证增长、库存、美元、商品价格和利润率传导。
- `gold / Treasury-sensitive assets`
  验证实际利率、美元、地缘风险、央行需求和 risk-off/risk-on 传导。
- `export chain`
  验证美元、全球需求、关税和地区资本流传导。

预期增量：

- 明确 macro_weight。
- 把宏观观点落到传导链。
- 提升 memo 的刷新条件和失效条件。
- 避免把宏观正确性误当成单票正确性。

## Falsification Conditions

- 如果启用后多数 memo 只是多了一段宏观背景，而没有改变 thesis 质量，应降级。
- 如果无法稳定写出 market pricing 和 transmission chain，不进入 `adopted`。
- 如果在试跑案例中宏观 overlay 不能改善 refresh trigger 或 falsification condition，不升级。
- 如果它经常压过更重要的公司/行业变量，说明 routing 规则过宽，需要收紧。

## Adoption Decision

当前判断：`trial`

原因：

- 机构和实务基础足够强，且与 Mira 现有 framework routing 高度兼容。
- 但宏观分析最容易事后化和泛化，需要用真实案例验证是否能稳定提高研究质量。
- 先作为 overlay 与 skill 试用，不直接进入 `adopted`。

## Source Notes

- J.P. Morgan Asset Management, `Guide to the Markets`, quarterly market and economic chart framework: https://am.jpmorgan.com/wr/en/asset-management/liq/insights/market-insights/guide-to-the-markets/
- BIS Annual Economic Report 2025, Chapter II, `Financial conditions in a changing global financial system`: https://www.bis.org/publ/arpdf/ar2025e2.htm
- IMF World Economic Outlook, April 2026: https://www.imf.org/en/publications/weo/issues/2026/04/14/world-economic-outlook-april-2026
- Federal Reserve Monetary Policy Report, June 2025 summary: https://www.federalreserve.gov/monetarypolicy/2025-06-mpr-summary.htm
- Goldman Sachs Research, `Forecasts for the World's Biggest Economies in 2026`: https://www.goldmansachs.com/insights/articles/forecasts-for-the-worlds-biggest-economies-in-2026
- BlackRock Investment Institute, 2026 Investment Outlook: https://www.blackrock.com/americas-offshore/insights/blackrock-investment-institute/global-macro-outlook
