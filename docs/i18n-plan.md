# Mira 国际化方案 (Internationalization Plan)

> **状态**: Phase 0–3 已实现（待评审 / 待合并）。实现摘要见文末 §9。
> **TL;DR**: Mira 是一个纯协议层产品（markdown 协议 + CSV/JSON schema），模型本身已会说所有语言，所以国际化的重点**不是翻译界面字符串**。核心架构是一句话：**协议不变，表达本地化**——机器契约（token、字段名、文件名）保持语言无关且稳定，只本地化用户可读的渲染层。真正的工作和风险在三个被混为一谈的层：交互/输出/证据语言的拆分、路由启发式与语言解耦、本地市场一手源覆盖。

---

## 1. 背景：为什么 Mira 的国际化不是翻译问题

传统软件 i18n = 把 UI 字符串抽到 locale 文件。但 Mira 的"产品"是协议层本身：`MIRA.md` / `OPERATING_CONTRACT.md` / `loops/` / `skills/` / `templates/` / `data/` 全是 markdown 协议和 schema，渲染器是模型本身。把界面"翻译成多语言"几乎是免费的，也不是重点。

真正的国际化债务藏在三个层里，现在它们是**纠缠的**，方案的第一步就是把它们拆开：

| 层 | 现状 | 问题 |
| --- | --- | --- |
| **表达层**（交互/输出/证据语言） | `output_language` 已存在（controlled-vocabulary 的 Language Field），但尚未和 `interaction_language` / `evidence_languages` 形成正式三轴语言模型 | 三个独立变量被当成一个；无法表达"英文提问→中文 memo→中文公告+英文 SEC 证据"这类组合 |
| **路由层**（意图/深度/角色识别） | 路由启发式硬编码在中英文表面词上：唤醒词、`"看一下"→quick_map`、`"能不能冲"`→trader（见 `OPERATING_CONTRACT.md`、`MIRA.md`） | 日/德/韩语用户说等价的话**完全不触发**；路由智能与语言强耦合 |
| **证据/覆盖层**（本地市场一手源） | search log 已有 `language_or_circle` 列；methodology 反复记录"只搜英文漏掉本地市场 ETF""缺中文 buy-side 写法" | 国际化缺口是有机冒出来的自由文本，没有被正式化为路由/刷新条件 |

---

## 2. 核心架构决策：协议不变，表达本地化

**不变层（机器契约，永远英文、永远稳定）**

- 状态/动作 token：`quick_map` / `standard` / `deep_dive` / `no_action` / `needs_refresh` 等
- 输出纪律字段：`research_object` / `market_scope` / `judgment_confidence` / `reversal_condition` 等
- 文件名与 schema：`evidence-log.csv`、`investment-memo.md`、CSV/JSON 表头

> 好处：可测试、可 diff、可自动更新、跨语言研究包结构不漂移。

**本地化层（用户可读，跟随用户语言）**

- 对话回答、解释、follow-up prompts
- 模板里的人类可读标题与字段说明（**渲染**出来，不维护静态翻译文件，见 §6 非目标）
- 证据摘要、术语解释

---

## 3. 设计原则（评审时请重点确认这几条）

1. **锁行为，不锁文风。** 国际化最大的风险是"翻译后协议约束变弱"（约束泄漏）：本地化解释时，纪律性从句（FIJ 分离、弱证据降级、refresh condition、stop rules）会在"翻得顺一点"时悄悄丢失。回归测试断言**结构和行为**，不断言字面文本。这是整个方案的成败点，不是一个次要测试项。
2. **glossary 与 controlled-vocabulary 逻辑同源，但物理分离。** `data/controlled-vocabulary.md` 是 prose 协议规格（385 行：token 枚举 + 语义 + validation），**不适合承载 N 语言显示宽表**。新建结构化表 `data/localization-glossary.csv`，表头如 `key,kind,en,zh-CN,ja,notes,canonical_token`，`kind ∈ {protocol_token, field_label, domain_term}`。仍是"一套 key"，但不污染协议文档。已实现 `validate_localization_glossary`（[scripts/validate_repo.py](../scripts/validate_repo.py)）：**仅对 `kind=protocol_token` 强约束**——其 `canonical_token` 必须存在于 controlled-vocabulary 的 token 全集（`schemas/vocab.json` 路由枚举 + validate_repo.py 的 evidence/state/action hardcoded 枚举 + 语言字段名），防止漂移；并校验结构（必填列、kind 枚举、key 唯一、`en` 非空）。`field_label` 与 `domain_term` 不强制 canonical_token。注：#51/#52 后路由 token 已迁到 `schemas/vocab.json`，depth_mode 等也在其中可解析。
3. **市场默认包挂在 `market_scope` 上，不挂在语言上。** 语言和市场是正交两轴。中文用户研究美股 = 中文输出 + EDGAR/USD/GAAP 默认。
4. **命名复用，不新造。** 沿用已存在的 `output_language`（tracked case 已在用），不引入 `display_language` 等同义 token，避免 diff/自动化裂开。
5. **canonical 单源，不 fork。** 一份英文 canonical 协议；本地化只做薄薄一层人类表面。坚决不把 loops/skills/templates 翻译成 N 份（`README.md` / `README.zh.md` 的手工双语 fork 是反面教材，不要扩大）。

---

## 4. 工作项（按层组织）

### 4.1 表达层

> **现状校正**：`output_language` **已经**是正式 token（见 `data/controlled-vocabulary.md` 的 `## Language Field` 段，含 `zh-CN`/`en`/`mixed` 与默认规则），且已在 `routing_carryover` 白名单内。所以这层只有两个净新增。

- 净新增两个语言变量进 controlled-vocabulary（machine token 不含括号 / 复数歧义）：
  - `interaction_language`：用户提问语言（默认回答语言）。
  - `evidence_languages`：**输出级**——整个研究包用到的证据语言集合。与行级 `source_language`（evidence-log 单行的原文语言，见 §4.3）分工清楚，不要共用一个名。
- `output_language`：已存在。在 MIRA.md Output Discipline 里**限定范围补必填**——正式 Mira research output 必填；`quick_answer` / 普通对话**隐式继承 `interaction_language`**，无需每次显式输出，避免轻量回答变重。
- 语言行为规则：默认用提问语言回答；混合语言时保持主语言、关键术语双语一次。

### 4.2 路由层（隐藏的硬债务）

- **不新增独立 `semantic_intent` 字段**；将现有 `primary_intent` / `secondary_intents`（OPERATING_CONTRACT Step 0 已用来拆复合 prompt）的取值**约束为一组 semantic intent 闭合词表**，eval 直接锁这组枚举（比"短语硬编码"更可测）。候选值：`low_commitment_triage` / `formal_research` / `incremental_update` / `actionability_question` / `methodology_reliability` / `position_or_portfolio_review`。这组值正好对应现有 Fast Paths / Role Defaults 表——本质是把隐式路由表显式化。
  - **三个字段分工划清，互不重叠：** semantic intent 枚举选**路由 / loop**（哪条研究线）；`interaction_mode`（`quick_answer`/`routed_research`/`decision_support`/`routing_unclear`）选**回答形状与是否触发 decision gate**；`depth_mode`（`quick_map`/`standard`/`deep_dive`）选**研究深度**。三者不要互相代替。
  - **保留复合能力：** 复合 prompt（如"看财报，顺便对比 AMD，我都重仓"）仍按 `primary_intent` / `secondary_intents` 拆分，每个值取自 intent 枚举，routing card 标 primary。
- 把中英文短语降级为多语言 few-shot 示例（映射到 intent 枚举），规则本身用抽象意图描述。
- 在 `evals/` 的 golden examples 中补**非中英文**样本，用 behavior-eval 锁死回归。

### 4.3 证据/覆盖层（长期护城河）

> **现状校正**：翻译溯源不是从零加——`data/public-source-targets.md` 第 46 行已要求外文页面标注 `translation_or_summary` 并说明"是否回查原文"，日股/韩股行也已写"关键结论回到原文"。本层是把已有 prose 纪律落成 evidence-log 的结构化字段。

- evidence log **只新增两列**：`source_language`、`translation_basis`。
  - **不要加泛泛的 `source_quality`**——会与现有 `authority_level`(L1–L6) / `confidence` / `evidence_category` / `readiness_impact` 重复并制造口径冲突。
  - 这是 evidence-log schema **v1.2 bump**，需同步改模板、validator、legacy handling（现 schema 要求表头完全一致）。
- **翻译溯源规则**：对**承担判断的引用**（如管理层措辞，本身即 variant-perception 信号）要求 verbatim 原文 + 译文；背景性引用存译文即可。挂在 claim taxonomy 上——做分析功的 claim 才要原文。
  - **`claim_text` 保持纯净**：schema 要求它是"一句可核验 claim"（[evidence-log-schema.md:25](../data/evidence-log-schema.md)），**不得塞原文+译文**，否则聚合 / validator / 读表全脏。
  - 原文与译摘进 `notes` 的结构化键值：`original_excerpt=...; translated_summary=...`。
  - `translation_basis` 是**新列（机器字段）**，**不在 `notes` 重复**，避免双源。新列仍只有 `source_language` / `translation_basis` 两个。
- 按 `market_scope` 升格**每市场默认包**：`data/public-source-targets.md` 已有分市场 disclosure / structure target 雏形（A股/港股/日股/台股/韩股/欧股）；缺的是 (a) 升格成 `market_scope`-keyed、路由自动套用的 pack，(b) 补 `calendar` / `currency` / `accounting_standard`(GAAP/IFRS/CAS) / `translation_caveats` 等非源维度。
- 把"本地一手源覆盖不足"从 search_gaps 自由文本提升为一等的 `source_gap` / `needs_refresh` / `watch_only` 条件。

### 4.4 实体规范化（i18n 暴露出来的相邻问题）

- ticker/同名公司消歧（`BABA` / `9988.HK` / `阿里` 不能静默合并）。严格说这是 `research_object` 的实体规范化（canonical id + aliases），单独治理，**不要当翻译做**。

### 4.5 偏好与隐私

- 用户语言偏好写入 gitignored `private/preferences/`，**不**写进 tracked product state。与 `MIRA.md` 的 product/private 边界一致。

---

## 5. 分阶段落地

| 阶段 | 内容 | 验收标准 |
| --- | --- | --- |
| **Phase 0 — 最瘦一刀**（高杠杆/低维护） | (1) 新建 `data/localization-glossary.csv`（token 当 key，配 canonical_token validator）；(2) 净新增 `interaction_language` / `evidence_languages` 进 controlled-vocab，`output_language` 在 Output Discipline 补成 formal Mira research output 必填、quick_answer / 普通对话隐式继承；(3) 多语言 golden prompts 进 behavior-eval | 同一意图中/英/日三语提问 → 路由一致、必填字段齐全、FIJ 分离存在、refresh condition 存在 |
| **Phase 1 — 证据双语化** | **先成文** `claim_text`/`notes` 翻译溯源规则（原文进 `notes` 键值，`claim_text` 保持单条 claim），**再动 schema**；evidence log 仅增 `source_language` / `translation_basis`（v1.2 bump，同步改模板/validator/legacy） | 外文来源的 evidence 行带原文语言标注；关键 quote 原文在 `notes`；`claim_text` 仍是单条可核验 claim；validator 通过 |
| **Phase 2 — 市场默认包** | 从 `public-source-targets.md` 抽象成 `market_scope` 默认包，每包含 `primary_disclosure_targets` / `market_structure_targets` / `calendar` / `currency` / `accounting_standard` / `translation_caveats` | 选定 `market_scope` 即自动套用对应包；覆盖缺口进 `source_gap`/`needs_refresh`/`watch_only` |
| **Phase 3 — 渲染规则（可缓/可不做）** | 模板人类可读标题按 `output_language` + glossary 即时渲染 | 同一模板三语渲染，schema 字段名不变 |

---

## 6. 非目标 / 反模式（明确不做）

- ❌ 把 loops / skills / templates 翻译成 N 份语言文件（无法维护的漂移矩阵）。
- ❌ 建静态 `i18n/template-labels.{zh,en,ja}.md`——模型即时渲染 + glossary 已能覆盖，静态 label 文件会重新制造 fork 维护负担。
- ❌ 引入 `display_language` 等与已有 `output_language` 同义的新 token。
- ❌ 在 evidence log 加泛泛的 `source_quality`（与 `authority_level`/`confidence`/`evidence_category`/`readiness_impact` 重复）。
- ❌ 把 verbatim 原文塞进 `claim_text`（它须保持单条可核验 claim）；原文进 `notes` 结构化键值。
- ❌ 为 verbatim 原文新开第三列。
- ❌ 在 `notes` 里重复 `translation_basis`（它已是新列）。
- ❌ machine token 用括号 / 复数歧义命名（如 `evidence_language(s)`）。
- ❌ 翻译机器 token / schema 字段名 / 文件名。
- ❌ 对所有引用强制存原文（过度工程；只对判断性引用要求）。

---

## 7. 测试策略（独立成节，因为它是核心）

复用已有的 behavior-level eval harness（`evals/` + `score_behavior_eval.py`）。新增**多语言 golden prompts**（中 / 英 / 中英混合 / 第三语言），断言：

- 路由是否正确（意图→正确 loop/skill/depth/role）
- 输出必填字段是否齐全
- facts / inferences / judgments 是否分离
- refresh / stale 条件是否存在

**重点：锁结构与行为，不锁文风。** 测试通过 = 在任意语言下协议约束强度一致。

---

## 8. 待决问题（评审时拍板）

1. glossary 首发覆盖哪几种语言？（建议 zh + en 起步，schema 设计成 N-way）
2. intent 枚举 / `interaction_mode` / `depth_mode` 三者边界如何成文，确保不重叠？（建议：分别选路由、回答形状+gate、研究深度）
3. 确认 semantic intent 作为 `primary_intent` / `secondary_intents` 的闭合词表落地，而非新增独立字段。
4. Phase 2 市场默认包先做哪个市场？（建议从覆盖痛点最大的 A 股 / 港股切入）
5. 翻译溯源对"判断性引用"的判定边界如何界定？（建议绑定现有 claim taxonomy 的等级）
6. `private/preferences/` 的语言偏好与 tracked product example 偏好如何不冲突？

---

## 9. 实现摘要（已落地）

**Phase 0**
- 新建 [data/localization-glossary.csv](../data/localization-glossary.csv)（protocol_token / field_label / domain_term）。
- [data/controlled-vocabulary.md](../data/controlled-vocabulary.md) Language Field 扩成三轴：新增 `interaction_language` / `evidence_languages`。
- [MIRA.md](../MIRA.md) Output Discipline 加 `output_language`（正式 output 必填、quick_answer 隐式继承）。
- [evals/behavior-eval-cases.jsonl](../evals/behavior-eval-cases.jsonl) +5 个多语言 case。

**Phase 1**（evidence-log v1.2）
- [data/evidence-log-schema.md](../data/evidence-log-schema.md)：表头升 v1.2（末尾追加 `source_language` / `translation_basis`），加翻译溯源规则 + worked example；v1/v1.1 仍容忍。
- [scripts/validate_repo.py](../scripts/validate_repo.py)：接受 v1.2、校验 `translation_basis` 枚举、`mira/provider_translation` 缺 `original_excerpt=` 时 WARN。
- 7 个 `templates/*/evidence-log.csv` 全部升 v1.2。**透明说明**：其中 6 个原本停留在 v1（连 v1.1 posture 字段都没有），本次一并补齐到 v1.2——顺带完成了之前未完成的 posture 迁移。
- 翻译溯源遵循：`claim_text` 保持单条 claim，原文进 `notes` 的 `original_excerpt=` 键值，未开第三列。

**Phase 2**（市场默认包）
- 新建 [data/market-default-packs.csv](../data/market-default-packs.csv)（US / CN_A_share / HK / JP / TW / KR / EU，含 disclosure/structure targets、calendar、currency、accounting_standard、translation_caveats、coverage_gap_action）。
- [data/public-source-targets.md](../data/public-source-targets.md) 加 Market Default Packs 段；[OPERATING_CONTRACT.md](../OPERATING_CONTRACT.md) lazy-loading map 加一行。规则：pack 按 `market_scope` 套用，与语言正交。

**Phase 3**（渲染规则）
- [data/controlled-vocabulary.md](../data/controlled-vocabulary.md) 加 Localization Rendering 段（render-don't-fork；机器层永不翻译）。
- [templates/delivery-checklist.md](../templates/delivery-checklist.md) 加 output_language / market-pack / 本地化渲染 / evidence v1.2 校验项。

**验证**：`validate_repo.py` 0 errors / 0 warnings；behavior eval **17 passed / 0 failed**（原 12 + i18n 5，均有 test-blind transcript）；v1.2 校验逻辑通过合成自测。

**i18n eval 跑通记录（test-blind 子代理，方法同 BASELINE）**：首轮 5 个 prompt 跑出 3 PASS / 2 FAIL，2 个失败各含一处 eval 脆性 + 一处真实发现：
- 真实发现 ①（已修）：英文 prompt 在中文为主的 workspace 里，`output_language` 被锚定成 `zh-CN`。把语言规则从 controlled-vocabulary（加载靠后）**前置到 [MIRA.md](../MIRA.md) Identity Contract**（高显著度）后，重跑产出 `output_language=en` 且全英文 → 转 PASS。这是 eval→修→复验闭环的实证。
- 真实发现 ②（校准）：英文"can I add now"被判 `decision_pressure=high`，中文等价 fixture 为 `medium`。该措辞 band 处于边界、跨语言可分歧；i18n case 改为锁 `disconfirmation_required=yes`（真正的纪律），精确 band 仍由中文 case 单独锁定。
- eval 脆性（已修）：英文输出首字母大写/空格渲染（"Facts"、"Must Refresh If"、"Flip the question"）未匹配小写下划线断言 → 断言改为大小写/渲染容忍。

**未做（留作后续）**：未强制迁移历史 cases/ 的 evidence-log（v1/v1.1 仍容忍，按 schema 迁移顺序逐步推进）；glossary 暂未纳入 evidence-schema 枚举（translation_basis 值）的多语言显示串。
