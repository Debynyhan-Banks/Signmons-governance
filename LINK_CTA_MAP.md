# Link and CTA Map

Purpose: remove dead links and ambiguous CTA behavior.

## Public CTA Contract

| Location | CTA Label | Route/Action | Capture Requirement | Backend | Status |
| --- | --- | --- | --- | --- | --- |
| Header nav | Demo | `/demo` | optional (demo flow captures) | `POST /api/marketing/try-demo` | active |
| Home hero | Experience the Demo | `/demo` | yes (phone + consent in live demo flow) | `POST /api/marketing/try-demo` | active |
| Pricing plans | Book Revenue Demo / Build My AI Dispatcher / Talk to Sales | `/contact` | yes (email minimum) | `POST /api/marketing/lead-capture` (target) | target |
| Contact form | Submit | `/contact` form submit | yes (email minimum, required) | `POST /api/marketing/lead-capture` (target) | target |
| Contact success | live demo | `/demo` | none | none | active |
| Footer nav | Demo | `/demo` | optional | `POST /api/marketing/try-demo` | active |

## Rules

- CTA routes must resolve in `SCREEN_ROUTE_API_MATRIX.md`.
- No `#` dead links for primary conversion CTAs.
- Demo route must open live demo flow, not static dead-end content.
- Minimum lead capture is email on contact conversion paths.
