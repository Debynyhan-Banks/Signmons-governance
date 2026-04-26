# Signmons Governance

Canonical governance repository for the Signmons SaaS program.

This repository defines what Signmons builds, how work is executed, and what "done" means across implementation repositories.

## Repositories in Scope

- Backend: https://github.com/Debynyhan-Banks/signmons-calldesk-backend
- Frontend marketing: https://github.com/Debynyhan-Banks/Signmons-Marketing-Web-Feat-Marketing-Site
- Governance (this repo): https://github.com/Debynyhan-Banks/Signmons-governance

## Canonical Source Of Truth

Read and enforce in this order:

1. `SYSTEM_OF_RECORD.md`
2. `SAAS_SCOPE_DOD.md`
3. `EXECUTION_BOARD.md`
4. `SCREEN_INVENTORY.md`
5. `MVP_BACKLOG.md`
6. `DATA_CONTRACTS.md`
7. `QUALITY_GATES.md`
8. `AI_WORKFLOW_RULES.md`
9. `SESSION_HANDOFF.md`

## Governance Documents

- `SYSTEM_OF_RECORD.md` - precedence, non-contradiction rules, CI policy
- `GLOBAL_EXECUTION_POINTER.md` - cross-repo single pointer to active ticket
- `EXECUTION_BOARD.md` - governance board and sequencing
- `SCREEN_INVENTORY.md` - canonical screen IDs
- `SCREEN_ROUTE_API_MATRIX.md` - route-to-screen-to-API map
- `LINK_CTA_MAP.md` - conversion links and CTA behavior contract
- `MVP_BACKLOG.md` - ticket roadmap
- `TICKET_TEMPLATE.md` - required ticket spec format
- `WORKFLOW_RUNBOOK.md` - repeatable session protocol for bots/humans
- `DESIGN_SYSTEM.md`, `ENGINEERING_STANDARDS.md`, `DATA_CONTRACTS.md`, `SECURITY_BASELINE.md`, `QUALITY_GATES.md` - implementation standards
- `AI_WORKFLOW_RULES.md` - mandatory AI operating rules
- `SESSION_HANDOFF.md` - current session state and next handoff

## Working Agreement

- Strict ticket sequencing: one `Now` ticket only.
- No coding starts without `Now` assignment.
- One focused commit per ticket.
- Archive superseded docs/tickets immediately in the same PR.
- Docs consistency gate must pass on every PR.
