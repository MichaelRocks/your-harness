# Security

Security guidance should be practical, explicit, and proportionate to the risk.

## Baseline Rules

- Prefer secure defaults over optional hardening.
- Minimize privileges, tokens, scopes, and exposed surfaces.
- Validate inputs at trust boundaries.
- Handle secrets through approved secret-management paths, not ad hoc config.
- Keep dependency and platform updates current enough to avoid known exposure.

## Review Questions

- What new trust boundary is being crossed?
- What data is sensitive, and where can it leak?
- What is the abuse path if validation fails?
- What happens if credentials, sessions, or tokens are replayed or stolen?

## Validation Ideas

- Authorization and authentication tests
- Input validation and malformed-input tests
- Secret exposure review in logs, traces, and error messages
- Dependency and configuration review for risky defaults
