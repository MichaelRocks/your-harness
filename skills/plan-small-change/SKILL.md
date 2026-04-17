---
name: plan-small-change
description: Use when a requested functionality change is small, contained, low-risk, and unlikely to need multiple implementation passes.
---

# Plan Small Change

## Overview

Prepare a short implementation plan for a small functionality change, get user
approval, and stop before coding. This skill is only for the planning step.

## Use This Skill When

- The requested work is small, contained, and easy to describe in a few steps.
- The change is not cross-cutting, risky, or multi-hour.
- A short approval checkpoint is enough before implementation starts.

Do not use this skill when the change touches many subsystems, needs a saved
execution record up front, or will likely take multiple iterations. Use
`$plan-medium-large-change` instead.

## Workflow

1. Read `docs/index.md` and `docs/core/workflow.md`, then inspect the relevant
   code and docs before proposing a plan.
2. Confirm the task still looks small. If it has grown into a medium or large
   change, stop and switch to `$plan-medium-large-change`.
3. Draft a concise plan in chat only. Keep it short and concrete:
   - scope
   - expected behavior
   - tests and direct validation
   - docs or observability follow-up if needed
4. Ask the user to approve the plan.
5. Stop after the approval request. Do not edit files, do not implement, and
   do not save the draft plan to a file during this step.

## After Approval

If the user wants implementation to begin, record the approved change in
`docs/plans/active/` with the lightweight template before editing tracked
files. The unsaved draft in chat does not replace the repository workflow.
