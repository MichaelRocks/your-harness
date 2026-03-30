# Engineering Principles

These principles apply across backend, frontend, mobile, and infrastructure
work. They exist to keep the repository legible to humans and agents.

## Legibility First

- Prefer code, tests, and docs that can be understood locally.
- Prefer explicit boundaries and obvious data flow over clever indirection.
- Choose boring, inspectable building blocks when they meet the need.

## Root-Cause Fixes

- Treat symptom suppression as a failure mode.
- Do not remove assertions, reduce visibility, or weaken acceptance criteria to
  make a bug appear resolved.
- Fix the mechanism that causes the bug, or document the remaining gap and
  follow-up work in the plan or `docs/plans/tech-debt.md`.

## Behavior Over Internals

- Write and validate against observable behavior whenever possible.
- Unit tests are useful, but they are not enough when user, system, or operator
  behavior is what actually matters.
- Specs, tests, and review notes should describe what the system does from the
  outside.

## Observability Is Part of the Design

- Logs, metrics, traces, and dashboards are part of the product, not cleanup
  work for later.
- Favor structured telemetry tied to user journeys, system flows, and operator
  questions.
- Changes that affect debugging or operations should usually add or improve
  observability.

## Durable Knowledge

- Record hypotheses, findings, decisions, and surprises while working.
- Promote durable guidance into the right doc instead of burying it in a plan.
- Keep `AGENTS.md` reserved for repo-wide operating rules that affect most
  tasks.

## Simple Does Not Mean Careless

- Avoid over-engineering, but do not cut corners that create hidden coupling,
  poor diagnostics, or maintenance traps.
- Prefer the smallest complete solution, not the smallest patch that can make a
  test turn green.
