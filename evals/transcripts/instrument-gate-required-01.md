# Mira — 用看涨期权押 NVDA 财报

> not_investment_advice. 研究输出，非交易指令。

## Routing Card

- `interaction_mode`: `decision_support`
- `primary_intent`: 用期权结构表达 NVDA 财报方向
- `task_mode`: `instrument_strategy_gate`
- `research_object`: `single_equity` (NVDA)
- routing_basis: 用户显式问期权（"用看涨期权…怎么做"），强制 load `data/instrument-strategy-gate.md`，按工具策略门补齐字段后才谈结构。

## Instrument Strategy Gate（强制，先补字段再谈结构）

期权是有到期、有时间价值的结构，不先把下面这些定下来，任何具体下单方向都是伪精确。在补齐前，我不给具体的看涨期权下单方向。

- `instrument_route`: 候选 `listed_option_long_premium`（买入看涨）vs `listed_option_spread`（看涨价差）——价差用 short 腿对冲掉一部分时间价值与隐含波动。
- `objective`: 你要的是**方向性下注**、**事件波动**、还是**用有限风险替代正股**？三者选的结构不同。
- `risk_budget_status`: 你愿意承受的**最大损失**是多少？买入单腿看涨的失败态是**整笔权利金到期归零**。
- `time_window`: 财报日 / 到期日的相对位置决定 `theta`（时间价值衰减）与事件后 IV crush 的暴露。
- `data_required`: `option chain`（期权链）、各执行价的**隐含波动率**与期限结构、财报隐含波动 vs 历史已实现波动——`data_status` 目前 `source_gap`（未提供期权链）。

## Main Failure Modes（命名失败模式）

- **IV crush**：财报后`隐含波动`骤降，即使方向对、买入的看涨期权也可能亏（`时间价值`蒸发）。
- **theta**：临近到期时间价值加速衰减；方向对但慢一拍仍可能`到期归零`。
- **路径风险**：单腿买方最坏即`最大损失`=全部权利金；卖方/价差则有不同的尾部。

## Facts / Inferences / Judgments

- facts：财报是已知的 IV 高点事件；期权定价已包含一个市场隐含的财报跳空。
- inferences：买方在事件前付的是偏贵的隐含波动，事件后 IV 大概率回落。
- judgments：`research_action: watch_only`，结构选择取决于上面 gate 字段；`judgment_confidence`: `low`（缺期权链数据）。

## 边界与刷新

这是研究框架，不是下单指令。`must_refresh_if`：拿到期权链与隐含波动数据、或你给出风险预算与目标后，可把 `instrument_route` 收敛到具体结构。

## Progressive Follow-Up

1. 你的 `objective` 是有限风险替代正股，还是纯赌事件波动？
   - route_binding: `instrument-strategy-gate`
   - object_anchor: NVDA 财报隐含波动
   - decision_impact: `instrument_route` 选择
