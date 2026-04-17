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
- changes start with a saved plan under `docs/plans/active/`
- executable behavior changes start with a failing test
- durable guidance gets promoted into the right long-lived doc before closure
- functionality changes should start with the right planning skill before
  implementation:
  - use `$plan-small-change` for small, contained requests that only need a
    brief approval plan in chat
  - use `$plan-medium-large-change` for medium or large requests that need a
    saved plan file before coding

## Start Here

1. Read `AGENTS.md`
2. Open `docs/index.md`
3. Keep the active change plan live while you work
