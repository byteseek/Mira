# Playbook: NFP Establishment vs Household Survey

- last_updated: 2026-05-08

## Use When

- 美国月度就业报告（每月第一个周五）发布前后
- 飓风/罢工/政府停摆等一次性事件污染数据时
- BLS 年度基准修正（每年 9 月初）

## Signal Set

- Establishment（CES）NFP change vs Bloomberg consensus
- Household（CPS）失业率
- 平均时薪 MoM/YoY
- 劳动参与率
- 全职 vs 兼职就业（CPS）
- 本地出生 vs 外国出生工人份额（CPS）
- 月度数据修订幅度 + BLS 年度基准修正幅度

## Pattern

- 一次性事件（飓风、罢工、政府停摆）打 CES 不打 U-rate ⇒ "数据差但 Fed 不慌"，2024-11 教科书案例
- CES 强 + CPS 弱 ⇒ 兼职/移民驱动；2024 年贯穿
- CES 弱 + 大幅向下修订 ⇒ 给 Fed 50bp 降息理由，2024-09 / 2025-09 类比
- 失业率算术：手算 失业人口/劳动人口 给未四舍五入精确值（4.145% ≠ 4.1%）
- U-rate 触及 4.4% ⇒ Sahm rule 触发，衰退概率提升

## Interpretation

CES 是岗位数（含非法移民/兼职、不含罢工工人），CPS 是人头数（不含非法移民、含罢工工人）。两者背离时按背离方向解读市场反应方向，而非看 headline NFP 大小。
