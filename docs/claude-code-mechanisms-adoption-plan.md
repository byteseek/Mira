# Mira 吸收 Claude Code 设计思想优化工具无关架构 (Absorbing Claude Code's Design Principles into Mira's Tool-Agnostic Architecture)

> **状态**: 草案 / 待评审。本文只写方案，不改动任何协议文件。
> **自包含**: §1 附「现状病症速览」，未读过其他方案也能跟上。房屋风格参照 [docs/i18n-plan.md](i18n-plan.md)；背景见 [AGENTS.md](../AGENTS.md) / [MIRA.md](../MIRA.md) / [OPERATING_CONTRACT.md](../OPERATING_CONTRACT.md) / [loops/analysis-routing.md](../loops/analysis-routing.md)。
> **两条硬约束**：① 不做 CC 兼容——只取**可移植原理**进内核，驱动专属原语（plan-mode、MCP、plugin marketplace）不是交付物；② **丝滑优先、治疗不能比病重**——每个改动都必须让模型热路径上要 juggle 的字段/gate **变少或持平，绝不变多**。
> **TL;DR**: Mira **用散文手搓了 Claude Code 的一半机制**，但停在「散文规则」。因为 **Mira 的渲染器就是模型本身**，CC 思想的价值在协议改变模型行为那刻就兑现，与 harness 无关——所以只取原理、不做适配。但病症①②的本质是「**太重 / 太散**」，所以吸收原理的方式必须是**净减负**，而不是再加机制：路由**变轻**（1 屏索引取代 1.1k 行前置）、模式**变少**（一个开关收编散落 gate）、停顿**变稀**（只在真冲突时确认一次，否则声明假设照常作答）。工具**克制使用**：只在能减摩擦处放一个可选的交付前校验，不铺在每个检查点。核心纪律一句话：**能用索引就别全量加载，能合并就别新增，能不停就别阻塞，工具只在减摩擦时才用。**

---

## 1. 给外部评审者：Mira 是什么 + 现状病症速览

**Mira 是什么。** 一个「协议层、工具无关」的投研 agent 产品：纯 markdown 协议 + CSV/JSON schema，**渲染器是模型本身**；同时支持 Codex 和 Claude Code 两种驱动（见 [AGENTS.md](../AGENTS.md)）。它的「产品」是 `MIRA.md` / `OPERATING_CONTRACT.md` / `loops/` / `data/` / `schemas/` 这组协议：先路由研究类型，再选框架与证据路径，最后输出带来源链、时效边界和刷新条件的研究包。

**工具无关 ≠ 没有工具。** Mira 已有 ~40 个 `validate_*.py` CLI（[scripts/](../scripts/)），在 Codex 与 CC 下跑法一致——这证明「可移植工具」可行：只要是**普通 CLI**（读文件/stdin、写 stdout），任何驱动都能 shell 调用，不绑某个 harness。本文据此**克制地**允许新增极少量这类工具（详见 §6），但不让工具变成必经仪式。

**四个病症**（行号/字段数为本仓库实测，便于自包含）：

| # | 病症 | 现象（实测） | 本质 |
| --- | --- | --- | --- |
| ① | **重上下文** | 读到第一个具体 loop 前要顺序读 ≈ **1.8k 行**（仅 [analysis-routing.md](../loops/analysis-routing.md) 就 **1,109 行**），全部前置加载 | 太重 |
| ② | **三层不对齐** | 散文层声明 ~50 字段 / ~15 步，schema 强制 **27 property / 13 required**，eval 锁 **30 例**；模型锚在最重的散文层，只有最轻两层被自动检查 | 太散 |
| ③ | **路由卡形状漂移** | 同一逻辑路由可见字段 4–28 不等，缺机器锚点 | 太散 |
| ④ | **接力反问没做成阶梯** | 渐进反问退化成「刷新数据 + watch item」平铺清单，没爬上定价变量 / 证伪 / 下一 route | 太散 |

> 关键观察：①②本质是「太重 / 太散」。所以**任何治疗如果增加字段、增加停顿、增加工具调用，就是在加重病情**。这是本文的统帅约束。

---

## 2. 核心论点：吸收原理，用「净减负」的方式落地

Mira 不缺机制，而是**用散文重新发明了 CC 已做成原语的东西**，停在「散文规则」没走到「机器承载」。

**为什么只取原理。** 渲染器就是模型本身，CC 思想的价值在协议改变模型行为那刻兑现。harness 适配层只增**强制力**（gate 跳不过），不增**思考质量**——强制 ≠ 思考，对「提升问答效果」是无关变量，还赔上工具无关。**适配层不是交付物。**

**三条原理，但每条都以「变轻 / 变少 / 变稀」落地：**

| CC 思想 | 可移植原理 | 现状（重 / 散） | 丝滑落地 | 净复杂度 |
| --- | --- | --- | --- | --- |
| ToolSearch 索引→按需取 | 路由只读索引、命中才取正文 | 1.1k 行前置 | 1 屏 `routing-index.csv`，手读即可（工具可选） | **↓↓**（病①③） |
| hooks 确定性交给代码 | 校验交给 CLI，模型只判断 | 40 个 validator 靠「记得跑」 | 交付前**一次** `check`，收成单次调用 | **↓**（病②） |
| permission mode | 散落 gate 收敛成一个开关 | actionability / instrument / 无持仓 gate 散在多处 | 复用既有 `interaction_mode` 当 posture 开关 | **↓**（病②） |
| plan mode 确认即状态 | 范围未确认不深挖 | `scope_confirmation_required` 可跳过 | 真冲突时**确认一次**，否则声明假设照答 | **净 0**（不新增阻塞，病④） |
| subagent 对抗复核 | 独立视角复核 thesis | disconfirmation 偶发 | 强化既有 disconfirmation（**pattern**，不做工具） | 净 0（病④） |

**Mira 已学对的一半**：`CLAUDE.md` 25 行纯指针、`routing.schema.json` 结构化输出、Lazy Loading Map 雏形、~40 个现成 validator CLI。缺的另一半是把这些从「散文 / 给人读」升级成「轻索引 / 单开关 / 偶尔一次工具」，**而且总账要更轻**。

---

## 3. 深入一：索引 → 按需取（最丝滑的一刀，病①③）

ToolSearch 的本质是「先给名字索引，用时才取正文」。Mira 路由层正相反：把 12 loops / 9 skills 正文**全量前置**，模型读完 1.1k 行才碰到具体 loop。这一刀直接把「读 1.1k 行」变成「读 1 屏」——是对「丝滑」最直接的兑现。

### 3.1 `data/routing-index.csv`：1 屏窄表，模型手读即可

```csv
task_mode,trigger_one_liner,primary_loop_or_skill,load_gate
first_pass_research,"首次覆盖 / 重建 thesis",loops/research-loop.md,on_hit
earnings_event,"新财报 / 业绩会 / 指引 / 财报后反应",skills/earnings-report-analysis/SKILL.md,on_hit
sec_supplement,"补 SEC 事实核验（supplement 模式，不拆全文）",skills/sec-filing-analysis/SKILL.md,on_hit
discovery_or_screening,"找候选 / 筛选；按 research_object 分派 discovery skill",loops/analysis-routing.md,on_hit
position_review,"review 单一真实头寸",loops/position-review-loop.md,on_hit_decision_support
```

完整 12 行见 [../data/routing-index.csv](../data/routing-index.csv)（单源，勿在本文复制全表）。

- `task_mode`：Step 1 的 12 值枚举，作机器锚点 → 同一逻辑路由 = 同一 key，堵病症③。`research_object`（single_equity / industry_concept…）是自由文本、未进 vocab，故**不做索引 key**，留在 Step 2 散文。
- `trigger_one_liner`：一句话触发条件（常驻可读）。
- `primary_loop_or_skill`：正文位置，**命中前不加载**；必须是真正的执行正文（loop / skill），**不是模板 CSV**（否则命中后会失去分析指令）。
- `load_gate`：`on_hit` / `on_hit_decision_support`（与 §5 posture 联动）。
- `validate_repo.py` 校验：`task_mode` 全部属于 [schemas/vocab.json](../schemas/vocab.json) 枚举、**覆盖全部 12 个**、`primary_loop_or_skill` 路径存在、`load_gate` 合法——索引与 schema 不各漂各的。

### 3.2 工具是可选便利，不是必经步骤

- **默认丝滑路径**：模型直接手读这张小表 → 命中 → 只加载那一个 `primary_loop_or_skill`。**不需要任何工具。**
- **可选便利** `scripts/route.py`（想要的驱动可调）：读 `routing-index.csv` + `vocab.json`，输入信号→返回 `task_mode` + 唯一 `primary_loop_or_skill` + 触发的 gate + `routing.json` 骨架。它只是把手读这步自动化，**不是新依赖**；离线/不调用也不影响。
- 与现有 Lazy Loading Map 的关系：Map 留作**人类可读总览**；`routing-index.csv` 是**机器锚点**；analysis-routing.md 正文**不删**，只是路由**不再前置整篇**。契约一句话：**「路由先看索引；选定 `task_mode` 后只加载对应 `primary_loop_or_skill`，绝不前置整篇 analysis-routing。」**

---

## 4. 深入二：确认即状态——但停顿要「稀」（病④）

CC 的 plan mode 是「未批准不执行」。Mira 今天 [analysis-routing.md](../loops/analysis-routing.md) Step 0 的 `scope_confirmation_required: yes/no` 是个**可跳过字段**。但**丝滑的修法不是加一个会频繁打断的状态机**——研究 agent 逢事先确认是灾难。

### 4.1 不新增字段，强化既有机制

- **不引入** `scope_state` 四值枚举（那是再添一个 mode 字段，正中病症②）。
- **复用** Step 0 已有的 **Assumption Register**——它本就是「**声明运行假设、先答、邀请用户修正**」的非阻塞设计。默认就走它：声明假设，照常作答。
- **只在真冲突时升级成一次明确停顿**，触发条件确定性（沿用 Step 0.5 「No Silent Skip」纪律，不另起炉灶）：
  - `复合 prompt 且子任务 depth / 数据冲突`（一个要 quick_map、一个要真实持仓 review），**或**
  - `interaction_mode = decision_support` 且 `decision_pressure ∈ {medium, high}`。
- 升级后规则：该一次停顿里，**可**给 quick_map 级方向 + 路由卡 + 假设，但**不**花 deep_dive 预算、不写 durable artifact，直到用户确认或明确「别问直接做」。

### 4.2 净效果

把 `scope_confirmation_required` 从「可静默跳过的提示」**收紧成「真冲突时必停一次」**，其余一切照旧——**零新字段、零新阻塞机制**，只是给既有字段一条确定性触发线。任何驱动一致；若某驱动恰好有 plan-mode 原语，是白捡，不依赖。

---

## 5. 顺带收敛：用既有 `interaction_mode` 当 posture 开关（病②）

Mira 的领域 gate 今天**散落**：不给交易指令（MIRA.md）、actionability-risk-control、instrument-strategy-gate、无持仓不给仓位（多处 Stop Rule）。模型要同时记这 4 条。

收敛成**一个开关——但不新增字段**。`interaction_mode` 已有 `decision_support` 值，且 [schemas/routing.schema.json](../schemas/routing.schema.json) 已强制 `decision_support` → `decision_pressure`，它本就是那个开关；再造 `interaction_posture` 会与之同义、正中 §9 非目标，故**复用既有字段**：

- **research_only posture** = `interaction_mode ∈ {quick_answer, routed_research, routing_unclear}`（默认）：禁仓位 / 订单 / 交易指令输出，现有各 gate 成为它的**子条款**（不删规则，只统一挂到这一个开关下）。
- **decision_support posture** = `interaction_mode = decision_support`：仅当用户带动作语或给真实持仓时进入；进入即触发 §4 的确认停顿 + Step 0.5 decision pressure gate。

**这是净减项**：模型从「记 4 条散落规则」变成「判断一个 posture」，且**零新字段**。落地是 [loops/analysis-routing.md](../loops/analysis-routing.md) Step 0.5 的 posture 小节 + eval，无新 vocab、无 adapter。

> **实现说明**：本仓库已落地此节——`analysis-routing.md` Step 0.5 新增「Posture: research_only ↔ decision_support」小节，把安全门统一挂到既有 `interaction_mode` 下，未新增字段、未改动安全门正文。

---

## 6. 复杂度护栏 + 工具纪律

> 这些护栏的优先级**高于**任何单条改进——违反就别做。

0. **丝滑 / 净减负（统帅）**：每个 PR 合并后，模型在热路径上要 juggle 的字段 / gate / 停顿**必须变少或持平，绝不变多**。治疗不能比病重。
1. **合并优先于新增**：能用一个开关收编 N 条散落规则，就不新增并行字段；能强化既有字段，就不造同义新字段。
2. **gate 默认非阻塞**：默认「声明假设、先答、邀请修正」，只在**确定性冲突**时阻塞一次。
3. **工具克制**：① 只用**可移植 CLI**（读文件/stdin、写 stdout，任何驱动 shell 可调），禁 driver-native / MCP；② 只读 canonical 单源（`vocab.json` / `routing-index.csv` / schema），绝不 hardcode；③ 保留 **markdown fallback**，离线能手做；④ **只在减摩擦处放工具**（交付前一次 `check`），不铺在每个检查点；⑤ 确定性才配工具，判断（对抗复核）只配 pattern + eval。

**核心纪律一句话**：

> **能用索引就别全量加载，能合并就别新增，能不停就别阻塞，工具只在减摩擦时才用。**

---

## 7. 如果只挑三件（全部是净减负）

| # | 改动 | 让什么变轻 | 净复杂度 | 病症 |
| --- | --- | --- | --- | --- |
| 1 | `routing-index.csv`（+可选 `route.py`） | 路由从读 1.1k 行 → 读 1 屏 | ↓↓ | ①③ |
| 2 | `interaction_mode`-as-posture（复用既有字段） | 4 条散落 gate → 1 个开关 | ↓ | ② |
| 3 | scope 真冲突时确认一次（强化既有字段，**不新增**） | 停顿从「可静默跳过」→「稀而准」 | 净 0 | ④ |

三件都不新增 mode 字段：`task_mode` 索引复用既有枚举，posture 复用既有 `interaction_mode`，scope 复用既有字段。**总账是减的。**

---

## 8. 迭代路线（精简到 3 步）

> 治理：schema 先冻结一刀切完（防病症②再生）；加法式向后兼容（新字段先 optional + 容忍，迁完再 required，复刻 evidence-log v1.2）；锁行为不锁文风（配 eval + test-blind transcript）；**净减负**（每步合并后热路径字段不增）。

| Phase | 目标 | 主要改动 | 验收门 |
| --- | --- | --- | --- |
| **0 地基** | `routing-index.csv` + schema 微调 | 新建 `data/routing-index.csv`、`vocab.json` 复用既有枚举、`validate_repo.py` 校验 key⊆vocab + 路径存在 | validate 0 err；eval 不回归(30 passed)；无行为变化 |
| **1 路由变轻（MVP）** | 病①③ | 路由「只看索引」契约写进 [OPERATING_CONTRACT.md](../OPERATING_CONTRACT.md)；analysis-routing 不再前置整篇；**可选** `scripts/route.py` | 同 prompt 仍命中同 loop；task_mode 跨 depth 稳定；路由上下文显著变轻 |
| **2 模式变少 + 停顿变稀** | 病②④ | 复用 `interaction_mode` 当 posture，统一收编 [actionability-risk-control](../data/actionability-risk-control.md) / [instrument-strategy-gate](../data/instrument-strategy-gate.md) / 无持仓 gate（不改安全门正文）；scope 冲突即停一次（强化既有字段）；**可选**交付前 `check` | research_only 拒仓位输出；真冲突才停、否则照答；旧 gate 行为不回归 |

**MVP**：Phase 0 + 1——纯减负、零新阻塞、零必经工具，是最安全的先导切片。

**已知测试缺口（诚实标注）**：behavior-eval 打分的是**输出**，无法直接断言「模型没读那 1.1k 行」。代理验证：① 路由卡正确 + task_mode 跨 depth 稳定；② 结构 lint（索引覆盖全部 12 个 task_mode、`primary_loop_or_skill` 存在）。不假装拿到硬证明。

**成功指标**：同一问题在 Codex / CC / 其他驱动下**路由一致、上下文更轻、答案更贴意图**，病症①③④ 削掉、② 收口——且**模型要 juggle 的字段比现在少**。

---

## 9. 非目标 / 反模式（明确不做）

- ❌ **不做 CC 兼容 / 不建 `adapters/`。** 驱动专属原语（plan-mode、permission mode、MCP、plugin marketplace）不是交付物；至多日后做成**非承载性便利**（删了协议照样完整）。
- ❌ **治疗不能比病重。** 不为强制力牺牲丝滑；任何增加字段 / 停顿 / 工具调用的改动，必须同时删掉等量或更多旧机制——净账只减不增。
- ❌ **不新增与现有同义的 mode 字段。** 不引入 `scope_state` 四值枚举 / `display_mode` / `interaction_posture`（`decision_support` 已是 `interaction_mode` 值并已 gate `decision_pressure`）；**强化既有字段优先于造新字段**。
- ❌ **gate 默认不阻塞。** 不把研究 agent 变成「逢事先确认」的官僚；只在确定性冲突时停一次。
- ❌ **工具不铺在每个检查点。** 只在减摩擦处放一个可选 `check`；索引够轻就手读，不强制 `route.py`。禁 driver-native / MCP；工具只读 canonical 单源；保留 markdown fallback。
- ❌ **`routing-index.csv` 不是第二真值源**，只是既有枚举的窄投影 + 正文指针。
- ❌ **不把 analysis-routing.md 拆碎成 12 文件**（过度拆分制造新漂移矩阵，参见 [docs/i18n-plan.md](i18n-plan.md)）。
- ❌ **`research_only` 不诱导成交易指令**——`decision_support` 只解锁分析框架，仍受 [actionability-risk-control](../data/actionability-risk-control.md) 边界约束。

---

## 10. 一句话给评审

> Mira 不缺机制，缺的是把手搓的散文规则升级成**更轻**的承载——吸收 Claude Code 的三条原理（索引按需取、确定性交给代码、确认即状态），但每条都以**净减负**落地：路由从 1.1k 行变 1 屏索引、4 条散落 gate 变 1 个开关、确认从「可跳过」变「稀而准」；工具克制到只在减摩擦处放一个可选 `check`；全程不做 CC 兼容、不新增模型要 juggle 的字段。先做 §8 的 MVP（routing-index），同一问题在任何驱动下都路由一致、上下文更轻、答案更贴意图——而且整套架构比现在**更丝滑、不是更复杂**。
