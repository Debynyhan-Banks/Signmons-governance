# APP-013 / 3A / P07 — payment-runtime access prerequisite

Status: **change proposal; not implemented or approved**. The owner approved only the separate local split-read correction. The selected October 20, 4:00–5:15 p.m. Eastern block is availability, not execution authority. No replacement readiness launch is ready. The expired repair3 package and all three consumed operations remain immutable.

## Demonstrated gap and workflow impact

Backend inspected source: `c426c319c240879dfb7c7ebf2f5aabfa5161c9d7`; governance source: `0a27a0fe5ef23f89a8b2718417e3997d295c0c9e`. Application/image source remains `cec82163bd67fe939d88aacb6fedf2d9c126b90e`, image `sha256:a88e64566133b9e734d245a928d0ade10b5064ff76d8e4fc712a4e3def3f0191`.

The old readiness proposal binds the candidate's only Prisma pool to `signmons-staging-p06-child-database-url:2`, whose reviewed role is `p06_intake_runtime`. That role is intentionally intake-only. The reviewed grant fixture and its negative tests exclude Payment/CalendarOperation reads and Job policy/pricing updates, and provide no StripeEvent rights. Current payment services require those operations. A successful health/readiness response would not prove that policy binding, Checkout persistence or signed settlement can work.

Inspected evidence:

- `scripts/fixtures/p06-runtime-role-review.sql` and `scripts/verify-p06-runtime-role.mjs`: original limited grants, zero memberships and intentional permission denials. Do not modify them to make P07 pass.
- `src/jobs/job-payment-policy.service.ts:79`: includes Payment and counts CalendarOperation; at line 184 updates Job policySnapshot/pricingSnapshot/updatedAt and inserts AuditLog.
- `src/payments/payment-requests.service.ts:531`: reserves Payment before provider creation; at line 624 persists returned Checkout references. Missing post-provider rights could leave an externally created Checkout without its local binding.
- `src/payments/stripe-webhooks.service.ts:84`: inserts StripeEvent, updates Payment and audit, then records event processing.
- `src/prisma/prisma.service.ts:53`: one configured DATABASE_URL; no separate payment pool.
- Existing dispatch page loads board/detail/payment/events together; detail also evaluates routing and candidates. These existing read dependencies must be proved, not bypassed with another temporary screen.

These are source/approved-boundary findings. **No fresh live ACLs or secret payloads were read.** The approved split-read diagnostic correction is locally tested, but cannot resolve this application-runtime mismatch.

## Alternatives and recommendation

| Option | Effect | Recommendation |
| --- | --- | --- |
| Dedicated payment runtime role in the same isolated child database | Preserves P06 intake restrictions; adds only proved payment and existing operator-display access | Recommended, subject to local real-role proof and later exact external approval |
| Expand p06_intake_runtime | Changes the accepted intake boundary and invalidates its intentional negative rights | Do not choose as a routine repair |
| Use administrator/migration/backup credentials in the app | Avoids permission errors through excessive authority | Reject |
| Deploy the current intake-role candidate and rely on health checks | Leaves demonstrated payment operations unsupported under the reviewed grants | Does not resolve readiness |

Proposed logical role: `p07_payment_runtime`, with no superuser, CREATEDB, CREATEROLE, replication, BYPASSRLS, ownership or inherited memberships. Its future live credential would stay hidden and bind only the isolated candidate during a separately approved bounded window. Preserve `p06_intake_runtime`, its password, numeric secret version 2, fixture and negative tests.

After proof, a future operation could store the new URL as **one new numeric version of the existing child-URL secret**, preserving version 2 and existing runtime IAM. This is a proposed secret-version approach, not authority to access/create/change it. A separate webhook-secret version would still be needed. Any future operation must reassess secret-version count/cost, exact URL/role target, login/expiry/session controls, rollback and retained cost; the old one-secret USD0.06/month allowance does not automatically cover two new active versions. No new cost allowance is approved here. A new version of the same secret does not isolate the stronger credential from existing resource-level accessors or the shared runtime service identity. Numeric revision pins preserve configuration, not credential isolation. Stronger isolation would require a separate secret/runtime-identity IAM decision in the future external proposal; this tradeoff must be reviewed explicitly before any live provisioning.

## Proposed access map to prove locally

This is a source-derived candidate boundary, **not executable GRANT SQL or a proven minimum**. Prisma methods without `select` return scalar rows; defaults, `@updatedAt`, relation SQL and RETURNING behavior must be exercised through an actual restricted login. Grant no blanket ALL, sequence/function, schema CREATE or unrelated-table access to compensate for a failed test.

| Table | Candidate read surface | Candidate writes |
| --- | --- | --- |
| TenantOrganization | id/status/settings/connected-account/charges/timezone and needed relation columns | updatedAt privilege only for the existing FOR SHARE lock; no settings/account/status change |
| Job | Current full scalar selection plus tenant/job predicates and relation keys | policySnapshot, pricingSnapshot, updatedAt only; no INSERT/DELETE, lifecycle, assignment or calendar change |
| CalendarOperation | id/tenantId/jobId/finishedAt for counts and unfinished-operation checks; verify generated aggregate SQL | None |
| Payment | Current full scalar reads/RETURNING, request and resource matching | INSERT request row; narrowly enumerated UPDATE union below; no delete/reassignment/transfer write |
| StripeEvent | Current full scalar RETURNING plus tracking/filter fields | INSERT event; UPDATE processingStatus/processedAt/errorMessage only |
| AuditLog | Current scalar RETURNING and existing bounded dispatch history | INSERT only; no UPDATE/DELETE |
| ServiceCategory, User, RoutingRule, ServiceArea | Existing full scalar selections in dispatch/routing | None |
| UserServiceCapability | Relation keys/isEnabled/proficiency and category filters, validated against generated SQL | None |
| UserAvailabilityBlock | Relation keys/type/startAt/endAt, validated against generated SQL | None |
| PropertyAddress | Relation keys/addressComponents/formattedAddress | None |

Payment INSERT currently supplies id, tenantId, jobId, jobTenantId, status, requestKeyHash, requestedAt, destinationAccountId, amountTotalCents, applicationFeeAmountCents and currency, plus generated/default fields that real SQL must verify.

The existing Payment UPDATE union is status, requestKeyHash, requestedAt, checkoutExpiresAt, stripeCheckoutSessionId, stripePaymentIntentId, stripeChargeId, destinationAccountId, amountTotalCents, applicationFeeAmountCents, currency, refundStatus, refundAmountCents, stripeRefundId, refundReason and Prisma-managed updatedAt. This covers existing request reset/recovery and signed refund-event observation; it authorizes **no provider refund transaction**. Do not grant identity/tenant/job reassignment or createdAt/transfer changes.

StripeEvent INSERT includes the generated ID, tenantId, stripeEventId, type, bounded payload, processingStatus and receivedAt. Audit INSERT must support existing actor-user composite identity/defaults; fixtures must contain the matching actor, tenant and job. Foreign keys do not justify runtime user/tenant creation, REFERENCES/DDL or constraint changes.

Table/column grants do not provide single-job or tenant row isolation. Application predicates, role guards, immutable policy, signature/account/resource checks and credential custody remain essential. A writable policySnapshot JSON column cannot distinguish binding from every other JSON operation at the SQL privilege level; do not claim database ACLs enforce an endpoint-only action list. No RLS or cryptographic webhook guarantee is inferred from database permissions.

## Proposed finite local implementation card — owner decision required first

Approved section, if the owner accepts this prerequisite: existing APP-013/3A/P07 within R1-W01. Acceptance criteria and the fixed walkthrough stay unchanged: the same accepted job must eventually settle through authentic matching Sandbox evidence, with replay/refusal and closeout. This local card would prove a viable runtime boundary before any new external operation is proposed.

Expected files are limited to:

1. `scripts/fixtures/p07-payment-runtime-role-review.sql`: review-only local role grants with explicit exclusions.
2. `scripts/verify-p07-payment-runtime-role.mjs`: actual restricted-login disposable proof using current migrations, real Prisma/services, synthetic actors/jobs, mocked provider transport and the existing Unix-socket disposable harness pattern.
3. `evidence/APP-013/p07-payment-runtime-role-local-proof-20261020.md`: source/grant hashes, positive/negative/concurrency/recovery/cleanup results and exact remaining live gates.
4. This proposal/section card and normal governance status/evidence references. No application, UI, Prisma schema or production migration change is included.

Reuse the isolation checks, direct current_user/session_user checks and cleanup patterns in `scripts/verify-p06-runtime-role.mjs` and `scripts/verify-staging-address-reservation.mjs`. Do not invoke an expired provider runner or accept environment DATABASE_URL/credentials as the disposable target. Use a newly named local database on an explicitly verified Unix socket, refuse existing role/database collisions, use synthetic data only and remove only resources created by that test. Preserve any pre-existing local service/data.

Finite proof checklist:

- Verify actual role/session identity, database/socket target, no inherited/elevated rights and exact initial grants.
- Bind controlled-v2 policy through the real service; prove exact replay, concurrent binding and audit rollback.
- Reserve a request, make one mocked Checkout call, persist returned references, recover the same active request and exercise lost-response replay. Provider transport must be mocked; database/Prisma must be real.
- Process locally signed authentic-format events through the real service; prove settlement, duplicate/concurrent event handling, wrong account/resource/money/mode/signature refusal, late-event monotonicity and audit rollback.
- Exercise existing operator board/detail/payment/event read dependencies through the current services and authentication-context/role guard assertions with the real restricted database client. Keep the existing desktop/mobile recovery browser fixture as a separate synthetic API regression; do not describe it as an integrated database/browser proof. No new screen or browser harness is included; integrated attended acceptance remains a later separately authorized gate.
- Deny tenant/job/actor reassignment, excluded columns/tables, all destructive writes, catalog secrets, SET ROLE escalation, memberships, schema/role/database creation and adjacent booking/dispatch/message/subscription writes. Preserve original P06 restrictions and rerun its applicable negative proof.
- Exercise partial failure/interruption; close clients; verify test role NOLOGIN, connection limit zero, past expiry and zero sessions before removing only newly created disposable resources. An unconfirmed cleanup is a failed proof.

Proposed verification commands, after approval and implementation: `npm run build`; `node scripts/verify-p07-payment-runtime-role.mjs`; `npx jest --runInBand src/jobs/job-payment-policy.service.spec.ts src/payments/payment-requests.service.spec.ts src/payments/stripe-webhooks.service.spec.ts src/jobs/dispatch-board.service.spec.ts src/jobs/routing.service.spec.ts`; `npm run lint`; `npm run arch:check`; backend governance baseline; governance frozen-baseline/consistency/25 safeguards; and both `git diff --check` checks. The unchanged synthetic browser regression is `node ui/scripts/payment-request-recovery-browser-qa.mjs`, using its existing local build/Playwright seam. It does not supply real-role permission evidence; that belongs to the new actual-login service proof. No new browser harness is proposed.

Observable finish: a source-hashed, actual restricted-role proof across the connected payment path, preserved P06 denials, verified local cleanup and a final exact grant boundary suitable for a separately reviewed live proposal. Mocked Prisma success, a role-creation helper or health 200 alone cannot satisfy this card.

Rollback: discard the new local fixture/proof changes and remove only that proof's disposable resources; no external state has changed. Any need for application/schema changes, more tables/writes, a new surface or infrastructure is a stop and a further proposal before implementation.

## Change impact and actual decisions

This is a newly demonstrated material prerequisite, not a new customer feature or acceptance milestone. It adds real-role permission proof and, only after later approval, dedicated runtime credential provisioning to existing R1-W01. Effort and timing are not yet measured. Do not manufacture a completion percentage, launch date or silently add ledger rows.

Unchanged: APP-013 sole Now; Next APP-017 → APP-018 → APP-019 → APP-015 → APP-016 → APP-033; accepted 1A/1B/2A/2B; 3A → 3B → 3C → 3D; R1 ledger denominator 27; legacy measures 6/60, 4/8, 0/13.

Actual owner decisions: selected 4:00–5:15 availability; approved narrow split-read local correction only. **This dedicated-role prerequisite, its local implementation/proof and every external action remain unapproved.** Implementer owns completing the exact local proof card and evidence if approved. Debynyhan Banks owns prerequisite approval, later exact provider/database/deployment/spend approval and final 3A acceptance.

Scope status: explicit deviation proposal before implementation. No grants, role/credential creation, secret payload access, provider operation, deployment, payment, booking, customer contact, repository merge or production change occurred.
