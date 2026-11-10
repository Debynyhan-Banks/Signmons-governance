# APP-013 / 3A / P08 — R21 connected qualification approval packet

Status: EXACT OWNER APPROVAL PENDING. Recovery R21 succeeded with HANDOFF_RETAINED, liveObserved true, failure null, no residuals and resource-closeout verified. Existing guard retains inputs until18:00UTC. Existing Sandbox endpoint supplied through hidden Terminal input and matched the pinned hash. Same-process builder validated actual scope using QualificationCapability with proposed clock/decision only; no qualification provider calls yet. Runtime source dbfeeac709c3dfb3f477eb5030bbb5b497253fad; packet artifact76ffeb8; existing connected packet card applies unchanged.

Exact operation eea127d2-387a-4dbc-8a7b-45dee9e510d0. Start now but strictly before12:22pm Eastern November10; reads stop12:28, independent database cleanup by12:33, private purge by1pm. One attempt/no retry. Existing Terminal parent waits for the matching committed decision, validates real time/source at handoff, then prompts for hidden SQL password. Decline, deadline or failure invokes existing cleanup/purge. Guard PID exit requires independent readback. Later native work remains separately gated.

Authority requested: at most27 SDK commands,20 direct HTTPS requests,4 read-only SQL reservations including independent cleanup,1 existing-owner credential-cache read. Existing reviewed SDK refresh/cache/internal-retry exception applies. Check exact Cloud Run candidate/traffic/environment, billing/project identity, retired service identity and secret version metadata/IAM, service availability, effective permission checks, prospective key absence, exact disabled Firebase test identity, and admitted job/tenant/payment gate/retired database role/sessions. No secret payload reads, SDK login, IAM/configuration changes, runtime activation, Stripe calls, payments, deployment or spending. Dynamic resource bindings come from guarded R21 inputs; raw values never enter this document.

Exact approval hashes and limits follow. The decision object below is a proposal only; do not install it as authority before owner approval.

```json
{
  "stage": "qualification",
  "decisionForReview": {
    "owner": "Debynyhan Banks",
    "decision": "APPROVE_EXACT_P08_CURRENT_QUALIFICATION",
    "externalReadAuthorized": true,
    "scopeSha256": "e5b7651e015e29ffb3e738be9b162c3187494a2d0ca93d6985151a2cc26850d7",
    "cleanupScopeSha256": "3c0210224c331dd5808cc13732dea6742da5923e18c3397118e2ac3c920d233a"
  },
  "operationId": "eea127d2-387a-4dbc-8a7b-45dee9e510d0",
  "nativeScopeSha256": "8b20101a34eacb3f9ba79225adaee64fbcd9b9388074ab90666b77c4c0c34329",
  "window": {
    "start": "2026-11-10T17:10:00Z",
    "cutoff": "2026-11-10T17:22:00Z",
    "readEnd": "2026-11-10T17:28:00Z",
    "closeoutEnd": "2026-11-10T17:33:00Z",
    "purgeEnd": "2026-11-10T18:00:00Z"
  },
  "limits": {
    "cache": 1,
    "cli": 27,
    "https": 20,
    "sql": 4
  },
  "sourceCommit": "dbfeeac709c3dfb3f477eb5030bbb5b497253fad",
  "endpointHashMatched": true,
  "localCapabilityPreflight": "PASS_PROPOSED_CLOCK_ONLY",
  "providerCalls": 0
}
```

Current usable permissions and external readiness remain UNKNOWN until this one read attempt. Implementer owns launch/receipts/cleanup; owner and credential/DB custodians own this exact decision/password entry. Next observable result CURRENT_EVIDENCE_OBSERVED or truthful failure and cleanup; successful qualification alone does not accept3A. Accepted1A/1B/2A/2B4/8;3A OPEN;R1newlyclosed0/27. No scope deviation.
