# Case Notes: A股 ETF 期权标的底层属性手册

- research_cutoff_date: `2026-05-26`
- primary_weight_data_as_of: `2026-05-25; 深证100采用国证指数2026年04月指数单张`
- market_scope: `CN A-share listed ETF options`
- research_object: `ETF option underlyings shown in the user's option menu`

## Framework Selection

- selected_framework: `large-mega`
- secondary_regime: `index-basket / derivatives-underlying`
- framework_basis: 这些标的不是单一公司，而是可交易 ETF 期权的底层指数篮子。大部分价格波动由指数权重、机构配置、流动性、政策预期、利率/风险偏好和行业轮动共同驱动，单票基本面只通过权重股传导。
- framework_mismatch_risk: 如果把 ETF 期权标的当成单票研究，容易高估某只成分股对整体 ETF 的解释力；如果只按宽基 Beta 理解，又会低估科创50、创业板、深证100里半导体、CPO、新能源等主题因子的主导性。

## Overlay Selection

- selected_overlays: `macro`, `supply-chain-lite`
- macro_weight: `secondary`
- dominant_macro_variable: `A股风险偏好、国内政策预期、人民币流动性、成长股贴现率`
- dominant_macro_chain: `宏观/政策预期 -> 风险偏好与贴现率 -> 指数估值倍数 -> ETF期权隐含波动率和方向性定价`
- supply_chain_lite_basis: 科创50和创业板的核心暴露不是普通行业标签，而是半导体国产替代、AI算力、CPO/光模块、新能源设备等产业链节点。完整供应链 overlay 暂不展开到单票，但在解释这些 ETF 的交易属性时必须保留。

## Source Quality Notes

- 交易所公告用于确认可交易 ETF 期权标的，证据等级最高。
- ETF.run 用于快速读取最新行业权重和前八大集中度；它是二级市场数据源，不是官方指数成分文件，所以结论中把这些权重作为 `working snapshot`。
- 深证100的 ETF.run 页面抓取不完整，本轮用国证指数 2026 年 4 月指数单张确认定位、行业权重和十大权重；其权重口径与 ETF.run 的申万一级行业口径不同，横向比较时需标注口径差异。
- 本文的“内部属性”是交易解释框架，不等同于申万一级行业的机械归类。例如创业板的“通信”权重主要映射到 CPO/光模块和 AI 硬件链，而不是传统电信运营商。

## Facts

- 上交所公告列示的 ETF 期权标的包括 `510050`、`510300`、`510500`、`588000`、`588080`。
- 深交所已上市 ETF 期权标的包括 `159919`、`159915`、`159922`、`159901`。
- `510300` 与 `159919` 跟踪同一指数方向：沪深300。
- `510500` 与 `159922` 跟踪同一指数方向：中证500。
- `588000` 与 `588080` 跟踪同一指数方向：科创50。

## Inferences

- 对期权交易者而言，同指数的沪深两地 ETF 期权，方向性风险基本一致；差异主要来自成交量、买卖价差、隐含波动率曲面、持仓结构和行权交收细节。
- 当前 ETF 期权菜单里，主题属性从强到弱大致为：科创50 > 创业板 > 深证100 > 中证500 > 沪深300 > 上证50。
- 当前 ETF 期权菜单里，半导体/硬科技纯度最高的是科创50；新能源/CPO 混合弹性最高的是创业板；传统价值和金融属性最高的是上证50。

## Open Issues

- 需要补一个自动化刷新表：每月读取六个底层指数的前十大、行业权重、估值百分位和 ETF 期权成交/持仓数据。
- 需要把期权流动性层拆出来：同一指数下，哪个 ETF 期权盘口更紧、期限结构更稳定、隐波偏度更可交易。
- 需要补“极端行情压力测试”：科创50/创业板在半导体或 CPO 单日冲击下，delta/gamma 暴露如何不同。

## Refresh Conditions

- stale_after: `2026-06-30`
- must_refresh_if:
  - 交易所新增或调整 ETF 期权标的。
  - 指数公司月度/季度权重更新后，任一底层指数前两大行业合计权重变化超过 `5pct`。
  - 科创50电子权重跌破 `60%`、创业板通信+电力设备权重合计跌破 `45%`，或深证100信息技术+电信业务+工业权重合计跌破 `50%`。
  - ETF 期权成交量/持仓量出现迁移，使同指数下沪深标的的交易优先级改变。
