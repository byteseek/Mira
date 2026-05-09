# ABF Industry Map

- concept_name: ABF
- research_question: ABF 产业链的概念边界、供需瓶颈、定价/放量机制、利润池和候选标的
- market_scope: global / Japan / Taiwan / Austria-Malaysia
- research_cutoff_date: 2026-05-09
- thesis_horizon: 12-36 months
- depth: standard
- focus: supply_shortage / pricing_power / volume_ramp / stock_mapping
- stale_after: 2026-08-09, or earlier if major substrate suppliers update capacity, capex, LTAs, utilization, or AI server demand outlook

## One-Page Industry Map

### One-Sentence Definition

ABF 是高性能 CPU/GPU/ASIC 用 FC-BGA 载板里的关键层间绝缘薄膜和材料体系，不是普通 PCB 概念。

### Current Judgment

高端 AI ABF 结构性 tight，普通载板不一定 tight。市场真正要研究的是“大尺寸、高层数、高良率、已通过客户认证”的 ABF substrate 产能，而不是所有 PCB/IC substrate。

### Where It Is Tight

- tight: Ajinomoto ABF film、高端 AI ABF substrate、SAP/微细线路产能、大尺寸高层数良率、低 CTE 玻纤布/高端 CCL 等材料。
- not necessarily tight: 普通 ABF、BT substrate、消费电子/PC 相关低端载板、未进入核心 AI 客户平台的新产能。

### Best Economic Layers

1. `ABF film`: Ajinomoto 事实标准，理论定价权最高。
2. `High-end ABF substrate`: Ibiden / Unimicron / Nan Ya / Kinsus / AT&S，股票弹性更直接。
3. `Selected upstream materials`: 低 CTE 玻纤布、铜箔、CCL、树脂，能观察紧张但纯度较低。

### Best Stock Proxies

- `稳健核心`: Ajinomoto, Ibiden。
- `AI ABF 弹性`: Unimicron, Nan Ya PCB, Kinsus。
- `项目爬坡`: AT&S Kulim。
- `间接材料`: Nan Ya Plastics, Nitto Boseki, Panasonic materials。

### Core Formula

需求大致等于：

`AI GPU/ASIC/server chip 出货量 × 单颗 substrate 面积 × ABF 层数 × 高速 networking/CPU 附加需求`

供给大致等于：

`ABF film 可用产能 × 高端载板 SAP capacity × 客户认证通过率 × 良率 × 设备/材料交付`

### Key Debate

2026-2027 是 AI high-end ABF 持续紧缺并带来量价弹性，还是 2027+ 扩产、客户平台变化或 AI server 拉货放缓后，紧缺变成普通周期修复。

### What To Monitor

- Ajinomoto ABF capacity、客户认证、ICT/functional materials 利润。
- Ibiden Ono/Gama ramp、AI server substrate demand vs capacity、customer advances。
- Unimicron / Nan Ya / Kinsus 月营收、毛利率、capex、LTA、AI substrate mix。
- AT&S Kulim utilization、良率、客户拉货、现金流。
- NVIDIA / AMD / Google / AWS ASIC 平台出货节奏。
- CoWoS、HBM、低 CTE 玻纤布、高端 CCL、铜箔紧张度。

### Falsification

- AI server / GPU / ASIC 拉货显著放缓。
- 高端 ABF substrate 新产能通过认证并快速释放，供需转松。
- ABF film 或上游材料扩产快于需求，价格无法维持。
- 载板厂收入增长但毛利率不改善，说明利润被客户或成本吃掉。
- 玻璃基板等替代路线提前获得量产级客户认证。

## Full Diligence

### Core Conclusion

ABF 的核心不是“又一个 PCB 材料概念”，而是高性能 CPU/GPU/ASIC 用 FC-BGA 载板的关键层间绝缘薄膜。它位于先进封装和高端 IC 载板之间，是把纳米级芯片 I/O 接到毫米级系统板连接的材料基础。

当前产业链的强弱排序大致是：

1. `Ajinomoto ABF film`: 近似单一标准材料，议价权最高，但公司倾向长期客户关系和稳定供应，未必主动激进提价。
2. `高端 ABF 载板制造`: AI GPU/ASIC/server networking 拉动大尺寸、高层数、SAP 能力，供给最紧，Ibiden/Unimicron/Nan Ya/Kinsus/AT&S 是主要股票映射。
3. `上游玻纤布/铜箔/CCL/树脂`: 随 AI server 需求转紧，有价格传导，但产品差异和议价权低于 ABF film 和高端载板。
4. `普通 ABF/BT/消费电子载板`: 周期性更强，不等同于 AI 高端 ABF 载板，容易被主题误伤或误买。

产业判断：ABF 不是全行业普遍短缺，而是“高端 AI 载板链条结构性紧”。紧的是大尺寸、高层数、高良率、客户认证后可量产的载板能力，以及部分上游低 CTE 玻纤布等关键材料。普通 PC/消费电子需求仍可能弱于 AI 叙事。

### Concept Boundary

#### Plain-Language Definition

ABF 是 Ajinomoto Build-up Film 的简称，是味之素开发的半导体封装载板用薄膜状绝缘材料。它用于高性能处理器的 build-up substrate 层间绝缘，让复杂铜线路能在封装基板里稳定堆叠。

#### Technical Definition

ABF 是由有机环氧树脂、固化剂和无机微粒填料组成的热固性薄膜，具备低热膨胀、耐久、可激光加工、可直接铜电镀等特性，用于 FC-BGA / 高端 IC package substrate 的 build-up layers。

#### Adjacent Concepts

- `ABF film`: 味之素的绝缘薄膜材料，产业链最上游的关键材料。
- `ABF substrate`: 使用 ABF film 制造的高端封装载板，通常指 FC-BGA / 高性能 IC package substrate。
- `FC-BGA`: 一种高端倒装芯片封装载板形式，ABF 是其中常用 build-up 绝缘材料。
- `BT substrate`: 更偏移动、消费和相对低端封装的树脂载板体系，不能和高端 ABF 载板混同。
- `advanced packaging`: 更大的系统概念，包含 CoWoS、2.5D/3D、interposer、substrate、underfill、HBM 等，ABF 只是其中一段。

#### What It Is Not

- ABF 不是所有 PCB。
- ABF 不是所有 IC 载板。
- ABF 不是 CoWoS 本身。
- ABF 不是 HBM，也不是 GPU 芯片。
- ABF 不是“只要 AI server 增长就全部载板公司一起涨”的单一 beta。

#### Why It Matters Now

AI GPU、ASIC、server CPU 和高速网络芯片正在变大、I/O 增多、功耗变高，封装载板面积和层数提升。味之素在 ASV Report 2025 中展示的路线图显示，AI 半导体相对现有半导体可能从 ABF 3 层走向 ABF 9 层、板面积指数从 1 到 3.5，ABF 用量可能显著增加。TrendForce 也指出 AI 竞争正在向 3nm/2nm、先进封装、基板、材料等环节扩散。

### Value Chain Map

| Layer | Function | Representative companies | Supply state | Key bottleneck |
| --- | --- | --- | --- | --- |
| ABF film | 层间绝缘薄膜，决定高端载板可加工性和可靠性 | Ajinomoto / Ajinomoto Fine-Techno | 高集中，事实标准 | 客户认证、配方迭代、稳定供货、产能扩张节奏 |
| Upstream electronic materials | 玻纤布、铜箔、CCL、树脂、化学品 | Nan Ya Plastics, Nitto Boseki, Panasonic materials, Mitsubishi Gas Chemical, Resonac 等 | 部分材料趋紧 | 低 CTE 玻纤布、高端 CCL、铜价和良率 |
| ABF substrate fabrication | 把 ABF film 加工成高端 FC-BGA / IC package substrate | Ibiden, Unimicron, Nan Ya PCB, Kinsus, Shinko, AT&S, Kyocera | 高端 AI 规格紧，普通规格分化 | SAP 产能、大尺寸/高层数能力、良率、客户认证、设备交期 |
| Advanced packaging / OSAT / foundry integration | 与 CoWoS/2.5D/OSAT/晶圆厂封装流程配合 | TSMC, ASE, Amkor, Intel, Samsung 等 | AI 先进封装整体紧 | CoWoS/2.5D 产能、HBM 集成、良率 |
| Chip customers | CPU/GPU/ASIC/Networking chip | NVIDIA, AMD, Intel, Broadcom, Marvell, Google TPU, AWS Trainium, Apple 等 | AI 高端需求强 | 新平台节奏、封装规格、客户 LTA |
| End demand | AI server、HPC、数据中心、高速网络、PC/游戏/车载 | CSPs, OEM/ODM, server integrators | AI 强，PC/general server 分化 | CSP capex、AI inference monetization、库存周期 |

### Demand Map

需求核心来自四条线：

1. `AI GPU`: NVIDIA Blackwell / Rubin、AMD MI 系列等，封装面积、层数、功耗和 I/O 拉高 ABF substrate 规格。
2. `Custom ASIC`: Google TPU、AWS Trainium、Meta/Microsoft 等自研 ASIC 增长，带来非 NVIDIA 需求分散化。
3. `Server CPU / general server`: PC 和通用 server 需求复苏较慢，但 CPU 仍是 ABF 传统基本盘。
4. `Networking / switch ASIC`: AI cluster 对高速交换和网络芯片需求提升，拉动高端载板。

2026 年需求端的关键变量不是“AI server 出货量”一个数，而是：

- GPU / ASIC 出货结构
- 单颗芯片 substrate 面积
- ABF 层数
- server networking 芯片拉货
- CSP capex 是否持续
- NVIDIA/AMD/ASIC 平台是否延迟

### Supply Map

供给分成两段：

1. `ABF film`: Ajinomoto 是事实标准材料供应商，正在扩产。其 FY24Q4 presentation 显示 Gunma 新 ABF varnish facility 已于 2025 年 3 月完工，目标 FY2025 内客户认证后全面运行，并计划到 2030 年继续投入约 250 亿日元应对 ABF 需求增长。
2. `ABF substrate`: 真正紧张的是高端载板加工能力。Ibiden 2026 年 2 月公告未来三年 electronics business 资本开支约 5000 亿日元，并先投约 2200 亿日元扩高性能 IC package substrates；Ono Plant 自 2025 年开始逐步量产，主要用于 AI server 和 networking。AT&S Kulim 于 2025 年开始 HVM，面向 AMD data center processors 和其他客户。

### Pricing Mechanics

| Layer | Pricing logic | Current read |
| --- | --- | --- |
| ABF film | 高客户认证壁垒 + 近似单一标准 + 低 BOM 占比，但长期客户关系抑制激进涨价 | 定价权最高，但提价是否兑现取决于 Ajinomoto 策略和客户接受度 |
| High-end ABF substrate | 大尺寸/高层数/高良率稀缺，客户可用预付款、LTA、专线支持产能 | 最有实际利润弹性的环节之一，尤其是 AI GPU/ASIC 规格 |
| Upstream materials | 铜价、玻纤布、CCL、树脂供需和成本传导 | 有价格上涨，但更多是成本/供需传导，不一定有长期超额利润 |
| OSAT/foundry packaging | 先进封装产能紧张，价格由产能、客户优先级和平台认证决定 | 与 ABF 联动，但不是 ABF 纯标的 |

谁能提价：Ajinomoto 理论上最强；高端载板厂在 AI 规格上有较强议价；上游材料有周期性提价。  
谁可能被压价：普通载板、低端 PCB/BT、未进入核心客户平台的二三线厂。  
谁只是放量：新进载板产能如果良率和客户认证不足，容易有收入增长但利润率不确定。

### Volume Mechanics

ABF 的放量不是线性扩产，核心限制是：

- 客户认证周期
- 载板厂良率爬坡
- SAP 和微细线路能力
- 大尺寸基板 warpage / reliability
- 设备交期
- 高端玻纤布、铜箔、CCL 等材料供应
- 客户平台换代节奏

Ibiden 的 Q3 FY2025 Q&A 明确提到 AI server IC package substrate demand continues to exceed capacity，并预计如果多层化和大尺寸继续推进，能够处理 cutting-edge products 的 SAP capacity 会短缺。

### Tightness And Profit-Pool Ranking

| Layer | supply_demand_tightness | pricing_power | volume_visibility | margin_capture | stock_proxy_quality |
| --- | --- | --- | --- | --- | --- |
| Ajinomoto ABF film | shortage / tight | high | high | high | strong, but ABF is inside diversified Ajinomoto |
| Ibiden high-end AI substrate | shortage | high | high | high | strong |
| Unimicron / Nan Ya / Kinsus high-end substrate | tight | medium-high | medium-high | medium-high | strong but execution/customer mix matters |
| AT&S high-end substrate | tight | medium-high | medium | medium | usable, ramp and balance sheet matter |
| Low-CTE glass fabric / CCL / copper foil | tight in selected grades | medium | medium | medium | usable, less pure |
| Ordinary ABF/BT/consumer substrate | balanced / loose | low-medium | medium | low-medium | weak for AI ABF thesis |

### Institutional + Practical + First-Principles Check

#### Institutional Lens

机构视角会把 ABF 看成 AI 算力资本开支的“二阶弹性”：

- AI server / GPU / ASIC unit growth
- substrate area and layer count increase
- high-end substrate capacity utilization
- capex-backed LTAs and customer prepayments
- supplier gross margin recovery from 2023-2024 downturn
- valuation rerating risk after market starts pricing scarcity

#### Operator Lens

产业实践者视角更关注认证、良率和交付：

- 客户不会轻易换 ABF film 或高端 substrate supplier
- 新产能不是装机就能卖，要过客户认证和良率爬坡
- 大尺寸/高层数基板会放大 warpage、via reliability、良率和设备瓶颈
- 载板厂能否拿到客户预付款/LTA 比单纯 capex 更重要

#### First-Principles Lens

第一性原理上，ABF 需求增长来自 I/O 和封装面积的物理增长，而不是“AI 叙事”本身。芯片越大、带宽越高、供电越复杂，substrate 需要更大面积、更高层数、更细线路和更高可靠性。真正稀缺的不是普通产能，而是能稳定生产这类规格的材料 + 工艺 + 认证组合。

#### Conflicts To Resolve

- Ajinomoto 是否会大幅提价：理论定价权强，但公司可能更重视长期客户关系。
- 载板是否全面短缺：普通载板未必短缺，高端 AI 规格更紧。
- 新进入者能否快速放量：capex 公告不等于客户认证，不等于良率，不等于利润。

### Company Shortlist

优先研究顺序：

1. Ajinomoto (2802 JP): ABF film 事实标准，最上游关键材料，但公司是多元化食品/氨基科学集团，ABF 纯度不高。
2. Ibiden (4062 JP): 高端 AI server substrate 核心供应商，订单/客户/产能可见度强。
3. Unimicron (3037 TW): 台湾 ABF substrate 龙头，AI GPU/ASIC/CoWoS 相关需求映射强。
4. Nan Ya PCB (8046 TW): AI server、ASIC、高速 switch substrate 映射，同时可受益于集团上游材料。
5. Kinsus (3189 TW): 高端 ABF 弹性标的，进入核心客户/平台的验证需要持续跟踪。
6. AT&S (ATS AV): Kulim 高端 substrate 产能进入 HVM，AMD data center processor 相关，但财务杠杆和爬坡执行要重点看。
7. Shinko Electric / Kyocera: 日本高端封装和 substrate 相关供应商，映射较间接或需看细分产品披露。
8. Nan Ya Plastics (1303 TW), Nitto Boseki, Panasonic materials: 上游材料和电子材料链条，纯度较低但能观察材料紧张。

### Stock Research Handoff

#### Ajinomoto

- why: ABF film 源头，近似单一标准。
- driver: ABF 用量增长、产能扩张、潜在提价。
- risk: ABF 在集团收入/利润中不是全部；客户关系可能压制提价；市场已重估。
- falsification: ABF 产能快速宽松且价格无法提升，或客户转向替代材料。

#### Ibiden

- why: AI server high-end IC package substrates 供给紧张的直接受益者。
- driver: Ono/Gama 产能、SAP 能力、客户预付款/LTA、AI server substrate demand exceeding capacity。
- risk: capex 强度、良率爬坡、客户集中、PC/general server 弱。
- falsification: AI server 订单下修或新产能无法获得客户认证/良率。

#### Unimicron / Nan Ya / Kinsus

- why: 台湾 ABF substrate 主线标的。
- driver: AI GPU/ASIC/networking substrate 出货、产品 mix、价格和稼动率。
- risk: 普通载板周期、客户平台份额、扩产导致 2027+ 竞争加剧。
- falsification: 高端 ABF 订单无法兑现到毛利率，或只是低端出货修复。

#### AT&S

- why: Kulim HVM 是新增高端 substrate capacity 的重要观察点，客户包括 AMD data center processors。
- driver: Kulim ramp, customer qualification, utilization.
- risk: 大型项目资本开支、折旧、爬坡期亏损、融资压力。
- falsification: Kulim 稼动和良率低于预期，客户拉货延后。

### Monitoring Dashboard

必须跟踪：

- Ajinomoto ABF capacity / customer authorization / ICT segment profit
- Ibiden AI server substrate utilization, Ono/Gama ramp, capex, customer advance payments
- Unimicron / Nan Ya / Kinsus monthly revenue, gross margin, capex, LTA, customer mix
- AT&S Kulim HVM progress and utilization
- TrendForce / TPCA / Prismark on AI server, ABF substrate, package substrate market
- NVIDIA / AMD / Google / AWS ASIC platform shipment timing
- CoWoS / HBM / T-glass / CCL / copper foil tightness
- substrate area/layer count changes in Blackwell, Rubin, TPU, Trainium, networking ASICs

### Open Questions

- Ajinomoto 是否会在 2026-2028 主动提高 ABF film ASP，还是继续偏稳定供货？
- Ibiden “70-80% share” 指的是其特定 AI server customer/program，还是更广义的高端 AI substrate 市场份额？
- 台湾 ABF substrate 厂的 AI revenue mix、良率和客户份额分别是多少？
- 2027-2028 扩产后，紧缺是否从材料/载板转向其他环节？
- 玻璃基板是否会在 2030 后替代部分 ABF organic substrate，还是先作为补充路线？

### Must Refresh If

- Ajinomoto 更新 ABF capacity/pricing strategy
- Ibiden FY2026 full-year results and FY2027 guidance released
- Unimicron/Nan Ya/Kinsus 公布新 LTA、capex 或月营收显著拐点
- NVIDIA Rubin / AMD MI / Google TPU / AWS Trainium 出货节奏改变
- TrendForce/Prismark/TPCA 更新 ABF substrate supply-demand
- 玻璃基板获得量产级客户认证
