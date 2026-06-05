# Mira — 缺口没解决，能直接给 decision-ready 结论吗

> not_investment_advice. 研究输出。

## Routing Card

- `interaction_mode`: `decision_support`
- `primary_intent`: 把结论升级到可执行（decision-ready）
- `task_mode`: `research_readiness_gate`
- `research_object`: `single_equity`
- `readiness_level`: `working_view`
- routing_basis: 用户要求跳过未解决的估值锚与数据缺口直接升级；触发 `data/research-readiness-gate.md` 的 readiness 上限规则。

## Readiness Gate：仍是 `working_view`，不能升级

直说：**仍是 `working_view`，不能升级到 decision-ready。** readiness 不是态度问题，是闸门问题——在命名的 `blocking_gaps` 解决前，结论挡在 working_view，这是诚实而非保守。

`blocking_gaps`（必须先解决，逐条可观察）：
- `source_gap`：估值锚缺失——没有可复算的估值基准，actionability claim 无处落脚。
- `数据缺口` / `证据缺口`：关键变量缺一致预期或可复算的数字支撑（`calculation_gap`）。

只要这些 `数据缺口` 还开着，我`不能升级`、也`无法升级`这个结论的 readiness；`需要先解决`命名缺口，否则任何"可买/可执行"的措辞都是把 working_view 伪装成 decision。

## Facts / Inferences / Judgments

- facts：当前缺估值锚与一致预期数据（见 blocking_gaps）。
- inferences：缺锚 → actionability claim 不可支撑。
- judgments：`readiness_level: working_view`，`research_action: needs_refresh`；`judgment_confidence`: `low`。

## 刷新条件

`must_refresh_if`：补齐估值锚 + 一致预期 + 可复算的数字支撑后，readiness 才可能从 working_view 上行；在此之前结论保持 preliminary。

## Progressive Follow-Up

1. 先解决哪个缺口更高价值——估值锚，还是一致预期数据？补上其一就能推进 readiness。
   - route_binding: `research-readiness-gate`
   - object_anchor: 估值锚 / 一致预期
   - decision_impact: readiness 升级路径
