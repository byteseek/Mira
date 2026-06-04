# Mira: NVDA 预期差在哪？

## 路由卡 (analysis-routing)

| 字段 | 值 |
| --- | --- |
| `interaction_mode` | `quick_answer`（要方向，不要完整 package） |
| `primary_intent` | variant-perception：刻画 NVDA 的预期差结构 |
| `secondary_intents` | 无（裸"预期差"问题，未叠加动作语或持仓语境） |
| `execution_order` | 单任务 |
| `scope_confirmation_required` | `no` |
| `task_mode` | `thesis_system_update`（预期差判断走 variant-perception lens） |
| `research_object` | `single_equity` — NVIDIA Corp (NVDA), 美股 |
| `market_scope` | US large-mega |
| `time_boundary` | `medium_term_revision`（2Q–8Q / FY1–FY2），含 `transition` 张力 |
| `depth_mode` | `quick_map` |
| `information_value` | `medium` |
| `knowability_status` | `partially_knowable` |
| `decision_pressure` | `none`（裸预期差问题，未触发 actionability gate） |
| `framing_risk` | `none` |
| `disconfirmation_required` | `no` |
| `quant_dependency` | `high` |
| `calculation_gate` | `required` → 本轮 `waived`（无实时数据，降级为 `source_gap` / `calculation_gap`） |
| `selected_lenses` | `variant-perception` |
| `readiness_level` | `working_view` |

> 证据纪律声明：今天 2026-06-04，我没有联网/实时行情或最新财报数据。下文不给具体股价、收入、毛利率、目标价或倍数。凡需数字处用 `source_gap` / `calculation_gap` 标注。

## 研究判断：NVDA 的预期差"在哪一层"

预期差 = 市场共识与可被证据修正的真实变量之间的缺口。NVDA 被研究得极透，纯方向 alpha 薄，真正的预期差只可能藏在共识难以定价的变量上。

### 共识代理 (consensus proxy) — inference
- sell_side_proxy：一致预期集中在"数据中心收入继续高增 + 毛利维持高位 + 下一代平台按节奏放量"。具体数值 = `source_gap`。
- price_action_proxy：典型"beat 但卖事实"，高预期已被价格吸收。具体 = `source_gap`。
- narrative_proxy：多头="AI capex 超级周期 + 收税者 + CUDA 护城河"；空头="定制硅替代 + capex 见顶 + 毛利不可持续 + 客户集中度"。

### 可能被错价的变量 (what is mispriced) — judgment
预期差不在"NVDA 好不好"（共识），而在以下变量的斜率与持续性：
1. 超大客户 capex 的持续性与"消化期"——收入二阶导比绝对水平更易错价。
2. 毛利率可持续性——定制硅竞争、组合、HBM/CoWoS 成本、定价权。
3. 训练→推理的竞争替代速度——市场常把训练份额外推到推理。
4. 需求质量——真实部署 vs 提前拉货/囤货。
5. 估值已 price-in 的预期路径——隐含预期具体数字 = `calculation_gap`。

> judgment_confidence: low-medium。reversal_condition：若刷新数据显示一致预期已显著下修（市场已把减速/毛利风险 price in），则"减速类"预期差消失。

### 重估路径 — inference
catalyst：下一份季报与指引、超大客户 capex 表态、新代际放量、供给瓶颈、竞争份额数据。注意 NVDA 常"基本面修正与价格反应背离"，价格反应只作 `market_pricing`，不当基本面验证。

### 证伪条件 — judgment
"存在可用预期差"在以下情况失效：一致预期已充分计入减速/毛利压缩；需求与毛利多季持续超共识且无替代松动；关键变量被证实为 `irreducible_uncertainty`，此时应 `watch_only`。

## 结论
`thin variant`（working_view）。真正可能的预期差集中在三条数量变量的二阶特征：超大客户 capex 拐点、毛利可持续性、训练→推理替代速度。当前都需新财报/指引才能定位（`partially_knowable`），本轮以 quick_map + 证据纪律收口，不强行给方向。本输出为研究判断，非交易建议；未涉及仓位、买卖、目标价。

### 刷新条件
- stale_after：下一份 NVDA 季报/业绩会，或重大 AI capex / 供应链 / 竞争披露。
- must_refresh_if：拿到 FY1/FY2 一致预期；下一季毛利指引；超大客户 capex 指引变化；推理份额或定制硅替代硬数据。

## Progressive Follow-Up
1. 你这次"预期差"是服务 watchlist / working view，还是后续接成 thesis 更新或"是否参与"的 actionability 判断？
   - route_binding: `task_mode`（view_continuity vs thesis_system_update vs actionability-risk-control）
   - object_anchor: NVDA 数据中心收入斜率 / 毛利 / 客户集中度
   - decision_impact: `output_package` 与 `actionability_boundary`
2. 时间边界锁哪档：下 1–2 季 FY1/FY2 revision，还是 2–3 年训练→推理竞争终局？
   - route_binding: `time_boundary` / `horizon_bucket`
   - object_anchor: NVDA capex 周期 vs CUDA/代际护城河
   - decision_impact: `boundary` + `evidence_path`
3. 能否提供（或允许联网取）一致预期数值与当前估值锚？
   - route_binding: `calculation_gate`（waived → required）
   - object_anchor: NVDA 当前价/EV、FY1-FY2 一致收入与毛利、隐含倍数
   - decision_impact: `calculation_depth` + `readiness_level`
