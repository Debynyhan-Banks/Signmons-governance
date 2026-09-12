# Phone-only staging release authorization packet

2026-09-12. DRAFT — unresolved fields below prohibit activation or sending.

## Dedicated secrets completed with owner approval

Backend evidence/APP-013/phone-staging-secrets.md (16e0af8) records verified versions signmons-staging-phone-session-key/1 and signmons-staging-phone-digest-key/1 and resource-scoped runtime read grants. Values never printed or committed; existing Twilio credential unchanged. These are vault resources only: no deployment, enabled operator/tenant or minted session. Earlier no-new-secrets notes below are historical. Next is the exact disabled candidate release proposal, with separate build/deployment/IAM/spending approval and pinned version references. Do not repeat secret creation or infer permission to activate the test.

## Identity preparation completed with owner approval

Backend c2cee78/evidence/APP-013/isolated-phone-identity.md records disabled operator staging-phone-owner-20260912 and suspended tenant a1adcfd4-15be-404b-9ac3-5edb1fda20f0, created and read back in the existing Signmons staging identity/database systems. Exact application owner claim binds only that tenant; no email/password/phone on the identity, no session token, no new secret or IAM grant. Tenant phone approval disabled, zero customer/conversation/job records, charges/payouts false. Earlier missing-identity rows are superseded for preparation only. Existing staging tenant and provider configuration untouched.

Next is separately approved dedicated credential/session and candidate activation/release preparation. Do not enable the user or tenant, mint a token, deploy, or send from the identity-only approval. Preserve disabled/suspended state and arrange exact-target cleanup after the test/abandonment. Fixed source runtime remains ad909c8; operation script/evidence commit c2cee78 does not represent a new deployment.

## Latest private-binding preflight

Owner confirmed the US participant destination ending 3183. Full destination remains private; confirmation is not send authorization. Owner accepted keeping Stripe Checkout links for the MVP; Twilio Pay is deferred.

Official Verify pricing was checked online in the preceding conversation: https://www.twilio.com/en-us/verify/pricing publishes USD 0.05 per successful verification plus USD 0.0083 per US SMS; https://www.twilio.com/en-us/user-authentication-identity/verify states attempts are billed regardless of delivery and PAYG has no monthly minimum. One successful one-SMS base estimate is USD 0.0583. This supplies a public PAYG reference, not account-specific tax/adjustment proof or an invoice cap. Do not continue searching Product Plans for a required Verify subscription.

Current selected revision metadata binds both WEBCHAT_INTEGRATIONS_JSON and TWILIO_TENANT_IDENTITIES_JSON to tenant 059c4950-171c-4ff9-a963-20bf6b9d59a6, with Twilio environment staging. This is configuration evidence only: current tenant database state, isolation and the owner's Firebase user/role have not been qualified. No customer records, credentials or full destinations were retrieved.

Important correction: on signmons-calldesk-staging-app013smstest, DEV_AUTH_ENABLED=false and STRIPE_WEBHOOK_LIVEMODE=false, but SMS_DELIVERY_ENABLED=true and SCHEDULING_ENABLED=true. The new phone-only path has no downstream invocation, but the older tagged revision as a whole is not an all-sending/all-scheduling-disabled environment. Preserve existing traffic and settings; do not enable the phone test by blindly copying this revision. A separately approved candidate configuration must explicitly isolate the test and disable unrelated delivery/scheduling paths. No settings changed in this run.

Backend evidence/APP-012/release-checklist.md records deletion of previous disposable Identity Platform operators and tenants. No reusable current operator was established. Repository cloudbuild.deploy.yaml builds and pushes an image; it does not deploy it. Both focused branches were fetched clean; backend remains ad909c8. No new build, database query, secret access, IAM mutation, deployment or provider call.

Smallest next authorization: prepare a dedicated nonproduction tenant/operator/session and dedicated credential setup if an existing qualified operator cannot be supplied, with phone sending and other outbound operations disabled. Enumerate any required identity/secret/IAM changes before performing them. Build/deployment and the single paid OTP still require their explicit final authorization; UTC window is selected only when ready. Do not invent IDs or resurrect deleted fixture users.

## Verified this run

- Backend feature branch is clean at ad909c895a92b76b4a3b7bfbc5de2f40e3e10365; origin matches. PR #21 is open at that SHA; its returned statusCheckRollup is empty, not a new CI pass. Local validation is recorded in backend evidence/APP-013/phone-only-execution.md; not rerun for this documentation-only packet.
- Target project signmons, Cloud Run signmons-calldesk-staging, us-east5; runtime identity signmons-calldesk-runtime@signmons.iam.gserviceaccount.com.
- Normal traffic remains 100% signmons-calldesk-staging-app013bounds. Latest ready signmons-calldesk-staging-app013smstest was created 2026-09-08T00:04:15.004700Z and uses image digest sha256:37286933d882466b8592120f48eb69c34e14cdb5a23c1f37480e39a1e6ff933a. This predates the reviewed phone-only implementation.
- Selected revision metadata contains zero STAGING_PHONE_* environment names. No environment values or secret contents were printed. Artifact Registry lookup for a tag containing ad909c8 returned no matching image; this does not prove there is no differently tagged image. A new reviewed source-to-image binding is still required.
- Existing Safari Twilio account usage page shows Signmons LLC, Active, balance USD 20.00 and estimated September usage USD 26.15 (A2P fees USD 25.00 plus local number USD 1.15). No Verify line was displayed.
- Existing billing overview confirms PAYG, USD, one linked account and auto-recharge not set up. These are observations, not changes or permission to change billing. They do not establish account-specific Verify pricing or a guaranteed invoice ceiling.

## Fixed test scope

Owner is the only participant. One privately allowlisted US mobile, one isolated nonproduction tenant/conversation/session, exact authenticated owner/admin user. One SMS START and at most five CHECKs; stop on success, uncertainty or expiry. No resend or voice/email fallback. USD 0.50 is the maximum proposed application liability authorization; reserve the reviewed conservative full-flow amount before dispatch. Unrelated account usage and invoice taxes are not controlled by this path.

Use a short supervised window after deployment and private session preparation. The policy permits at most 30 minutes, but the existing session credential lasts at most 15 minutes; the operative deadline is the earlier expiry. Do not issue the session before a lengthy build/deployment or silently extend it. Exact UTC timestamps are intentionally unset until readiness.

Address calls, county admission, job creation, payments, calendar writes and confirmation messages remain off. A provider APPROVED receipt is phone-test evidence, not downstream authority. No actual test or acceptance claimed; walkthrough remains 3/8 (37.5%), not overall MVP completion.

## Remaining prerequisites — no invented defaults

| Item | Current disposition | How to resolve |
| --- | --- | --- |
| Reviewed deployment artifact | Source SHA fixed above; executable image/revision not qualified | Build/tag/digest verification through separately approved existing release workflow; no main merge or traffic promotion assumed |
| Isolated tenant and operator | Exact IDs not located in evidence inspected | Identify existing nonproduction tenant and authenticated Firebase owner/admin privately; do not infer production Eternity tenant or create records during this read-only run |
| Session and data lifecycle | No current test credential prepared; local fixtures are not staging records | Approve isolated session preparation, key references and cleanup/retention handling; deliver credential privately, never chat/repository/logs |
| Participant destination | Owner participation agreed; exact current destination not reconfirmed | Confirm privately at execution; previous test-phone assumption is not consent or current binding |
| Verify resources and protections | Prior account/service selection exists in PHONE_ONLY_STAGING_TEST_PACKET.md | Recheck exact service, effective US-only geography and Fraud Guard in existing account; no alternate service or new number |
| Fees | PAYG verified; Verify-specific rates and applicable extras unresolved | Inspect Products & Plans/account rate information, or obtain account-specific confirmation; public list arithmetic alone is not full fee evidence |
| Consent notice | Required runtime noticeVersion not selected for live test | Review exact OTP-only notice and current participant request; phone ownership is not transactional or marketing consent |
| Runtime configuration | Selected existing revision has no STAGING_PHONE_* names | Explicit approval required for new dedicated key/secret references, deployment configuration and matching database approval digest; no enable endpoint |
| Test window | Unset | Choose exact UTC interval only after prerequisites; no schedule or automation created |

Safari page reading works. Attempt to select Products & Plans through macOS accessibility was denied; no permissions were changed. Owner was asked to click that existing tab, without upgrading/changing a plan. No account-specific Verify rate inferred from the billing overview.

Owner requested a retry. The command then returned without an error, but the page stayed on Overview and the automation accessibility inventory exposed only one element, not the page controls. Reading remains available; selection is not demonstrated. No permission setting was changed or bypass attempted. Manual selection of Products & Plans is the smallest immediate unblock.

## Authorization sequence and acceptance

1. Resolve the read-only/private prerequisites above. Approve exact nonproduction configuration, isolated test records/key handling and reviewed revision deployment. Preserve existing traffic/webhooks and keep the phone switch disabled until the final test authorization. Any required IAM or billed build action must be listed explicitly, not assumed.
2. Once deployed and qualified, present the complete redacted packet with source/image/revision, private identity bindings, conservative amount and UTC window. Obtain explicit authorization for one Verify SMS to the confirmed participant. The present document does not grant it.
3. Confirm effective guards, reserve once, send once, let the participant enter the OTP privately, and observe the result. Record redacted correlation/outcome/liability and no downstream writes. Stop the test and verify refusal after stop. Never auto-retry an unknown result or erase its liability.

No new implementation section is proposed. If rates or private bindings remain unavailable, stop with that exact blocker; do not replace the live test with additional generic fixture work. Google responseId retention and county qualification remain separate full-2B admission blockers.
