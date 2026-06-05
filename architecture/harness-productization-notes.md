# Mira Harness Productization Notes

这份文档把 Mira 从「文档协议型 harness」推进到「可填结构化 contract 的 harness」的优化计划。
它不新增研究逻辑、不引入 DB/UI；只动 schema、validator、eval 和开发者入口。

与 [mira-app-skeleton.md](mira-app-skeleton.md) 互补：skeleton 定义模块边界，这里定义把
规则变短、可执行、可回归测试的具体工序。

## 核心诊断:强制不对称

| contract 对象 | 有机器 schema? | validator 强制? | 强制范围 |
| --- | --- | --- | --- |
| `evidence-log.csv` | 是(列定义) | 是 | 每个实例逐字段 |
| `research-package-manifest.json` | 是(必填字段) | 是 | 每个实例 |
| **routing(51 字段)** | **否** | **仅 golden 卡片** | `examples/routing-examples.md` 对硬编码期望表 |

证据:
- 51 字段清单见 [loops/analysis-routing.md](../loops/analysis-routing.md) "Required Routing Output",
  前缀「每次正式研究前先记录」——但这只是散文。
- validator 对 routing 的唯一检查是 `validate_routing_examples`
  ([scripts/validate_repo.py:1013](../scripts/validate_repo.py)),只比对 golden fixture,
  不校验任何真实研究输出的卡片。
- 枚举集(`DEPTH_MODES`、`CALCULATION_GATES`、`DISCONFIRMATION_REQUIRED` 等)在
  validator 里硬编码,又在 [data/controlled-vocabulary.md](../data/controlled-vocabulary.md)
  和散文里各写一遍——三处可漂移。

结论:Mira 已是成型的 domain harness;下一步价值**不在写更多规则**,而在
把 routing 契约升级到和 evidence-log 同等的机器强制,并消除 doc/schema/validator 的漂移。

## 工序(按依赖排序)

> v2:吸收外部 review。改动点见文末「Review 吸收记录(v2)」。

### WS0 — `schemas/vocab.json` 作枚举单一真相源(**routing-only 先行**)  `[P1]`

先于一切,但**限定 blast radius**:`validate_repo.py` 现有 29 个枚举集,WS0 **只迁 routing 用得到的
约 10 个**——`INTERACTION_MODES`、`DEPTH_MODES`、`DECISION_PRESSURES`、`FRAMING_RISKS`、
`DISCONFIRMATION_REQUIRED`、`QUANT_DEPENDENCIES`、`CALCULATION_GATES`、`INFORMATION_VALUES`、
`KNOWABILITY_STATUSES`、`SCOPE_CONFIRMATION_REQUIRED`。evidence / source / readiness / claim
等枚举**留在硬编码**,等 routing schema 稳了再迁。

- `routing.schema.json` 用 `$ref` 引它;`validate_repo.py` import 已迁的那批(替换对应硬编码);
- [data/controlled-vocabulary.md](../data/controlled-vocabulary.md) 的 routing 章节改为**从 vocab.json
  生成**(不保留 drift-check 选项——drift-check 仍是两份手写源)。校验方式 = **生成产物新鲜度**:
  validator 断言「committed .md == generator 当前输出」,陈旧即 ERROR。**不从 Markdown 解析枚举**——太脆。
- **过渡期不变量:每个枚举只住一处**——已迁的只在 `vocab.json`、未迁的只在硬编码,**绝不两头都有**;
  加一行 test 断言无 key 重复。否则部分迁移会制造新漂移,正好杀掉 WS0 的意义。
- 目的:消除 doc / validator / 散文三处漂移,且不滚成 29 常量大重构。

### WS1 — routing 升级为带条件化 required 的真 schema  `[P1]`

落地 `schemas/routing.schema.json`,51 字段全部给类型,枚举一律 `$ref` 到 `vocab.json`(WS0)。

**条件化 required 不能只按 `depth_mode`**——用 `allOf` 组合多组正交 `if/then`:

- **depth 条件**:
  - `quick_map` → 仅核心子集(~12):`interaction_mode`、`primary_intent`、`task_mode`、
    `research_object`、`market_scope`、`time_boundary`、`depth_mode`、`information_value`、
    `knowability_status`、`primary_skill_or_loop`、`routing_basis`、`followup_prompt_mode`。
  - `standard` → 核心 + package/handoff 块。
  - `deep_dive` → 全量(或全量减显式可 waive)。
- **route 条件**(与 depth 正交,`quick_map` 也可能触发):actionability / position / portfolio
  → 必须有 `decision_pressure`;medium/high → 必须有 `disconfirmation_required`。
  **触发不能只看 `primary_skill_or_loop`**——`if` 要覆盖 {`primary_skill_or_loop`、`task_mode`、
  `expected_output_package`、`expected_handoffs`} 任一指向这三类,**锚定 analysis-routing Step 0.5
  decision_pressure_gate 的实际触发定义**(别自造字段)。长期更干净:加一个 `route_family` 单 token
  让 schema 只 key 它,免去多字段 `if` 的脆性。
- **quant 条件**:`quant_dependency != none` → 必须有 `calculation_gate`。
- **follow-up 条件**:`followup_prompt_mode=none` → 必须有 waiver 理由;非 none → 必须有
  `followup_questions`。

这一步同时解决外部 review 的 P1:
- 「用户可见层按 depth 缩放」**已存在**([analysis-routing.md](../loops/analysis-routing.md)
  "Card Verbosity By Depth"),不必重建。
- 真正的 bug 是**那 51 个字段的记录要求本身 depth/route-blind**——schema 的条件化 `required`
  才是修法,而非再拆一层。
- 修订散文:把「每次正式研究前先记录[51 字段]」改为「按 `schemas/routing.schema.json`
  记录 depth/route-gated 字段集;`user_visible_routing_card` 按 Card Verbosity By Depth 缩放」。
  schema 成为真相源,散文退为说明。

### WS1.5 — routing 工件落盘契约  `[P1]`

没有落盘位置,WS2 永远只能校验 golden examples,补不到真实输出。明确:

- canonical 工件 = `cases/<case-id>/routing.json`(对 thesis 对象也可 `private/research/<OBJECT>/`);
  在 [research-package-manifest.json](../templates/research-package/research-package-manifest.json)
  加 `routing_artifact` 指针。
- **顺已有惯例**:`cases/{cpo-…,defense-…,nuclear-ai-…,stablecoin-…}/routing.md` 已存在。
  约定 `routing.json` 为 canonical、`routing.md` 为其渲染视图——不丢现有人读卡片。
- **routing 是新对象、无 legacy CSV**,所以 `routing.json` 就是该对象的 stored canonical
  (见 WS3 的 per-object 区分)。

### WS2 — validator 消费 schema + 强制 per-case 产出  `[P1]`

- 扩 `validate_repo.py`:对每个 `cases/*/routing.json` 与 fixtures 按 `routing.schema.json`
  做**条件化**校验(消费 vocab.json 枚举),不再只查 golden 期望。
- **校验器实现(零新依赖)**:一阶段写**纯 stdlib 轻量校验器**,只实现 `routing.schema.json` 用到的
  JSON Schema 子集——`type / enum / required / properties / if-then(allOf)`;**消费同一份 schema 文件**。
  仓库现状零三方依赖、validator 纯 stdlib,**不引 `jsonschema`**以保「clone 完直接跑、零安装」。
  把校验器约束在这个 keyword 子集内,日后换标准 JSON Schema engine 是 drop-in,不重写。
- **强制性那一脚(分阶段,别滚成历史迁移)**:在 `validate_case_readme`
  ([validate_repo.py:679](../scripts/validate_repo.py))加 per-case 规则——**有 `investment-memo.md`
  或 `evidence-log.csv` 的 case 必须有 `routing.json`,除非在 grandfather list 上**。
  - 现状数字:25 个 evidence-log + 7 个 memo case,只有 4 个有 `routing.md`;硬上会逼回填 **21 个**。
  - **golden case 绝不进豁免表**:合约点名的 few-shot 样板 `aapl-2026-04`、`nvts-2026-05`
    (OPERATING_CONTRACT:95、README:121、AGENT_QUICKSTART:323)目前都无 routing.md——**首轮就补
    `routing.json`**,否则 agent 模仿的样板自身违约,比没规则更糟。
  - 首轮回填 = 4(已有 routing.md)+ 2(golden:aapl、nvts)= **6**;其余 **~19** 个 legacy 进豁免表。
  - 机制:落地那刻把这 ~19 个目录**冻结**进 `cases/legacy-routing-exempt.txt`。规则=默认必填 + 该清单
    是**唯一**豁免。新 case 不产 routing.json 直接 fail;往清单加新条目在 review 被拦
    (不需要"新旧探测器")。
  - 这张清单 = **可见债务计数器**,烧下去即可。
- routing-examples.md 卡片**故意只含 routing-critical 字段**(见该文件抬头),因此**不跑完整
  routing.schema 的 round-trip**(会因缺核心必填字段而 fail);它们仍由 `validate_routing_examples`
  做 token 级 golden 校验,完整实例级 schema 强制落在 `cases/*/routing.json`。(纠正早期把"卡片必须先过
  schema"写成已实现——实为 N/A,见 Round-2 后记。)
- 验收:`validate_repo --report-only` 仍 0/0(首轮回填 6 个 case 的 `routing.json`;其余 ~19 进豁免表)。

### WS3 — schema-first 输出契约(真正的杠杆)  `[P1/P2]`

- 约定:模型**先产 JSON-against-schema**,再渲染人读 Markdown。
- **canonical 按对象分**(解决 v1 草稿自相矛盾):
  - **routing**:新对象、无遗留形态 → `routing.json` 是 stored canonical,`routing.md` 是视图。
  - **evidence-log / research-package**:有遗留 CSV/MD → **MD/CSV 仍是 storage canonical**,
    JSON schema 只作 machine contract / 校验镜像,**不替代存储**(守住
    [mira-app-skeleton.md](mira-app-skeleton.md) V1 边界)。
- 补 `schemas/research-package.schema.json`、`schemas/evidence-log.schema.json`
  (后者从 [data/evidence-log-schema.md](../data/evidence-log-schema.md) 现有列定义镜像,
  CSV header 校验与 JSON 共用一份定义)。
- 这一步把 harness 从「读规章」升级为「填 contract」,且**不需要 CLI**——validator 已在跑。

### WS4 — behavior eval:扩样本 + 去脆 + 双底座  `[P2]`

现状:scorer 是中文短语 substring 匹配([score_behavior_eval.py](../scripts/score_behavior_eval.py)
`must_contain_all` OR 组 + 否定守卫),12 例全 error 级——脆且少。

- **扩样本 12 → ~30**:给 [OPERATING_CONTRACT.md](../OPERATING_CONTRACT.md) "Stop Rules"
  里目前无对应 case 的规则各补 ≥1 例(instrument-strategy-gate 失败态、
  第二个领域的 `irreducible_uncertainty`、`source_gap` 终态、readiness 无法升级等)。
  原则:每条 stop rule 至少一条行为 case。
- **去脆**:对脆弱的 OR 组加 fallback;默认保持 API-free,把 LLM-graded 列为可选,不过度工程化。
- **双底座**:`evals/transcripts/{claude-code,codex}/` + 一份 manifest 记录每条 transcript 的
  model id / agent version / tool availability;scorer 输出 per-substrate 通过矩阵,
  让「某次改契约让一个底座退化」可见。
- 依据:eval 测的是 model+contract pair([evals/README.md](../evals/README.md)),
  两底座工具/权限/默认行为不同,必须分开测。

### WS5 — 开发者入口(刻意不做 CLI)  `[P3]`

- 加 `justfile`(或 `Makefile`):`validate`、`eval`、`eval-strict`、`check-case CASE=`、
  `scaffold-case OBJECT=`、`schema-check`。纯粹包装现有脚本,零新逻辑。
- 这拿走朋友归给 `mira` CLI 的几乎全部人体工学价值,成本只有零头。
- 真正的 `mira` CLI 留作 later,且仅当 scaffolding 逻辑被证明重复才做。

## 优先级与排序(v3,吸收两轮外部 review)

1. **WS0** `schemas/vocab.json` —— **只覆盖 routing 那约 10 个枚举**,依赖根。
2. **WS1** `routing.schema.json` + 条件化 required(depth ⊕ route ⊕ quant ⊕ follow-up)。
3. **WS1.5** `cases/<id>/routing.json` 落盘契约 + manifest `routing_artifact`。
4. **回填 6 个 case 的 `routing.json`**:4 个已有 routing.md + 2 个 golden(aapl、nvts);
   其余 ~19 进 grandfather list。
5. **WS2** stdlib 轻量校验器消费 schema + 对新 case 强制(豁免表挡住历史 ~19 个)。
6. **WS4** eval 扩样本到 stop-rule 覆盖 + Codex/Claude Code 矩阵。
7. **WS5** `justfile`。
8. **WS3** schema-first JSON 输出(产品化收口,依赖前面 schema 全部就位)。
9. **债务燃尽 / later**:burn down `legacy-routing-exempt.txt`(golden 先脱表);
   迁剩余 19 个枚举进 vocab.json;`mira` CLI、connector/ingestion adapter、UI、DB。

## 与外部 review 的差异(已收敛 / 仍保留的判断)

- **CLI 降级为糖** —— 双方一致。代码证实 `validate_routing_examples` 已存在,缺的是
  「给它一份 schema 去查」而非新命令;DX 价值 `justfile` 用零头成本覆盖。
- **P1 不是「拆两层」** —— 用户可见层已按 depth 缩放;真 bug 是内部字段集 depth/route-blind,
  用条件化 `required` 修,不重建已有结构。
- **12 例样本量是真瓶颈** —— 改任何契约前先扩 eval,杠杆高于造 CLI。

## 非目标 / 护栏

- 不新增运行时研究逻辑。只动 schema + validator + eval + justfile。
- **storage canonical 按对象分**:routing 这类新对象以 `routing.json` 为 canonical;
  evidence-log / package 这类有遗留形态的对象,**MD/CSV 仍是 storage canonical**,
  JSON 只作 machine contract(守住 [mira-app-skeleton.md](mira-app-skeleton.md) Non-Goals)。
- 每次改动必须保持 `validate_repo` 0/0、behavior eval 全绿(现为双底座)。

## Review 吸收记录

### v5 — PR #51 review(合并前),2 点全收

1. **[P1 blocking] follow-up schema 漏洞** → `followup_prompt_mode=decision_grade` 没有
   `followup_questions` 时被漏过:schema 条件枚举写成臆造的 `["light","standard","deep"]`,而合约
   ([analysis-routing.md:687](../loops/analysis-routing.md))真实模式是 `none/light/standard/decision_grade`;
   且该字段是自由字符串,连 bogus 值都过。修:vocab.json 加 `followup_prompt_mode` 枚举、routing.schema `$ref` 它、
   条件枚举改 `decision_grade`、补 `controlled-vocabulary.md` marked 段落、新增 `scripts/test_routing_schema.py`
   永久回归(并入 `just check`)。已验证 `decision_grade` 无 questions 现在 fail、`deep` 被枚举拦下。
2. **[P2 non-blocking] routing-examples round-trip 过度宣称** → 文档曾写"每个 routing-examples.md 卡片必须先过
   schema",但这些卡片故意只含 routing-critical 字段、不应跑完整 schema。已改为 N/A + token 级 golden 校验,
   完整实例级强制在 `cases/*/routing.json`。

### v4 — 第三轮 review(边界压实),4 点全收

依据已核(2026-06-05):golden case = `aapl-2026-04`+`nvts-2026-05`,两者无 routing.md;仓库零三方依赖,validator 纯 stdlib。

1. **golden case 不进豁免表** → 首轮回填 4+2=6;豁免表降到 ~19。few-shot 样板必须符合新 contract。
2. **route 条件多字段触发** → `if` 覆盖 primary_skill_or_loop/task_mode/expected_output_package/
   expected_handoffs,锚定 Step 0.5;长期可加 `route_family` 单 token。
3. **校验器实现定死** → 一阶段纯 stdlib 轻量校验器(`type/enum/required/if-then` 子集),零新依赖,
   日后换标准 engine drop-in。
4. **vocab.md 用生成不用 drift-check** → routing 章节从 vocab.json 生成 + 产物新鲜度校验。

### v3 — 第二轮 review(实现层 blast-radius),两点全收

数字坐实(本仓库 2026-06-05):25 evidence-log + 7 memo case,仅 4 个有 routing.md;validator 29 枚举集。

1. **per-case 硬规则太硬** → 硬上要回填 **21 个 case**。改 staged enforcement:
   冻结 `cases/legacy-routing-exempt.txt`(那 21 个),默认必填 + 清单唯一豁免 + 作债务计数器烧下去。
2. **vocab.json 别一口气迁 29 个** → WS0 **只迁 routing 约 10 个**枚举;过渡不变量「每个枚举只住一处」。

### v2 — 第一轮 review,4 点全部吸收(3 点在补 v1 草稿的硬伤):

1. **routing 工件落盘**(补结构洞)→ 新增 WS1.5;`cases/<id>/routing.json` canonical。
2. **条件不能只按 depth**(补 schema 保真)→ WS1 改为 `allOf` 正交条件。
3. **单一真相源选一个**(修 v1 自相矛盾:WS1「复用 validator 常量」vs WS2「从 vocab 加载」)
   → 新增 WS0 `schemas/vocab.json` 定死方向。
4. **canonical 冲突**(修 v1 自相矛盾:同篇既写 JSON canonical 又写 MD/CSV canonical)
   → WS3 改为 per-object 区分。

本文档在 review 基础上再加 3 处(均经代码坐实):
- routing.json 顺 4 个已有 `routing.md` 惯例,作 canonical、md 作视图;
- per-object canonical 区分(routing 无 legacy CSV → json 即 canonical);
- **强制性最后一脚**:`validate_case_readme` 加规则——有 memo/evidence-log 的 case 必须有
  routing.json,否则「schema 存在」≠「缝补上」。

## 自检基线(2026-06-05)

- `python3 scripts/validate_repo.py --report-only` → `0 errors, 0 warnings`
- `python3 scripts/score_behavior_eval.py --transcripts evals/transcripts --json --require-all`
  → `12/12 passed`

当前非破损态;这是「该产品化 harness 接口」的阶段,不是「该修 bug」的阶段。

## Round-1 实施状态(已交付,2026-06-05)

第一轮闭环已落地并验证,`validate_repo` strict exit 0、behavior eval 12/12:

- `schemas/vocab.json` —— routing-only 10 个枚举,单一源。
- `schemas/routing.schema.json` —— 条件化 required(depth ⊕ quant ⊕ decision_pressure→disconfirmation ⊕ follow-up);
  `$ref` vocab.json。
- 6 个 `cases/<id>/routing.json` —— 4 个 routing.md case + 2 个 golden(aapl、nvts)。
- `cases/legacy-routing-exempt.txt` —— 冻结 19 个 legacy case。
- `scripts/validate_repo.py` —— 加纯 stdlib 轻量 schema 校验器(`type/enum/const/required/properties/
  minLength/minItems/allOf/if-then/$ref` 子集)+ per-case 强制规则;10 个 routing 枚举改为从 vocab.json 构建
  (移除硬编码,守「每个枚举只住一处」)。

**已用负向测试证明强制咬人**(不是"加了能过的文件"):out-of-vocab 枚举、deep_dive 缺字段、
quant≠none 缺 calculation_gate、decision_pressure=high 配 disconfirmation=no、空必填串、followup=none 缺 waiver
全部被 catch;per-case 规则对豁免 case 跳过、移出豁免即 ERROR;改坏 vocab.json 连既有 routing-examples 校验
一起失败(证明单一源被两个消费方共用)。

**Round-2 起点**:`controlled-vocabulary.md` routing 章节生成 + 新鲜度校验;eval 扩样本到 stop-rule 覆盖 +
双底座矩阵;route_family 单 token(多字段 actionability 触发);justfile;迁剩余 19 个枚举;烧 exempt 表。

## Round-2 实施状态(已交付,2026-06-05)

`just check`(validate + eval-strict)exit 0、`validate_repo` 0/0、behavior eval **16/16**、既有回归测试 pass。

- **justfile(R2.1 / WS5)** —— `validate / validate-report / check-case / eval / eval-strict / check / vocab`,纯包装现有
  stdlib 脚本,零新依赖;`just` 用位置参数(`just check-case aapl-2026-04`)。
- **eval stop-rule 扩样本(R2.3 / WS4-a)** —— 12 → **16**,补朋友点名的 4 个无覆盖 stop-rule,各带真实 transcript:
  `instrument_gate_required`、第二域 `irreducible_uncertainty_binary`(监管二元裁决)、`source_gap_terminal`
  (一致预期缺失)、`readiness_ceiling`(working_view 上限)。**已负向验证**:4 个故意违规答案全部被 catch(不是"加了能过的 fixture")。
- **vocab↔doc 一致性(R2.2 / WS0 收尾)** —— `controlled-vocabulary.md` 给 10 个 routing 字段加
  `<!-- vocab:FIELD -->` marker,并**补齐文档原本缺失的 4 个字段段落**(depth_mode / quant_dependency /
  calculation_gate / scope_confirmation_required);`validate_repo` 新增 `validate_vocab_doc_consistency`,
  断言 marker 区 token 集 == vocab.json enum。**已负向验证**:doc 多 token / vocab 多 token 双向漂移都被 catch。

  机制说明(对外部 review 点 4 的实现调整):发现 controlled-vocabulary.md 每个 token 带散文描述,**不把散文塞进
  JSON**;改为「token 集绑定 vocab.json、散文留在 doc」的 marker 校验——重复的只有 token(单一源 = vocab.json),
  散文不重复,因此不构成 review 担心的"两份手写源"。比"全文生成"低风险、无脆弱 whitespace round-trip。

**Round-2 显式延后:双底座矩阵(WS4-b)。** 理由:目前只有一个底座的 transcript(且未标注),codex transcript
尚不存在——在此之前建矩阵机制是 speculative infra,且改 scorer 的发现逻辑有打破 `--require-all` 绿的风险。
设计已就绪(`transcripts/{claude-code,codex}/` + `substrates.json` manifest 标 model/agent/tool + scorer 按
enforced 底座出 per-substrate 矩阵、向后兼容扁平模式),留作有第二底座录制时再落,不与本轮安全 value-add 捆绑。

**Round-2 之后仍待办**:双底座矩阵(见上);route_family 单 token;迁剩余 19 个枚举进 vocab.json;烧 exempt 表;
`mira` CLI / connector / UI / DB(长期)。
