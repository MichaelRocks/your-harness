---
name: plan-medium-change
description: "Use when a repository categorizes a requested functionality change as medium: more than a quick small fix, but still suitable for one saved plan file and one approval checkpoint before implementation."
---

# Plan Medium Change

## Overview

Use the repository's medium-change category to plan and implement work that
needs a saved plan file before coding but does not need a phased execution
structure.

## Use This Skill When

- The repository's workflow categorizes the request as medium.
- The change spans enough code or behavior that a saved plan file is warranted.
- One approval checkpoint before implementation is sufficient.

Do not use this skill for a small change that should start with a brief chat
plan only, or for a large change that needs an overview plus one file per
phase. Use `$plan-small-change` or `$plan-large-change` instead.

## Workflow

1. Read `AGENTS.md`, `docs/index.md`, `docs/core/workflow.md`, and
   `docs/plans/lightweight-template.md`, then inspect the relevant code, docs,
   and tests before planning.
2. Confirm the task still fits the medium category. If it has become small or
   large, switch to the matching planning skill before writing the plan.
3. Ask clarifying questions before finalizing the plan whenever scope, success
   criteria, constraints, rollout expectations, or validation needs are still
   unclear.
4. Save one plan file in `docs/plans/active/YYYY-MM-DD-short-slug.md`.
5. Capture at least:
   - change summary
   - concise planned-change summary
   - explicit task checklist
   - expected behavior
   - open questions or working assumptions
   - validation approach
   - docs or observability follow-up if needed
6. Present the saved plan to the user and ask for approval.
7. Once the plan is approved, implement it. Do not ask for a second approval
   step unless the user limits approval to planning only or new ambiguity
   appears. While implementing, keep the saved plan current and mark each task
   as `[x]` immediately after it is completed.
8. If the work expands into a phased effort, pause and switch to
   `$plan-large-change` before continuing.
