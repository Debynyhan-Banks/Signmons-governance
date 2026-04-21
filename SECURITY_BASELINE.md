# Security Baseline (OWASP-Aligned)

## Core Controls

- Fail-closed auth and signature verification
- Strict input validation and normalization at boundaries
- Least privilege access controls for admin and tenant actions
- Safe error handling and diagnostic redaction
- Audit logging for sensitive operations

## OWASP Mapping (minimum)

- A01 Broken Access Control: tenant and role checks on every protected path
- A02 Cryptographic Failures: secure secret handling and transport-only sensitive data
- A03 Injection: validated inputs, parameterized DB access
- A04 Insecure Design: explicit threat checks for new critical flows
- A05 Security Misconfiguration: hardened env validation and safe defaults
- A06 Vulnerable Components: dependency audit gate in CI
- A07 Auth Failures: robust session/token checks and guard coverage
- A08 Data Integrity: verified webhooks and trusted event processing
- A09 Logging/Monitoring: actionable security logs and alert paths
- A10 SSRF: controlled outbound requests and allowlists where needed

## CI Security Gates

- Build + test gates must pass
- Architecture/security checks must pass
- Dependency critical vulnerability gate must pass or be formally risk-accepted
