# Trades Platform Completeness Standard

Purpose: define the operational capabilities required for Signmons to become a comprehensive, hard-to-replace platform for trades businesses without drifting into an ERP, payroll processor, lender, or autonomous diagnostic system.

## Product Promise

Every qualified opportunity should move from first contact to scheduled, paid, dispatched, documented, invoiced, and retained with no silent failure and a tenant-scoped audit trail.

This promise extends the Revenue Integrity Dispatch differentiator. Feature count alone is not completeness; the entire workflow must be explainable, recoverable, usable in the field, and measurable.

## Required Operating Capabilities

### APP-025 Memberships And Recurring Service Agreements

- Plan definitions, covered equipment, entitlements, member pricing, renewal state, recurring billing reference, and cancellation policy.
- Recurring inspections and maintenance visits must create governed scheduling demand without duplicate jobs.
- Renewal, payment, scheduling, and service failures must remain visible and recoverable.

### APP-026 Job Costing And Profitability

- Estimated and actual labor, materials, equipment, subcontractor, commission, and overhead attribution.
- Margin reporting by job, technician, service, customer, and date range with explicit cost-source timestamps.
- Corrections require authorization and audit history; reports must not silently rewrite historical costs.

### APP-027 Inventory, Purchasing, And Truck Stock

- Warehouse and vehicle locations, on-hand/allocated/used/returned quantities, reorder thresholds, transfers, purchase orders, and receiving.
- Parts usage links to the job, estimate, invoice, technician, and cost basis.
- Supplier integrations require approved adapters and cannot place unreviewed purchases by default.

### APP-028 Employee Time And Payroll Export

- Clock-in/out, job time, non-job time, breaks, adjustments, timesheet approval, and technician performance attribution.
- Export to approved payroll systems must be repeatable and reconciliation-safe.
- Signmons records and exports time; it does not calculate statutory payroll, deductions, withholding, or taxes in MVP.

### APP-029 Offline-First Field Synchronization

- Technicians can access assigned work and capture forms, notes, photos, signatures, estimates, and diagnostic readings during recoverable connectivity loss.
- Local data is encrypted where retained, scoped to the authenticated tenant/user, and removed according to device/session policy.
- Replay is idempotent; conflicts are visible and resolvable; retries cannot create duplicate jobs, reports, invoices, or messages.

### APP-030 Customer Financing

- Approved financing choices can be presented beside an estimate with clear provider attribution and customer consent.
- Signmons may retain a minimal provider reference, amount, expiration, and application status needed to govern the estimate workflow.
- Signmons does not underwrite, make lending decisions, store sensitive application data, or claim approval before provider confirmation.

### APP-031 Onboarding, Migration, And Data Ownership

- Guided trade-specific setup covers business hours, service areas, technicians, phone/SMS, pricebook, payment policy, taxes, templates, roles, and test workflows.
- Imports provide mapping preview, validation, duplicate detection, dry run, failure report, reconciliation totals, and a safe pre-finalization rollback.
- Tenants can export governed business records and attachments; retention and account closure have explicit timelines and ownership.

### APP-032 Reliability And Operational Recovery

- Provider outage handling, bounded retries, dead-letter review, manual replay, health visibility, alert ownership, incident response, and customer-safe degraded modes.
- Backup policy covers databases, objects, configurations, and required audit evidence.
- Restore procedures are exercised on a schedule with recovery-time and recovery-point evidence; a successful backup job alone is insufficient.

### APP-033 OpenAI Voice Intake And Booking Orchestration

- Twilio-delivered inbound calls enter a tenant-configured OpenAI conversational workflow with controlled tools and server-owned policy decisions.
- The workflow identifies and qualifies the request, screens safety/urgency, confirms critical facts, and hands off to canonical SMS, scheduling, payment, dispatch, or a human.
- Model/provider failure, silence, interruption, dropped calls, unsupported requests, emergencies, and transfer failures preserve recoverable state and visible ownership.

## Additional Trade-Critical Requirements

The following requirements must be decomposed into governed tickets before the affected capability is marketed as complete:

- **Identity and administrative security:** MFA, optional SSO for eligible plans, session/device controls, granular roles, approval limits, access review, and tamper-evident security audit history.
- **Sales and change control:** good/better/best estimate options, add-ons, change orders, scope revisions, customer approval/signature, expiration, financing handoff, and immutable accepted-version evidence.
- **Equipment, warranty, and compliance records:** equipment lifecycle, serial/model data, warranty dates and claims references, permit/inspection artifacts, maintenance history, and jurisdiction/tenant-configured disclaimers without claiming legal or code authority.
- **Commercial service:** organizations with multiple contacts and locations, purchase-order/authorization requirements, recurring inspections, multi-stage work orders, consolidated billing references, and role-based customer access.
- **Governed tenant knowledge:** approved service facts, hours, service areas, policies, FAQs, exclusions, credentials, and effective dates used by voice/chat/SMS; unsupported or stale knowledge fails to a human.
- **Implementation and support readiness:** guided launch validation, number forwarding/porting checks, sandbox calls/messages/payments, help content, support ownership, release notes, customer-visible status, and a recoverable escalation path.

## Cross-Cutting Acceptance Standard

Each capability must demonstrate:

- strict tenant isolation and least-privilege role enforcement;
- idempotent state transitions and visible failure ownership;
- mobile and keyboard accessibility for its supported surfaces;
- privacy-safe logs, exports, notifications, and customer views;
- auditability of actor, source, timestamps, revisions, approvals, and corrections;
- provider abstraction and recovery behavior for external dependencies;
- objective acceptance evidence, monitoring, rollback, and owner sign-off;
- marketing and plan claims that do not exceed released behavior.

## Sequencing

1. Complete and release APP-012 payment integrity.
2. Complete APP-013 communications, consent, delivery, and failure handling.
3. Continue the governed APP-014 through APP-024 workflow in the order approved by the global pointer.
4. Promote APP-025 through APP-032 individually only after contracts, screens, acceptance criteria, dependencies, and evidence plans are written.
5. Promote APP-033 only after BE-008 has an accepted communications boundary and the voice safety, latency, knowledge, recording/transcript, and human-fallback contracts are approved.

No item in this document is `Now` merely because it is documented. The global execution pointer and WIP limit remain authoritative.
