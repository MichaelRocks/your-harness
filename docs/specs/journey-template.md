# Journey Spec Template

Use this for user, system, or operator journeys that span multiple steps or
components.

## Template

```md
# Journey name

## Actor

User, service, batch job, or operator.

## Preconditions

State that must already be true.

## Main Path

1. Trigger
2. Intermediate system behavior
3. Final observable outcome

## Alternate and Failure Paths

- Failure mode:
  User or operator impact:
  Recovery path:
  Telemetry:

## Validation

- Primary end-to-end test:
- Secondary checks:
- Operational signals to review:
```
