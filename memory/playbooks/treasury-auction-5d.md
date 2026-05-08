# Playbook: Treasury Auction 5D Structure

- last_updated: 2026-05-08

## Use When

- 美国国债拍卖结果发布（2/3/5/7/10/20/30Y，每月或每周）
- 收益率突破关键位时回看最近几次拍卖质量
- 评估海外央行需求趋势

## Signal Set

- **Tail**：High yield − When-Issued (WI) yield，单位 bp
- **Bid-to-cover (BTC)** ratio vs 过去 6 次平均
- **Indirect bidder %**（外国央行/机构需求）
- **Direct bidder %**
- **Primary dealer take %**（高 = 没人接 = 滞销）

## Pattern

- Tail > 1.0 bp = 弱；> 2.0 bp = 警报
- BTC < 2.30 = 弱
- Indirect 跌破 60% = 海外需求恶化
- Dealer take > 20% = 滞销，鹰派信号
- 双重糟糕（高 tail + 低 BTC + 高 dealer）⇒ 收益率向上突破风险，2024-04-10 双拍卖暴雷案例
- 负 tail（拍卖收益率低于 WI）⇒ 强需求

## Interpretation

5 维拼起来给方向：执行质量（tail + BTC）+ 海外需求（indirect）+ 滞销信号（dealer）。短期映射当日收益率（±5bp 量级）；中期观察外国买家结构变化的趋势。
