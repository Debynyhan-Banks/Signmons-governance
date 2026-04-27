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

Calendar payload baseline:
- `tenantId` (required)
- `jobId` (required)
- `technicianId` (required)
- `startAt` (required, ISO-8601)
- `endAt` (required, ISO-8601)
- `timezone` (required)
- `serviceAreaId` (optional)
- `calendarProvider` (required: `google`)
- `calendarEventId` (optional until sync success)
- `syncStatus` (required: `pending` | `synced` | `failed`)

Conflict check payload baseline:
- `technicianId` (required)
- `startAt` (required)
- `endAt` (required)
- `bufferMinutes` (optional)
- `result` (required: `clear` | `conflict`)

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

Profile payload baseline:
- `tenantId` (required)
- `profileVersion` (required)
- `brandTone` (required)
- `greetingStyle` (required)
- `serviceFeeDisclosureTemplate` (required)
- `closingScript` (required)
- `forbiddenPhrases` (required, string[])
- `fallbackEscalationLanguage` (required)
- `updatedBy` (required)
- `updatedAt` (required, ISO-8601)

## Business Rules and Automation Contract (New)

Rules are stored in DB config and evaluated deterministically.

Rule entity baseline:
- `id` (required)
- `tenantId` (required)
- `ruleType` (required: `routing` | `urgency` | `payment` | `after_hours` | `messaging`)
- `priority` (required, integer)
- `conditions` (required, structured JSON)
- `actions` (required, structured JSON)
- `isActive` (required, boolean)
- `effectiveFrom` (optional)
- `effectiveTo` (optional)
- `updatedBy` (required)
- `updatedAt` (required, ISO-8601)

Rule evaluation trace baseline:
- `traceId` (required)
- `tenantId` (required)
- `inputContext` (required)
- `matchedRuleIds` (required, string[])
- `selectedAction` (required)
- `decisionReasonCodes` (required, string[])
- `evaluatedAt` (required, ISO-8601)

## Customer Profile and Service History Contract (New)

Customer profile baseline:
- `customerId` (required)
- `tenantId` (required)
- `fullName` (required)
- `phone` (required, E.164)
- `email` (optional)
- `primaryAddress` (required)
- `tags` (optional, string[])
- `createdAt` (required)
- `updatedAt` (required)

Service history baseline:
- `customerId` (required)
- `jobId` (required)
- `conversationId` (optional)
- `serviceCategory` (required)
- `urgency` (required)
- `status` (required)
- `paymentStatus` (required)
- `scheduledWindow` (optional)
- `completedAt` (optional)
- `summary` (optional)

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
