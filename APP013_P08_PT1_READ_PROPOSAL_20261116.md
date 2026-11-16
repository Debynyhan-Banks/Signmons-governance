# APP-013 / 3A / P08 — PT1 project-read timing diagnostic

QUALIFICATION ONLY; EXACT EXTERNAL APPROVAL PENDING. Preparation follows the owner's “proceed” after SQ2. This proposal authorizes nothing by itself. No installed source, manifest, shared transport or signing-runner limit changes. No Terminal/password/sign-in/payment/support contact.

## Demonstrated gap and bounded alternative

SQ2 stopped in the project CLI slot with SQ1_PROCESS_TIMEOUT after its owner predicate passed; it made no IAM change and never reached ST1's wait or SIGN. Source48a0a7d01481bb054ba47b5b73a70f8b0df94058 and safe evidence78b07e8 / APP013_P08_SQ2_RESULT_20261116.md are the baseline. Section3A still requires same-job Sandbox payment/event/gate acceptance; resolving this existing project-read prerequisite advances that same path without creating another acceptance section.

The actual bound NativeIO is evidence/APP-013/p08-https-output-category-local-20261029/source/qualification_launch.py, not the older similarly named module. Its _owned_run raises PROCESS_TIMEOUT when its parent read loop reaches deadline minus2seconds; a nonzero child exit is instead PROCESS_REFUSED. SQ1.safe_code maps that parent's PROCESS_TIMEOUT to the retained SQ1_PROCESS_TIMEOUT. Thus the parent read deadline was reached while output completion remained unconfirmed. This narrows the termination mechanism, not the remote cause; SDK startup, authentication refresh, network and provider delays remain indistinguishable in historical evidence.

SQ2 allocated an8-second envelope, including2seconds for process closure. PT1 proposes one fresh read-only owner/project sequence, using the existing AL1/AL2 direct read composition and owned-process transport. Keep owner at8seconds; give only the project command a32-second envelope with30seconds for SDK startup/read and2seconds for closure. The SDK watchdog parameter is30for that one command. This is an explicit diagnostic-only allowance increase, not a correction to all SDK calls or permission to change the signing runner.

Alternatives: stop; repeat an identical short read without learning whether the budget matters; change the signing runner globally; or observe this one isolated read under a stated longer bound. Recommend the last. If it returns correctly in over6seconds, that supports further budget review for a future workflow but does not prove SQ2's historical cause. A result within6seconds proves only current completion. A timeout/refusal remains unresolved; no automatic new read or budget increase follows.

## Exact action and command construction

Operation ac1bd7cc-5c28-4255-9203-22e80494848b. APP013_P08_PT1_READINESS_20261116.json pins owner debynyhan@signmons.com, project signmons, expected project-number hash, source/SDK/configuration hashes, exact CLI vectors and both literal watchdog bootstrap strings/hashes. Use no identity or signing action.

Exactly two SDK invocations, stopping after the first failed predicate:

1. `/opt/homebrew/bin/gcloud auth list --filter=status:ACTIVE --format=json(account,status)`; require the exact single ACTIVE owner object using the existing predicate. Maximum8-second envelope,6-second parent read horizon.
2. `/opt/homebrew/bin/gcloud projects describe signmons --format=json(projectId,projectNumber,lifecycleState)`; parse with existing strict_json and validate_recovery_project using the pinned project-number hash. Maximum32-second envelope,30-second parent read horizon.

Both commands are constructed by existing sq1_signing_boundary.sdk_command(vector, deadline), through the pinned sandbox-exec/Python/SDK path and q.sdk_environment(os.environ). For project only, verify argv[8] equals the original pinned SDK_BOOTSTRAP, then replace that argument with the readiness record's exact project bootstrap: the sole literal change is `min(8.0,end-time.time())` to `min(30.0,end-time.time())`. argv[9] remains deadline minus2 and the SDK entrypoint is unchanged. Owner uses the original bootstrap. No command argument, executable, profile or source substitution is permitted in live operation.

Dispatch once through existing q.NativeIO._owned_run with its two-second closure reserve, stdout cap65536bytes, stderr discarded and no direct retry. Sample wall/monotonic clocks immediately around dispatch and retain elapsed seconds only, not raw output. Preserve rollback/deadline checks, source/configuration comparison before each call and final closure. Defer interruption across bounded spawn/registration/owned close, then refuse subsequent reads; no unowned PID or process group is signalled. The independent watchdog bounds the SDK if the coordinating process is lost. No new installed runner is needed; any transient exact operator must retain this sequence and pass its actual interruption check before live dispatch. Failure to reproduce the reviewed composition blocks launch rather than authorizing implementation expansion.

## Window, limits and effects — November16,2026 Eastern

Launch before9:55a.m.; reads end9:57; independent local cleanup10:00; final private/process review10:02. Existing confirmed availability through10:10 covers this window. Exact live approval and current no-overlap confirmation remain required. Do not reschedule on late approval.

Maximum2CLI invocations,0direct HTTPS,0explicit token/cache exports,0SQL and0provider mutations. No SIGN, identity enable/disable, IAM binding, key/secret/runtime changes, payment or customer data. Permit the existing-owner SDK refresh/internal authentication/read-retry/cache effects within these exact bounded calls. Two CLI calls do not cap underlying SDK HTTP/cache operations. No browser sign-in, scope expansion or separate renewal. The existing SDK cache is not deleted. Additional allowance$0 is an authorization limit, not a hard cloud-billing cap; existing liabilities remain unchanged.

## Readiness, retention and independent closeout

Static source_guard (51repository/61SDK pins), current configuration comparison and actual owner/project vector/validator inspection pass. Four local probes used the exact proposed bootstrap through existing owned transport, replacing only the SDK entrypoint with an inert temporary script and shortening the absolute deadline: matching response, timeout, malformed output and wrong binding all passed with owned processes closed. Initial empty synthetic environment correctly refused HOME_OVERRIDE before subprocess dispatch; using the existing validated environment function resolved the fixture. No guard was changed. No live provider/credential calls occurred during preparation. These probes validate local behavior, not current provider availability.

The existing project's exact required keys, string project-number type/hash and ACTIVE lifecycle predicate are reused; missing/null/foreign/oversized/malformed responses cannot be success. Source/configuration drift, clock rollback, deadline, consumed root or process uncertainty blocks further reads. Current credentials and project-read outcome remain UNKNOWN, owned by cloud/credential custodians. Readiness does not imply payment or signing readiness.

Before launch, compare actual command/bootstrap hashes/source/configuration/time/resource pins and the separately committed exact owner decision against the reviewed readiness. Reserve a fresh exclusive safe root `/private/tmp/p08-pt1-ac1bd7cc-5c28-4255-9203-22e80494848b` before the first call; an existing root refuses replay. Retain only operation/source/config hashes, slot, elapsed monotonic seconds, safe error category, owner/project match flags and closure fields. Raw project output/identifiers and all SDK bodies stay in memory; do not capture stderr/debug logs or authorization material. Store no raw token, expiry or hash. No API key is used.

Always close all registered processes through existing NativeIO.close, verify exact owned process absence, source/configuration/custody and private inventory, and remove any transient operator after hash/custody verification. Preserve safe audit receipts; do not promise SDK cache deletion. Host loss or unverified process absence must retain an explicit residual. No extra provider read is authorized for closeout.

Completed local checklist: source/receipt timeout attribution; exact two-vector/budget/pin review; output/timeout/binding probes; source/configuration and static no-mutation review; concrete scope/retention/cleanup handoff. Remaining: exact owner/cloud/credential approval and no overlap; then implementer verifies any transient launch composition before one dispatch sequence, classifies safe result, independently closes and records evidence. No runtime behavior was implemented or promoted by preparation.

Next observable result: MATCHED_WITHIN_SIX_SECONDS, MATCHED_AFTER_SIX_SECONDS, a bounded process timeout/refusal, or explicit output/binding UNKNOWN, accompanied by truthful local closure. None authorizes another read, a signing run or a global timeout change. Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1newlyclosed0/27. Explicit prospective diagnostic-only timing allowance; no live deviation executed.

AGENTS.md states “Planning/implementation approval does not imply external action approval.” SQ2 is consumed and its8-second allowance cannot fund this separate longer read. The exact PT1 external decision is therefore required before launch.
