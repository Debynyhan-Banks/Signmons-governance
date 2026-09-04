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

## APP-012 Payment Gate And Payment Request Contract

Current bounded endpoints:
- `GET /jobs/dispatch-board`
- `GET /jobs/dispatch-board/:jobId`
- `POST /jobs/:jobId/assignments`
- `POST /jobs/:jobId/payment-requests`
- `GET /jobs/:jobId/payment-request`

Policy source and state:
- The job's tenant-policy snapshot is authoritative for whether payment is required. Payment is required when `depositRequired` or `serviceFeeRequired` is explicitly `true`.
- The job's pricing snapshot is authoritative for checkout amount and currency. A required deposit uses positive integer `depositAmountCents`; a required service fee uses positive integer `serviceFeeAmountCents`; when both are required, the checkout amount is their sum. Currency is a three-letter code from `pricingSnapshot.currency`.
- Missing or invalid required pricing fails closed before provider access.
- Gate state is `NOT_REQUIRED`, `LOCKED` or `UNLOCKED`. Only canonical payment status `SUCCEEDED` unlocks a required job; not requested, pending, failed, canceled and refunded states fail closed.
- `manual_override` is reserved by `PaymentPolicy` but is not implemented by this checkpoint; operator assignment reasons cannot bypass a locked payment gate.

Payment request boundary:
- Only verified `owner`, `admin` and `dispatcher` roles may create or track a payment request. Tenant and actor identity come from verified request context, never the body.
- Creation requires the latest `expectedJobUpdatedAt` and a version-4 `Idempotency-Key`. The server stores only the SHA-256 request-key hash.
- Closed, deleted, missing, cross-tenant or stale jobs fail before provider access. A contractor payment account must have a connected-account identifier and `chargesEnabled=true`.
- Checkout is created as a direct charge on the contractor tenant's connected Stripe account. The Signmons application fee is fixed at zero.
- Exact idempotency replay may return the same short-lived checkout URL without duplicating the success audit. A different request key cannot replace a pending request; failed, canceled or refunded requests may be retried with optimistic concurrency.
- The operator tracking response contains only internal payment-request ID, canonical status, amount, currency, requested timestamp, expiry timestamp and active flag.

Privacy and audit:
- Dispatch and tracking projections prohibit Stripe account, payment-intent, checkout-session, charge, request-key and credential values.
- Successful request creation audits `payment.request_created`; provider failure audits `payment.request_failed` with a bounded reason code. Audit metadata contains internal job/payment IDs, request kind, amount, currency, status and expiry, never provider identifiers or checkout URLs.
- Payment reservation and final audit persistence are tenant-scoped. Webhook processing remains separately responsible for canonical payment-state transitions.

Dispatch enforcement:
- A locked, unassigned, non-escalated job stays in `NEW_REQUEST`, produces no eligible recommendation and cannot be newly assigned. An urgency escalation remains visibly `ESCALATED`, but it still cannot be assigned while locked.
- A locked assignment request returns conflict before candidate lookup, job mutation or audit creation.
- An existing assignment is not silently removed if a later payment state locks the gate; refund/cancellation follow-up is an explicit later APP-012 workflow.
- Successful canonical payment state restores normal routing eligibility and `READY_TO_ASSIGN` behavior.

Commercial boundary:
- The gate and checkout cover a tenant contractor's required customer deposit/service payment.
- They do not create a Signmons setup, usage, booked-job, emergency-capture, revenue-share, application or per-invoice fee; Signmons-to-tenant pricing remains subscription-only.

Remaining APP-012 contract work:
- Secure customer status/recovery endpoints and operator request UI.
- Signature-verified, idempotent Stripe webhook ingestion and visible processing outcomes.
- Payment/gate transition audits after verified webhooks and any separately governed manual override.

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
