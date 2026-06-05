Mira Mode.

## Routing Card

- interaction_mode: `routed_research` (variant-perception is a research lens, not a one-line direction)
- primary_intent: locate the variant perception (预期差) on NVDA — where consensus and Mira's view could diverge, and along which variable
- secondary_intents: none stated (a follow-up actionability/sizing question is a separate route)
- execution_order: single intent this turn
- scope_confirmation_required: no
- routing_assumptions (assumption_confidence: `medium`): US-listed NVDA (NASDAQ); research-only "where is the gap," not "can I buy/add"; time_boundary mixed but anchored to the next 1–2 quarters of datacenter revision; "answered" = the candidate gap axes are named with their consensus proxy and what would confirm/break each
- task_mode: `thesis_system_update` (variant-perception mapping), entered via single-equity lens, not full first-pass coverage
- research_object: `single_equity` — NVDA (NVIDIA Corp)
- market_scope: US equities / semiconductors; market_scope_gate: US large-cap, deep liquidity, index/passive + crowded institutional base → `market_structure_weight: context`
- time_boundary: `2Q_8Q_or_FY1_FY2` primary, with a `gt_1y` tail on the durability question (`horizon_uncertainty: noted`)
- depth_mode: `quick_map` ("where's the variant perception" = locate the gap, not price it)
- output_language: `en` (interaction language is English) | evidence_languages: `[en]`
- decision_pressure: `none` | framing_risk: `none` | disconfirmation_required: `no` (bare 预期差 question, no action verb, no position context)
- private_state_action: `waive` (no NVDA private view exists; can save_working_view on request)
- routing_carryover: `none` (session start)
- quant_dependency: `high` | calculation_gate: `required` but `calculation_waived_by_speed` this turn — I have no live consensus/estimate feed, so every number is `source_gap`
- information_value: `high` | knowability_status: `partially_knowable` (some gap axes are structurally unknowable until disclosure events)
- primary_skill_or_loop: `skills/equity-research-core` → `variant-perception` lens
- selected_framework: expectations / revision-driven (NVDA is priced off datacenter compute demand and forward estimate revisions)
- selected_overlays: `supply-chain` (CoWoS/HBM, foundry), `macro` (secondary — hyperscaler capex cycle, rates on long-duration multiple)
- selected_lenses: `variant-perception`; lens_basis: user explicitly asked for the 预期差; what_it_forces_us_to_check: the consensus proxy at variable level, the divergence point, and the repricing path
- readiness_level: `working_view` (no live data; cannot upgrade past this)
- routing_mismatch_risk: treating a research "where's the gap" question as an actionability "can I add" question — explicitly held to research-only

## Critical Constraint Up Front

I do not have live market access this turn (no consensus estimates, no current price, revision history, options-implied move, or positioning data). Per the contract, **I will not invent those numbers.** A real variant-perception read requires the consensus proxy *stated at variable level* — without it, this is a **map of where the gap candidates live and what data closes each one**, not a quantified 预期差 call. Every numeric anchor below is flagged `source_gap`.

## Facts (structural, do not require a live feed)

- NVDA is priced predominantly off **datacenter compute demand** — accelerators (current-gen Blackwell-class GPUs), networking (NVLink/Spectrum/InfiniBand), and the CUDA software moat. Datacenter dwarfs gaming/auto/pro-viz in the revenue mix.
- The dominant demand counterparties are a **concentrated hyperscaler + large-AI-lab buyer base**, plus sovereign/enterprise AI build-outs. Customer concentration is a known structural fact.
- The supply chain bottleneck has historically sat in **advanced packaging (CoWoS) and HBM**, gating how much demand converts to shipped revenue.
- The stock carries a **large expectation burden**: the valuation embeds continued high datacenter growth and durable gross margin, so the marginal price-setter is *revision direction*, not absolute level.

## Where the Variant Perception Candidates Actually Sit

The 预期差 on NVDA is rarely "is AI demand real" (consensus already says yes). It lives in five narrower axes. For each: the variable, what consensus likely embeds (proxy = `source_gap` without a feed), and what would confirm or break a divergent view.

**1. Demand durability vs. digestion (the biggest live gap)**
- Variable: is current datacenter run-rate a durable multi-year ramp, or a pull-forward that digests into an air-pocket?
- Consensus proxy: continued sequential datacenter growth into FY-forward — `source_gap` (need sell-side datacenter revenue path + revision history).
- Divergence point: bears argue hyperscaler capex growth *decelerates* even if absolute spend stays high; the second derivative is what reprices the stock, not the level.
- Confirms a positive gap: hyperscaler capex guides raised, next-gen ramp ahead of schedule, backlog/visibility extended.
- Confirms a negative gap: any hyperscaler trimming capex growth, channel/inventory build, or "good enough" inference shifting spend off training GPUs.

**2. Gross margin trajectory**
- Variable: does datacenter gross margin hold at elevated levels, or mean-revert as competition/mix/new-node costs bite?
- Consensus proxy: margin sustained near recent highs — `source_gap`.
- The gap: the market may under-price margin *normalization* on a new architecture ramp (early-ramp cost) or over-price pricing power if custom silicon erodes it.

**3. Custom silicon / competitive share (the slow-burn gap)**
- Variable: how much accelerator TAM do hyperscaler in-house ASICs and rival GPUs capture at the margin?
- Consensus proxy: NVDA holds dominant share — `source_gap`.
- The gap is structural, not next-quarter: it bites the *terminal* growth and margin, which is why it's the `gt_1y` tail. Hard to falsify on any single print.

**4. Supply unlock vs. demand (a gap that can flip sign)**
- Variable: is the constraint still supply (CoWoS/HBM), meaning reported revenue *understates* demand — or has supply caught up, exposing true demand?
- The variant perception flips: while supply-constrained, beats are "demand is even bigger"; once supply unlocks, the same revenue gets read as "demand is now the question." `source_gap` on current CoWoS/HBM capacity status.

**5. Sovereign/enterprise breadth and export policy**
- Variable: does demand broaden beyond a handful of hyperscalers (sovereign AI, enterprise), and how do export controls shape the addressable mix?
- This is a `knowability_status: unknowable_now` axis on the policy side — driven by regulatory events, not researchable to a clean answer today.

## Inferences

- The *highest-information* variant perception right now is **Axis 1 (capex second-derivative)** — it is the variable most likely to actually reprice the stock and is at least `partially_knowable` from hyperscaler capex commentary and revision history.
- Axes 3 and 5 are real but are **terminal-value / policy** gaps: deep research today won't settle them (`information_value: medium`, partly `irreducible_uncertainty`), so over-researching them now is low-yield.
- Without a consensus feed, I **cannot state which direction the gap currently leans** — "where's the gap" is answerable structurally; "is the gap positive or negative right now" is `source_gap`.

## Judgments

- Judgment: NVDA's exploitable variant perception lives in **demand durability / capex second-derivative and margin trajectory**, not in "is AI real."
  - judgment_confidence: `medium`
  - confidence_basis: structural pricing facts (revision-driven name, concentrated buyer base, expectation burden) are stable and don't need a live feed; the *direction* of the gap does.
  - base_rate_anchor: high-expectation semi leaders historically reprice on capex-cycle inflections and margin normalization far more than on demand existence.
  - reversal_condition: if a live consensus pull shows estimates already embed a sharp deceleration (i.e., the bear case is *consensus*), the variant perception flips to the upside-surprise side and this framing inverts.
- Judgment: I cannot responsibly state a *signed* 预期差 (positive/negative) this turn.
  - judgment_confidence: `high` (this is a data-availability fact, not a market call)
  - reversal_condition: a consensus/estimate feed becomes available.

## State / Refresh

- thesis_state: `draft` (variant-perception map only; not an active thesis)
- research_action: `watch_only`
- stale_after: next NVDA earnings/guidance event, or any major hyperscaler capex update
- must_refresh_if: (a) NVDA reports or guides; (b) a hyperscaler revises capex; (c) CoWoS/HBM supply status changes; (d) a material export-policy change; (e) I get a live consensus/revision feed (would upgrade `quick_map` → `standard` and let me sign the gap)
- source notes: no live sources accessed this turn (network/data off). All quantitative anchors = `source_gap`. Structural facts above are stable industry-structure claims, not freshly verified figures.

## Progressive Follow-Up

下一步最有用的问题：围绕 **NVDA 的 datacenter capex 二阶导 vs. 毛利率轨迹**，你更希望我在拿到 consensus/revision 数据后**给这个预期差定向（正/负）**，还是先把它落成一个可追踪的 **expectation-map + thesis-ledger** 私有对象？

1. 你这个预期差问题是服务于一个长期 thesis，还是为下一份财报做 event-setup?
   - route_binding: `task_mode` → `thesis_system_update` vs `loops/event-delta-loop.md`
   - object_anchor: NVDA datacenter revenue path / next earnings guidance
   - decision_impact: `thesis_state` + `output_package` (build expectation-map vs. event-delta)
2. 要不要我把这版 variant-perception map 存成 NVDA 的私有 working view，方便下次"接着上次看"?
   - route_binding: `private_state_action=save_working_view` → `loops/view-continuity-loop.md`
   - object_anchor: `private/research/NVDA/working-view.md`
   - decision_impact: `readiness_level` (working_view continuity) + `refresh_condition`

(If you want the gap *signed* rather than mapped, I'll need a consensus/estimate feed enabled — that upgrades this from `quick_map` to a `standard` package with a calculation ledger. And if your question is actually "能不能买/加" rather than "预期差在哪," that's a different route — I'd run the actionability gate, which needs your time window, position context, and an invalidation level.)
