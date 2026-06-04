# Mira Golden Routing Examples

These are golden routing cards: a user prompt and the routing output Mira should
produce before any analysis. They double as few-shot references and as a manual
regression fixture for [../loops/analysis-routing.md](../loops/analysis-routing.md).
They are routing examples, not investment recommendations. Key fields are
validated by `scripts/validate_repo.py`.

- not_investment_advice: true
- purpose: lock routing behavior for ambiguous prompts (预期差 sense, interaction_mode vs depth_mode, knowability, compound intent)

Each card shows only the routing-critical fields. A full task would also record
the remaining Required Routing Output fields.

## 1. Bare 预期差 is research, not actionability

Prompt: `Mira, NVDA 的预期差在哪？`

- `interaction_mode`: `routed_research`
- `primary_intent`: variant-perception research on NVDA
- `task_mode`: `thesis_system_update`
- `research_object`: `single_equity` (NVDA)
- `selected_lenses`: `variant-perception`
- `decision_pressure`: `none`
- `framing_risk`: `none`
- `disconfirmation_required`: `no`
- routing_basis: 裸预期差是“市场预期 vs 我的预期”的研究问题，进 variant-perception lens / thesis update，不强制 actionability。

Counter-example — same object, action-paired:

Prompt: `Mira, NVDA 预期差兑现了，现在还能不能加？`

- `interaction_mode`: `decision_support`
- `task_mode`: `thesis_system_update` → actionability bridge
- `decision_pressure`: `medium`
- `framing_risk`: `position_defense` (问题锚定在“已有 / 想加的仓位”上，描述问题结构而非用户心理)
- `disconfirmation_required`: `yes`
- routing_basis: 叠加动作语 + 持仓语境，必须 load actionability risk-control，并给反向检验。

## 2. quick_answer + quick_map (shape and effort agree)

Prompt: `Mira, 看一下 AAPL 方向就行`

- `interaction_mode`: `quick_answer`
- `depth_mode`: `quick_map`
- `user_visible_routing_card`: 一行假设条
- routing_basis: 用户要一句话方向，研究也只需浅层 triage。

## 3. quick_answer + deep_dive (shape and effort diverge)

Prompt: `Mira, 一句话告诉我 CRWV 现在贵不贵`

- `interaction_mode`: `quick_answer`
- `depth_mode`: `deep_dive`
- `quant_dependency`: `high`
- `calculation_gate`: `required`
- routing_basis: 输出形状是一句结论，但“贵不贵”要靠估值 / 隐含预期才能诚实回答；研究深、答案短。不要因为是 quick_answer 就跳过 valuation 工作。

## 4. Knowability terminal

Prompt: `Mira, 下个月 CPI 会不会超预期？`

- `interaction_mode`: `quick_answer`
- `information_value`: `low`
- `knowability_status`: `unknowable_now`
- routing_basis: 单月数据点由不可知变量主导，深挖不提高判断质量。输出方向性区间 + 可观察刷新条件，不强行给点估计。

## 5. Compound prompt decomposition

Prompt: `Mira, 看 NVDA 这次财报，顺便对比 AMD，这俩我都重仓了`

- `primary_intent`: NVDA earnings event
- `secondary_intents`: [AMD peer / industry compare, position review of both]
- `execution_order`: earnings → peer compare → position review
- `scope_confirmation_required`: `yes`
- `decision_pressure`: `medium` (持仓语境 + “都重仓了”)
- routing_basis: 复合 prompt，先确认范围再花 depth 预算；持仓部分进 position review，无真实持仓数据时保持 `research_only`。
