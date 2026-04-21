# Signmons Governance

Canonical governance repository for the Signmons SaaS program.

This repository defines what Signmons builds, how work is executed, and what "done" means across all implementation repositories.

## Repositories in Scope

- Backend: https://github.com/Debynyhan-Banks/signmons-calldesk-backend
- Frontend marketing: https://github.com/Debynyhan-Banks/Signmons-Marketing-Web-Feat-Marketing-Site
- Governance (this repo): https://github.com/Debynyhan-Banks/Signmons-governance

## Core Objective

Create a durable operating system for product and engineering delivery so multiple contributors and AI coding agents can collaborate without scope drift.

## Source-of-Truth Rule

If documents conflict, precedence is:

1. `SAAS_SCOPE_DOD.md`
2. `EXECUTION_BOARD.md`
3. plan docs (`MVP_BACKLOG.md`, `REFACTOR*.md`)
4. implementation docs (`DESIGN_SYSTEM.md`, `DATA_CONTRACTS.md`, `SECURITY_BASELINE.md`, `QUALITY_GATES.md`)

## Governance Documents

- `SAAS_SCOPE_DOD.md` - product scope and Definition of Done
- `EXECUTION_BOARD.md` - active queue and current ticket
- `MVP_BACKLOG.md` - epics, ticket bundles, acceptance criteria
- `SCREEN_INVENTORY.md` - canonical screen IDs and coverage map
- `DESIGN_SYSTEM.md` - visual, interaction, accessibility standards
- `ENGINEERING_STANDARDS.md` - SOLID, modularity, SoC, testing conventions
- `DATA_CONTRACTS.md` - API/event contract rules and compatibility policy
- `SECURITY_BASELINE.md` - OWASP-aligned baseline controls
- `QUALITY_GATES.md` - mandatory architecture, security, contract, and test gates
- `AI_WORKFLOW_RULES.md` - mandatory operating rules for AI coding sessions
- `SESSION_HANDOFF.md` - current session state and next actions

## Working Agreement

- One active ticket at a time in `EXECUTION_BOARD.md`.
- No coding starts without a ticket in `Now`.
- One focused commit per ticket.
- Evidence is required for completion (tests, logs, screenshots, API proof).
- End every session by updating `SESSION_HANDOFF.md`.
