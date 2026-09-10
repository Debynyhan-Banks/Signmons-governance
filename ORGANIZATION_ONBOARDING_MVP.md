# Organization onboarding MVP — 2026-09-10

## Approved local payment-policy prerequisite (2026-09-10)

Explicit user approval added local owner/admin fixed-USD policy draft/approval and reviewed-job snapshot attachment, backend b61bb55. It is a separate policy source from FAQ/brand prose, preserves webhook validation and fail-closed behavior, and never charges or books. New controllers remain unregistered in production; system-wide adoption and existing-job repricing remain gates. Evidence: backend evidence/APP-013/organization-payment-policy/README.md. This supports O2 but does not establish full canonical routing/booking consistency or formal acceptance; onboarding remains 3/6 local and 0/6 accepted.

## Local journey connection (2026-09-10)

Approved profile facts now feed a demonstrated local customer submission → separate operator review/approval → one CREATED job browser path. See GLOBAL_EXECUTION_POINTER.md and backend evidence/APP-013/browser-review-admission/README.md. Production identity, live AI and provider actions are not accepted; no onboarding denominator or formal acceptance changes. Retain 3/6 = 50% locally demonstrated and 0/6 accepted. Older setup-only descriptions below are historical checkpoints.

## Organization setup slice (2026-09-10, latest review-ready)

Completed the owner-approved S0 page/API slice within the explicitly amended APP-013 steel-thread dependency. Company facts, greeting/tone and sourced FAQs save to a tenant-scoped draft; exact saved-version approval preserves a separate approved snapshot; deterministic FAQ or human-contact fallback preview uses only that snapshot. Source routes are registered and the root sandbox links to /app/organization; nothing is deployed. No runtime AI, customer-journey/job connection, canonical policy changes or provider calls. Details and exact commands: backend evidence/APP-013/organization-setup/README.md; governance DATA_CONTRACTS.md.

Validation: 1511 backend tests (19 new), 170 UI tests, lint/build/architecture/Prisma and four clean dependency audits. Seven local database/browser proof groups cover concurrency, audit rollback, tenant/role refusal, draft/approval separation, desktop/mobile and stale-save recovery. Fixture identity is explicitly substituted, not production Firebase acceptance. Temporary databases removed; cleanup query empty. No migration/package changes. Profile facts do not configure scheduler timezone or replace payment/routing policies; manual consistency review is still required. Exact-match preview is not semantic AI or automatic human-task creation.

Progress: onboarding 3/6 = 50% locally demonstrated outcomes (O1/O3/O4), 0/6 = 0% formally accepted. APP-013 recorded scope coverage remains 50%, formal acceptance 0/12 = 0%; pilot acceptance 0/12 = 0%. These are distinct denominators, not an engineering ETA. Next after owner review: connect the approved organization snapshot to the protected customer intake/operator request-to-job path, preserving tenant/revision authority and no external actions. Full steel thread is not complete. APP-013 stays sole Now; Next empty; FE-014 paused. No merge/deploy, production migration, IAM/secrets/billing, real-data/provider or charge authority.

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
