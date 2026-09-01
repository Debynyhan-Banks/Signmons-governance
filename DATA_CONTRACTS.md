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
- Recommendation version is `dispatch-v1`.
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

## GOV-017 Commercial Contracts (Locked)

### PricingPlan

Required fields:
- `planId` (`starter` | `growth` | `pro` | `enterprise`)
- `publicMonthlyPriceCents`
- `publicAnnualMonthlyPriceCents` (nullable for enterprise)
- `setupFeeCents`
- `includedCallVolume`
- `overageBlockSizeCalls`
- `overageBlockPriceCents`
- `maxActiveVehicles` (nullable)
- `maxTechnicianSeats` (nullable)
- `status` (`active` | `legacy` | `draft`)
- `effectiveFrom`
- `effectiveTo` (nullable)

### PerformanceFeePolicy

Required fields:
- `tenantId`
- `planId`
- `qualifiedBookedJobFeeCents` (nullable)
- `emergencyCapturedJobFeeCents` (nullable)
- `revenueShareBps` (nullable)
- `billingMode` (`subscription_only` | `subscription_plus_performance` | `custom_enterprise`)
- `enabled` (boolean)
- `effectiveFrom`
- `effectiveTo` (nullable)

### BillableEvent

Required fields:
- `billableEventId`
- `tenantId`
- `eventType` (`qualified_booked_job` | `emergency_captured_job` | `overage_block_consumed`)
- `sourceEventId`
- `jobId` (nullable)
- `leadId` (nullable)
- `occurredAt`
- `billableAmountCents`
- `currency`
- `status` (`pending` | `finalized` | `voided`)
- `reasonCode`

### InvoiceRule

Required fields:
- `tenantId`
- `invoiceCadence` (`monthly` | `custom`)
- `roundingMode` (`none` | `nearest_cent`)
- `trialPolicy` (`none` | `time_limited`)
- `creditPolicy` (typed object)
- `lineItemRules` (typed object; includes setup, subscription, overage, performance fees)
- `providerFeeRules` (typed object; disclosed pass-through fees only)
- `disputeWindowDays`
- `effectiveFrom`

### Contractor Customer Billing Contracts (Reserved for APP-020)

These contracts govern a tenant contractor billing its homeowner/business customer. They are separate from `InvoiceRule`, which governs Signmons billing the tenant.

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

- A `qualified_booked_job` billable event may be emitted only when required booking fields are complete and job status has transitioned to booked/scheduled under tenant policy.
- An `emergency_captured_job` billable event may be emitted only when urgency is `emergency` and dispatch or escalated dispatch has been triggered according to tenant rules.
- An `overage_block_consumed` event may be emitted only from deduplicated qualifying-call counts under `BILLABLE_EVENTS_SPEC.md`; excluded calls must carry a reason code.
- `BillableEvent` must be immutable after `finalized`; reversals occur through explicit credit/void events.
- Pricing page and ROI calculator must never calculate invoice totals from hardcoded constants when contract-backed pricing data is available.
