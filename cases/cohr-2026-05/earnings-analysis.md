# Coherent Corp. (COHR) 财报分析

- market: US
- report_period: FY2026 Q3
- report_type: quarterly earnings release
- fiscal_period_end: 2026-03-31
- release_date: 2026-05-06
- analysis_cutoff_date: 2026-05-07
- thesis_horizon: 6-18 months
- stale_after: 2026-08-15

## 分析设置

COHR 在 2026-05-06 美股盘后发布 FY2026 Q3 财报。本案例使用公司财报新闻稿、完整财务表、电话会转写、SEC 投资者展示材料，并引入 Lumentum Holdings Inc. (LITE) FY2026 Q3 作为同业同期对照。

核心问题是：COHR 的 AI 数据中心增长，到底是可持续的公司 alpha，还是已经在同行中普遍体现的行业 beta。

## 核心结论

COHR 交出了一份增长很强、但质量并不完美的财报。收入、毛利率、经营杠杆和 Q4 指引都改善；主要弱点是现金转换，库存、应收和 CapEx 正在吸收利润表改善。

Thesis impact：`+1`。本季度确认 AI 光通信增长主线，但不足以给到 `+2`，因为现金转换偏弱，而且 LITE 展现出更强的相对增长和利润率扩张。

## 来源映射

- `cohr_q3_fy2026_results`：COHR 官方财报新闻稿和财务表。
- `cohr_q3_fy2026_transcript`：管理层关于数据中心需求、800G、1.6T、OCS、CPO、backlog 和磷化铟产能的口径。
- `cohr_q3_fy2026_presentation_sec`：提交给 SEC 的投资者展示材料，用于确认收入结构和 pro forma 口径。
- `lumentum_q3_fy2026_results`：LITE 同期财报，用于 AI 光通信行业需求和同业质量交叉验证。
- `derived_cohr_may2026_earnings_analysis`：本案例派生分析。

## 核心业务图谱

- core_business：Datacenter & Communications 已经成为主业务，Q3 收入 $1.362B，约占公司总收入 75%。
- core_growth：AI 数据中心光通信需求、800G 和 1.6T transceivers、OCS 系统、CPO 路线，以及磷化铟产能扩张。
- core_drag：Industrial 收入从去年同期 $529M 降至 $444M；同时库存、应收和 CapEx 使现金转换恶化。
- thesis_driver：AI 数据中心光互连基础设施的持续需求和供给约束。
- non_core_noise：A&D 和 Munich 业务出售影响 pro forma 对比；GAAP 重组和出售相关项目不是核心 thesis。

这不是一个全面复苏故事，而是一个业务结构迁移故事：一个业务分部已经成为公司 thesis 的主体。

## 定价 / 放量桥

### 定价

COHR 有定价权证据，但证据并不纯粹。管理层提到 pricing optimization、健康的供需关系、产品结构改善，以及外部组件成本上升时可以传导或通过内部生产抵消。800G 向 1.6T 迁移也支持更高 ASP。

更准确的判断是：COHR 不是单纯靠提价，而是靠供需紧张、高价值产品结构、自有磷化铟产能和 6-inch 良率改善共同推高毛利率。

### 放量

放量是更强的主线。Datacenter & Communications 收入从 FY2025 Q3 的 $969M 增至 FY2026 Q3 的 $1.362B，也高于 FY2026 Q2 的 $1.208B。管理层还提到多客户、多产品类别需求强劲，1.6T 快速采用，OCS 贡献，backlog 创纪录，订单延伸到 2028。

公司不是简单“看到需求”，而是处在产能受限状态，并通过资本开支释放更多供给。

### 增长归因

| driver | classification | evidence | durability |
| --- | --- | --- | --- |
| AI 数据中心光通信需求 | volume-driven | Datacenter & Communications 同比 +40.6%、环比 +12.7% | 如果 hyperscaler AI CapEx 延续，持续性高 |
| 1.6T 迁移和 OCS 系统 | mix-driven / volume-driven | 管理层预计 Q4 增长来自 transceivers 和 OCS | 中高，仍在爬坡 |
| Pricing optimization 和供给紧张 | price-driven | Non-GAAP 毛利率同比 +105 bps，管理层提到 pricing optimization | 中等，取决于供需平衡 |
| 6-inch 磷化铟良率改善 | cost-driven | 管理层将良率和 input cost 改善与 margin 关联 | 中高，取决于产能爬坡执行 |
| Industrial 疲弱 | negative volume / mix | Industrial 收入从 $529M 降至 $444M | 中等；不是 thesis driver，但稀释公司级增长 |

## 财务快照

COHR 的报告增长很强，但现金转换偏弱。

| metric | FY2026 Q3 | change |
| --- | ---: | ---: |
| revenue | $1.806B | 同比 +20.5%，环比 +7.1% |
| GAAP gross margin | 37.7% | 同比 +243 bps |
| non-GAAP gross margin | 39.6% | 同比 +105 bps |
| GAAP EPS | $0.97 | 同比 +$1.08 |
| non-GAAP EPS | $1.41 | 同比 +$0.50 |
| non-GAAP operating margin | 20.3% | 同比 +163 bps |
| FY2026 YTD operating cash flow | $10.1M | 去年同期 $503.3M |
| FY2026 YTD CapEx | $547.2M | 去年同期 $309.5M |

## 三表分析

### 利润表

利润表很强。收入同比增长 20.5%，non-GAAP 毛利率扩大到 39.6%，non-GAAP operating margin 达到 20.3%。EPS 增速高于收入增速，说明经营杠杆在改善。

### 资产负债表

流动性明显改善。现金及等价物为 $1.593B，短期投资 $825M，公司还持有受限现金。$2B 普通股发行增强了资产负债表，也为产能扩张提供资金。长期债务从 FY2025 年末的 $3.499B 降至 $3.185B。

风险在营运资本。应收账款增至 $1.188B，库存从 FY2025 年末的 $1.438B 增至 $2.127B。这支持产能爬坡叙事，但后续必须转化为收入和现金。

### 现金流

现金流是主要弱点。FY2026 前九个月经营现金流只有 $10.1M，去年同期为 $503.3M。同期 CapEx 为 $547.2M，去年同期为 $309.5M。这符合“提前投入满足需求”的叙事，但会阻止本季度被定义为全维度高质量财报。

## 驱动桥

本季度主要由放量和产品结构驱动，也有一部分定价贡献：

- volume：AI 数据中心需求、客户扩张、800G、1.6T、OCS 和产能释放。
- mix：Datacenter & Communications 已占收入 75%，并承载主要增长。
- pricing：pricing optimization 和供需紧张支撑毛利率。
- cost/yield：6-inch 磷化铟良率改善和 input cost 下降帮助 margin。
- drag：Industrial 下滑和营运资本吸收现金。

## 可持续性测试

需求信号足以支撑正向 thesis impact。订单延伸到 2028、Nvidia 合作、多产品类别增长和产能扩张都支持多季度爬坡。

限制在于：可持续性仍需现金流验证。如果库存和应收继续快于现金生成，市场可能会把收入增长视作昂贵增长，而不是高质量增长。

## 同业财报交叉验证

- peer_company：Lumentum Holdings Inc.
- peer_ticker：LITE
- peer_report_period：FY2026 Q3
- peer_selection_reason：LITE 是直接的 optical/photonics AI datacenter 同行，并在同一周发布 FY2026 Q3。

LITE 验证了行业 thesis。LITE FY2026 Q3 收入同比增长 90.1%、环比增长 21.5%，non-GAAP gross margin 为 47.9%，non-GAAP operating margin 为 32.2%。管理层将 margin 扩张归因于 operational rigor、pricing discipline 和 product mix。

同行读数是双向的：

- 对 COHR 正面：AI 数据中心光通信需求是广泛存在的，不是 COHR 单家公司叙事。
- 对 COHR 相对负面：LITE 的收入增速、毛利率、经营利润率和 Q4 隐含增长都强于 COHR。

COHR 更像一个规模更大、产能和产品覆盖更宽的平台。LITE 当前更像一个更干净、更高 beta 的 margin expansion 标的。

## 管理层口径

管理层强调数据中心和通信需求强劲、快速扩产和多年机会。最关键的不是“需求强”，而是反复强调产能：COHR 正试图通过内部磷化铟扩产，把供给约束转化为收入。

## 市场预期与反应

市场反应偏混合，因为 AI optical 标的的预期已经很高。根本问题不是本季度弱，而是强财报可能已经被部分定价，同时 LITE 抬高了同行增长和利润率基准。

## 质量评分

| dimension | score | rationale |
| --- | ---: | --- |
| growth_quality | 4.0 | 核心分部增长强且可见，但 Industrial 拖累 |
| pricing_power | 4.0 | Pricing optimization 和供需紧张真实存在，但 margin 改善也依赖成本和良率 |
| volume_durability | 4.0 | Backlog、LTAs、产品爬坡和扩产支持持续放量 |
| margin_quality | 3.5 | Margin 改善真实，但低于 LITE，且依赖产能爬坡执行 |
| cash_conversion | 1.0 | YTD 经营现金流几乎消失，同时 CapEx 大幅上升 |
| balance_sheet_risk | 4.0 | 股权融资和债务下降后，流动性明显改善 |
| guidance_credibility | 4.0 | Q4 指引强，且 LITE 验证行业需求 |
| peer_relative_quality | 3.0 | 方向正确，但 LITE 展现更强增长和 margin |
| thesis_impact | 1.0 | 确认 AI optical thesis，但现金流和同行差距限制置信度 |

## Thesis Impact

`+1`：COHR 仍是有效的 AI 数据中心光通信受益标的，具备较强放量持续性和一定定价权。但在经营现金流改善、且相对 LITE 的质量差距收窄之前，不应上调到 `+2`。

## 风险与跟踪项

- 库存和应收无法顺利转化为现金。
- 1.6T 和 OCS 爬坡需要比预期更多 CapEx。
- LITE 或其他同行继续展现明显更好的毛利率和经营杠杆。
- Industrial 疲弱对公司级增长造成更大拖累。
- 行业磷化铟供给追上后，定价权减弱。

## 事实与推断

- fact：COHR Q3 收入 $1.806B，non-GAAP gross margin 39.6%，non-GAAP EPS $1.41。
- fact：Datacenter & Communications 收入 $1.362B；Industrial 收入 $444M。
- fact：FY2026 YTD 经营现金流 $10.1M，CapEx $547.2M。
- fact：LITE Q3 收入同比 +90.1%，non-GAAP gross margin 47.9%。
- inference：COHR 的增长更偏放量驱动，而不是纯定价驱动。
- inference：COHR 有定价权，但相对 LITE 的质量不够干净。
- inference：COHR 应获得正向 thesis impact，但还不是高置信度上调。

## 刷新触发条件

- COHR FY2026 Q4 财报或更新指引。
- Nvidia、hyperscaler、1.6T、OCS 或 CPO 相关新合同披露。
- 库存或应收增速继续快于收入。
- LITE 或其他直接同行给出明显不同的需求或定价信号。
- COHR gross margin 突破或跌破 Q4 指引区间 39%-41%。
