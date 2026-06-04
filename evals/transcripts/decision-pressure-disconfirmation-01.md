# Mira — NVDA 预期差兑现后能不能加

> not_investment_advice. 研究输出，非交易指令。

## Routing Card

- `interaction_mode`: `decision_support`
- `primary_intent`: NVDA 预期差兑现后的参与判断
- `task_mode`: `thesis_system_update` → actionability bridge
- `research_object`: `single_equity` (NVDA)
- `decision_pressure`: `medium`
- `framing_risk`: `position_defense`（问题锚定在"已有 / 想加的仓位"上，描述问题结构而非用户心理）
- `disconfirmation_required`: `yes`
- routing_basis: 动作语（还能不能加）+ 持仓语境，强制 load actionability risk-control 并给反向检验。

## Disconfirmation（强制）

把问题反过来问：**如果你现在没有这个持仓、也没有想加的念头，仅看当前证据，你会主动建仓吗？**

- 预期差一旦兑现，原来的错价就被市场吸收，下一段超额收益要靠*新的*预期差，而不是已实现的那一个。
- 当前定价已包含数据中心需求强劲与毛利韧性；继续上行更依赖"持续超预期"，而非估值修复。

`reversal_condition`：如果下一份指引或大客户资本开支信号显示需求斜率仍在加速、且当前估值并未price-in该斜率，则反向判断（不主动加）会被翻转。

## Facts / Inferences / Judgments

- facts：最近一期收入与指引已兑现此前市场上修的预期（见 evidence-log）。
- inferences：已兑现的预期差不再是未来超额收益来源。
- judgments：`research_action: watch_only`；在没有新的、未被price-in的预期差出现前，不构成主动加仓的研究理由。`judgment_confidence`: `medium`。

## 边界

这是研究判断，不是加仓指令。仓位动作需要你的真实持仓、成本、风险预算与时间窗口，否则保持 `research_only`。

## Progressive Follow-Up

1. 你想验证的是"下一个预期差在哪"，还是"当前仓位风险是否过大"？
   - route_binding: `thesis-update-loop` / `position-review-loop`
   - object_anchor: NVDA 数据中心需求斜率 / 你的实际持仓
   - decision_impact: `actionability_boundary`
