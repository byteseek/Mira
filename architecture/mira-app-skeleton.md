# Mira App Skeleton

这个文件定义文档版应用骨架。V1 不新增可运行代码、不引入数据库、不做 UI；Markdown + CSV 是正式接口。未来 CLI/API/UI 必须围绕同一组对象工作，不能绕过 evidence 和 thesis 协议。

## Conceptual Modules

### Router

Input:

- 用户问题
- 研究对象
- 时间边界
- 已有 research package / memory refs

Output:

- `task_mode`
- `research_object`
- `primary_loop`
- `required_objects`
- `expected_output_package`

Router 必须识别 `thesis_system_update`，例如：

- 更新 thesis
- 看预期差
- 复盘判断
- 某个事件是否改变 thesis
- 当前 thesis 是否 stale

### Source And Claim Layer

职责：

- 维护 `source-registry.csv`
- 生成或更新 case-level `evidence-log.csv`
- 对所有可用信息执行 claim classification

这个层只回答“信息是什么”和“来自哪里”，不直接输出投资判断。

### Expectation Layer

职责：

- 维护 `expectation-map.csv`
- 记录 consensus proxy、Mira view、price-in status 和 next check
- 识别哪些新信息可能改变 revenue、margin、multiple、risk premium、positioning 或 liquidity expectation

### Thesis Layer

职责：

- 维护 `thesis-ledger.md`
- 处理 thesis state change
- 连接 supporting claims、key assumptions 和 disconfirming evidence
- 管理 `stale_after` 和 `must_refresh_if`

### Event Layer

职责：

- 在事件前建立 `pre_event_setup`
- 在事件后生成 `event-delta.md`
- 更新 expectation map
- 判断是否触发 thesis update 或完整 research-loop

### Decision And Review Layer

职责：

- 维护 `decision-log.csv`
- 生成 `postmortem.md`
- 把复盘结论写入 methodology queue、playbook 或 retired rules

## Directory Contract

Recommended object locations:

- `memory/research/<OBJECT>/thesis-ledger.md`
- `memory/research/<OBJECT>/expectation-map.csv`
- `memory/research/<OBJECT>/decision-log.csv`
- `memory/research/<OBJECT>/postmortem.md`
- `cases/<case-id>/event-delta.md`
- `cases/<case-id>/expectation-map.csv`

Templates live in:

- `templates/thesis-system/`

Methodology research lives in:

- `cases/institutional-thesis-system-methodology-YYYY-MM-DD/`
- `memory/methodologies/institutional-thesis-system.md`

## Future CLI/API Boundaries

If code is added later, the minimum commands should map to object updates:

- `mira route`: classify task and required objects.
- `mira thesis init`: create thesis-ledger and expectation-map from a research package.
- `mira event delta`: generate event-delta from pre-event setup and new claims.
- `mira thesis update`: apply event or monitoring delta to thesis state.
- `mira review`: create postmortem and methodology update.
- `mira validate`: check required fields and evidence references.

The CLI/API must treat Markdown + CSV as canonical storage until a migration plan is approved.

## Non-Goals For V1

- No autonomous trading.
- No background monitoring unless a separate automation is created.
- No database migration.
- No UI.
- No attempt to replace analyst judgment with a score.

## Acceptance Criteria

- A research object can have a current thesis, expectation map, refresh policy and postmortem path.
- An earnings event can explain what changed versus expectations.
- A high-narrative case can downgrade weak evidence before it affects thesis state.
- Every durable conclusion remains traceable to evidence logs or explicit source notes.
