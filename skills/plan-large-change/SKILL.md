---
name: plan-large-change
description: "Use when a repository categorizes a requested functionality change as large: cross-cutting, risky, multi-phase, or requiring explicit phase-by-phase execution control."
---

# Plan Large Change

## Overview

Use the repository's large-change category to plan and implement work that
needs a multi-file plan set: one overview file plus one file per phase. Large
changes pause for approval before implementation and, by default, between
phases.

## Use This Skill When

- The repository's workflow categorizes the request as large.
- The change is cross-cutting, risky, or needs multiple deliberate phases.
- Phase-by-phase execution control matters unless the user explicitly approves
  the whole plan end to end.

Do not use this skill for work that fits the repository's small or medium
categories. Use `$plan-small-change` or `$plan-medium-change` instead.

## Workflow

1. Read `AGENTS.md`, `docs/index.md`, `docs/core/workflow.md`, and
   `docs/plans/PLANS.md`, then inspect the relevant code, docs, and tests
   before planning.
2. Confirm the task really fits the large category. If it does not, switch to
   the matching smaller planning skill before writing files.
3. Ask clarifying questions before finalizing the plan whenever scope, success
   criteria, constraints, rollout expectations, dependencies, or phase
   boundaries are still unclear.
4. Create a plan folder in `docs/plans/active/YYYY-MM-DD-short-slug/`.
5. Save:
   - `overview.md` with the big picture, constraints, phase sequence, and
     cross-phase validation strategy, plus a roadmap task checklist with
     explicit tasks and a concise planned-change summary
   - one phase file per phase, such as `phase-01-foundation.md`, each with
     a concise planned-change summary and an explicit task checklist
6. Present the plan set to the user and ask for approval.
7. If the user explicitly approves implementing the whole plan, execute the
   phases in order without additional permission checkpoints unless new
   ambiguity appears.
8. Otherwise, implement one phase at a time and ask for permission before
   continuing to the next phase.
9. Keep the overview and phase files current as discoveries, decisions, and
   outcomes evolve, and mark each roadmap or phase task as `[x]` immediately
   after it is completed.
