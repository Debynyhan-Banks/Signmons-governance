# APP-013 / 3A / P07 — atomic webhook transition repair

Status: **owner-approved focused local repair implemented and tested locally**. Owner explicitly answered “Approve focused local repair” to the bounded webhook repair and recovery-hold probe clarification. Implementation-entry heads: backend 83b7a2cb7d959e14dc32a2e4cac9baab049c45c8; governance 16f4b881a58bc22c44712b8711f0bad32fdfb506. This is the smallest next action after the owner-approved real local payment-role proof. Existing R1-W01/3A acceptance, same-job identity, section order, queue and denominators remain fixed. No external operation or reusable window is authorized.

## Demonstrated gap and traceability

Source entry backend `f5931e214a1f40dee63c311bad1837e51255f29f`, governance `1010571d84eb66e9d2b6eee256380fd225b558cd`. The failing image application source was `cec82163bd67fe939d88aacb6fedf2d9c126b90e`; the locally tested repaired source is now committed at `465e12cf7ecf4874ddbd13a34bee60d85fbb02bd`. Evidence: backend `evidence/APP-013/p07-payment-runtime-role-local-proof-20261020.md`; reproducible real-database case in `scripts/verify-p07-payment-runtime-role.mjs`.

Exact acceptance served: only authentic matching events clear the same job's payment gate; failed, duplicate and late/out-of-order outcomes cannot regress settled state. The current service reads Payment and computes its transition before opening the event transaction. Two distinct events can read PENDING; paid then commits SUCCEEDED, while the stale failure subsequently overwrites it to FAILED. The proof preserves actual Prisma/database responses and controls only scheduling. This is a demonstrated customer-path defect, not a new product feature.

The tested payment-role grants support the successful path and its negative permission boundaries; broader grants cannot fix this race. The unused existing image contains the defect and is not ready for payment acceptance.

## Recommended bounded change and alternatives

Serialize transition decisions on the exact payment row inside the existing transaction, then re-read/revalidate its latest tenant/account/resource/job/request/money binding before calculating and persisting the transition. Keep event uniqueness, atomic event/payment/audit writes, exact resource identity, signature/mode checks and existing state policy. An exact row lock or equivalent guarded transactional update is acceptable only if the actual restricted-role proof demonstrates both interleavings and terminal-state preservation. Do not grant new rights merely to support an implementation choice; the tested role already has payment SELECT and limited UPDATE rights.

Reject delaying callbacks, ignoring all failures, weakening signature/resource checks or accepting a sequential-only test as the fix. A new queue, payment stack, schema, SDK, provider API or generic reconciliation subsystem is excluded.

## Owner-approved finite implementation card

Expected application files: `src/payments/stripe-webhooks.service.ts` and its existing `.spec.ts` only. Reuse and extend the existing local real-role verifier, SQL fixture and evidence. Normal section/status documents may change. No new app endpoint, UI, policy, database role grant, schema/migration or provider operation is included.

Checklist:

1. Move the final payment-state decision into the existing event transaction with exact-row serialization and current-state revalidation. Maintain the duplicate event path and atomic audit rollback. No provider call occurs inside the transaction.
2. Add focused unit regressions for the transactional boundary; retain the real mixed-event counterexample and test both success-first and failure-first ordering. Prove identical-event concurrency, sequential late expiry/failure, wrong resource/account/money/mode/signature, terminal success/refund-state preservation and audit rollback.
3. Rerun the actual restricted-role proof, including existing policy/request/dispatch/refusal/cleanup behavior. The race must become green without changing its expected SUCCEEDED result or using mocked database responses. Stop if new grants, app surfaces or schema are needed.
4. Run build; the full affected webhook/payment/policy/dispatch Jest suites; lint; architecture; the unchanged isolated synthetic browser regression only if affected behavior warrants it; governance baseline/consistency/25 safeguards; and both whitespace checks. The browser regression already passed under localhost/external-block controls; do not reuse staging-pinned output with a localhost-only interceptor.
5. Publish source hashes and true local findings for review. No live payment acceptance is awarded. Any later image build/deployment must use the repaired source through a fresh exact proposal/approval; the old image/consumed operations cannot be replayed as payment-ready.

Exact local commands reuse the approved card: `npm run build`; `node scripts/verify-p07-payment-runtime-role.mjs`; `npx jest --runInBand src/payments/stripe-webhooks.service.spec.ts src/payments/payment-requests.service.spec.ts src/tenants/organization-payment-policy.spec.ts src/jobs/dispatch-board.service.spec.ts src/jobs/routing.service.spec.ts`; `npm run lint`; `npm run arch:check`; current governance commands. The verifier creates only its own private PG18 Unix-socket cluster with TCP disabled and mocked Checkout transport.

Identity/retention: keep current app context and exact tenant/job/payment/provider-resource bindings; no customer/provider payloads, credentials, raw event bodies or Checkout URLs in evidence. Locally signed synthetic events remain synthetic. Cleanup must verify role closed/expired/limit0/sessions0 and remove only the owned test database/role/cluster. Preserve accepted P06 fixture/negative behavior and all historical operation receipts.

Observable finish: the same real-role counterexample leaves SUCCEEDED after the late failure, all applicable positive/negative/concurrency/rollback/cleanup gates pass, and a reviewable repaired source is ready for a later image/runtime proposal. Rollback: revert only this local patch and test changes; no external state has changed. Implementer owns implementation and evidence if approved; Debynyhan Banks owns approval, later exact external actions and 3A acceptance. Size: bounded to the existing webhook transaction, moderate confidence from the reproduced gap; no ETA is promised.

## Recovery-hold observation and explicit test clarification

The proof also probed **immediate** retry after a deliberately rejected post-Checkout audit. It observed Conflict409 because an existing PENDING reservation is protected for five minutes. The same key recovers the same mocked Checkout after that timeout. Ordinary lost-response recovery with already persisted references passes.

Recommendation: retain that existing five-minute safety hold for this repair. Immediate recovery after database rollback is not an established product promise and should not silently become an additional MVP feature. The owner approved this proposal; explicitly clarify the exploratory probe to expect truthful Conflict409 during the hold and same-key recovery after the existing timeout, preserving the original failed-run evidence. This is not permission to remove the failure test, create a second Checkout, reset a hold, change the timeout or turn the mixed-event race green by changing its assertion. Any immediate-recovery enhancement needs a separate demonstrated need and proposal.

## Authority and scope impact

Owner explicitly approved this focused local application repair after the local permission proof and isolated browser rerun. The approved decision covers the focused local atomic webhook repair and the documented recovery-hold probe clarification only. No live grants/credentials, secret access/change, cloud build, deployment, event delivery/resend, Checkout, charge/refund, booking, customer contact, merge or production action is included.

This is an explicit defect-repair proposal before implementation, inside existing APP-013/3A/P07/R1-W01. It changes neither protected acceptance criteria nor package/section counts. Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. Original browser artifact drift and uncertain external request effects remain disclosed in the linked evidence; later owner approval does not retroactively authorize that initial run.

Implementation choice within this approved card: retain initial no-write resource/money validation, discard its provisional transition, acquire the exact Payment id/tenant FOR UPDATE inside the existing transaction, revalidate current tenant/account and re-find the exact resource using that transaction, require the original payment/job binding, then compute the authoritative transition and persist event/payment/audit atomically. All callbacks use the same Payment-before-event order; duplicate processing still writes no second transition. Existing tested SELECT/column-UPDATE rights cover the lock, so no grant change is included.

## Recorded result

The approved local patch is complete. Local build/lint/architecture and five affected Jest suites 97/97 pass. The actual restricted-role verifier passes 22 checks with failures[], both commit orderings, processed event/audit evidence, full-refund terminal state, unchanged 49+13 permission refusals, and normal/SIGINT cleanup. Source, fixture/ACL and output hashes are indexed by backend evidence/APP-013/p07-webhook-atomicity-local-repair-20261020.md. Original failing evidence remains unchanged. No further grant/schema/app surface was added. No browser rerun was required for this backend-only change; prior synthetic evidence is explicitly historical.

Remaining authority is unchanged: no cloud build, deployment, live provisioning, provider event or payment approval. Fresh repaired-source review archive preparation is complete; backend evidence/APP-013/p07-atomic-repaired-source-preparation-20261020.md records exact hashes and preservation checks. Next is a concrete fresh image-build/runtime proposal and exact operation packet for owner review. No scope deviation from the explicitly approved repair; no customer acceptance or ledger completion is awarded.
