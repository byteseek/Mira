task_mode: `first_pass_research`
research_object: `single_equity` (NVDA)
depth_mode: `standard`

核心判断：这次 NVDA 研究不能只问 Blackwell 是否供不应求；真正要拆的是 Blackwell 供给兑现、云厂 capex 持续性、FY1/FY2 数据中心收入上修和毛利率路径是否仍能同时成立。当前 readiness 仍应保持 `working_view`，直到 consensus proxy、公司/云厂披露和估值隐含预期被对齐。

事实 / 推断 / 判断：
- facts: 需要公司披露、主要云厂 capex 指引、供应链交付节奏和市场估值数据。
- inferences: 如果 Blackwell 交付和云厂 capex 同时支撑 FY1/FY2 上修，预期差才可能落到变量层。
- judgments: 未复算一致预期和估值隐含预期前，不应把“继续上修”写成高置信 durable conclusion。

刷新条件：`must_refresh_if` NVDA 财报/指引、主要云厂 capex 指引、Blackwell 交付节奏或毛利率口径变化。

## Progressive Follow-Up

1. 你希望我先补哪组 NVDA 证据：Blackwell 交付/供给链，还是云厂 capex 指引和订单持续性？
   - rung: `Rung A - boundary_or_data`
   - route_binding: `source_boundary`
   - object_anchor: `NVDA Blackwell supply and hyperscaler capex`
   - decision_impact: `evidence_path`
2. 对 NVDA 来说，你想把 `consensus proxy` 锚定到 FY1/FY2 数据中心收入、毛利率，还是 capex read-through？
   - rung: `Rung B - pricing_variable_or_consensus`
   - route_binding: `quant_dependency`
   - object_anchor: `NVDA data center revenue, margin and hyperscaler capex`
   - decision_impact: `calculation_depth`
3. 哪个证据会证伪这条 NVDA 上修 thesis：Blackwell 交付延迟、云厂 capex 下修，还是毛利率被供给成本压住？
   - rung: `Rung C - falsification_or_next_route`
   - route_binding: `thesis_system_update`
   - object_anchor: `NVDA Blackwell, cloud capex and margin path`
   - decision_impact: `thesis_state`
