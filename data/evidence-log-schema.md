# Evidence Log Schema

`evidence-log.csv` 是 case-level claim record，不是 source registry。

`source-registry.csv` 回答“材料从哪里来”。`evidence-log.csv` 回答“这条被用于研究的具体信息是什么、性质是什么、能否支撑结论”。

## Canonical Columns

所有新的 `evidence-log.csv` 必须使用以下表头，顺序固定：

```csv
source_id,claim_area,claim_type,claim_text,source_speaker,verification_status,authority_level,source_date,as_of_date,url_or_path,used_by_agent,used_by_skill,confidence,upstream_sources,notes
```

## Required Fields

| field | required | description |
| --- | --- | --- |
| `source_id` | yes | 指向 `source-registry.csv` 或 case-local source note 的唯一标识。 |
| `claim_area` | yes | 信息支撑的研究区域，例如 `guidance`、`pricing`、`valuation`、`market_reaction`。 |
| `claim_type` | yes | 必须来自 [claim-taxonomy.md](claim-taxonomy.md)。 |
| `claim_text` | yes | 一句可核验 claim。不能只写 source name。 |
| `source_speaker` | yes | 信息说话者，例如 `company`、`management`、`regulator`、`market`、`mira`。 |
| `verification_status` | yes | 必须来自 [claim-taxonomy.md](claim-taxonomy.md)。 |
| `authority_level` | yes | `L1` 到 `L6`。 |
| `source_date` | yes | 来源发布或数据生成日期，`YYYY-MM-DD`。 |
| `as_of_date` | yes | claim 的信息时点，`YYYY-MM-DD`。 |
| `url_or_path` | yes | 原始 URL、repo path 或 explicit source note。 |
| `used_by_agent` | yes | 使用该 claim 的 agent。 |
| `used_by_skill` | yes | 使用该 claim 的 skill 或 loop。 |
| `confidence` | yes | `high` / `medium` / `low`。 |
| `upstream_sources` | yes | L6 或派生 claim 必须列上游 L1-L5 source id；非派生可写 `not_applicable`。 |
| `notes` | yes | 口径、限制、刷新条件或证据降权说明。 |

## Validation Rules

- 表头必须与 canonical columns 完全一致。
- `claim_type` 必须是允许枚举。
- `verification_status` 必须是允许枚举。
- `authority_level` 必须是 `L1` 到 `L6`。
- `source_date` 和 `as_of_date` 必须是 `YYYY-MM-DD`。
- `confidence` 必须是 `high`、`medium` 或 `low`。
- `derived_calculation` 或 `authority_level=L6` 的记录必须有非空 `upstream_sources`，且不能写 `not_applicable`。
- `rumor_signal` 不能有 `confidence=high`。
- `sentiment`、`opinion`、`rumor_signal` 默认不能作为 durable conclusion 的唯一证据。
- `market_pricing` 只能说明市场如何定价，不能写成基本面验证。

## Legacy Handling

历史 case 中存在 source-record 形态或旧 claim schema 的 `evidence-log.csv`。这些文件应保留作为历史产物，但不得作为新样板。

迁移顺序：

1. 先迁移新的或仍在活跃跟踪的 case。
2. 再迁移被 README 或 quickstart 称为样板的 case。
3. 归档类、发现类或历史类 case 可以标记 `legacy_evidence_schema`，但正式结论必须显式降级或补充 canonical evidence log。

## Practice Bar

一条 claim 能进入 evidence log，不代表它能支撑行动。Mira 使用时还必须检查：

- 这条 claim 改变了哪个 expectation variable。
- 它是事实、公司口径、预测、市场定价还是 Mira 推断。
- 如果它错了，哪个 thesis、event delta 或 research action 会被影响。
