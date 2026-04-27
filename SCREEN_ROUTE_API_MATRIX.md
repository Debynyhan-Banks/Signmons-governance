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

## APP Sequence (Blocked Until Marketing DoD Exit)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Delivery Ticket |
| --- | --- | --- | --- | --- |
| `SCR-APP-012` | `/app/intake-review` (planned) | backend app surface | intake read model + job readiness API (ticket-defined) | APP-006 |

## Contract Rules

- Every route in `LINK_CTA_MAP.md` must appear in this matrix.
- Every backend endpoint here must be defined in `DATA_CONTRACTS.md`.
- Delivery ticket ownership must be explicit for each API-dependent screen.
