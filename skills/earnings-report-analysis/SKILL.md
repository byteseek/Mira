# Earnings Report Analysis Skill

这个 skill 用于对单家公司的一份季报、半年报或年报做结构化分析。它服务于 `research package`，但输出重点从完整投资 memo 收窄到财报质量、经营变化和预期差。

默认时间跨度是 `near_term_execution` 到 `medium_term_revision`。只有当本期财报证据触及长期驱动变量，并且被订单、客户、产能、现金流、同行或产业链证据支持时，才允许把结论升级为 `long_term_thesis` 或 `regime_transition`。

## Use When

- 需要快速拆解一份新发布的财报
- 需要复核一个已有 thesis 是否被本期财报强化或削弱
- 需要比较本期披露与上一期、去年同期、市场预期或管理层指引
- 需要把财报、业绩会和市场反应整理成可追溯结论

## Required Inputs

- company_name
- ticker
- market
- report_period
- report_type
- fiscal_period_end
- release_date
- analysis_cutoff_date
- thesis_horizon
- prior_thesis_optional
- peer_company_name
- peer_ticker
- peer_report_period
- peer_selection_reason

## Required Source Types

- `L1` 财报、公告、业绩新闻稿或监管文件
- `L1` 或 `L4` 业绩会 transcript / prepared remarks / Q&A 摘要
- `L5` 价格、估值、市场预期或分析师一致预期
- `L1` 至少一家核心竞争对手的同期财报、公告或业绩新闻稿
- `L6` 派生计算表在只摘录披露数字时可选；如果输出同比、环比、margin bridge、implied guidance、peer relative quality、valuation delta 或任何影响 thesis/actionability 的数量判断，则必须生成 calculation ledger，并指向上游 `L1` 到 `L5`

## Output Package

默认输出到 `templates/earnings-analysis-package/` 结构：

- `earnings-analysis.md`
- `evidence-log.csv`
- `financial-snapshot.csv`
- `peer-comparison.csv`

如果财报事件用于维护已有 thesis，还必须输出或更新 Thesis System 事件对象：

- `event-delta.md`

如果该财报足以改变投资结论，再同步更新标准 `research package`：

- `investment-memo.md`
- `case-notes.md`
- `evidence-log.csv`

## Analysis Flow

### 1. Disclosure Check

- 明确财报口径：GAAP / non-GAAP / IFRS / adjusted
- 标记报告期、财年口径、发布日期和分析截止日期
- 区分已披露事实、公司解释、市场预期和 agent 推断
- 检查是否存在会计重述、分类调整或一次性项目

### 2. Core Business Map

先用经营语言描述本期财报，而不是直接进入会计数字：

- 核心业务：公司真正产生价值和支撑 thesis 的业务是什么
- 核心增长：本期增长主要来自哪条业务线、客户类型、产品代际或地区
- 核心拖累：本期拖累来自需求、价格、产能、成本、产品结构还是一次性事项
- thesis driver：哪些变化会改变中期判断，哪些只是非核心噪音

核心业务图谱必须回答：这家公司本期到底是“卖得更贵了”、“卖得更多了”，还是只是会计口径或组合变化。

### 3. Price / Volume Bridge

把增长拆成两个优先维度：

- `pricing`：是否具备定价权、提价权、议价权或供需主动权
- `volume`：供需上是否可以扩大业务量，且扩量是短期还是持久

`pricing` 判断要覆盖：

- 价格是否上升，或折扣是否收窄
- 产品 mix 是否向高 ASP / 高毛利产品迁移
- 供需是否紧张，公司是否能主动选择订单或客户
- 毛利率改善是否来自提价、成本下降、良率提升，还是产品结构

`volume` 判断要覆盖：

- 出货、产能、订单、backlog、客户扩张是否支持放量
- 放量是一次性补库存、短期订单拉动，还是多年需求周期
- 产能扩张、供应链、营运资本和 CapEx 是否支持继续放量
- 放量是否以牺牲价格、毛利率或现金流为代价

每个增长驱动必须标记为 `price-driven`、`volume-driven`、`mix-driven`、`cost-driven`、`accounting-driven` 或 `one-off`，并标记证据强度：`high`、`medium`、`low` 或 `source_gap`。

#### Evidence Ladder

定价、放量和持久性不能只引用管理层口径。必须把证据分层，并记录反证。

| dimension | high evidence | medium evidence | weak evidence / not enough alone | common counter-evidence |
| --- | --- | --- | --- | --- |
| pricing | realized price / ASP / net price 上升；折扣收窄；续约或新合同提价被接受；毛利改善可排除成本、汇率、补贴或一次性项目 | product mix 向高 ASP / 高毛利迁移；交期拉长、配额销售或供给紧张；同行同步提价或折扣收窄 | 管理层只说 pricing strong；收入增长但没有 ASP、折扣或毛利桥；毛利改善主要来自成本下降或良率改善 | ASP 下滑；促销或折扣扩大；gross-to-net 恶化；客户重谈合同；同行降价 |
| volume | 出货、销量、活跃客户、订单、RPO/backlog、book-to-bill 或 usage 明确增长；产能、供应链和客户验收支持交付 | 指引隐含放量；产能扩张按期；新客户、新地区或新平台开始贡献；渠道 sell-through 改善 | 低基数同比高增；一次性补库存；提前拉货；只给 TAM 或 pipeline 叙事 | backlog / RPO 环比下降；订单取消或延期；库存快于收入上升；应收恶化；渠道库存过高 |
| durability | 多季度连续验证；订单可取消性低；留存、续约、复购或客户预算强；现金流、营运资本、CapEx 和同行口径支持持续增长 | backlog 覆盖未来几个季度；管理层指引与历史兑现率匹配；产能爬坡路径可解释；同行需求方向一致 | 单季 beat；短期供需紧缺；一次性大单；政策、补贴或事件催化尚未转成合同和现金流 | 指引依赖后置季度；放量靠降价；毛利率随放量下降；现金消耗扩大；同行口径相反 |

Evidence strength rules：

- `high`：至少有一个 L1/L4/L5 来源直接支持，并能被财务表、订单/合同、客户行为、同行或市场预期中的至少一类交叉验证。
- `medium`：证据方向一致，但缺少直接 ASP / volume / contract / cash-flow 披露，或只覆盖未来指引而未被本期验证。
- `low`：主要来自管理层叙事、单季同比、低基数、pipeline、TAM 或 agent 推断。
- `source_gap`：关键证据缺失；不得把该驱动写成 durable conclusion。
- L6 派生计算可以支持解释，但不能单独把结论升级为 `high`。
- 若存在 material counter-evidence，必须把结论标记为 `mixed` 或降低 evidence_strength，并写明需要什么后续披露来证伪或确认。

### 4. Three-Statement Read

- income statement：收入、毛利、费用、营业利润、净利润、EPS
- balance sheet：现金、应收、存货、债务、递延收入、营运资本
- cash flow：经营现金流、自由现金流、资本开支、回购、分红
- 三表之间必须互相校验，不能只看利润表。
- 如果三表交叉校验会影响财报质量、thesis impact 或 actionability，必须运行 `data-analysis-quality-gate`，并把派生指标写入 `calculation-ledger.csv` 或 explicit formula note。

### 5. Forward Outlook / Guidance Bridge

财报分析必须把本季度事实和未来 4-8 个季度的预期变化连接起来。不能只写本季度 beat / miss，也不能把管理层指引当作已经验证的事实。

必须覆盖：

- `reported_vs_consensus`：本季度实际收入、利润率、EPS、FCF 或核心 KPI 相对市场预期如何
- `next_quarter_guidance`：下一季度收入、利润率、EPS、FCF、CapEx 或关键经营指标指引
- `full_year_guidance`：全年指引是否上调、下调、维持或首次给出
- `implied_bridge`：按指引倒推，后续季度需要什么增长、利润率、出货、利用率或现金流路径
- `guide_vs_consensus`：指引相对 consensus 是 beat、miss、inline，还是 consensus 不可得
- `guidance_drivers`：管理层称指引由价格、量、mix、产能、成本、客户预算、供应链、FX、利率或一次性项目驱动
- `guidance_quality`：指引是否被订单、backlog、RPO、库存、客户预算、产能、同行财报或历史兑现率支持
- `estimate_revision_impact`：对 FY1 / FY2 revenue、margin、EPS、FCF、CapEx、net debt 的方向性影响
- `guidance_risks`：指引最容易失效的假设
- `transcript_QA_delta`：业绩会 Q&A 是否改变新闻稿表面结论，若 transcript 不可得必须标记 `source_gap`

如果公司不提供正式指引，必须用 prepared remarks、Q&A、订单/产能数据、同行指引和市场预期构建 `soft guidance bridge`，并降低证据强度。

如果使用指引倒推后续季度路径、implied bridge 或 guide vs consensus，必须运行 `data-analysis-quality-gate`。如果 consensus 或必要输入不可得，相关判断必须标记 `source_gap` 或 `calculation_gap`，不能写成高置信预期差结论。

### 6. Driver Bridge

把同比和环比变化拆成经营驱动：

- volume / price / mix
- segment / geography / product line
- margin bridge
- operating leverage
- working capital
- capital allocation

每个驱动必须标记为 `confirmed`、`inferred` 或 `unknown`。

### 7. Durability Test

定价和放量必须继续做可持续性测试：

- 定价权是结构性壁垒、技术代际、客户锁定、认证周期，还是短期供需紧缺
- 放量是由新平台、新客户、新产能或行业周期驱动，还是一次性订单
- 毛利率改善是否可以在放量后维持
- 现金流、库存、应收、CapEx 是否支持当前增长叙事
- 管理层指引是否与实际订单、backlog、产能和同行口径一致
- 是否存在 pricing、volume 或 durability 的反证；若存在，必须说明为什么不改变结论，或把结论降级

### 8. Peer Earnings Cross-Check

必须选择至少 1 家竞争对手或最相关同行的同期财报做交叉验证：

- 同行是否也看到相同需求方向
- 同行的定价权、放量能力和毛利率变化是否更强或更弱
- 本公司增长是行业 beta，还是公司 alpha
- 本公司管理层口径是否被同行验证、削弱或反驳
- 如果没有完全同期财报，必须标记 `timing_mismatch` 并降低结论强度

同行选择优先级：

1. 同产品/同客户/同技术路线直接竞争者
2. 同一产业链位置的替代供应商
3. 上下游最能验证需求真实性的公司

### 9. Quality Assessment

对本期质量做分层判断：

- high quality：收入、利润、现金流同向改善，且不是一次性因素驱动
- mixed quality：核心经营改善但有现金流、库存、费用或指引瑕疵
- low quality：利润依赖一次性收益、会计调整、费用延后或资本化
- unclear：披露不足，必须等待后续 filing、transcript 或分部数据

## Required Sections

`earnings-analysis.md` 必须包含：

- setup
- headline result
- source map
- core business map
- price volume bridge with evidence ladder
- financial snapshot
- three-statement analysis
- forward outlook / guidance bridge
- driver bridge
- durability test
- peer earnings cross-check
- management commentary
- market expectation and reaction
- event delta
- thesis impact
- risks and watch items
- fact vs inference
- refresh triggers

`event-delta.md` 必须包含：

- `pre_event_setup`
- `actual_disclosure`
- `delta_vs_expectation`
- `revision_path`
- `price_reaction_quality`
- `thesis_impact`
- `expectation_map_updates`
- `required_followup`

## Scoring

评分只用于强制结构化，不可替代文字判断。

| dimension | score range | meaning |
| --- | --- | --- |
| growth_quality | 1-5 | 增长是否来自可持续经营驱动 |
| pricing_power | 1-5 | 是否具备定价权、提价权或供需主动权 |
| volume_durability | 1-5 | 放量是否有供需、产能和客户基础支撑 |
| margin_quality | 1-5 | 利润率变化是否可解释且可持续 |
| cash_conversion | 1-5 | 利润与现金流是否匹配 |
| balance_sheet_risk | 1-5 | 资产负债表是否支持继续投入 |
| guidance_credibility | 1-5 | 指引与历史兑现、订单、需求信号是否一致 |
| guidance_market_delta | -2 to +2 | 指引相对市场预期和估值隐含预期的方向与幅度 |
| peer_relative_quality | 1-5 | 相对同行的增长、定价、放量和现金流质量 |
| thesis_impact | -2 to +2 | 对原 thesis 的影响方向和强度 |

## Thesis Impact Rules

- `+2`：核心争议被明显证实，且财务和管理层口径一致
- `+1`：方向改善，但仍需要后续季度确认
- `0`：与原 thesis 基本一致，信息增量有限
- `-1`：出现可解释但需要跟踪的瑕疵
- `-2`：核心 thesis 被削弱，或财务质量显著恶化

## Earnings-To-Thesis Bridge

财报分析必须明确本期证据能影响哪一层 thesis：

- `near_term_execution`
  本期实际、下一季指引、短期催化剂和价格反应。
- `medium_term_revision`
  FY1 / FY2 收入、利润率、EPS、FCF、CapEx、net debt 或估值锚修正。
- `long_term_thesis`
  一年以上的产业趋势、竞争位置、技术路径、利润池、商业模式或资本配置。
- `regime_transition`
  短期财报信号正在改变长期 thesis，或长期 thesis 正在被短期证据证伪。

如果把财报影响升级到 `long_term_thesis` 或 `regime_transition`，必须写明：

- 触及的长期变量是什么
- 哪些财报数字和管理层口径支持它
- 哪些外部证据链支持它
- 为什么它不是 one-off
- 后续哪些披露会证伪这个外推

如果证据不足，必须把长期影响降级为 watch item。

## Event Delta Rules

财报事件不能只总结 beat / miss。必须说明本期披露改变了哪个预期变量：

- revenue expectation
- margin expectation
- cash flow expectation
- capex expectation
- balance sheet risk
- valuation multiple
- risk premium
- positioning
- catalyst timing

如果没有可用的 pre-event consensus proxy，必须在 `event-delta.md` 写 `source_gap`，并降低 thesis impact 置信度。

价格反应只能作为 `market_pricing`，不能替代经营证据。管理层口径只能作为 `company_claim` 或 `guidance`，除非被财务、订单、客户、同行或外部数据验证。

## Evidence Rules

- 核心财务数字必须来自 `L1`。
- 市场预期和股价反应可以来自 `L5`，但必须写明时间戳。
- 管理层解释必须与原文或 transcript 对应，不得转述成已验证事实。
- 每条进入 evidence log 的信息都必须保留 `claim_type`、`claim_text`、`source_speaker` 和 `verification_status`。
- 财务事实、管理层口径、正式指引、长期目标、外部 consensus、市场反应和 Mira 倒推计算必须分开标注。
- 非 GAAP 指标必须同时检查调整项，不能只引用调整后 EPS。
- 如果使用 agent 计算的同比、环比、margin bridge、implied guidance、peer relative quality 或 valuation delta，必须登记为 `L6`、写上游来源，并在 `calculation-ledger.csv` 或 explicit formula note 中记录公式、口径、期间、单位和限制。
- 指引、consensus 和 implied bridge 必须区分公司口径、市场预期和 agent 倒推计算。
- 如果 transcript / Q&A 尚不可得，必须把未来预期分析标记为 `source_gap`，并把 transcript 发布列为刷新触发。
- 定价权、放量和竞争优劣必须有财务指标、订单/产能信号、管理层原话或同行财报支撑。
- 同行对比必须登记同行来源，并写明为何该同行可比。

## Red Flags

- 收入增长但应收账款或存货异常上升
- EPS beat 主要来自回购、税率、利息收入或一次性项目
- 毛利率改善但公司没有给出可验证驱动
- 收入增长主要来自放量，但价格、毛利率和现金流同步恶化
- 公司宣称定价权增强，但同行财报显示价格压力或供给过剩
- 公司宣称需求持久，但放量只来自短期补库存或一次性订单
- 经营现金流连续弱于净利润
- 资本开支下降支撑短期 FCF，但削弱中长期产能或产品力
- 指引上调但订单、backlog 或需求信号没有同步支持
- 维持全年指引但下一季度指引偏弱，导致后半年度隐含爬坡过高
- 收入或 EPS 指引 beat，但 CapEx、利息、库存、应收或 FCF 明显恶化
- 业绩会 Q&A 软化了新闻稿中的强指引，但市场只交易 headline
- 管理层把一次性因素包装成结构性改善

## Boundaries

- 这个 skill 不自动下载财报或 transcript。
- 它不直接给交易建议，只输出 thesis impact 和 watch items。
- 它可以触发更新 investment memo，但不能跳过 evidence log。
- 它不把单季波动自动外推成长期趋势。
