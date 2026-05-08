# Skill 提案草图（5 个）

按 Anthropic skill-creator 约定写：每个 skill 含 name / description / when to trigger / workflow / fixed reference data。这里只是草图，不是 SKILL.md 文件本身。

> 通用建议：所有 skill 的输出语言跟随用户问话语言；技术 identifier（CPI、NFP、tail bp、bid-cover）保持英文。引用具体投行/分析师时给出原始链接。

---

## Skill 1: `treasury-auction-postmortem`

### Description
拆解美国国债拍卖结果（2Y / 3Y / 5Y / 7Y / 10Y / 20Y / 30Y），用 5 维结构判断需求强弱以及对收益率曲线的方向性影响。Use when user mentions Treasury auction, bid-to-cover, indirect bidder, or pastes raw auction stats.

### Trigger keywords
"国债拍卖" / "Treasury auction" / "bid-to-cover" / "10Y auction" / "tail" / "indirect bidder" / "30Y bond auction result"

### Workflow
1. 收集本次拍卖的 5 个核心数字（如果用户没给齐就从 Treasury Direct / NY Fed 取）：
   - High yield, when-issued (WI) yield → tail in bp
   - Bid-to-cover ratio
   - Indirect bidders allotment %
   - Direct bidders allotment %
   - Primary dealer take %
2. 拉过去 6 次同期限拍卖的均值（reference table 或 web fetch）
3. 给出三段式判断：
   - **执行质量**：tail 正负 + 历史排序（如 "since 2022"）
   - **海外需求**：indirect 份额 vs 趋势
   - **滞销信号**：dealer take 高 = 没人接 = 鹰派
4. 转化成方向性预期：当日收益率反应、对股票流动性影响、对未来发行计划的暗示
5. 如果是双重糟糕（高 tail + 低 BTC + 高 dealer），明确标注"市场拒绝"信号

### Fixed reference data
- 各期限近 12 次拍卖的 high yield / BTC / indirect / dealer historical table（CSV，每月手动或脚本更新）
- 关键阈值：
  - tail > 1.0 bp = 弱 / tail > 2.0 bp = 警报
  - BTC < 2.30 = 弱
  - indirect 跌破 60% = 海外需求恶化
  - dealer take > 20% = 滞销

### 不是 skill 也能做但容易漏的点
- WI yield 容易和 secondary market yield 混
- 直接 / 间接的定义会变化
- 拍卖前后 1 小时收益率对比的解读容易主观
→ 固化到 skill 后这些都能稳定。

---

## Skill 2: `liquidity-plumbing-monitor`

### Description
追踪美国市场流动性的"管道层"信号链：财政部短债 vs 长债发行结构、RRP 余额、银行准备金、SOFR、SRF/IORB、Fed RMP/Term Repo 操作。诊断"流动性紧 / 松"的方向，并映射到风险资产影响。

### Trigger keywords
"liquidity" / "RRP" / "reserves" / "T-bill issuance" / "Fed balance sheet" / "QT" / "RMP" / "SRF" / "SOFR spike" / "短债发行"

### Workflow
1. 抓当前快照（数据源：Fed H.4.1 / NY Fed / SIFMA / Treasury Quarterly Refunding）：
   - O/N RRP 余额
   - 银行 reserve balances
   - Fed balance sheet 总规模 + 4 周变化
   - SOFR vs IORB spread（紧张信号）
   - T-bill share of total marketable debt
2. 判断当前所处"阶段"：
   - 阶段 A（2022-2024H1）：T-bill 大发 + RRP 释放 → 隐性放水
   - 阶段 B（2024H2-2025H1）：RRP 接近耗尽 → 流动性渐紧
   - 阶段 C（2025H2 起）：QT 结束 + RMP 启动 → 隐性 QE
3. 给出"风险资产 friction"评分（1-5）
4. 如果 SOFR 跳升、RRP 抽干、SRF 放量同时出现 → 触发"压力情景"标注，提示跨月末/季末的临时操作

### Fixed reference data
- Bessent vs Yellen 偏好（短债 / 长债）注释
- 2019-09 repo crisis、2020-03 dash for cash 历史 case study
- 关键阈值（RRP < $200B、reserves < $3.0T、SOFR-IORB > 5bp）

### 价值
这是 Ray 最有"信息差感"的一类输出，但其实底层数据完全公开，只是要求把多个数据源缝起来。固化为 skill 让 Claude 每次都拼对，比临时推导稳得多。

---

## Skill 3: `nfp-establishment-vs-household`

### Description
读取 BLS 月度 Employment Situation Report，用 establishment（CES）vs household（CPS）survey 二元拆解失业率与就业增长的真实信号。识别飓风/罢工/政府停摆引起的一次性扭曲。

### Trigger keywords
"NFP" / "non-farm payroll" / "BLS" / "大非农" / "household survey" / "establishment survey" / "失业率"

### Workflow
1. 提取 6 个核心数字：
   - Headline NFP change（CES）vs consensus
   - Unemployment rate（CPS-derived）
   - Average hourly earnings YoY/MoM
   - Labor force participation
   - Full-time vs part-time（CPS）
   - Foreign-born vs native-born（CPS）
2. 二元拆解：
   - CES 强 + CPS 弱 → "兼职/移民驱动"
   - 一次性事件（飓风、罢工、政府停摆）→ 通常砸 CES 但不动失业率
   - CES 大幅修订 → 标注"修订疑虑"
3. 校验失业率算术：失业人口 / 劳动人口 → 给出未四舍五入的精确值（Ray 的"4.145% → 4.1%"小招）
4. 输出 Fed reaction 预测：
   - U-rate 跨 4.3% / 触发 Sahm rule → 50bp 概率提升
   - Headline 强但工资降速 → 鸽派（"招聘增加、不裁员"）
   - 大幅修订 → 历史上引发 Fed 50bp 紧急降息（2024-09 类比）
5. 提示下次 BLS 年度基准修正窗口（每年 9 月初）

### Fixed reference data
- 2014-至今 NFP 月度修订幅度时间序列
- 历次 BLS 年度基准修正幅度（2024-08 -818K 是 hallmark）
- Sahm rule 阈值
- 飓风影响参考：2017-Harvey、2024-Helene+Milton 案例

### 注意
- 不内化"BLS 数据是民主党造假"立场——只识别"修订风险"
- 季调黑盒提示："警惕但不武断指控"

---

## Skill 4: `fomc-statement-decoder`

### Description
解码 FOMC 决议、点阵图（SEP）、Powell 记者会的鸽鹰倾向，并预测未来 1-2 次会议路径。

### Trigger keywords
"FOMC" / "议息会议" / "Powell" / "dot plot" / "SEP" / "rate decision" / "降息 25" / "降息 50"

### Workflow
1. 抓三件事：
   - 决议本身（cut/hold/hike + size + dissent count + 谁 dissent）
   - SEP / 点阵图（仅季度会议）：median Fed funds 路径 vs 上次
   - Powell 记者会措辞
2. 措辞分级（鸽 → 鹰）：
   - "actively considering further cuts" / "well positioned to act"  → 鸽
   - "patient" / "data-dependent" → 中性
   - "Skip" → 跳过下次
   - "Hold" → 暂时不动
   - "Pause" → 不动一段时间（最鹰，2024-12 案例）
3. dissent 解读：哪一方 dissent + 其立场 → 给出未来 dissent 扩大概率
4. 与会前市场定价（Fed Funds Futures）对比 → 量化 "鹰/鸽 surprise" 的 bp 数
5. 映射资产价格：
   - 鹰派降息 → 短端起飞、长端起飞、股市跌、美元强、黄金有阻力
   - 鸽派降息 → 短端跌、长端取决于通胀预期、股市涨
   - 注意"流动性新闻"（QT 结束 / RMP 启动）经常喧宾夺主

### Fixed reference data
- Powell 历次"措辞日历"——每次会议用了哪个 keyword（2022 至今）
- 历次 dot plot 中位数与实际路径偏差
- "Fed put" 触发条件历史观察

### 注意
- Ray 提到 Nick Timiraos 是关键 leak channel——可在 skill 中加 step "如果会议前 24h 内有 Nick 文章则单独读取"

---

## Skill 5: `cpi-ppi-release-template`

### Description
读取 CPI / PPI 月度报告，按 Fed 反应函数评估对降息路径的影响。

### Trigger keywords
"CPI" / "PPI" / "通胀数据" / "core inflation" / "SuperCore" / "PCE" / "shelter inflation"

### Workflow
1. 发布前（如果触发时间 < 24h）：
   - 抓 Bloomberg consensus、Cleveland Fed Inflation Nowcast、BAML / GS / MS / JPM 个家预测
   - 标记分歧（哪家偏高 / 偏低）
   - 给出"Fed 容忍线"：核心 CPI MoM ≤ 0.3% = 鸽 / = 0.4% = 鹰
2. 发布后：
   - 拆 6 个分项：energy / food / shelter / core goods / core services / SuperCore（剔除房租的核心服务）
   - 把 CPI + PPI 翻译成核心 PCE 预估（Ray 的简易换算："核心 CPI 0.3% → 核心 PCE ≈ 0.2% → 年化 2.4%"）
   - 标记一次性扭曲：保险费、医疗、季节调整黑盒、汽油价格 vs PPI 汽油背离
3. Fed 路径影响：
   - 同比走势 + 3 个月年化 + SuperCore → 给出"是否改变下次会议预期"的二元判断
   - 量化：如果核心 CPI 0.4%，Fed Funds Futures 6 月降息概率应该从 X 跌到 Y（用历史回归经验值）

### Fixed reference data
- BLS / BEA 数据 API endpoints
- Ray 的"核心 CPI → 核心 PCE"换算系数（约 0.6-0.7x，因为权重不同）
- 各家投行历史预测准确率（BAML 在零售上准确率确实较高，但 CPI 上没那么领先）
- SuperCore 的精确定义：core services excluding shelter

---

## 不做 skill 的另外几个候选 + 理由

| 候选 | 不做的原因 |
|---|---|
| 历史类比框架（A2 在 patterns） | Claude 自带能力，做 skill 反而限制 |
| BLS 造假主题 | 单一假设带政治色彩，做 skill 会固化偏见 |
| 央行购金 / 黄金 ETF | 主题型而非框架型；Ray 直接转引投行目标价 |
| Buffett 13F 跟踪 | 一年 4 次的事件，写日历而非 skill |
| 中国宏观政策日历 | 可以做"会议日历 + 关键词分级"参考资料，但不需要单独 skill |
| 美国大选 / 玄学预测 | one-off |

---

## 下一步建议

如果用户认为这 5 个里面有 2-3 个值得真正做：
1. 优先级建议：`treasury-auction-postmortem` > `nfp-establishment-vs-household` > `fomc-statement-decoder` > `cpi-ppi-release-template` > `liquidity-plumbing-monitor`
2. 拍卖和 NFP 是 ROI 最高的，因为：(a) 频率高（拍卖每周、NFP 每月）、(b) 结构稳定 25 年没变、(c) Claude 临时推容易漏维度
3. liquidity-plumbing 价值最大但最难——需要持续维护 reference data
4. 其余三个让 Claude + WebSearch 临时干已经够好，做不做 skill 边际效益较小

如果只做 1 个，做 `treasury-auction-postmortem`。
