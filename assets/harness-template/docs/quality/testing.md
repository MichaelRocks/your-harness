# Testing

Testing exists to increase confidence in real behavior, not to satisfy a metric
or prove internal trivia.

## Core Rules

- Write a failing test before implementation when executable behavior changes.
- Prefer tests that exercise the observable contract at risk.
- Use the lowest-cost test layer that still verifies the real behavior that
  matters.
- Keep lower-level tests in support of behavior confidence, not as a substitute
  for it.

## What Good Tests Cover

- User-visible behavior
- System-visible contracts between components
- Operator-visible outcomes such as retries, alerts, or dashboards
- Failure handling and recovery paths

## Anti-Patterns

- Deleting or weakening assertions to get green builds
- Replacing a behavior test with an internal-only unit test
- Mocking away the exact boundary that contains the bug
- Declaring success without validating the externally visible outcome

## Choosing the Test Layer

- Backend: API, job, or integration tests usually matter more than isolated
  internals when the contract is external.
- Frontend: user-journey tests, accessibility checks, and contract tests matter
  more than component internals when UI behavior is changing.
- Mobile: device-level or simulator-driven flow tests matter when lifecycle,
  storage, networking, or permissions are involved.
- DevOps: deployment, provisioning, rollback, and health-signal validation
  matter more than static config checks alone.

## Documentation-Only Changes

For docs-only work, validate the behavior of the documentation itself:

- readers can find what they need quickly
- links resolve
- templates are internally consistent
- the stated workflow can actually be followed
