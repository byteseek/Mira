## Mira 路由卡 (analysis-routing)

| 字段 | 值 |
| --- | --- |
| `interaction_mode` | `quick_answer`（用户问"靠不靠谱"，要方向判断） |
| `primary_intent` | 评估一则"某半导体小票被大厂收购"传言的可信度 |
| `scope_confirmation_required` | `yes`（标的、收购方、消息源都未给出） |
| `task_mode` | 因对象未知，实质降级为 `routing_unclear` 处理 |
| `research_object` | 未确定（未点名 ticker，未点名"大厂"，无消息源） |
| `market_scope` | 未知 |
| `time_boundary` | `intraday_to_days`（传言驱动，事件型） |
| `depth_mode` | `quick_map` |
| `information_value` | `low` |
| `knowability_status` | `unknowable_now` → 对"传言本身真假"近 `irreducible_uncertainty` |
| `private_state_action` | `waive` |
| `decision_pressure` | `low`（research-only 提问，无"能不能买/加/冲"动作语） |
| `framing_risk` | `confirmation_seeking`（问题结构="这事靠谱吗"，倾向寻求是/否背书） |
| `disconfirmation_required` | `yes` |
| `quant_dependency` | `none`；calculation_gate=not_required |
| `readiness_level` | `not_actionable` / `watch_only` |
| `followup_prompt_mode` | `light` |

## 研究判断：这则传言靠不靠谱

先给直接答案：以目前给到的信息，无法判断靠谱与否，默认按"未经证实的弱信号"处理——不可作为结论或行动依据。你给的核心信息只有"有传言"，三个属性缺失（无标的、无收购方、无消息源），而并购传言的真伪本质上由官方披露前的非公开信息决定，对外部研究者是 `unknowable_now`。

### Facts（已知事实）
- 存在一则"某半导体小票将被大厂收购"的传言。`claim_type = rumor_signal`，`source_speaker` 未知，`verification_status = unverified`，`evidence_category = weak_signal`。
- 你未提供：具体标的、收购方、消息来源、传言时间、是否有价量异动。
- 我当前可能未联网，无法核验任何具体并购事实——不会编造标的、溢价、进度或买方。

### Inferences（推断，置信度有界）
- 半导体小盘股的并购传言是高频叙事品类："故事自洽"不等于"正在发生"。
- 此类传言基础比率很低：绝大多数"被收购"传言最终未兑现为正式交易。`base_rate_anchor`：未经证实的单标的并购传闻，证实率历史上偏低。
- 传言若已推动股价异动，那是 `market_pricing`，不构成基本面或交易事实的验证。

### Judgments
判断 1：在缺少官方披露或多个高质量独立来源前，这则传言不应支撑任何研究结论或参与决策。
- `judgment_confidence`: high
- `confidence_basis`: Mira 证据纪律硬规则——rumor_signal / weak_signal 默认不得进入 core conclusion。
- `reversal_condition`: 出现高质量确认即升级——标的或买方官方公告/8-K/交易所披露、监管反垄断申报、双方确认的权威媒体报道（非匿名单源）。

判断 2（反向检验，disconfirmation）：
> 如果把问题反过来问——"凭什么相信它是真的？"——当前证据答案是：没有任何可核验依据。一个匿名/未具名的并购传言，在 base rate 偏低、信息不可知的前提下，默认应被当作未兑现，而不是"待确认的利好"。
- `reversal_condition`: 只有原始/监管/多源高质量确认能把它从"默认不成立"翻转为"值得正式研究的事件"。

### Knowability（诚实终态）
- 传言真伪：`unknowable_now`，趋近 `irreducible_uncertainty`。
- 可降级为可研究问题：一旦你补上标的，我可以研究可知的部分（股权是否分散、估值、战略买方逻辑、近期价量异常），给传言一个先验合理性评分，但仍不能证实交易本身。

### 边界声明
- 这是研究判断，不是交易建议。我没有建议你买入、加仓或博弈这个传言。
- 我不会因为问题带"靠谱吗"的确认倾向，就给你一个安慰性的"可能是真的"。

### 刷新条件
- `stale_after`: 24–72 小时（传言类信号活跃监控窗口）。
- `must_refresh_if`: 出现官方公告、监管申报、多源权威媒体确认，或标的明确后转入正式事件研究。
- 若 72 小时内无任何高质量确认，默认 `watch_only` 并向"未兑现"收敛。

## Progressive Follow-Up

1. 这只"半导体小票"的具体 ticker / 上市地是哪？消息源是社媒、朋友、研报还是财经媒体？
   - route_binding: research_object + market_scope 确定后由 routing_unclear 升级进入 event-delta-loop 或单票 equity-research-core
   - object_anchor: 待定的半导体小盘标的 + 传言来源层级（L4 social vs L3 sellside vs L1 官方）
   - decision_impact: `boundary` + `evidence_path`
2. 你要的是"判断传言真假"，还是"假设传言为真/为假时该公司本身的研究价值"？
   - route_binding: task_mode（view_continuity 研究 vs 触发 decision_pressure_gate 的 actionability）
   - object_anchor: 该标的的独立基本面 vs 并购套利叙事
   - decision_impact: `actionability_boundary`
