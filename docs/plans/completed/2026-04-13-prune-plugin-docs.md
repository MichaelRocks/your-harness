# Prune repo-root docs for the plugin shape

## Change Summary

Remove repo-root `docs/` content that only made sense when this repository was
itself the reusable harness scaffold. Keep a smaller maintainer-docs set that
matches a Codex plugin with skills, shared helpers, and a bundled scaffold in
`assets/harness-template/`.

## Expected Behavior

- `docs/` only contains maintainer-facing guidance needed for the plugin.
- Dead scaffold-only folders are removed from repo-root `docs/`.
- Routing docs point maintainers to `assets/harness-template/` for shipped
  scaffold content instead of keeping parallel copies under repo-root `docs/`.

## Hypotheses / Findings

- Finding: `docs/architecture/`, `docs/decisions/`, `docs/generated/`,
  `docs/playbooks/`, `docs/references/`, and `docs/specs/` are leftovers from
  when the repo root itself was the scaffold.
- Finding: `docs/quality/testing.md` and `docs/quality/observability.md` still
  map cleanly to plugin helper and skill maintenance.
- Finding: `docs/operations/`, `docs/quality/reliability.md`, and
  `docs/quality/security.md` were removable without losing necessary maintainer
  guidance for this repository.

## Planned Tests

- Review `AGENTS.md`, `docs/index.md`, and `docs/core/*` for broken references.
- Run a link/reference scan over `AGENTS.md`, `README.md`, `docs/`, `skills/`,
  and `references/`.

## Planned Observability

- No new telemetry; validation is documentation integrity only.

## Completion Notes

- Reduced repo-root `docs/` to `core/`, `plans/`, and the two live quality docs
  for testing and observability.
- Removed the obsolete repo-root sections: `architecture/`, `decisions/`,
  `generated/`, `operations/`, `playbooks/`, `references/`, `specs/`,
  `quality/reliability.md`, and `quality/security.md`.
- Updated `AGENTS.md`, `docs/index.md`, `docs/core/knowledge-management.md`,
  `docs/core/workflow.md`, and `docs/plans/tech-debt.md` so the maintainer docs
  no longer point at deleted sections.
- Validation completed with:
  - a live-doc reference scan over `AGENTS.md`, `README.md`, `docs/index.md`,
    `docs/core/*.md`, and `docs/quality/*.md`
  - a structure review via `find docs -maxdepth 3 \\( -type d -o -type f \\) | sort`
