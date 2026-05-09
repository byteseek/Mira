# EUV 深度分析：Corgi Lithography & Semiconductor Photonics ETF

- ticker: `EUV`
- issuer: `Corgi Strategies`
- exchange: `Cboe BZX`
- listed: `2026-05-06`
- product_type: 主动管理主题 ETF
- research_cutoff_date: `2026-05-09`
- conclusion: `confirmed high-priority exposure-watch`

## 一句话结论

`EUV` 是一个值得认真看的新 ETF。进一步核验后，持仓已经可以从 Corgi 官网前端调用的 holdings API 交叉确认，不再只是推断暴露。它的产品叙事正好卡在 AI 基础设施从 GPU / HBM 扩散到光互联、光子、EUV 光刻、计量检测的下一层瓶颈；真实持仓也确实围绕 TSM、ASML、Lam、Applied Materials、KLA、Corning、Ciena、Lumentum、Coherent、MACOM 等光刻/设备/光通信链条展开。

我的当前判断：

- 主题质量：高。
- 产品信号：高于初判。
- 持仓可信度：已通过 Corgi holdings API 初步确认。
- 发行意图：`theme-purity` + `strategic-direction`，仍夹带 Corgi 批量发行带来的 `hype-capture` 风险。
- 投资动作：从“等待持仓”升级为“确认持仓后继续跟踪主题纯度、规模和交易质量”。

## 2026-05-09 核验更新

通过 Corgi 官网前端代码可以看到，`EUV` 产品页会调用公开 API：

`https://cmltk98h4m.execute-api.us-east-2.amazonaws.com/api/v1/holdings?account=EUV&limit=1000`

该 API 返回 Corgi holdings CSV 解析结果，source file 为 `Corgi_Adv.40C8.C8_ETF_Holdings.csv`。截至本次核验，API 返回 `2026-05-06`、`2026-05-07`、`2026-05-08` 和 `2026-05-11` 四个 holding_date。注意：当前本地日期是 `2026-05-09`，所以 `2026-05-11` 更像是周五晚间已发布的下一交易日篮子/持仓文件，不应误读为已经发生的历史交易日。

最新可见 `2026-05-11` 文件：

- rows: `41`
- stock / fund holdings: `40`，另有 `Cash&Other`
- net_assets: `$2,894,518`
- shares_outstanding: `110,000`
- creation_units: `22`
- weight_sum: `100.01%`
- cash / money market: `3.18%`，主要是 `FGXXX`

前十大持仓：

| rank | ticker | weight | name | read-through |
| --- | --- | ---: | --- | --- |
| 1 | `TSM` | 10.01% | Taiwan Semiconductor Manufacturing | 先进制程 / AI 半导体基础 beta |
| 2 | `ASML` | 8.47% | ASML Holding | EUV 光刻核心 |
| 3 | `LRCX` | 5.14% | Lam Research | 晶圆设备 |
| 4 | `GLW` | 4.97% | Corning | 光学材料 / 光纤 / 显示材料 |
| 5 | `AMAT` | 4.96% | Applied Materials | 晶圆设备 |
| 6 | `KLAC` | 4.26% | KLA | 计量 / 检测 |
| 7 | `CIEN` | 4.17% | Ciena | 光网络 |
| 8 | `LITE` | 4.12% | Lumentum | 光通信 / 激光组件 |
| 9 | `COHR` | 3.57% | Coherent | 光子 / 光学材料 / 激光 |
| 10 | `MTSI` | 3.28% | MACOM Technology Solutions | RF / photonics / optical connectivity |

前十大合计约 `52.95%`。这说明 `EUV` 不是等权 ETF，也不是纯小票 basket，而是主动管理下的核心龙头 + 二阶光子/设备组合。

每日 NAV API 也能确认早期规模和交易质量：

- `2026-05-05`: net_assets `$25.47`，更像 pre-launch seed record。
- `2026-05-06`: net_assets `$529,959.75`，shares outstanding `20,000`，NAV `$26.4980`，premium/discount `-0.0309%`。
- `2026-05-07`: net_assets `$2,810,055.27`，shares outstanding `110,000`，NAV `$25.5460`，premium/discount `-0.0564%`，30-day median spread shown as `0.1500%`。

这说明上市初期 creation units 已明显扩张，但样本只有数日，不能把它写成已被市场资金长期验证。

## 已确认事实

Cboe 页面确认 `EUV` 在 2026-05-06 上市，产品名为 `Corgi Lithography & Semiconductor Photonics ETF`。Cboe 对它的描述覆盖四条链：

- 光刻系统。
- 激光与光学元件。
- 面向 AI 数据中心的硅光平台。
- 计量、检测、精密传感。

招募文件口径显示，`EUV` 是主动管理 ETF，正常情况下至少 80% 净资产投向与 photonics / light-based technologies materially involved 的公司。覆盖范围包括 EUV 光刻、光源、光学、掩膜、光刻胶、计量、检测、过程控制、激光、光学元件、PIC、光纤通信、AI 数据中心光互联、成像、传感、lidar、控制电子和 specialty materials。

Corgi 发行背景也很关键：Corgi 在 2026-05-06 同日推出 28 只主动主题 ETF，EUV 是其中一只。发行人新闻稿强调这些产品提供 single-ticker 主题暴露，并使用基本面、主题和量化筛选。这个背景提高了产品覆盖面，但也降低了单只产品的“强客户需求”确定性。

## 发行意图

### 主判断：`theme-purity`

`EUV` 最有价值的地方，是它试图把普通半导体 ETF 里混在一起的几类暴露拆出来：

- EUV 光刻和先进制程设备。
- metrology / inspection / process control。
- optical interconnect / silicon photonics。
- lasers / optics / photonic components。

持仓确认后，这个判断增强：它没有把 `NVDA / AVGO / AMD / MU` 做成主仓，而是把光互联、光学组件、检测、设备、材料和 foundry 串成一个组合。

### 次判断：`strategic-direction`

Corgi 同日推出大量主动主题 ETF，说明它的战略不是做一个单点爆款，而是快速铺一组“AI + 产业瓶颈 + 主题货架”。`EUV` 在这组产品里属于技术含量较高的一只，说明发行人至少判断 photonics / lithography 已经到了可以单独产品化的阶段。

### 风险判断：`hype-capture`

这不是传统大管理人单独打磨出来的主题 ETF，而是新发行人批量推出主题货架的一部分。好消息是，已确认持仓并不是普通半导体 mega-cap 重包；风险是 Corgi 后续能否持续维护、营销、披露和发展这个产品。

## 持仓与暴露地图

当前持仓状态：`confirmed via Corgi holdings API`。

下面是基于 `2026-05-11` holding_date 的持仓桶归类。桶分类是研究归类，不是发行人官方分类。

| bucket | confirmed tickers | weight | 为什么重要 | 纯度判断 |
| --- | --- | ---: | --- | --- |
| optical interconnect / networking | `AAOI`, `VIAV`, `POET`, `MTSI`, `MRVL`, `LWLG`, `LITE`, `CRDO`, `COHR`, `CIEN`, `ADTN` | 26.08% | AI 数据中心从电互联转向光互联的瓶颈 | 高，且比普通半导体 ETF 更有差异 |
| EUV / lithography equipment | `VECO`, `UCTT`, `LRCX`, `ASML`, `AMAT` | 21.79% | 先进制程资本开支和 EUV 生态核心 | 高，但大票价格影响有限 |
| metrology / inspection / test | `PDFS`, `ONTO`, `NVMI`, `KLAC`, `FORM`, `CAMT`, `AEHR` | 15.06% | 良率、检测、先进封装和过程控制 | 高，是 EUV 质量最高的部分之一 |
| lasers / optics / components | `TDY`, `NOVT`, `LASR`, `IPGP`, `GLW`, `FN` | 12.90% | 光源、精密制造、光学组件和代工链 | 中高 |
| foundry / semis | `TSM`, `TSEM`, `GFS` | 10.88% | 半导体制造 beta | 中，`TSM` 权重高会拉低主题纯度 |
| materials / masks / substrates | `PLAB`, `MTRN`, `ENTG`, `AXTI` | 6.63% | photomask、材料、基板和 process chemicals | 中高，权重不大但有新意 |
| lidar / sensing | `OUST`, `HSAI`, `AEVA` | 3.49% | 招募范围覆盖 sensing / lidar | 低到中，当前权重可控 |
| cash / money market | `FGXXX`, `Cash&Other` | 3.18% | 流动性管理 | 中性 |

结论：持仓纯度比初判更好。它不是简单把 `NVDA / AVGO / AMD / MU` 重包，事实上最新前十大没有这些名字。但它也不是极纯的 EUV 光刻 ETF，因为 `TSM` 是第一大持仓，且 optical networking / photonics 权重超过纯 lithography equipment。

## 管理与权重机制

`EUV` 是主动管理，权重不是指数规则自动决定。已确认的机制特征：

- 前十大约 `52.95%`，集中但未失控。
- `TSM + ASML` 合计约 `18.48%`，说明组合有龙头锚，但不是单一 ASML proxy。
- `NVDA / AVGO / AMD / MU` 不在最新可见持仓中，这是很强的主题纯度正信号。
- 持有非美/ADR 或外资标的，例如 `ASML`、`TSM`、`TSEM`、`CAMT`、`NVMI`、`HSAI`。
- 持有货币基金 `FGXXX` 约 `3.18%`，没有看到明显 ETF sleeve 稀释。
- 上市后净资产从 `2026-05-06` 的约 `$0.51M` 增至 `2026-05-07/08/11` 附近的约 `$2.8M-$2.9M`，shares outstanding 从约 `20,000` 增至 `110,000`。

## 与同类 ETF 的差异

### 对 `SMH`

`SMH` 是大市值半导体 beta。它的优势是流动性、规模和机构接受度；弱点是 mega-cap 主导。`EUV` 不是替代 `SMH`，而是补它没有表达清楚的光子/光刻/检测瓶颈。

### 对 `SOXX`

`SOXX` 比 `SMH` 更分散一些，但本质还是半导体行业 ETF，不是 photonics / lithography 主题 ETF。`EUV` 的差异来自持仓颗粒度，而不是名字。

### 对 `CHPX`

`CHPX` 已经包含 AI semiconductor / quantum 暴露，前列持仓中有 `TSM`、`ASML`、`AVGO`、`NVDA`、`INTC`、`MU` 等。`EUV` 已确认明显提高 `COHR`、`LITE`、`ONTO`、`IPGP`、`NOVT`、`PLAB` 等权重，并且没有把 `NVDA` / `AVGO` 放进前十大。因此它相对 `CHPX` 的新增研究价值成立：它更偏 optical / photonics / lithography / metrology，而不是泛 AI semiconductor。

### 对 `DRAM`

`DRAM` 是 memory/HBM 方向的集中表达，已经验证过市场愿意为 AI 二阶硬件买单。`EUV` 可以被理解为“DRAM 之后的另一条二阶硬件试验”：从 memory bottleneck 扩展到 optical / lithography / metrology bottleneck。但 `DRAM` 的成功不能直接外推给 `EUV`，因为 EUV 的持仓边界更宽，主题也更难被普通投资者理解。

## 单票 read-through

以下股票已在 Corgi 最新可见 holdings API 中确认。需要注意，EUV 当前净资产不到 `$3M`，所以“ETF 买盘”本身对大票价格影响很小；更大的价值是暴露地图和市场叙事 read-through。

优先级 A：高质量核心，但 ETF 价格影响有限

- `ASML`: EUV 光刻核心资产，权重 `8.47%`。
- `TSM`: 第一大仓，权重 `10.01%`，是先进制程 beta，也是主题纯度的双刃剑。
- `KLAC`: metrology / inspection 核心，权重 `4.26%`。
- `AMAT`, `LRCX`: 半导体设备龙头，合计约 `10.10%`。

优先级 B：更能体现 EUV 是否有新意

- `COHR`: 光学材料、激光、光通信链条，权重 `3.57%`。
- `LITE`: optical components / datacom 暴露，权重 `4.12%`。
- `ONTO`: process control / metrology，权重 `2.16%`。
- `IPGP`, `NOVT`: 激光和光子组件方向。
- `PLAB`: photomask 暴露，权重 `1.51%`。
- `MTSI`, `CRDO`, `AAOI`, `CIEN`: optical connectivity / networking 方向，是这只 ETF 和普通半导体 ETF 的主要差异来源。

优先级 C：谨慎看待

- `MRVL`: 与 AI 光互联相关，但容易把 ETF 变成普通 AI networking basket；当前权重 `2.33%`，可接受。
- `OUST`, `HSAI`, `AEVA`: lidar / sensing 属于招募范围，合计约 `3.49%`，当前没有明显稀释主线。

## 升级条件

把 `EUV` 从 `exposure-watch` 升级为 `actionable-theme`，已经满足“持仓披露确认”这一条，但还需要看到：

- 光刻、光子、metrology、optical interconnect 合计权重持续维持在高位，而不是快速漂移。
- 与 `SMH` / `SOXX` / `CHPX` 的重合度可解释，且新增暴露持续存在。
- 发行人后续持续披露、营销和维护产品，而不是批量上市后缺少跟进。
- 上市后成交和价差足够支持实盘交易。

## 降级条件

下调 `EUV` 的条件：

- 后续前十大漂移为 `NVDA`、`AVGO`、`TSM`、`AMD`、`MU`、`INTC` 这类普通半导体权重。
- `COHR`、`LITE`、`ONTO`、`IPGP`、`NOVT`、`PLAB` 等二阶标的缺席或权重很低。
- 持仓过度依赖 lidar / sensing 小票，导致主题从半导体光子漂移到高波动概念股。
- cash / money market / ETF sleeve 明显稀释主题。
- 交易价差长期偏宽，无法成为实用表达工具。

## 下一步核验清单

1. 每日拉取 Corgi holdings API，记录前十大、权重和总持仓数。
2. 计算 `SMH`、`SOXX`、`CHPX` 的 top holdings overlap。
3. 将持仓按八个 bucket 分类：optical interconnect、EUV/lithography equipment、metrology/inspection、lasers/optics、foundry/semis、materials/masks、lidar/sensing、cash。
4. 检查是否持有非美核心标的，特别是日本、欧洲光学/材料公司。
5. 5、20、60 个交易日后复盘 AUM、成交、价差和折溢价。

## 当前实战结论

`EUV` 已经从“持仓未知的新 ETF”升级为“持仓确认、主题纯度较高、但规模和交易质量仍待观察的新 ETF”。真正值得跟踪的不是 ticker 本身短期涨跌，而是它确认暴露出市场正在把 `AI 光子 / 光互联 / 光刻 / 检测` 这条二阶硬件链产品化。

如果后续持仓维持当前结构，它会成为一个很好的主题观察器；如果后续漂移成普通半导体 mega-cap basket，才应降级为 Corgi 批量主题货架里的名字型产品。

## Sources

- Cboe EUV listed product page: https://www.cboe.com/us/equities/listings/listed_products/symbols/EUV/
- Corgi launch release via PR Newswire: https://www.prnewswire.com/news-releases/corgi-launches-28-actively-managed-thematic-etfs-on-cboe-bzx-302763988.html
- Corgi ETF Trust I prospectus filing mirror: https://www.otcmarkets.com/filing/html?guid=uAv-kpdejknNB3h&id=19392954
- StockAnalysis EUV market snapshot: https://stockanalysis.com/etf/euv/
- StockAnalysis CHPX holdings snapshot: https://stockanalysis.com/etf/chpx/holdings/
- StockAnalysis SMH snapshot: https://stockanalysis.com/etf/smh/
- StockAnalysis SOXX holdings snapshot: https://stockanalysis.com/etf/soxx/holdings/
- StockAnalysis DRAM snapshot: https://stockanalysis.com/etf/dram/
- Corgi holdings API used by official site: https://cmltk98h4m.execute-api.us-east-2.amazonaws.com/api/v1/holdings?account=EUV&limit=1000
- Corgi daily NAV API used by official site: https://cmltk98h4m.execute-api.us-east-2.amazonaws.com/api/v1/daily-nav?fund_ticker=EUV&limit=50
