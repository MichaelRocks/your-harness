# Docs Index

This `docs/` tree is the system of record for maintaining the `your-harness`
plugin itself. The shipped harness copied into user repositories lives under
`assets/harness-template/`.

## Read Order

1. `docs/core/workflow.md`
2. `docs/core/principles.md`
3. The most relevant shared reference in `references/` if the change touches a
   skill workflow
4. The shipped template under `assets/harness-template/` if the change touches
   generated user-project content

## If You Are Doing X, Read Y

| Task | Read first |
| --- | --- |
| Planning any change | `docs/plans/lightweight-template.md` or `docs/plans/PLANS.md` |
| Understanding the work loop | `docs/core/workflow.md` |
| Deciding where knowledge belongs | `docs/core/knowledge-management.md` |
| Changing the shipped scaffold | `assets/harness-template/AGENTS.md` |
| Designing or updating helper tests | `docs/quality/testing.md` |
| Improving CLI or skill diagnostics | `docs/quality/observability.md` |
| Updating skill prompts or defaults | `references/create-harness-questionnaire.md` |
| Updating adoption conflict policy | `references/adoption-conflict-policy.md` |

## Structure

- `docs/core/`: plugin-maintainer workflow, principles, and knowledge rules.
- `docs/plans/`: active/completed change plans plus planning templates.
- `docs/quality/`: testing and observability expectations for helpers and
  skills.
- `assets/harness-template/`: canonical scaffold copied into user repos.
- `references/`: shared skill inputs and adoption policy.

## Documentation Rules

- Keep durable guidance in `docs/`, not in ad hoc chat history.
- Keep shipped scaffold guidance in `assets/harness-template/`, not only in the
  root maintainer docs.
- Keep transient work notes in the change plan until they become durable.
- Favor cross-links over duplication.
- When docs conflict, prefer the more specific doc, but fix the conflict rather
  than normalizing inconsistency.
