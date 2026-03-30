# Mobile Playbook

## Common Change Types

- App flows and screen transitions
- Local storage, sync, and offline behavior
- Push, background, or lifecycle-driven behavior
- Device capability, permission, and platform integration changes

## Preferred Test Layers

- Start with a failing device-level, simulator, or end-to-end flow test for the
  user-visible behavior at risk.
- Add lower-level tests for business logic, serialization, or platform shims as
  needed.
- Do not rely on isolated model tests when the real risk is lifecycle or device
  interaction.

## Observability Expectations

- Crash and error reporting with device, version, and network context
- Metrics for launch, sync, latency, battery-sensitive work, and failure rates
- Tracing or breadcrumb-style flow visibility for multi-step experiences
- Signals for permission denials, background failures, and offline recovery

## Failure Modes and Root-Cause Cues

- Lifecycle races, stale caches, offline conflicts, permission handling gaps,
  device fragmentation issues, and background task starvation
- Look for assumptions that hold only on one OS version, device class, or
  connectivity state
- Do not hide bugs by removing user affordances that expose the broken path

## Validation Patterns

- Exercise the affected flow on representative devices or simulators
- Validate offline, resume, retry, and permission-denied behavior
- Check crash, error, and performance telemetry
- Confirm the visible state after app restarts, backgrounding, and network
  changes
