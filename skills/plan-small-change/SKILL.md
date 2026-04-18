---
name: plan-small-change
description: Use when a requested functionality change is small, contained, low-risk, and unlikely to need multiple implementation passes.
---

# Plan Small Change

## Overview

Use the repository's small-change category to plan and implement a contained
functionality change. Small changes start with a short plan in chat, wait for
approval, then execute in the same session.

## Use This Skill When

- The requested work is small, contained, and easy to describe in a few steps.
- The change is not cross-cutting, risky, or multi-hour.
- A short approval checkpoint is enough before implementation starts and the
  work can usually land in one focused pass.

Do not use this skill when the repository's categorization says the change is
medium or large, when the work needs a saved plan file before coding, or when
phase-by-phase approval gates are likely to matter. Use
`$plan-medium-change` or `$plan-large-change` instead.

## Workflow

1. Read `AGENTS.md`, `docs/index.md`, and `docs/core/workflow.md`, then inspect
   the relevant code and docs before proposing a plan. Use the repository's
   small/medium/large categorization, not guesswork in isolation.
2. Confirm the task still fits the small category. If it has grown into a
   medium or large change, stop and switch to the matching planning skill.
3. Ask clarifying questions before finalizing the plan whenever scope, success
   criteria, constraints, rollout expectations, or validation needs are still
   unclear.
4. Draft a concise plan in chat only. Keep it short and concrete:
   - scope
   - expected behavior
   - tests and direct validation
   - docs or observability follow-up if needed
5. Ask the user to approve the plan.
6. Once the plan is approved, implement it. Do not ask for a second approval
   step unless the user limits approval to planning only or new ambiguity
   appears.
7. If the work expands beyond the small category while implementing, pause,
   re-categorize, and switch to `$plan-medium-change` or `$plan-large-change`
   before continuing.
