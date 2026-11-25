# BA1 — exact linked billing-account status qualification

APP-013 / 3A / P08. Local preparation and independent review are complete; **no live approval is recorded**. This single read sequence checks the billing account API state after the owner confirmed the actual console Status field is Active with no alerts. It does not repeat the Secret Manager read or launch payment.

## Fixed operation and limits

Operation `089eb0aa-30dd-4931-bf61-8d099402d235`; scope `APP013_P08_BA1_SCOPE_20261124_089eb0aa.json`; scope SHA256 `dce4dbc58ca9715f195893dfd5c8010ee8dc5ca204dde3e9b493ec19d95b9d2c`. Backend source `2f13f90ae4cda3a61e719308d54cc19c1dd3c0d1`, current VM2 manifest `0c3c90cdad6cf8a1c742a37de20d9cbf8f9fcd7ad772f97fbd486dbfe71bec78`, one-shot command SHA256 `e143e8bfe1a0910c69c564fb52c97ca84ca6a971a152d5f38944779352f28dd1`, and nonsecret SDK configuration SHA256 `528ceadadc8a5491e54ee82dbad0026eda881252564f96f2be242d70d1d2f111` are bound. Owner principal is `debynyhan@signmons.com`; project is `signmons`; full billing-account reference must match fingerprint `df8c89e72b72b59ac6b06c0a20fa7d5f85a15b5d6d7450ff57a72722be172935`.

Exactly three ordered logical CLI reads are permitted:

1. Confirm the active owner account.
2. Obtain the project's linked billing-account reference in memory and verify its existing fingerprint; retain only match flags and explicit billingEnabled Boolean.
3. Read only `open` for that exact account with the existing `json(open)` descriptor; retain only the explicit Boolean.

The actual command list is in the scope. The account reference never enters a retained receipt. This format does not echo an account name, so account identity is established by the fingerprint-bound request. SDK error text is discarded; a nonzero CLI exit can yield only `PROCESS_REFUSED`, with the specific provider reason UNKNOWN.

Maximum 3 CLI; 0 separate credential-cache reads; 0 separate HTTPS, SQL or provider mutation. The explicitly included existing exception is `SDK_EXISTING_OWNER_REFRESH_CACHE_INTERNAL_RETRIES_NO_TOKEN_EXPORT`: normal Google SDK owner-token refresh, internal authentication retries and SDK-managed cache maintenance may occur within those CLI calls. This is not a logical command retry or permission to sign in as another principal. The 3-call count is not an internal network-request count. $0 additional allowance is not a hard cloud-billing cap.

## Window — November 24, 2026, Eastern

- Launch no earlier than 9:20 p.m. and strictly before **9:35 p.m.**
- Reads end by **9:38 p.m.**; each CLI also has the existing 30-second outer bound.
- Independent local closeout and final private-data review end by **9:40 p.m.**
- Owner must remain reachable through 9:40 p.m. and confirm no overlapping Signmons operation. No Terminal attendance, password entry or browser session is required.

The UTC scope rolls into November 25. One attempt only; no retry or silent time extension. A consumed/expired packet cannot be reused. Missing source/configuration/authority, a changed account link, late clock or competing identity lease prevents dispatch.

## Actual launch and closeout

After explicit approval, record the owner decision in `APP013_P08_BA1_APPROVAL_20261124_089eb0aa.json`, commit the exact scope/decision/command, and recompare source, command, nonsecret configuration, descriptors, actual clock, authority and exclusive root absence. No approval exists merely because this proposal or a synthetic decision passed tests.

Execute once using:

```text
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B
/Users/debynyhanbanks/Web Projects/signmons-governance-r08-recovery/APP013_P08_BA1_READ_COMMAND_20261124.py
<exact approval commit>
APP013_P08_BA1_SCOPE_20261124_089eb0aa.json
APP013_P08_BA1_APPROVAL_20261124_089eb0aa.json
```

These lines describe one argv invocation, not separate commands. Exclusive attempt reservations, existing identity lease, flag-only interruption, owned-child termination/reaping and process-handle absence readback are enforced by the reviewed command. An independent post-exit review must use the actual exit and printed result digest with `readback`, verify the immutable interruption veto, exact safe inventory/modes, source/configuration and absence of the operation/owned processes. Do not adopt disk PIDs or treat an abnormal-exit partial result as success. Retain only safe flags, Booleans, finite failure code, timestamps, counts and hashes; no raw provider output or billing identifier. Shared owner credential caches are not deleted or represented as private operation inputs.

## Verified readiness and remaining unknowns

`APP013_P08_BA1_ACCOUNT_STATUS_CARD_20261124.md` records acceptance traceability, finite boundaries, exclusions and existing components. `APP013_P08_BA1_READINESS_20261124.json` records current source/runtime/SDK/configuration checks, fixed descriptor validation, absent operation root, actual installed SDK serialization/full-reference proof with zero network/credential calls, and two passing runs of the same 18-test assembled-command suite. Independent review has no remaining findings. The suite covers true/false/missing values, malformed output, account mismatch, privacy, exact reservations, authority, concurrency, replay, timeout/interruption, actual inert owned-child reaping and independent exit/digest/veto interpretation. Existing unchanged runtime suites are prior evidence, not new tests.

Current live credential usability, project link, account API `open` and successful closeout remain UNKNOWN until this separately approved qualification. Fixture success is not current provider evidence. If a read fails, record its safe stage/category and close out; do not start another diagnostic or payment attempt automatically.

No sign-in, secret payload, payment, billing/account configuration, IAM, customer data/contact, support contact or new application subsystem is included. Implementer owns exact launch, evidence reconciliation and independent closeout; owner/cloud billing custodian owns external authorization and any later remedy. Finish is one sanitized matched account-level observation or bounded UNKNOWN with closure. Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. **No scope deviation.**

Approval basis: the owner-approved browser review did not authorize this new CLI sequence, and prior bounded CLI attempts/windows are consumed or expired. AGENTS.md states, “Readiness review does not itself authorize provider reads or changes.” The current proceed authorizes routine preparation within the existing card; this final exact external decision is separate.
