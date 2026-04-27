# Screen Route API Matrix

Purpose: canonical alignment between screen IDs, frontend routes, and backend APIs.

## Public Marketing (Current Phase)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Delivery Ticket |
| --- | --- | --- | --- | --- |
| `SCR-PUB-001` | `/` | `signmons-marketing-web-feat-marketing-site` | none required | FE baseline shipped |
| `SCR-PUB-006` | `/pricing` | `signmons-marketing-web-feat-marketing-site` | none required | FE baseline shipped |
| `SCR-PUB-007` | `/demo` | `signmons-marketing-web-feat-marketing-site` | `POST /api/marketing/try-demo`, `GET /api/marketing/try-demo/:leadId`, `POST /api/marketing/try-demo/status` | FE-008 |
| `SCR-PUB-009` | `/contact` | `signmons-marketing-web-feat-marketing-site` | `POST /api/marketing/lead-capture` | FE-007 + BE-002 |
| `SCR-PUB-010` | `/privacy`, `/terms` | `signmons-marketing-web-feat-marketing-site` | none required | FE-006 |
| `SCR-PUB-011` | `/setup` (planned) | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |
| `SCR-PUB-012` | `/rules` (planned) | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |
| `SCR-PUB-013` | `/brand-voice` (planned) | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |
| `SCR-PUB-014` | `/dispatch` (planned) | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |
| `SCR-PUB-015` | `/revenue-dashboard` (planned) | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |
| `SCR-PUB-016` | `/roi-calculator` (planned) | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |
| `SCR-PUB-017` | `/compare-answering-services` (planned) | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |
| `SCR-PUB-018` | `/compare-fsm` (planned) | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |
| `SCR-PUB-019` | `/customer-tech-experience` (planned) | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |

## APP Sequence (Blocked Until Marketing DoD Exit)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Delivery Ticket |
| --- | --- | --- | --- | --- |
| `SCR-APP-012` | `/app/intake-review` (planned) | backend app surface | intake read model + job readiness API (ticket-defined) | APP-006 |
| `SCR-APP-025` | `/app/scheduling` (planned) | backend app surface | calendar availability + appointment APIs (ticket-defined) | APP-016 |
| `SCR-APP-026` | `/app/rules` (planned) | backend app surface | business rules CRUD + evaluation trace APIs (ticket-defined) | APP-017 |
| `SCR-APP-027` | `/app/brand-voice` (planned) | backend app surface | tenant voice profile APIs (ticket-defined) | APP-018 |
| `SCR-APP-028` | `/app/customers` (planned) | backend app surface | customer profile + history APIs (ticket-defined) | APP-019 |

## Contract Rules

- Every route in `LINK_CTA_MAP.md` must appear in this matrix.
- Every backend endpoint here must be defined in `DATA_CONTRACTS.md`.
- Delivery ticket ownership must be explicit for each API-dependent screen.
