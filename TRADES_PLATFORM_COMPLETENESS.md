# Trades Platform Completeness Standard

## Core commercial release amendment — October 20, 2026

This is the broader platform roadmap. MVP_CORE_RELEASE_SCOPE_CHANGE_20261020.md defines the smaller first commercial release. Operational safety, ownership, support and tested recovery remain R1 obligations; full diagnostics, memberships, costing, inventory, time export, offline, financing, broad migration/integration and APP-034 are not R1 prerequisites. Preserve these later requirements without placing their systems in the core booking/payment path.

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

### APP-034 Acquisition-to-Profit Attribution — Later only

**Status:** Future governed scope; not approved for implementation. APP-034 must not displace APP-013 or the owner-approved Next sequence. It cannot be promoted until its dependencies have completed their own acceptance and the canonical pointer/board explicitly advances it.

**Purpose:** Extend Signmons Growth from lead-source reporting into auditable operating and financial outcomes: `Lead -> qualified opportunity -> booking -> completed job -> collected revenue -> job profitability -> retention`. This protects Revenue Integrity Dispatch by showing which sources produce completed, paid, profitable, retained trade work; it is not a generic marketing suite.

**Dependencies:** BE-007's existing tenant-scoped pilot; APP-019 customer identity and service history; APP-020 estimates, invoices, payments/receipts; APP-026 governed job costs and profitability; and relevant communication/channel foundations. No dependency may be skipped or mocked as accepted. Current BE-007 primarily recognizes `website_chat`; it counts created/booked/completed/cancelled jobs and attributed/unattributed outcomes, computes lead-to-booking and booked-to-completed ratios, and groups by UTM source/medium/campaign and landing page. It does not report collected revenue, job profit, full channel coverage, customer retention, or broad campaign performance.

**Future acceptance boundary:**

- Every report and attribution correction is tenant-scoped; cross-tenant access is denied, and correction actor, time, reason, before/after value, and source remain auditable.
- A governed source model may include `website_chat`, `web_form`, `phone`, `sms`, `google_business_profile`, `referral`, `property_manager`, `repeat_customer`, `manual`, and `unattributed`. Channels are added only when technically and legally supportable; an unknown source remains unattributed and is never inferred or fabricated.
- Preserve available `landingPage`, `sourcePage`, `referrerHost`, `utmSource`, `utmMedium`, `utmCampaign`, `utmContent`, `utmTerm`, and approved click identifiers such as `gclid`, `gbraid`, or `wbraid`. Initial acceptance does not require ad-platform integration. First-touch and latest meaningful attribution may be adopted only with explicit, versioned policy and audit semantics.
- Demonstrate lifecycle lineage across lead/conversation, customer, booking, job, estimate, invoice, and payment using stable, tenant-owned identifiers and idempotent updates; preserve corrections and source provenance.
- Report quoted estimate value, invoiced value, and collected revenue separately. Failed, partial, refunded, and reversed payments remain distinguishable; estimates are never labeled revenue. Collected revenue requires accepted APP-020 and relevant APP-012 payment records.
- Report gross profit only after APP-026 provides governed actual-cost inputs and calculation semantics. Missing/incomplete costs are visibly unavailable, never treated as zero. Future calculations may include cost per lead, booking conversion, customer acquisition cost, revenue and collected revenue by source, gross profit by source, ROAS when approved spend data exists, marketing contribution, and repeat-customer rate, each with explicit denominator, time basis, and missing-data handling.
- Approved spend is manually entered or imported through an explicitly approved adapter. No autonomous purchasing, campaign management, or budget changes; no ad-platform spend control absent explicit owner approval.
- Analytics expose only the minimum customer information needed. No sensitive customer data appears in campaign/source summaries; retention and deletion follow governed source-record policies.
- The future tenant screen `SCR-APP-034` is an outcome report for sources, leads, bookings, completed jobs, collected revenue, available gross profit, conversion rates, and unattributed volume. It does not become a campaign-management console, website builder, social tool, SEO agency surface, or broad marketing-automation interface.

**Validation when later authorized:** tenant isolation and role tests; source normalization and unknown-source negatives; correction audit tests; lifecycle lineage, duplicate/replay, partial/refund/reversal, missing-cost and date-boundary tests; privacy output checks; adapter failure/reconciliation tests where adapters are approved; and browser review of loading, empty, error, unavailable-profit, and populated states. Acceptance requires correlated source-to-payment/cost evidence and owner review. This future validation plan grants no present implementation, deployment, billing, provider, or data-use authority.

### Capacity-aware Signmons Intelligence — future recommendation boundary

Future intelligence may use verified Signmons operating data to recommend that an owner or authorized manager review demand against available service capacity, excessive backlog, paid-lead volume, or whether additional technician/truck capacity may be justified. Possible measures include revenue per technician/field hour, average ticket, gross profit per technician (only after APP-026), schedule utilization, callback rate, booking and maintenance conversion, backlog, and repeat-customer rate. Recommendations remain advisory: Signmons does not autonomously hire, purchase, or change advertising budgets. This is a product boundary note, not an implementation ticket or authorization.

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
