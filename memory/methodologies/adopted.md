# Methodology Queue: Adopted

- last_updated: 2026-04-22

## Purpose

记录已经正式纳入 `Mira` 的方法。

## Entry Format

- `method_name`
- `role`
- `adoption_reason`
- `based_on_cases`
- `notes`

## Current Items

- `framework-routing`
  role: `framework-router`
  adoption_reason: 不同股票的主导定价变量不同，统一框架会系统性错配。
  based_on_cases: `AAPL sample and routed design iteration`
  notes: 已进入 `research-loop` 的正式步骤。

- `supply-chain`
  role: `overlay`
  adoption_reason: 能沿上下游和同层级补证据链，但不替代主框架。
  based_on_cases: `design iteration`
  notes: 当前已作为首个 overlay 进入正式结构，仍需要更多 case 验证写法细节。
