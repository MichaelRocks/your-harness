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

This overview is a living document. Keep the roadmap tasks, phase sequence,
cross-phase decisions, and overall outcomes current as work proceeds. Mark
each roadmap task as `[x]` immediately after completion.

## Purpose / Big Picture

Explain why this change exists, what problem it solves, and what observable
outcome defines success.

## Scope and Constraints

State the intended scope, explicit non-goals, compatibility constraints, and
important operational or product limits.

## Context and Orientation

Describe the relevant current-state facts, files, components, and runtime
behavior someone would need before starting any phase.

## Planned Changes

Use this section for a quick summary of the intended edits.

- High-level files, components, interfaces, docs, or workflows that will
  change
- Important non-goals, unchanged areas, or rollout constraints
- Short notes on how the full change is expected to reshape the current system

## Clarifications Needed

- Open question:
  Why it matters:
  How it will be resolved:

## Phase Sequence

1. `phase-01-short-name.md` — what this phase achieves
2. `phase-02-short-name.md` — what this phase achieves

## Roadmap Task Checklist

- [ ] Explicit roadmap task tied to a phase deliverable.
- [ ] Explicit roadmap task tied to a later phase deliverable.
- [ ] Explicit cross-phase validation, migration, or documentation task.

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

## Planned Changes

Use this section for a quick summary of the intended edits.

- High-level files, components, interfaces, docs, or workflows that this phase
  will change
- Important non-goals or areas deferred to other phases
- Short notes on how this phase moves the system toward the roadmap goal

## Task Checklist

- [ ] Concrete implementation task.
- [ ] Concrete validation or migration task.
- [ ] Concrete documentation or follow-up task.

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
- Executable: roadmap and phase tasks should be concrete enough to follow.
- Truth-seeking: surprises and disproved assumptions stay in the saved plan.
- Phase-aware: each phase should have a clear boundary and completion signal.
- Task-driven: roadmap and phase checklists are explicit and updated as work
  completes.
- Skimmable: `Planned Changes` should orient the reader quickly without
  duplicating the task checklists.
