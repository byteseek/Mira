# Evidence Log Schema

`evidence-log.csv` 是 case-level claim record，不是 source registry。

`source-registry.csv` 回答“材料从哪里来”。`evidence-log.csv` 回答“这条被用于研究的具体信息是什么、性质是什么、能否支撑结论”。

## Canonical Columns

所有新的 `evidence-log.csv` 必须使用以下表头，顺序固定（v1.2）：

```csv
source_id,claim_area,claim_type,claim_text,source_speaker,verification_status,authority_level,source_date,as_of_date,url_or_path,used_by_agent,used_by_skill,confidence,upstream_sources,notes,evidence_category,freshness_status,conflict_status,treatment,readiness_impact,source_language,translation_basis
```

版本沿革：

- v1：缺最后五个 evidence posture 字段。
- v1.1：在 v1 末尾追加 `evidence_category,freshness_status,conflict_status,treatment,readiness_impact`。
- v1.2：在 v1.1 末尾追加 `source_language,translation_basis`（i18n 语言列）。

validator 继续兼容 v1 / v1.1 历史 case；新模板和新 case 应使用 v1.2 表头。两个语言列**追加在末尾**，因此 v1.1→v1.2 是纯追加迁移，不改动既有列顺序。

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
| `evidence_category` | yes | 必须来自 [evidence-posture-taxonomy.md](evidence-posture-taxonomy.md)。 |
| `freshness_status` | yes | `current` / `acceptable_for_period` / `preliminary` / `stale` / `unknown`。 |
| `conflict_status` | yes | `none` / `unresolved` / `contradicted` / `not_checked`。 |
| `treatment` | yes | `use_normally` / `attribute` / `sensitize` / `haircut` / `source_gap` / `monitor` / `exclude` / `open_item`。 |
| `readiness_impact` | yes | `supports_durable_conclusion` / `supports_working_view` / `monitoring_only` / `blocks_actionability` / `blocks_publication` / `not_material`。 |
| `source_language` | yes (v1.2) | 来源原文语言，BCP-47 风格标签，例如 `zh-CN`、`en`、`ja`、`ko`。派生/无语言文本的行用底层来源语言或 `not_applicable`。 |
| `translation_basis` | yes (v1.2) | `not_translated` / `mira_translation` / `provider_translation` / `official_translation` / `bilingual_source` / `not_applicable`。 |

## Validation Rules

- 表头必须与 canonical columns 完全一致。
- `claim_type` 必须是允许枚举。
- `verification_status` 必须是允许枚举。
- `authority_level` 必须是 `L1` 到 `L6`。
- `source_date` 和 `as_of_date` 必须是 `YYYY-MM-DD`。
- `confidence` 必须是 `high`、`medium` 或 `low`。
- v1.1 表头中的 evidence posture 字段必须使用允许枚举。
- `derived_calculation` 或 `authority_level=L6` 的记录必须有非空 `upstream_sources`，且不能写 `not_applicable`。
- 影响 durable conclusion 的 `derived_calculation` 必须有 `calculation-ledger.csv` 记录或 explicit formula note。
- `rumor_signal` 不能有 `confidence=high`。
- `sentiment`、`opinion`、`rumor_signal` 默认不能作为 durable conclusion 的唯一证据。
- `market_pricing` 只能说明市场如何定价，不能写成基本面验证。
- `evidence_category=verified_fact` 不应搭配 `verification_status=unverified`、`claim_type=assumption`、`claim_type=opinion`、`claim_type=sentiment` 或 `claim_type=rumor_signal`。
- `readiness_impact=supports_durable_conclusion` 不应搭配 `evidence_category=unknown`、`weak_signal`、`stale` 或 `contradicted`，除非 notes 说明控制来源和降级方式。
- v1.2：`source_language` 必须非空；`translation_basis` 必须是允许枚举。
- v1.2：**判断性 claim**（`claim_type ∈ {guidance, company_claim, commitment, target}`）且 `translation_basis ∈ {mira_translation, provider_translation}` 的行，`notes` 应包含 `original_excerpt=`（保留原文片段，否则 validator WARN）。背景性/聚合类 claim 可只留译摘，不触发 WARN。

## Translation Provenance (v1.2)

外文一手源在进入 evidence log 时，**译文不能取代原文**——尤其管理层措辞本身就是 variant-perception 信号，翻译会丢失语气和对冲性措辞。

字段职责（不新开第三列，原文进 `notes`）：

- `claim_text`：保持**一句标准化、可核验 claim**，不得塞原文 + 译文。
- `source_language`：来源原文语言标签。
- `translation_basis`：译文来源（Mira 译 / 供应商译 / 官方译 / 双语源 / 未翻译 / 不适用）。
- `notes`：承担判断的跨语言引用必须保留 `original_excerpt=...; translated_summary=...` 键值。背景性引用可只留译摘。

判定边界：是否要 `original_excerpt` 跟随 [claim-taxonomy.md](claim-taxonomy.md)——做分析功的 claim（`guidance`、`company_claim`、`commitment`、`target` 等）要原文；纯背景/聚合数据可豁免。

示例（中文公告，Mira 翻译，承担判断）：

```csv
cninfo_2026q1,guidance,guidance,"Management guided 2026 revenue growth to 'around 20%'.",management,disclosed,L1,2026-04-20,2026-04-20,https://www.cninfo.com.cn/...,research-orchestrator,equity-research-core,medium,not_applicable,"original_excerpt=公司预计2026年营收同比增长20%左右; translated_summary=full-year rev growth ~20%; hedged with 左右",company_statement,current,none,attribute,supports_working_view,zh-CN,mira_translation
```

## Legacy Handling

历史 case 中存在 source-record 形态或旧 claim schema 的 `evidence-log.csv`。这些文件应保留作为历史产物，但不得作为新样板。v1 / v1.1 表头仍被 validator 容忍为 legacy；新 case 用 v1.2。

迁移顺序：

1. 先迁移新的或仍在活跃跟踪的 case。
2. 再迁移被 README 或 quickstart 称为样板的 case。
3. 归档类、发现类或历史类 case 可以标记 `legacy_evidence_schema`，但正式结论必须显式降级或补充 canonical evidence log。

## Practice Bar

一条 claim 能进入 evidence log，不代表它能支撑行动。Mira 使用时还必须检查：

- 这条 claim 改变了哪个 expectation variable。
- 它是事实、公司口径、预测、市场定价还是 Mira 推断。
- 如果它错了，哪个 thesis、event delta 或 research action 会被影响。

证据姿态字段提供这个实战分层：

- `claim_type` 回答“这是什么信息”。
- `authority_level` 回答“来源层级多高”。
- `evidence_category` 回答“这条信息对当前结论有多可用”。
- `readiness_impact` 回答“它能不能支撑 durable conclusion 或 actionability”。

## Calculation Relationship

`evidence-log.csv` 记录派生计算作为 claim 的来源链和研究用途；`calculation-ledger.csv` 记录公式、口径、输入、结果和复算限制。

当一个数字由 Mira 或研究员计算得出，并且会影响 thesis、event delta、valuation、peer comparison 或 actionability 时，不能只在 evidence log 中写 `derived_calculation`。还必须在 calculation ledger 或 explicit formula note 中保留可复算路径。
