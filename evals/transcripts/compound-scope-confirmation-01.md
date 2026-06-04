Mira Mode.

# 路由卡 (Analysis Routing)

**Step 0 — 意图入口 (复合 prompt 拆分)**

- `interaction_mode`: `decision_support`（携带持仓语境"都重仓了"，必须联动 Step 0.5）
- `primary_intent`: NVDA 本次财报事件分析（earnings_event / single_equity）
- `secondary_intents`:
  1. AMD 同期对比（earnings_event peer cross-check / single_equity）
  2. 双标的持仓语境（position_or_portfolio — 但无真实持仓数据）
- `execution_order`: NVDA 财报判断框架 → AMD 对比维度 → 持仓相关只做研究边界，不做仓位结论。
- `scope_confirmation_required`: `yes`（深度与数据冲突：财报分析需要实际数字，而我当前无联网；持仓 review 需要权重成本，你都没给）
- `routing_assumptions`（assumption_confidence: low）: 对象=NVDA(主)+AMD(对比)；time_boundary=财报驱动 1Q_2Q；"看财报+对比"=方向性研究判断，不是下单或给仓位。

**Step 0.5 — Decision Pressure Gate（强制输出）**

- `decision_pressure`: `low`（你陈述了持仓事实，但没有问"能不能加/要不要减"；未出现动作语）
- `framing_risk`: `position_defense`（问题结构锚定在"我重仓的两只"上，天然倾向找确认证据；标注问题结构，非心理推测）
- `disconfirmation_required`: `yes`（因 framing_risk 非 none）→ 见下方反向检验

**核心路由字段**

- `task_mode`: `earnings_event`（主）→ skills/earnings-report-analysis
- `research_object`: single_equity × 2（NVDA, AMD）
- `market_scope`: US equities / 美股半导体
- `time_boundary`: 1Q_2Q，可升级 medium_term_revision
- `depth_mode`: `quick_map`（受 source 限制）
- `information_value`: `low`；`knowability_status`: `unknowable_now`（关键变量=本次实际营收/毛利/指引 vs 一致预期，当前不可得）
- `private_state_action`: `waive`（提到重仓，但未给权重/成本/风险预算）
- `quant_dependency`: `high`；`calculation_gate`: `required` → 当前 `calculation_gap`
- `readiness_level`: `working_view`

# 研究判断

## 关键事实状态 (Facts)
- `source_gap`（决定性）：当前没有联网，也没有 NVDA / AMD 本次财报的实际数据、一致预期或财报后股价反应。今天是 2026-06-04。
- 不会编造任何具体财报数字、增速、毛利率或股价。
- 时点提示：NVDA 财季通常滞后日历季约一个月，AMD 日期不同 → 两者大概率不是完全同期披露，做对比存在 timing_mismatch 风险。

## 正确的读法 (Inferences — 框架级)
NVDA 本次财报真正定价的变量：数据中心分部同比/环比+指引；下季指引 vs 一致预期；毛利率方向；供给/产能口径与客户集中度；业绩会 Q&A delta。
AMD 对比：既是独立持仓又是 NVDA read-through，别混。维度=数据中心/AI 加速器份额方向、定价权、毛利质量、指引可信度。关键问题：增长是行业 beta（AI capex 周期）还是公司 alpha（份额转移）。若两只都靠同一 beta，则"两只"其实是一笔重复 bet。

## 反向检验 (Disconfirmation — 因 framing_risk = position_defense 强制)
> 把问题反过来问：如果你没有持有这两只，仅看证据，这次财报会让我更想买，还是更警惕？

- NVDA 与 AMD 高度暴露于同一个 AI 数据中心 capex 周期，重仓两者很可能不是分散，而是对单一产业变量的加倍下注。一份财报里若 AI 需求出现降速信号，两只会同向回撤。
- `reversal_condition`：若财报显示二者增长由不同驱动（AMD 靠份额转移、NVDA 靠新代际+软件/网络生态），且毛利与指引各自独立改善，则"重复 bet"担忧减弱。
- judgment_confidence: low。这是研究视角，不是减仓指令。

## 信息价值与诚实终态
information_value: low + knowability_status: unknowable_now：在拿到实际财报数字+一致预期前，深挖不会提高判断质量。当前可交付的最高价值=待验证变量清单。

## 刷新条件 (Refresh)
- `stale_after`: 一旦你提供（或我能联网取到）NVDA/AMD 本次财报新闻稿+transcript+一致预期。
- `must_refresh_if`: 任一公司财报实际数字可得 → 启用 earnings-analysis 全流程；拿到一致预期 → 才能谈"预期差"；你给出持仓权重/成本 → 才可进入 position_review（否则保持 research_only）。

## Progressive Follow-Up

1. 你手上有没有这两份财报的新闻稿或一致预期数字可以贴给我？
   - route_binding: earnings-report-analysis skill / calculation_gate: required → fillable
   - object_anchor: NVDA 数据中心分部+下季指引；AMD AI 加速器份额与毛利率
   - decision_impact: `evidence_path` + `readiness_level`
2. 你更想要哪层结论：NVDA 本次是否超预期/指引是否改 FY，还是 NVDA vs AMD 的相对质量排序？
   - route_binding: time_boundary / peer cross-check 深度
   - object_anchor: 两者数据中心增长的 beta vs alpha 拆分
   - decision_impact: `boundary` + `output_package`
3. 这"两只都重仓"要不要进入仓位/组合视角（检查是否为对 AI capex 周期的重复 bet）？需要你提供各自权重、成本、风险预算。
   - route_binding: position_review_loop / portfolio-construction-review + Step 0.5 重算
   - object_anchor: NVDA+AMD 在你组合中的合计 AI-周期暴露
   - decision_impact: `actionability_boundary`（无持仓数据则保持 research_only / no_position_data）

*这是研究输出，不是交易建议。当前无实时数据，所有数字级结论标记为 source_gap / calculation_gap。*
