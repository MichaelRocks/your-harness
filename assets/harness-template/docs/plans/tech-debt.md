# Tech Debt Log

Capture meaningful debt discovered during implementation or incident response
but intentionally left out of the current change or mitigation.

## Entry Template

```md
### Short title

- Source: `docs/plans/completed/YYYY-MM-DD-short-slug.md` or
  `docs/plans/completed/YYYY-MM-DD-short-slug/overview.md` or
  `docs/operations/incidents/completed/YYYY-MM-DDTHH-MM-SSZ-short-slug.md`
- Area:
- Problem:
- Risk if left as-is:
- Why it was deferred:
- Suggested follow-up:
- Prevention benefit:
- Owner:
- Status: `open` | `planned` | `done`
```

## Rules

- Do not use this file to hide unfinished critical work that should block the
  current change.
- Link back to the originating completed plan or incident whenever possible.
- Every incident action item that is not resolved during mitigation should also
  be captured here with a backlink to the incident report.
- Prefer a small number of clear debt items over a vague backlog dump.
