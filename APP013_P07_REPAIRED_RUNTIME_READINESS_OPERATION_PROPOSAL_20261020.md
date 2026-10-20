# APP-013 / 3A / P07 exact repaired-runtime readiness operation

Status: **exact external-operation approval pending; no external action authorized**.

## Traceability and purpose

- Section: R1-W01 / APP-013 / 3A / P07.
- Criterion served: prepare one isolated, production-equivalent, zero-normal-traffic Sandbox runtime so the later separately approved P08 can request and settle one authentic payment for accepted job `9180bef4-561d-47a0-869f-925e6a3dfd96`.
- Approved prerequisites: the dedicated-role/identity/secret design in `APP013_P07_REPAIRED_DIGEST_RUNTIME_READINESS_PROPOSAL_20261020.md` and the four candidate-only startup secrets in `APP013_P07_STARTUP_CREDENTIAL_CORRECTION_PROPOSAL_20261020.md`.
- Application source/image: `465e12cf7ecf4874ddbd13a34bee60d85fbb02bd` / `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend@sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da`.
- Package: `/private/tmp/p07-repaired-runtime-readiness-20261020-prep1`; plan `139a3a66-ae17-420d-b18e-7075541e457b`; packet `6afbeebc-373b-4ae4-a552-c1a1ab673730`; operation `f8aa3170-6ac9-4b09-96d9-cc0b688fae0c`.
- Bound window: October 20, 2026, 7:00–8:30 p.m. Eastern; start strictly before 7:15; ordinary work ends 8:00; containment through 8:20; window closes 8:30. Retained resources retire by October 21 at 7:00 p.m. Eastern.

This operation prepares P07 runtime readiness only. It creates no Checkout, accepts no card, moves no money, delivers no event, books no appointment and awards no 3A acceptance.

## Exact authorized actions requested

One attended, no-retry operation would:

1. Run read-only Cloud, IAM, Stripe Sandbox and exact-job/database preflight. The owner enters the current CHILD administrator password and the single enabled Sandbox connected-account ID only into hidden Terminal prompts.
2. Create only database role `p07_payment_runtime`, initially closed, using reviewed fixture SHA-256 `35785d3857f6fc9b01042d6dee3137eebb18950601fb1b8e7644e340be8fb83c`; open it only for the bounded work period; prove exact grants, no elevation/membership/ownership and direct runtime access.
3. Create exactly six secret resources and one numeric version each: the P07 database URL, P07 webhook signing secret, disabled OpenAI placeholder, candidate admin token, conversation key and technician-link key. Reference existing `signmons-staging-stripe-secret-key:1` without reading or copying it.
4. Create only service identity `signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com` and add exactly seven resource-level `roles/secretmanager.secretAccessor` bindings. Add no project role, key, P06-secret access or other membership.
5. In the signed-in Stripe Sandbox browser, create exactly one Connected accounts destination for the tagged candidate `/webhooks/stripe`, with the approved six-event set; capture its creation-only signing secret privately, immediately disable the destination, and read back disabled state, zero deliveries, exact URL/scope/events and stable API version.
6. Deploy exact revision `signmons-calldesk-staging-app013p07atomic1`, tag `app013-p07-atomic`, from the exact image, with replacement environment/secret maps, minimum zero, maximum one and zero normal traffic. Preserve 100% normal traffic on `signmons-calldesk-staging-app013dbrot2`; prove liveness/readiness and exact configuration.
7. Perform mandatory containment: close the database role and verify zero sessions; preserve the disabled destination and zero normal traffic. On failure or uncertainty, also remove the tag, disable created secret versions, remove added bindings, disable the new identity and require Stripe absence/disabled/deleted readback.

Allowed action identifiers are exactly:

- `create_one_restricted_database_role`
- `create_six_secret_resources_and_versions`
- `create_one_service_identity`
- `add_seven_resource_secret_bindings`
- `create_disable_readback_one_stripe_destination`
- `deploy_one_zero_normal_traffic_revision`
- `mandatory_containment_and_retirement`

Checkout, card entry, payment, refund, booking, customer contact, message delivery, test event, event resend and normal traffic are forbidden. Automatic retry is false. Any stop consumes the operation.

## Guardrails, cost and closeout

- Cloud allowance: USD 1.00, not a provider-enforced cap. Six temporary secret versions have a conservative full-month equivalent of at most USD 0.36 above the free tier; actual cost is unverified and the versions retire within 24 hours.
- The controller writes a sanitized mutation journal before provider mutations. It rejects source, proposal, package, window, approval, identity, target-state or cost drift.
- Passwords, account identifiers, signing secrets, API keys, customer data and private URLs remain out of chat, command arguments and receipts.
- On success, retained state is only the zero-traffic tagged revision, disabled zero-delivery destination, closed restricted role, six numeric secret versions, one service identity and seven resource bindings until the fixed retirement deadline.
- Cleanup-only recovery is allowed after a consumed attempt. It cannot retry readiness or authorize payment. Retirement removes the tag, disables six new versions, removes seven bindings, disables the identity and confirms the role remains closed. Secret destruction and role deletion are excluded.

Success is only `P07_REPAIRED_RUNTIME_READY_DISABLED` with exact readbacks and verified role closeout. Any other result is a named `P07_STOP_*` plus `CONTAINMENT_VERIFIED` or `CONTAINMENT_UNCONFIRMED`; the latter requires cleanup-only recovery before handoff.

## Local validation and decision

The bound package passes **29/29 focused tests**, syntax checks and `P07_PREPARATION_CHECK_PASSED_NO_ACTION`. Without an exact approval record, `--run` refuses with `P07_REFUSED_OWNER_APPROVAL_INVALID`. Manifest SHA-256 is `6f3b4e1a66962d64248fab185d6388c1d2e78e68dd280d839cc57d412af5ae69`; controller SHA-256 is `e1f8fe898ae299f354f8b728afc90407ef0d0b1e6487768deaeaff4fce31258f`; test SHA-256 is `e589484982a76df6223e144092cb6546ce565d3ae2ca5be29964be913a19ab31`; binding SHA-256 is `c5eb72c440ecc1c840b94c4b25a304f0e3ffb74d553dd1c62350166bab111d8e`.

**Decision requested:** approve or refuse this exact operation before the 7:15 p.m. Eastern start cutoff. Approval authorizes only the listed external readiness actions, allowance and mandatory containment/retirement. It does not authorize P08 or payment.

Accepted progress remains **0/27 newly closed R1 packages; 6/60 legacy packages; 4/8 walkthrough milestones; 0/13 full-intelligence rows**. **No scope deviation from the two previously approved prerequisite changes.**
