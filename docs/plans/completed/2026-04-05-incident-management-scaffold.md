# Incident management scaffold

## Change Summary

Add a first-class incident management workflow to the harness by introducing a
new `docs/operations/` area, a live incident report template, active/completed
incident directories, and stronger guidance for promoting takeaways and action
items into durable docs and the tech debt log.

## Expected Behavior

- Readers can find incident management guidance from `docs/index.md` and the
  repository routing docs.
- Incident reports live under `docs/operations/incidents/` and use a file-safe
  ISO 8601 UTC timestamp plus slug naming scheme.
- The incident template supports active response and final closure in one live
  document.
- Incident action items are also recorded in `docs/plans/tech-debt.md` with a
  backlink to the source incident.

## Hypotheses / Findings

- Finding: The scaffold already separates transient notes from durable guidance
  via plans, quality docs, and knowledge-promotion rules.
- Finding: A dedicated `docs/operations/` area fits the existing docs
  taxonomy better than placing incident artifacts under `docs/quality/` or
  `docs/plans/`.
- Finding: The tech debt log needs a richer entry template to carry
  incident follow-up items without losing ownership or source context.

## Planned Tests

- Documentation navigation review from `AGENTS.md` and `docs/index.md`
- Internal consistency review for directory lifecycle, templates, and naming
- Link and workflow review for incident-to-tech-debt and incident-to-durable
  knowledge promotion guidance

## Planned Observability

- Docs-only change; no runtime telemetry changes
- Add guidance that incident reports should capture signals, timelines, and
  operator-visible symptoms clearly

## Completion Notes

- Final outcome: Added `docs/operations/` with incident routing, lifecycle
  directories, and a live incident template; updated `AGENTS.md`,
  `docs/index.md`, `docs/core/workflow.md`, `docs/core/knowledge-management.md`,
  and `docs/plans/tech-debt.md` so incident reports fit the existing harness
  workflow without replacing change plans.
- Validation: Reviewed doc navigation from `AGENTS.md` and `docs/index.md`,
  verified the incident template supports unknown root cause, evolving
  hypotheses, live recovery updates, and action-item debt linkage, confirmed
  the new operations tree exists, and ran `git diff --check` successfully.
- Follow-up debt or docs to update: None.
