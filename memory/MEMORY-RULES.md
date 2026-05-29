# Memory Rules

这个仓库采用 `wiki-style memory`，但 memory 不是原始信息堆积区，而是整理后的研究知识层。

## Memory Layers

### Identity And Preference Memory

记录 Mira 的稳定身份边界和用户偏好。

身份边界以根目录 [../MIRA.md](../MIRA.md) 为准，不在普通 memory 中重复维护。

适合写入用户偏好的内容：

- 长期关注的市场、行业和资产类别
- 偏好的输出语言、深度和格式
- 证据严格度和来源偏好
- 反复出现的 watchlist 或研究兴趣

默认写入位置：

- [user-preferences.md](user-preferences.md)

不适合写入：

- 与研究无关的私人信息
- 一次性闲聊、情绪或临时口味
- 没有明确用户授权的敏感信息
- 会把研究推向默认看多或默认看空的主观偏好

### Research Memory

记录某个主题或标的的研究结果链。

适合写入：

- 稳定的公司概览
- 长期 thesis
- 历史分歧点
- 历史证伪点
- 刷新记录

### Methodology Memory

记录研究方法本身的拆解、比较和状态。

适合写入：

- 候选方法的 `todo` 队列
- 已进入试用的 `trial` 方法
- 已纳入正式系统的 `adopted` 方法
- 已淘汰或失效的 `retired` 方法
- 方法的 credibility、reverse-engineering 来源和 follow-through 结果

### Market Playbook

记录可复用的市场经验类型。

适合写入：

- 财报前后常见价格行为
- 拥挤交易信号
- 周期股拐点特征
- 叙事过热与退潮模式

### Skill Knowledge

记录技能方法论。

适合写入：

- 技术面扫描框架
- 财务质量检查清单
- 舆情筛噪规则
- 研报使用规则

## Write Rules

- Mira 的唤醒词和人格边界只在 `MIRA.md` 中维护，其他文件引用它，不分叉定义。
- 只有经过案例验证的稳定内容，才进入 `memory/`
- memory 条目必须带 `last_updated`
- research memory 必须带 `based_on_cases`
- methodology memory 必须带 `status`
- methodology memory 应尽量带 `credibility_score`
- preference memory 必须来自用户明确表达或稳定重复行为，并且不得覆盖证据纪律
- 推断必须标为 `working view` 或 `hypothesis`
- 没有日期或来源依据的内容，不得写入正式 memory
- 未经比较和失效模式说明的方法，不得直接进入 `adopted`
- 没有 follow-through 的方法，默认只停留在 `todo` 或 `trial`

## Hygiene

- daily update 先进入 monitoring 记录，不直接进入 memory
- memory 只保留慢变量和复用价值高的内容
- 短期情绪不应污染长期 thesis 页面
- 拟人化只能用于交互入口，不应污染研究结论、证据判断或长期 memory
- 方法论队列可以保留探索性内容，但必须显式区分 `todo / trial / adopted / retired`
- 不要把“作者名气”写成方法质量本身，方法质量应由结构、证伪和表现决定
