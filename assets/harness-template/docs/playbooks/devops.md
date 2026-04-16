# DevOps Playbook

## Common Change Types

- Infrastructure provisioning and configuration
- Deployment and rollout behavior
- CI/CD pipeline behavior
- Monitoring, alerting, and operational automation

## Preferred Test Layers

- Start with a failing validation that exercises the changed operational
  behavior: deployment, rollout, provisioning, rollback, or health checks.
- Add static linting or config tests in support, not as the only evidence.
- Do not treat syntax validation as proof that production behavior is safe.

## Observability Expectations

- Structured deploy and automation logs
- Metrics for rollout health, error rate, latency, capacity, and saturation
- Traces or correlation IDs across pipeline and runtime systems where useful
- Dashboards and alerts for service health, drift, and automation failures

## Failure Modes and Root-Cause Cues

- Drift, partial rollouts, hidden manual steps, retry loops, credential
  expiration, and unowned alerts
- Look for missing rollback paths, poor blast-radius control, or invisible
  automation assumptions
- Do not hide bugs by muting alerts or reducing health checks without solving
  the underlying issue

## Validation Patterns

- Exercise the deployment or automation path in a realistic environment
- Validate rollback, drift detection, and health-signal behavior
- Check the resulting dashboards, alerts, and operational logs
- Confirm operator-visible outcomes, not just config validity
