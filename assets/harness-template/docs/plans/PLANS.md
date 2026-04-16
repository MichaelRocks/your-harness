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

This ExecPlan is a living document. Keep `Progress`,
`Surprises & Discoveries`, `Decision Log`, and
`Outcomes & Retrospective` current as work proceeds.

## Purpose / Big Picture

Explain why this change exists, what problem it solves, and what observable
outcome defines success.

## Scope and Constraints

State the intended scope, explicit non-goals, compatibility constraints, and
important operational or product limits.

## Context and Orientation

Describe the relevant current-state facts, files, components, and runtime
behavior someone would need before making changes.

## Hypotheses / Open Questions

- Hypothesis:
  Why it matters:
  How it will be tested or disproved:

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
- Executable: steps should be concrete enough to follow directly.
- Truth-seeking: surprises and disproved hypotheses stay in the plan.
- Validation-oriented: success is tied to observable behavior, not only code
  structure.
