# NVTS Supply Chain Position Note

- company: Navitas Semiconductor
- ticker: NVTS
- analysis_cutoff_date: 2026-05-29
- research_mode: single_equity supply-chain overlay
- selected_framework: micro-small with narrative_and_revision secondary regime
- selected_overlays: supply-chain, strategic-catalyst
- stale_after: 2026Q2 earnings or next material customer / NVIDIA 800 VDC ecosystem update

## Routing

NVTS is best analyzed as an early-scale power semiconductor supplier with a strategic-catalyst overlay from NVIDIA's 800 VDC AI factory architecture. The main question is not whether 800 VDC power distribution has a logical role; NVIDIA, Infineon, TI, ST, ROHM, and Navitas all provide evidence that the architecture is being actively developed. The harder question is whether NVTS captures durable share in that architecture rather than becoming one qualified vendor among many.

## Chain Position

NVTS sits in the power conversion semiconductor layer, not in GPUs, servers, data-center construction, or final power-supply system assembly.

The chain is:

1. Grid / utility connection and facility-level power equipment.
2. Transformers, rectifiers, solid-state transformer concepts, busways, protection and energy-storage components.
3. Power semiconductor devices and ICs: Si, SiC, GaN, drivers, controllers, protection.
4. Power modules, PSUs, bus converters, DC/DC boards, and rack power shelves.
5. AI racks and compute trays using NVIDIA or other accelerator platforms.

NVTS's claimed position is "grid to GPU" wide-bandgap semiconductor coverage: high-voltage SiC for higher-voltage AC/DC or 800 VDC-related conversion, 650 V GaN for high-power conversion stages, and 100 V GaN for lower-voltage DC/DC stages closer to GPU power boards.

## Upstream Map

- Manufacturing model: fabless / outsourced manufacturing, which reduces capex burden but leaves scaling, process control, packaging, and supply assurance dependent on partners.
- Key material / process dependencies: GaN-on-Si process capability for lower-voltage GaN, SiC device technology and wafer availability for high-voltage power, advanced packaging and thermal designs.
- Scaling signal: Navitas disclosed that its 100 V GaN FETs are fabricated on a 200 mm GaN-on-Si process through a strategic partnership with Powerchip.

## Downstream Map

- Immediate customers are likely power-supply makers, power module makers, ODMs, server/rack power ecosystem participants, and distributors, not only NVIDIA directly.
- End-market pull comes from AI data centers, grid/energy infrastructure, performance computing, and industrial electrification.
- NVIDIA is a strategic architecture validator, but public disclosures show a broad ecosystem, not a single-supplier architecture.

## Same-Layer Peer Map

| company | role vs NVTS | implication |
| --- | --- | --- |
| Infineon | broad grid-to-core power portfolio across Si, SiC, GaN | strongest scale and system-know-how competitor |
| Texas Instruments | complete 800 VDC reference designs with analog/control depth | competes in integrated architecture and power management |
| STMicroelectronics | 800 VDC delivery boards using SiC/GaN and NVIDIA validation | direct proof that board-level alternatives exist |
| ROHM | SiC/GaN power devices for 800 V HVDC architecture | direct SiC/GaN substitute set |
| onsemi / Renesas / MPS / ADI / Innoscience | named NVIDIA silicon ecosystem participants | reduces exclusivity value of NVTS selection |
| Power Integrations | high-voltage power conversion and GaN read-through | validates demand backdrop but has stronger profitability |

## What Is Differentiated

NVTS has a clean pure-play identity around wide-bandgap power, and it owns both GaN and SiC product families after adding GeneSiC. That matters because 800 VDC AI power is not a single-device problem. It needs high-voltage, high-density, thermally robust conversion across multiple stages. NVTS also has useful narrative clarity: GaNFast / GaNSafe for fast, protected GaN switching and GeneSiC for high-voltage/high-reliability SiC.

The strongest company-specific evidence is that NVIDIA-related disclosures mention Navitas in the 800 VDC architecture context and NVTS has demonstrated specific AI data-center power designs, including 8.5 kW, 12 kW, and 20 kW-class boards. This places NVTS in the qualified-technology discussion.

## What Is Replaceable

NVTS is not irreplaceable at the system level. NVIDIA's own ecosystem materials list multiple silicon providers, including Infineon, Innoscience, MPS, Navitas, onsemi, Renesas, ROHM, STMicroelectronics, Texas Instruments, Analog Devices, and others. Infineon, TI, ST, and ROHM all publicly position their own SiC/GaN or complete power solutions for the same 800 VDC transition.

The likely replacement paths are:

- SiC device substitution: Infineon, ROHM, ST, onsemi, Wolfspeed-like SiC suppliers.
- GaN device substitution: TI, ST, Infineon, Innoscience, Power Integrations, ROHM, and others.
- Architecture substitution: 800 V to 54 V / 12 V / 6 V conversion topology choices can change which voltage class and device family wins.
- System integrator substitution: power-supply makers may design in alternative semiconductors if cost, reliability, supply, or qualification support is better.

Therefore NVTS has potential differentiation at device + reference design level, but not monopoly control over the chain.

## Future Development View

Base case: NVTS becomes a credible niche/second-source wide-bandgap supplier in AI power and grid/industrial power. Revenue grows from the current low base, but profitability takes time because operating expenses are large relative to revenue.

Bull case: 800 VDC adoption starts in 2027-era AI factory deployments, NVTS wins production sockets in both SiC high-voltage and GaN lower-voltage conversion stages, and high-power revenue scales fast enough to produce operating leverage. Confirmation would require named production programs, backlog, customer diversification, and quarterly revenue far above the current $8M-$10M level.

Bear case: NVTS remains a technology demo / early qualified supplier while larger vendors capture production volume. In this case the NVIDIA association supports valuation temporarily but does not convert into durable revenue; dilution and cash burn become central again.

## Key Falsification Points

- Q2/Q3 2026 revenue growth stalls despite 800 VDC publicity.
- Customer concentration remains extreme or worsens.
- NVIDIA / OCP ecosystem announcements increasingly highlight Infineon, TI, ST, ROHM, or other vendors without NVTS production evidence.
- Gross margin fails to improve as high-power mix rises.
- NVTS raises capital before clear revenue conversion.

## Refresh Conditions

must_refresh_if:

- NVTS discloses named AI data-center production wins, not just demos or collaborations.
- NVIDIA updates the 800 VDC partner list or Kyber/Rubin Ultra power architecture timing.
- Infineon, TI, ST, ROHM, onsemi, or Power Integrations disclose competing production deployments.
- NVTS reports Q2 2026 or changes guidance.
- Distributor concentration, cash burn, or financing terms materially change.
