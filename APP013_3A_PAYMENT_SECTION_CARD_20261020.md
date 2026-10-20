# APP-013 / 3A / P07 section card — same-job Sandbox payment wiring

## Status and authority

Entry inspection and the bounded local implementation are complete for the existing 3A section. APP-013 remains the sole `Now` ticket; owner-accepted 2B supplies admitted job `9180bef4-561d-47a0-869f-925e6a3dfd96` in `CREATED` state. P07 is review-ready, while P08 and 3A acceptance remain pending. Accepted progress stays 6/60 remaining-work packages, 4/8 walkthrough milestones and 0/13 fully accepted pilot rows. Local evidence: backend `evidence/APP-013/p07-local-implementation-20261020.md`.

This card authorizes no Stripe account access, Sandbox Checkout creation, webhook delivery, secret/configuration change, charge, deployment, migration, booking or customer contact. Exact Sandbox account/mode/actions still require a separately reviewed proposal and owner approval. The existing 3A acceptance criteria, order and denominator are unchanged. **No scope deviation.**

## Source and evidence anchor

- Focused backend branch: `codex/p06-r08-recovery-20260918`, HEAD `3cf8a9dc53d0282a35e6263a36d749c5b32f8e2e`; existing mixed worktree changes remain uncommitted and preserved.
- Focused governance branch: `codex/p06-r08-recovery-20260918`, HEAD `8d7c644ecc8e65ec139bcfcc3fef055ad5d423cd`; existing mixed worktree changes remain uncommitted and preserved.
- Accepted entry evidence: backend `evidence/APP-013/p06-r11-enabled52-live-result-20261019.md` and enabled52 `owner-acceptance.json`.
- Inspection evidence: backend `evidence/APP-013/p07-3a-entry-inspection-20261020.md`.
- Inspected clean payment source hashes: `payment-requests.service.ts` `895a739b...f864e`; `stripe-checkout.provider.ts` `579f7143...c021`; `stripe-webhooks.service.ts` `acc32f4f...fcbe`; `job-payment-policy.service.ts` `4485a6c9...2b71`; dispatch page `58d02c32...0863`; UI API `f9b71d74...6416`.
- The inspected controlled-intake source has pre-existing uncommitted changes and content hash `88b2dfb5...5606`; this card does not modify or commit them.

## Exact acceptance criterion

The same accepted job opens one authorized Stripe Sandbox Checkout from its current approved payment policy. Only an authentic signed event from the exact Sandbox mode, connected account and exact Checkout/payment resource, with matching payment request, job, amount and currency, may move the payment to `SUCCEEDED` and clear the persisted payment gate. Redirect state alone, missing policy, unpaid/failed/forged/foreign events, duplicates, late events and lost responses must not create a second logical request or regress settled state.

## Existing components to reuse

| Boundary | Existing component | Qualified behavior |
| --- | --- | --- |
| Approved terms | `organization-payment-policy.*`, `job-payment-policy.service.ts` | Approved tenant terms, digest and immutable job snapshot writer already exist. |
| Request | `payment-requests.service.ts`, controller/access guard | Tenant/job/role checks, trusted amount/currency snapshots, hashed request key, reservation, provider failure state and privacy-safe tracking. |
| Checkout | `stripe-checkout.provider.ts` | Direct connected-account Checkout Session, no Signmons fee, idempotency header, dynamic payment methods by omission, bounded timeout and sanitized provider failure. |
| Event truth | `stripe-webhooks.service.ts` | Raw-body HMAC verification, five-minute tolerance, configured mode check, connected-account tenant lookup, amount/currency check, duplicate event suppression and monotonic refund protection. |
| Operator/customer surfaces | dispatch payment controls, payment return page and `continue_payment` recovery | Operator creates/views a request; redirect copy is pending-only; customer recovery reopens an existing active Checkout after a management link exists. |
| Downstream gate | shared payment-gate reducer plus dispatch/scheduling guards | Persisted verified payment, not the browser redirect, controls assignment and booking eligibility. |

No replacement payment stack, new fee model or SDK/API upgrade belongs in P07.

## Demonstrated gaps

1. **The accepted controlled job has no payable snapshot.** Controlled admission records `paymentApprovedAt` and `paymentDigest`, but writes an empty `pricingSnapshot` and no `depositRequired`/`serviceFeeRequired` fields. `PaymentRequestsService.create` therefore refuses before Checkout. The existing policy binder requires `intakeAdmission.humanReviewed === true`; enabled52 is correctly deterministic/non-human-reviewed. Its controller is explicitly local-only and unregistered. P07 must bind the current approved policy to this exact controlled job without relabeling it human-reviewed and without bypassing its saved payment digest.
2. **Operator lost-response recovery is incomplete before booking.** The dispatch client generates a new UUID on every request. After a successful server response is lost or the page reloads, tracking reports an active request, disables creation and does not expose the active Checkout URL. Existing customer recovery requires an appointment-management link, which this pre-booking job does not yet have. P07 needs an authorized exact-active-request recovery/replay path that neither creates a new logical request nor exposes provider identifiers.
3. **Signed foreign events can reach metadata fallback.** Webhook lookup currently ORs `paymentRequestId` metadata with Checkout Session, PaymentIntent and Charge identifiers. A signed same-account event with guessed/copied metadata and matching money can select the payment without proving that the event's exact resource is the stored resource. P07/P08 must require the resource appropriate to each event type and validate the stored request/job binding; metadata may corroborate but must not substitute for exact resource identity.
4. **Sandbox configuration is partially qualified.** On October 20, after the user stated that Chrome was signed into the Stripe account intended for 3A, a read-only browser check confirmed the visible context is the **Signmons LLC sandbox**, Stripe Test/Sandbox mode, and a Connect platform with exactly one test connected account showing **Enabled**. The human sign-in identity is not Debynyhan Banks; the user states they hold all listed access, so the controlling authorization level is recorded as owner/admin. Exact tenant/destination binding, webhook destination/secret/runtime binding, API version and effective test payment methods remain unverified. No configuration defect is inferred. Evidence: backend `evidence/APP-013/p07-stripe-sandbox-readiness-20261020.md`.

The existing implementation already satisfies the Stripe review principles relevant here: Checkout Sessions for the one-time payment, no hard-coded `payment_method_types`, no fulfillment from the redirect, required signed webhooks, mode/account checks, server-held secrets and sanitized errors. The provider uses the existing direct HTTP adapter rather than an SDK; the frozen contract excludes an SDK/API upgrade in this section.

## Bounded P07 implementation contract

1. Extend the existing job-policy binding boundary for controlled admission version 2 only when tenant/job/undeleted/`CREATED` state, absence of payment/calendar activity, exact job version, current approved tenant policy, saved `paymentApprovedAt` and saved `paymentDigest` all match. Preserve the deterministic actor and never write `humanReviewed: true`. Bind only the already approved deposit/service-fee flags, fail-closed mode, webhook-required flag, USD pricing and a versioned audit receipt. Missing/foreign/stale/malformed state refuses before payment/provider access.
2. Expose that binding through an existing owner/admin authenticated application boundary or compose it into the operator P07 flow. Do not register a generic local helper or accept policy/amount/account fields from the browser. The response grants no Checkout, booking, dispatch or messaging authority.
3. Make operator Checkout creation retryable with one stable client operation identity and add explicit authorized recovery of the exact active request. Recovery must revalidate tenant, job, role, stored destination account, tenant account, charges-enabled state, pending status and expiry; it returns only the validated `checkout.stripe.com` URL and expiry and writes a bounded audit. It must not create another Checkout Session.
4. Tighten webhook correlation by event type: Checkout events require the stored Checkout Session ID; PaymentIntent failure requires the stored PaymentIntent ID; refund events require the stored Charge ID once known. Require the same tenant/destination account and matching stored job/payment metadata where present. Unknown or mismatched resources refuse with no payment/audit mutation. Preserve duplicate acknowledgement and terminal-state monotonicity.
5. Keep the return page informational and pending. Refresh operator/payment-gate state only from persisted signed-event processing. No redirect query parameter may mark payment succeeded.

Expected implementation files are limited to the existing policy binding/service registration, payment request/controller/provider, webhook service, dispatch API/page, their focused tests and this section's evidence. A schema change, new payment subsystem, new fee/routing behavior or provider configuration is a change request, not routine P07 work.

## Data, state, identity and retention boundaries

- Identity: owner/admin may bind policy; owner/admin/dispatcher may create/recover a payment request under existing guards; customer recovery remains scoped by the existing private management capability. Browser fields never select tenant, connected account, amount, currency, payment status or webhook truth.
- State: controlled `CREATED` job -> reviewed immutable payment snapshot -> one logical `PENDING` payment -> exact signed event -> `SUCCEEDED`/failure state. No job status, appointment, dispatch, message or refund action belongs here.
- Money: amount/currency derive only from the job snapshot; application fee remains zero. Real mode and real charges are excluded.
- Provider data: store only existing Checkout/PaymentIntent/Charge/Event identifiers, bounded event type/timestamps/status and sanitized audit metadata. Do not store keys, raw event bodies, Checkout URLs, card data or provider diagnostics in evidence/logs.
- Secrets: existing secret and webhook-signing values remain server-side and unchanged. Exact Sandbox qualification may confirm presence/binding only through a separately authorized secret-safe process.

## Finite verification matrix

- Policy binding: controlled-v2 positive; stale/foreign digest or approval timestamp; wrong actor/version; human-reviewed legacy compatibility; cross-tenant/deleted/non-CREATED/payment/calendar activity; concurrent binding; audit rollback; exact replay.
- Request/recovery: missing policy/pricing/account/charges; wrong role/tenant/job; exact request success; same-key lost response; active-request recovery; expired/replaced request; concurrent keys; sanitized provider failure; no provider call on refusal.
- Webhooks: valid exact paid session; unpaid completed; async success/failure; wrong signature/time/mode/account/session/payment-intent/charge/job/request/amount/currency; duplicate; success after failure; late failure/expiry after success; refund then late success.
- UI/browser: desktop and 390x844 operator flow shows policy-bound request, stable retry, active-link recovery, pending redirect, signed-event success and truthful error states with no application-origin console error or horizontal overflow. No live Checkout is required for local browser fixtures.
- Full gates after code: focused tests, full Jest, backend lint/build/architecture/Prisma; affected UI test/lint/build; disposable database proof if persistence behavior changes; governance baseline/consistency/21 safeguards and both diff checks.

## Dependencies, owners, rollback and stop

- Implementer: bounded local P07 code/tests/evidence and a concrete Sandbox execution proposal after local review readiness.
- Debynyhan Banks: exact Sandbox action approval and later 3A acceptance. The intended platform sandbox and one enabled connected account are observed, and the signed-in user is recorded as owner/admin; exact tenant/destination binding and webhook/runtime readiness remain open. No open-ended provider authority.
- Rollback/disabled state: no deploy means current runtime is unchanged. Code rollback removes the policy-binding/recovery/correlation patch. If any external run later starts, its packet must define exact stop/reconciliation and must not infer booking or 3B authority.
- Stop on any inability to correlate the accepted job, approved policy, connected Sandbox account, exact Checkout resource or signed event. Do not substitute a new job, manual database edit, redirect screenshot, broad Stripe search or real-mode transaction.

## Observable finish

P07 becomes review-ready only when local implementation and the full applicable matrix pass, with a concrete secret-safe Sandbox proposal. It is accepted only through the existing package ledger after owner review; preparation and tests do not change 6/60 or 4/8. P08 then owns the separately authorized authentic Sandbox event, duplicate/late-event demonstration and owner acceptance of 3A.

## October 20 — additional approved atomicity repair and actual-role proof

The owner approved APP013_P07_WEBHOOK_ATOMICITY_REPAIR_PROPOSAL_20261020.md after an actual restricted-role proof demonstrated stale concurrent FAILED overwriting SUCCEEDED. The existing webhook service now serializes the exact Payment row and revalidates current state before deciding a transition. Both distinct-event orderings and terminal refund state pass through real Prisma/PostgreSQL, as do 22 reported local proof checks, unchanged 49+13 negative rights, normal/SIGINT cleanup, local build/lint and 97 affected Jest cases. Existing five-minute reservation behavior is unchanged and explicitly tested. Evidence: backend evidence/APP-013/p07-webhook-atomicity-local-repair-20261020.md. No new schema, grants, endpoint, UI or provider behavior is introduced. No scope deviation from that explicitly approved repair.

The old unused image lacks this patch. The fresh source review archive is prepared; see backend evidence/APP-013/p07-atomic-repaired-source-preparation-20261020.md. Fresh image build and live runtime/destination/secret readiness remain separate exact approval gates; P08 and 3A acceptance remain pending. The selected availability is not launch authority. Accepted measures remain 0/27 newly closed R1, 6/60 legacy, 4/8 walkthrough, 0/13 full-intelligence rows; no denominator or criterion changes.


## Historical October 20 — local build preparation review before the later approved build

At this local checkpoint the repaired-source review packet remained disabled. Owner explicitly approved the finite six-guard correction in `APP013_P07_REPAIRED_BUILD_PREPARATION_PROPOSAL_20261020.md` before implementation; the corrected private controller and 45 local methods now pass, with original artifacts preserved. All eight finite local card tasks are complete. No app fix is reset; build-only external authority/window and later repaired-digest/runtime/credential/destination approval stay separate. Preparation evidence: backend evidence/APP-013/p07-repaired-build-preparation-review-20261020.md. Counts and acceptance criteria remain unchanged.


## October 20 — exact repaired image build completed

The separately approved one-build operation completed once: build `9ee7772a-62b1-4a07-86ad-0c3b9daf3032` SUCCESS; exact uploaded archive matched; repaired image digest `sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da` agrees across build/registry. All three temporary permissions were removed/read back absent; separate live source/build/registry/IAM readback passed eight checks with failures[]. Image remains unused; operation is consumed. Backend evidence: evidence/APP-013/p07-repaired-image-build-result-20261020.md. No deployment/runtime/Stripe/payment authority follows. Next is the concrete repaired-digest readiness proposal with explicit credential-isolation/secret/destination/cost/containment decisions. P08/3A and all accepted measures stay unchanged; no scope deviation from the exact approved build.

## October 20 — repaired-digest runtime architecture proposal prepared

`APP013_P07_REPAIRED_DIGEST_RUNTIME_READINESS_PROPOSAL_20261020.md` now binds the repaired digest and exact accepted-job/readiness boundaries. It recommends a dedicated `p07_payment_runtime` role, separate P07 database and webhook secrets and a dedicated zero-traffic service identity; reusing or expanding the accepted P06 credential boundary is rejected. The proposal includes exact resource names, six-event disabled Sandbox destination, numeric pins, conservative two-version cost, mandatory containment and a 24-hour retirement boundary.

Owner replied “Approve Alternative 1,” approving the dedicated role/secrets/identity architecture for local package preparation before implementation. A fresh attended window, tested no-action package and separate external-action approval remain required. No live role, secret, identity, IAM binding, destination, revision, database/customer row or payment changed. P08/3A and all accepted measures remain unchanged.

## October 20 — startup-credential correction proposed before package implementation

Source inspection during exact package preparation demonstrated that production startup also requires `OPENAI_API_KEY`, `ADMIN_API_TOKEN`, `CONVERSATION_DATA_ENCRYPTION_KEY` and `TECHNICIAN_LINK_SECRET`. Those credentials are outside the approved three-secret identity design, so the supplied 6:45–8:15 p.m. Eastern block was not bound or attempted. Owner replied “yes i approve” to `APP013_P07_STARTUP_CREDENTIAL_CORRECTION_PROPOSAL_20261020.md`, authorizing local package preparation/testing around four independent candidate-only secret versions, exact environment/secret replacement and removal/disable readback within the existing 24-hour retirement boundary. No code, role, secret, IAM, Stripe, deployment or payment action occurred. Accepted measures remain unchanged. **Approved scope deviation before implementation; no external implementation.**

Fresh private package `/private/tmp/p07-repaired-runtime-readiness-20261020-prep1` now passes 27 focused tests and no-action/refusal checks. It binds plan `139a3a66-ae17-420d-b18e-7075541e457b`, exact repaired digest, six new candidate-only secret resources, seven resource bindings, replacement environment maps, mutation-ahead journaling and cleanup-only recovery. It has no window or live approval and cannot execute. Evidence: backend `evidence/APP-013/p07-repaired-runtime-readiness-preparation-20261020.md`; manifest `da1d18696aaf40127239a63f1b22ac4a89a6c7677ac81f90b7f6a0004055a0a7`. Owner supplies a new attended 90-minute block next; exact binding/retest and separate live approval remain required.
