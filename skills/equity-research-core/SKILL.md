# Equity Research Core Skill

这是 MVP 唯一的研究 skill，用于在单次研究中统一处理：

- 基本面
- 财务质量
- 技术面节奏
- 事件与舆情

它不是四个独立 skill 的简单拼接，而是一个面向 `research package` 的最小主 skill。

## Use When

- 需要对单一股票做首次覆盖或阶段性复核
- 需要把多源数据整理成一个可追溯的研究包
- 需要在同一份输出里同时包含公司、财务、价格、事件四个视角

## Required Inputs

- company_name
- ticker
- market
- research_question
- research_cutoff_date
- thesis_horizon

## Required Source Types

- `L1` 公司披露或官方材料
- `L5` 市场数据
- `L4` 事件/新闻材料可选但建议使用

## Output Package

这个 skill 必须输出统一的 `research package`：

- `investment-memo.md`
- `evidence-log.csv`
- `case-notes.md`

## Required Sections In Case Notes

- business and industry
- financial quality
- technical context
- events and sentiment
- fact vs inference

## Boundaries

- 它只定义研究组织方式，不承诺自动抓取。
- 它不区分短线、中线、长线独立流程。
- 它允许写技术面和事件面，但它们服务于 thesis，不单独形成交易系统。

## Quality Bar

- 核心结论必须可回溯到来源
- 事实与推断必须显式区分
- 每份 memo 必须有时效边界
- 至少覆盖公司、财务、价格、事件四个视角中的三个

