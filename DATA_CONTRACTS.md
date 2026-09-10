# Data Contracts

## Local address draft connection (2026-09-10, latest review-ready)

Backend checkpoint 8a0178a on codex/app-013-transactional-messaging, PR #21; incremental c5e4f6d..8a0178a. Exact review and reproduction: backend evidence/APP-013/address-draft/README.md.

Selected fictional address and customer-stated unit now enter the existing read-only draft preview, sourced server-side and checked against the exact active session, address revision, candidate/query/unit and current catalog/service-area fingerprint before and after preview. UNKNOWN and OUT_OF_AREA remain visible snapshots, not permission. Local address mode hides/guards submission; existing admission and verification blockers are unchanged.

Contract: optional addressSelection on POST /customer-session/draft contains exactly candidateId, query, revision and unit, requires explicit fixtureLoopback and injected address port. The original draft request remains unchanged without that field. Local address action review uses the existing eight-field envelope and reads without mutation/audit. Response localAddress is fixtureOnly with address/booking/delivery authority false. Joined address must satisfy the existing draft length bound. Separate read transactions provide a snapshot, not atomic admission or continuously current policy; any later consumer must revalidate. APP-013 owns replacing this fixture seam under a separately approved proof-transfer contract.

Evidence: eight new transport cases; 1731 backend tests passed / three existing skips; build/lint/architecture/Prisma/syntax/diff checks and two zero-finding audits. Eleven-group address browser/database summary, desktop/mobile screenshots and parent regression passed; disposable database removed. Address fixture uses real address/session/database/transport but scripted transcript preview; parent separately covers real continuation preview. No production/live acceptance claimed.

No schema/package/migration, production registration, provider configuration, real data, master address/job creation, booking/send permission, billing, charges, merge or deployment. Unit remains customer-stated; pg deprecation and real provider/cost/retention/recovery decisions remain open.

Stop for review. Next proposed bounded connection: retain the explicitly non-authoritative local snapshot in the existing saved operator-review handoff with fresh revision/policy checks, without clearing verification blockers or changing job admission. This is not approval to implement the proposal or release. APP-013 sole Now; Next empty; FE-014 paused. APP-013 50% recorded scope / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted, not 0% built. No defensible overall engineering percentage or ETA.

## Local address selection and coverage (2026-09-10, prior checkpoint)

Implemented optional local customer address suggestions, explicit candidate/unit confirmation and separate configured ZIP coverage using encrypted session state and existing active ServiceArea rows. Exact revision/replay, atomic audit, and whole-area/catalog fingerprint checks refuse stale selection or configuration. Missing/inactive/malformed/unsupported geography is UNKNOWN; explicit valid nonmatch is OUT_OF_AREA. Existing routing fallback is unchanged.

Evidence: backend evidence/APP-013/address-journey/README.md, eight-group browser/database summary and mobile/desktop/UNKNOWN screenshots. Fourteen new policy cases; full backend 1723 passed / three existing skips; build/lint/architecture/Prisma/syntax and two clean audits. Real audit rollback, concurrent correction once, forged session/tenant refusal and policy insertion invalidation tested; parent regression retained. Disposable database removed.

Fictional catalog only; no provider, production registration, schema/package/migration, master-address/job creation, real data, booking/send authority, billing, charges, merge or deployment. Selected address remains separate from the customer-stated draft; unit is not independently validated. Result is a snapshot, not live geographic authority. Existing pg warning and production recovery/retention/provider decisions remain open.

Stop for review. Next proposed connection: carry selected fictional address/unit into local draft review with exact revision and current policy revalidation, without real verification or admission/booking authority. APP-013 sole Now; Next empty; FE-014 paused. APP-013 50% recorded scope / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No defensible overall engineering percentage or ETA.

## Address and service-area source map (2026-09-10, prior checkpoint)

Completed the approved inspect/map section; see ADDRESS_COVERAGE_CONNECTION.md (repository-root path). Current structured address fields are placeholders in protected admission; CustomerCoverageCheck has no application consumer found under src. Existing active ZIP configuration is reusable, but routing's no-rule covered:true fallback and formatted-text ZIP extraction cannot establish validated customer service coverage. No routing behavior changed.

Next proposed implementation is one connected local address suggestion/selection/confirmation and explicit configured-ZIP coverage result in the existing customer journey, using fictional injected data and session-scoped evidence. Address/unit and area-policy changes invalidate stale results; missing geographic authority remains UNKNOWN. No new provider, master-address backfill, job/admission mutation or booking/send permission. The $50 phone budget does not authorize address-provider spend.

Backend evidence: evidence/APP-013/address-coverage-map/README.md. Documentation-only audit at backend 77c2744 / governance b37ae9b, following remote refresh. Existing backend 1709 tests passed / 3 skipped; build/lint/architecture/Prisma passed. No runtime/UI changes, new browser QA or provider acceptance claimed. No merge, deployment, migration, live calls, charges, real data, IAM/secrets or billing.

Stop for review of the source map and six local acceptance cases before implementation. APP-013 sole Now; Next empty; FE-014 paused. APP-013 50% recorded scope / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No defensible overall engineering percentage or ETA.

## Local customer verification journey (2026-09-10, prior checkpoint)

Connected the approved consent/budget controls to the existing optional local customer page: trusted test notice and unchecked acknowledgment, exact-number binding, mocked START/CHECK, wrong/correct code, lost-response exact retry, correction invalidation and draft-preserving refusal. Local-only POST /customer-session/verify reuses the existing origin/session/tenant/request-budget boundary and requires explicit fixture binding and port injection. All phone/booking/delivery authority remains false.

Evidence: backend evidence/APP-013/verification-journey/README.md, seven-group verification-journey-summary.json and desktop/mobile/refusal screenshots. 11 new unit cases; full backend 1709 passed / 3 existing skips, lint/build/architecture/Prisma/syntax checks and two zero-finding audits. New browser helper uses real session/durable/budget services and mocked Verify adapter, scripted surrounding reply, two START/two CHECK invocations, zero live calls and no new jobs. Parent organization/admission/browser/local-phone/durable-budget regression also passed; disposable database removed.

The exported notice matches the saved fixture consent copy; example.test Terms/Privacy are placeholders, not production legal acceptance. Unknown outcomes permit only exact retry; correction does not erase saved requests or refund costs, and replacement verification within the session remains unavailable. $50 ceiling/$25 and $40 threshold policy unchanged; fictional $25 flow prices only, no settlement/monthly replenishment or alert delivery implemented. No production registration, schema/package/migration, provider configuration, live spending/sending, billing, real data, merge or deployment.

Stop for owner review. Next proposed MVP section: inspect/map existing address-validation and service-area evidence into the same customer journey, reusing current contracts; no provider setup or live calls. Phone live activation still needs approved real rate/account/service binding, legal notice, reconciliation/retention, shared abuse controls, recovery, alerts and separately approved capped testing. Application proof transfer remains open.

APP-013 sole Now; Next empty; FE-014 paused. APP-013 50% recorded scope / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted, not 0% built. No defensible overall engineering percentage or ETA.

## Approved verification budget and opt-in (2026-09-10, prior checkpoint)

Owner approved a $50 USD per-organization monthly verification ceiling, internal alerts at $25/$40, explicit approval for higher limits, and no automatic cost-bearing starts beyond the ceiling. This is an internal phone-verification safeguard, not a customer charge, paid-plan entitlement, approved live spend or guarantee of profitability. Review actual usage, conversion and subscription economics after the first pilot month.

Implemented one inactive consent/budget admission connection before durable verification invocation. Explicit request and trusted notice version are bound to session/phone digest; shared tenant lock and atomic audit reserve the fictional whole-flow upper bound before START. CHECK uses the original held reservation; exact replay does not reserve twice. Missing opt-in/pricing or insufficient balance refuses. Unknown outcomes retain cost; approved provider outcomes grant no application authority.

Proof is fixture-only, with $25/$30 fictional whole-flow costs for boundary tests, never actual provider prices. Current model uses USD integer micro-units and UTC month labels. All reservations remain HELD, including older-month liabilities; there is no settlement, release or automatic monthly reset yet. Alert threshold crossings are recorded, not delivered. No production rate source, provider binding, configurable override UI or real customer consent UI is claimed.

Evidence: backend evidence/APP-013/verification-budget/README.md and fourteen-group database summary. Full backend 1698 passed / 3 existing skips; 22 new tests, lint/build/architecture/Prisma and two zero-finding audits. Existing browser regression and disposable PostgreSQL concurrency/rollback proof passed; database removed. No new UI, module registration, schema/package/migration, provider configuration, live sending/spending, billing, real data, merge or deployment.

Stop for review. Next bounded outcome: connect the explicit notice/code request and budget-refusal states to the existing local customer journey using mocked verification, not another disconnected backend slice. Before live activation, finish rate/account/service binding, reconciliation/retention and abuse controls, alert delivery, customer recovery and separately approved capped testing. Address/coverage and admission proof transfer remain open.

APP-013 sole Now, Next empty, FE-014 paused. Progress unchanged: APP-013 50% recorded scope / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No defensible overall engineering percentage or ETA.

## Durable verification reservation and observation (2026-09-10, prior checkpoint)

Implemented inactive session-bound reserve/invoke/finalize around the Verify adapter, with no transaction spanning the mocked provider call. Encrypted bounded ledger and atomic audits preserve attempt identity. Exact replay returns the saved result or unresolved reservation without invoking again; changed payload refuses. Check SID comes from the matching saved start, not the customer. Failed finalization retains unknown invocation count and UNRECONCILED potential cost; no automatic reservation reclaim or resend.

Evidence: backend evidence/APP-013/durable-verification/README.md and nine-group database summary. 18 new unit tests; full backend 1676 passing / 3 existing skips; lint/build/architecture/Prisma, two clean backend audits and existing full browser regression passed. Disposable database removed. No new UI, actual delivery, process-kill or reconciliation claim; all authority flags remain false and local phone fixture stays separate.

One START/five CHECK local bound is not a production budget. Reserve/observe audit rows share attempt ID and must not be counted twice. Rate/account/service binding, OTP opt-in, shared traffic limits, monetary cap, recovery and admission proof transfer remain open. Next after review: durable verification opt-in and usage-budget admission prerequisites, mocked/inactive; no live sends or configured costs. No schema/package/migration, production registration, real data, merge/deploy, IAM/secrets/billing or charges.

APP-013 sole Now, Next empty, FE-014 paused. Progress unchanged: APP-013 50% scope coverage / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No overall engineering ETA.

## Inactive Verify adapter and cost boundaries (2026-09-10, latest review-ready)

Owner approved the Twilio recommendation and requested competitive/profitable pricing awareness. Implemented one unregistered injected-client adapter: strict tenant/account/service/phone/SID binding, SMS start/check mapping, sanitized outcomes and no automatic retries. APPROVED is provider evidence only; all application authority flags remain false. No live client/configuration, provider calls, UI/route/persistence changes, secrets, billing or charges.

Evidence: backend evidence/APP-013/twilio-verify-adapter/README.md. 42 new tests; full backend 1658 passed / 3 existing skips, lint/build/architecture/Prisma and two clean backend audits. Installed SDK tested with network-free HTTP client; maxRetries:0 defaults to 3, so autoRetry:false is the effective guard. No new browser/UI QA claim; none required for inactive adapter-only change.

Usage output records attempted SDK calls and UNRECONCILED billing, not billable SMS or implemented cost enforcement. VERIFICATION_UNIT_ECONOMICS.md defines per-tenant/cohort costing, versioned rate inputs, failure/retry attribution, reconciliation and margin-planning requirements without setting prices or margins. Missing cost is unknown, not zero.

Stop for review. Next bounded connection: durable request reservation/finalization and deduplicated usage observations using mocked provider outcomes. Opt-in, spend circuit breaker, recovery, live activation and admission transfer remain gates. APP-013 sole Now, Next empty, FE-014 paused. Percentages unchanged: APP-013 50% scope / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No overall engineering ETA or production authority.

## Phone verification provider recommendation (2026-09-10, latest review-ready)

Completed the bounded provider/source review. Recommend Twilio Verify v2 provider-generated SMS codes, subject to owner review; see PHONE_VERIFICATION_PROVIDER_DECISION.md for official sources, comparison, costs, recovery and activation gates. Existing SDK supports create/check; no dependency or account change needed for an inactive adapter. Critical differences from fixture: provider default 10-minute code, same-code resend, ambiguous 404 after approval/expiry/exhaustion, explicit OTP opt-in, and no Verify support in standard test credentials.

Next after review: inactive injected-client Verify adapter and contract tests, with no production registration, provider calls or secrets. Durable network reservation/finalization and authenticated recovery must follow before real-recipient acceptance. No provider configuration, live sends, charges, real data, IAM, billing, merge or deployment authorized. Directory plugin was unavailable; official-document fallback used without installation.

Documentation only, no new runtime/acceptance claim. APP-013 sole Now, Next empty, FE-014 paused. Progress unchanged: APP-013 50% scope coverage / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No overall engineering ETA.

## Local phone-code journey (2026-09-10, latest review-ready)

Implemented the approved first local phone slice: request/check/resend/clear/status in the existing fictional customer browser, encrypted durable session-bound state, exact version/retry handling, atomic audits and database-backed per-destination request/attempt limits. Explicit number change revokes prior test proof without staff verification. Lost-response retry writes once. Deterministic code 123456 is a labeled fixture; FIXTURE_VERIFIED never grants phoneAccessAuthorized, bookingAuthorized or deliveryAuthorized. No job verification flag or admission authority changes.

Evidence: backend evidence/APP-013/local-phone-verification/README.md, ten database proof groups, browser summary and mobile/desktop screenshots. 1616 backend tests (18 new), 170 UI tests, lint/build/architecture/Prisma, four clean audits and full local browser/database proof passed. Initial sandbox socket refusal and advisory-lock void-result issue were resolved and final gates passed; existing toolchain/pg warnings remain. Fictional database removed; original dirty checkouts preserved.

Local QA policy only: 5-minute challenge, 10-minute test proof capped by session, 30-second resend cooldown, 3 requests/5 checks per session and per tenant/destination over one hour. No approved production thresholds or provider semantics inferred. Optional transport is fixture-only, with no module/controller registration, package/schema/migration changes or live sending. No provider, real data, merge/deploy, IAM/secrets/billing or charges.

Stop for review. Next is the real verification provider contract/selection and activation plan, not silent activation; define actual delivery/check semantics, costs, limits and channel behavior before production evidence or admission transfer. Address/coverage and existing human-reviewed admission remain distinct unfinished connections. APP-013 sole Now, Next empty, FE-014 paused. Progress unchanged: APP-013 50% scope coverage / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No overall engineering ETA.

## Automated verification contract mapping (2026-09-10, latest)

Completed the approved source audit; see AUTOMATED_VERIFICATION_CONNECTION.md. Existing Twilio transport is not customer OTP; intake address fields are placeholders, not validated locations; routing fallback is not coverage proof. Proposed first implementation is a connected local customer phone request/check/resend/correction flow with durable session-bound evidence and no live sending. Provider contracts, explicit expiry/abuse policy and the later admission proof transfer remain to be resolved. Existing operator admission is not silently removed.

Documentation only; no runtime or acceptance change. APP-013 sole Now, Next empty, FE-014 paused. Progress remains APP-013 50% recorded scope / 0 of 12 accepted, onboarding 50% local / 0 of 6 accepted, pilot 0 of 12 accepted. No provider activation, charges, real data or release. Stop at mapping review before implementation.

## Approved automated verification MVP decision (2026-09-10, current)

Owner approved an automated normal verification path: phone one-time code, address autocomplete/validation, automatic configured service-area checks and existing verified-payment/availability gates. Mandatory operator contact/address confirmation is superseded; human help is for exceptions. Phone access is not identity, payment is not verification, and neither grants messaging consent. Existing human-reviewed admission is not silently removed. Current requirements, acceptance cases and approval boundaries: CALLDESK_MVP_PLAN.md, section "Approved automated verification MVP decision".

Documentation only; implementation and provider acceptance remain open. Next is to inspect/reuse contracts and bound the automated connection, including expiry, retry, abuse controls and invalidation on changed details. No provider selection/configuration, live code sending, charges, production action or release authorized. APP-013 sole Now, Next empty, FE-014 paused. Percentages unchanged: APP-013 50% scope coverage / 0 of 12 accepted; onboarding 50% local / 0 of 6 accepted; pilot 0 of 12 accepted. No overall engineering ETA.

## Local reviewed preferred service window (2026-09-10)

Unregistered POST /preferred-window-review/save accepts exactly jobId UUID, canonical expectedUpdatedAt, trimmed preference (1–500 plain-text characters; no control/format characters or unknown/not-provided placeholders), acknowledged:true. Verified non-impersonated owner/admin/dispatcher and active tenant supply actor/scope. Shared tenant lock then job lock; exact undeleted CREATED human-reviewed job, no payment record, Calendar history or scheduling fields. Unknown/foreign/advanced state refuses.

Atomically update preferredTimeText, clear preferredWindowLabel and add policySnapshot.preferredWindowReview {version:1,actorId,digest,expectedUpdatedAt,updatedAt,source:CUSTOMER_STATED_OPERATOR_REVIEW,availabilityChecked:false}; USER audit uses that metadata without preference text. Preserve other policy/pricing, status, serviceWindowStart/End and calendarEventId. Source text is customer-stated and operator-reviewed, not independently verified or parsed into availability. Current exact same-actor/version/text replay returns original receipt without another write; fresh-version corrections produce a new review/audit. Stale/different actor or advanced job refuses. Previous exact-version payment/admission commands are not silently rebased.

Receipt: jobId, updatedAt, preference, source, availabilityChecked:false, bookingAuthorized:false, deliveryAuthorized:false. Authorized private readiness projection additionally returns preferredServiceWindow; removal of the missing preference blocker never establishes a booking. UI edits reset acknowledgment, freezes uncertain pending input for explicit retry, clears private state and reloads readiness after save. New route/service are local-only; no provider, payment, booking, confirmation, production registration or schema changes. Evidence: backend evidence/APP-013/preferred-window-review/README.md.

## Approved local payment policy and job binding (2026-09-10)

Explicit owner-approved prerequisite, not inferred policy authority. TenantOrganization.settings.organizationPaymentPolicyV1 is {version:1,draft,approved:null|{draft,actorId,approvedAt}}; tenantId comes from verified context and tenant updatedAt provides optimistic versioning. Draft fields exactly currency:usd, serviceFeeRequired:boolean, serviceFeeCents:positive integer|null, depositRequired:boolean, depositPolicy:{kind:none}|{kind:fixed,amountCents:positive integer}, emergencyFeePolicy:{kind:none}, paymentGateMode:fail_closed, webhookValidationRequired:true. Required amount range 1..100000000 cents; disabled fee must be null and disabled deposit none. No manual overrides, percent deposits, emergency surcharge or non-USD policy in this slice. This is the local fixed-policy subset of the conceptual PaymentPolicy contract below.

Unregistered GET/PUT /organization/payment-policy and POST /organization/payment-policy/approve: active-tenant owner/admin without impersonation. Save exactly expectedUpdatedAt/draft; approve exactly expectedUpdatedAt/acknowledged:true. Validate stored envelopes, preserve other settings and approved snapshot on draft edits; conditional tenant update and privacy-safe audit commit atomically. Approval snapshots have a monotonic ISO approvedAt identity; not merely an incremented UI flag.

Unregistered POST /job-payment-policy/apply input exactly jobId, expectedUpdatedAt, approvedAt, acknowledged:true. Owner/admin only. Shared tenant lock then job lock; current approved identity/digest, exact CREATED undeleted human-reviewed job, no existing terms/pricing/payment/scheduling/Calendar history. Attach gate flags and USD pricing (serviceFeeAmountCents,depositAmountCents,currency), preserving other policy fields. paymentPolicyBinding holds version:1, actorId, approvedAt, digest, expectedUpdatedAt, updatedAt and canonical approved draft snapshot. No preferred-window, verification, booking/status or payment mutation. Job update and audit atomic.

Exact same-actor/input replay requires unchanged job version, matching bound terms/pricing and still-current approval; returns same receipt with policyBound:true, paymentInitiated:false, bookingAuthorized:false, deliveryAuthorized:false. Existing terms, reprice/replacement, changed approval, any payment/scheduling history refuse. New approval never silently updates prior jobs. Job/history recovery after supersession and system-wide adoption by existing creation paths require separate review. Local UI uses explicit saved-policy and job acknowledgments, memory-only state and exact pending retries; these controls grant no production activation or charge authority. Evidence: backend evidence/APP-013/organization-payment-policy/README.md.

## Local CREATED-job booking readiness (2026-09-10)

Unregistered POST /booking-readiness/preview accepts exactly jobId UUID. Identity/tenant guards, sanitized private/no-store responses; service requires non-impersonated owner/admin/dispatcher and active tenant. In a repeatable-read PostgreSQL READ ONLY transaction, load undeleted tenant job/customer with tenant-correct address/category/payment and refuse non-CREATED states. Reuse intake snapshot assessment without transcript/history reads or audit writes and existing payment-gate evaluator; count unfinished Calendar operations. No provider/cipher/customer token dependency.

Return jobId, jobUpdatedAt, CREATED status, snapshotOnly:true, assessment BLOCKED or REQUIRES_BOOKING_VALIDATION, blockers, payment state/reason, confirmation UNAVAILABLE/eligible:false/APPOINTMENT_NOT_FINALIZED with explanatory text, bookingAuthorized:false and deliveryAuthorized:false. Both depositRequired and serviceFeeRequired must be explicit booleans before payment state is known. Otherwise UNKNOWN/PAYMENT_POLICY_UNRESOLVED regardless of the legacy evaluator's missing-policy fallback. This is diagnostic conservatism, not a new booking/payment policy or verification mechanism. Missing intake facts and human review, unverified contact/address and unfinished Calendar operations block. A clean diagnostic does not establish current policy, pricing, service area, availability or booking authority.

No confirmation content is fabricated for an unbooked job. Existing finalized-event/recipient/current-consent/mailbox/expiry checks remain required and are not bypassed. Operator fixture opens the newly admitted job in memory, uses readable labels and clears stale/error/identity-change state. No general history or post-reload job recovery added. Details and executable proof: backend evidence/APP-013/booking-readiness-preview/README.md. No schema/module/production activation.

## Local browser submission and operator decision transport (2026-09-10)

Inactive same-origin customer transport adds POST /customer-session/submit with exactly sessionToken, requestId, expectedRevision, draft, confirmed:true. Existing origin/Fetch Metadata/marker/content/body/budget and integration-scope checks apply. Optional review port must exist; validates seven-field draft, UUID/revision and rechecks credential expiry. Response projects only requestId, state:PENDING_REVIEW, original expiresAt, jobCreated:false, bookingAuthorized:false, deliveryAuthorized:false.

Customer fixture enables submission only under explicit local data-review-submit composition, after read-only preview. Exact pending request is retained through uncertainty; customer sees a reference and original deadline. This is submission authority, not job creation.

New unregistered CustomerIntakeReviewController exposes local POST /intake-review-request/read and /approve, delegating unchanged exact service contracts below. RequestAuthGuard and TenantGuard plus sanitized private/no-store errors; explicit fixture guard substitution in the proof is not production identity acceptance. No production module registration or shared rate-limit activation. Operator fixture holds its own bearer only in memory, loads by reference, displays draft/version/deadline and requires urgency plus acknowledgment before approval. Exact decision is locked across uncertainty and retried only by explicit action. Reload/clear loses private retry state without undoing committed work. Closed read returns refusal, not an admitted-status lookup. UI directs human history review; automatic renewal/replacement and post-expiry recovery are not implemented.

Browser proof: separate customer/operator contexts, server-side lost-response injection after commit on both operations, one CREATED job, no customer credentials in operator requests, role/foreign/closed refusal, no storage, mobile fit and no page errors. No booking/delivery authority or external provider action. See backend evidence/APP-013/browser-review-admission/README.md.

## Token-free durable review admission (2026-09-10, unregistered local method)

admitReview accepts exactly requestId (UUID), expectedOrganizationApprovedAt (canonical ISO), review {urgency:EMERGENCY|HIGH|STANDARD,reasonCode:OPERATOR_REVIEWED_INTAKE,acknowledgeCustomerStatements:true}. Trusted non-impersonated owner/admin/dispatcher context supplies tenant/actor. No customer token verification, issuance or reconstruction; no input draft/customer/tenant/actor override. Existing customer-submitted encrypted review is the only draft source. Legacy scripted/unbound reviews cannot enter this organization-bound path.

Reread the durable review under shared tenant/session locks; require original unexpired deadline, active scope, current approved organization version and exact bound transcript/draft. An existing tenant category is required. Shared persistence atomically writes customer/address, CREATED job, CREATED_FROM link, optional immutable consent association, privacy-safe audit and COMPLETED/JOB_CREATED conversation. Job policy intakeAdmission retains version:1 for existing projection compatibility and adds requestId, organizationApprovedAt, organizationDigest; its opaque digest is computed from a version-2 admission input including request, tenant/actor, transcript/draft, human review and organization binding. Existing event remains unchanged; policy/audit link is the durable outcome, not a new request-state row or database FK. Final deadline check can roll back all writes.

Return requestId, state:ADMITTED, organizationApprovedAt plus existing admission receipt fields (jobId,status,urgency,transcriptRevision,humanReviewed:true,consentEvidence:BOUND|NOT_RECORDED,jobCreated:true,bookingAuthorized:false,deliveryAuthorized:false). Historical grant/decline/revoke association never means current send authority. No evidence is permitted as NOT_RECORDED.

Exact same-actor/decision/request replay may return the recorded still-CREATED, undeleted job only within the original deadline, with matching approval, urgency, digest and link/consent outcome. Changed actor/decision/version, expired state or advanced job refuses rather than creating another job. Pending readReview still refuses after conversation close; this is not a general admitted-status API or post-deadline recovery mechanism. Shared helper preserves legacy admitDraft customer-token checks. No production route/module/UI, schema, migration, provider or release change; future UI must expose uncertainty honestly and not resubmit as a fresh request.

## Approved organization-bound intake turns (2026-09-10, inactive local connection)

continueOrganization accepts exact sessionToken/interactionId/message, with existing credential/message bounds and no caller-selected tenant, profile or history. Under shared tenant/session locks it loads only the active tenant's validated approved organizationProfileV1. Deterministic exact FAQ match or approved fallback is used; no collaborator/model/tool call. Tabs/newlines are normalized only for FAQ matching, not stored input. Draft-only organization edits do not affect the approved snapshot. Final encrypted turn commit rechecks the approved snapshot digest under the shared tenant lock.

protected_intake_turn_v1 payload version 2 adds exact organizationApprovedAt (canonical ISO approval timestamp) and organizationDigest (SHA-256 of canonical validated approved snapshot) to existing sessionId/revision/encryptedInput/encryptedReply/type/version. Legacy version 1 remains readable only in scripted mode; all turns in organization mode must be version 2 and agree on the still-current approval. Missing/malformed/new approval, mixed history or attempted mode switch refuses. Reapproval with the same facts but a new approval identity also invalidates the old session. No automated rebase, renewal or recovery; original expiry remains.

Existing review request version 1 retains transcriptDigest covering the bound turns. submitReview and readReview validate current organization-bound history; readReview adds organizationApprovedAt without exposing a customer bearer, organization facts or digest. Operator read remains nonmutating, no credential methods and no job authority. Exact turn replay is allowed only while original session/history/approval remain valid. All source profile facts stay inert and cannot override booking/payment/category/consent policy. This does not connect the live tenant runtime to the new profile.

No production transport/module/UI registration in this slice. Local fixture uses existing protected browser transport with continueOrganization as its continuation port. Service-level submission/read are not browser action acceptance. Older readers refuse version-2 turns; any future deployment requires explicit version-compatibility review. Next request-to-job admission must preserve organization binding and stale-state refusal; no job/consent outcome is added here.

## Organization setup profile v1 (2026-09-10, source registered; not deployed)

GET/PUT `/organization/profile` and POST `/organization/profile/approve` or `/preview` require existing RequestAuthGuard/TenantGuard plus service-verified non-impersonated owner/admin of an active tenant. Tenant/actor authority never comes from the body. Private/no-store responses and existing sanitized error filtering apply.

PUT exact body: expectedUpdatedAt (canonical ISO timestamp), draft. Draft exact fields: companyName (120), timezone (80, valid Intl timezone), hours/services/fallback (500 each), greeting (200), tone warm|concise, faqs (1–10). FAQ exact fields: question (200), answer (1000), source (200). Text is trimmed, nonempty and excludes controls; question matching is case-insensitive exact text after trim; duplicate questions refuse. Descriptive timezone/services/hours are not changes to canonical tenant timezone, routing, scheduling, payment or cancellation policy. No automatic conflict comparison.

TenantOrganization.settings.organizationProfileV1 contains version:1, draft, approved:null or {draft,actorId,approvedAt}. Existing settings are preserved. Write compares the exact tenant updatedAt and updates the JSON plus a strictly increasing updatedAt and privacy-safe USER audit in one transaction. Approve exact body is expectedUpdatedAt + acknowledged:true and copies the saved draft, not client content. Draft edits preserve approved content. Audit records action/version/timestamps/actor, not facts or FAQ text. A conflict or unknown outcome requires reload; no automatic replay/approval claim. Malformed stored profiles refuse. No new migration or immutable history archive.

Preview exact body: expectedUpdatedAt + question. Reads the approved snapshot at the observed version or refuses. Returns approvedAt, mode:DETERMINISTIC_PREVIEW, matched, requiresHumanFollowup, answer, source, actionsAuthorized:false. Unmatched questions return owner-authored contact instructions; no callback/job is created. FAQ text is inert data and never a tool instruction; owner content review still required. No live AI or customer runtime wiring. Service snapshots return runtimeConnected:false. Source routes are registered but no deployment or provider activation is authorized.

Current source/evidence: backend evidence/APP-013/organization-setup/README.md. Fixture identity is not production auth acceptance. Approved-version withdrawal/archive/retention and customer-journey binding are not implemented; further review required before live usage.

## Purpose

Define canonical request/response/event/data shapes so frontend, backend, and governance stay aligned.

## Global Contract Rules

- Contract-first: define schema before implementation.
- Backward compatibility by default.
- Breaking changes require versioning + migration note.
- Validate ingress payloads at boundary.
- Persist canonical IDs for lead/demo/job flows.

## FE-007 Marketing Lead Capture Contract (Required)

Endpoint:

- `POST /api/marketing/lead-capture`

Request body:

- `email` (required, string, normalized lowercase)
- `firstName` (optional)
- `lastName` (optional)
- `businessName` (optional)
- `phone` (optional, E.164 when provided)
- `industries` (optional, string[])
- `callsPerWeek` (optional, enum/string)
- `notes` (optional)
- `consentToContact` (required, boolean)
- `consentTextVersion` (required, string)
- `utm` (optional: source/medium/campaign)
- `referrerUrl` (optional)

Success response (`202` or `201`):

- `leadId` (required)
- `status` (required: `accepted` | `queued`)
- `createdAt` (required, ISO-8601)

Validation error (`400`):

- `errorCode` (required)
- `message` (required)

## FE-008 Try-Demo Contract (Existing, Retained)

Endpoints:

- `POST /api/marketing/try-demo`
- `GET /api/marketing/try-demo/:leadId`
- `POST /api/marketing/try-demo/status`

Required invariants:

- `leadId` returned from submit is pollable on status endpoint.
- Status transitions are deterministic and auditable.

## Persistence Contract

`marketingLead` is canonical storage for both:

- contact-capture leads,
- try-demo leads.

Required persisted fields for FE-007 minimum:

- `id`, `email`, `consentToContact`, `consentTextVersion`, `createdAt`

## Business Rules Source Of Truth (Locked)

- Source of truth: **DB config**.
- JSON is allowed only as onboarding template seed.
- UI form builder is a management layer over DB config (not the source of truth).

## Scheduling + Calendar Contract (Locked)

- Google Calendar integration is a hard MVP requirement.
- Scheduling payloads must carry timezone and preferred window.
- Booking creation must record calendar sync result status.

## Emergency Fee Policy Contract (Locked)

Emergency fee behavior is conditional by:

- trade/category,
- time window.

Required policy output shape:

- `isEmergency` (boolean)
- `emergencyFeeApplied` (boolean)
- `emergencyFeeCents` (number)
- `reasonCode` (string)

## Tenant Brand Voice Contract (Locked)

Per-tenant single voice profile:

- `brandTone`
- `greetingStyle`
- `forbiddenPhrases`
- `escalationLanguage`

## Dispatch Mode Contract (Locked)

- Starter: manual dispatch
- Growth: recommended dispatch
- Pro/Enterprise: optional auto-dispatch

Decision payload must include:

- `mode`
- `recommendedAssigneeId` (nullable)
- `reasonCodes` (string[])

## KPI Contract (Top 5 MVP)

1. `leadToBookingRate`
2. `paymentLinkCompletionRate`
3. `missedCallRecoveryRate`
4. `emergencyCaptureRate`
5. `firstResponseLatencyP95Ms`

## Verification

- Contract tests for FE-007 and FE-008 endpoints.
- CI validation for route/CTA/API mapping docs.
- Evidence in ticket completion notes.

## BE-003 Server-to-Server Webchat Triage Contract

Endpoint:

- `POST /api/integrations/webchat/triage`

Authentication and tenancy:

- The tenant website calls its own server-side proxy; browser code never receives the Signmons credential.
- The proxy sends `Authorization: Bearer <integration secret>` over HTTPS.
- Signmons stores only a SHA-256 credential hash in configuration and resolves `tenantId` from the matched credential.
- The request body cannot supply or override `tenantId`.

Request body:

- `sessionId` (required, 4–64 safe identifier characters)
- `message` (required, 1–1000 characters after normalization)

Reply response:

- `status: "reply"`
- `reply` (string)

Life-safety response:

- `status: "safety_escalation"`
- `reply` (deterministic emergency guidance)
- `requiresHumanHandoff: true`
- `emergencyServicesRecommended: true`

Tool response:

- Existing tenant-scoped `job_created` response may be returned only after required fields validate and the configured tool budget permits it.

Contract rules:

- The assistant must disclose that it is automated and is not a technician.
- It must not diagnose equipment, promise an appointment or arrival, publish a fee, or upsell unless an approved tenant policy expressly allows that behavior.
- Gas odor, carbon monoxide, fire, smoke, sparks or immediate electrical danger must be intercepted before the AI provider is called.
- Rate limits apply per resolved integration tenant.
- Direct browser CORS access is not part of this contract.

## BE-007 Tenant Lead-Source Report Contract

Endpoint:

- `GET /reports/lead-sources?from=<ISO-8601>&to=<ISO-8601>`

Authentication and tenancy:

- Firebase bearer authentication is required in production.
- The authenticated tenant claim is authoritative; the request cannot supply or override `tenantId`.
- Only `owner`, `admin` and `manager` roles may read the report.

Date rules:

- `from` is inclusive and `to` is exclusive.
- Both values must be valid ISO-8601 timestamps with explicit timezone offsets.
- `to` must be later than `from`; the range may not exceed 366 days.

Response:

- `period`: normalized UTC `from` and `to`.
- `totals`: raw counts for `created`, `booked`, `completed`, `cancelled`, `attributed` and `unattributed`.
- `rates`: `leadToBooking` and `bookedToCompleted`, returned with their raw denominators in `totals`.
- `bySource`: privacy-safe channel/source/medium/campaign groups with the same counts and rates.
- `topLandingPages`: normalized site paths and job counts.

Metric lineage:

- Created: `Job.createdAt` falls inside the requested period.
- Booked: accepted lineage exists (`acceptedAt`) or current status is `ACCEPTED`, `IN_PROGRESS` or `COMPLETED`.
- Completed: completed lineage exists (`completedAt`) or current status is `COMPLETED`.
- Cancelled: current status is `CANCELLED`.
- Attribution: bounded values from `Job.policySnapshot.leadAttribution`; missing values are grouped as `unattributed`.

Privacy rules:

- The report must not select or return customer names, phone numbers, addresses, free-text descriptions, conversation contents, calendar event IDs or appointment-management credentials.
- Reporting credentials must remain server-side and must never be embedded in browser JavaScript.
- Rate values are ratios from `0` to `1`, rounded to four decimal places.
- Responses use `Cache-Control: private, no-store`.

## APP-003 Audited Job Completion Contract

Endpoint:

- `POST /jobs/:jobId/complete`

Authentication and tenancy:

- Firebase bearer authentication is required in production.
- Tenant and actor identity come only from verified request context.
- The pilot permits `owner` and `admin` roles.

Transition rules:

- `ACCEPTED -> COMPLETED` and `IN_PROGRESS -> COMPLETED` are allowed.
- `COMPLETED -> COMPLETED` is an idempotent replay and does not create a second audit entry.
- Created, offered, declined, expired and cancelled jobs cannot be completed through this endpoint.
- Missing and cross-tenant jobs return the same not-found boundary without revealing another tenant's data.

Success response:

- `jobId`
- `status: "COMPLETED"`
- `completedAt` (ISO-8601)
- `changed` (`true` for the first transition; `false` for idempotent replay)

Audit rules:

- The first transition and its `AuditLog` record commit in one database transaction.
- Audit action: `job.completed`.
- Metadata may contain only the prior status and completion timestamp.
- Customer names, contact details, addresses, descriptions, calendar identifiers and management credentials are prohibited from the response and audit metadata.

## APP-007 Urgency Classification And Escalation Review Contract

Endpoints:

- `GET /jobs/urgency-review`
- `GET /jobs/urgency-review/:jobId`
- `POST /jobs/:jobId/urgency/override`
- `POST /jobs/:jobId/escalations`

Authentication and tenancy:

- Firebase bearer authentication is required in production.
- Tenant and actor identity come only from verified request context; request payloads cannot supply or override either value.
- `owner`, `admin` and `dispatcher` roles may review urgency, record authorized overrides and initiate an internal escalation.
- Missing and cross-tenant jobs return the same not-found boundary.

Urgency rules:

- Canonical urgency values are `EMERGENCY`, `HIGH` and `STANDARD`; `HIGH` must not be collapsed into `STANDARD` during persistence.
- The review response includes a concise operational rationale, trigger reason codes, the decision source and a confidence note. It must not expose hidden model reasoning or imply diagnostic certainty.
- The response includes an escalation-path preview and a chronological history of urgency overrides and escalation delivery attempts.

Override request:

- `urgency` (required: `EMERGENCY` | `HIGH` | `STANDARD`)
- `reason` (required, normalized string, 10-500 characters)

Override rules:

- The job update and `AuditLog` entry commit in one database transaction.
- Audit action: `job.urgency_overridden`.
- Idempotent same-value overrides do not create duplicate audit entries.
- Audit metadata may contain only prior/new urgency, normalized reason, decision source and timestamp.

Escalation request and result:

- An escalation request notifies the tenant's configured internal operations recipients through configured channels; customer recipients are out of scope.
- Every attempt is audit logged with action `job.urgency_escalated`, including privacy-safe channel, recipient group, outcome and timestamp.
- A configured-provider failure is returned as a recorded failed outcome and must not be presented as delivered.
- If no notification channel is configured, the request is audit logged with a `not_configured` outcome.

Privacy and safety:

- Review-list and audit responses must not contain customer phone numbers, email addresses, street addresses, full transcripts, calendar identifiers or appointment-management credentials.
- Urgency classification is an operational routing aid, not a diagnosis or emergency-services determination.

## APP-008 Dispatch Board And Technician Assignment Contract

Endpoints:

- `GET /jobs/dispatch-board`
- `GET /jobs/dispatch-board/:jobId`
- `POST /jobs/:jobId/assignments`
- `POST /jobs/:jobId/assignments/cancel`
- `POST /jobs/:jobId/escalations` (shared APP-007 operation)

Authentication and tenancy:

- Firebase bearer authentication is required in production.
- Tenant and actor identity come only from verified request context; request payloads cannot supply or override either value.
- `owner`, `admin` and `dispatcher` roles may view and operate the dispatch board.
- `tech` and `read_only` roles cannot assign, reassign, cancel assignments or initiate dispatch escalation.
- Candidate technicians and jobs must be selected within the verified tenant boundary. Missing and cross-tenant jobs return the same not-found boundary.

Board response:

- Active jobs are returned in one of `NEW_REQUEST`, `READY_TO_ASSIGN`, `ASSIGNED` or `ESCALATED`.
- `ASSIGNED` takes precedence when a job has a current technician; an unassigned escalated job is `ESCALATED`; scheduled/accepted work is `READY_TO_ASSIGN`; remaining active intake is `NEW_REQUEST`.
- Dispatch-inactive (`DECLINED`, `EXPIRED`, `COMPLETED`, `CANCELLED`) and soft-deleted jobs are excluded.
- Each summary may contain only job reference, queue, service category, urgency, status, service window, current assigned technician name/role, and timestamps.

Recommendation response:

- Recommendation version is `dispatch-v2` after APP-010 and includes a bounded `routing-v1` policy trace.
- Candidate ranking is deterministic and uses enabled service capability, proficiency, operator-maintained availability, overlapping availability blocks and active assignment count.
- A recommendation is decision support only; CallDesk does not automatically dispatch the job.
- The response exposes bounded reason codes and plain-language operational factors, never hidden model reasoning or diagnostic claims.
- Operators may select a non-recommended or otherwise ineligible active candidate only with a normalized 10-500 character override reason.

Assignment request:

- `technicianId` (required UUID)
- `expectedUpdatedAt` (required ISO-8601 timestamp used as the optimistic concurrency token)
- `reason` (optional for the current recommendation; required, normalized and 10-500 characters for reassignment or recommendation override)

Assignment-cancellation request:

- `expectedUpdatedAt` (required ISO-8601 timestamp)
- `reason` (required, normalized string, 10-500 characters)
- Cancellation clears only the technician assignment. It does not cancel or close the customer job.

Concurrency, idempotency and audit:

- Assignment writes must match both tenant and `expectedUpdatedAt`; a stale token returns conflict and creates no audit event.
- Assigning the already assigned technician is idempotent and creates no duplicate audit event.
- Job update and audit event commit in one database transaction.
- Audit actions are `job.assigned`, `job.reassigned` and `job.assignment_cancelled`.
- Audit metadata may contain only prior/new technician identifiers, recommendation version and reason codes, override flag, and normalized operator reason.

Privacy and safety:

- Board, detail, recommendation and assignment-history responses must not contain customer names, phone numbers, email addresses, street addresses, job descriptions, transcripts, calendar identifiers, payment credentials or appointment-management credentials.
- Assignment history exposes actor identifiers for internal accountability but no actor contact information.

## APP-009 Technician Mobile Job Workflow Contract

Endpoints:

- `POST /jobs/technician-links/:technicianId`
- `GET /technician/jobs`
- `GET /technician/jobs/:jobId`
- `POST /technician/jobs/:jobId/status`

Link issuance and access:

- Only authenticated `owner`, `admin` and `dispatcher` operators may issue a link for an active technician in the verified tenant.
- The credential is an HMAC-signed, versioned bearer token scoped to one tenant and one technician, with an explicit issue time, expiration and nonce.
- The token is returned only in the URL fragment so normal HTTP requests do not send it as a route or query value.
- Link lifetime is bounded to 1-168 hours; production requires a dedicated secret of at least 32 characters.
- Signature validation is constant-time and canonical. Missing, malformed, tampered, future-issued and expired links return the same unauthorized boundary.
- Every read and write revalidates that the technician remains active with role `tech` in the signed tenant.

Technician list and detail:

- A technician may read only non-deleted jobs currently assigned to their tenant-scoped user identity.
- The list groups assigned work into `today`, `upcoming` and the most recent 90 days of `completed`, using the tenant timezone.
- List summaries include job reference, service category, service address, service window, urgency, technician status, available actions and update token.
- Assigned-job detail may additionally include customer contact fields, access notes, issue summary and preferred-time text required for field service.
- Responses use `Cache-Control: private, no-store` and never expose another technician's assignments.

Status actions and transitions:

- Supported actions are `accept`, `decline`, `on_my_way`, `in_progress`, `complete` and `cannot_take`.
- `ASSIGNED` permits accept, decline or cannot-take.
- `ACCEPTED` permits on-my-way, in-progress, decline or cannot-take.
- `EN_ROUTE` permits in-progress or cannot-take.
- `IN_PROGRESS` permits complete; `COMPLETED` is terminal.
- Decline and cannot-take release only the technician assignment so dispatch can reassign the open job.
- Accept, in-progress and complete update the shared job lifecycle fields used by dispatcher workflows.

Concurrency and audit:

- Every mutation requires `expectedUpdatedAt`; a stale value returns conflict and creates no audit event.
- Replaying the already-current technician status is idempotent.
- The job write and audit event commit in one database transaction.
- Audit actions are `job.technician_accepted`, `job.technician_declined`, `job.technician_en_route`, `job.technician_started`, `job.technician_completed` and `job.technician_unavailable`.
- Audit metadata is limited to prior/new technician status, assignment-release flag and an optional normalized note of at most 500 characters.

## APP-010 Routing Rules, Service Areas, And Availability Contract

Endpoints:

- `GET /jobs/routing`
- `POST /jobs/routing/rules`
- `POST /jobs/routing/rules/:ruleId`
- `POST /jobs/routing/service-areas`
- `POST /jobs/routing/service-areas/:serviceAreaId`
- `POST /jobs/routing/technicians/:technicianId`
- `POST /jobs/:jobId/routing/evaluate`

Authentication and tenancy:

- Production requires verified Firebase operator identity. Only `owner`, `admin` and `dispatcher` roles may read or change routing configuration.
- Tenant and actor identity come only from verified request context. Rule, service-area, service-category and technician identifiers are resolved inside that tenant boundary.
- Missing and cross-tenant resources use the same not-found or invalid-reference boundary.

Routing configuration:

- A routing rule has a tenant-scoped name, active state, deterministic integer priority, optional service category, optional service area, optional urgency, time scope, availability/on-call requirements and emergency escalation targets.
- Lower numeric priority wins. Rules are evaluated deterministically by priority and stable identifier.
- ZIP service areas contain normalized US postal codes and may be activated or deactivated without deleting their audit history.
- Technician controls include base availability, on-call state, service capabilities and bounded availability blocks.

Evaluation and enforcement:

- Evaluation version is `routing-v1`; the combined dispatch recommendation is `dispatch-v2`.
- Business hours are evaluated in the tenant timezone. Until tenant-specific hours are introduced, the baseline is Monday-Friday, 8:00 AM-6:00 PM.
- Once applicable active rules exist, the service address must match an active configured service area. Out-of-area work is ineligible for normal recommendation.
- Availability, schedule-conflict and on-call requirements are enforced before a candidate is eligible. An authorized human override remains possible only with the existing normalized reason requirement.
- Emergency rules may return owner/administrator and on-call escalation targets. The output is decision support and does not autonomously notify, diagnose or dispatch.
- The response exposes bounded reason codes and plain-language factors, not hidden model reasoning.

Audit:

- Configuration actions are `routing.rule_created`, `routing.rule_updated`, `routing.service_area_created`, `routing.service_area_updated` and `routing.technician_updated`.
- Explicit evaluations create `routing.rule_evaluated`; assignment audits embed the exact bounded `routing-v1` trace used by `dispatch-v2`.
- Configuration writes and their audit event commit in one transaction.

## APP-013 Legacy CREATE Technician/Lifecycle Safeguard

- Shared job-calendar-guard now serves dispatch, technician workflow and direct completion. Dispatch behavior is unchanged by the helper rename. Existing unfinished-journal hold plus Job.status ACCEPTED/either reserved window endpoint/no nonblank Calendar reference defines this narrow legacy hold.
- Technician list/detail use existing calendarSyncPending:true with availableActions:[]; authorized technician details remain visible and labeled provisional. All six actions and target-state no-op replays reject with existing office-review 409 before writes/audit/intent. Signed-link/active-tech/current-assignment/tenant/deletion authority remains first.
- Direct completion selects booking reference/window and holds an unconfirmed ACCEPTED reservation before completion. Both technician and completion writes compare exact observed booking fields/status/version; technician also matches the submitted expectedUpdatedAt. Existing assignment, tenant, deleted and no-unfinished predicates remain. Version advance/audit/intent atomicity is preserved.
- An ABORTED CREATE journal with an unconfirmed local reservation remains held. Ordinary terminal history/completion replay and unscheduled/in-progress behavior remain compatible; no blanket claim that nonblank references or terminal journal status prove provider state. Already-IN_PROGRESS or terminal Job rows are not newly reclassified without evidence.
- Evidence: 684 backend tests including ten new cases, 45 real field snapshots/270 mutation-no-op refusals/nine direct-completion refusals/two competing-write cases, prior 15 migrations/11 actual crashes. UI runtime unchanged; 60 tests/14 pages, five synthetic browser suites and four zero-finding audits pass. No new crash case or live provider acceptance.
- Historical inventory/repair, explicit reader/worker/office-review ownership, authorized CREATE orchestration, post-read/provider races, reschedule/cancel and SENDING recovery remain open. No migration outside disposable local fixtures, real-data action, provider configuration/activation, merge or deployment. Backend `7026d0824607938b7ea1ff1f46e3f9e81045cf53`; evidence: readiness-report.md and legacy-field-summary.json.

## APP-013 Legacy CREATE Dispatch Safeguard (Earlier)

- Dispatch pending policy now includes ACCEPTED jobs with either reserved window endpoint and no nonblank Calendar reference, even without an unfinished journal. Summary/detail use existing calendarSyncPending:true, ESCALATED classification and CALENDAR_SYNC_PENDING candidate reason; all candidates are ineligible and recommendation is null. The operator may inspect provisional local details but must not treat them as confirmed.
- Assignment/reassignment/override and assignment cancellation refuse with existing office-review 409 before same-technician/unassigned no-op success. Tenant/undeleted lookup precedes the hold; missing/cross-tenant/deleted lookups retain not-found behavior. No new response fields, job status, schema or migration.
- Both conditional mutation writes match observed status, reference, window endpoints and observed updatedAt plus submitted expectedUpdatedAt, tenant, deletedAt:null and no unfinished journal. Exact field matching rejects an intervening unconfirmed reservation even if a competing write preserves the timestamp. It does not serialize all job/provider changes or prove external Calendar state.
- Six new unit cases (674 total) and real PostgreSQL evidence cover eighteen legacy snapshots/54 mutation refusals, tenant/deleted boundaries and two competing commits between read and write; held rows/audits remain unchanged. Existing 15 migrations/11 process-crash cases pass; no new crash case or provider call.
- UI runtime unchanged; synthetic desktop/390px assigned/unassigned/full/partial fixtures preserve provisional banner and disabled assignment controls, while operations escalation remains available. Technician link generation, routing evaluation/audit and other screen actions are not newly guarded. Five browser suites, 60 UI tests/14 pages and four clean audits pass; no live acceptance.
- Remaining legacy technician/lifecycle guarding, discovery/repair, authorized CREATE reader/worker/review ownership, external races, reschedule/cancel and SENDING recovery remain open. No real-data repair/deletion, provider configuration, activation, merge or deployment. Backend `8450113ebfb30a478a72ce476f9491dcda2e3114`; evidence: readiness-report.md and legacy-dispatch-summary.json.

## APP-013 Legacy CREATE Messaging Safeguard (Earlier)

- The shared transactional message evaluator returns CALENDAR_PENDING for an undeleted ACCEPTED job with either reserved service-window endpoint and no nonblank Calendar reference, even without an unfinished journal. Null/empty/whitespace references and partial windows are covered; missing/deleted records remain MISSING first. A terminal journal marker alone does not release an unconfirmed reservation.
- Existing manual queue and durable capture reject pending work. Intent recovery checks pending before hash mismatch, defers 60 seconds without spending failure budget, and keeps PENDING with calendar_sync_pending. Exhausted owner retry cannot reset or audit the held intent. Pre-send delivery checks before decrypt/consent/provider, conditionally releases only its unsent claim to QUEUED, refunds the claim attempt and defers 60 seconds. No unknown/already-sent SENDING reset is added.
- Existing public error/status shapes and state hashes are unchanged. Notification center renders the existing On hold for Calendar review label, without provider/journal details; pending work has no retry button. Unscheduled departure compatibility and terminal cancellation policy are unchanged. Once the legacy predicate no longer applies, ordinary state/hash/consent gates still apply; a stored reference is not independent Calendar proof.
- Local evidence: twelve new unit cases, 668 total tests, 36 real database reference/window/template combinations, nine transaction rollbacks and 36 stale/incompatible post-settlement refusals. All 15 migrations/11 prior crash cases, UI 60 tests/14 pages, five browser suites and four zero-finding audits pass. No new crash case or live acceptance claimed.
- Hold may persist indefinitely pending separately authorized repair. Global legacy dispatch/technician safeguards, reader/worker/review ownership, Calendar repair, post-read/provider races, reschedule/cancel and SENDING recovery remain open. Runtime change is only the shared messaging predicate; no schema/dependency/provider configuration, real-data change, activation, merge or deployment. Backend `a8154f74c55a347f1e888e745ee9fe3634eecd6d`; evidence: readiness-report.md and legacy-message-summary.json.

## APP-013 Soft-Deleted Customer-Management Access Safeguard (Earlier)

- loadAppointment selects id/tenantId/deletedAt:null and defensively rejects a deleted returned row. Already-deleted, missing and cross-tenant management records share existing HTTP 400 with Appointment not found, before journal/legacy-state disclosure, activity lookup or any of seven management actions. Token signature/expiry and expected tenant validation remain first; no public deletion metadata or new error code.
- Customer action/payment handlers clear stale booking data on 400 as well as existing 409. Missing/deleted refusal replaces booking controls/details with the existing error panel; payment failure closes the blank popup without checkout navigation. Other 400 validation failures also conservatively clear the snapshot. No payment-policy, provider or retention change.
- Twelve added unit cases verify query predicate, deleted/missing equality, all actions, no downstream activity and five lifecycle states. Three real PostgreSQL active/terminal fixtures succeed before deletion, then reject all actions for deleted/missing/cross-tenant identities (63 refusals) without changing rows or producing audit/intent/message. 656 backend tests/55 suites, lint/build/architecture/Prisma, 15 disposable migrations/11 prior crashes pass; no new crash case.
- UI 60 tests, lint/type/build/14 pages and five desktop/mobile harnesses pass. Extended browser checks cover initial refusal, stale action cleanup and payment popup closure; 30 customer/dispatch requests and 22 synthetic POSTs, zero external requests/page errors. All four backend/UI audits remain zero. This is local synthetic proof, not live provider/browser integration acceptance.
- Deleted-at-load boundary is closed, but deletion after the read can still race with in-flight responses/actions. No client push revocation, global locking, new deletion endpoint, real-data deletion, hard-delete, token rotation or automatic repair is added. Legacy dispatch/technician/message guards, authorized CREATE recovery ownership, reschedule/cancel and SENDING recovery, external races and acceptance remain open. Backend `e7024c1d87a84de3d602994c02a31af313b0f05c`; readiness report and deleted-booking-summary.json contain exact commands/limits. No production migration, provider action, merge, deployment or activation.

## APP-013 Legacy CREATE Customer-Management Safeguard (Earlier)

- Signed management-token/tenant authority and existing unfinished-journal checks run first. An ACCEPTED job with either reserved window endpoint and no nonblank Calendar reference now returns fixed office-review 409 for all seven management actions, before provisional serialization/activity lookup or downstream calls. No new success-state enum or public journal/Calendar field is added.
- Covers view, confirm, request_reschedule, continue_payment, availability, reschedule and cancel for that narrow legacy state. Unscheduled payment recovery, cancelled/completed historical viewing and finalized booking behavior remain unchanged. This is a customer management boundary guard, not a change to payment policy or automatic repair.
- Fourteen unit cases cover actions/partial windows/blank references/compatibility. The three prior PostgreSQL CREATE failure fixtures add 21 action refusals, tenant checks, absence of journals and exact row/no-success-side-effect proof. 644 backend tests, lint/build/architecture/Prisma, disposable 15 migrations/11 prior crash cases and 60 UI tests/14 pages pass. All four audits remain zero.
- The extended synthetic browser harness verifies legacy hold on initial load and removal of old details/actions after conflict at 1440/390 pixels; all five harnesses pass, zero external requests/page errors. Rendered UI code is unchanged; this is not live provider/backend/browser integration proof.
- Snapshot races, dispatch/technician/message handling of unjournaled reservations, legacy repair and authorized CREATE reader/worker/review orchestration remain open. Inspection found loadAppointment lacks an explicit deletedAt predicate; soft-deleted management-link access remains a separate remediation before acceptance. No new journal activation, schema/migration, provider action, real data, merge or deployment. Backend `d1a18ff15309d4c551e05e584031d173ea8d4cfd`; readiness report and legacy-create-customer-summary.json contain exact proof/limits.

## APP-013 Legacy Initial CREATE Uncertainty Safeguard (Earlier)

- Existing initial confirmation retains its tenant/session/signed-slot/eligibility/availability and conditional reservation checks. After a reservation succeeds, any insert exception now keeps the reservation/newer job state, does not reset to CREATED or clear the window and does not run finalization or emit a confirmation. Existing HTTP 503 now directs office review instead of choosing another appointment. No success response field, payment policy, schema, module registration or provider adapter changes.
- Diagnostic logging emits fixed appointment_calendar_insert_review_required plus tenant/job identity only, no raw provider/credential/body error. Logger failure cannot replace the safe response. There is no compensating Calendar call, reinsert, new journal, durable event ID, retry worker or automatic release.
- All post-reservation insert failures are conservatively held, including pre-dispatch credential failure/definite rejection. Slots may require manual review even when Calendar created nothing. Existing same-window replay rejects missing finalization; different-window conditional claim cannot reuse the held job. This does not add a global guard to other legacy job mutation paths or a new review UI/repair authority.
- Fifteen added unit cases plus three actual PostgreSQL failure cases verify no rollback/newer-edit overwrite, no success audit/intent/message and no same/different signed-choice reinsertion from fresh service instances. Synthetic lost acknowledgment includes an in-memory provider event before the throw; no real Calendar request. 630 backend tests, all local gates/15 migrations/11 prior process-crash cases, 60 UI tests and five synthetic desktop/mobile browser harnesses pass. All four backend/UI audits remain clean. No new process-crash or live webchat/provider acceptance claim.
- Backend `fd68377c5f151ab08ccdf32712167f269432b862`; readiness report and create-uncertainty-summary.json record exact steps and limitations. Authorized CREATE journal orchestration/reader-worker/review ownership, legacy visibility/repair, reschedule/cancel and SENDING recovery, external-state races and acceptance remain open. No production operation, real data, migration outside disposable fixtures, provider configuration, merge, deployment or activation.

## APP-013 Scoped Google/UUID Compatibility Checkpoint (Earlier)

- Exact-parent gaxios 6.7.1, google-gax 4.6.1 and teeny-request 9.0.0 overrides select uuid 11.1.1 rather than 9.0.1; exactly one lock entry changes. Major transitive-library exception only: no Firebase/Google parent upgrade, runtime application/API/auth/payment/provider, UI/static-hosting, schema or migration contract change. Prior overrides stay intact.
- Fourteen native checks automatically wrapped by Jest verify CJS/ESM resolution, v4 IDs, v3/v5/v6 integer buffer bounds and exact writes, actual gax request-ID and gaxios/teeny multipart paths via synthetic transports, and unchanged Firebase initialization/malformed-token refusal. Small installed 9.0.1 v3/v5 buffers reproduced silent partial writes; no v6 baseline or public CallDesk exploit claimed. No sockets, credentials or real provider requests in these fixtures.
- All three inspected consumers use zero-argument v4. UUID v11 timestamp-options/state, types and packaging changes are not assumed universally compatible. APP-013 owns all three exact-parent exceptions: re-review on any parent/Firebase change or new UUID API use; remove once native patched resolution and consumer/bounds/application/PostgreSQL/browser gates pass. No upstream Google endorsement or full provider integration acceptance is claimed.
- Backend 615 tests, lint/build/architecture/Prisma and disposable 15-migration/11-crash suite pass; zero provider calls and database absence verified. UI 60 tests, lint/type/build and five desktop/mobile synthetic browser harnesses pass unchanged. Backend full/omit-dev and UI full/omit-dev audits all pass with zero findings; prior eight moderate findings are absent. Current audit success is not comprehensive security or APP-013 acceptance.
- Backend `606a803b3153e160d4f45e3a88d154bd9c0330cd`; readiness report and google-uuid-audit-summary.json contain exact proof/limits. Authorized CREATE orchestration/recovery ownership, external-state races, reschedule/cancel and SENDING recovery, prior override/in-place-API limitations, future upload limits/error mappings, acceptance and release gates remain open. No production operation, provider configuration, real data, merge, deployment or activation.

## APP-013 Scoped Prisma Merge Compatibility Checkpoint (Earlier)

- Exact-parent `@prisma/config@7.10.0 -> deepmerge-ts: 8.0.2` override replaces 7.1.5, with one lock entry changed. Intentional major library exception only: no Prisma/client/adapter, Nest/Express, runtime application/API/auth/payment/provider, UI/static-hosting, schema or migration contract change. Prior overrides stay intact.
- Installed 7.1.5 baseline reproduced stack RangeError with two tiny self-referencing objects; patched cycle checks pass. Twelve native tests automatically wrapped by Jest verify consumer resolution and ordinary deepmerge use, cycles, record/array compatibility, changed Map behavior, in-place aliasing limits, real CJS/ESM Prisma config loading and invalid/missing config rejection. Synthetic files/objects; no loader DB connection or seed execution.
- This exception is scoped to the inspected Prisma c12 merger using ordinary deepmerge. Tests pin that consumer and exclude in-place/unsafe entrypoints. v8 changes Map merging and custom types; current CallDesk config uses plain records/strings, not Maps/custom callbacks. An exploratory deepmergeInto immutability assertion failed because aliases may persist; the retained limitation test and separate ordinary-deepmerge immutability proof prevent a blanket safety claim.
- APP-013 owns this exception. Re-review on every Prisma/config change; remove when native resolution is patched and cycle/config/PostgreSQL/application/browser gates pass. No upstream Prisma endorsement of this major override is claimed. Existing mysql2/Multer/PostCSS retirement gates remain.
- Backend 614 tests, lint/build/architecture/Prisma and disposable 15-migration/11-crash suite pass; zero real provider calls and database absence verified. UI 60 tests, lint/type/build and five desktop/mobile synthetic browser harnesses pass unchanged. Backend full/omit-dev audits 4 high/8 moderate -> 0 high/8 moderate; UI clean. High-only gate passes, but Firebase/Google/uuid and full-audit failure remain unaccepted.
- Backend `d05eb9a82355359a8cfa9ee48bf4cd10bb1a5c72`; readiness report and prisma-merge-audit-summary.json contain exact proof/limits. Authorized CREATE orchestration/recovery ownership, external-state races, reschedule/cancel and SENDING recovery, future upload limits/error mappings, acceptance and release gates remain open. No production operation, provider configuration, real data, merge, deployment or activation.

## APP-013 Scoped Nest/Multer Compatibility Checkpoint (Earlier)

- Scoped `@nestjs/platform-express@^11.2.3 -> multer: 2.3.0` override replaces 2.2.0; only the Multer lock entry changes. No Nest/Express major upgrade, application/API/auth/payment/provider, UI/static-hosting, Prisma/schema or migration change; prior overrides remain intact.
- Twelve native tests automatically wrapped by Jest cover Nest consumer resolution, ordinary/invalid fields, explicit index limit, async file-size limits across four upload methods, exact-limit acceptance, real disk descriptor close/unlink and Nest interceptor compatibility. Invalid sparse append is caught without iterating/serializing the array; no old-version negative reproduction or resource-exhausting load test. Disk-layer stream failure is not full network-abort acceptance.
- Future upload activation remains gated: explicit fieldArrayIndexLimit plus field/file size/count/depth controls and 4xx mapping for new Multer errors. Nest 11's new array-index error remains a plain Error, verified by the fixture. No upload handlers were found in current application source; no new endpoint or global upload middleware is enabled. Version upgrade alone does not guarantee bounded array parsing.
- APP-013 owns the override: re-review on any Nest change (test pins reviewed 11.2.3); remove when native resolution is patched and multipart/application/browser gates pass. Existing mysql2/PostCSS retirement conditions remain.
- Backend 613 tests, lint/build/architecture/Prisma and disposable 15-migration/11-crash suite pass; zero real provider calls and database absence verified. UI 60 tests, lint/type/build and five desktop/mobile synthetic browser harnesses pass unchanged. Full backend audit 9 high/8 moderate -> 4 high/8 moderate; omit-dev 4 high/8 moderate; UI clean, zero critical. Multer/Nest findings absent, remaining Prisma/deepmerge-ts and Firebase/Google/uuid unaccepted.
- Backend `ace10ff7ed892c49ee1824ebd988ee1dcf3d01f8`; readiness report and multer-audit-summary.json contain commands/evidence. Authorized CREATE orchestration/recovery ownership, external-state races, reschedule/cancel and SENDING recovery, remaining acceptance and release gates stay open. No production operation, provider configuration, real data, merge, deployment or activation.

## APP-013 Scoped Prisma/mysql2 Compatibility Checkpoint (Earlier)

- Scoped `prisma@^7.10.0 -> mysql2: 3.24.4` override replaces the 3.15.3 pin. Six lock entries change: mysql2/lru.min updates, sql-escaper addition, sqlstring/denque/seq-queue removal. Prisma/client/adapter 7.10.0 and PostgreSQL schema remain unchanged; no application/API/auth/payment/provider/UI/static-hosting contract or new migration.
- Ten native Node fixtures automatically wrapped by Jest exercise resolution, default cleartext-auth refusal, explicit opt-in compatibility, prototype-plugin refusal, real packet parser sync/async inflation bounds/order/malformed input and public SQL formatting. At most 18 KB synthetic data, no sockets or real credentials. No full TLS enforcement, old-version negative reproduction, MySQL/Studio live acceptance or large-payload stress claim.
- APP-013 owns the temporary override. Review on any Prisma update; tests intentionally require Prisma 7.10.0. Remove when native resolution is reviewed/patched and protocol/PostgreSQL/application/browser gates pass. No cleartext option, provider setting or new connection is configured.
- Backend 612 tests, lint/build/architecture/Prisma and disposable 15-migration/11-crash suite pass, zero real provider calls and fixture absence verified. UI 60 tests, lint/type/build and five desktop/mobile synthetic browser harnesses pass unchanged.
- mysql2 findings absent. Fresh baseline already 9 high/8 moderate due new Multer/Nest findings. Final backend full 9 high/8 moderate, omit-dev 8 high/8 moderate; existing deepmerge risk additionally propagated to @prisma/client in final audit. UI audits clean, zero critical. Changing audit metadata/aggregation is recorded, not a net count-reduction or acceptance claim. Multer/Nest, Prisma/deepmerge-ts and Firebase/Google/uuid remain open.
- Backend `54b613f922ffecc84652c6bee81b1952b44d24f3`; readiness report and mysql2-audit-summary.json hold exact evidence. Authorized CREATE orchestration with upstream guards and explicit recovery ownership remains next functional scope; additional dependency sections must be explicitly selected. No merge, deployment, production migration, external sends, real data or activation; release gates remain open.

## APP-013 Backend Lint-Tool Compatibility Checkpoint (Earlier)

- Four backend dev-only lock entries change: @humanfs/node 0.16.8, required @humanfs/core 0.19.2 and @humanfs/types 0.15.0, brace-expansion 1.1.18. No manifest, runtime application/API/DTO/auth/payment/provider, UI/static-hosting, schema or migration contract change; no override or SDK downgrade.
- Five native Node tests automatically wrapped by Jest verify import-only humanfs resolution, lock agreement, direct file and contained file/directory symlinks remaining links, normal copying and bounded brace/minimatch behavior. Preserving links is not a sandbox; no top-level directory-link, filesystem-race or large-input performance claim. The maintainer advisory and reviewed patched-version metadata differ; installed source/fixtures support only the documented bounded behavior.
- Backend 611 tests, lint/build/architecture/Prisma and disposable 15-migration/11-crash fixture pass; zero real provider calls, database removed and absence verified. UI 60 tests, lint/type/build and all five desktop/mobile synthetic browser harnesses pass unchanged.
- Backend full audit improves 5 high/9 moderate -> 4 high/8 moderate; omit-dev still 4 high/8 moderate, unaccepted. UI full/omit-dev remain zero. Prisma/deepmerge-ts/mysql2 and Firebase/Google/uuid dependency work remains separately scoped; no automatic audit-suggested major downgrades. Known-audit cleanliness is not comprehensive security or acceptance.
- Backend checkpoint `9eb43e5e8ec3eab1d6ab85c4b5a06ef3b1959165`; readiness report and backend-toolchain-audit-summary.json contain commands/evidence. Authorized CREATE orchestration with upstream guards and explicit recovery ownership remains next functional scope. No activation, external sends, real data, provider/configuration, production migration, merge or release; prior approval gates remain open.

## APP-013 UI Development-Tool Compatibility Checkpoint (Earlier)

- Eight UI dev-only lockfile entries across ajv, brace-expansion, flatted, js-yaml, minimatch and picomatch move to compatible reviewed releases within existing majors. No manifest/new override, backend dependency, application-source/API/DTO/auth/payment/provider or static-hosting contract change. Next/React and the existing scoped PostCSS override are unchanged.
- Sixteen new tests verify installed/locked consumer resolution, configuration/schema parsing, cyclic cache data, prototype-reference refusal and both glob-library generations. ESLint still flags deliberately invalid synthetic source; no lint suppression. No large attack payload, customer data or deployed exploitability test.
- UI lint/type/build (14 pages), 60 tests and all five desktop/mobile browser harnesses pass. Backend 610 tests, architecture/Prisma and 15-migration/11-crash local suite pass with zero real provider calls; database removed.
- Full and omit-dev UI audits now report zero findings. Backend remains 5 high/9 moderate, omit-dev 4 high/8 moderate, unaccepted. Audit cleanliness is scoped to current known advisories, not a security guarantee or functional acceptance. Existing support-lifecycle/deprecation warnings and PostCSS override retirement ownership remain.
- Backend checkpoint `d12ba7c3f62ba119ddcb02a27a7d2d9293f7f6d7`; APP-013 readiness report and toolchain-audit-summary.json contain exact commands and evidence. No merge, deployment, provider configuration, external sends, real data, production migration or activation; prior recovery and release gates remain open.

## APP-013 PostCSS Compatibility Checkpoint (Earlier)

- UI only: exact `next@15.5.25` scoped override selects PostCSS 8.5.28 instead of Next's 8.4.31 pin; no other resolved package or application-source/API/DTO/auth/payment/provider contract changes. Static hosting and Next/React remain unchanged.
- Eight regression tests resolve PostCSS through Next's CSS build consumer, checking manifest/install/lock, source-map disclosure boundaries and normal adjacent/inline/explicit maps, plugin transformation and safe closing-style serialization. Three synthetic disclosure tests failed on the previous version and pass on the patch; no real customer/secret files or public exploit tested.
- UI 44 tests, lint/type/build (14 pages) and all five desktop/mobile browser regressions pass. Backend 610 tests, architecture/Prisma and local 15-migration/11-crash suite pass; zero real provider calls and test database removed.
- UI full audit 5 high/1 moderate remains unaccepted; omit-dev now zero. Backend unchanged 5 high/9 moderate, omit-dev 4 high/8 moderate. Zero critical. No implication that development/build dependencies or functional recovery risks are accepted.
- APP-013 owns the temporary override: re-review on the next framework change; remove when the native Next dependency is reviewed/patched and tests/build/browser gates pass. Exact-version scope avoids silently applying the exception to a different framework. No broad audit-fix or future-major authorization.
- Backend checkpoint `6c467a12eb0dabc651addb9784c7e7c9aaa0795d`; details: APP-013 readiness report and postcss-audit-summary.json. No migration outside local fixture, production action, merge, deployment, provider configuration, real data, external send or activation. Prior functional/release acceptance gates remain open.

## APP-013 UI Framework Compatibility Checkpoint (Earlier)

- Next/eslint-config-next 15.5.25 and React/React DOM 19.2.8 replace the prior Next 14/React 18 runtime. React 19 types are aligned; exact installed/manifest/lock agreement is tested. No backend dependency, API/DTO, auth, payment, provider or data contract changed.
- Hosting remains static `ui/out`, without a Next-server rewrite. The web manifest explicitly exports `dynamic = "force-static"` to preserve static generation under Next 15; start_url remains `/app/technician`. Six home anchors migrate to Next Link with prefetch disabled; local browser navigation passes. Secure-link rejection, Calendar holds, retry uncertainty and payment-return copy retain prior semantics.
- UI 36 tests, lint/type/build (14 pages), 22 desktop/mobile route checks, 12 home navigations, static manifest and four prior synthetic workflow browser regressions pass. Backend 610 tests, architecture/Prisma and 15-migration/11-crash local fixture pass; no real provider calls.
- Fresh audit UI 1 critical/9 high/1 moderate -> 0 critical/6 high/2 moderate. Omit-dev 1 high/1 moderate remains via PostCSS/Next; backend unchanged 5 high/9 moderate, omit-dev 4 high/8 moderate. Remaining findings unaccepted. Critical advisory's Windows-server condition does not match checked-in static hosting; no live exposure or deployed remediation claim.
- Backend checkpoint `5ac324c0cd9b9cd108e8074ba2578feeed94d597`; evidence/commands: APP-013 readiness report and framework-audit-summary.json. No merge, deployment, provider configuration, migration outside disposable local fixture, external sends, real data or activation. Prior functional recovery gates remain open.

## APP-013 qs Dependency Compatibility Checkpoint (Earlier)

- Backend locked qs 6.16.0 replaces 6.15.3; no API, DTO, business policy, runtime application code, UI or provider SDK change. Loopback tests use Nest's rawBody/extended-form parser to verify exact callback bytes, ordinary nested forms and Unicode/plus handling. No real callback acceptance is claimed.
- Twelve installed-code regression tests cover the two maintainer-reported library defects and consumer resolution. Runtime dependency presence does not establish an exploitable application route. Backend full audit is now 5 high/9 moderate (qs absent), omit-dev 4 high/8 moderate; UI 10 high/1 moderate. Remaining findings are not accepted.
- Evidence and reproducible clean-install/audit/test commands: backend APP-013 readiness report and qs-audit-summary.json. No activation, merge, deployment or production action; authorized CREATE orchestration and recovery ownership remain pending.

## APP-013 Job Policy Calendar Guards (Review-Ready)

- Urgency overrides and payment exception APPROVE/REVOKE reject any unfinished CalendarOperation (finishedAt null), using only existence, before same-value urgency replay or financial entitlement processing. They return the existing office-review 409 without job/audit/provider side effects.
- Urgency replaces the direct policySnapshot update with tenant/job/deletion/server-observed updatedAt/no-unfinished-operation compare-and-set. Payment exceptions retain client expectedJobUpdatedAt and add current status/no-unfinished-operation predicates. Both advance updatedAt monotonically and audit only the successful mutation in its transaction.
- A competing urgency/payment snapshot or Calendar reservation cannot be overwritten using an older observed job version. A committed policy mutation invalidates older reservation inputs. Existing unrelated snapshot fields remain intact. This does not introduce a client-reviewed-version field to urgency requests or globally lock asynchronous payment/subscription state.
- Existing required-payment/manual-override/advanced entitlement, exception revocation, closed-job and verified-payment rules remain unchanged. No payment status, amount, fee, Checkout, webhook, subscription or provider configuration mutation. Existing operations escalation remains available while urgency overrides are held; no escalation provider action is part of this acceptance proof.
- Local proof: 598 backend tests, 30 UI tests; 12 journal action/status combinations, both read/write race orders, competing policy snapshot preservation, tenant/deletion isolation and actual audit rollback. Prior 11 process-crash cases still pass. Synthetic urgency conflict browser QA at 1440px/390px verifies no false success and available escalation; payment exception remains API-only proof.
- Requires the prior journal-table migration, still approval-gated. Inactive execution remains unregistered; authorized scheduling orchestration and fresh upstream policy/payment/availability validation, reader/worker ownership/recovery/review and provider-race handling remain prerequisites. Dependencies and remaining acceptance remain open. Exact evidence/commands: backend APP-013 readiness report.

## APP-013 Lifecycle and Technician Calendar Guards (Review-Ready)

- Any CalendarOperation with finishedAt null holds generic completion and all six technician status/assignment-release actions before idempotent replay, audit or departure-intent work. Uses the existing existence-only relation and office-review 409; terminal history removes this hold only, not ordinary lifecycle/authorization rules.
- Generic completion matches the observed tenant/job/undeleted/status/updatedAt snapshot and no unfinished operation in its transactional update. Its concurrent-completed fallback also verifies the hold before returning a replay. The public completion request shape is unchanged; this is internal observed-version concurrency control.
- Technician mutations retain signed-link verification, active technician/tenant/assignee/deletion and client expectedUpdatedAt controls, adding current job status and no-unfinished-operation predicates. Both mutation paths explicitly advance updatedAt monotonically; audit and existing departure intent remain transactional. No payment or urgency policy behavior is modified.
- Technician summary/detail add calendarSyncPending boolean without provider/journal metadata. The existing bounded assigned-job list includes unfinished cancelled reservations; tenant/assignee/deletion/take-200 boundaries remain. Held and terminal jobs expose no availableActions. List grouping and customer-contact visibility retain existing semantics.
- Field UI labels held work provisional, instructs no travel/start/status mutation, hides every field action even if stale actions accompany the hold, and clears old detail after mutation 409. This is synthetic desktop/390px proof, not live-phone or provider acceptance.
- Local evidence: 588 backend tests, 30 UI tests, 15 disposable migrations, 12 action/status combinations, deterministic reservation-before-mutation-CAS and reverse ordering, audit rollback, terminal/departure regression and prior 11 actual process crashes. Zero real provider calls; new screenshots/harness and exact commands in backend APP-013 readiness report.
- Prior journal table remains a runtime prerequisite. Executor/journal/reconciler remain unregistered; legacy live scheduling is unchanged. Policy-version coordination, authorized orchestration, reader/worker ownership/retry/review, reschedule/cancel recovery, post-preflight races, dependencies and acceptance remain open. No activation/migration/release authority is granted.

## APP-013 One-Shot CREATE Execution (Inactive)

### Reader Attempt-Ownership Safeguard (2026-09-08)

- An unfinished PENDING CREATE belongs to the executor. Reconciliation validates tenant/action/terminal state, then returns existing pending result without job/provider access, expiry classification, journal/job changes, audit, intent, enqueue or send. Apparently matching evidence cannot bypass the durable attempt latch. The executor retains its existing expiry/review policy; the reader does not scan or expire pending rows.
- UNCERTAIN/APPLIED remain eligible for existing strict read-back proof, not automatic insertion. These statuses do not prove that execution has ended: active-attempt/recovery-reader coordination is still required before a worker is activated. No rearm, replacement event ID, lease, retry worker, route, module registration or live scheduling switch is introduced.
- A stale PENDING snapshot can return pending after concurrent execution finalizes; it cannot alter the newer receipt. A fresh lookup returns historical already_finalized. Unsupported/cross-tenant/held/terminal handling and exact evidence/version transactions remain unchanged.
- Evidence: five new unit cases (689 backend total), four replayed early-reader database scenarios followed by exactly one synthetic execution, one delayed-reader/concurrent-executor case, all 15 migrations/11 prior crashes. Read-back fixtures now traverse the real durable execution latch before synthetic reconciliation. Four clean audits, 60 UI tests/14 pages and five browser suites pass. No new crash case or provider call.
- Backend `ab88f68bd63a746c49bb9e8fad1081d29b8518b1`; readiness-report.md and create-reader-ownership-summary.json. This is an inactive ownership-boundary fix, not legacy repair, active-request fencing, authorization integration or release.

- Internal executor accepts tenant/operation identity only for an already-authorized persisted CREATE reservation; there is no route/worker/module registration or public scheduling-flow switch. Existing upstream tenant/auth/payment/signed-slot/availability protections must be preserved by eventual integration.
- Exact PENDING journal version plus matching undeleted ACCEPTED job/claim version/window/label/no-event/unassigned/no-technician-status are claimed atomically. Job version and journal claimedUpdatedAt advance together; journal transitions UNCERTAIN before any POST. UNCERTAIN is a durable at-most-one-attempt latch, not a retry lease or proof of network dispatch. Unknown commit acknowledgment prevents insertion.
- Concurrent calls/restarts on UNCERTAIN/APPLIED return pending without insert/read; FINALIZED reports historical completion, NEEDS_REVIEW/ABORTED stay held. No rearm/replacement ID exists. Future window and observed current journal/job versions are rechecked before the one attempt.
- Creator POST uses saved Calendar/event ID and private tenant/job/signmonsCalendarOperationId markers, exact absolute window/time zone, fixed reference summary, default/opaque/private event and disabled default reminders. No customer content/attendees/conference/management token. Encoded target, eight-second HTTP timeout, redirects refused and no automatic retry. All statuses/bodies, including 2xx/409, are discarded and errors are not exposed. Provider notification/ID guarantees are not overstated; see official reference in backend evidence.
- Every returned/thrown insert outcome then requires existing matching read-back reconciliation before atomic journal/job/intent/audit finalization. Missing evidence remains held; unknown outcomes never release reservations, roll back Calendar or authorize reinsert. A crash before actual POST can intentionally require office review. Separate recovery orchestration is not implemented here.
- Original execution checkpoint audited competing technician/lifecycle/urgency/payment-policy writes. The subsequent lifecycle/technician guards above address those two entry points; policy coordination, authorized scheduling orchestration, reader/worker ownership/retry/review, prior migration and retention remain activation prerequisites. Current checks do not globally serialize all mutations or prevent a post-check external race. No financial-policy changes or provider actions in either checkpoint.
- Objective local proof: 570 backend tests, 29 UI tests, 15 disposable migrations, two new process exits before/after synthetic insertion (11 total), concurrent single attempt, lost insert/commit acknowledgments and read-back-only recovery; zero real provider calls. No new API/schema/dependency or release authorization.

## APP-013 Unfinished Calendar Consumer Guards (Review-Ready)

- A job is held while any related CalendarOperation has `finishedAt: null`, including PENDING, UNCERTAIN, APPLIED and NEEDS_REVIEW. Relation selection takes one ID only; missing selection fails closed. Only existence affects consumer policy; provider identifiers, journal details and raw errors are not returned.
- Existing initial confirmation and all signed `POST /appointments/manage` actions (including view and payment recovery) return 409 with an office-review message before exposing provisional details or performing actions. No success-state enum is added. UI removes previously displayed booking details after action/payment conflict. Changed customer response audits use a transaction with exact tenant/job/version/no-unfinished conditional update and monotonic version advance.
- Legacy initial reservation, reschedule/cancel claim/restore/finalize and dispatch mutation predicates require no unfinished journal. Initial reservation also matches observed updatedAt. These are bounded row/version protections, not global serialization of every job/technician endpoint.
- Dispatch summary/detail add `calendarSyncPending: boolean`. A held job uses ESCALATED before assigned/payment/window queue classification; locally CANCELLED unfinished work remains in the tenant-bound undeleted list (existing 200-record limit). Candidates are ineligible with CALENDAR_SYNC_PENDING, no recommendation or assignment override; assignment/cancellation/no-op replay fail 409. UI labels local data provisional and disables assignment controls.
- Transactional message selection includes unfinished existence; CALENDAR_PENDING is distinct from MISSING/INCOMPATIBLE and checked before stale digest comparison. Existing hashes exclude journal state. Manual admission, intent recording and owner retry reject pending work. Enqueue recovery preserves PENDING and failure count, emits fixed `calendar_sync_pending`, and defers 60 seconds. Delivery detects this before decrypt/consent/provider, conditionally releases SENDING/attempt ownership to QUEUED, refunds only the unsent claim and defers 60 seconds. Direct claims honor nextAttemptAt. No reset of possibly sent/unknown work is added.
- Terminal journal history removes only this hold; ordinary lifecycle/hash/consent/version gates still apply. Inactive CREATE reconciliation finalizes the journal before recording its intent in the same transaction, so these guards do not block proven atomic finalization.
- Requires the prior journal-table migration at runtime; no new migration or activation. Existing legacy/unrecorded crash gaps, post-check provider race and SENDING pre-release crash gap remain. Before any journal writer activation, review competing technician/job mutation entry points, guarded CREATE integration, recovery ownership/retry/review and retention. Reschedule/cancel recovery, dependencies and acceptance remain open; no release/provider/production authorization.
- Evidence: backend APP-013 readiness report; 535 backend tests, 29 UI tests, 12 real action/status combinations in the disposable 15-migration suite, prior nine process crashes, and desktop/390px synthetic browser proof with zero provider calls.

## APP-013 Local Human-Reviewed Intake Admission (2026-09-10, inactive)

Latest split-review foundation adds two unregistered methods. Customer submitReview accepts exactly sessionToken/requestId/expectedRevision/draft/confirmed:true. It verifies the customer credential and current ongoing, unlinked, protected WEBCHAT transcript. One protected_intake_review_v1 CommunicationEvent/content plus CUSTOMER audit commits under the shared session lock. Payload contains encrypted canonical draft, session scope identifier, transcript revision/digest and original credential expiry, never the bearer token. One request per conversation; exact unexpired replay returns the same receipt, changed/replacement requests refuse. No new schema/migration or database-immutable record constraint.

Operator readReview accepts exactly requestId and requires verified non-impersonated owner/admin/dispatcher context. It loads the event in that tenant, rechecks durable shape/ciphertext/expiry and current protected session/history under locks, then rereads the record. It never calls customer credential verification/issuance or reconstructs a bearer. Private output is request ID, expiry, validated draft, transcript revision, PENDING_REVIEW and explicit human-review/no-job/no-booking/no-delivery flags; session/conversation identifiers and tokens are omitted. Operator transport must supply verified identity; no route/UI is registered here.

Original 15-minute session deadline caps review; this is not a new review SLA, credential renewal or production approval lifetime. New transcript, closed/deleted scope, expiry or malformed/foreign record refuses. Customer edits can invalidate the one pending request; replacement/withdrawal/recovery and per-request revocation/retention are unfinished. Records use application locking and strict type boundaries, not newly enforced database immutability. Reads are not admission approvals or durable operator decisions. Existing combined admitDraft remains inactive and unchanged; token-free operator admission is the next separate section, followed by intake-review UI integration. No job/consent binding, Calendar/payment/provider or sending effect occurs from submit/read.

- `CustomerIntakeContinuationService.admitDraft` remains unregistered. It accepts exactly sessionToken, expectedRevision, the existing seven-field validated customer-stated draft and review. Review is exactly urgency (`EMERGENCY` | `HIGH` | `STANDARD`), fixed reasonCode `OPERATOR_REVIEWED_INTAKE` and acknowledgeCustomerStatements:true. Caller tenant/actor/job/consent/payment/booking/delivery fields refuse.
- Verified request context must be a non-impersonated owner/admin/dispatcher with tenant matching the protected customer-session credential. The credential remains required and is rechecked under and after persistence locks. This local combined authority is not an approved production endpoint, browser flow or dual-credential transport.
- One database transaction uses the existing tenant/session/conversation lock, requires ONGOING protected WEBCHAT ownership, exact gap-free transcript revision and zero prior conversation job link. The issue category must already exist in that tenant catalog; admission never creates a category or guesses support.
- Customer upsert, customer-stated unverified address, CREATED job, CREATED_FROM link, optional `AppointmentEmailConsentBinding`, `job.customer_intake_admitted` USER audit and Conversation COMPLETED/JOB_CREATED close commit together. The job has no preferred window. Pricing snapshot is empty; no payment row, Calendar operation, dispatch state, SMS/email intent, queue/provider action or notification is created.
- Job policy records property/service intent, website-chat attribution, `OPERATOR_OVERRIDE` urgency with `HUMAN_INTAKE_REVIEW`, and intakeAdmission version/digest/revision/fixed review/unverified contact-address/email-choice facts. Audit/policy binding contain no customer name, phone or address. Ordinary customer/job/address records contain the reviewed statements for existing operator intake review.
- Existing consent evidence, including decline/revoke, is associated through the immutable one-time scope/job binding in the same transaction; `BOUND` is not current permission or delivery authority. A session without evidence records `NOT_RECORDED` and no binding. Closing the session prevents later protected transcript/draft, capture or prompt mutations.
- Exact same-actor/request replay with the same unexpired credential and unchanged original CREATED admission returns the same privacy-safe receipt. A one-way SHA-256 exact-request digest prevents changed draft/review adoption; it is internal and not a bearer capability. Concurrent identical requests serialize to one job/link/audit. Later lifecycle state requires ordinary job reads, not receipt replay.
- Failures after writes are reported as unconfirmed and require exact replay; transaction rollback covers binding/close failures. Customer/contact/address remain unverified and human urgency is operational classification, not diagnosis. Production split ownership, transport/retention, preferred-window/payment/Calendar handoff, notification/email delivery/status/recovery and owner acceptance remain open.
- Evidence: backend `1e145d1858c95453d4548b706115b1558c5e31c5`, `evidence/APP-013/customer-intake-admission/`. Nineteen new unit cases; 1471 backend/170 UI tests, nine new PostgreSQL groups, 19 migrations/19 prior process crashes, prior browser regressions and four clean audits pass. No production action or APP-013 acceptance checkbox.

## APP-013 Local Customer Session and Consent Response (2026-09-09, inactive)

Latest integrated journey adds read-only /customer-session/draft model dispatch accepting exactly sessionToken/expectedRevision/draft. Draft has exactly customerName (1-120), phone (international + and 8-15 digits), address (1-200), description (1-400), issueCategory, propertyType and serviceIntent from the existing intake vocabulary. Strings must be trimmed and control-free. No urgency, email, tenant, job ID or authority overrides. It is format-validated customer-stated data, not identity/contact/address verification, model extraction, a complete CreateJobPayload or saved job.

previewDraft rechecks current protected active/ongoing/unlinked ownership, exact transcript revision 1-20 and credential expiry under the same lock. It reads the session's latest historical email choice or NOT_RECORDED without making consent mandatory. Private receipt is projected draft/transcriptRevision/emailChoice plus urgencyAssessment:NOT_PERFORMED, requiresHumanReview:true, jobCreated:false, bookingAuthorized:false, deliveryAuthorized:false. No writes or admission authority; a later transcript makes the request stale, and a returned snapshot is not a future mutation credential.

Fictional integrated browser composes existing capture/prompt/respond with conversation and explicit draft review. Grant requires separate mailbox confirmation; decline and no-email skip both continue to draft. Skip creates no capture or consent evidence. Capture/response uncertain outcomes retry exact pending input only; the steps are individually durable, not one distributed transaction. Description carries forward without another question; customer supplies/reviews contact/category/property/service fields. Draft input errors permit correction, but auth/stale/expiry refusal clears private state. No job, Calendar/payment/provider, urgency decision or sending is connected.

Latest browser continuation adds the inactive /customer-session/continue model dispatch with exact sessionToken/interactionId/message and the existing server/origin/credential/body/budget gates. The optional injected continuation service is never registered in production; absent authority refuses. Success projection is reply/revision/deliveryAuthorized:false only. Fictional browser pending input is immutable across explicit same-ID retries; no automatic retry, editing or new submit while outcome is unknown. Network/timeout/429/503/malformed success retain pending state; request/auth/409 refusals clear private state, with no renewal or adoption. Clear/page exit/expiry invalidates the client generation so late responses cannot appear in a new session. Abort does not undo server writes. New local fixture only; see APP013_CUSTOMER_BROWSER_TRANSPORT.md.

Latest transcript continuation: unregistered CustomerIntakeContinuationService accepts exactly sessionToken/interactionId/message. The unexpired credential owns an ongoing, protected, active-tenant/undeleted WEBCHAT conversation without any job link. Input/reply are nonblank, at most 2000 characters; history caps at twenty turns. Strict protected_intake_turn_v1 encrypted input/reply pairs have exact session metadata and gap-free revisions, no plaintext fallback. Legacy caller-ID history is excluded and legacy readers exclude protected pairs.

Scripted-only reply computation runs outside transactions. Ownership, expiry and history digest are rechecked under the shared session/conversation lock before atomic CommunicationEvent/content plus privacy-safe CUSTOMER audit. Event status is RECEIVED, never SENT. Exact interaction/message replay returns only reply/revision/deliveryAuthorized:false; changed input and globally occupied foreign/legacy IDs refuse. Lost acknowledgment requires the same interaction/message and same unexpired credential; no automatic retry or credential renewal. Concurrent computations may duplicate, not persisted pairs. This is application serialization, not database immutability/retention or provider exactly-once. No browser dispatch, AI/tool adapter, booking, consent or delivery integration. Evidence: customer-intake-continuation/.

Latest browser-boundary continuation: unregistered CustomerConsentBrowserTransport requires a fixed origin/tenant and verified server integration context, TLS/socket identity (explicit loopback HTTP fixture exception), exact Origin/Host/Fetch Metadata including Sec-Fetch-Dest:empty and a custom JSON header. Cookies/public integration Authorization, cross-site/same-site/missing metadata, query credentials and noncanonical paths refuse. Non-start operations additionally verify customer-session tenant before the existing protected service. No deployed route is added.

Headers and streamed/final bodies are bounded; fatal UTF-8, compact JSON and exact operation fields refuse duplicate/ambiguous input. Budget is mandatory; the injected local fixed-window model caps starts/total/per-peer/in-flight work and consumes failed admitted attempts. It resets on restart and is not shared across replicas. All modeled outcomes are private/no-store with fixed errors; diagnostics contain only fixed operation/status. Browser success projection omits internal evidence IDs and extra service fields. No automatic retry. Full protocol and production BFF/TLS/proxy/access-log/parser/distributed-limiter limits: APP013_CUSTOMER_BROWSER_TRANSPORT.md.

Latest continuation: fresh bootstrap writes collectedData.customerSessionVersion:1, never adopts or upgrades old sessions. Legacy ensureConversation and email observe/requestOnce refuse any present marker, including malformed values, before downstream work; unmarked sessions preserve prior behavior. Shared customer-session lock requires exact marker 1 plus active tenant/undeleted scoped customer/WEBCHAT conversation/session under session advisory and row locks. Marker is application-owned JSON, not a database-immutable boundary; privileged SQL, old-writer rollout and retention still require review.

Unregistered CustomerConsentCaptureService.capture accepts exactly sessionToken/email with a normalized standalone address. Credential verifies before database and again under/after persistence locks. One encrypted capture and CUSTOMER privacy-safe audit commit together; same-address replay does not rewrite ciphertext/time/audit, replacement or malformed existing state refuses. Missing/expired/raw-ID/wrong-tenant/session credentials refuse. Capture is not consent, mailbox verification or sending. Prompt/respond now also require the protected marker.

Expired/lost session handling has no automatic renewal/adoption or historical appointment recovery. Clear private form/token, then explicitly start a new scope; office help is needed for existing appointments. Same unexpired credential can retry identical capture after an uncertain acknowledgment; reload loses the memory-only token. This is modeled in a fictional browser fixture only. Production BFF/HTTPS/origin/CSRF/abuse/redaction and full credential-bound AI intake remain unimplemented. No schema, active route/configuration/key, collection or send activation in this continuation. See APP013_CUSTOMER_SESSION_SECURITY_PLAN.md and latest handoff.

- Owner explicitly approved local credential-model implementation/testing. CustomerConsentCredentials and CustomerConsentResponseService remain absent from production modules/controllers/config. No schema/migration change.
- Verified business integration can bootstrap only a new random session/conversation/customer in one transaction. Existing webchat sessionId and integration key are not customer credentials. Session tokens bind tenant/conversation/session/jti/issue/expiry and a fixed customer-consent purpose.
- Dedicated injected 32-byte signing keys; explicit active key ID and at most two accepted versions, no environment/default/shared-key fallback. Strict canonical token framing/signature and claim shape. Local default TTLs: 15-minute session, at most 5-minute prompt capped by the session, exact expiry refusing; no renewal.
- Prompt binds the session-token identity, hash of randomized encrypted mailbox capture, fixed approved prompt digest and expected initial revision. It privately returns the displayed address/text only after current scoped state validation. A GRANTED response requires separate boolean mailboxConfirmed:true; DECLINED does not infer permission.
- Response revalidates current tenant/conversation/customer/session/capture under locks, creates the exact CUSTOMER receipt and invokes the immutable evidence store in the same transaction. Expiry is checked after evidence persistence to force rollback on an elapsed deadline. Same prompt/choice is idempotent, changed choice and competing prompt after completion refuse; no repeated completed question.
- Current receipt return is only historical identity/revision plus deliveryAuthorized:false. Scope/job binding remains separate and unchanged. No mailbox verification, event-time grant reference, event expiry enforcement, positive eligibility, queue or sending is connected. Historical events remain unchanged.
- Local browser uses fictional mailbox/keys, memory-only credentials and no-store responses. It is not real customer authentication rollout, secure-cookie/BFF/CSRF/abuse acceptance or full credential-bound AI intake. Legacy paths now refuse protected model sessions; historical unmarked intake is not retrofitted. Production secret loading/rotation, fingerprint adapter, transport/recovery integration, suppression/regrant and retention compatibility are unfinished.
- Key/transport plan and next boundary: [APP013_CUSTOMER_SESSION_SECURITY_PLAN.md](APP013_CUSTOMER_SESSION_SECURITY_PLAN.md). Backend customer-consent-session/ evidence: 44 unit tests, 18 database checks and grant/decline browser proof at 1440/390 widths. No production actions.

## APP-013 Inactive Consent Evidence Foundation (2026-09-09)

- Migration 20260909210000_add_appointment_email_consent_evidence supplies AppointmentEmailConsentScope, AppointmentEmailConsentEvidence and AppointmentEmailConsentBinding. No backfill or production migration. Scope is unique by tenant/conversation and tenant/session; immutable original intake-customer identity is separate from the immutable bound job-customer snapshot.
- Append-only GRANTED/DECLINED/REVOKED evidence is ordered by positive, gap-free revision under a scope row lock. The highest revision is the versioned current-state projection, not a mutable Customer flag. Source audit and tenant/interaction uniqueness deduplicate receipts; CHECKs constrain purpose/prompt/decision/fingerprint shape; database triggers reject UPDATEs.
- Unregistered transaction-local store accepts IDs, not caller-provided consent/address/expiry overrides. It reads only session/intakeEmail from the conversation, requires WEBCHAT/active tenant/undeleted scoped customers, exact structured metadata and a new CUSTOMER audit in the same transaction. Receipt replay returns its historical ID/revision and deliveryAuthorized:false; it never returns current permission or decrypts private data for the caller.
- A same-transaction audit establishes persistence linkage, NOT external customer authentication. The new local-only CustomerConsentResponseService validates a separate server-issued session credential plus exact mailbox/prompt token and creates that receipt atomically. It remains unregistered, with no live key loader or production route; existing address-only capture, SMS or owner approval cannot supply authority. Production bootstrap/transport and legacy intake protection remain required.
- A required fingerprint port has no production implementation/key/configuration; absence refuses before database access. The fixture injects a fictional tenant-scoped HMAC. Production key lifecycle/rotation/domain separation must be reviewed before adapter implementation or activation; no secret is created/reused here.
- One-time bindJob uses caller-owned transaction and tenant/conversation/scope/job locks, exact session and unique CREATED_FROM links in both directions; FK parent locks prevent competing link inserts during the decision. Ambiguous/wrong-tenant/deleted/different-job binding refuses. Both grant and decline histories may be associated with a job; association is not permission.
- Independent conversation/job/audit deletions are RESTRICTed while evidence references exist; root scope deletion cascades fixture-owned children. There is no active root-delete/purge API. Before release, review tenant deletion ordering, 90-day retention, legal holds and suppression/idempotency tombstones. Rollback/exception propagation remains mandatory for future transaction callers.
- D2 verification, D3 deadlines, D4 lifecycle/retention execution, customer suppression surfaces, event-time grant references, positive eligibility, credentials and durable admission are not implemented in this section. Old finalized events remain unchanged and ineligible. No sends or production actions.
- Proof: backend consent-evidence/database-summary.json and validation-summary.json; 29 unit cases, 24 local database checks and unchanged production-caller/eligibility boundaries. See the latest readiness report for fresh regression evidence and exact review commands.

## APP-013 Finalized Email Eligibility Diagnostic (2026-09-09, inactive)

Approved design with inactive evidence foundation only: [APP013_EMAIL_CONSENT_EXPIRY_PROPOSAL.md](APP013_EMAIL_CONSENT_EXPIRY_PROPOSAL.md). D1-D4 remain approved; the schema/recorder/job-binding checkpoint below does not authenticate customers or enforce expiry. Existing diagnostic behavior is unchanged and historical events remain blocked. Verification challenge/transport, fingerprint key lifecycle, retention/hold compatibility and positive admission remain gated; no sending or purge is authorized.

- AppointmentEmailEligibilityService.evaluate accepts only {intentId: UUID}; verified owner/admin user and tenant context, without impersonation, is required before any query. Submitted tenant, kind, recipient, consent, expiry or other override is rejected. No controller, module, worker or production caller is registered.
- Use PostgreSQL RepeatableRead with SET TRANSACTION READ ONLY; bounded 2-second acquisition/5-second transaction. Event/current-state query and retained-recipient resolver share one MVCC snapshot. Review time is explicitly projected in UTC. No write, lease, deduplication reservation, audit, credentials, composition or sending.
- Require a version-1 RECORDED supported immutable event and matching tenant/job/customer/intake-session/current job version, ordered minute-aligned window, current lifecycle/reference hash, active tenant and undeleted job/customer, no unfinished Calendar operation. Validate source audit action/actor/job/tenant/finalized version and matching SMS receipt. CREATE_READBACK requires its matching finalized CREATE operation; cancellation requires its bound immutable pre-clear window/hash snapshot. Missing or inaccessible event returns uniform 404, read failures sanitized 503.
- Event-time PERMITTED and currently valid enabled same-event preference are both necessary. BLOCKED/INVALID historical events never become eligible merely because preferences later change. Then reuse the retained encrypted-intake recipient resolver on the same transaction: exactly one valid CREATED_FROM conversation/session association, valid captured mailbox; no customer-master fallback or recipient override. Missing/declined/ambiguous/corrupt capture refuses; no address is returned from eligibility review.
- Every result is {resolution:blocked, eligible:false, deliveryAuthorized:false, snapshotOnly:true, reason}. Fixed reasons distinguish invalid/stale event, pending Calendar work, event/current policy blocked/invalid and unavailable recipient. If those checks pass, reason is CONSENT_AUTHORITY_UNAVAILABLE with blockers [CONSENT_AUTHORITY_UNAVAILABLE, EXPIRY_POLICY_UNAVAILABLE]. The optional binding contains intent/tenant/job/kind, job/settings/conversation versions, conversation ID, UTC review time, recipientSource:conversation_intake and ownershipVerified:false. These are private operational data, not a bearer capability or send token.
- No production trusted email-consent source or configured event-expiry enforcement exists. The inactive evidence store is not registered or consumed here; approved D1-D4 and synthetic receipts are not actual customer authority. An address, owner review, tenant permission or SMS consent is not substituted. No positive path, configured TTL or active collection is introduced.
- A consistent snapshot is deliberately allowed to become stale after its transaction. Concurrent policy/recipient revocation proof shows the current diagnostic stays internally coherent and blocked; a fresh read sees revocation. Future atomic admission/dispatch must recheck all authority and cannot trust this diagnostic as authorization. Durable queue/idempotency, consent, expiry, credential binding, transport and recovery remain separate unfinished work.
- Evidence: backend email-eligibility/ and readiness-report.md; 42 new tests, 1232 backend/170 UI tests, 23 reads with eleven-table invariance, actual read-only write refusal and cross-connection revocation race; 18 existing local migrations/19 crash regressions pass. Zero admitted events/providers/production actions; no schema or UI changes.

## APP-013 Reschedule/Cancellation Email Events (2026-09-09, recording only)

- AppointmentEmailIntent now supports APPOINTMENT_CONFIRMED, APPOINTMENT_RESCHEDULED and APPOINTMENT_CANCELLED, immutable state RECORDED/version 1. CREATE_READBACK is permitted only for initial confirmation; reschedule/cancellation use existing customer Calendar-acknowledgment finalizers. Existing source-audit and tenant/job/kind/version uniqueness, UPDATE rejection and retention cascades remain. No event backfill, addresses, raw Calendar IDs, bodies, credentials or transport.
- AppointmentCancellationSnapshot is a separate immutable pre-clear claim record, NOT finalization or send authority: composite tenantId/jobId/claimedUpdatedAt primary key; previousUpdatedAt, customerId/intakeSessionId, prior window, SHA256 Calendar reference and creation timestamp. Canonical active tenant/job/customer plus exact original job version and no unfinished Calendar operation are required. Snapshot insert and cancellation CAS commit together; failure preserves the original window. CHECKs require an ordered window, advancing claim version and valid hash; UPDATE is rejected; job/tenant hard-retention cascades delete snapshots.
- Cancellation claim/restore/finalization advance versions monotonically. Restore or abandoned execution leaves a historical snapshot, never an email event. Finalization audit adds claimedUpdatedAt and finalizedUpdatedAt. Its current-transaction xmin, customer actor, tenant/job/action, matching SMS kind, exact finalized job version and current state must match. Cancellation also joins the exact earlier claim version and unchanged customer/session while requiring cleared windows/reference; it projects the preserved prior window/hash. Reschedule projects the new active window/hash. No caller-supplied window or historical audit reconstruction.
- Cancellation online replay now requires metadata.finalizedUpdatedAt equal to the current job version. Old unversioned cancellation audits do not qualify. Pre-migration in-flight cancellations have no claim snapshot and cannot create a new finalized event; office review is required, not invented history. This compatibility boundary must be reviewed before any release.
- Apply forward migration 20260909200000_extend_appointment_email_events after the initial email-intent migration and before separately approved code rollout. Nothing is applied in production here. Snapshot storage failure prevents the provider call; post-acknowledgment event storage failure rolls back local finalization, not Calendar, and remains a recovery/review condition.
- Preference disposition is captured independently for each event, including blocked/invalid events. It is not permission, consent, a queue or a delivery claim. Future admission must bind event-time/current policy, consent, expiry and fresh tenant/job/recipient/credential authority, without automatically replaying historical events. Existing composition and recipient readers remain inactive.
- Proof: backend email-change-intents/ and readiness-report.md; 1190 backend/170 UI tests, 18 local migrations/19 crash cases including six new claim/finalization exits, 12 fresh-process reads, real snapshot/FK/receipt refusals and rollback/concurrency tests; zero provider calls. This does not solve external Calendar uncertainty or activate delivery.

## Earlier: APP-013 Initial Confirmation Email Intent (2026-09-09, recording only)

- This bounded section covers initial confirmation in the existing acknowledgment finalizer and inactive CREATE read-back finalizer. Reschedule/cancellation intent capture remains open; cancellation must preserve its old window before clearing current fields. No backfill from historical audits/current jobs.
- AppointmentEmailIntent records an immutable initial-confirmation event, not a delivery queue item: tenant/job/customer/intake-session identity, exact finalized job version, exact window, hashed calendar reference, source audit, optional matched CREATE operation, observed tenant-settings version and default-off email preference disposition. Fixed version 1/kind APPOINTMENT_CONFIRMED/state RECORDED. No email address, body, management credential, raw Calendar reference or provider request.
- Record only inside the same transaction as job finalization, existing SMS intent and appointment.initial_confirmed audit. Audit gains finalizedUpdatedAt matching that exact job version; PostgreSQL xmin must match the current transaction, refusing older committed receipts. A tenant/job/version-bound audit and matching unfinished-operation-free canonical state are required; CREATE read-back additionally requires its FINALIZED CREATE journal. No successful event can survive local rollback. Source audit and job-version uniqueness prevent duplication; database UPDATE rejection preserves snapshots. FK cascades permit existing job/tenant/audit retention deletion.
- The record captures the event even when preference is blocked/invalid, to distinguish a finalized event from delivery eligibility. It is never automatically replayed or sent when preferences change. Future admission must enforce event-time and current policy, consent, fresh tenant/job/recipient authority, deduplication, expiry and safe credentials. Recording does not solve provider acknowledgment loss or pre-finalization crashes.
- Forward migration 20260909190000_add_appointment_email_intent is supplied/tested locally and must precede any code release. Production migration/release require separate approval. No delivery worker/API/preview registration. Preference disposition is a snapshot, not authorization or proof of consent. Pre-migration confirmed jobs have no intent; no historical backfill is performed. Local persistence failure rolls back local finalization, not the external Calendar action, and remains a review/recovery condition.

## APP-013 Customer Email Event Preferences (2026-09-09)

- Approved bounded continuation: independent confirmation/reschedule/cancellation customer-email controls, default off. GET/PUT /communications/customer-email-settings use verified owner/admin tenant context, reject impersonation, and require an active tenant. No tenant or recipient is submitted. PUT accepts only canonical expectedUpdatedAt and exactly three boolean events: APPOINTMENT_CONFIRMED, APPOINTMENT_RESCHEDULED, APPOINTMENT_CANCELLED.
- Persist only TenantOrganization.settings.customerEmailPreferences = {version:1, events}; preserve SMS and unrelated root settings. Missing policy yields source default and all false; malformed policy yields invalid and all false. Invalid root settings cannot be overwritten. Unknown stored policy versions/fields require review rather than silent downgrade. Save uses tenant/version/status compare-and-swap and an atomic privacy-safe communication.customer_email_preferences_updated audit; stale writes return 409, uncertain writes require reload, never automatic retry.
- Response: {updatedAt, source:default|saved|invalid, events, recipientRole:customer, deliveryAvailable:false}. No customer address, raw settings, credential, email body or provider state. Both success/error responses are private/no-store. UI offers an explicit channel selection, requires review acknowledgment, clears stale responses on channel/token/session changes, and describes email switches as preferences only.
- No delivery consumer is connected to these preferences in this section. Permission is not consent, mailbox verification, finalized event proof or sending authorization. Existing SMS policy/worker behavior remains unchanged. No migration, provider setup, outbound calls, queue activation or credentials.

## APP-013 Appointment Email Recipient Snapshot (2026-09-09, inactive)

- Internal class `AppointmentEmailRecipientService.resolve({jobId, kind, expectedJobUpdatedAt})`, not an HTTP route, module provider or worker. Kind is confirmed/rescheduled/cancelled; UUID job and canonical millisecond UTC version required. Verified request context must have user, tenant UUID and owner/admin role with no impersonation. Submitted tenant/email overrides are ignored. Context fixtures do not prove Firebase/HTTP authentication.
- Exactly one parameterized SQL statement reads the current tenant-owned undeleted job, active tenant and undeleted job customer. It rejects version mismatch and any unfinished same-tenant/job CalendarOperation. Active review requires ACCEPTED, nonblank calendar reference and ordered minute-aligned windows; cancellation requires CANCELLED, null calendar reference and both windows null.
- Recipient comes only from exactly one CREATED_FROM conversation/job link with matching tenant columns, undeleted conversation/source customer and exact intake session binding. The conversation customer may be the original placeholder and need not equal the final job customer. ABOUT/FOLLOW_UP are not recipients. Multiple origins, even an invalid second origin, fail closed. No Customer.email fallback, newest-email selection or transcript/root-JSON projection.
- Only the intakeEmail subfield from a valid binding is projected. Version-1 captured state, bounded canonical authenticated-cipher envelope and normalized single mailbox are required; absent/declined/malformed/corrupt capture refuses. Decryption occurs after scope, lifecycle and ambiguity checks. Errors are fixed and input-free; no query/cipher cause is returned.
- Output is `{resolution:"recipient_resolved", sensitivity:"customer-private", snapshotOnly:true, deliveryAuthorized:false, tenantId, jobId, kind, jobUpdatedAt, recipient:{email, source:"conversation_intake", conversationId, conversationUpdatedAt, ownershipVerified:false}}`. This private payload must not reach logs, analytics, operator preview/history or a public endpoint. It contains no ciphertext, management credential or calendar payload.
- This is structural recipient resolution, NOT send eligibility, verified mailbox ownership, consent, event finalization, payment eligibility, provider truth or send-time freshness. Confirmed/rescheduled kind is caller-selected; current Job cannot distinguish their event identities. Legacy cancellation clears references/windows before provider finalization; cleared fields cannot prove deletion. A separately bound immutable finalized event must supply cancellation's previous window; never invent it or use an old audit as a current receipt.
- Future integration must establish independently configured email policy, required permission/consent, finalized event identity/snapshot, revalidated recipient/job versions, privacy-safe credential binding and durable idempotent admission/delivery/recovery. Resolver remains inactive. No schema, migration, existing API or delivery behavior changes.

## APP-013 Appointment Email Composition Contract (2026-09-09, inactive)

- Pure internal composeAppointmentEmail(snapshot, actions?) and previewAppointmentEmail(snapshot); no route, module registration, database, provider, logger or runtime consumer. Caller supplies verified canonical tenant/job state in any future integration; this function cannot establish authority, freshness, payment, consent or delivery eligibility.
- Snapshot: kind confirmed/rescheduled/cancelled; UUID tenantId/jobId; bounded control-free brandName/serviceType; E.164 supportPhone; status CONFIRMED/CANCELLED matching kind; calendarOperationPending exactly false; nonempty active calendarEventId or null on cancellation; canonical UTC-millisecond windowStart/windowEnd/updatedAt. Window endpoints must be ordered and minute-aligned to match displayed precision; updatedAt may retain milliseconds (calendar DTSTAMP uses seconds).
- Active actions require already-authorized absolute HTTPS managementUrl, explicit server-approved bare allowedManagementOrigin, exact /appointment/manage path, no userinfo/query, canonical URL spelling and 20-2048-character base64url/dot-compatible fragment. No signing, token verification, origin discovery or real credential issuance. Future verified adapter must bind origin/credential/recipient to the same tenant/job.
- Output: fixed templateId appointment_email:<kind>:v1, version 1, subject, HTML/text and sensitivity customer-private. Customer output may contain the bearer link and must never enter operator previews, logs or analytics. Escaped HTML; no external image/script/tracker; fixed input-free errors. Future MIME encoding/sending remains out of scope.
- Operator preview receives no action parameter, projects explicit display fields without accessing unrelated properties, returns previewOnly true, no private URL or calendar payload. This is not a role/auth boundary or protection against a caller deliberately placing secrets into display fields.
- Active messages show brand, full job reference, service type, full Eastern date/time endpoints including DST zone, fallback phone and private-link warning. Calendar attachment appointment.ics is RFC 5545 content with UTC dates, stable tenant/job-derived hashed UID, private class, escaped text and UTF-8 75-octet folding. No management action, customer contact/address, raw IDs, organizer/attendee/alarm or METHOD is copied into the calendar. It is a calendar copy, not synchronized scheduling; client duplicate/replacement behavior is not guaranteed.
- Cancellation rejects an actions argument, requires null event reference, labels the prior window and offers no management link/calendar attachment; advises removal of any saved copy.
- Evidence: backend email-composition/summary.json and browser-summary.json. 55 focused tests, 1075 backend/159 UI tests, local desktop/mobile rendering and fictional download, zero providers. No email-client/Calendar-import/live delivery acceptance. Existing 16-migration/11-crash disposable regression passes independently of this inactive renderer. No schema/API contract changes elsewhere.

## APP-013 Optional Customer Email Capture Contract (2026-09-09, review-ready)

- Existing authenticated/integration-scoped triage flow; no new endpoint or tool argument. Service scope is verified tenant plus ensured conversation ID and session ID. New serialized conversation creation rejects legacy duplicates/deleted sessions; no automatic repair/backfill.
- `Conversation.collectedData.intakeEmail` is version 1 with `status: asked | declined | captured`, `askedAt: ISO timestamp | null`, and `encryptedEmail` only for captured status. Uses existing AES-256-GCM ConversationMemoryCipher/key. Other JSON preserved; invalid state fails closed. No plaintext email in audit/status responses or new public job field. Customer master is unchanged; existing tenant-scoped ConversationJobLink associates intake data with the job.
- Accept exactly one syntax-valid ASCII mailbox in a standalone message or supported explicit email phrasing. Reject ambiguous/multiple/control-separated/invalid/unconfirmed mentions rather than guessing. Preserve local-part case and lowercase domain. No mailbox ownership or delivery verification. First captured address is immutable through this workflow; decline can later become captured on a clear volunteered address. Correction/master-contact reconciliation remains separate.
- Transaction-scoped advisory locks keyed by tenant/session serialize first conversation creation and email transitions. Capture/ask/decline and privacy-safe conversation.email_* audit commit together. Unknown commit outcome produces fixed unconfirmed error; retry reads committed state without duplicate capture. Locks do not serialize entire model turns or other writers.
- At-most-once optional prompt reservation before ready-residential/model create_job finalization; volunteered email skips question, skip/invalid/missing address adds no required job field, life safety bypasses capture. A reserved prompt can be lost before display; no exactly-once client-delivery guarantee. Persistent state is independent of bounded/closed transcript memory.
- Model receives only capture status in authoritative state instruction; email questions, echo, invented email/tool argument or delivery claim are forbidden. Runtime guard replaces email-bearing ordinary model replies with the next required intake question. This local proof does not establish all live model/language behavior.
- New real PostgreSQL concurrency, rollback/lost-ack, separate-process restart and AiService/JobsService/log/cipher/link composition proof; model/tenant prompt/notification sink synthetic, zero provider calls. 1020 backend/159 UI tests pass. Backend 00337a756a177d3752204acfb082c2bf774d431f, evidence/APP-013/email-capture/summary.json. No new schema/key/provider configuration, customer email delivery, migration outside fixture, production or release action.

## APP-013 Technician Notification Inbox Contract (2026-09-09, review-ready)

- `GET /technician/notifications` uses existing `x-technician-link` HMAC bearer credential; no operator/JWT/tenant-header fallback. Real link verification and ACTIVE TECH membership in the signed tenant precede reading. New controller registered in JobsModule source only, private/no-store errors/success, 30 reads per 60 seconds under existing throttler.
- One parameterized SQL statement joins AuditLog entityId to Job id as text and equal tenantId, then current assignedUserId/assignedUserTenantId to active TECH User. Signed tenant equality and undeleted job predicates are explicit. No requested job/technician/tenant IDs can widen access. Another active technician, tenant, unassigned/deleted job, non-Job audit or unknown action is excluded.
- Allowlist: job.assigned, job.reassigned, job.urgency_escalated, appointment.initial_confirmed, appointment.customer_rescheduled, appointment.customer_cancelled, job.technician_accepted, job.technician_en_route, job.technician_started, job.technician_completed. Reads existing committed audit records; no new event writes or provider calls.
- Returns `{snapshot:true,asOf,lookbackDays:90,limit:100,hasMore,items:[{id,jobId,action,occurredAt}]}`. Query takes 101, returns 100, timestamp-desc/ID-desc order, excludes future/older-than-90-day records. No audit metadata, actor details, customer contact/address/body, payment, provider or secure-management fields selected. Row/time cap is not a query-cost guarantee; production query-plan/load review remains.
- Current-assignment visibility is evaluated at the SQL read, not event creation. Earlier activity on currently assigned jobs may be shown; after reassignment/unassignment/deletion it disappears on refresh. This is a recorded job-activity snapshot, not proof of delivery, read state or present booking truth. No unread counts, read/dismiss persistence, timeline recovery or push/SMS/email notification.
- Existing technician workspace embeds explicit refresh/clear panel with same in-memory link. Fixed parser/labels, GET-only no-store transport, no cookies/storage or token in request URL. Clear or token change aborts/discards old results using non-secret session generation; unauthorized session stays disabled until replaced. Fifteen-second read timeout/error requires explicit refresh; server work can continue after client abort.
- Local evidence: aa5baddc925755c5db7ea786236f6c1de7a6bac9; 995 backend/159 UI tests; actual React browser/CORS/Nest/HMAC/SQL disposable-PostgreSQL proof (13 GET/13 OPTIONS), zero provider calls/inbox mutations. Real HMAC uses fictional fixture key/technicians; no deployed or production-scale acceptance. APP-013 remains Now and broad acceptance criteria unchecked.

## APP-013 Customer Messaging Settings Contract (2026-09-09, review-ready)

- Owner/admin GET/PUT `/communications/customer-messaging-settings`, server-verified tenant context, private/no-store responses and sanitized errors; source registration only. GET limit 30/minute, PUT 5/minute under existing throttling architecture.
- Persistence uses existing `TenantOrganization.settings.customerSmsPreferences`: exact `{version: 1, events: {APPOINTMENT_CONFIRMED: boolean, APPOINTMENT_RESCHEDULED: boolean, APPOINTMENT_CANCELLED: boolean, TECHNICIAN_ON_THE_WAY: boolean}}`. No schema migration. Missing policy in a valid object means legacy event eligibility; malformed root/property/version/events fails closed. Saving invalid root settings refuses instead of discarding unrelated data.
- PUT body exactly `{expectedUpdatedAt: canonical ISO timestamp, events: all four booleans}`. Tenant timestamp CAS plus strictly advancing timestamp preserves unrelated JSON keys; `communication.customer_sms_preferences_updated` USER audit with policy/version/timestamps commits in the same transaction. Stale or lost CAS refuses 409; unknown commit outcome is 503/unconfirmed and requires explicit reload.
- GET/success PUT returns only updatedAt, source (legacy/saved/invalid), and four enabled fixed rendered templates with key/body/template identifiers/version. Branding/timezone from this tenant; date and technician are fixed fictional examples, never customer or booking references. UI projects safe fields, has no custom text/channel/provider controls and stores tokens only in page memory.
- Both manual/lifecycle queue admission and fresh pre-send validation enforce the saved preference. Suppressed intent is STALE; suppressed queued record is DEAD_LETTER with fixed `suppressed_tenant_preference`. Re-enabling alone never replays records or starts workers. Consent, opt-out, quiet hours, provider eligibility and Calendar controls remain separate. Disabling cannot recall an in-flight provider call or remove the check-to-provider race.
- Local evidence: 989 backend/145 UI tests, actual browser/CORS -> isolated Nest guard/service -> disposable PostgreSQL with synthetic identity verifier; two saves, one stale refusal, tenant/role isolation, atomic rollback/concurrency and all-four-template suppression. Zero provider calls, no deployed/live acceptance. Backend 7d2a4eef0dee30447bee59e526d45a2f335c3299, evidence/APP-013/customer-messaging-settings/.

## APP-013 Subscribed Review Panel Composition (2026-09-09, inactive)

- CalendarReviewSessionPanel accepts an externally owned CalendarReviewHttpSession, subscribes to every descriptor transition with useSyncExternalStore and passes its non-secret snapshot into the existing keyed panel. No token prop, default fetch/origin, storage or app-route registration. Parent must bind on every identity/tenant/token change and clear/dispose on logout.
- Optional onClearSession callback preserves standalone reader compatibility; the composed panel clears both private client snapshots and the transport credential. Unmount cancels that panel's reads without destroying a potentially shared session. Remount starts with blank references/data; cleared/denied sessions remain denied.
- Backend a42f0a42660cb148734e67e81985a4765cc5bfae: actual browser-to-loopback proof, 20 GETs/20 preflights/19 synthetic reads, six observed cancelled connections and no stale publication after server completion. Firebase verifier and Prisma are read-only doubles, not real identity/database acceptance. Exact-origin noncredentialed CORS and CSP are fixture-only, not deployed settings. No interception/response fulfillment; server authority, no-store/privacy bounds and snapshot/request-only meanings remain unchanged.
- No mutation/recovery control, active module/route/worker, real-data/provider/production/release action. After review the agreed next step is APP-013 acceptance-gap assessment and user-facing workflow prioritization, not another automatic remediation section.

## APP-013 Review HTTP Adapter/Session Binding (2026-09-09, inactive)

- CalendarReviewHttpSession is an inactive seam, not an app route or composed UI. Constructor requires trusted origin and injected ReviewFetch; no default URL/fetch. Only HTTPS or explicit loopback HTTP; URL credentials/query/fragment/non-root path refuse. Origins must come from approved deployment configuration, never editable user input.
- bind({bearerToken, role}) rotates a non-secret generation every time, including same-token bind. Tokens are private in-memory fields; getSnapshot/subscribe exposes only sessionKey/role/read. Blank/malformed/runtime-invalid tokens and unsupported display roles erase prior credentials. clear/dispose/rebind invalidate old readers and cancel pending work. Parent integration must subscribe and replace/clear panel/client on every descriptor change; it remains unwired.
- Reader maps resource job|operation|requests and canonical UUID to exactly the three reviewed GET paths. Only Accept and bearer Authorization headers; credentials:omit, cache:no-store, redirect:error, referrerPolicy:no-referrer. No cookie/admin/dev/tenant header fallback, request body, arbitrary path or mutation method. Parent role is not authority; existing verified server role/tenant guards remain mandatory.
- Transport deadline 15 seconds across headers/body, with abort and generation checks. Success requires exact response URL/no redirect, JSON content type, no-store header, <=256 KiB declared/streamed bytes, valid UTF-8 and parsed JSON. Existing client validates/project-maps the result. Non-200 bodies are cancelled and omitted; failures are fixed non-private errors, no retry/polling. 401/403 erases credentials and rotates denied state while cancelling siblings. Abort cannot retract an already-received GET or guarantee distributed cancellation.
- Evidence 39a2c9b20a136c428979d027cc8bd45a70cc178f: 36 new adapter/session tests/135 UI total; real native-fetch loopback proof across adapter/client/parser/Nest/guards/context/service/filter, 16 GETs/15 read queries. Firebase verification and Prisma reads are synthetic. Real HTTP tenant/auth refusal, safe 503/manual refresh and in-flight tenant replacement pass with zero provider/mutation requests. Existing backend 962 tests and disposable 16-migration/11-crash regression pass. Browser suites remain separate unchanged regressions, not adapter browser/CORS acceptance.
- Prior pointer/table/step placement mistake repaired without changing active scope. Governance docs-consistency-check now includes execution-placement validation; four cases reject the exact swap, missing/duplicate status rows and broken numbering. Exact evidence/commands: backend readiness-report.md and calendar-review-http-session-summary.json.
- No component wiring, active route/module/worker, backend runtime/schema/dependency/provider configuration, production migration/backfill, real data/payment/message/secret/IAM/billing action, merge or deployment. Next proposed section is inactive subscribed panel/session composition with synthetic browser-to-loopback HTTP proof; live acceptance and recovery actions remain gated.

## APP-013 Read-only Review UI/Client Contract (2026-09-09, inactive)

- Unlinked CalendarReviewPanel accepts a non-secret opaque session-generation key, role and injected ReviewReader; there is no app route/navigation import, default HTTP adapter, token input/decoding or browser storage. Parent owner/admin role is only a display gate. Future integration must bind the reader to existing verified bearer/tenant authority and change the generation key on every credential/user/tenant transition. Never pass a bearer token as sessionKey.
- ReviewReader input: resource job|operation|requests, canonical lowercase reference UUID, AbortSignal. Result: HTTP-style status and unknown body. No mutation/provider method. Three independent manual views use idle/loading/ready/error states. New reads clear old view data; identity/role/reference/reader changes cancel pending work and clear views. Duplicate same-view clicks are ignored; unique pending ownership discards stale completions even if cancellation is ignored.
- Timeout 15 seconds; no automatic retry or polling. 401/403 clears all snapshots, cancels siblings and denies the current session key; reference edits cannot restore it. Other errors remain view-local, preserving explicitly separate partial snapshots. Fixed safe copy never renders raw errors. A failed read is not a recovery request or outcome.
- Parser requires exact snapshotOnly/requestOnly flags, UUID reference correspondence, supported actions/statuses/kinds, canonical timestamps, candidate/state consistency, boolean hasMore, no duplicate IDs and <=100 records. hasMore requires 100 returned records. Private/extra keys discarded via explicit projection. Unknown/malformed data fails closed; no clock-derived upgrade of server timing hints.
- UI labels empty/truncated limits, request-only history and separate-read semantics. Journal FINALIZED is not a current booking receipt; ABORTED is not proof of provider absence. No hold/recovery/execute/retry button. UTC versions/boundaries are observed snapshots, not permissions/countdowns/leases.
- Evidence 0e276f9f005afd4a3ab78e3d3fff140f1ff99179: 39 new focused UI tests/99 UI total, 14-page unchanged export, actual unlinked React component at 1440px/390px with real timeout/late discard, privacy/partial/error/access/keyboard/storage/200% root-text checks and zero external/mutation requests/errors. Four screenshots; desktop ready/mobile ready/mobile partial visually inspected. Backend 962 tests and unchanged real DB regression (16 migrations/11 prior crashes) plus four clean audits. Underlying HTTP auth/DB and component reader remain separate test seams, not integrated real Firebase/deployed acceptance.
- Source preview uses existing TypeScript/webpack in a loopback-only temporary bundle; no package, hosting, production route, schema or provider change. Current evidence/review commands: backend readiness-report.md and calendar-review-ui-summary.json. Next proposed section is inactive read-only HTTP adapter/session binding with isolated cross-layer tests; activation/mutations/live acceptance remain approval-gated.

## APP-013 Protected Read-only Review HTTP Boundary (2026-09-09, inactive)

- CalendarReviewController is test-composed only and absent from every application module. Declared GET routes: /scheduling/calendar-review/jobs/:jobId/operations; /scheduling/calendar-review/operations/:operationId; /scheduling/calendar-review/operations/:operationId/recovery-requests. No live routing, UI, mutation transport or worker is enabled.
- RequestAuthGuard -> TenantGuard -> CalendarReviewAccessGuard; trusted verified user/tenant and normalized owner/admin only. Existing production-mode bearer verifier checks revocation and configured issuer/audience. Developer headers refuse when development auth is disabled. No new auth mapping or credential/configuration action. UUID path validation plus service validation; any query parameter is 400. Body/custom headers cannot supply tenant, actor, scope, limit or service arguments.
- Delegates only to existing CalendarReviewStateService listForJob/read/listRecoveryRequests; DTOs/caps/filtering/ordering unchanged. Unknown/cross-tenant job history is empty; exact operation/request history is uniformly 404 before audit access. Snapshot-only hints are not authority/receipts/provider truth; request-only history is not execution or success evidence. Separate reads are not atomic or exhaustive.
- Cache-Control: private, no-store on success and controller-handled errors. Scoped CalendarReviewHttpFilter delegates to existing SanitizedExceptionFilter; HTTP error body is only statusCode plus existing generic message. Authentication 401, role/developer-header 403, malformed/query 400, absent operation 404, query/projection 503 and throttle 429 are tested. Internal refresh guidance is not returned verbatim; consumers must handle errors without claiming success.
- Class throttle: 30 requests per 60,000ms for each existing local route/IP tracker; both existing global guards are included in tests. Global guards precede auth, so this is not a verified-tenant-wide or distributed quota. Future composition must retain context middleware, auth dependencies, LoggingService and throttler setup; no infrastructure configuration is changed here.
- Evidence d1512b459a20db2a0cda5c74d8ed92ddd227f301: 45 new isolated HTTP tests/962 backend total, synthetic Firebase and database doubles with real guards/context/service/filter. Existing underlying real PostgreSQL suite separately passes all 16 migrations/11 prior crashes and readiness/history proofs, with zero real provider calls and cleanup verified. UI/browser regression and four clean audit results in backend readiness-report.md and calendar-review-http-summary.json. No new real-auth/deployed HTTP/HTTP-to-real-DB/process-crash or visual-inspection claim.
- No schema/dependency/provider configuration, production migration/backfill, real-data or payment action, message, secret/IAM/billing change, activation, merge or deployment. Review UI/acceptance, mutation transport/receipt semantics, clock/provider assumptions, customer/payment handoff, legacy repair and migration/release ordering remain gated.

## APP-013 Recovery Readiness and Request History (2026-09-09, inactive)

- Existing internal CalendarReviewStateService job/exact snapshots add recoveryReviewCandidate:applied_create|uncertain_create|null and recoveryReadbackNotBefore:ISO|null. Unfinished CREATE/APPLIED is a local review candidate; UNCERTAIN uses shared persisted readbackNotBefore or updatedAt+grace fallback. Future/invalid boundaries and unsupported/held/terminal/finished records cannot be candidates. Raw readbackNotBefore is now selected solely to derive these bounded hints; no target/window/customer/payment records are selected.
- New listRecoveryRequests({operationId}) reuses trusted user/tenant owner/admin checks and UUID validation before queries. Exact tenant-bound operation existence precedes audit access (missing/cross-tenant uniformly 404). Audit filters: tenantId, entityType CalendarOperation, exact entityId, actorType USER and the APPLIED/UNCERTAIN readback-request action allowlist.
- Select only audit id/action/createdAt. DTO items: requestId, kind:applied_create|uncertain_create, requestedAt canonical ISO. Never load or serialize actor identity, metadata, trace IDs, related customer/payment/provider records. Order createdAt DESC/id DESC; query cap 101, return cap 100, hasMore plus snapshotOnly:true/requestOnly:true. No pagination or complete-history guarantee.
- Request history proves only matching request rows at its query snapshot, not execution, success, provider state or absence of earlier recovery. Readiness is not permission/current job eligibility or receipt. Separate state/history reads are not one atomic snapshot. Existing mutation services independently recheck role/ack/version/status/deadline/evidence. Unknown query/projection errors are bounded 503, without retry/cache/private diagnostics.
- Evidence 911df72a3f77ef3caa42477f72fc3bacb1cfa27d: 30 new cases/917 total/59 focused; real 101-row cap/tie ordering/five-filter decoys, timing/clock rollback, unchanged reads and actual lost-admission-ack request-only visibility; 16 existing local migrations/11 prior crashes, UI/browser gates/four clean audits. No new migration/process crash or Firebase/HTTP/live acceptance. Exact commands: backend readiness-report.md and recovery-readiness-history-summary.json.
- No route/module/worker registration, mutation/recovery/provider call or production action. Protected read-only API boundary, UI/acceptance, mutation transport/receipt semantics, clock/provider assumptions, customer/payment handoff and migration/release ordering remain gated.

## APP-013 Reviewed UNCERTAIN CREATE Recovery (2026-09-09, inactive)

- Additive nullable CalendarOperation.readbackNotBefore via 20260909190000_add_calendar_readback_deadline; no backfill. Null rows retain persisted updatedAt + 10-second grace. Executor/eight-second write deadline unchanged. First admitted UNCERTAIN review persists the pre-existing read boundary; admission never shortens or restarts it. New field remains absent from public/review-state DTOs.
- CalendarUncertainRecoveryService.recover({operationId, expectedUpdatedAt, acknowledgeReadback}) is inactive/internal. Trusted user/tenant context, normalized owner/admin, UUID, canonical exact reviewed timestamp and true acknowledgment required. Only current UNCERTAIN CREATE/unfinished state with finite elapsed read boundary can be admitted. Client tenant/actor/deadline/target/evidence ignored; future RequestAuthGuard/TenantGuard required.
- Exact-version admission updates only updatedAt/readbackNotBefore and atomically writes USER appointment.uncertain_create_readback_requested. Metadata: jobId, reasonCode:UNCERTAIN_CREATE_REVIEWED, acknowledged:true, reviewedUpdatedAt, admittedUpdatedAt, readbackNotBefore. Job/status/event/window/claimed version/unfinished hold preserved; request audit is not completion.
- Acknowledged admission passes its exact server version to reconciliation. Shared persisted/fallback deadline is checked again before job/provider access; clock rollback returns pending without read. Existing evidence/job/future-window/CAS rules remain. On later unavailable read, persisted deadline renews the existing read-failure backoff; admission never renews it.
- Audit failure rolls back. Unknown admission acknowledgment returns bounded 503 and never reads/retries. Fresh explicit review after refresh can recover without resetting the original deadline. Same-version admission is single; newer explicit reviews can supersede in-flight reads with one finalization/intent. Version ownership is not exclusive read lease. Internal status only, no public receipt/automatic takeover/writer/clear.
- Evidence 1e389842494a730e21568d885b4db280a5fd0e44: 42 new cases/887 total/79 focused, real exact-boundary and future-deadline refusal, clock rollback, deadline-preserving lost acknowledgment/fresh-service recovery, backoff, audit rollback and ownership races; 16 local migrations/11 prior crashes, UI/browser gates and four clean audits. No new process-crash or Firebase/HTTP/provider acceptance. Evidence: backend readiness-report.md and uncertain-create-recovery-summary.json.
- Migration applied only to disposable local fixtures; release migration/order needs separate approval. Forward-clock/cross-host skew and delayed provider completion remain assumptions, not solved by this change. Readiness/request-audit visibility, protected review API/UI, customer/payment handoff, legacy repair and acceptance remain gated. No activation/production action.

## APP-013 Reviewed APPLIED CREATE Recovery (2026-09-09, inactive)

- CalendarAppliedRecoveryService.recover({operationId, expectedUpdatedAt, acknowledgeReadback}) is inactive/internal. Existing trusted user/tenant context and normalized owner/admin role precede queries; UUID, exact canonical timestamp and explicit true acknowledgment are required. Future invocation requires RequestAuthGuard/TenantGuard; no submitted tenant/actor/target/evidence authority or new route/UI.
- Only tenant-bound current APPLIED CREATE with finishedAt null is admitted. Conditional exact-version update advances only journal updatedAt and atomically creates USER appointment.applied_create_readback_requested. Audit metadata: jobId, fixed APPLIED_CREATE_REVIEWED reasonCode, acknowledged:true, reviewedUpdatedAt, admittedUpdatedAt. Job/status/target/window/claimed version/unfinished hold remain unchanged. Audit means request, not completion.
- Only acknowledged admission invokes existing reconciliation with server-derived tenant/operation/admitted expectedUpdatedAt. Optional reconciler version precondition refuses stale state before job/Calendar reads; existing callers unchanged. PENDING/UNCERTAIN/held/terminal/unsupported work is not admitted, and existing UNCERTAIN grace is not bypassed. Existing matching-evidence and job/journal finalization CAS remain authoritative; no Calendar writer or message processing.
- Admission audit failure rolls back; unknown admission acknowledgment is fixed 503 with no read or retry. After admission, stale entry/exception/unknown result is fixed refresh-required 503. Result allowlist is internal status only: finalized/already_finalized/pending/needs_review, not public booking receipt. No compensation/rearm/clear or automatic repeat.
- Version ownership is not an exclusive provider-read lease: a newly refreshed explicit review can supersede an in-flight read. Same-version concurrency admits once; different explicit versions may each record a request, but finalization CAS prevents duplicate confirmation/intent. Lost admission acknowledgment leaves APPLIED/new version plus request audit; only a fresh explicit review may proceed. Unavailable/unverified evidence retains UNCERTAIN/NEEDS_REVIEW.
- Evidence 52e3e25fbe6749a694d78f29e8af2f7b361c0360: 35 new unit cases/845 total/70 focused, real audited read-back and concurrency, rollback/lost acknowledgment, fresh-service explicit recovery, pre-read newer hold and in-flight superseding-review races; 15 migrations/11 prior crashes, UI/browser gates and four clean audits. No new process-crash/Firebase/HTTP/provider acceptance. Review commands: backend readiness-report.md and applied-create-recovery-summary.json.
- UNCERTAIN ownership/persisted grace, request-audit visibility, protected review API/UI, customer/payment handoff, post-read/provider/payment/clock risks, legacy repair/retention and acceptance remain gated. No activation or production action.

## APP-013 Privacy-Safe Calendar Review State (2026-09-09, inactive)

- CalendarReviewStateService.listForJob({jobId}) and read({operationId}) are internal and inactive. Existing trusted user/tenant identity plus normalized owner/admin role precede all queries; references must be UUIDs. Future invocation requires RequestAuthGuard/TenantGuard. No submitted tenant/actor authority, route, UI, worker or new authentication mechanism.
- Per-job history selects at most 101 rows ordered createdAt DESC then id DESC, returns at most 100 items plus hasMore and snapshotOnly:true. No pagination/tenant-wide inventory. Exact composite tenant/operation refresh is independent of the history cap. Missing/cross-tenant detail is 404; unknown/cross-tenant job history is empty. Empty history is not proof of no legacy/provider work.
- Database select allowlist: id, jobId, action, status, createdAt, updatedAt, finishedAt. Explicit DTO: snapshotOnly:true, operationId, jobId, action, status, canonical ISO createdAt/updatedAt, nullable ISO finishedAt, pendingHoldReviewCandidate. No private target/event/window/text, claimed job version, tenant/related customer/payment/policy record or token is loaded or serialized.
- pendingHoldReviewCandidate means only observed CREATE/PENDING/unfinished; it is not authority, orphan detection, provider truth or booking confirmation. Caller must separately acknowledge and invoke the existing exact-version hold; any later execution/version change can invalidate the snapshot. All other actions/statuses have a false hint and retain historical metadata. Reads are uncached, have no writes/audit/provider/recovery effects, and return fixed refresh-required 503 on unknown query/projection failure.
- Evidence 880658a68a8d8078bb6c614abd21c9e35c04bd4f: 29 new unit cases/810 total; real 101-row cap/tie ordering/exact refresh, unchanged read snapshots, reviewed-hold refresh and committed-attempt stale-hold refusal; 15 migrations/11 prior crashes, UI/browser gates and four clean audits. Synthetic contexts/provider seams are not Firebase/HTTP/live-owner acceptance. Exact review commands: backend readiness-report.md and review-state-projection-summary.json.
- Point-in-time/capped history is not a global hold inventory, current Job receipt or recovery authorization. Attempted-operation ownership, protected review API/UI acceptance, customer/payment handoff, post-read/provider/payment/clock risks, legacy repair/retention and release remain separately gated.

## APP-013 Reviewed PENDING CREATE Containment (2026-09-09, inactive)

- CalendarPendingReviewService.hold is an unregistered internal owner/admin review action. Verified request context supplies tenant and actor; caller-provided identity fields are ignored. Acknowledgment must be true, operation ID a UUID, and reviewed updatedAt an exact canonical timestamp. Future invocation requires existing RequestAuthGuard/TenantGuard; no authenticated route or UI is introduced.
- Only exact current tenant-bound PENDING CREATE/unfinished version may move to NEEDS_REVIEW. Conditional status/version competes with executor ownership: hold-first blocks its attempt, executor-first refuses the stale hold. No timeout/abandonment inference; review can intentionally stop an unattempted operation even when a request is still preparing to execute it.
- Only journal status/updatedAt and one USER appointment.pending_create_held audit change atomically. Job, claimed version, saved event/window and unfinished uniqueness lock remain. Metadata: jobId, fixed PENDING_CREATE_REVIEWED reasonCode, acknowledged:true, reviewedUpdatedAt; no provider/customer/payment payload. Audit failure rolls back; unknown acknowledgment returns fixed refresh-required 503 without retry. Stale/repeated/attempted/terminal/unsupported work is 409; no clear/rearm/reinsert.
- Evidence 91aae55f7b7d0bda9344ee50a76cb4d46583614b: 27 new unit cases/781 total; real context-role/tenant/ack/version/action/status proof, concurrent single audit, audit rollback/lost-commit acknowledgment, both executor race orders and fresh stopped-executor refusal. 15 migrations/11 prior crashes, five unchanged browser regressions/four clean audits pass. Auth/provider seams are synthetic, not Firebase/HTTP/live-owner acceptance.
- Containment is not provider-absence proof, repair, restart execution, terminal resolution or release authority. Service remains unregistered/unrouted/unscheduled. Review-state projection, attempted-operation recovery ownership, customer handoff, provider/payment/clock races, legacy repair/retention and acceptance remain open. Exact evidence: backend readiness-report.md and pending-create-review-summary.json.

## APP-013 Guarded CREATE Fresh Receipt (2026-09-09, inactive)

- The inactive journaled booking service returns the existing appointment_confirmed/job/appointment/managementToken shape only after a fresh signed tenant/job/session-scoped receipt read. Exact signed window, nonblank server-expected event ID, ACCEPTED/undeleted job and no unfinished journal are required. New execution also requires the exact tenant-bound FINALIZED CREATE journal, finished timestamp and matching saved event/window; settled replay instead matches its observed job version/event.
- Executor finalized/already_finalized is no longer a sufficient response. Preflight replay data/token is discarded and read again. Pending, review-needed, unknown outcomes or failed receipt reads become fixed office-review 503, never a success-shaped response or stale token fallback. Preflight/claim refusals remain bounded. This changes only the unregistered internal path, not an active endpoint.
- Receipt reading has no provider, availability, mutation, finalization, audit, notification, payment or recovery side effect. Existing mapped JobRecord/appointment/token fields are retained; no new journal/policy/payment payload is exposed. This proves current local settlement at the query snapshot, not external Calendar freshness or a lock against subsequent changes.
- Evidence 10d64d1fc8cb7844ee5188e2d3126004df888a7c: 12 added unit cases/754 total, real canonical receipt/replay/private token checks, seven post-finalization job/journal changes and one replay-version race refusing stale output while retaining winners/committed intent/audit, plus independent authority/proof refusals. 15 migrations/11 prior crashes, five synthetic browser suites and four clean audits pass; zero real provider calls.
- No module/route/worker activation, provider configuration or payment-policy change. Recovery/office-review ownership and PENDING restart handling, customer payment handoff, post-claim/provider/clock risks, retention/legacy repair and acceptance remain open. Exact evidence: backend readiness-report.md and guarded-create-receipt-summary.json.

## APP-013 Guarded CREATE Composition (2026-09-09, earlier/inactive)

- New internal JournaledAppointmentBookingService accepts the existing signed booking input and calls the exact shared SchedulingService preparation path used by legacy confirmation. Tenant/job/session/signed-slot, enabled/lifecycle/journal/service/payment and availability guards precede reservation. Preparation includes private canonical data, is not serialized by any route and is not durable authority.
- Canonical job/version/window/label plus server Calendar/time-zone configuration feed CREATE journal reserve; no caller-supplied operation ID/payment assertion/Calendar target is consumed. Journal canonical payment/version checks remain independent. Only an acknowledged new operation reaches the one-shot executor.
- Lost reservation acknowledgment stops with fixed office-review 503; no reserve retry, inferred-ID lookup, legacy fallback, compensation or insert occurs. Pending/review/execution error retains the durable reservation; customer replay cannot take over existing unfinished work. PENDING restart and recovery/office-review ownership remain separate activation prerequisites.
- Internal statuses finalized/already_confirmed/pending/needs_review are not a public receipt contract. Finalized means executor read-back finalization or historical receipt; replay is the existing settled admission snapshot. No public claim of current Calendar state or new message/operations-notification processing is added.
- Evidence a092344f816a114333c12911d6e5da331100384e: 14 new unit cases/742 total; real composed signed-request success/replay, thrown insert acknowledgment with read-back, unavailable/absent holds, lost reservation acknowledgment, payment change and concurrent one-attempt/intent/audit. 15 local migrations/11 prior process crashes, five synthetic browser suites and four clean audits pass. No provider calls.
- New service remains unregistered/unrouted/unscheduled; live legacy confirmation uses shared admission only. Public-receipt mapping, customer handoff, explicit recovery/office-review ownership, post-claim/provider/clock risks, retention/legacy repair and acceptance remain open. No activation or release authority. Exact commands: backend readiness-report.md and guarded-create-composition-summary.json.

## APP-013 Journal CREATE Payment Admission (2026-09-09, inactive)

- The internal journal transaction now re-evaluates canonical shared payment policy for CREATE from the tenant/job/undeleted/exact-version snapshot and related payment ID/status/updatedAt. Locked states refuse before job/journal writes. Caller assertions and browser returns are not authorization; upstream request/slot/availability/payment guards remain mandatory.
- Successful-payment admission adds a payment ID/tenant/SUCCEEDED/version relation predicate to the job claim. No-requirement/approved-exception decisions retain the job-version guard. This is statement-snapshot protection only; no payment lock, post-claim revocation handling, amount validation or payment-provider mutation is added. Existing shared default/exception semantics are unchanged.
- RESCHEDULE/CANCEL payment behavior is unchanged. No payment details are persisted in the journal. Job claim and journal insert remain atomic, and insert failure rolls both back without changing payment rows. Repeat reserve is refused, not a new operation or a success receipt.
- Evidence bb8859431fbb90525940fe41cc6278d6d659995c: 17 new unit cases/728 total; ten real unpaid refusals, three allowed/repeat-refusal cases, four committed payment/policy races, paid insertion rollback; 15 local migrations/11 prior crashes, five synthetic browser suites and four clean audits. Fixture setup alone mutates fictional payment/policy rows; no real provider calls.
- Inactive/unregistered service only. Guarded CREATE integration and explicit execution/recovery/office-review ownership, customer handoff, post-claim/provider/clock risks, legacy repair/retention and acceptance remain open. No activation, migration outside the disposable fixture or release. Exact commands: backend readiness-report.md and journal-payment-admission-summary.json.

## APP-013 Initial CREATE Payment Admission (2026-09-09)

- Before a new reservation through the existing signed initial-confirmation entry point, SchedulingService evaluates persisted job policy and related payment using the shared payment-gate reducer. Required unpaid states return fixed office-review 409 before Calendar availability or writes. Tenant/job/session authority, unfinished-state/lifecycle/service/slot validation remain first.
- Existing finalized same-window replay stays read-only and is not retroactively blocked or charged. NOT_REQUIRED and existing approved manual-exception semantics remain compatible; this changes enforcement location, not amounts, pricing, exception/refund policy or payment-provider behavior.
- When SUCCEEDED is the basis for admission, reservation update requires observed payment ID/tenant/status/updatedAt plus existing job-version/unreserved/journal conditions. Committed refund/version/replacement before the statement snapshot prevents reservation. No runtime payment write occurs; later concurrent payment changes are not globally serialized.
- Evidence: 303765149af178082146b386e30c7faa9e630b92; eight new unit cases/711 total, ten real unpaid refusals, three allowed/replay paths, three committed-payment races with exact preservation and tenant/session checks. All 15 migrations/11 prior crashes, unchanged UI/browser gates and four clean audits pass. Fixture-only payment mutations, zero real provider calls.
- No journal integration/worker activation or checkout UI is added. Customer payment handoff acceptance, post-claim races, guarded CREATE integration and legacy recovery remain open. Evidence: readiness-report.md and initial-booking-payment-summary.json.

## APP-013 CREATE Active-Attempt Coordination (Inactive)

- PENDING remains exclusively owned by the authorized executor and cannot be read, expired or held by reconciliation. The executor conditionally advances the exact journal/job claim to UNCERTAIN before the provider seam; only that winning caller may attempt the persisted CREATE ID.
- Fresh UNCERTAIN returns pending before job lookup, Calendar access or persistence until ten seconds after the persisted attempt timestamp. The executor passes an absolute attemptDeadline at that same timestamp plus eight seconds; database claim/lookup latency consumes this budget. At expiry the executor conditionally holds without insertion. The Google creator rejects invalid/exhausted deadlines before credentials, uses only the remaining duration for AbortSignal and rechecks wall-clock expiry after credential/header loading before fetch. A delayed timer alone cannot authorize a late POST; client abort is not proof of provider-side cancellation.
- When the adapter exits, the executor conditionally advances UNCERTAIN to APPLIED before read-back. APPLIED means the client attempt is quiescent and recovery may read; it is not proof that the event exists or that Calendar accepted the insert. Matching identity/window/version evidence remains mandatory.
- Unknown APPLIED-write acknowledgment reloads current state. A crash before handoff leaves UNCERTAIN; after grace, read-only reconciliation may inspect the saved target and finalize or hold it. No path retries CREATE, generates a replacement event ID, rearms UNCERTAIN, clears the reservation or treats absence as permission to insert.
- The ten-second grace is coupled to the reviewed eight-second creator bound. Changing the adapter or either constant requires re-review of active-reader concurrency, delayed authentication, process-crash and provider-uncertainty proof before activation. This is not a retry lease, eventual-consistency guarantee, distributed Calendar/PostgreSQL transaction or global scheduling lock.
- These services remain unregistered, unrouted and unscheduled. Authorized CREATE integration must preserve tenant/auth/payment/availability guards and explicit executor/recovery/office-review ownership; no standalone recovery activation is permitted by this contract.

## APP-013 CREATE Persisted-Deadline Safeguard (Inactive, 2026-09-09)

- Backend `3238c40ac959832c9d9bb808860bf8520c404f47` corrects the former adapter-relative timeout origin. No timing constants, schema, public API, module registration or live scheduling switch changed. The deadline is private internal input, absent from provider JSON and public output.
- Eleven new unit cases (703 total) and two clock-advanced real PostgreSQL commit/lookup cases pass; expired work retains the claimed job, event identity and unfinished hold without creator/reconciler/audit/intent work. Existing APPLIED handoff, 15 migrations/11 prior process crashes, five browser suites and four clean audits pass.
- This is not a distributed fence or provider absence guarantee. Clock skew/suspension, post-dispatch processing, authorized integration and explicit recovery/office-review/retention policy still need review before activation. Evidence: backend readiness-report.md and create-absolute-deadline-summary.json.

## APP-013 CREATE Calendar Read-Back Reconciliation (Inactive)

- Owner reviewed journal foundation and approved continuation. Narrow `CalendarEventReader` and Google GET-only implementation feed `CalendarCreateReconciliationService`; neither is registered, scheduled or routed. No Calendar write or public API is added. All provider observations in acceptance tests are synthetic.
- Reconciliation looks up CREATE operation by composite tenant/operation identity, then requires the exact current undeleted ACCEPTED local reservation/version/window/label with no Calendar reference. FINALIZED returns a historical `already_finalized` receipt, not a claim of current Calendar state. ABORTED/NEEDS_REVIEW are not rearmed; unsupported actions fail closed.
- Matching evidence requires saved event ID, private tenant/job/`signmonsCalendarOperationId` markers, confirmed single blocking timed event, nonempty bounded ETag and exact start/end instants. Offset-free/all-day/recurring/nonblocking/nonstandard/mismatched events are rejected. Arrival window must not have begun; this is rechecked inside finalization. Existing unjournaled/legacy events cannot be adopted.
- Journal FINALIZED/finishedAt/version, job Calendar reference/version, canonical confirmation SMS intent and `appointment.initial_confirmed` system audit commit atomically. Audit actor SYSTEM_AI/`calendar-reconciliation` distinguishes recovery from customer action; metadata contains journal/intent IDs, fixed evidence code and ETag SHA-256 hash only. No immediate enqueue/send/notifier runs.
- Provider GET is encoded to the saved Calendar/event target, uses read-only scope, redirects fail and the HTTP call has an eight-second timeout. Only allowlisted identity/time/version fields escape the adapter. 404/410 mean unverified, not safe absence; other HTTP/auth/transport/JSON failures mean unavailable. No raw errors, payloads or credentials are logged/returned.
- Missing/conflicting/past-window evidence or changed local claim is NEEDS_REVIEW; unavailable provider/persistence outcomes are UNCERTAIN/pending. Holds retain the unfinished-job uniqueness lock. Conditional original journal status/version blocks late reads/failures from replacing newer completion/review decisions. Commit acknowledgment loss re-reads the receipt; failed writes roll back all four records. A later manual Calendar edit can still diverge after the observation; no distributed atomicity claim.
- Local proof includes three new process exits after synthetic read, before finalization commit and after acknowledged commit, in addition to six reservation crash cases. Nine total crashes, 15 existing local migrations, real rollback/concurrency/late-read/ack-loss checks and zero provider calls passed. Full commands and limitations are in backend APP-013 evidence.
- Activation remains prohibited until journal-aware customer/dispatch/message pending guards and guarded CREATE writer (saved ID plus operation marker), bounded worker ownership/retry policy, review controls and retention policy are reviewed. Reschedule/cancel reconciliation, historical repair, dependency remediation and live acceptance remain open; prior journal migration and any provider configuration/release require separate approval.

## APP-013 Calendar Operation Journal Foundation (Inactive)

- Owner approved the Calendar reconciliation/crash-resilience recommendation on 2026-09-08. This checkpoint supplies persistence and local fault proof only; no API, worker, provider adapter or SchedulingModule consumer is activated.
- `CalendarOperationJournalService.reserve` atomically creates a PENDING journal and conditionally claims CREATE/RESCHEDULE/CANCEL local state. It requires exact current tenant/job version, undeleted compatible lifecycle and observed window/event; versions advance monotonically. CREATE accepts only an unreserved CREATED job; RESCHEDULE/CANCEL require ACCEPTED with a complete ordered window and event ID. Upstream auth/payment/signed-slot/availability checks remain mandatory before eventual integration.
- Each record stores trusted server Calendar ID/time zone, stable generated 32-hex CREATE event ID or the existing target, previous status/event/window/label, desired window/label, expected/claimed job timestamps and creation/update times. A cancellation retains the target even after its local claim clears it. Calendar identifiers and scheduling text remain private server-side; no public serialization, raw provider payload, management credential or message body is introduced.
- Migration `20260908180000_add_calendar_operation_journal` adds composite tenant/job foreign keys and SQL checks for action snapshots, ordered windows/versions and terminal status/time agreement. The partial unique index on tenant/job where finishedAt is null blocks multiple unfinished operations, including UNCERTAIN and NEEDS_REVIEW. Status values are PENDING, UNCERTAIN, APPLIED, NEEDS_REVIEW, FINALIZED and ABORTED; this service only creates PENDING. No terminal transition or force-unlock is offered.
- Journal insertion and local claim commit together or neither commits. A journal means intended work, NOT Calendar success. No notification intent, successful-appointment audit, external request, automatic retry or rollback is performed. Hard-deleting a referenced job or tenant is restricted, including completed records; approved archival/privacy deletion policy is a prerequisite before activation.
- Local tests exercise all 15 migrations and six process exits: before/after commit for each action. They prove local atomicity and persisted restart evidence, not provider-side recovery. Existing scheduling callers still bypass this inactive foundation, so prior Calendar ambiguity/pre-finalization risks are NOT closed.
- Next approved direction remains bounded APP-013 journal-aware integration/reconciliation: preserve request guards, persist external version/ownership evidence, read before retry, protect concurrent external writes, atomically finalize journal/job/audit/SMS intent, and surface unresolved cases for office review. No full Calendar/PostgreSQL atomicity, historical repair, live acceptance or production migration is claimed.

## APP-013 Transactional SMS Lifecycle Contract (Review Checkpoint)

- `POST /communications/sms/transactional` accepts a job UUID, one of four versioned template keys, and an idempotency key under verified owner/admin/dispatcher tenant context. Recipient and content are resolved server-side.
- Missing, cross-tenant and soft-deleted jobs return the same not-found response before rendering or queue access.
- Cancellation messages require stored `CANCELLED` job status. Other templates reject cancelled or completed jobs with HTTP 409.
- Confirmation/reschedule messages require a persisted calendar event and a complete, ordered service window. Technician-on-the-way messages require a current assignee and stored `EN_ROUTE` technician status. Unsupported state returns HTTP 409 before queue creation.
- After Calendar acknowledges initial insertion, database finalization conditionally matches the tenant/job ACCEPTED reservation and atomically persists the calendar reference, confirmation SMS intent and `appointment.initial_confirmed` customer audit containing intent linkage only. Queue/operations-notification/logging failure after that commit cannot undo booking. Cancellation/reschedule finalization is defined below; neither uses direct post-commit scheduling queue calls now.
- Failed/ambiguous finalization after acknowledged insertion retains the reservation for office review rather than deleting the calendar event or releasing the slot. Same-window retry without a stored reference cannot claim success or insert again; finalized replay does not capture a second intent. Closed/deleted requests cannot reopen through initial confirmation. Calendar/database atomicity and pre-finalization crash reconciliation remain unsolved; the existing pre-acknowledgment calendar-error rollback is unchanged and does not resolve unknown provider outcomes. An absent intent cannot be repaired from this screen.
- A changed technician `on_my_way` records a `SmsEnqueueIntent` inside the job/audit transaction. Intent-write failure prevents that transaction committing; post-commit queue/logging/provider failure cannot reverse committed status. No-op status replays create no new intent. Intent identity includes tenant/job/template plus canonical state hash; on-the-way hashes include `technicianStatusUpdatedAt` to distinguish departures.
- Immediate and scheduled intent processing remain gated by `smsDeliveryEnabled`. A conditional 60-second claim expires after crashes; retries reuse the existing canonical queue identity. Recovery rejects changed/deleted/incompatible snapshots as `STALE`, backs off policy/configuration/queue failures and stops as `FAILED` after five failures. `QUEUED` indicates acknowledged enqueue, not delivery. Earlier on-the-way hashes without the departure timestamp fail closed; appointment hashes are unchanged.
- Cancellation retains a pre-Calendar local CANCELLED claim, now matching original tenant/job/version, undeleted state and calendar/window. No cancellation intent is captured until external deletion acknowledgment. Finalization conditionally matches the claimed version and atomically advances the job version, records `APPOINTMENT_CANCELLED` intent and `appointment.customer_cancelled` CUSTOMER audit with only intent linkage. The explicit version advance is monotonic even within one clock millisecond. Changed/cross-tenant/deleted claims cannot finalize; intent/audit/commit failure rolls back those writes.
- After acknowledged Calendar deletion, finalization failure returns office-review-required and never restores an active appointment. Post-finalization worker, operations-notification or logging failure cannot reverse cancellation. A CANCELLED replay requires tenant-bound finalization audit; otherwise legacy/in-flight/crash-stranded records require office review. A finalized replay creates no new Calendar request/intent/audit. No historical backfill or repair UI is added.
- Calendar and the database remain non-atomic. The existing pre-acknowledgment compensation is retained but matches the exact claim version; it cannot overwrite a later finalized cancellation. An unknown deletion outcome or process loss before finalization still needs manual reconciliation, and errors do not promise the event remains scheduled. The customer view still reflects local status, not independent Calendar proof. Absent intents cannot be recovered by the notification center.
- Rescheduling claims the new local reservation only if original tenant/job/undeleted ACCEPTED status, calendar/window and exact version match. After Calendar PATCH acknowledgment, finalization matches the claimed version/window and atomically advances the version, records `APPOINTMENT_RESCHEDULED` intent and `appointment.customer_rescheduled` CUSTOMER audit. Existing `previousAppointmentLabel` and `appointmentLabel` are retained; `notificationIntentId` and `finalizedUpdatedAt` are additive audit metadata. All claim/finalization/compensation versions advance even within one clock millisecond.
- Same-window reschedule replay requires tenant/job audit matching exact current `updatedAt`; local dates alone do not prove completion. Pending/legacy/changed snapshots fail closed to office review, including unrelated edits that conservatively invalidate the proof. Finalized replay makes no new Calendar call/intent/audit. Finalization failure after acknowledged PATCH keeps the new local reservation and never rolls Calendar back; intent/audit writes roll back together. Later worker/operations-notification/logging failure cannot undo finalization.
- Reschedule pre-acknowledgment compensation still exists but matches the exact claimed version/window. Unknown Calendar outcomes, crashes before finalization and concurrency between independent external operations are not reconciled automatically; errors do not guarantee the original time remains. Local customer status is not independent Calendar verification. No global external-operation serialization, historical backfill or absent-intent recovery is included.
- Durable capture covers initial appointment finalization, post-Calendar cancellation/reschedule finalization and technician departures. Owner/admin retry of exhausted intents is defined below; this does not override suppression or replay a queued/dead-letter event. Intent recovery permits these four current templates only, validating the recorded state hash before queue insertion. Cross-system pre-finalization gaps remain explicit.
- Lifecycle queue identity is derived from the template key plus a SHA-256 digest of template-relevant canonical state. The durable queue key remains tenant-keyed and one-way; duplicate lifecycle execution reuses the same event.
- Transactional queue records retain the state digest. Immediately before provider access, the worker reloads the composite tenant/job record and verifies current lifecycle, recipient, tenant brand/timezone, schedule and relevant technician state against that digest. Missing, incompatible or changed state is dead-lettered before send; transactional records without verifiable state metadata fail closed.
- Send-time validation narrows but cannot eliminate the check-to-provider race; external delivery is not atomic with a later concurrent lifecycle mutation. Remaining automatic assignment, other technician, payment and dispatcher events stay APP-013 work.
- `GET /communications/sms/history` returns bounded tenant/job history without message bodies, recipient phones or provider identifiers. Existing BE-008 consent, quiet-hour, encryption, idempotency and delivery controls remain authoritative.
- `/app/notifications` reads history with `limit=100` and optional UUID job filter, plus separate enqueue-intent and capability reads. History status filters/counts apply only to loaded history, not tenant-wide totals. Sent is explicitly delivery-unconfirmed; failed/dead-letter entries require attention. This view cannot detect an absent intent; only the exhausted-intent recovery below is supported.
- Operator credentials stay in page memory; token/job changes and session clearing invalidate pending responses and clear records. Generic errors do not render raw server payloads. The server remains authoritative for tenant/role access; no developer-auth or provider mutation control is added to this screen.
- `GET /communications/sms/enqueue-intents` is read-only/no-store under the same owner/admin/dispatcher tenant boundary. It returns the latest 100 intent IDs, job IDs, template key, status, attempt count, bounded error code, next-attempt time, linked communication-event ID, creation time and `updatedAt` (additive retry-concurrency timestamp). It omits state hashes, recipients and content. The notification center consumes it with independent loading/error state; successful history survives intent-read failure and vice versa.
- Intent job/status filters operate locally within the latest 100 tenant records, not a server-side job query. Copy/counts label this subset; an empty result cannot establish complete notification coverage. Initial confirmation, reschedule, cancellation and technician departure intents exist; backfill/reconciliation remain absent. Pending may reflect disabled delivery, a claim or backoff; next-attempt time is not a promised send. QUEUED is acknowledgment, not delivery; STALE/FAILED are stopped for review. Token/job edits and session clearing invalidate all reads, including late capability responses.
- `GET /communications/sms/capabilities` is authenticated, tenant-bound, private/no-store and throttled at 30 requests per 60,000 ms. It returns only `{ "canRetryEnqueueIntent": boolean }`: owner/admin true, dispatcher false; other roles denied. It shares the POST role policy and is a UI hint, never authorization for a later write. Failed/missing/non-true responses keep controls unavailable; the UI does not decode claims or use developer headers.
- The UI offers review only for supported FAILED/five-attempt/unlinked intents with a canonical listed timestamp and verified capability. Review displays job/intent/template/version and requires a fixed reason choice plus an unchecked-by-default acknowledgment of possible later SMS. Cancellation sends nothing. One submission is allowed in flight; its reviewed snapshot is cleared immediately, and every outcome requires a new manual load before another review. A 15-second timeout, network/server or malformed-success response is uncertain: the server may have accepted. No automatic resubmission occurs. Token/job/session edits suppress late POST messages but do not undo a request accepted server-side. This screen cannot force STALE recovery, send directly or replay dead letters.
- `POST /communications/sms/enqueue-intents/:intentId/retry` is owner/admin only, private/no-store and throttled at 5 requests per 60,000 ms using the existing process-local tracker. It accepts only `acknowledgeRetry: true`, `reasonCode` (`CONFIGURATION_REVIEWED`, `CONSENT_POLICY_REVIEWED`, `TRANSIENT_FAILURE_REVIEWED`) and exact canonical UTC-millisecond `expectedUpdatedAt`; tenant/actor derive from verified claims. Returns 202 `{ "status": "pending" }`, not queued/sent/delivered.
- Retry eligibility: same-tenant FAILED intent at five failures, no acknowledged communication-event link, current reviewed timestamp, supported template and compatible unchanged canonical job digest. Missing/cross-tenant is 404; ineligible/state-changed/stale/concurrent/repeated submission is 409; malformed input/extra fields is 400. Conditional reset to PENDING/zero attempts/current due time and `communication.enqueue_intent_retry_requested` USER audit commit atomically. Audit records fixed reason/template codes, IDs, prior failure count, acknowledgment and reviewed timestamp; no free-text reason/message/recipient/state hash. Existing identity/digest are preserved.
- Retry only re-arms work; it never calls the queue or provider directly. Once enabled, the normal worker may subsequently send subject to current state, consent, quiet hours and identity controls. A review reason is not consent and cannot enable delivery. Each cycle retains the five-failure bound and needs another fresh owner/admin review to reset again. Stale intents cannot be forced; existing queue/dead-letter events are not replayed. Review is a snapshot, with worker/pre-send checks remaining authoritative for later mutations. Live retry use and acceptance remain separately approval-gated.
- Intent tenant/job and tenant/communication-event references are composite-FK enforced. Migration `20260908120000_add_sms_enqueue_intents` must precede deployment through a separately approved release; only disposable-local migration proof exists at this checkpoint.

## GOV-008 High-Ticket Domain Contracts (High-Level)

### TenantBrandProfile

Required fields:

- `tenantId`
- `greeting`
- `tonePreset`
- `forbiddenPhrases` (string[])
- `serviceFeeLanguage`
- `escalationLanguage`
- `closeoutLanguage`
- `updatedAt`

### BusinessRuleSet

Required fields:

- `tenantId`
- `version`
- `rules` (typed object)
- `status` (`draft` | `active`)
- `updatedBy`
- `updatedAt`

### DispatchPolicy

Required fields:

- `tenantId`
- `dispatchMode` (`manual` | `recommended` | `auto`)
- `serviceAreaRules`
- `skillRoutingRules`
- `afterHoursRules`
- `fallbackEscalationRules`

### SchedulingWindow

Required fields:

- `tenantId`
- `timezone`
- `businessHours`
- `afterHoursPolicy`
- `bufferMinutes`

### Appointment

Required fields:

- `appointmentId`
- `tenantId`
- `jobId`
- `scheduledStart`
- `scheduledEnd`
- `assignedTechnicianId` (nullable)
- `status`
- `calendarSyncStatus`

### CustomerProfile

Required fields:

- `customerId`
- `tenantId`
- `name`
- `primaryPhone`
- `addresses` (array)
- `consentFlags`
- `lastInteractionAt`

### RevenueEvent

Required fields:

- `eventId`
- `tenantId`
- `eventType`
- `eventTimestamp`
- `sourceFlow` (`voice` | `sms` | `chat` | `manual`)
- `jobId` (nullable)
- `leadId` (nullable)

### NotificationPolicy

Required fields:

- `tenantId`
- `eventType`
- `recipientType` (`owner` | `dispatcher` | `technician` | `customer`)
- `channels` (array of `sms` | `email` | `push`)
- `templateId`
- `retryPolicy`
- `quietHoursPolicy` (nullable)
- `updatedAt`

### PaymentPolicy

Required fields:

- `tenantId`
- `serviceFeeRequired` (boolean)
- `serviceFeeCents` (nullable)
- `depositRequired` (boolean)
- `depositPolicy` (typed object)
- `emergencyFeePolicy` (typed object)
- `paymentGateMode` (`fail_closed` | `manual_override`)
- `webhookValidationRequired` (boolean)
- `updatedAt`

## GOV-017 Subscription Commercial Contracts (Locked)

### PricingPlan

Required fields:

- `planId` (`starter` | `growth` | `pro` | `enterprise`)
- `publicMonthlyPriceCents`
- `publicAnnualMonthlyPriceCents` (nullable for enterprise)
- `fairUseCallCapacity` (nullable for enterprise; nonfinancial plan-suitability guide)
- `maxLocations` (nullable)
- `maxActiveVehicles` (nullable)
- `maxTechnicianSeats` (nullable)
- `status` (`active` | `legacy` | `draft`)
- `effectiveFrom`
- `effectiveTo` (nullable)

### SubscriptionEntitlement

Required fields:

- `tenantId`
- `planId`
- `billingMode` (`subscription_only` | `fixed_enterprise`)
- `monthlySubscriptionPriceCents`
- `annualSubscriptionPriceCents` (nullable)
- `featureEntitlements` (versioned typed object)
- `capacityEntitlements` (versioned typed object)
- `status` (`trial` | `active` | `past_due` | `paused` | `cancelled`)
- `effectiveFrom`
- `effectiveTo` (nullable)

Rules:

- No entitlement may define setup, per-call overage, booked-job, emergency-capture, revenue-share, or basic per-invoice Signmons fees.
- Every active paid-plan entitlement includes the basic Stripe payment-before-booking gate after the Signmons Money release gate. The gate is fail-closed whenever the tenant's governed payment policy requires a booking fee or deposit.
- Growth and higher entitlements may add advanced deposit/preauthorization rules, exception approvals, partial-payment policy, and payment recovery controls; they do not own exclusive access to the basic gate.
- Capacity is nonfinancial and cannot alter an invoice automatically.
- A plan change requires explicit tenant acceptance and a new effective entitlement version.

### UsageMetricEvent

Required fields:

- `usageMetricEventId`
- `tenantId`
- `eventType` (`ai_call_handled` | `sms_sent` | `sms_received` | `booking_confirmed` | `emergency_escalated` | `active_technician_observed` | `location_observed`)
- `sourceEventId`
- `jobId` (nullable)
- `occurredAt`
- `quantity`
- `excludedFromCapacity` (boolean)
- `reasonCode`

Rules:

- Usage metrics support operations, plan-suitability warnings, forecasting, and product analytics only.
- A usage metric carries no billable amount and cannot create a Signmons invoice line item.
- Duplicate, spam, silent, blocked, failed-test, and approved-test events must be excluded with an auditable reason code.

### SubscriptionInvoiceRule

Required fields:

- `tenantId`
- `planId`
- `invoiceCadence` (`monthly` | `custom`)
- `fixedSubscriptionPriceCents`
- `roundingMode` (`none` | `nearest_cent`)
- `trialPolicy` (`none` | `time_limited`)
- `creditPolicy` (typed object)
- `prorationPolicy` (typed object)
- `disputeWindowDays`
- `effectiveFrom`

### Contractor Customer Billing Contracts (Reserved for APP-020)

These contracts govern a tenant contractor billing its homeowner/business customer. They are separate from `SubscriptionInvoiceRule`, which governs Signmons billing the tenant.

`ServiceEstimate` required fields:

- `tenantId`, `estimateId`, `estimateNumber`, `customerId`, `propertyAddressId`, `jobId`
- `status` (`draft` | `sent` | `approved` | `declined` | `expired` | `converted` | `voided`)
- versioned line items, subtotal, tax, discount, total, currency, terms, and expiration
- customer approval identity/method/timestamp when approved
- created/updated/sent timestamps and audit source

`JobInvoice` required fields:

- `tenantId`, `invoiceId`, tenant-unique `invoiceNumber`, `customerId`, `jobId`, optional `estimateId`
- `status` (`draft` | `sent` | `partially_paid` | `paid` | `overdue` | `voided`)
- immutable issued line-item snapshot, subtotal, tax, discount, total, balance, currency, due date
- processor references only; no raw card data
- created/updated/issued/sent/paid timestamps and audit source

`CustomerPaymentAllocation` required fields:

- `tenantId`, `allocationId`, `invoiceId`, provider payment reference, amount, currency, status
- idempotency key, allocation timestamp, refund/credit references, and audit source

`CustomerReceipt` required fields:

- `tenantId`, `receiptId`, `invoiceId`, payment allocation references, paid amount, currency, issued timestamp
- immutable customer-facing receipt snapshot and delivery status

Rules:

- Estimate and invoice numbering is unique and sequential within the configured tenant policy; it never shares a sequence with Signmons SaaS invoices.
- Estimate approval, invoice issue, payment allocation, refund, credit, and void transitions are auditable and tenant-scoped.
- General-ledger posting, payroll, tax filing, and bank reconciliation remain outside these contracts and flow through approved accounting adapters.

## Commercial Verification Rules

- Signmons invoices use the fixed active `SubscriptionEntitlement` price only, subject to versioned trial, credit, proration, and applicable-tax policy.
- `UsageMetricEvent` records never contain a billable amount and never create an invoice line item.
- Plan-capacity warnings use deduplicated usage under `USAGE_METRICS_SPEC.md`; exclusions carry a reason code.
- A fixed-price plan change requires explicit tenant acceptance and a new effective entitlement version.
- Contractor booking fees, deposits, estimates, job invoices, and Stripe processor costs remain in the contractor-to-customer billing domain.
- Pricing pages and ROI calculators must not add setup, usage, booked-job, emergency-capture, revenue-share, or basic per-invoice Signmons fees.
