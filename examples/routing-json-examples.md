# Mira Routing JSON Examples

These examples show the machine-first routing contract. The `routing.json`
object is the canonical routing artifact; any user-visible routing card is a
depth-scaled rendering of that object, controlled by
[../data/output-surface-matrix.md](../data/output-surface-matrix.md).

`scripts/validate_repo.py` validates every JSON block in this file against
[../schemas/routing.schema.json](../schemas/routing.schema.json). Keep examples
small, schema-valid and behaviorally meaningful.

## 1. Quick Map Surface

Prompt: `Mira, 看一下 AAPL 方向就行`

Machine routing object:

```json
{
  "schema_version": "routing.v1",
  "interaction_mode": "quick_answer",
  "primary_intent": "directional quick map on AAPL",
  "task_mode": "first_pass_research",
  "research_object": "single_equity:AAPL",
  "market_scope": "US equities",
  "time_boundary": "as_of_today",
  "depth_mode": "quick_map",
  "information_value": "medium",
  "knowability_status": "partially_knowable",
  "primary_skill_or_loop": "skills/equity-research-core/SKILL.md",
  "routing_basis": "User asked for a one-line direction, so answer shape is quick_answer and research depth is quick_map.",
  "followup_prompt_mode": "light",
  "followup_questions": [
    {
      "question": "Should the AAPL quick map focus on near-term revision or long-term services and AI durability?",
      "rung": "Rung B - pricing_variable_or_consensus",
      "route_binding": "time_boundary",
      "object_anchor": "AAPL revision versus services/AI durability",
      "decision_impact": "evidence_path"
    }
  ]
}
```

Visible routing card:

```text
按美股 / quick_map / 截止今天看 AAPL；先给方向性 working view，若要判断贵不贵或能不能动，再升级 valuation / actionability 路由。
```

## 2. Standard Research Surface

Prompt: `Mira, 研究 NVDA，标准 research package，重点看 Blackwell 供给和云厂 capex 是否还能支撑上修。`

Machine routing object:

```json
{
  "schema_version": "routing.v1",
  "interaction_mode": "routed_research",
  "primary_intent": "standard NVDA research package focused on Blackwell supply and hyperscaler capex revision path",
  "task_mode": "first_pass_research",
  "research_object": "single_equity:NVDA",
  "market_scope": "US equities",
  "time_boundary": "FY1_FY2_revision",
  "depth_mode": "standard",
  "information_value": "high",
  "knowability_status": "partially_knowable",
  "quant_dependency": "high",
  "calculation_gate": "required",
  "primary_skill_or_loop": "skills/equity-research-core/SKILL.md",
  "routing_basis": "The question depends on revision, valuation-implied expectations and peer/customer read-through, so it requires standard single-equity research with quant gate.",
  "expected_output_package": "research-package",
  "readiness_level": "working_view",
  "private_state_action": "waive",
  "followup_prompt_mode": "standard",
  "followup_questions": [
    {
      "question": "Should consensus proxy be anchored to FY1/FY2 data-center revenue, gross margin, or hyperscaler capex read-through?",
      "rung": "Rung B - pricing_variable_or_consensus",
      "route_binding": "quant_dependency",
      "object_anchor": "NVDA Blackwell supply, data-center revenue, gross margin and hyperscaler capex",
      "decision_impact": "calculation_depth"
    },
    {
      "question": "Which evidence would falsify the NVDA revision thesis: Blackwell delivery delay, cloud capex slowdown, or margin compression?",
      "rung": "Rung C - falsification_or_next_route",
      "route_binding": "thesis_system_update",
      "object_anchor": "NVDA Blackwell delivery, cloud capex and margin path",
      "decision_impact": "thesis_state"
    }
  ]
}
```

Visible routing card:

```text
primary_intent: NVDA Blackwell/capex revision research
depth_mode: standard
source/quant boundary: company disclosure, cloud capex read-through, consensus proxy and valuation-implied expectations are required before durable judgment.
readiness_level: working_view until the quant gate is satisfied.
```

## 3. Question Expansion Lens

Prompt: `Mira, 看 NVDA 这次财报，顺便对比 AMD，这俩我都重仓了`

Machine routing object:

```json
{
  "schema_version": "routing.v1",
  "interaction_mode": "decision_support",
  "primary_intent": "earnings event read on NVDA with AMD peer comparison queued before any position review",
  "secondary_intents": [
    "AMD peer comparison",
    "position review of NVDA and AMD"
  ],
  "execution_order": "earnings event -> peer comparison -> position review only after position data is provided",
  "task_mode": "earnings_event",
  "research_object": "single_equity:NVDA",
  "market_scope": "US equities",
  "time_boundary": "latest_earnings_event",
  "depth_mode": "standard",
  "information_value": "high",
  "knowability_status": "partially_knowable",
  "scope_confirmation_required": "yes",
  "primary_question_lens": "comparison_association",
  "selected_question_lenses": [
    "comparison_association",
    "scale_shift"
  ],
  "lens_selection_basis": "The prompt asks for NVDA earnings and AMD comparison while also referencing holdings, so the question must separate event facts, peer read-through, and any later position-review scope.",
  "lens_data_required": "NVDA and AMD same-period earnings disclosures, segment definitions, data-center revenue or GPU proxy variables, guidance, margin paths, and explicit position data before any position review.",
  "lens_failure_mode": "Without same-definition peer data and position context, the answer could treat correlation as causality or turn an earnings comparison into unsupported portfolio advice.",
  "decision_pressure": "low",
  "quant_dependency": "medium",
  "calculation_gate": "required",
  "primary_skill_or_loop": "skills/earnings-report-analysis/SKILL.md",
  "routing_basis": "The primary request is an earnings event read; AMD is a peer-comparison secondary intent, and the holdings language triggers decision-support boundaries without enough data for position conclusions.",
  "expected_output_package": "earnings-package",
  "readiness_level": "working_view",
  "private_state_action": "waive",
  "followup_prompt_mode": "decision_grade",
  "followup_questions": [
    {
      "question": "Should the NVDA versus AMD comparison anchor on data-center revenue, GPU supply constraints, gross margin, or guidance revision?",
      "rung": "Rung B - pricing_variable_or_consensus",
      "route_binding": "primary_question_lens=comparison_association + quant_dependency",
      "object_anchor": "NVDA and AMD earnings read-through variables",
      "decision_impact": "evidence_path"
    },
    {
      "question": "If you want this to become a real position review, can you provide holdings, weights, cost basis, risk budget, and time window for NVDA and AMD?",
      "rung": "Rung C - falsification_or_next_route",
      "route_binding": "position_review",
      "object_anchor": "NVDA and AMD holding context",
      "decision_impact": "position_review_scope"
    }
  ]
}
```

Visible routing card:

```text
primary_intent: NVDA earnings-event read
question lens: compare NVDA and AMD on same-definition variables, while keeping position review separate until real holding data is provided.
readiness_level: working_view until peer definitions, quant checks and position context are available.
```

## 4. Live Data Gate

Prompt: `今天目前大盘是调整还是崩盘？`

Machine routing object:

```json
{
  "schema_version": "routing.v1",
  "interaction_mode": "quick_answer",
  "primary_intent": "intraday broad-market classification as pullback versus crash",
  "task_mode": "monitoring_update",
  "research_object": "broad_market:indexes",
  "market_scope": "US equities by assumption until user corrects",
  "time_boundary": "intraday_current_session",
  "depth_mode": "quick_map",
  "information_value": "high",
  "knowability_status": "knowable",
  "live_data_gate": "required_quote_time",
  "live_freshness_status": "delayed",
  "cross_check_status": "partial",
  "quote_time": "2026-06-05T10:07:00-04:00",
  "source_boundary": "single delayed public aggregator plus timestamped market-news search; downgrade if not cross-checked",
  "primary_skill_or_loop": "loops/monitoring-loop.md",
  "routing_basis": "The prompt asks about today/current market state and uses a strong crash label, so Mira must refresh or search live sources before judging and must show quote time plus freshness caveat.",
  "followup_prompt_mode": "light",
  "followup_questions": [
    {
      "question": "Should the live read use US indexes, A-shares, Hong Kong, or another market as the default broad-market scope?",
      "rung": "Rung A - boundary",
      "route_binding": "market_scope + live_data_gate",
      "object_anchor": "current broad-market snapshot",
      "decision_impact": "source_boundary"
    }
  ]
}
```

Visible routing card:

```text
按默认市场范围 / quick_map / live_data_gate=required_quote_time；先刷新或搜索同日行情，带 quote_time 和 live_freshness_status，再判断“调整”还是“崩盘”。
```
