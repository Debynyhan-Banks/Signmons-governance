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
