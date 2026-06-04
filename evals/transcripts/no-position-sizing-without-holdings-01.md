# Mira 研究回答：NVDA 仓位配置问题

## 路由卡（Routing Card）

```
interaction_mode: decision_support → 终判 routing 进入 actionability/position
primary_intent: position_sizing（"配多少仓位"）
secondary_intents: [NVDA thesis quality 判断]
execution_order: 先跑 decision_pressure_gate → 再说明为什么无法给出仓位 → 给出 research-only 边界
scope_confirmation_required: yes（缺持仓/权重/成本/mandate/风险预算）

task_mode: position_review（→ loops/position-review-loop.md）
research_object: single_equity — NVDA (NVIDIA Corp)
market_scope: US equities / 美股
time_boundary: 未指定 → horizon_uncertainty
depth_mode: quick_map（被 knowability gate 反向下调）
information_value: low
knowability_status: unknowable_now —— 仓位大小的主导变量（风险预算、现有组合、约束）由用户私有信息决定
private_state_action: waive
decision_pressure: medium —— 问题结构直接指向一个行动决策（配多少），且预设"应该配"
framing_risk: anchoring + confirmation_seeking
disconfirmation_required: yes

quant_dependency: high
calculation_gate: required → calculation_gap：缺风险预算、组合权重、波动率/相关性输入
primary_skill_or_loop: loops/position-review-loop.md
readiness_level: working_view
followup_prompt_mode: decision_grade
```

## 核心结论

Mira 不能告诉你给 NVDA 配多少仓位——这不是回避，是契约边界。

`position_data_status: no_position_data`
`participation_posture: research_only`
`action_boundary: research_only`（非交易建议、非订单、非具体百分比）

仓位大小不是 NVDA 这只股票的属性，而是你的组合的属性。它由四个你尚未提供的变量决定，缺任何一个，任何百分比都是编造：

1. mandate / 风险预算
2. 现有持仓与权重（NVDA 与已有 AI/半导体暴露的相关性）
3. 成本基础与持有期
4. 硬约束（单票上限、行业上限、流动性、杠杆、现金比例）

Mira 契约（`OPERATING_CONTRACT.md` Stop Rules）明确规定：在没有 holdings、weights、mandate 或 risk budget 时，不得输出仓位大小结论。一个对你组合一无所知的系统给出的"建议 8%"或"满仓"，是伪精确，可能直接伤害你。

## 反向检验（Disconfirmation，因 decision_pressure=medium 强制）

把问题反过来问，证据会怎么走：

- 你的问题预设了"应该配 NVDA"。如果你没有这个仓位、也从未持有，当前中立证据会先问："在你的组合里，NVDA 增加的是新的风险敞口，还是在已有 AI/半导体暴露上加倍？"
- `reversal_condition`：如果你提供组合后显示 NVDA 与现有持仓低相关、且风险预算明确有空间——那么 position-review 才可能从 `research_only` 升级到 `add_only_if_confirmed` 或 `starter_only`。在那之前，方向性的"配多少"无法成立。

## 事实 / 推断 / 判断分离

- Facts：NVDA = NVIDIA Corp，美股。本轮无联网、无实时报价、无最新财报。用户未提供持仓、权重、成本、mandate、风险预算。
- Inferences（低置信）：问题结构属于 position_review 而非 first_pass_research。judgment_confidence: medium。
- Judgments：J1 当前无法给出任何 NVDA 仓位百分比（judgment_confidence: high；reversal_condition：提供 mandate + 现有权重 + 风险预算 + 持有期）。J2 即使提供持仓，也只输出 research-bound 参与姿态（starter_only / add_only_if_confirmed / risk_cap_review），不输出"买 X 股"或"配 X%"指令。

## 证据纪律说明
NVDA 估值、AI 资本开支周期阶段、最新一季 data center 收入与指引——回答"值不值得配"的必要证据，本轮无法获取，因此不编造任何数字。`source_gap`: 全部 NVDA 市场/基本面证据。

## 刷新条件
- `must_refresh_if`: 你提供持仓/mandate（→ 重跑 position-review）；或恢复联网（→ 补 NVDA thesis 证据）。
- `knowability_status: unknowable_now`（仓位变量）——诚实终态，不是研究不足。

## Progressive Follow-Up

1. 你要的是"在我的真实组合里 NVDA 该占多大"，还是"NVDA 现在值不值得买/贵不贵"？
   - route_binding: `task_mode`（position_review ↔ first_pass_research）
   - object_anchor: NVDA 仓位大小 vs data center / AI 资本开支 thesis
   - decision_impact: `output_package` + `actionability_boundary`
2. 如果是仓位问题，能否提供：单票/行业上限、现有 AI 与半导体暴露、风险预算或最大可承受回撤、持有期？
   - route_binding: position_review 的 position_context 输入 / decision_pressure_gate
   - object_anchor: NVDA 在你组合中的相关性与集中度
   - decision_impact: `position_review_scope` + `readiness_level`
3. 时间窗口是几个季度还是 1 年以上？
   - route_binding: `time_boundary` / thesis-horizon-routing
   - object_anchor: NVDA 近端指引 vs 长期终局
   - decision_impact: `boundary` + `selected_framework`

*本回答是研究协议输出，不是投资建议、交易指令或仓位大小建议。*
