# Full ExecPlan Template

Use this format for any change that is multi-step, risky, cross-cutting, or
likely to take more than a short focused session.

An ExecPlan is a living implementation document. A different engineer or agent
should be able to resume the work using only the plan plus the repository
state. Update it while working, not just at the end.

## File Placement

- Create the file in `docs/plans/active/` before editing tracked files.
- Use the naming scheme `YYYY-MM-DD-short-slug.md`.
- Move the file to `docs/plans/completed/` when the change is finished.

## Required Sections

```md
# Short change title

This ExecPlan is a living document. Keep `Task Checklist`,
`Surprises & Discoveries`, `Decision Log`, and `Outcomes & Retrospective`
current as work proceeds. Mark each task as `[x]` immediately after
completion.

## Purpose / Big Picture

Explain why this change exists, what problem it solves, and what observable
outcome defines success.

## Scope and Constraints

State the intended scope, explicit non-goals, compatibility constraints, and
important operational or product limits.

## Context and Orientation

Describe the relevant current-state facts, files, components, and runtime
behavior someone would need before making changes.

## Planned Changes

Use this section for a quick summary of the intended edits.

- High-level files, components, interfaces, docs, or workflows that will
  change
- Important non-goals, unchanged areas, or rollout limits
- Short notes on how the change will reshape the current system

## Hypotheses / Open Questions

- Hypothesis:
  Why it matters:
  How it will be tested or disproved:

## Task Checklist

- [ ] Concrete implementation task.
- [ ] Concrete validation or migration task.
- [ ] Concrete documentation or follow-up task.

## Surprises & Discoveries

- Observation:
  Evidence:
  Impact:

## Decision Log

- Decision:
  Rationale:
  Date/Author:

## Validation

- Automated checks:
- Real behavior validation:
- Observability reviewed or added:

## Knowledge To Promote

- Docs to update if the work changes future defaults or guidance.

## Outcomes & Retrospective

Summarize the final result, unresolved risks, follow-up debt, and what future
changes should learn from this work.
```

## Quality Bar For Good ExecPlans

- Self-contained: the reader should not need hidden context from chat history.
- Executable: tasks should be concrete enough to follow directly.
- Truth-seeking: surprises and disproved hypotheses stay in the plan.
- Validation-oriented: success is tied to observable behavior, not only code
  structure.
- Task-driven: completed work is reflected immediately by updating the saved
  checklist.
- Skimmable: `Planned Changes` should orient the reader quickly without
  duplicating the task checklist.
