# APP-013 / 3A / P08 — exact R23 connected Sandbox native approval

Status: OWNER/CREDENTIAL/PROVIDER/DB APPROVAL PENDING. This is the native/payment stage, not another qualification. R23 qualification succeeded with current observations for all nine checks, no failed database checks, failure null, no residuals and independent SQL closeout. Candidate below is copied exactly from its receipt and binds the same native scope; private envelope remains only in the attended parent, guarded until3pm. Versioned wrapper96bd05e; runtime source 96bd05ed2cd74fe071ee7b9cacef5214e30bb6f6. Current source/manifest/SDK checks passed locally before this proposal; no native attempt exists or is authorized yet. This document does not fabricate a successful native Capability check: existing handoff validates the complete private envelope against exact committed approval and actual clock before entry.

## Exact operation and time

Operation695e247a-3a09-4841-95e6-cceecb6de7a4. November10 Eastern: launch2:28–strictly before2:38; payment work ends2:46; all work2:47; independent cleanup2:58; private purge3:00. Same original R23 custody deadline. One attempt, no automatic retry; one logical Sandbox Checkout request with the new request key in the R23 spec. Qualification evidence valid through2:58 for this scope only. No R21 reuse.

## Exact authorized actions if approved

1. Read the pinned signmons-staging-stripe-secret-key version1 in memory; require a test key. Read/validate only the existing hash-bound Disabled webhook endpoint, fixed API2026-03-25.dahlia, URL and six events before activation. No endpoint creation, signing-secret rotation or production payment.
2. Temporarily enable existing signmons-calldesk-p07-runtime@signmons.iam.gserviceaccount.com and retire it at cleanup. Enable/disable version1 of exactly signmons-staging-p07-payment-database-url, signmons-staging-p07-stripe-webhook-secret, signmons-staging-p07-disabled-openai-key, signmons-staging-p07-admin-token, signmons-staging-p07-conversation-key, signmons-staging-p07-technician-link-key. Add/remove the runtime identity's secretAccessor bindings on those six and signmons-staging-stripe-secret-key. Existing restoration reads are source-bound; no new secret/version.
3. Add/remove bounded conditional bindings for existing projects/signmons/roles/signmonsP08FirebaseUserLookup (firebaseauth.users.get) and projects/signmons/roles/signmonsP08ServiceAccountSignBlob (iam.serviceAccounts.signBlob). Conditions derive from exact operation/start/workEnd through the locked bridge. No custom-role creation or permanent grant.
4. Add/remove only temporary Cloud Run tag app013-p07-atomic pointing to existing candidate signmons-calldesk-staging-app013p07atomic1 and pinned image sha256:36f887749947c0b01db683482c081ca663534e7ffe597560b24597f3d46be9da. Existing normal revision signmons-calldesk-staging-app013dbrot2 remains100percent. No deployment or percentage change.
5. Temporarily set p07_payment_runtime LOGIN, connection limit6 and validity through workEnd, then NOLOGIN/limit0 and owned-session cleanup. Exact existing disabled test ADMIN/app/Firebase identity is enabled for bounded token/authentication flow, then tokens revoked and identity disabled. Passwords entered hidden, not printed or persisted.
6. Create/delete only owned key signmons-p08-695e247a3a09484195e6cceecb6de7a4 with API restriction identitytoolkit.googleapis.com. Enable API Keys service only if required; retain enabled under the existing contract. Current qualification reports required services usable. No new credential login or broader key restriction.
7. Use the same authenticated session to open the existing private local payment bridge, bind the admitted job's current approved policy, create one logical Sandbox Checkout, let the owner complete it, and inspect authentic matching signed event plus canonical payment/job state. Temporarily enable/disable only the hash-bound existing Sandbox webhook endpoint. Uncertain creation uses the same request key and existing bounded recovery, never a new payment. No real charge/refund, booking, dispatch, messages/customer contact or new spending allowance; allowanceUsd0 and existing holds remain unchanged.

## Budgets and cleanup

Parent ceilings192CLI/100HTTPS/60SQL/6children/200reservations per child. Endpoint14maximum; application30combined reads,1policy bind,2create transmissions with one key,1recovery. Up to6pinned secret reads; existing reviewed SDK refresh/cache/internal retries apply. These are reservation ceilings, not claims about total provider network requests or free infrastructure.

The already waiting parent consumes only the exact committed decision below after2:28. Existing handoff validates source/private scope/qualification and actual deadlines; no changed pin may be silently rebaselined. entry.py --run uses the owned native envelope. Its exit2 pending cleanup must still run --closeout in finally. Cleanup verifies endpoint Disabled, token revocation/disabled identity, runtime/database role/key/IAM retirement and session absence. Recovery guard purge runs in outer finally even if approval expires/is declined, with raw-file absence and guard PID exit independently inspected. Never restart work on error. Any unverified residual remains UNKNOWN and blocks acceptance.

Owner must stay at Terminal and in chat to enter hidden credentials and complete only the Sandbox Checkout. Next observable result: connected native/payment receipt, authentic event/application state and independent cleanup. Payment UI completion or a redirect alone is not acceptance. Implementer owns command/cleanup verification; owner/custodians own exact authority and hidden input. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. No scope deviation.

## Bound review record (proposal only)

```json
{
  "stage": "native",
  "decisionForReview": {
    "owner": "Debynyhan Banks",
    "decision": "APPROVE_EXACT_P08_CONNECTED_PAYMENT",
    "externalActionAuthorized": true,
    "operationId": "695e247a-3a09-4841-95e6-cceecb6de7a4",
    "scopeSha256": "e4ded971d20ec57817eec88a76049cdf23deec6e4e83370d279dfeb72b43cdaa",
    "sourceManifestSha256": "2998fccd1c51874512eb0b95272ee5d29fa3c640444ed07916248df638ed6754"
  },
  "operationId": "695e247a-3a09-4841-95e6-cceecb6de7a4",
  "window": {
    "start": "2026-11-10T19:28:00Z",
    "cutoff": "2026-11-10T19:38:00Z",
    "workEnd": "2026-11-10T19:47:00Z",
    "cleanupEnd": "2026-11-10T19:58:00Z",
    "purgeEnd": "2026-11-10T20:00:00Z"
  },
  "paymentWorkEnd": "2026-11-10T19:46:00Z",
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
    "operationId": "695e247a-3a09-4841-95e6-cceecb6de7a4",
    "qualifiedUntil": "2026-11-10T19:58:00Z",
    "roleAclSha256": "649d517af81c235f8045894d73207b7d892b3607ee165418151af6b9975c1560",
    "runtimeEnvironmentSha256": "b3b3e19722bbd8f5ceadb94323e86612e4b26b8bc896b1d0223e74e683f67cc8",
    "scopeSha256": "d688c588e710109725890e1d235a2e4cd67df599bc8ee262c731de8c1330ea38",
    "status": "QUALIFIED_FOR_NATIVE_ENTRY"
  },
  "limits": {
    "cli": 192,
    "https": 100,
    "sql": 60,
    "child": 6,
    "childRequests": 200
  },
  "sourceCommit": "96bd05ed2cd74fe071ee7b9cacef5214e30bb6f6"
}
```

Current readiness19:14UTC: exact candidate matched current qualification receipt; all nine checks true, no failure/residuals. Guard PID alive and purge receipt absent after qualification input consumption. Corrected96bd05e source/manifests/SDK verified. No native attempt or resource activation. Existing same-parent private scope remains guarded; exact committed approval and actual start gate still required. PriorR22 approvals are not reused.
