## Routing Card

| field | value |
| --- | --- |
| interaction_mode | `routed_research` |
| primary_intent | research AAPL 的 moat（竞争优势/护城河结构与耐久性） |
| secondary_intents | 无显式次任务（用户只点了 moat + standard package） |
| execution_order | 单任务，无队列 |
| scope_confirmation_required | `no` |
| routing_assumptions | (1) 真正要判断的是「AAPL 护城河由什么构成、有多耐久、什么会侵蚀它」，不是估值或能不能买；(2) market_scope = 美股；(3) time_boundary = `gt_1y`（moat 本质是长期竞争问题）；(4) 「答完了」= 给出护城河来源分解 + 耐久性判断 + 侵蚀条件 + 刷新触发，而非目标价 |
| assumption_confidence | `medium`（moat 路由清晰；但用户未给时间窗与是否含持仓语境） |
| task_mode | `first_pass_research` |
| research_object | `single_equity` — Apple Inc. (AAPL) |
| market_scope | US（NASDAQ；price_discovery_venue = 美国本土；dominant_investor_base = 全球机构 + 被动资金） |
| time_boundary | `gt_1y` → `long_term_thesis` |
| depth_mode | `standard`（"research + standard package" 明确指向标准包） |
| source_budget | 复用 golden case 已核验来源（FY2025 10-K、Q1 FY2026 results）；不联网 |
| ingestion_route | `none`（无新文件/API；复用 tracked case 证据） |
| ingestion_artifacts | `waived` |
| source_registry_action | `reuse`（`cases/aapl-2026-04/evidence-log.csv`） |
| information_value | `medium`（护城河结构在现有 filing 证据下可知；侵蚀速度部分不可知） |
| knowability_status | `partially_knowable`（moat 来源可由 10-K 与运营数据确证；AI/监管/产品周期对护城河的侵蚀速率 = `unknowable_now`） |
| private_state_action | `waive`（未提供持仓/观点；如需保存可走 view-continuity） |
| decision_pressure | `none`（纯研究问题，无买/加/冲动作语，未触发 actionability gate） |
| framing_risk | `none` |
| disconfirmation_required | `no` |
| quant_dependency | `low`；calculation_gate = `waived`（moat 质性判断为主；估值数字 = `source_gap`，不联网无法刷新） |
| primary_skill_or_loop | `loops/research-loop.md` → `skills/equity-research-core/SKILL.md` |
| horizon_bucket | `long_term_thesis` |
| selected_framework | `large-mega`（framework_basis：超大市值、机构+被动主导、估值锚有效、盈利稳定、平台型成熟业务） |
| framework_mismatch_risk | 把「护城河耐久性」误写成「短期产品周期交易结论」 |
| selected_overlays | `supply-chain`（关税/制造集中度对护城河成本侧的影响）、`market-structure-policy`（监管/反垄断对生态封闭性的侵蚀）；`macro` 仅作背景 |
| selected_lenses | `long-term-multibagger` 部分调用（强制检查终局与市场误解），但主用 `variant-perception` 判断 moat 是否被市场充分定价 |
| readiness_level | `working_view`（市场/估值侧 source_gap，无法升级到 decision-ready） |
| routing_mismatch_risk | 把成熟平台护城河当成高弹性预期差交易；或在缺持仓数据时给仓位结论 |
| output_language | `zh-CN`（继承 interaction_language）；evidence_languages = `[en]` |
| followup_prompt_mode | `standard` |

---

## AAPL Moat 研究包 (Standard)

研究对象: Apple Inc. (AAPL) | 市场: 美股 | 时间边界: `gt_1y` 长期竞争问题
证据截止: 复用 golden case，基本面数据至 fiscal Q1 2026（结束于 2025-12-27），filing 基准 FY2025 10-K（2025-10-31）
本轮无联网: 市场/估值/最新竞争动态为 `source_gap`，下文显式标注。

### 一、Moat 来源分解（按耐久性排序）

| 护城河来源 | 类型 | 强度判断 | 证据基础 |
| --- | --- | --- | --- |
| 软硬件 + OS 一体化整合 | 转换成本 + 生态锁定 | 强、最难复制 | FY2025 10-K 业务模式（L1, verified） |
| 25 亿+ 活跃设备安装基数 | 网络/规模 + 用户惯性 | 强 | Q1 FY2026 results（L1, disclosed） |
| 品牌与定价权 | 无形资产 | 强 | 10-K + Q1 高毛利结构（L1） |
| 渠道与分发（自营零售 + 运营商） | 分发优势 | 中-强 | 10-K（L1, verified） |
| Services 变现（App Store、订阅、支付） | 安装基数货币化 | 中-强，但有监管暴露 | Q1 FY2026 Services 走强（L1, disclosed） |

护城河的核心机制不是任何单一硬件，而是「安装基数 × 转换成本 × Services 货币化」的复利闭环：设备越多 → 生态越黏 → Services 收入越稳 → 越能反哺研发与定价权。

### 二、Facts / Inferences / Judgments 分离

Facts（已核验 / 已披露，L1）
- FY2025 10-K 是业务模式、分部结构、风险因素的一手来源（verified）。
- Q1 FY2026: 收入 143.8B（同比 +16%）、EPS 2.84（+19%）、经营现金流近 54B、安装基数 25 亿+（disclosed）。
- 10-K 风险因素明确将关税与贸易措施列为供应链与毛利的潜在逆风（verified）。

Inferences（基于事实的推断）
- iPhone 与 Services 同步走强 → Apple 是安装基数驱动的平台，而非单一硬件公司。
- 高毛利结构 + 现金流韧性 → 品牌定价权与转换成本仍在有效运转。
- Services 占比上升 → 货币化护城河仍在加深，但同时把更多利润暴露在 App Store 监管/抽成风险下。

Judgments（带置信度）

判断 1: AAPL 的护城河结构在长期维度仍属「宽且耐久」级别。
- judgment_confidence: `high`
- confidence_basis: 多条高权重 L1 证据交叉（一体化整合 + 安装基数 + 高毛利现金流），且彼此自洽。
- base_rate_anchor: 拥有强转换成本 + 大安装基数的平台型龙头，护城河衰减通常以多年计而非数季。
- reversal_condition: 连续多季 iPhone 走弱且 Services/毛利无法对冲，或生态封闭性被监管强制打开（如被迫开放支付/侧载并显著侵蚀 App Store 经济）。

判断 2: 护城河「是否被市场充分定价」是更尖锐的问题，而非护城河本身是否存在。
- judgment_confidence: `medium`
- confidence_basis: golden case 已指出市场广泛认可 Apple 质量，变体认知偏弱；但估值锚 = `source_gap`，无法在本轮量化。
- reversal_condition: 出现刷新后的估值模型显示市场对 Services 货币化或 AI 落地的预期明显偏低/偏高。

判断 3: 最可能侵蚀护城河的不是竞品硬件，而是监管对生态封闭性的拆解 + AI 重塑入口。
- judgment_confidence: `medium`
- confidence_basis: 10-K 已自述监管/关税风险；AI 是否改变「设备即入口」尚不可知。
- reversal_condition: 出现监管终局裁决强制开放生态核心抽成，或 AI 入口证据显示设备层黏性下降。

### 三、Moat 侵蚀路径（什么会让护城河变窄）

1. 监管/反垄断: 强制侧载、第三方支付、降低 App Store 抽成 → 直接削弱 Services 货币化护城河（market-structure-policy overlay）。
2. AI 入口重构: 若 AI 助手/智能体成为新交互入口，可能弱化「iPhone = 默认入口」的转换成本（当前 = `unknowable_now`）。
3. 供应链/关税: 制造集中度 + 关税抬高成本，压缩毛利即削弱定价权护城河（supply-chain overlay；10-K 已列明）。
4. 产品周期疲劳: 单轮 iPhone 周期驱动而非生态持续变现 → 高质量叙事降温（折叠屏延期类信号为 unverified 风险 watch，非 thesis 锚）。

### 四、Source Notes / Evidence Posture

复用 `cases/aapl-2026-04/evidence-log.csv`（source_registry_action = `reuse`）:
- L1 verified: `sec_apple_10k_2025`（业务模式 + 风险因素）
- L1 disclosed: `apple_q1_2026_results`（财务质量 + 安装基数 + 资本回报）
- L5 estimated（市场数据，已过期）: `financecharts_aapl_summary`、`stockanalysis_aapl_history` → 估值/价格结构 = `source_gap`
- L4 unverified: `macrumors_foldable_delay_2026` → 仅作 event-risk watch
- evidence_posture: 护城河结构性结论由 L1 支撑（可靠）；估值与「是否便宜」侧为 `source_gap`，本轮不联网无法关闭。

### 五、Readiness 与刷新条件

- readiness_level: `working_view`。护城河结构判断证据充分，但「moat 是否充分定价」受估值 `source_gap` 限制，无法升级到 decision-ready。
- stale_after: 下一次季度财报或正式指引更新。
- must_refresh_if:
  - 监管/反垄断对 App Store 抽成或生态封闭性出现实质裁决；
  - AI 入口出现削弱设备层黏性的可观察证据；
  - 关税/供应链对毛利产生披露级冲击；
  - 刷新后估值模型显示市场预期与 Services 货币化路径明显背离。
- knowability: `partially_knowable` — moat 来源可知；侵蚀速率（监管终局 + AI 重构）当前 `unknowable_now`，列为 watch 而非强行给方向。

注: 本输出为研究判断，非投资建议；不含买卖/仓位结论。如需把 moat 结论桥接到 actionability，需补时间窗口、持仓语境、失效条件与刷新后的估值锚。

---

## Progressive Follow-Up

1. 这次 moat 研究是服务于 watchlist 长期跟踪，还是要升级成正式 durable thesis（写入 thesis ledger）？
   - route_binding: `task_mode` (first_pass_research → thesis_system_update) / `loops/thesis-update-loop.md`
   - object_anchor: AAPL 安装基数 × Services 货币化护城河闭环
   - decision_impact: `readiness_level`（working_view → active thesis，需补刷新后的估值锚与 consensus）

2. 你更想压力测试哪条侵蚀路径作为下一层证据：App Store 监管终局，还是 AI 入口对「设备即默认入口」转换成本的削弱？
   - route_binding: `selected_overlays`（market-structure-policy vs 产品/生态）/ `skills/sec-filing-analysis` 补 10-K 风险因素细节
   - object_anchor: AAPL 生态封闭性与 Services 抽成经济
   - decision_impact: `evidence_path`（决定下一轮拉哪类一手披露 / 监管文件）

3. 是否要把「moat 是否被市场充分定价」这条 source_gap 关掉？这需要刷新当前价格、PE、市值与 sell-side consensus。
   - route_binding: `quant_dependency` (low → medium) / `calculation_gate` (waived → required)
   - object_anchor: AAPL 估值锚 + Services 隐含预期
   - decision_impact: `calculation_depth` / `actionability_boundary`（缺当前市场数据与 consensus，目前无法升级到 actionability）
