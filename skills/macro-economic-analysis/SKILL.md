# Macro Economic Analysis Skill

这个 skill 用于把宏观经济分析转成可执行的资产定价判断。

它不是宏观背景介绍，也不是经济学教材式综述。它服务于一个核心问题：

> 当前宏观状态是否正在改变目标资产的盈利路径、贴现率、风险溢价、流动性、仓位或催化剂时间表？

## Use When

- 研究对象是指数、宏观敏感资产、周期股、资源品、银行、地产、出口链、黄金、美债、美元或高估值成长股。
- 单票研究中，价格波动明显由利率、通胀、增长、政策、美元、信用、资金流或风险偏好解释。
- 财报或公司事件本身不足以解释价格，必须判断市场在交易 `growth scare`、`reflation`、`policy pivot`、`liquidity easing/tightening` 或 `risk-off/risk-on`。
- 用户明确要求宏观、利率、经济周期、央行、财政、流动性或市场风险偏好分析。

如果研究对象是具体商品、商品期货曲线、库存、供需平衡或成本曲线，先使用 `skills/commodity-cycle-analysis/SKILL.md`。只有当商品冲击传导到通胀、利率、财政、外部账户、美元、信用或风险偏好时，才升级为本 macro skill 或叠加 `macro` overlay。

## Required Inputs

- `asset_or_ticker`
- `market_scope`
- `research_question`
- `research_cutoff_date`
- `thesis_horizon`
- `current_market_pricing`
  例如收益率曲线、Fed funds futures、美元、信用利差、指数走势、行业相对强弱、估值倍数。
- `macro_sources`
  至少覆盖官方数据、央行/财政/国际组织材料、市场定价数据，以及机构或 practitioner 观点中的两类。

## Macro Regime Map

先用以下维度判断当前 regime。不要机械打分，要写清楚哪些变量真正影响本次研究对象。

### 1. Growth

关注：

- GDP、工业生产、PMI、零售、消费、就业、收入、企业投资、库存周期。
- 需求是加速、减速、韧性还是断裂。
- 增长变化是 broad-based，还是只集中在少数行业或 capex 主题。

核心问题：

- 增长变化影响的是收入 beta、盈利弹性、信用质量，还是风险偏好？

### 2. Inflation

关注：

- CPI、PCE、PPI、工资、租金、商品、能源、进口价格、通胀预期。
- 通胀是需求拉动、供给冲击、工资粘性，还是政策/关税/汇率传导。

核心问题：

- 通胀变化是否改变央行反应函数、实际利率、利润率或估值倍数？

### 3. Policy

关注：

- 央行政策路径、forward guidance、财政脉冲、税收、产业政策、监管政策、贸易政策。
- 市场预期路径与政策制定者反应函数是否偏离。

核心问题：

- 政策是提供 liquidity cushion，还是制造 discount-rate / margin / demand shock？

### 4. Liquidity And Financial Conditions

关注：

- 实际利率、收益率曲线、期限溢价、美元流动性、QT/QE、准备金、TGA、回购市场、信用利差、银行信贷、融资成本。
- 金融条件内部是否分裂，例如利率收紧但信用利差和股票估值仍宽松。

核心问题：

- 当前融资环境会放大还是压制风险资产估值、企业融资、回购、并购和 capex？

### 5. Credit

关注：

- 投资级与高收益利差、违约率、贷款标准、银行放贷、私募信用、再融资墙、杠杆水平。

核心问题：

- 信用条件是否正在改变企业生存性、投资能力、估值下限或尾部风险？

### 6. FX And Rates

关注：

- 美元指数、实际利率、名义利率、曲线形态、期限溢价、跨币种套保成本、资本流向。

核心问题：

- 汇率和利率通过收入换算、进口成本、资金流、估值贴现或外债压力传导到资产了吗？

### 7. Risk Appetite And Positioning

关注：

- VIX、信用利差、股债相关性、市场宽度、资金流、CTA/vol-control、期权偏度、拥挤度、主题集中度。

核心问题：

- 价格变化来自基本面 revision，还是来自仓位、杠杆、流动性和风险预算变化？

### 8. Market Pricing

这是必须单独写的一层。

关注：

- 市场已经 price in 什么。
- 数据或政策相对预期是 surprise 还是 confirmation。
- 当前价格隐含的是 soft landing、recession、reflation、stagflation、AI productivity boom，还是 liquidity rally。

核心问题：

- 哪个宏观变量的边际变化最可能触发重定价？

## Transmission Chains

宏观结论必须落到至少一条传导链。常用链条：

- `growth -> revenue beta -> operating leverage -> earnings revision -> multiple`
- `inflation -> policy path -> real rates -> duration multiple -> equity valuation`
- `inflation -> input cost -> gross margin -> pricing power test`
- `policy -> liquidity -> risk appetite -> positioning -> valuation`
- `rates -> mortgage/credit demand -> housing/banks/consumer`
- `dollar -> translation/import cost/EM liquidity -> earnings and flows`
- `credit spread -> financing access -> default risk -> equity risk premium`
- `commodity shock -> inflation + margins + fiscal/external balance`
- `fiscal impulse -> nominal demand -> sector revenue -> rates/term premium offset`

If no credible transmission chain exists, macro should stay as context and not enter the core thesis.

如果传导链的第一变量是具体商品供需、库存、期货曲线或成本曲线，先运行 `commodity-cycle-analysis`，再把结论压缩成 macro transmission input。

## Data Release Triage

当用户问单次宏观数据发布，例如 CPI、PPI、PCE、NFP、ISM、retail sales 或 GDP 时，先运行 `macro-data-release-triage`，再决定是否升级为完整 `macro-regime-analysis`。

最低流程：

1. 确认官方发布时间、数据期和修正项。
2. 比较 headline 与 consensus / market pricing，判断 surprise 是确认还是反转。
3. 从 headline 拆到核心子项，定位问题来自 level、change、revision、breadth 还是 composition。
4. 区分一次性噪音与可持续传导，例如能源、食品、工资、租金、运费、库存、信贷或利润率。
5. 做历史类比，但必须写出相似点、不同点和政策环境差异。
6. 推演数据继续恶化或转好的上游条件。
7. 映射到资产传导链、市场已计价路径、`stale_after` 和 `must_refresh_if`。

输出字段：

- `release_context`
- `headline_surprise`
- `component_problem`
- `historical_analogue`
- `upstream_conditions`
- `market_pricing`
- `asset_transmission`
- `what_is_already_priced`
- `must_refresh_if`

相关方法卡：`memory/methodologies/macro-data-release-triage.md`。

## Output Requirements

For a standalone macro note, output:

- `macro_regime`
- `dominant_macro_variable`
- `market_pricing`
- `transmission_chain`
- `asset_impact`
- `what_is_already_priced`
- `what_would_change_the_view`
- `stale_after`
- `must_refresh_if`

For an equity research package, add these fields to `case notes` or memo:

- `macro_weight`
  one of `none`, `context`, `secondary`, `primary`
- `macro_overlay_basis`
- `dominant_macro_chain`
- `macro_mismatch_risk`
- `macro_refresh_triggers`

## Practical Checks

- Do not ask whether the economy is good or bad. Ask whether the macro path is changing relative to market expectations.
- Do not ask whether rate cuts are bullish or bearish. Ask whether cuts mean liquidity support, growth scare, or disinflation relief.
- Do not ask whether CPI is high or low. Ask whether the print changes the policy path, real rates, margins, or inflation expectations.
- Do not use broad macro labels unless they change the target asset's earnings path, discount rate, risk premium, liquidity, or positioning.
- Always separate official data, market pricing, institutional interpretation, practitioner signal, and Mira-derived inference.

## Failure Modes

- Turning every memo into a generic macro chapter.
- Treating commodity-specific inventory, curve or trade-flow signals as generic macro.
- Treating lagging macro data as if it were a forward signal.
- Ignoring what the market already priced.
- Confusing level with change, and change with surprise.
- Using one macro regime for every asset even when transmission differs.
- Explaining price action after the fact without predefining falsification triggers.

## Source Quality Guidance

- Official data and central bank materials are best for facts and policy language.
- BIS, IMF and similar institutions are useful for macro-financial structure and cross-border transmission.
- T0/T1 sell-side and asset-manager outlooks are useful for how professionals connect macro variables to asset allocation, but they remain interpretation rather than fact.
- Practitioner material is useful for high-frequency signals, positioning and market sensitivity, but must be downgraded if not cross-checkable.

## Current Status

- methodology_status: `trial`
- related_methodology_card: `memory/methodologies/macro-regime-analysis.md`
- related_overlay: `skills/equity-research-core/references/macro-overlay.md`
