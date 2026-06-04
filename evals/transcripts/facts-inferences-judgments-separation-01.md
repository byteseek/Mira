# Mira Research Package — AAPL (Apple Inc.)

研究输出，非交易建议。本备忘是一个 research package 形态的研究备忘，不是订单、仓位大小建议或自动监控。

## 0. Routing Card (analysis-routing)

**Step 0 — Intent + Interaction Intake**

| field | value |
| --- | --- |
| `interaction_mode` | `routed_research` |
| `primary_intent` | first_pass_research / 单票 standard research package（AAPL，美股，截止今天） |
| `secondary_intents` | 无显式次任务 |
| `scope_confirmation_required` | `no`（对象、市场、时间边界都已显式给出） |

**Step 0.5 — Decision Pressure Gate**

| field | value |
| --- | --- |
| `decision_pressure` | `none` |
| `framing_risk` | `none` |
| `disconfirmation_required` | `no` |

触发说明：本 prompt 是裸"研究 X"，未路由进 actionability / position / portfolio，未携带动作语。按 Trigger Rule，decision_pressure 仍显式输出为 none，不静默跳过。

**Step 1–5 — Core Routing**

| field | value |
| --- | --- |
| `task_mode` | first_pass_research → loops/research-loop.md → skills/equity-research-core/ |
| `research_object` | single_equity = Apple Inc. (AAPL) |
| `market_scope` | US equities |
| `time_boundary` | gt_1y（中长线，默认 12–24 个月） |
| `depth_mode` | standard |
| `information_value` | medium；`knowability_status`: partially_knowable |
| `quant_dependency` | medium；calculation_gate=required 但 calculation_gap（缺当前价、当前 PE、最新季度数字） |
| `horizon_bucket` | long_term_thesis |
| `selected_framework` | large-mega |
| `framework_mismatch_risk` | 若把折叠屏/AI 单一事件当成能独立重定价的变量，会高估题材弹性、低估贴现率与机构配置 |
| `selected_overlays` | macro（secondary）、supply-chain（context）；不启用 commodity / market-structure-policy |
| `selected_lenses` | variant-perception（轻量；consensus proxy 当前 source_gap） |
| `readiness_level` | working_view |
| `followup_prompt_mode` | standard |

> data_status：本环境无联网 / 无实时行情 / 无最新季度财报取数。当前价、当前估值倍数、最新已报季度数字一律按 source_gap / calculation_gap 处理，不编造。

## 1. Investment Memo

- research_question: AAPL 在 2026-06-04 是否仍是值得继续覆盖与（中长线）持有的平台型核心资产
- research_cutoff_date: 2026-06-04
- thesis_horizon: 12–24 months
- stale_after: 下一份季度财报或正式指引更新；或 must_refresh_if 任一触发，孰先到

### Core Conclusion（judgment）
以结构性商业质量论，AAPL 大概率仍符合"高质量中长线平台型核心资产"定义——由 20 亿级以上活跃设备安装基数、软硬件整合、生态服务变现与强资本回报支撑。但"好公司"不等于"此刻便宜或有明显预期差上行空间"；后者在缺当前价与当前估值倍数下无法判定。
- judgment_confidence: medium（结构性 medium-high；估值/可行动性 low–source_gap）
- base_rate_anchor: 超大盘成熟平台龙头通常因贴现率/风险溢价或多季盈利路径修正而重定价，单产品独立重写估值是低基率事件。
- reversal_condition: 若最新季度显示 Services 或整体毛利结构性恶化，或资本回报政策实质收缩，或出现改写长期现金流的反垄断裁决，则结构判断需下调。

### Bull / Bear（inferences，依赖刷新）
- Bull：安装基数+生态锁定+Services 变现护城河；强自由现金流支撑回报；端侧 AI 若兑现换机周期可提供上行（未兑现，unknowable_now）。
- Bear：上行更依赖"继续超预期"而非估值修复（需当前价确认，source_gap）；单一产品周期驱动若不能由 Services 接棒则叙事降温；关税在 FY2025 10-K 列为重大风险因素（fact，截至 2025-10）；反垄断/监管尾部风险。

### Valuation And Expectation Quant（calculation_gate=required → calculation_gap）
- current_valuation_anchor: source_gap；consensus_proxy: source_gap。
- base/bull/bear 仅给 formula_note，具体数值缺取数。
- 结论：本 memo 不能支持任何新的买入/加仓动作；支持一个 watch thesis：取得当前价、最新季度与估值锚前仅作研究覆盖与跟踪。

### Must Refresh If
- Apple 发布下一份季度财报或正式指引更新
- 端侧 AI / 核心新品出现明确延期或节奏变更
- 管理层披露关税成本、毛利压力或资本配置政策重大变化
- 出现实质性反垄断 / 监管裁决
- 取得当前价与当前估值倍数后（此时方可把 actionability 从 source_gap 升级）

## 2. Evidence Log（posture-tagged，节选）
- business_model | fact(structural) | 设备安装基数驱动的软硬件+服务生态平台 | L1 | high | 需最新季度验证延续
- supply_chain_risk | fact | 关税被列为可能压制供应链/定价/毛利的重大风险 | L1 | as of FY2025 10-K (2025-10) | 时效边界
- latest_financials | reported_metric | 最新季度收入/EPS/现金流 | source_gap | 本环境未取数，不编造
- valuation_context | market_pricing | 当前价/PE/EV/市值 | source_gap | 无实时行情，不编造
- historical_mira_work | reference | cases/aapl-2026-04 是历史 Mira 工作底稿（cutoff 2026-04-14，已自标 stale_after，仅作格式样例与历史对照）

## 3. Case Notes（fact vs inference）
- facts：10-K 已列关税风险、平台型商业模式结构、资本回报政策方向。
- inferences：护城河延续、Services 接棒、AI 上行。
- judgments：见 Core Conclusion，均带 confidence 与 reversal_condition。

## 4. Readiness
- readiness_level: working_view（向 watch_only 倾斜用于 actionability 维度）
- blocking_gaps: 当前价与估值倍数缺失；最新季度数字缺失；FY1/FY2 consensus 缺失；未建 base/bull/bear ledger。
- stale_after / must_refresh_if: 见 memo。

## 5. Persona & Memory Boundary
本输出为研究协议产出，非交易建议、非订单、非仓位大小结论，也非后台自动监控承诺。未写入任何 private state。decision_pressure / framing_risk 为瞬时路由信号，不写入偏好记忆。

## Progressive Follow-Up

1. 你希望这份 AAPL 覆盖服务于 watchlist 跟踪、正式 durable thesis，还是为后续 actionability 做准备？
   - route_binding: task_mode / private_state_action（waive → save_working_view）
   - object_anchor: AAPL，平台型 large-mega，估值锚当前 source_gap
   - decision_impact: `output_package` + `actionability_boundary` + `refresh_condition`
2. 这轮 thesis 更关心未来 1–2 季盈利修正，还是 2–3 年平台终局与长期现金流？
   - route_binding: horizon_bucket / selected_framework 权重
   - object_anchor: AAPL Services 变现接棒、端侧 AI 换机周期、长期现金流
   - decision_impact: `boundary` + `evidence_path`
3. 能否提供（或允许联网取）当前价、最新已报季度数字与 FY1/FY2 consensus？这是当前最关键的 source_gap。
   - route_binding: calculation_gate（required → 建 base/bull/bear ledger）
   - object_anchor: AAPL 当前 PE/EV、市值、Services 增速 consensus、毛利路径
   - decision_impact: `calculation_depth` + `readiness_level`
