# AI Hardware Bottleneck Watchlist

Date: 2026-05-25

Scope: AI hardware, data-center infrastructure, semiconductor supply chain, storage, optical interconnect, PCB/ABF, power, liquid cooling, testing, and selected resource-cycle names.

This document is a watchlist and classification note, not an investment recommendation. It separates direct silicon/semiconductor exposure from broader "price increase + volume ramp + bottleneck" exposure.

## Classification Rules

- Silicon/semiconductor core: business economics are directly tied to wafer manufacturing, memory, AI chips, semiconductor equipment, EDA/IP, testing, probe cards, or semiconductor-grade optical/electrical chips.
- Semi/edge silicon: optical modules, optical components, compound semiconductor materials, power semiconductor modules, or AI connectivity components where the bottleneck is related to semiconductor or high-speed electronics but the company is not a pure silicon-chip business.
- Non-silicon bottleneck: PCB, ABF, CCL, glass fiber, copper foil, power equipment, liquid cooling, data-center electrical infrastructure, server assembly, or resources.
- "Price increase" means product pricing, contract pricing, utilization/mix uplift, or resource-cycle pricing could improve. "Volume ramp" means shipment or backlog growth could be the main driver.
- `order_linkage` should be assessed separately from `narrative_beta`: a stock can have high theme sensitivity but weak visible order linkage.
- `theme_beta` names require extra caution. Do not upgrade them to bottleneck names unless customer qualification, backlog, ASP, utilization, or shipment evidence improves.

## Event Overlay: Huawei Tau Scaling / LogicFolding

Date added: 2026-05-25

Event: Huawei announced the Tau (tau) Scaling Law at IEEE ISCAS 2026 and said it expects high-end chips based on this path to reach transistor density equivalent to 14 angstrom / 1.4 nm processes by 2031. Huawei also said its Fall 2026 Kirin chips will be the first to adopt LogicFolding.

Evidence status: official company announcement and conference keynote listing; third-party product teardown, benchmark, density verification, foundry/packaging order evidence, and independent performance validation are still pending.

Investment interpretation:

- Direct read-through: domestic AI chips, foundry, EDA/IP, semiconductor testing, probe cards, advanced packaging, semiconductor equipment, and semiconductor materials.
- Medium read-through: PCB/ABF/CCL, optical interconnect, power/HVDC, liquid cooling, and AI server integration if the architecture accelerates domestic AI hardware volume.
- Not yet proven: this is not proof that Huawei has already mass-produced 1.4 nm chips, nor proof that EUV constraints have been commercially bypassed.
- Validation points: Fall 2026 Kirin launch, third-party teardown and benchmarks, density/performance claims, foundry or OSAT capacity signals, semiconductor equipment/materials orders, and whether LogicFolding migrates from mobile chips to Ascend or other AI compute products.

Watchlist impact:

- Upgrade evidence weight for A-share semiconductor equipment/materials, EDA/IP, testing/probe cards, and advanced packaging names from "generic domestic substitution" to "domestic scaling-path validation" if order evidence appears.
- Keep most AI chip design names as `high narrative_beta / variable order_linkage` until customer deployments and gross-margin evidence improve.
- Keep PCB/ABF, optical, power, and liquid cooling in the broader AI hardware bottleneck framework rather than treating them as pure Tau Scaling beneficiaries.

## US Stocks

| 标的 | 环节 | 涨价预期/周期 | 放量预期/周期 | 瓶颈属性 | 备注 |
|---|---|---|---|---|---|
| MU, SNDK, SIMO | 存储/HBM/NAND/控制器 | 强，2026H1-H2 | 强，2026 全年 | HBM 转产、DRAM/NAND 供给、库存周期 | 存储涨价最直接；SIMO 更偏控制器放量 |
| STX, WDC | 近线 HDD/企业存储 | 强，2026H1-H2 | 中-强，2026 | 近线 HDD 产能、AI 数据湖、企业存储订单 | 非硅基，但价格和产能锁定逻辑强 |
| AVGO, MRVL, CRDO, ALAB | ASIC/交换芯片/高速互联 | 中，2026 | 强，2026-2027 | ASIC、SerDes、AEC、PCIe/CXL、AI 集群互联 | AI 网络和自研 ASIC 核心链 |
| ANET | AI Ethernet 交换机 | 中，2026 | 强，2026-2027 | Ethernet AI 集群网络、交换机架构 | 更偏放量，不是典型涨价票 |
| COHR, LITE, AAOI, AXTI, GLW, CIEN | 光模块/光器件/衬底/相干传输 | 中-强，2026 | 强，2026-2027 | 800G/1.6T、激光器、相干光、光学材料 | 光互联瓶颈链；AXTI 偏化合物半导体衬底 |
| NVTS, TXN, MPWR, VICR | 800V HVDC/电源芯片/功率半导体 | 中，2026H2 起 | 强，2026-2027 | GaN/SiC、模拟电源、功率密度、AI 机柜供电 | NVTS 弹性高；TXN/MPWR/VICR 更偏稳健电源链 |
| VRT, GEV, ETN, POWL | 数据中心电力/液冷/开关设备 | 中，2026 | 强，2026-2028 | 电力交付、开关柜、变压器、散热、燃机/电网 | AI 基建瓶颈，周期长于芯片链 |
| TER, FORM | 测试设备/探针卡 | 中，2026 | 强，2026-2027 | HBM/AI 芯片测试容量、探针卡 | 后道测试瓶颈，受 AI/HBM 复杂度提升拉动 |
| AMAT, LRCX, KLAC | 半导体设备 | 中，2026-2027 | 中-强，2026-2027 | 先进制程、存储扩产、检测量测 | 偏设备 beta，订单周期需跟踪 |
| CDNS, SNPS | EDA/IP | 弱-中，持续 | 中-强，2026-2027 | 芯片设计工具、IP、验证复杂度 | 不是涨价票，更偏长期工具链 |
| AMD, INTC | GPU/CPU/晶圆制造 | 弱-中，2026 | 中-强，2026-2027 | 算力供给、二供、制程、封装 | AMD 偏放量；INTC 偏困境反转 |
| ALB, CRML, CCJ, SCCO | 锂/铀/铜资源 | 中，周期波动 | 中，周期波动 | 资源供给、资本开支周期 | 资源品涨价，不是 AI 硅基主线 |
| RNMBY, KTOS, RKLB, ONDS, MTSI | 国防/太空/RF 光电 | 弱-中，项目周期 | 中，2026-2028 | 政府订单、产能认证、航天/无人系统 | 太空和国防新科技链 |
| DOCN, INOD | 云/数据服务 | 弱 | 中 | 软件服务、数据处理、云资源 | 非硬件瓶颈 |

## A-Share / RMB Stocks

| 标的 | 环节 | 涨价预期/周期 | 放量预期/周期 | 瓶颈属性 | 备注 |
|---|---|---|---|---|---|
| 中芯国际、海光信息、寒武纪 | 晶圆代工/国产 AI 芯片 | 弱-中，2026 | 中-强，2026-2027 | 国产算力、晶圆产能、客户验证 | 硅基核心，但涨价弹性不如存储直接 |
| 北方华创、中微公司、拓荆科技、芯源微、华海清科、盛美上海、中科飞测 | 半导体设备/检测量测 | 中，2026-2027 | 中-强，2026-2028 | 刻蚀、薄膜沉积、清洗、CMP、涂胶显影、检测量测 | 韬定律事件强化国产设备叙事；订单、国产线导入和先进封装扩产是关键验证 |
| 南大光电、安集科技、雅克科技、沪硅产业、华特气体、金宏气体 | 半导体材料 | 中，2026-2027 | 中，2026-2028 | 光刻胶/前驱体、CMP材料、电子特气、硅片、封装材料 | 材料弹性取决于国产制程扩产和客户认证，不宜只按概念交易 |
| 华大九天、概伦电子、广立微、芯原股份 | EDA/IP/设计基础设施 | 弱-中，持续 | 中，2026-2028 | EDA、验证、良率分析、IP授权、设计服务 | 与软件/架构/芯片协同更相关；不是典型涨价票，偏长期国产替代 |
| 长电科技、通富微电、华天科技、甬矽电子、颀中科技、利扬芯片 | 封测/先进封装/测试服务 | 中，2026 | 中-强，2026-2027 | Chiplet、SiP、先进封装、封测产能、测试服务 | 后摩尔和AI芯片复杂度提升的直接链条；需跟踪高端封装占比和客户结构 |
| 江波龙、兆易创新、北京君正、东芯股份、普冉股份、聚辰股份、佰维存储、德明利、香农芯创 | 存储/模组/利基存储/分销 | 强，2026H1-H2 | 中-强，2026 | DRAM/NAND 涨价、库存重估、模组需求、利基存储周期 | A股存储涨价弹性；多数不是纯HBM，不应等同于三星/SK海力士主线 |
| 长川科技、华峰测控、矽电股份、燕麦科技 | 测试设备/探针卡 | 中，2026 | 强，2026-2027 | 测试平台、探针卡、国产替代 | HBM/AI 芯片后道瓶颈 |
| 中际旭创、新易盛、天孚通信、源杰科技、光迅科技、剑桥科技、华工科技 | 光模块/光器件/激光芯片 | 中-强，2026 | 强，2026-2027 | 800G/1.6T、激光器、光器件 | 光互联主线；源杰科技偏 InP |
| 长飞光纤、亨通光电、中天科技 | 光纤/线缆/连接 | 中，2026 | 中，2026-2027 | 光纤、线缆、数据中心连接 | 偏材料和网络基础设施 |
| 胜宏科技、沪电股份、生益科技、兴森科技、鼎泰高科、宏和科技、东材科技 | PCB/ABF/CCL/玻纤/钻针 | 强，2026H1-H2 | 强，2026-2027 | 高层 PCB、ABF、T-glass、低介损材料、钻针 | A股硬件瓶颈最强一组 |
| 铜冠铜箔、德福科技、中钨高新 | 铜箔/钨/钻针材料 | 中，2026 | 中，2026-2027 | 高端铜箔、钨耗材、PCB 加工耗材 | 资源和制造耗材复合逻辑 |
| 三环集团、风华高科 | MLCC/被动元件 | 中，2026 | 中-强，2026-2027 | 高规格 MLCC、AI server 规格升级 | 规格升级比总量更重要 |
| 英维克、同飞股份、申菱环境、高澜股份、领益智造、东阳光 | 液冷/温控/冷却液/部件 | 中，2026 | 强，2026-2027 | 液冷渗透、冷板、分水器、冷却液 | 东阳光具体供应关系需要持续验证 |
| 麦格米特、欧陆通 | 电源/HVDC/服务器电源 | 中，2026H2 起 | 强，2026-2027 | 高压直流、电源密度、服务器电源 | 800V/HVDC 国产链 |
| 工业富联、浪潮信息、紫光股份、中兴通讯 | AI server/网络/通信设备 | 弱-中，2026 | 强，2026-2027 | 整机交付、供应链整合、算力网络 | 放量强，毛利率通常较薄 |
| 洛阳钼业、紫金矿业、灵宝黄金 | 铜/钴/金 | 中，周期波动 | 中，周期波动 | 资源供给、矿山扩产、金属价格 | 资源涨价，不是硅基 |
| 赣锋锂业、石大胜华、鹏辉能源、湖南裕能 | 锂/电解液/电池/磷酸铁锂 | 中，周期波动 | 中，周期波动 | 电池材料库存周期、价格周期 | 独立于 AI 硬件主线 |
| 电科蓝天、航天环宇 | 航天/军工 | 弱-中，项目周期 | 中，2026-2028 | 军工订单、型号放量、卫星/航天设备 | 太空链 |

## Global Ex-US Stocks

| 标的 | 环节 | 涨价预期/周期 | 放量预期/周期 | 瓶颈属性 | 备注 |
|---|---|---|---|---|---|
| 台积电 / TSM | 先进制程/CoWoS | 中，2026-2027 | 强，2026-2028 | 先进制程、先进封装产能、客户排产 | AI 基础设施核心 |
| 三星电子、SK 海力士 | DRAM/NAND/HBM | 强，2026H1-H2 | 强，2026-2027 | HBM 产能、良率、客户认证、DRAM/NAND 供给 | 全球存储核心 |
| Advantest、京元电子 | 半导体测试 | 中，2026 | 强，2026-2027 | AI/HBM 测试容量、ATE、外包测试 | Advantest 更纯；京元电子偏台系测试链 |
| Disco、Tokyo Electron、ASML、ASM International、BESI | 半导体设备/先进封装 | 中，2026-2027 | 强，2026-2028 | EUV、ALD、切割研磨、hybrid bonding、先进封装设备 | 先进制程和封装瓶颈 |
| Alchip、GUC | ASIC 设计服务 | 中，2026 | 强，2026-2027 | CSP 自研 ASIC、台积电生态、设计服务产能 | 高弹性但订单集中度需要跟踪 |
| ASE 日月光 | 封测 | 中，2026 | 中-强，2026-2027 | 先进封装、SiP、封测产能 | 偏封测龙头 |
| 台达电、鸿海/富士康 | 电源/液冷/AI server 代工 | 中，2026 | 强，2026-2027 | 电源、散热、整机交付、客户认证 | 台达偏电力散热；鸿海偏整机 |
| 欣兴电子、揖斐电、味之素 | ABF/IC 载板/ABF 膜 | 强，2026H1-H2 | 强，2026-2027 | ABF 材料、高端载板、封装基板供给 | 全球载板瓶颈核心 |
| 村田制作所 | MLCC | 中，2026 | 中-强，2026-2027 | 高规格被动元件、AI server 规格升级 | 全球 MLCC 龙头 |
| 三井、古河、住友、精工细研 | 铜箔/光纤/材料/光学部件 | 中，2026 | 中，2026-2027 | 高端铜箔、光纤、电缆、光学部件 | 偏材料链 |
| Schneider Electric、ABB、Siemens Energy、Hitachi | 配电/电网/变压器/电气设备 | 中，2026 | 强，2026-2028 | 电力接入、变压器、开关设备、燃机/电网 | AI 数据中心电力瓶颈 |
| 新意网集团 | IDC/数据中心 | 弱-中，2026 | 中，2026-2027 | 数据中心资源、租约、电力接入 | 偏资产端 |
| SpaceX | 航天/卫星 | 弱-中，项目周期 | 中-强，2026-2028 | 发射、卫星网络、政府/商业订单 | 非上市，适合跟踪不适合普通股票池 |

## Priority Tracking Baskets

| 主线 | 优先观察 |
|---|---|
| 存储涨价 | MU, SNDK, 三星电子, SK 海力士, 江波龙, STX, WDC |
| 光互联 | AVGO, MRVL, CRDO, ALAB, COHR, LITE, 中际旭创, 新易盛, 天孚通信, 源杰科技 |
| PCB/ABF/材料 | 生益科技, 沪电股份, 胜宏科技, 兴森科技, 欣兴电子, 味之素, 揖斐电, 宏和科技 |
| 国产半导体设备/材料 | 北方华创, 中微公司, 拓荆科技, 芯源微, 华海清科, 盛美上海, 中科飞测, 南大光电, 安集科技, 雅克科技 |
| 先进封装/封测 | 长电科技, 通富微电, 华天科技, 甬矽电子, 颀中科技, 利扬芯片, ASE 日月光, BESI |
| EDA/IP/设计基础设施 | CDNS, SNPS, 华大九天, 概伦电子, 广立微, 芯原股份 |
| 800V/HVDC/电源 | NVTS, TXN, MPWR, VICR, VRT, 台达电, 麦格米特, 欧陆通 |
| 电力瓶颈 | GEV, ETN, POWL, Schneider Electric, ABB, Siemens Energy, Hitachi |
| 测试/设备 | TER, FORM, Advantest, Disco, AMAT, LRCX, KLAC, 长川科技, 华峰测控, 矽电股份 |

## A-Share Evidence Ranking Heuristic

Use this overlay when reviewing domestic names after major policy, Huawei, or domestic semiconductor news.

| Rank | Evidence profile | Typical names / segments | Action |
|---|---|---|---|
| A | Visible bottleneck plus price or backlog evidence | PCB/ABF/CCL, optical modules, testing/probe cards, selected equipment | Keep in priority basket; refresh ASP, utilization, backlog, and customer certification |
| B | Strong volume path but margin/pass-through uncertain | AI servers, network equipment, liquid cooling, power supplies | Track orders and gross margin; avoid assuming revenue growth equals EPS leverage |
| C | Strategic substitution with long validation cycle | EDA/IP, semiconductor materials, advanced equipment | Track customer adoption, tender wins, process-node penetration, and revenue mix |
| D | High narrative beta but weak order evidence | Broad Huawei concept, generic chip design, loosely related suppliers | Keep as theme-beta watch only; require evidence before upgrading |

## Current Working Conclusions

1. The strongest "price increase + volume ramp + bottleneck" overlap is in memory/HBM, HDD enterprise storage, ABF/PCB/T-glass, optical interconnect, 800V/HVDC power, power equipment, and AI/HBM testing.
2. The purest silicon/semiconductor exposure is in foundry, memory, semiconductor equipment, testing/probe cards, EDA/IP, ASIC/connectivity chips, and AI processors.
3. Huawei Tau Scaling / LogicFolding raises the narrative value of domestic semiconductor equipment, materials, EDA/IP, testing, and advanced packaging, but it remains an event overlay until product-level validation and order evidence appear.
4. Liquid cooling and electrical infrastructure have a longer cycle than memory or optical modules. Their thesis should be refreshed with backlog, customer certification, and data-center power-availability evidence rather than only product announcements.
5. Resource names can work as price-upcycle trades, but they should be tracked separately from AI hardware bottleneck trades.

## Source Notes

The watchlist classification is based on public company disclosures and public market/industry commentary available through 2026-05-25, including:

- Navitas and NVIDIA 800V HVDC collaboration announcements.
- Texas Instruments 800VDC AI data-center power architecture announcement.
- TrendForce commentary on DRAM/NAND pricing, AI server demand, optical modules, PCB materials, and liquid cooling.
- Goldman Sachs public research commentary on optical networking as an AI infrastructure trend.
- Publicly available institutional commentary from Barclays, Morningstar, JPMorgan/BofA-related summaries, and company investor materials where available.
- Huawei's 2026-05-25 Tau Scaling / LogicFolding announcement and IEEE ISCAS 2026 keynote listing. Treat this as event evidence, not independent product validation.

## Refresh Policy

stale_after: 2026-06-30

must_refresh_if:

- NVIDIA Rubin/GB300/800V HVDC shipment timing changes.
- CSP capex guidance is cut or pushed out.
- DRAM/NAND/HBM contract pricing turns down.
- 800G/1.6T optical module customer orders are cut or ASP pressure accelerates.
- PCB/ABF/T-glass supply expands faster than expected.
- Data-center electrical equipment backlog, lead time, or pricing weakens.
- Huawei Fall 2026 Kirin LogicFolding product claims are confirmed, delayed, or contradicted by third-party teardown/benchmark evidence.
- Domestic semiconductor equipment, EDA/IP, materials, or advanced packaging names disclose order acceleration, customer qualification, or revenue mix changes tied to domestic AI chips.
- Company-specific customer certification, qualification, or exclusive-supply claims are confirmed or disproven.
