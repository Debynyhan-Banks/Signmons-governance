# Signmons-governance
Canonical source of truth for Signmons scope, screen inventory, execution workflow, quality gates, security standards, and Definition of Done

# Signmons Governance

Canonical governance repository for the Signmons SaaS program.

This repo defines what we are building, how we execute, and what “done” means across all implementation repos (backend, frontend, marketing, admin tools).

## Purpose

- Keep one source of truth for scope, architecture rules, and delivery standards.
- Prevent drift between repos, contributors, and AI coding sessions.
- Enforce consistent quality, security, and release readiness.

## What belongs here

- Product scope and boundaries
- Definition of Done (ticket, feature, release)
- Execution board and sprint sequencing
- Screen inventory and ownership
- Design system standards
- Engineering standards (SOLID, SRP, SoC, modularity)
- Data contracts and versioning rules
- OWASP/security baseline and guardrails
- AI workflow rules and session handoff format

## What does NOT belong here

- Production app code
- Feature implementation PRs
- Runtime secrets or environment values
- Build artifacts

## Canonical precedence order

If docs conflict, resolve in this order:

1. `SAAS_SCOPE_DOD.md`
2. `EXECUTION_BOARD.md`
3. Source plan docs (`MVP_BACKLOG.md`, `REFACTOR*.md`)
4. Supporting docs (`SCREEN_INVENTORY.md`, `DESIGN_SYSTEM.md`, etc.)

## Core docs in this repo

- `SAAS_SCOPE_DOD.md` — product scope + ship gates
- `EXECUTION_BOARD.md` — single active `Now` ticket and queue discipline
- `MVP_BACKLOG.md` — epics, tickets, acceptance criteria
- `SCREEN_INVENTORY.md` — authoritative screen IDs and ownership
- `DESIGN_SYSTEM.md` — tokens, components, motion, accessibility rules
- `ENGINEERING_STANDARDS.md` — coding standards and architecture rules
- `DATA_CONTRACTS.md` — API/event contracts and change policy
- `SECURITY_BASELINE.md` — OWASP controls and required checks
- `AI_WORKFLOW_RULES.md` — operating contract for any coding assistant
- `SESSION_HANDOFF.md` — session continuity and next actions

## Screen ID convention

- `SCR-PUB-###` — marketing/public
- `SCR-APP-###` — tenant/product app
- `SCR-ADM-###` — platform admin/internal

All tickets must map to one or more screen IDs (if UI scope exists).

## Execution model

1. One active `Now` ticket at a time.
2. No coding without a ticket in `EXECUTION_BOARD.md`.
3. One focused commit per ticket.
4. Ticket must include evidence (tests, logs, screenshots, or API proof).
5. Update `SESSION_HANDOFF.md` at end of each working session.

## Definition of Done (summary)

### Ticket DoD
- Acceptance criteria complete
- Required checks passed
- Evidence captured
- Docs/contracts updated when changed
- One focused commit

### Feature DoD
- All child tickets complete
- Cross-flow validation done
- Security and observability verified

### Release DoD
- Scope gates satisfied
- Security baseline satisfied
- KPI instrumentation available
- Rollback plan documented

## Security baseline

Signmons standards require:
- Fail-closed auth/signature verification
- Input validation at boundaries
- Least-privilege access controls
- Sanitized error handling and auditability
- OWASP-aligned controls on all exposed surfaces

## AI collaboration policy

All AI-assisted implementation must follow `AI_WORKFLOW_RULES.md`:
- execute only current ticket
- no scope expansion
- run required gates
- produce explicit change report
- update handoff before stop

## Ownership

Repo owner: Signmons product owner and authorized maintainers.

Changes to scope, DoD, or governance require:
- rationale in commit/PR
- updated related docs
- explicit impact notes for active repos
