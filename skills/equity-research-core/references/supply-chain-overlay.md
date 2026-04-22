# Overlay: Supply Chain

这个 overlay 用于沿公司上下游和同层级关系继续研究，而不是只停留在公司本体。

## Objective

回答五个问题：

1. 上游谁决定成本、产能、良率或交付。
2. 下游谁决定需求、收入确定性或 ASP。
3. 同层级公司里，谁在抢份额，谁在验证行业景气。
4. 利润池和议价权在哪一层。
5. 哪个环节最可能成为 thesis 被证伪的位置。

## Required Outputs

至少给出：

- upstream map
- downstream map
- same-layer peer map
- transmission logic
- falsification points

## What To Look For

上游：

- 原材料、零部件、设备、代工、物流
- 成本变化是否能传导
- 产能约束是否会卡住兑现

下游：

- 客户集中度
- 终端需求强弱
- 渠道库存和补库去库节奏
- 订单可见度和续单风险

同层级：

- 可比公司谁先给出景气信号
- 哪家公司更能代表行业真实变化
- 当前标的是领先、跟随，还是边缘受益者

## Large-Mega Example Shape

如果主框架是 `large-mega`，`supply-chain` overlay 更关注：

- 宏观需求如何传导到终端消费
- 龙头客户如何拉动整条供应链
- 哪些上游或中游公司是受益映射

典型用途像：

- 从 AAPL 出发，往消费电子需求、零部件、代工、渠道和竞品映射

## Micro-Small Example Shape

如果主框架是 `micro-small`，`supply-chain` overlay 更关注：

- 单一客户是不是收入锚
- 单一供应商或产能瓶颈是不是成本和兑现风险
- 同层级竞品里谁更能证明这家公司真的有优势

典型用途像：

- 从一个小票出发，核验它是否真的卡位某个环节，还是只是在讲故事

## Common Failure Mode

最常见错法不是“不看供应链”，而是：

- 只画链条，不判断哪一层对股价最重要
- 把产业链常识误当成公司级证据
- 忽略同层级对照，导致无法验证叙事真伪
