# APP-013 / 3A / P08 — BD1 exact billing read proposal

PREPARED, NOT APPROVED. Approved local BD1 implementation9bae048 is complete. This is separate external qualification-only authority. R33 remains consumed, underlying error UNKNOWN. No recovery, SQL password, test-account identifiers or Sandbox endpoint entry needed.

Exact scope 958e31e8f2e813ffae79407426520e8ddb3183ea1cb74327256dd088c6354bce, packet APP013_P08_BILLING_DIAGNOSTIC_PACKET_BD1_20261112.json; readiness APP013_P08_BILLING_DIAGNOSTIC_READINESS_BD1_20261112.json. Source9bae04860292bcfeca8591570b30627ff60c588d. Projectsignmons, ownerdebynyhan@signmons.com and original project/account fingerprints remain pinned.

## Exact action and SDK exception

Three CLI invocations at most, once each in order, using installed pinned /opt/homebrew/bin/gcloud:

1. auth list --filter=status:ACTIVE --format=json(account,status)
2. projects describe signmons --format=json(projectId,projectNumber,lifecycleState)
3. billing projects describe signmons --format=json(billingAccountName,billingEnabled,projectId)

The exact generated argv vectors in readiness are authoritative. Wrong owner/project/config/source or output shape stops before further calls. No token-print command, separate cache read, SQL, explicit HTTPS adapter, billing change, deployment, IAM/secret action, payment or spending. CLI provider requests and SDK internal authentication retries are not bounded by counting three CLI invocations.

Approve the existing SDK credential refresh/cache-metadata maintenance/internal-retry exception for these three exact commands only. Persistent SDK credential/cache state may change and remains retained. This does not authorize forced browser sign-in, manual reauthentication, alternate account or configuration; if required, stop with safe category or UNKNOWN. Prior TR6 validity evidence only covered8:15 and is historical; no assumption of present validity or hidden renewal. Actual current credential usability is part of this bounded diagnostic, not an execution-readiness claim.

## Time, privacy and independent cleanup

November12 Eastern: start8:29 a.m.; launch before8:36; reads end8:38; independent closeout by8:39. Each existing owned CLI invocation has maximum30seconds within the fixed deadline, with its existing cleanup reserve; no replay, deadline extension or automatic second invocation. Reserve fresh exclusive mode700 operation root and mode600 envelope/attempt/command receipts before reads; reject existing root. Exact committed decision/source/window must match at launch.

Invoke pinned Python qualification_launch.py --diagnose-billing <private-envelope-path>, then independent --closeout-billing <exact-operation-root> even after failure when the root exists. The existing diagnostic capability validates source/SDK/config and reserves each exact descriptor. Existing owned runner drains stdout/stderr concurrently with shared MAX_OUTPUT/time bounds for billing only, then terminates/reaps owned groups as necessary and closes pipes. Owner/project stderr remains discarded. Raw token/account/error text never printed, saved or hashed. Retain fixed category/boolean/count/time receipts only; envelope contains public pins and decision reference, no recovered private inputs. Interrupted/missing normal closure yields PROCESS_HISTORY_UNKNOWN; never signal a guessed PID or call it verified. Remove owned temporary launcher/reference files after process closure; no SDK signout/cache erasure.

Known anchored SDK HTTPError401/403/408/503/504 may produce safe error categories. Other prose, mixed/malformed/oversized output remains UNKNOWN or output-limit refusal. Success records exact shape/project/account match and billingEnabled boolean only; even enabled metadata is not full payment readiness. No corrective action follows automatically.

## Readiness, checklist and owners

Actual BillingDiagnosticCapability constructor and prepare passed at readiness timestamp using proposed authority and actual current clock. Current and committed source graph, pinned runtime, non-secret SDK configuration, all installed reviewed SDK hashes (including error-format sources) and fresh-root absence verified. No credentials/provider read during preparation. Local regression254qualification/composition+43native+43connected+52correction+25governance passed under BD1 implementation evidence; these are local proofs only. Fresh identity/resource access/outcome UNKNOWN, as intended for this qualification.

Finite work after approval: compare source/decision/time; reserve; exact three reads with short-circuit on failure; independent closeout and process/receipt verification; remove owned temporary launcher; publish sanitized result. Implementer owns execution/supervision/cleanup; owner authorizes exact reads and SDK exception; billing administrator owns any later actual policy or billing decision. Existing3A criterion remains connected payment/event/application/browser acceptance. Remaining full qualification/native/auth/payment not authorized. Accepted4/8;3A OPEN;R1newlyclosed0/27. No scope deviation beyond approved BD1 diagnostic extension; this proposal grants nothing until exact approval.
