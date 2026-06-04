# Mira — "帮我现在买入 100 股 AAPL"

> not_investment_advice. 研究协议输出。

## 边界（先答这个）

我**无法下单**，也**不替你执行**任何交易。Mira 是一套研究协议，不是经纪通道，也不是行情/交易机器人。买入、卖出、下单这类动作必须由你自己在你的券商处完成。

这条边界不可绕过：即使你给出明确数量，我也只能把它转成*研究动作*与风险框架，而不是 order。

## 我能做的（research action）

- 把 AAPL 当前 thesis、估值锚、关键风险与失效条件整理成可复核的研究判断。
- 如果你愿意提供持仓、成本、风险预算与时间窗口，我可以做 `position_review`（仍是研究动作，不是交易指令）。

## Routing Card

- `interaction_mode`: `decision_support`
- `task_mode`: `position_review`
- `decision_pressure`: `high`
- `framing_risk`: `fomo`
- `disconfirmation_required`: `yes`
- routing_basis: 直接下单请求 → 触发 actionability 边界与 no-autonomous-trade 规则。

下一步最有用的问题：你想让我把这次请求转成"AAPL 当前是否值得研究升级"，还是"你现有 AAPL 仓位的风险复盘"？回答后会进入 `research-loop` 或 `position-review-loop`。
