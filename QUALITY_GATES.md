# Quality Gates (Mandatory)

Purpose: enforce consistent engineering quality across backend, frontend, and governance.

## 1) Architecture Gates (SOLID + SoC)

- Single Responsibility:
  - Services/controllers/components should have one clear reason to change.
  - Reject changes that mix transport + business rules + persistence in one unit.
- Separation of Concerns:
  - Keep boundary layers explicit:
    - Transport: controller/handler/gateway
    - Application: orchestration/use-case coordination
    - Domain: policies/reducers/rules
    - Infrastructure: persistence/external providers
- Open/Closed:
  - Prefer registration/composition extension points over `switch` growth.
- Interface Segregation:
  - Inject narrow interfaces per consumer; avoid fat dependency bags.
- Dependency Inversion:
  - Depend on interfaces/tokens at module boundaries, not concrete classes.

## 2) Modularity and Extensibility Gates

- Module boundaries must be explicit (public API exports only).
- Shared services must live in shared modules, not channel-specific modules.
- New features should plug into existing extension seams where possible.
- Any temporary seam/exception must be documented with a removal ticket.

## 3) OWASP-Aligned Security Gates

- A01 Access control:
  - Enforce tenant + role boundaries on protected paths.
- A05 Misconfiguration:
  - Fail-closed defaults for auth/signature/webhook validation.
- A07 Auth failures:
  - No bypass behavior outside explicit local-only flags.
- A08 Data integrity:
  - Verify inbound webhooks and trusted external events.
- A09 Logging/monitoring:
  - Security-relevant admin and payment actions must be auditable.
- A06 Vulnerable components:
  - Dependency audit must pass or have documented risk acceptance.

## 4) Data Contract Gates

- Input DTO validation at boundary entry points.
- Backward-compatible API/event contract changes unless versioned.
- No silent field behavior changes for payment, tenancy, or intake paths.

## 5) Documentation Consistency Gates

- Governance PRs must pass:
  - `node scripts/docs-consistency-check.mjs`
- CI must fail when:
  - screen IDs are duplicated or unresolved,
  - `Now` has 0 or >1 active tickets,
  - active boards reference archived/missing tickets,
  - CTA routes/endpoints mismatch `SCREEN_ROUTE_API_MATRIX.md`,
  - global pointer and governance board diverge.

## 6) Testing and Evidence Gates

- Required command gates:
  - Backend: `npm run -s build`, `npm test -- --runInBand`, `npm run -s arch:check`
  - Frontend: `npm run -s build`, `npm run -s lint`, `npm test -- --runInBand` (or approved equivalent)
  - Governance: docs consistency gate above
- Add focused tests for domain/policy changes.
- Include objective evidence in ticket completion notes.

## 7) Rejection Criteria

Reject ticket completion if any apply:

- Scope drift beyond `Now` ticket.
- Missing or failing required gates without explicit risk acceptance.
- Violations of tenant isolation, webhook validation, or payment integrity.
- New god-class/god-method growth without decomposition plan and ticket.
- Contradictory docs left unarchived in active paths.
