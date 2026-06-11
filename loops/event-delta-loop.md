# Event Delta Loop

`event-delta-loop` 用于事件前后对比。它把事件从“新闻摘要”转成对 expectation map 和 thesis ledger 的影响判断。

## Use When

- earnings / guidance / transcript / investor day
- macro release / FOMC / CPI / jobs report
- product launch / customer win / supply-chain event
- regulatory action / litigation / policy change
- peer earnings read-through
- major price move that needs expectation attribution

## Loop Input

- `research_object`
- `event_name`
- `event_type`
- `event_date`
- `pre_event_setup`
- `prior_thesis_ref`
- `expectation_map_ref`
- `new_sources`
- `price_reaction_window`

## States

### `pre-event-setup`

事件前必须记录：

- 市场共识代理
- Mira prior view
- 关键变量
- 预期中的 beat / miss / inline 判断标准
- 最可能改变 thesis 的 disclosure items

### `collect-event-claims`

收集事件后来源，并登记到 evidence log。

必须分开：

- actual disclosure
- management explanation
- guidance
- peer read-through
- market reaction
- Mira derived calculation

### `delta-vs-expectation`

逐项比较：

- actual vs consensus proxy
- guidance vs consensus
- management tone vs prior tone
- peer data vs company claim
- price reaction vs fundamental delta

### `revision-path`

判断事件最可能触发哪类修正：

- `revenue_revision`
- `margin_revision`
- `cash_flow_revision`
- `capex_revision`
- `multiple_rerating`
- `risk_premium_change`
- `positioning_unwind`
- `no_material_revision`

### `thesis-impact`

给出 `-2` 到 `+2`，并说明影响的是：

- `near_term_execution`
- `medium_term_revision`
- `long_term_thesis`
- `regime_transition`

### `write-event-delta`

输出 `event-delta.md`，并列出需要写回 `expectation-map.csv` 和 `thesis-ledger.md` 的字段。

## Output

- `event-delta.md`
- `expectation map update`
- `thesis impact`
- `escalation decision`
- `required research follow-up`（内部研究待办，字段名 `required_research_followup`；区别于 Step 4.5 的 progressive follow-up）
- Step 4.5 critical interaction: ask one natural-language next question that routes the user into expectation-map update, thesis update, SEC supplement, or a waiver if no useful next interaction exists.

## Stop Rules

- 没有 pre-event expectation 时，必须降级为 `event summary with source gap`。
- 只有价格反应、没有基本面或市场预期证据时，不能直接归因为 thesis change。
- 管理层口径未被财务、订单、客户、同行或外部数据支持时，不能升级长期 thesis。
