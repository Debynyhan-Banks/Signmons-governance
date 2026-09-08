# Data Contracts

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

## APP-013 UI Framework Compatibility Checkpoint

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
