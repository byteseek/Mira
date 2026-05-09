# CoreWeave, Inc. (CRWV) 财报分析

- market: US
- report_period: FY2026 Q1
- report_type: quarterly earnings release
- fiscal_period_end: 2026-03-31
- release_date: 2026-05-07
- analysis_cutoff_date: 2026-05-09
- thesis_horizon: 6-18 months
- stale_after: 2026-08-15

## 分析设置

这次分析对象是 CoreWeave 2026Q1 财报。时间边界是 2026-05-09，重点不是判断“AI 需求是否存在”，而是判断本季度是否证明 CRWV 可以把巨额 backlog 和资本开支按时转成收入、利润和可承受的现金流。

Framework routing：`large-mega` 主框架，secondary regime 为 AI capex 事件型成长股。CRWV 市值、交易关注度和融资规模已经不是小票逻辑，定价核心是未来收入曲线、资本开支、利率/信用融资环境和 AI 基建周期。框架错配风险是：如果把它当普通 SaaS 或纯成长股，会低估资产负债表和交付时点对估值的约束。

Selected overlays：`supply-chain` 和 `macro`。Supply-chain 用于跟踪 GPU、数据中心、用电、第三方开发商交付和客户履约；macro 权重为 `secondary`，主变量是信用利差、利率和 AI capex 风险偏好。

## 核心结论

CRWV 这份财报是“需求极强、经营质量混合、资产负债表压力继续上升”。收入、backlog、客户扩张和 active power 都证明 AI 云需求很真实；但 adjusted operating margin 压到 1%、GAAP 净亏损扩大到 7.40 亿美元、Q1 购买物业设备现金流出 76.95 亿美元，说明增长仍然高度依赖融资和准时交付。

Thesis impact：`+1`，不是 `+2`。本季度强化了需求和客户多元化 thesis，但没有解决市场最担心的两个问题：一是新产能能否按时转成收入，二是高杠杆融资成本会不会吃掉经营利润。

## 来源映射

- `crwv_q1_2026_results`：公司官方 Q1 财报新闻稿和财务表。
- `crwv_q1_2026_presentation`：Q1 earnings presentation，用于 capex 定义、backlog aging 和历史趋势。
- `crwv_q4_2025_results`：公司官方 Q4/FY2025 财报，用于环比基准。
- `oracle_q3_fy2026_results`：Oracle FY2026 Q3 财报，用于 AI 云基础设施同行验证。
- `market_reaction_sources`：市场预期、Q2 指引低于预期和股价反应用。

Source limitation：截至 2026-05-09，本次未拿到可稳定引用的完整 earnings call transcript。管理层口径主要来自官方新闻稿和市场报道，因此对指引解释、Q2 timing risk 和 capex inflation 的判断需要在 transcript/10-Q 可用后刷新。

## 核心业务图谱

- core_business：为 AI labs、hyperscalers、AI-native 企业和企业客户提供 GPU 加速 AI 云基础设施。
- core_growth：客户合同和 backlog 激增，Meta、Anthropic、Cohere、Jane Street、Mistral 等客户扩展；active power 超过 1GW。
- core_drag：部署成本、折旧、利息、数据中心建设和供应链时点在收入充分释放前先进入成本和现金流。
- thesis_driver：能否把 $99.4B backlog 在 2026-2027 年按时转成收入，同时维持融资可得性和较低边际资金成本。
- non_core_noise：GAAP EPS 本身不是最核心，因为折旧和融资结构会扭曲短期利润；但利息费用不是噪音，是核心风险。

## 定价 / 放量桥

### 定价

CRWV 的定价权证据是间接的。公司有 $99.4B backlog、active power 超过 1GW、合同电力超过 3.5GW，并能与 Meta、Anthropic、NVIDIA 等签下大额合作；这些说明供需位置很强。但本季度 adjusted EBITDA margin 从 62% 降到 56%，adjusted operating margin 从 17% 降到 1%，说明“供需紧张”没有直接转化为当期经营利润率扩张。

判断：有供给稀缺带来的议价能力，但短期被部署成本、折旧和融资成本抵消。定价权更像订单获取能力，不是利润表已充分兑现的定价权。

### 放量

放量是主线。收入 $2.078B，同比 +112%，环比 Q4 的 $1.572B 增长约 32%；backlog 从 Q4 的 $66.8B 增到 $99.4B，环比约 +49%。这不是会计口径制造的增长，而是客户合同和容量扩张驱动。

但放量质量仍要打折：收入确认取决于 GPU、数据中心、电力、网络和第三方开发商交付节奏。只要交付延后，capex 和利息先发生，收入后移，利润表就会继续承压。

### 增长归因

| driver | classification | evidence | durability |
| --- | --- | --- | --- |
| AI 云需求和新客户合同 | volume-driven | Q1 backlog $99.4B，Meta $21B commitment，Anthropic 多年协议 | 高，但取决于客户履约和产能交付 |
| Active power 和 contracted power 扩张 | volume-driven / supply-driven | active power 超过 1GW，contracted power 超过 3.5GW | 中高，受数据中心、电力和组件供应约束 |
| NVIDIA 投资和 DDTL 4.0 融资 | financing-driven | NVIDIA $2B equity，$8.5B DDTL 4.0 | 中高，取决于信用市场继续支持 GPU-backed financing |
| 部署成本先于收入 | cost-driven | adjusted operating margin 1%，GAAP operating loss $144M | 短期负面；若利用率爬坡可改善 |
| 利息费用上升 | financing-cost-driven | Q1 interest expense $536M，约为收入 26% | 中高风险，需观察边际融资成本 |

## 财务快照

| metric | Q1 2026 | change |
| --- | ---: | --- |
| revenue | $2.078B | 同比 +112%，环比 +32% |
| GAAP operating loss | $(144)M | 去年同期 $(27)M |
| GAAP net loss | $(740)M | 去年同期 $(315)M |
| adjusted EBITDA | $1.157B | margin 56% |
| adjusted operating income | $21M | margin 1%，去年同期 17% |
| revenue backlog | $99.4B | 同比 +284%，环比 +49% |
| operating cash flow | $2.984B | 去年同期 $61M |
| purchase of property and equipment | $(7.695)B | 去年同期 $(1.407)B |
| total debt | $24.859B | Q4 2025 为 $21.373B |

## 三表分析

### 利润表

收入很好，但利润表质量混合。收入同比翻倍以上，adjusted EBITDA 也达到 $1.157B，说明在折旧和融资成本前，资产一旦投入使用有较强赚钱能力。问题是 operating expenses 同比从 $1.009B 增至 $2.222B，GAAP operating loss 扩大到 $144M；调整后 operating margin 也只有 1%。

最关键的是利息费用。Q1 interest expense net 为 $536M，相当于收入约 26%。这说明 CRWV 不是普通高增长云公司，而是带有基础设施融资属性的 AI utility-like buildout。

### 资产负债表

资产端快速扩张。Property and equipment net 从 2025 年末 $30.557B 增至 $36.424B。现金及等价物从 $3.127B 降到 $2.244B；总债务从 $21.373B 增到 $24.859B。公司同时拿到 $8.5B DDTL 4.0 和 NVIDIA $2B 股权投资，说明融资窗口仍开着，但 leverage 对 equity holder 的约束也在变强。

### 现金流

经营现金流 $2.984B 表面很好，但其中包括应收账款下降、递延收入增加和应付/应计项目增加。投资现金流流出 $7.708B，其中购买物业设备 $7.695B。也就是说，公司不是缺需求，而是每一美元未来收入都要先投入大量资本。

## 未来预期 / 指引桥

| item | analysis |
| --- | --- |
| reported_vs_consensus | Q1 revenue $2.078B，高于约 $1.97B 的市场预期；但 adjusted operating income $21M 只有 1% margin，质量不如收入 headline。 |
| next_quarter_guidance | 市场报道显示 Q2 revenue guidance 约 $2.45B-$2.60B，低于约 $2.7B consensus；Q2 利息费用仍会是核心压力项。 |
| full_year_guidance | 公司维持 FY2026 revenue $12B-$13B，但 capex 低端从约 $30B 抬到约 $31B，全年 capex 区间约 $31B-$35B。 |
| implied_bridge | Q1 实际 $2.078B 加 Q2 指引中点约 $2.525B 后，要达到 FY2026 revenue 中点 $12.5B，Q3+Q4 需要约 $7.9B，隐含后半年度显著加速。 |
| guide_vs_consensus | 当季 revenue beat，但 Q2 revenue guide miss；市场反应说明 forward miss 和 capex risk 压过了 Q1 beat。 |
| guidance_drivers | 指引兑现依赖新集群上线、客户合同转收入、GPU/电力/数据中心交付、利用率爬坡和融资成本控制。 |
| guidance_quality | Backlog、客户名单和 active power 支持全年收入可见度；但 Q2 guide 低于预期、capex 上修和 transcript 缺口降低了指引质量。 |
| estimate_revision_impact | FY2026 revenue 方向暂时维持；FY2026 capex 和利息压力偏负面；margin/FCF 估计大概率需要更谨慎。 |
| guidance_risks | 数据中心交付延迟、组件成本上升、客户部署节奏后移、融资成本上升、后半年收入爬坡不足。 |
| transcript_QA_delta | source_gap：截至本次分析未取得稳定可引用的完整 Q1 transcript；需要在 transcript/10-Q 发布后复核管理层对 Q2 timing、capex inflation 和全年桥的解释。 |

## 驱动桥

- volume：客户合同、backlog、active power 和 contracted power 是本季度增长主因。
- price/mix：推断存在供给稀缺和高价值 AI workload mix，但当期利润率没有证明强定价权已经落地。
- margin：adjusted EBITDA margin 仍高，但 adjusted operating margin 被部署费用和折旧前置压低。
- working capital：经营现金流改善部分来自营运资本释放，不应直接外推。
- capital allocation：继续重仓 capex，并通过债务、结构化融资和 NVIDIA 股权融资支撑。

## 可持续性测试

需求可持续性：高。backlog 接近 $100B，Oracle 的 AI cloud RPO 同步暴涨，说明行业需求不是 CRWV 单点叙事。

交付可持续性：中等。合同和订单很强，但收入确认受数据中心、电力、GPU、网络、冷却和客户部署时点影响。

利润率可持续性：中等偏低。本季度 adjusted operating margin 只有 1%，需要后续季度证明新集群利用率爬坡后能恢复。

融资可持续性：中等。DDTL 4.0 和 NVIDIA 投资是正面信号，但总债务、租赁负债和利息费用都在上升。信用市场如果重新定价 AI capex 风险，CRWV 的股权价值会被迅速压缩。

## 同业财报交叉验证

- peer_company：Oracle Corporation
- peer_ticker：ORCL
- peer_report_period：FY2026 Q3
- peer_selection_reason：Oracle 是 AI 云基础设施最相关的公开大型对照之一，虽不是纯 neocloud，但能验证 AI cloud demand、RPO、capex 和融资压力。

Oracle FY2026 Q3 显示 Cloud Infrastructure revenue $4.9B，同比 +84%；RPO $553B，同比 +325%；FY2026 capex 指引 $50B。这个验证 CRWV 的需求方向：AI 云供给仍紧，合同需求真实存在。

但 Oracle 也暴露 CRWV 的相对弱点。Oracle 同期 GAAP net income $3.7B，non-GAAP operating margin 43%，并表示许多大型 AI 合同由客户预付款或客户自供 GPU 支撑。相比之下，CRWV 当前更依赖自身资产负债表和融资市场承接建设节奏。

结论：同行验证需求，不验证 CRWV 的融资风险已解除。

## 管理层口径

管理层核心口径是：这是公司历史上最强 bookings quarter；AI 原生客户和企业客户选择 CoreWeave，是因为公司位于模型和硅片之间；市场从训练转向推理时，专用 AI 云平台差异更重要。

这是合理但需要验证的说法。Q1 的客户和 backlog 支持“需求真实”；但是否能在 Q2-Q4 按时交付并释放 operating leverage，需要后续财报验证。

## 市场预期与反应

市场没有否认收入和 backlog，而是在惩罚 timing risk 和 capex risk。市场报道显示，Q2 revenue guidance 大约 $2.45B-$2.60B，低于约 $2.7B 的市场预期；公司维持 FY2026 revenue $12B-$13B，并将 capex 低端抬高到约 $31B。股价盘后/次日下跌，核心原因是 Q2 指引和资本开支压力抵消了 Q1 收入 beat。

## 质量评分

| dimension | score | rationale |
| --- | ---: | --- |
| growth_quality | 4.0 | 收入和 backlog 很强，客户扩张真实 |
| pricing_power | 3.0 | 供需位置强，但当期 margin 没有证明价格已经落到利润 |
| volume_durability | 4.0 | backlog、active power 和 contracted power 支撑多季度放量 |
| margin_quality | 2.0 | EBITDA 好，但 adjusted operating margin 只有 1% |
| cash_conversion | 2.5 | OCF 强，但 capex 巨大且部分来自营运资本 |
| balance_sheet_risk | 2.0 | 融资能力强，但债务、租赁和利息压力很高 |
| guidance_credibility | 3.0 | 维持全年收入指引，但 Q2 指引低于市场预期，后半年度爬坡压力大 |
| guidance_market_delta | -1.0 | Q1 revenue beat 被 Q2 guide miss、capex 上修和 margin 压力抵消 |
| peer_relative_quality | 2.5 | 需求被 Oracle 验证，但盈利和资金结构弱于 Oracle |
| thesis_impact | 1.0 | 强化需求和客户多元化，但未解决交付/融资风险 |

## Thesis Impact

`+1`：这份财报强化了 CRWV 是 AI 基础设施核心受益者的判断。backlog、客户名单、active power 和融资事件都提高了中期收入可见度。

但不应升级到 `+2`。原因是 adjusted operating margin 跌到 1%，Q2 指引低于市场预期，且 capex 和利息费用继续扩张。现在最重要的不是“有没有需求”，而是“交付和融资曲线能不能跟上需求曲线”。

## 风险与跟踪项

- Q2 revenue 是否落在 $2.45B-$2.60B 区间上沿，或者再次受交付时点影响。
- FY2026 $12B-$13B revenue 指引是否维持，后半年是否需要异常强的收入爬坡。
- adjusted operating margin 是否从 Q1 的 1% 修复。
- interest expense / revenue 是否继续维持在 20% 以上。
- capex 是否继续上修，尤其是组件价格和数据中心交付成本。
- Meta、OpenAI、Anthropic、Microsoft 等大客户履约和集中度变化。
- GPU-backed debt、AI 数据中心债券和 CDS/credit spread 是否恶化。

## 事实与推断

- fact：Q1 2026 revenue 为 $2.078B，同比 +112%。
- fact：Q1 revenue backlog 为 $99.4B。
- fact：Q1 adjusted EBITDA 为 $1.157B，margin 56%。
- fact：Q1 adjusted operating income 为 $21M，margin 1%。
- fact：Q1 GAAP net loss 为 $740M，interest expense net 为 $536M。
- fact：Q1 purchase of property and equipment 为 $7.695B。
- inference：CRWV 的增长主要由放量和合同需求驱动，而不是当期提价。
- inference：CRWV 的最大风险已经从需求验证转向交付、融资和利润释放。
- judgment：财报质量为 mixed quality，thesis impact 为 `+1`。

## 刷新触发条件

stale_after：2026-08-15。

must_refresh_if：

- CRWV 发布 2026Q2 财报或更新 FY2026 指引。
- CRWV 发布 Q1 2026 完整 earnings call transcript 或 10-Q 后，复核 Q2 指引、capex、融资成本和客户集中度细节。
- 公司上调 FY2026 capex、披露新的大额债务融资或信用评级/利差显著变化。
- Q2 revenue 低于 $2.45B 或 adjusted operating margin 未明显修复。
- Meta、OpenAI、Anthropic、Microsoft 或 NVIDIA 关系出现合同、履约、付款或供应链变化。
- Oracle、Nebius、主要 hyperscalers 或 NVIDIA 对 AI compute demand/capex 给出明显相反信号。
