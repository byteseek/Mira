# View Continuity Loop

`view-continuity-loop` 用于把 Mira 问答中的用户私有观点变成可延续、可更新、可废弃的轻量状态。

它不是完整 research package，也不是 tracked Mira product memory。它只处理用户私有 working view 与正式 thesis system 之间的边界。

## Objective

- 读取当前对象的用户私有观点，只在任务需要时读取。
- 判断本次输出是否应该保存为 working view。
- 判断新增证据是否更新、降级、废弃或升级已有 private view。
- 防止用户私有观点、持仓、watchlist 或偏好进入 tracked Mira product files。
- 给后续问答留下可追溯的 `stale_after` 和 `must_refresh_if`。

## Storage Boundary

Tracked product state:

- `MIRA.md`
- `OPERATING_CONTRACT.md`
- `loops/`
- `skills/`
- `templates/`
- `memory/` for default methodology, public examples and reusable playbooks
- `cases/` for public or de-identified examples

Gitignored user state:

- `private/views/view-register.csv`
- `private/research/<OBJECT>/working-view.md`
- `private/research/<OBJECT>/thesis-ledger.md`
- `private/research/<OBJECT>/expectation-map.csv`
- `private/portfolio/`
- `private/preferences/user-preferences.md`
- `local/` for local data, downloads and cache

Do not write real user state into tracked `memory/`, `cases/` or `templates/` unless the user explicitly asks to promote a de-identified example or product method.

## Loop Input

- `research_object`
- `market_scope`
- `time_boundary`
- `current_question`
- `private_state_action`
- `prior_private_view_refs`, optional
- `new_claims`, optional
- `source_notes_or_evidence_refs`
- `user_save_intent`, if stated

## States

### `locate-private-state`

Check only object-specific private state:

- `private/views/view-register.csv`
- `private/research/<OBJECT>/working-view.md`
- `private/research/<OBJECT>/thesis-ledger.md`
- `private/research/<OBJECT>/expectation-map.csv`

If the object has no private state, record `prior_view_status: none`.

Do not scan all `private/`.

### `classify-current-output`

Classify the current answer:

- `ephemeral_answer`: useful now, no need to save.
- `working_view`: reusable view with source notes but not full thesis quality.
- `hypothesis`: plausible but weak, incomplete or pending evidence.
- `watch_item`: something to track, not a thesis.
- `durable_thesis_candidate`: enough evidence to consider promotion.

### `save-or-waive`

Default actions:

- Save `working_view`, `hypothesis` or `watch_item` to `private/research/<OBJECT>/working-view.md` when it would help future continuity.
- Waive saving when the answer is pure explanation, too weak, too broad, stale on arrival or explicitly not worth preserving.
- Never auto-promote a view to tracked product memory.

Every saved view must include:

- `last_updated`
- `research_object`
- `market_scope`
- `time_boundary`
- `view_status`
- `core_view`
- `facts`
- `inferences`
- `judgments`
- `source_notes_or_evidence_refs`
- `confidence`
- `stale_after`
- `must_refresh_if`
- `promotion_criteria`
- `private_state_action`

### `update-existing-view`

When prior private state exists, compare new claims to the prior view:

- unchanged
- strengthened
- weakened
- contradicted
- stale
- promoted_candidate
- retired

If new claims lack source notes, update only as `watch_item` or waive.

### `register-view`

When saving or updating a view, add or update one row in `private/views/view-register.csv`.

The register should be object-level and lightweight. It is an index, not the full view.

### `promotion-gate`

Promote private working view into a formal private thesis object only when:

- core claims have source trails or evidence log refs
- facts, inferences and judgments are separated
- expectation variables are named
- `stale_after` and `must_refresh_if` are explicit
- the user wants ongoing tracking

Promotion target is still private by default:

- `private/research/<OBJECT>/thesis-ledger.md`
- `private/research/<OBJECT>/expectation-map.csv`

Promote to tracked `memory/` or `cases/` only with explicit user instruction and de-identification review.

## Output

- `private_state_action`
- `prior_view_status`
- `view_status`
- `view_delta`
- `saved_to` or `save_waived_reason`
- `stale_after`
- `must_refresh_if`
- `next_update_trigger`
- `promotion_status`
- Step 4.5 critical interaction asks one natural-language question about saving, updating, promoting, or waiving the working view; active follow-up state remains transient routing state, not preference memory.

## Stop Rules

- Do not save private state when the user explicitly opts out.
- Do not write private holdings, weights, preferences or working views into tracked files.
- Do not upgrade an unsourced or sentiment-only view beyond `hypothesis` or `watch_item`.
- Do not treat private view continuity as investment advice or autonomous monitoring.
