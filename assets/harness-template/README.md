# {{PROJECT_NAME}}

{{PRODUCT_DESCRIPTION}}

## Initial Context

- Primary stacks: `{{PRIMARY_STACKS}}`
- Platforms: `{{PLATFORMS}}`
- Operations profile: `{{OPS_PROFILE}}`
- Testing posture: `{{TESTING_POSTURE}}`
- Areas of emphasis: `{{EMPHASIS_AREAS}}`

## Working Model

This repository uses the `your-harness` workflow scaffold:

- `AGENTS.md` stays compact and routes work into `docs/`
- executable behavior changes start with a failing test
- durable guidance gets promoted into the right long-lived doc before closure
- functionality changes are categorized before implementation:
  - small: plan briefly in chat, wait for approval, then implement
  - medium: save one plan file, wait for approval, then implement
  - large: save an overview plus one file per phase, wait for approval, then
    implement phase by phase unless the whole plan is explicitly approved
- ask clarifying questions whenever the plan still has unclear requirements,
  constraints, success criteria, or sequencing

## Start Here

1. Read `AGENTS.md`
2. Open `docs/index.md`
3. Categorize the change before implementation and keep any saved plan files
   current while you work
