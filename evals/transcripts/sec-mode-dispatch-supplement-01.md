task_mode: `sec_supplement` ｜ research_object: COHR (Coherent Corp, US) ｜ depth: `quick_map` ｜ primary_skill: `skills/sec-filing-analysis` ｜ routing_basis: 既有 thesis 工作流内的 SEC 事实核验，不拆全文

**结论先说：这次离线，SEC 拿不到，share count 和 SBC 两项都是 `source_gap`，本地案例数据替代不了，我不会给未经核验的数字。**

**本地已查到的（事实）**

- 活跃案例 `cases/cohr-2026-05/` 里有 FY2026 Q3（季度截至 ~2026-03-31）的数据，但来源是 2026-05-06 的 earnings release（`cohr_q3_fy2026_results`，L1），证据链里没有 10-Q 本体。
- `financial-snapshot.csv` 没有 share count 行、没有 SBC 行——这两项当时就没入库，所以没法"从本地核实"，只能等联网补。

**推断（非事实）**

- COHR 财年 6 月底截止，到今天（2026-06-10）为止"最新 10-Q"应是 FY2026 Q3 那份，预计 2026 年 5 月上中旬随财报前后递交。具体 filing date 和 accession number 待联网确认。

**拿到数据后怎么补（refresh 计划）**

1. SEC submissions 确认 CIK 与最新 10-Q 的 accession number、filing date。
2. Share count 三处交叉：封面 "shares outstanding as of [date]"（最及时）、资产负债表 issued/outstanding、利润表 weighted-average basic/diluted；顺带核 diluted 口径对 Bain 系可转优先股的处理（if-converted 与否直接影响你 thesis 里的每股分母）。
3. SBC 两处：现金流量表 share-based compensation 行（YTD 口径）+ SBC 附注的分项；与 release 的 non-GAAP 调节表对账，确认 GAAP→non-GAAP EPS 差值里 SBC 占多大头。
4. 落库：按 `templates/sec-supplement-source-note.csv` 补一行 source note，`cases/cohr-2026-05/` 的 evidence-log 和 financial-snapshot 各加对应行（含 accession number、报告期、提取方法），标注 confirms / corrects 现有案例。

**refresh 条件**：must_refresh_if = 联网可用即补；另注意 COHR 财年 6 月底结束，FY2026 10-K 预计 ~2026 年 8 月发布，届时 Q3 10-Q 的数字将被年报口径覆盖，share count 以更新的封面日期为准。

follow-up（一条）：联网补数时，要不要顺带把回购授权余额和可转优先股的 if-converted 稀释口径一起核了写进 snapshot？这两项和 share count 是同一组分母问题，一次查完省得二跑。
