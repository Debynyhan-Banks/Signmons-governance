# ED1 live1 — one read to identify the webhook mismatch

**Qualification-only; external approval pending.** APP-013 / 3A / P08. The exact command is prepared and locally verified. It reads the existing pinned Sandbox webhook once and reports the comparison fields that fail. It does not run R58 again or change the webhook. No scope deviation.

## Exact operation

- Backend source: `92c4d03712153558717f918e1d53fc87a54de663`, containing ED1 implementation `5ea6fcb`.
- Operation: `32337134-670a-45d0-bc83-21cf25f64cdd`. Command SHA256: `800f2a83f42a218aa18615156f984317d6c408994fb3a2a4685e884f153c37ab`.
- Exact files: `APP013_P08_ED1_LIVE1_COMMAND_20261125.py`, `APP013_P08_ED1_LIVE1_SCOPE_20261125.json`, and `APP013_P08_ED1_LIVE1_READINESS_20261125.json`. The command requires a separate committed decision that matches the complete scope and command bytes; no decision exists yet.
- One application-level HTTPS GET to Stripe's `/v1/webhook_endpoints/{privately-entered pinned ID}`, through the existing `key_check.mjs --endpoint-once --field-report` worker. One child invocation; no retry, redirect, extra account/balance query or mutation. Zero SQL, SDK commands and credential-cache reads. $0 additional spending allowance; no charge or payment authorization.
- Expected endpoint fingerprint `dbaae6448069a186dc4b9e2fc6182707dda7b61218376e9e97cd21b20b4bfeae`; URL derived by the existing resource function: `https://app013-p07-atomic---signmons-calldesk-staging-p572d6wipq-ul.a.run.app/webhooks/stripe`; API version `2026-03-25.dahlia`. Expected events come from the source-bound shared predicate, with exact order-independent list comparison and no deduplication. No raw destination ID is retained in this packet.

November 25, Eastern: launch **9:07–before 9:22 a.m.**; hidden inputs finish before **9:27**; reads end **9:28**; independent local cleanup and review end **9:30**. A late start or expired stage refuses. No automatic extension. The owner must confirm reachability through 9:30, standalone Terminal readiness and no overlapping Signmons operation.

## Owner interaction and private-data handling

The implementer opens the exact command in standalone macOS Terminal using the existing native Terminal dispatch method, activates that window, and supervises safe result files. No VS Code terminal or browser is involved. The invocation is `/opt/homebrew/bin/python3 -I -B <this reviewed command> <exact approval commit>`; only nonsecret paths and the approved commit appear in shell history.

Type READY when the command asks. Then enter, in order: **1/2 existing Sandbox secret key beginning sk_test_**, **2/2 existing pinned destination ID beginning we_**. Both prompts are hidden. Do not enter a Neon password and do not paste either value into chat. Existing TTY/getpass handling refuses echo fallback; each input has at most 120 seconds within the absolute cutoff. A malformed value closes this one attempt without an automatic retry.

Private inputs exist only in process memory and bounded child stdin. They are excluded from argv, environment, files, stdout, stderr, exception text and durable evidence. References are cleared during closeout and owned process exit is verified; no physical-memory-erasure claim is made. Safe immutable receipts contain the operation binding, request reservation, finite labels and closure flags only.

## Readiness and reuse

The accompanying readiness record binds the actual dynamic resource function, current interpreter hashes, exact argv, current source manifests, authority and timing. The real existing source guards passed with synthetic authority and zero external dispatch. The final launch comparison repeats current source/command/approval/time checks before input and before the one worker.

Fourteen new synthetic composition tests passed: exact source/authority binding, expiry during guards, Boolean/integer strictness, unsafe or missing output, useful exit-2 drift, hidden-input ordering, consumed-root refusal, real owned local child cleanup, timeout and interruption. Four independent completion probes passed: late signal veto, masked pending-signal veto/readback, restoration after publication failure and missing-history refusal. Earlier ED1 415-test proof is reused, not described as new. Current repository checks are retained with this packet.

The command reuses the tested hidden-input helper, `EndpointChild` owned-process boundary, legacy seven-field validator, VM2 immutable Journal/source guards/interruption/readback helpers and the existing containment lease. Only the eight finite ED1 field labels are added to safe output. Worker HTTP timeout is at most five seconds; body cap 64 KiB; worker work timeout at most 15 seconds, plus up to two seconds of owned-process cleanup; each output stream cap 8 KiB. Application-level retries and redirects remain refused.

The lease prevents simultaneous users of that same lock; it does not automatically exclude every Signmons workflow. Owner no-overlap confirmation and implementer local launch review are still required. Current credential usability, endpoint configuration and disabled status remain UNKNOWN; this read is intended to resolve those endpoint facts, not to claim execution readiness.

## Finish, cleanup and remaining work

Valid finite labels, including a `PAYMENT_ENDPOINT_DRIFT`/exit-2 response, are useful diagnosis. HTTP, JSON, input or transport refusal without labels remains UNKNOWN. Diagnostic completion never means the endpoint qualifies for payment. No configuration correction, disable action, webhook resend, authentication attempt or payment follows automatically.

The command reserves the attempt before prompts, verifies the actual owned child history, reaps the leader and checks group absence. Independent local closeout has no provider request. It persists safe immutable closeout/results, handles interruption without losing child ownership and restores original handlers before output. The implementer then independently checks safe receipts, related-process absence and private-file absence before preserving evidence. Existing operation root/attempt and lock inode stay consumed; no PID is adopted from disk for termination.

Rollback: no provider state changes exist to undo. On refusal, stop and close the owned local process; retain safe UNKNOWN evidence. The product owner/Stripe custodian authorizes this read and any later remedy separately. Implementer owns exact launch and closure. Same-job Sandbox payment, authentic matching signed event, application gate clearance and owner acceptance remain pending. Accepted milestones **4/8**, 3A OPEN, R1 newly closed **0/27**.
