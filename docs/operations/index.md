# Operations

Use this area for operator-facing material: incident records, recovery
procedures, and future runbooks.

## Start Here

- `docs/operations/incidents/index.md`

## What Belongs Here

- Live incident reports created at incident start
- Completed incident records kept for historical reference
- Operator-facing recovery procedures and future runbooks
- Operational guidance that should be available during diagnosis or mitigation

## Incident Workflow

1. Create a new incident report in `docs/operations/incidents/active/`.
2. Name it with a file-safe ISO 8601 UTC timestamp plus slug:
   `YYYY-MM-DDTHH-MM-SSZ-short-slug.md`.
3. Keep one live document from first detection through mitigation, validation,
   and closure.
4. Update symptoms, timeline, hypotheses, recovery steps, and outcome as facts
   change.
5. If the incident requires tracked file changes, also create or update a
   change plan in `docs/plans/active/`.
6. Promote durable takeaways into the right long-lived docs under `docs/`.
7. Copy unresolved prevention work into `docs/plans/tech-debt.md`.
8. Move the report to `docs/operations/incidents/completed/` when the incident
   is closed.

## Promotion Rules

- Keep transient investigation detail in the incident report.
- Promote repo-wide workflow or policy changes to `docs/core/`.
- Promote architecture or dependency lessons to `docs/architecture/`.
- Promote behavior contracts or operator journeys to `docs/specs/`.
- Promote testing, observability, reliability, or security defaults to
  `docs/quality/`.
- Promote operator-facing recovery procedures and future runbooks here under
  `docs/operations/`.
- Record deferred prevention work in `docs/plans/tech-debt.md`.
