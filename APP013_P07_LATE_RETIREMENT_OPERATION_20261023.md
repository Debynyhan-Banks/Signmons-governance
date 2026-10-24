# APP-013 / 3A / P07 exact late-retirement cleanup-only operation — October 23

Status: **prepared; exact external owner approval pending. No attempt or external action.**

## Authority, evidence and timing

The original P07 deadline **October23,6:15 p.m. Eastern** was missed. This operation requests cleanup after that breach; it does not extend or rewrite the original deadline, revive readiness/payment authority or claim timely retirement. Owner supplied tonight8:15–9:15 p.m. attendance only. Local preparation was separately approved before code at8a6377a against proposal2f2a419; local proof backend200045d, governance5104ab9. All92 tests pass (30focused +62unchanged original controller), unchanged database helper/SQL/source/journal, source/inventory/privacy/owned fixture and required governance/architecture checks verified. No actual PostgreSQL/provider/browser test occurred during preparation; local mocks do not prove retirement.

- Private packet `/private/tmp/p07-overdue-retirement-20261023-prep1`; plan `89165e55-4f04-4e1c-b271-e1d11afa63b9`, packet `9f257010-5fe9-48d5-830c-8338980cbc80`, operation `3e86198b-fa22-4881-9988-d3f023c4cc32`, mode **CLEANUP_ONLY**.
- Source manifest **29fdcdbe8dd82e241ce05133c6a5d68b2ebd274c5c8a14774782ffe562dbc14b**. Original manifest006a0c5e4d204cdc8d0b0042c9336724c4b553251dacfd3b42ad17d506b6300c and journal46283a76afad78f82b12988ba9d80e631c6734fa42d86c34b614dc6ac1611638 remain unchanged. The binding will pin the immutable version of this exact proposal before asking approval.
- **Tonight October23,8:30–9:15 p.m. Eastern**. Start at/after8:30 and **strictly before8:40**. Hidden input, all cleanup calls and mandatory final readbacks end **9:12 p.m.**; owner remains until9:15 for result reconciliation. UTC start2026-10-24T00:30:00Z, cutoff00:40Z, cleanup end01:12Z.
- One exclusive reservation; **no automatic retry**, no rerun of this or either consumed original operation. No new resource, retained-resource extension, billing allowance increase, secret payload access or payment authority. Actual preexisting provider costs remain unverified; no provider-enforced cap is claimed.

## Exact finite actions requested

1. Verify local immutable source, exact original journal/resource/version inventory, fresh complete binding/proposal/owner approval and current clock before one-use reservation or hidden input. Current source/stale-receipt drift refuses; do not reconstruct missing facts by broad provider scans.
2. Owner enters current **CHILD administrator database password** only at the attended hidden prompt. The unchanged database closeout helper reads only `p07_payment_runtime` attributes/current sessions; if needed sets NOLOGIN/limit0/expired and terminates only that dedicated role's database client sessions, then verifies closed/zero sessions. No application job/customer/payment/audit query or business write, no role creation/drop/grants or P06 change.
3. Cloud project `signmons`, region `us-east5`, service `signmons-calldesk-staging`: remove only tag `app013-p07-atomic`. Read back tag absence and preserve **signmons-calldesk-staging-app013dbrot2 at100% normal traffic**, candidate app013p07atomic1 at0%. No new revision, deploy, deletion, test request, normal-traffic shift or runtime call.
4. Disable only version **1** of the six original dedicated secret resources: signmons-staging-p07-payment-database-url; signmons-staging-p07-stripe-webhook-secret; signmons-staging-p07-disabled-openai-key; signmons-staging-p07-admin-token; signmons-staging-p07-conversation-key; signmons-staging-p07-technician-link-key. Read state only; no value access, destruction, broad version enumeration or shared Stripe-key disable.
5. Remove only the seven original resource-level `roles/secretmanager.secretAccessor` bindings with conditionNone for `serviceAccount:signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com`: the six resources above plus signmons-staging-stripe-secret-key. Read back absence. Do not change another member/role/condition or project policy. Disable only that dedicated service account and read back its exact email/disabled state. No new identity, key or role/binding; no P06/shared runtime changes.
6. At fixed **P07_RETIREMENT_STRIPE_READBACK_READY**, implementer uses signed-in Stripe Sandbox in Chrome to read only **Signmons P07 same-job sandbox**, its exact candidate webhook URL and Disabled/zero-delivery status. No event test/send/resend, enable/delete/configuration change, secret reveal/copy or clipboard action. Save new private metadata-only receipt containing new operation ID, actual observed UTC time after this attempt, exact destination-name/URL hash and zero-delivery/disabled facts. Do not reuse yesterday's receipt. If missing, changed, enabled or nonzero-delivery, report the fixed unconfirmed residual; do not invent or execute a corrective provider action.
7. Fresh final normal-traffic/tag readback; save exclusive sanitized exact-operation result with completed/remaining stages and fixed failures. **P07_LATE_RETIREMENT_VERIFIED** only if every current readback succeeds before9:12 and receipt persistence succeeds; otherwise **P07_LATE_RETIREMENT_UNCONFIRMED**, explicit residuals/no retry. Interrupted hidden input cannot be called verified. Catchable/repeated signals during cleanup cannot defeat its deadline; cleanup cannot run beyond9:12. No return to P08 or role reopening follows.

## Owner command and observable finish

Do not run yet. After separate exact execution approval is recorded/validated, a new command will be released for at/after8:30 and strictly before8:40:

```sh
cd '/private/tmp/p07-overdue-retirement-20261023-prep1' && /opt/homebrew/bin/python3 -B cleanup.py --retire
```

Only that new cleanup.py command; never legacy/controller.py or any expired command. Keep Terminal open. Have the current CHILD administrator database password and signed-in Stripe Sandbox ready; share only fixed P07_ status lines. Do not type any password, signing secret or private link into chat. At Stripe marker, wait for fresh metadata reconciliation; no Stripe signing secret is needed.

Observable finish: exact role closed/zero sessions, original tag absent/normal traffic100%, six exact versions DISABLED, seven exact bindings absent, dedicated identity disabled, exact Sandbox destination still disabled/zero deliveries, all current readbacks and correlated result. Original deadline remains missed even on success. No payment/3A acceptance credit. Evidence retains historical source/approvals/failed test logs and all consumed receipts; do not delete business records or private credentials by broad cleanup. No actual private candidate receipt was created by yesterday's unstarted diagnostic.

## Exact decision requested

Approve/refuse **this one exact late-retirement cleanup-only operation**, including only the listed database closure/session termination, Cloud tag/secret-version/binding/identity cleanup and narrow Stripe browser metadata readback within the fresh window, with mandatory current readbacks and no retry. This does not approve payment/Checkout/events, booking/messages/customer contact, diagnostics/Firebase/operator selection/token issuance, provision/deploy/build, new grants/secrets/resources, additional allowance or original-retention extension. If cutoff passes before launch, do not start or silently rebind.

Accepted1A/1B/2A/2B; **0/27 newly closed R1;6/60 legacy;4/8 walkthrough;0/13 intelligence** unchanged. P08 operator selection/payment remain pending. **Deviation: original mandatory retirement deadline missed; this exact bounded cleanup is proposed before external action.**
