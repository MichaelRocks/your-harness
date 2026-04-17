---
name: plan-medium-large-change
description: Use when a requested functionality change is medium or large in scope, cross-cutting, risky, or likely to take multiple iterations.
---

# Plan Medium Or Large Change

## Overview

Prepare a saved change plan for a medium or large functionality change, get
user approval, and stop before implementation begins.

## Use This Skill When

- The request spans multiple files, subsystems, or user flows.
- The work is risky, hard to estimate, or likely to take multiple passes.
- The change needs a durable execution record before coding starts.

Do not use this skill for a small, contained change that can be described and
approved in a brief chat plan. Use `$plan-small-change` instead.

## Workflow

1. Read `docs/index.md` and `docs/core/workflow.md`, then inspect the current
   code, docs, and tests before writing the plan.
2. Save a plan file in `docs/plans/active/YYYY-MM-DD-short-slug.md` before any
   tracked-file implementation work.
3. Use:
   - `docs/plans/lightweight-template.md` only if deeper exploration shows the
     change is actually still small.
   - `docs/plans/PLANS.md` for the intended medium or large change.
4. Capture at least:
   - change summary and scope
   - expected observable behavior
   - hypotheses and open questions
   - failing tests or validation strategy
   - observability or documentation updates
5. Present the saved plan to the user and ask for approval.
6. Stop after the approval request. Do not implement the plan yet.

## Notes

- Keep the saved plan live as new findings arrive.
- If the user narrows the scope enough that the work is genuinely small, it is
  acceptable to switch to `$plan-small-change` before implementation.
