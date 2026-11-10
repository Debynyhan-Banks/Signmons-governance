# APP-013 / 3A / P08 — exact R24 connected Sandbox native approval

Status: OWNER/CREDENTIAL/PROVIDER/DB APPROVAL PENDING. This is the native/payment stage, not another qualification. R24 qualification succeeded with current observations for all nine checks, no failed database checks, failure null, no residuals and independent SQL closeout. Candidate below is copied exactly from its receipt and binds the same native scope; private envelope remains only in the attended parent, guarded until4pm. Versioned wrapperf6f74cf; runtime source f6f74cf3f24b27d48dfaa6c6afc90c18925e2c9e. Current source/manifest/SDK checks passed locally before this proposal; no native attempt exists or is authorized yet. This document does not fabricate a successful native Capability check: existing handoff validates the complete private envelope against exact committed approval and actual clock before entry.

## Exact operation and time

Operation48812ecf-d99a-4357-9038-43fa925c24c6. November10 Eastern: launch3:28–strictly before3:38; payment work ends3:46; all work3:47; independent cleanup3:58; private purge4:00. Same original R24 custody deadline. One attempt, no automatic retry; one logical Sandbox Checkout request with the new request key in the R24 spec. Qualification evidence valid through3:58 for this scope only. No consumed R21/R22/R23 reuse.

## Exact authorized actions if approved

1. Read the pinned signmons-staging-stripe-secret-key version1 in memory; require a test key. Read/validate only the existing hash-bound Disabled webhook endpoint, fixed API2026-03-25.dahlia, URL and six events before activation. No endpoint creation, signing-secret rotation or production payment.
2. Temporarily enable existing signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com and retire it at cleanup. Enable/disable version1 of exactly signmons-staging-p07-payment-database-url, signmons-staging-p07-stripe-webhook-secret, signmons-staging-p07-disabled-openai-key, signmons-staging-p07-admin-token, signmons-staging-p07-conversation-key, signmons-staging-p07-technician-link-key. Add/remove the runtime identity's secretAccessor bindings on those six and signmons-staging-stripe-secret-key. Existing restoration reads are source-bound; no new secret/version.
3. Add/remove bounded conditional bindings for existing projects/signmons/roles/signmonsP08FirebaseUserLookup (firebaseauth.users.get) and projects/signmons/roles/signmonsP08ServiceAccountSignBlob (iam.serviceAccounts.signBlob). Conditions derive from exact operation/start/workEnd through the locked bridge. No custom-role creation or permanent grant.
4. Add/remove only temporary Cloud Run tag app013-p07-atomic pointing to existing candidate signmons-calldesk-staging-app013p07atomic1 and pinned image sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da. Existing normal revision signmons-calldesk-staging-app013dbrot2 remains100percent. No deployment or percentage change.
5. Temporarily set p07_payment_runtime LOGIN, connection limit6 and validity through workEnd, then NOLOGIN/limit0 and owned-session cleanup. Exact existing disabled test ADMIN/app/Firebase identity is enabled for bounded token/authentication flow, then tokens revoked and identity disabled. Passwords entered hidden, not printed or persisted.
6. Create/delete only owned key signmons-p08-48812ecfd99a4357903843fa925c24c6 with API restriction identitytoolkit.googleapis.com. Enable API Keys service only if required; retain enabled under the existing contract. Current qualification reports required services usable. No new credential login or broader key restriction.
7. Use the same authenticated session to open the existing private local payment bridge, bind the admitted job's current approved policy, create one logical Sandbox Checkout, let the owner complete it, and inspect authentic matching signed event plus canonical payment/job state. Temporarily enable/disable only the hash-bound existing Sandbox webhook endpoint. Uncertain creation uses the same request key and existing bounded recovery, never a new payment. No real charge/refund, booking, dispatch, messages/customer contact or new spending allowance; allowanceUsd0 and existing holds remain unchanged.

## Budgets and cleanup

Parent ceilings192CLI/100HTTPS/60SQL/6children/200reservations per child. Endpoint14maximum; application30combined reads,1policy bind,2create transmissions with one key,1recovery. Up to6pinned secret reads; existing reviewed SDK refresh/cache/internal retries apply. These are reservation ceilings, not claims about total provider network requests or free infrastructure.

The already waiting parent consumes only the exact committed decision below after3:28. Existing handoff validates source/private scope/qualification and actual deadlines; no changed pin may be silently rebaselined. entry.py --run uses the owned native envelope. Its exit2 pending cleanup must still run --closeout in finally. Cleanup verifies endpoint Disabled, token revocation/disabled identity, runtime/database role/key/IAM retirement and session absence. Recovery guard purge runs in outer finally even if approval expires/is declined, with raw-file absence and guard PID exit independently inspected. Never restart work on error. Any unverified residual remains UNKNOWN and blocks acceptance.

Owner must stay at Terminal and in chat to enter hidden credentials and complete only the Sandbox Checkout. Next observable result: connected native/payment receipt, authentic event/application state and independent cleanup. Payment UI completion or a redirect alone is not acceptance. Implementer owns command/cleanup verification; owner/custodians own exact authority and hidden input. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. No scope deviation.

## Bound review record (proposal only)

```json
{
  "stage": "native",
  "decisionForReview": {
    "owner": "Debynyhan Banks",
    "decision": "APPROVE_EXACT_P08_CONNECTED_PAYMENT",
    "externalActionAuthorized": true,
    "operationId": "48812ecf-d99a-4357-9038-43fa925c24c6",
    "scopeSha256": "3ac57f1a8f11d8ff76ddaa641f0dd565e161bcb312ae32a0f321e36ced65f056",
    "sourceManifestSha256": "779524b3d50edad5c049960b8acb44acfd07905a9b0d87a046ee81a265bf8a80"
  },
  "operationId": "48812ecf-d99a-4357-9038-43fa925c24c6",
  "window": {
    "start": "2026-11-10T20:28:00Z",
    "cutoff": "2026-11-10T20:38:00Z",
    "workEnd": "2026-11-10T20:47:00Z",
    "cleanupEnd": "2026-11-10T20:58:00Z",
    "purgeEnd": "2026-11-10T21:00:00Z"
  },
  "paymentWorkEnd": "2026-11-10T20:46:00Z",
  "qualification": {
    "checks": {
      "billing": true,
      "database": true,
      "effectiveAccess": true,
      "firebase": true,
      "job": true,
      "owner": true,
      "privateInventory": true,
      "retiredRuntime": true,
      "services": true
    },
    "operationId": "48812ecf-d99a-4357-9038-43fa925c24c6",
    "qualifiedUntil": "2026-11-10T20:58:00Z",
    "roleAclSha256": "649d517af81c235f8045894d73207b7d892b3607ee165418151af6b9975c1560",
    "runtimeEnvironmentSha256": "b3b3e19722bbd8f5ceadb94323e86612e4b26b8bc896b1d0223e74e683f67cc8",
    "scopeSha256": "24c4e7b2442527389f6e9d26818f7d39a23b7de6d6d3828ead8a6c2370f4ac6b",
    "status": "QUALIFIED_FOR_NATIVE_ENTRY"
  },
  "limits": {
    "cli": 192,
    "https": 100,
    "sql": 60,
    "child": 6,
    "childRequests": 200
  },
  "sourceCommit": "f6f74cf3f24b27d48dfaa6c6afc90c18925e2c9e"
}
```

Current readiness20:11UTC: exact candidate matched current qualification receipt; all nine checks true, liveObservedtrue, failure null, residuals empty; independent-closeout receipt exists. Guard alive and purge receipt absent after qualification consumption; native root absent. Corrected f6f74cf source/native manifest and35SDK hashes verified. Actual source includes forced publication/startup contention and two-transfer/cleanup proof. Current full private scope remains only in the waiting parent; native handoff must validate exact committed approval, scope and actual start time. Current native activation/payment state is not yet observed. No provider action by this review, no changed scope or authority inferred. Implementer owns launch/verification/cleanup; owner/custodians own exact approval and hidden input. Next observable result native attempt/payment evidence and verified independent cleanup;3A remains OPEN. No scope deviation.
