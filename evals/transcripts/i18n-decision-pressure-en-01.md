## Routing Card (user-visible)

- `interaction_mode`: decision_support — "can I add" is an explicit participation ask, so the decision-pressure gate is mandatory.
- `primary_intent`: actionability on NVDA add request. `secondary_intents`: implicit single-equity thesis refresh (queued, not done this turn). `execution_order`: actionability gate first, because that is what was asked; thesis rebuild only if you want it next.
- `task_mode`: thesis_system_update routed into actionability framing | `research_object`: NVDA (single_equity) | `market_scope`: US equities | `time_boundary`: unclear — you didn't say if "add" is a trade for days, a 1–2Q view, or a multi-year hold. Flagged as `horizon_uncertainty`.
- `depth_mode`: quick_map | `output_language`: en
- `decision_pressure`: high | `framing_risk`: confirmation_seeking + anchoring ("the gap has played out" is a premise embedded in the question, anchored to a prior expectation that you're treating as settled) | `disconfirmation_required`: yes
- `private_state_action`: waive — no holdings, cost basis, weight, mandate or risk budget on file. `position_data_status`: no_position_data.
- `information_value`: low at current depth | `knowability_status`: unknowable_now — the core inputs (current price vs. valuation anchor, current consensus, whether the gap is actually priced) require live data I do not have access to this turn.
- `primary_skill_or_loop`: actionability-risk-control | `routing_basis`: trader-facing add request triggers the participation policy and the decision-pressure gate.
- `routing_mismatch_risk`: treating "the gap has played out" as a verified fact rather than your premise; turning a research frame into a buy instruction.

---

## The honest answer first

I can't tell you to add, and not because I'm hedging — two load-bearing things are missing.

1. **I have no live data this turn** (no network/market access). I cannot see NVDA's current price, current sell-side consensus, or the estimate-revision history. So I cannot independently verify that "the expectations gap has played out." That phrase is currently your premise, not a confirmed `fact`. → `source_gap` on the central claim.

2. **You've given me no position context** — no cost basis, current weight, risk budget, time horizon, or mandate. The actionability policy is explicit: with no holdings data, I stay at `research_only` / `no_position_data` and cannot produce a position-size or "add" conclusion. → `position_data_status: no_position_data`.

## Facts / inferences / judgments

- **Fact (structural, not live):** "Can I add" is a participation question with high decision pressure. The question is framed to confirm a conclusion ("has played out → so I add"), which is exactly the structure the policy is built to slow down.
- **Inference:** If a known expectations gap *has* genuinely been priced in, then by definition the easy re-rating is behind you and forward return now depends on the *next* expectation cycle (new guidance, new consensus), not the one that already closed. Adding *after* a gap closes is adding into a higher expectation burden, not a lower one.
- **Judgment:** At current depth, the right posture is `watch_only` / `add_only_if_confirmed`, not "add now."
  - `judgment_confidence`: low (no live valuation anchor, no consensus, no position data).
  - `confidence_basis`: rests on the structure of the question plus missing data, not on NVDA fundamentals I've verified today.
  - `reversal_condition`: I'd revisit toward a starter/confirmed frame if you supply (a) a current valuation anchor vs. forward estimates, (b) the consensus you think the gap was measured against, and (c) your position context and horizon.

## Disconfirmation move (required — decision_pressure is high)

Flip the question: **if you held no NVDA at all, would you initiate here, today, purely on "the gap has played out"?** "The gap closed" is a reason the prior thesis *worked* — it is not, by itself, evidence the *next* leg is favorable. The bullish version of your question quietly assumes the re-rating that already happened will repeat. The disconfirming read: a closed gap means consensus has caught up, so you'd now be paying for expectations that are already in the price, and your forward edge has to come from a *new* variant view you haven't stated yet.

What would flip me to a more constructive stance (`reversal_condition`): a *fresh* identifiable expectations gap (a specific variable where you think consensus is still wrong — e.g., a segment estimate, a margin path, a demand-durability question), not the one that already resolved.

## Participation frame

- `participation_posture`: watch_only / add_only_if_confirmed (cannot go higher without live valuation + position data)
- `basis`: central premise unverifiable this turn (`source_gap`); no position context (`no_position_data`)
- `confirmation_required`: name a *new* variant view where current consensus is wrong, plus a current valuation anchor vs. forward estimates. A closed gap is not a confirmation variable.
- `invalidation`: thesis-level — if the new demand/margin variable you're betting on is already in consensus, there is no edge regardless of price. (Price drawdown is a risk trigger only, secondary to thesis invalidation.)
- `action_boundary`: research_only. This is not a buy instruction, a share count, or a weight. I do not place or size trades.

## Refresh conditions

- `stale_after`: this read is stale immediately for live use — it contains no current market data.
- `must_refresh_if`: you provide live price/consensus, NVDA reports or guides, or you supply position context. Any of these can move the posture off `watch_only`.

## Progressive Follow-Up

下一步最有用的问题：围绕 **NVDA**，你说的"预期差兑现了"是相对哪一个具体共识变量讲的——是某个 segment 的收入、毛利率路径，还是需求持续性？回答后会把判断从 `unknowable_now` 推向可验证，并决定是否要进 thesis-update-loop 重建一个*新的* variant view。
- route_binding: `thesis_system_update` / `variant-perception` lens
- object_anchor: NVDA 的具体定价变量（segment / 毛利 / 需求持续性）
- decision_impact: evidence_path + readiness_level（从 working_view 起步）

第二个：这次"加仓"的时间边界是几天的交易、1–2 个季度，还是多年持有？并且你当前的持仓、成本、权重和风险预算是什么?
- route_binding: `actionability-risk-control` -> `position-review-loop`
- object_anchor: 你的 NVDA 持仓语境与 `time_boundary`
- decision_impact: actionability_boundary + position_review_scope（有了持仓数据才可能从 `research_only` 升级到 starter/confirmed 框架）

`followup_prompt_mode`: decision_grade.
