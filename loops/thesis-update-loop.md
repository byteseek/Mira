# Thesis Update Loop

`thesis-update-loop` 用于创建、更新、降级、废弃或复盘一个已存在或即将建立的 thesis object。

它不是完整重研，也不是普通新闻更新。它只回答：新增证据是否改变 thesis ledger、expectation map 或 thesis state。

## Loop Input

- `research_object`
- `market_scope`
- `time_boundary`
- `prior_thesis_ledger`
- `expectation_map`
- `new_claims`
- `trigger`
- `research_package_refs`

## States

### `load-current-state`

读取当前：

- `thesis-ledger.md`
- `expectation-map.csv`
- 最近 research package
- 最近 event-delta
- 最近 decision-log

如果没有 thesis-ledger，先判断是否应该从现有 research package 初始化。

### `classify-new-claims`

把新增信息拆成 claim，并沿用 `data/claim-taxonomy.md`。

必须区分：

- `fact`
- `reported_metric`
- `company_claim`
- `guidance`
- `forecast`
- `assumption`
- `market_pricing`
- `sentiment`
- `rumor_signal`
- `derived_calculation`

### `map-to-expectations`

判断新增 claim 改变哪个变量：

- revenue expectation
- margin expectation
- cash flow expectation
- capex expectation
- balance sheet risk
- valuation multiple
- risk premium
- positioning
- catalyst timing

如果找不到明确变量，默认是 `watch_item`，不能升级 thesis。

### `assess-thesis-impact`

使用 `-2` 到 `+2`：

- `+2`: 核心 thesis 被强验证。
- `+1`: 方向改善，但仍需后续确认。
- `0`: 与 thesis 一致，信息增量有限。
- `-1`: 出现可解释但需要跟踪的瑕疵。
- `-2`: 核心 thesis 被削弱或证伪。

### `state-change`

允许的状态变更：

- `draft -> active`
- `active -> upgrade_watch`
- `active -> downgrade_watch`
- `active -> stale`
- `watch -> active`
- `watch -> retired`
- `downgrade_watch -> retired`
- `stale -> active`

任何状态变更都必须写入 state change log，并指向 evidence ref。

### `write-objects`

更新：

- `thesis-ledger.md`
- `expectation-map.csv`
- `decision-log.csv`，如有研究动作

## Escalation Rules

升级回 `research-loop` 的条件：

- 新 claim 改变核心业务、估值锚、风险溢价或长期 thesis。
- 原 thesis 的 supporting claim 被证伪。
- 原本只是 `company_claim`、`forecast` 或 `assumption` 的关键输入被正式证实或证伪。
- 主导定价变量变化，导致 framework 可能失效。
- expectation map 出现多项关键变量同时漂移。

## Output

- `thesis update summary`
- `expectation map changes`
- `thesis impact`
- `state change decision`
- `required research follow-up`（内部研究待办，字段名 `required_research_followup`；区别于 Step 4.5 的 progressive follow-up）
- Step 4.5 critical interaction: ask one natural-language next question that tests the key state-change uncertainty, confirms escalation, or records why follow-up is waived.

## Stop Rules

- 新信息没有 source_id 或 explicit source note，不更新 thesis state。
- 新信息只是 sentiment 或 rumor_signal，只能更新 watch item。
- 无法定位被影响变量时，不允许写成 thesis upgrade。
