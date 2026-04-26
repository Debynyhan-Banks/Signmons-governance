# Screen Route API Matrix

Purpose: canonical alignment between screen IDs, frontend routes, and backend APIs.

## Public Marketing (Current)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Notes |
| --- | --- | --- | --- | --- |
| `SCR-PUB-001` | `/` | `signmons-marketing-web-feat-marketing-site` | none required | Home marketing page |
| `SCR-PUB-006` | `/pricing` | `signmons-marketing-web-feat-marketing-site` | none required | Pricing page |
| `SCR-PUB-007` | `/demo` | `signmons-marketing-web-feat-marketing-site` | `POST /api/marketing/try-demo`, `GET /api/marketing/try-demo/:leadId` | Live demo flow route |
| `SCR-PUB-009` | `/contact` | `signmons-marketing-web-feat-marketing-site` | `POST /api/marketing/lead-capture` (target), fallback pending | Email-min capture path |
| `SCR-PUB-010` | `/privacy`, `/terms` | `signmons-marketing-web-feat-marketing-site` | none required | Static legal pages |

## APP-006 Steel Thread (Current Program Now)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Status |
| --- | --- | --- | --- | --- |
| `SCR-APP-012` | `/app/intake-review` (planned) | backend app surface | intake read model + job readiness API (ticket-defined) | `Now` |

## Contract Rules

- Every route in `LINK_CTA_MAP.md` must appear in this matrix.
- Every backend endpoint listed here must be versioned in `DATA_CONTRACTS.md` when implemented.
- Placeholder endpoints must be tagged as `target` until shipped.
