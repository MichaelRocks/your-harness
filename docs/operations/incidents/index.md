# Incident Reports

Use this area for one live incident document per incident. The report starts
when the incident is detected and stays live until recovery is verified and
follow-up work is captured.

## Start Here

- `docs/operations/incidents/incident-template.md`
- `docs/operations/incidents/active/README.md`
- `docs/operations/incidents/completed/README.md`

## Naming

- Use a file-safe ISO 8601 UTC timestamp plus slug:
  `YYYY-MM-DDTHH-MM-SSZ-short-slug.md`
- Example: `2026-04-04T19-42-00Z-database-timeouts.md`

## Lifecycle

- Create new reports in `docs/operations/incidents/active/`.
- Update the same file throughout response, mitigation, and validation.
- Move the file to `docs/operations/incidents/completed/` after the incident is
  closed and any deferred action items are copied to `docs/plans/tech-debt.md`.

## Expectations

- Use facts and timestamps wherever possible.
- Keep `Root Cause` honest. If it is not yet known, write `Under investigation`
  or `Unknown`.
- Mark each hypothesis as `open`, `confirmed`, or `disproved`.
- Keep the recovery plan current as tasks complete or new mitigation steps
  appear.
- Promote durable takeaways out of the incident report before closing it.
