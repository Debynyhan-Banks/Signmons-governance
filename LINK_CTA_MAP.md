# Link and CTA Map

Purpose: remove dead links and ambiguous CTA behavior.

## Public CTA Contract

| Location | CTA Label | Route/Action | Capture Requirement | Backend | Delivery Ticket |
| --- | --- | --- | --- | --- | --- |
| Header nav | Demo | `/demo` | optional (demo flow captures) | `POST /api/marketing/try-demo` | FE-008 |
| Home hero | Experience the Demo | `/demo` | yes (phone + consent) | `POST /api/marketing/try-demo` | FE-008 |
| Pricing plans | Book Revenue Demo / Build My AI Dispatcher / Talk to Sales | `/contact` | yes (email minimum) | `POST /api/marketing/lead-capture` | FE-007 + BE-002 |
| Business Rules page | Book Revenue Demo / See Live Demo | `/contact`, `/demo` | contact: yes (email minimum) / demo: optional | `POST /api/marketing/lead-capture`, `POST /api/marketing/try-demo` | FE-010 |
| Brand Voice page | Book Revenue Demo / See Live Demo | `/contact`, `/demo` | contact: yes (email minimum) / demo: optional | `POST /api/marketing/lead-capture`, `POST /api/marketing/try-demo` | FE-011 |
| Dispatch and Scheduling page | Book Revenue Demo / See Live Demo | `/contact`, `/demo` | contact: yes (email minimum) / demo: optional | `POST /api/marketing/lead-capture`, `POST /api/marketing/try-demo` | FE-012 |
| Contact form | Submit | `/contact` form submit | yes (email minimum, required) | `POST /api/marketing/lead-capture` | FE-007 + BE-002 |
| Contact success | Live Demo | `/demo` | none | none | FE-008 |
| Footer nav | Demo | `/demo` | optional | `POST /api/marketing/try-demo` | FE-008 |

## Rules

- CTA routes must resolve in `SCREEN_ROUTE_API_MATRIX.md`.
- No `#` dead links for primary conversion CTAs.
- Demo route must use live demo API flow.
- Contact conversion must persist backend lead record with email minimum.
