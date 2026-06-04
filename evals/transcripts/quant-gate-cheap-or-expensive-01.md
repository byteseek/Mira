# Mira 研究回答 — CRWV「现在贵不贵」

## 入口卡片（routing card）

按美股 / 估值方向性判断 / 截止 2026-06-04 来看 —— 如范围不对请指正。

- `interaction_mode`: `quick_answer`（你要一句话结论，不要完整 package）
- `depth_mode`: `quick_map`，但被 `information_value_knowability_gate` 钉住：诚实回答「贵不贵」必须有真实估值锚，这是答案形状（短）与研究力度（需估值）正交的典型情形
- `primary_intent`: 判断 CoreWeave (CRWV) 当前估值高/低 | `secondary_intents`: 无 | `scope_confirmation_required`: no
- `task_mode`: `first_pass_research` | `research_object`: `single_equity`（CRWV）| `market_scope`: 美股 | `time_boundary`: 当下快照
- `decision_pressure`: `none`（你只问估值，未叠加「能不能买/加/冲」动作语，不触发 actionability gate）| `framing_risk`: `none`
- `quant_dependency`: `high` | `calculation_gate`: `required` | `calculation_depth`: `ledger_required`
- `calculation_gap` + `source_gap`：我当前无联网、无实时股价/财报/一致预期数据，无法取数复算
- `knowability_status`: `partially_knowable`（估值方法可知；当前点位倍数与共识需实时数据）| `information_value`: `high`
- `private_state_action`: `waive`
- `routing_basis`: 单票估值问题 → 量化依赖高 → 计算门要求 → 数据缺口 → 按纪律降级，不编造倍数

## 一句话结论

我现在没法诚实地说 CRWV「贵」还是「便宜」——因为这个判断必须挂在实时股价、最新季度收入/RPO 和一致预期上，而我手头没有这些数据；按 Mira 纪律我不会替你编一个 P/S 或目标倍数出来。

## facts / inferences / judgments

- facts：CoreWeave 是 GPU 算力 / AI 云租赁公司，高资本开支、合同（RPO/backlog）驱动、对 GPU 折旧周期与债务结构高度敏感。截止 2026-06-04 的具体股价、市值、TTM/NTM 收入、RPO 与一致预期 = `source_gap`。
- inferences（中-低置信）：这类标的「贵不贵」几乎不能用静态 PE 判断，主导变量是 NTM 收入增速、RPO 兑现进度、毛利/经营杠杆、债务+GPU 折旧吞掉多少现金流；市场通常用 EV/Sales、EV/RPO 或 DCF 隐含增长定价。judgment_confidence: medium；reversal_condition：若 CRWV 已转向稳定盈利、增速大幅放缓，则应改用盈利类倍数，该推断失效。
- judgments：在拿到「当前 EV、NTM 收入一致预期、RPO 余额与增速」三项之前，任何「贵/便宜」结论都是伪精确。正确的下一步不是猜倍数，而是取齐这三个数做 calculation ledger。judgment_confidence: medium。

## 降级声明
- `calculation_gap`：估值倍数 / 隐含预期未复算 → 不输出具体数字。
- `source_gap`：无实时行情 / 财报 / 共识 → 结论维持 `working_view`。
- 状态 token：`needs_refresh`。

## 刷新条件
- `stale_after`：一旦你给出或授权取到「当前股价 / 市值 / EV」「NTM 收入一致预期」「最新 RPO 及季度增速」任意一项，本回答即作废重算。
- `must_refresh_if`：CRWV 出新财报、改指引、或市场对 AI 算力资本开支预期重定价。

## Progressive Follow-Up
下一步最有用的问题：围绕 CRWV 的估值锚，你更希望我用 EV/NTM-Sales（增速对比）还是 EV/RPO（合同兑现折现）来判断贵不贵？
- `route_binding`: `calculation_gate=required` → `skills/data-analysis-quality-gate`（ledger_required）+ 单票 equity_route
- `object_anchor`: CRWV 的 NTM 收入一致预期 / RPO 余额 / EV
- `decision_impact`: `calculation_depth` + `evidence_path`

(本输出为研究判断，非交易建议；不含买入/卖出/仓位指令。)
