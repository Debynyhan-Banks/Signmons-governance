# Organization onboarding MVP — 2026-09-10

## Approved requirement and execution boundary

Owner requested organization business rules, common answers in the company brand voice, and an intake page if absent; then approved inspection/planning and requested continuing percentages. This adds explicit onboarding acceptance to the approved business-specific-controls capability, not another general-purpose knowledge platform. No code, provider configuration, tenant provisioning or release is performed here. APP-013 remains Now; selecting an implementation ticket for onboarding requires pointer/board/handoff alignment before coding. APP-033 already owns consumption of approved tenant knowledge and brand voice; it is not promoted by this document.

## Verified inventory

Inspected backend feature checkpoint f0ba587 (implementation 670e973), governance fca57a5; fetched origins before this update. `src/tenants/dto/create-tenant.dto.ts` accepts name, displayName and 10–500 character instructions. `src/tenants/tenants.controller.ts` exposes admin-guarded POST /tenants; this is not owner self-service onboarding. `src/tenants/tenants.service.ts` stores instructions/prompt in tenant settings, defaults timezone to UTC, and adds automated-assistant/no-unsupported-promises guidance. These free-text fields do not demonstrate structured facts, approval/version lifecycle or grounded FAQ answers.

The inspected `ui/src/app` page inventory includes routing, messaging settings, intake review, dispatch and technician pages, but no organization onboarding page. `src/communications/twilio-webhook.service.ts` emits a configured greeting, not conversational company FAQ answering. TICKETS/APP-033.md already specifies brand voice, service facts, hours, coverage, approved knowledge sources and version/access controls. Reuse those requirements and existing tenant settings; do not duplicate operational policy authority.

## Minimal owner/admin intake page

1. Company profile: display name, timezone, approved contact details, business hours and after-hours fallback.
2. Services: offered and unsupported services; reference the canonical service catalog and coverage configuration.
3. Operating rules: show/link authoritative booking, payment, cancellation and escalation settings. Conflicting prose cannot override these controls. Identify missing policy rather than invent defaults.
4. Common questions: owner-authored question/answer pairs, source or accountable owner, and review date. Pricing, warranties and other claims require explicit approved facts; unknowns escalate.
5. Brand voice: greeting, tone, preferred wording and prohibited claims. Clearly identify Signmons as an automated assistant. Voice cannot authorize diagnosis, price exceptions, booking, payment or dispatch.
6. Review: draft → owner/admin review → approved version. Draft edits cannot silently replace the approved version used in conversations. Show a preview of common answers and fallback before approval.

No website crawling, uploads/RAG, unrestricted rule editor, multi-location workflow or provider activation is needed for this first page. Organization signup/billing/provisioning is separate from configuring an authorized existing organization.

## Six acceptance outcomes and percentage baseline

- [ ] O1 Authorized owner/admin can save and reopen a tenant-scoped draft; denied and foreign-tenant access fails.
- [ ] O2 Required company facts validate and canonical routing/payment/booking references show missing/conflicting state truthfully.
- [ ] O3 Approved FAQ answers and brand-voice fields persist with explicit unknown-answer/human fallback.
- [ ] O4 Review/approval records actor, version and time; unapproved edits cannot alter the approved runtime snapshot.
- [ ] O5 A local test conversation answers approved questions in the selected voice, identifies itself as automated, refuses unsupported facts and cannot bypass server policy or follow malicious FAQ instructions.
- [ ] O6 Owner can complete the page and review preview on desktop/mobile; audit/privacy, stale-update and end-to-end save/approve/read tests pass.

Baseline: **0/6 accepted = 0% onboarding acceptance**. This is not 0% existing infrastructure: tenant creation and settings are reusable. A checkbox requires complete evidence plus owner acceptance; implementation or mock preview alone is not runtime answering acceptance.

## Next proposed milestone and stop condition

S0 Organization setup precedes S1 customer intake: one fictional organization → facts/rules/FAQ/voice draft → authorized approval → local answer preview using approved snapshot → unknown question becomes human handoff. First select/map its implementation ownership in governance; do not silently enlarge APP-013 or start APP-033. Then size the smallest complete page/API/approval/preview slice against existing auth and policy contracts. Stop at local review-ready evidence, with production and paid model/provider calls disabled.

Full pilot still requires phone/SMS/web chat, payment/booking, communications, dispatch, technician progress and operational readiness. S0 is an explicit missing setup prerequisite, not permission to restart completed foundations.
