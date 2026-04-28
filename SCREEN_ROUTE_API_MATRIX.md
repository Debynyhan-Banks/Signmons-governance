# Screen Route API Matrix

Purpose: canonical alignment between screen IDs, frontend routes, and backend APIs.

## Public Marketing (Current Phase)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Contract Dependency | Delivery Ticket | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SCR-PUB-001` | `/` | `signmons-marketing-web-feat-marketing-site` | none required | n/a | FE baseline shipped | implemented |
| `SCR-PUB-006` | `/pricing` | `signmons-marketing-web-feat-marketing-site` | none required | `PaymentPolicy` (display dependency) | FE baseline shipped | implemented |
| `SCR-PUB-007` | `/demo` | `signmons-marketing-web-feat-marketing-site` | `POST /api/marketing/try-demo`, `GET /api/marketing/try-demo/:leadId`, `POST /api/marketing/try-demo/status` | marketingLead/try-demo contract | FE-008 | implemented |
| `SCR-PUB-009` | `/contact` | `signmons-marketing-web-feat-marketing-site` | `POST /api/marketing/lead-capture` | FE-007 lead-capture contract | FE-007 + BE-002 | implemented |
| `SCR-PUB-010` | `/privacy`, `/terms`, `/sms-terms` | `signmons-marketing-web-feat-marketing-site` | none required | n/a | FE-006 | implemented |
| `SCR-PUB-011` | `/done-for-you-setup` | `signmons-marketing-web-feat-marketing-site` | none required | `BusinessRuleSet`, `TenantBrandProfile` (messaging dependency) | FE-009 | implemented |
| `SCR-PUB-012` | `/business-rules` | `signmons-marketing-web-feat-marketing-site` | none required | `BusinessRuleSet`, `DispatchPolicy`, `PaymentPolicy` | FE-010 | implemented |
| `SCR-PUB-013` | `/brand-voice` | `signmons-marketing-web-feat-marketing-site` | none required | `TenantBrandProfile` | FE-011 | implemented |
| `SCR-PUB-014` | `/dispatch-scheduling` | `signmons-marketing-web-feat-marketing-site` | none required | `SchedulingWindow`, `Appointment`, `DispatchPolicy` | FE-012 | implemented |
| `SCR-PUB-015` | `/revenue-dashboard` | `signmons-marketing-web-feat-marketing-site` | none required | `RevenueEvent` | FE-013 | placeholder |
| `SCR-PUB-016` | `/roi-calculator` | `signmons-marketing-web-feat-marketing-site` | none required | `RevenueEvent` (input assumptions) | FE-013 | placeholder |
| `SCR-PUB-017` | `/compare/answering-services` | `signmons-marketing-web-feat-marketing-site` | none required | n/a | FE-014 | placeholder |
| `SCR-PUB-018` | `/compare/field-service-software` | `signmons-marketing-web-feat-marketing-site` | none required | n/a | FE-014 | placeholder |
| `SCR-PUB-019` | `/customer-technician-experience` | `signmons-marketing-web-feat-marketing-site` | none required | `NotificationPolicy`, `CustomerProfile`, `Appointment` | FE-015 | placeholder |

## APP Sequence (Blocked Until Marketing DoD Exit)

| Screen ID | Route | UI Owner Repo | Backend Endpoint(s) | Contract Dependency | Delivery Ticket | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SCR-APP-012` | `/app/intake-review` (planned) | backend app surface | intake read model + job readiness API (ticket-defined) | intake/job readiness contract | APP-006 | planned |
| `SCR-APP-025` | `/app/schedule` (planned) | backend app surface | scheduling/availability API set (ticket-defined) | `SchedulingWindow`, `Appointment` | APP-016 | planned |
| `SCR-APP-026` | `/app/business-rules` (planned) | backend app surface | tenant rules policy API set (ticket-defined) | `BusinessRuleSet`, `DispatchPolicy`, `PaymentPolicy` | APP-017 | planned |
| `SCR-APP-027` | `/app/brand-voice` (planned) | backend app surface | tenant brand voice profile API set (ticket-defined) | `TenantBrandProfile` | APP-018 | planned |
| `SCR-APP-028` | `/app/customers` (planned) | backend app surface | customer profile/history API set (ticket-defined) | `CustomerProfile`, `NotificationPolicy` | APP-019 | planned |

## Contract Rules

- Every route in `LINK_CTA_MAP.md` must appear in this matrix.
- Every backend endpoint here must be defined in `DATA_CONTRACTS.md`.
- Delivery ticket ownership must be explicit for each API-dependent screen.
