# Large Change Plan Set

Use this format for large changes: work that is cross-cutting, risky,
multi-phase, or important enough to warrant explicit phase boundaries and
phase-by-phase approval.

Large changes use a folder-based plan set. A different engineer or agent
should be able to resume the work using only the saved plan folder plus the
repository state. Update the overview and phase files while working, not just
at the end.

## File Placement

- Create a folder in `docs/plans/active/YYYY-MM-DD-short-slug/` before editing
  tracked files.
- Save `overview.md` in that folder.
- Save one file per phase, such as `phase-01-foundation.md`,
  `phase-02-migration.md`, and `phase-03-rollout.md`.
- Move the entire folder to `docs/plans/completed/` when the change is
  finished.

## `overview.md` Required Sections

```md
# Short change title

This overview is a living document. Keep the phase sequence,
cross-phase decisions, and overall outcomes current as work proceeds.

## Purpose / Big Picture

Explain why this change exists, what problem it solves, and what observable
outcome defines success.

## Scope and Constraints

State the intended scope, explicit non-goals, compatibility constraints, and
important operational or product limits.

## Context and Orientation

Describe the relevant current-state facts, files, components, and runtime
behavior someone would need before starting any phase.

## Clarifications Needed

- Open question:
  Why it matters:
  How it will be resolved:

## Phase Sequence

1. `phase-01-short-name.md` — what this phase achieves
2. `phase-02-short-name.md` — what this phase achieves

## Cross-Phase Validation

- Automated checks:
- Real behavior validation:
- Observability reviewed or added:

## Decision Log

- Decision:
  Rationale:
  Date/Author:

## Outcomes & Retrospective

Summarize the final result, unresolved risks, follow-up debt, and what future
changes should learn from this work.
```

## Phase File Required Sections

```md
# Phase N: Short title

## Goal

What this phase must accomplish before the next phase can begin.

## Scope and Dependencies

- In scope:
- Out of scope:
- Dependencies or prerequisites:

## Clarifications Needed

- Open question:
  Why it matters:
  How it will be resolved:

## Plan of Work

1. Concrete implementation step.
2. Concrete validation or migration step.
3. Concrete documentation or follow-up step.

## Progress

- [ ] Timestamped checkpoint for meaningful work items.

## Surprises & Discoveries

- Observation:
  Evidence:
  Impact:

## Validation

- Automated checks:
- Real behavior validation:
- Observability reviewed or added:

## Completion Notes

Summarize the phase outcome, remaining risks, and whether the next phase is
ready to start.
```

## Quality Bar For Large Plan Sets

- Self-contained: the reader should not need hidden context from chat history.
- Executable: overview and phase files should be concrete enough to follow.
- Truth-seeking: surprises and disproved assumptions stay in the saved plan.
- Phase-aware: each phase should have a clear boundary and completion signal.
