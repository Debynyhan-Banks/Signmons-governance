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
| `SCR-PUB-011` | `/done-for-you-setup` | `signmons-marketing-web-feat-marketing-site` | none required | FE-009 |
| `SCR-PUB-012` | `/business-rules` | `signmons-marketing-web-feat-marketing-site` | none required | FE-010 |
| `SCR-PUB-013` | `/brand-voice` | `signmons-marketing-web-feat-marketing-site` | none required | FE-011 |
| `SCR-PUB-014` | `/dispatch-scheduling` | `signmons-marketing-web-feat-marketing-site` | none required | FE-012 |
| `SCR-PUB-015` | `/revenue-dashboard` | `signmons-marketing-web-feat-marketing-site` | none required | FE-013 |
| `SCR-PUB-016` | `/roi-calculator` | `signmons-marketing-web-feat-marketing-site` | none required | FE-013 |
| `SCR-PUB-017` | `/compare/answering-services` | `signmons-marketing-web-feat-marketing-site` | none required | FE-014 |
| `SCR-PUB-018` | `/compare/field-service-software` | `signmons-marketing-web-feat-marketing-site` | none required | FE-014 |
| `SCR-PUB-019` | `/customer-technician-experience` | `signmons-marketing-web-feat-marketing-site` | none required | FE-015 |

## APP Sequence (Blocked Until Marketing DoD Exit)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Delivery Ticket |
| --- | --- | --- | --- | --- |
| `SCR-APP-012` | `/app/intake-review` (planned) | backend app surface | intake read model + job readiness API (ticket-defined) | APP-006 |
| `SCR-APP-025` | `/app/schedule` (planned) | backend app surface | scheduling/availability API set (ticket-defined) | APP-016 |
| `SCR-APP-026` | `/app/business-rules` (planned) | backend app surface | tenant rules policy API set (ticket-defined) | APP-017 |
| `SCR-APP-027` | `/app/brand-voice` (planned) | backend app surface | tenant brand voice profile API set (ticket-defined) | APP-018 |
| `SCR-APP-028` | `/app/customers` (planned) | backend app surface | customer profile/history API set (ticket-defined) | APP-019 |

## Contract Rules

- Every route in `LINK_CTA_MAP.md` must appear in this matrix.
- Every backend endpoint here must be defined in `DATA_CONTRACTS.md`.
- Delivery ticket ownership must be explicit for each API-dependent screen.
