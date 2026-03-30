# Docs Index

This `docs/` tree is the system of record for the repository. `AGENTS.md`
should stay short and route readers here.

## Read Order

1. `docs/core/workflow.md`
2. `docs/core/principles.md`
3. The most relevant stack playbook in `docs/playbooks/`
4. Any architecture, spec, quality, or decision docs touched by the change

## If You Are Doing X, Read Y

| Task | Read first |
| --- | --- |
| Planning any change | `docs/plans/lightweight-template.md` or `docs/plans/PLANS.md` |
| Understanding the work loop | `docs/core/workflow.md` |
| Deciding where knowledge belongs | `docs/core/knowledge-management.md` |
| Changing system boundaries | `docs/architecture/index.md` |
| Changing behavior or journeys | `docs/specs/index.md` |
| Designing tests | `docs/quality/testing.md` |
| Improving telemetry or debugging | `docs/quality/observability.md` |
| Changing reliability characteristics | `docs/quality/reliability.md` |
| Making security-sensitive changes | `docs/quality/security.md` |
| Working in backend code | `docs/playbooks/backend.md` |
| Working in frontend code | `docs/playbooks/frontend.md` |
| Working in mobile code | `docs/playbooks/mobile.md` |
| Working in platform or infra | `docs/playbooks/devops.md` |
| Recording a lasting cross-cutting decision | `docs/decisions/index.md` |

## Structure

- `docs/core/`: repo-wide principles, workflow, knowledge rules, and future
  enforcement policy.
- `docs/plans/`: active/completed change plans plus planning templates.
- `docs/architecture/`: system maps, boundaries, dependency rules, and other
  structure docs.
- `docs/specs/`: behavior and journey specs anchored to observable outcomes.
- `docs/quality/`: testing, observability, reliability, and security guidance.
- `docs/playbooks/`: stack-specific engineering guidance with a shared shape.
- `docs/decisions/`: durable decision records and the template for new ones.
- `docs/references/`: curated external material and vendor references.
- `docs/generated/`: generated artifacts that should not bloat hand-written
  docs.

## Documentation Rules

- Keep durable guidance in `docs/`, not in ad hoc chat history.
- Keep transient work notes in the change plan until they become durable.
- Favor cross-links over duplication.
- When docs conflict, prefer the more specific doc, but fix the conflict rather
  than normalizing inconsistency.
