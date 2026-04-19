# Lightweight Plan Template

Use this template for medium changes: work that is larger than a quick
chat-planned small change but does not need a phased large-change plan set.
The saved plan must still be detailed enough that another engineer or agent
could pick it up without hidden chat context.

## File Placement

- Create the file in `docs/plans/active/`.
- Use the naming scheme `YYYY-MM-DD-short-slug.md`.
- Move it to `docs/plans/completed/` when done.

Small changes start with an approved plan in chat and do not use this file
template. Large changes use `docs/plans/PLANS.md` and save an overview plus
one file per phase.

## Template

```md
# Short change title

This plan is a living document. Keep `Task Checklist` and `Completion Notes`
current as work proceeds. Mark each task as `[x]` immediately after
completion.

## Change Summary

One paragraph describing the problem, scope, and intended outcome.

## Planned Changes

Use this section for a quick summary of the intended edits.

- High-level files, components, workflows, or contracts that will change
- Important non-goals or unchanged areas
- Short notes that help a reader understand the shape of the work quickly

## Expected Behavior

- What should be true after the change from the outside

## Task Checklist

- [ ] Detailed implementation task
- [ ] Detailed validation task
- [ ] Detailed documentation or follow-up task

## Hypotheses / Findings

- Hypothesis or confirmed finding

## Planned Tests

- Failing test to write first
- Additional automated checks
- Real behavior validation

## Planned Observability

- Logs, metrics, traces, dashboards, or alerts to add or review

## Completion Notes

- Final outcome
- Follow-up debt or docs to update
```

## When To Escalate To a Full ExecPlan

Switch to `docs/plans/PLANS.md` if the change becomes cross-cutting, risky,
hard to estimate, or needs explicit phases instead of one saved plan file.

## Quality Bar

- Keep `Planned Changes` concise and high-level.
- Make the task checklist explicit enough to execute directly.
- Update task checkboxes immediately as work completes.
