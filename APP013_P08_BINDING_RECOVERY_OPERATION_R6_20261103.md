# APP-013 / 3A / P08 — R6 exact binding recovery proposal

Status: PENDING_OWNER_APPROVAL, qualification-only. Owner requested preparation and confirmed November 3 availability from 6:00–6:45 p.m. Eastern. Availability is not external authorization. Source ef023e2f3e9f504e6c6ff7c3232a9f2b9cc3b2b2; local SDK diagnostic completion ef023e2, governance10945e7. No new code, live read, credential access or private input created. R5 scope/decision archived byte-for-byte as CONSUMED_R5; its successful resource closeout/private purge and the subsequent consumed full qualification remain immutable. Earlier R3/R4 uncertainty is unchanged.

## Exact decision

Approve one attended read-only binding recovery today **November 3, 2026, 6:00–6:45 p.m. EST**. Start at or after6:00 and strictly before6:10; work reads end6:15; resource closeout ends6:35; private data must be absent by6:45. No retry, rolling window or deadline extension. The requested scope is only two missing identifiers needed to bind the existing qualification; it does not repeat full qualification or authorize runtime/payment actions.

Operation `773f6c40-34a8-4be7-ba63-b503c611a868`; preselected later qualification `b4a78473-9082-44aa-8ba4-6da40c393c68` (no qualification authority). Scope APP013_P08_BINDING_RECOVERY_PACKET_20261103.json; canonical scope SHA256 `61597d9ad37a01f6cbd66256721989c233ec193a8dcccaeb52e378045fff5d47`. Decision APP013_P08_BINDING_RECOVERY_OPERATION_20261103.json remains PENDING_OWNER_APPROVAL / externalReadAuthorized=false.

Maximum **2 SDK CLI invocations and 3 remote SQL reads**, including normal and independent closeout. Zero direct HTTPS, explicit credential-cache inspection or token-print commands. Explicit SDK exception: existing-owner credential refresh, SDK cache maintenance and SDK-internal retries within the two commands and fixed deadlines; two commands are not a two-provider-request guarantee. No login/alternate identity or IAM/API/key/secret/billing/runtime configuration, payment, deployment, spending or customer contact is authorized.

Owner/credential/DB participant enters the SQL password once into the hidden Terminal prompt after owner/project validation. Up to120seconds is allowed, capped by remaining read/closeout deadline; explicit timeout stops. Password never goes in chat. Interrupted reconciliation may require hidden attendance again only for the unused independent closeout before6:35; no repeat work read or claim that lost process history is verified.

## Exact pins and retention

Project `signmons`, owner `debynyhan@signmons.com`; database `ep-jolly-flower-ayc6w9hv.c-5.us-east-2.aws.neon.tech:5432/neondb`, user neondb_owner. Existing verify-full TLS, /etc/ssl/cert.pem and /opt/homebrew/opt/postgresql@16/bin/psql. Commands remain the existing auth list ACTIVE projection and projects describe signmons projection, followed by existing qualification SQL projection and closeout query. No added query. Fingerprints project `37d4aa0f46ca5b8f0b81b1148bda235a0f4a9a424b6b4638ec993d889563be54`, ordered target `23d7b71141e7cdba27558c97333e6821fc76ec872a84cdc2f2f19a980bee029c` must match; no substituted value.

Manifest SHA256 `64ef0ea299b004f6ea91fa08fe6c4bf18bc0f45ba800f94b14354cf93920344a`; SDK/executable inventory digest `6ffa3de34fe1f602cdd26a1e8e6f64ec2e5a9048b1bed5e3ae5d1ff325e43a6a`. Actual source/dependency/35 SDK hashes and dynamically derived config/environment must pass the existing validators immediately before launch. No direct metadata membership is treated as usable remote access.

Only projectNumber and targetId may be written to0600 recovered-inputs.json in exclusive0700 `/private/tmp/p08-binding-recovery-773f6c40-34a8-4be7-ba63-b503c611a868`. Source-pinned independent guard must start before raw output and purge by6:45, at most45minutes. No password/token/full response persisted. A separately committed qualification approval may transfer values only to `/private/tmp/p08-current-input-b4a78473-9082-44aa-8ba4-6da40c393c68/envelope.json`, registered with the same guard and same or earlier purge deadline. No automatic qualification. If no separately approved handoff, purge and stop; no second recovery. Host/guard shutdown can leave purge UNKNOWN; authoritative owned-path reconciliation is mandatory. Unknown replacement files are not deleted. Sanitized receipts may remain.

## Shift-left readiness and finite checklist

Actual local verification timestamp `2026-11-03T22:45:43.320728+00:00`. Source/SDK/config checks were read-only; no credential-cache access. New diagnostic labels instrument QualificationIO only; BindingRecoveryIO remains unchanged and uses its existing durable owner/project/SQL reservation labels. Do not claim the new full-qualification metadata extends recovery.

| Prerequisite | Evidence and result | Responsible role / unresolved fact |
| --- | --- | --- |
| Actual serialization, null/missing/type/fingerprint and safe error handling | Existing BindingRecoveryIO/NativeIO, fixed descriptors, actual parsers; prior-turn133 qualification/recovery/model/owned TLS tests passed on ef023e2 | Implementer local proof; actual owner/project/target UNKNOWN |
| Exact resources, executable/dependency bytes, dynamic config | Existing verify_qualification_sources checks committed sources/dependencies and35 SDK files; sdk_environment and actual config_snapshot PASS at timestamp above | Implementer rechecks before launch; effective remote permissions/credentials UNKNOWN |
| Envelope/schema/identity/time pins | Actual BindingRecoveryCapability with PROOF_ONLY envelope at proposed start PASS; all new roots absent | This is schema proof only; external decision remains false |
| Client/TLS/API usability | Existing owned PostgreSQL/TLS10 tests included in prior133; exact live pins retained | Credential/DB roles approve smallest bounded recovery; actual remote compatibility UNKNOWN |
| One attempt, deadlines, concurrency, interruption, cleanup | Existing recovery guard/reservation/restart tests passed; normal and independent SQL included in3total | Implementer observes actual closeout/purge; prior success is not reusable evidence |
| Retention and transfer | Existing guard/handoff/purge implementation; fixed45minute cap, no overnight copy | Owner approves bounded retention; actual raw absence required at finish |
| Regression/governance | ef023e2 result133 runtime/local +25 governance=158PASS; not rerun as runtime proof during documentation preparation | Implementer runs current documentation/architecture/whitespace safeguards |
| Authority | Pending public decision false, no private envelope | Owner/credential/DB roles approve this exact scope/window/SDK exception before launch |

1. Review/approve this concrete packet or defer. Commit APPROVE_EXACT_P08_BINDING_INPUT_RECOVERY with externalReadAuthorized=true and unchanged scope hash only after approval.
2. Recheck actual committed source/authority/resource pins/clock/config/hash/root absence. Missing or drifted evidence blocks launch. Construct0600 envelope in exclusive0700 `/private/tmp/p08-binding-request-773f6c40-34a8-4be7-ba63-b503c611a868` only after approval; decision reference uses actual committed bytes.
3. Launch existing --recover-binding-inputs once in attended Terminal. Input is consumed before transport; observe sanitized result and normal/independent resource cleanup.
4. If matched, bind a separate qualification proposal using existing trusted helper before purge; do not infer approval. Otherwise stop/closeout. Verify exact private paths absent and guard exited by6:45; report late/unknown truthfully.

Existing executable command uses pinned Python `/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14`, flags -I -B, the same runpy launcher and source directory `evidence/APP-013/p08-https-output-category-local-20261029/source` in backend. Work entry `--recover-binding-inputs /private/tmp/p08-binding-request-773f6c40-34a8-4be7-ba63-b503c611a868/envelope.json`; independent entry `--closeout-binding-inputs /private/tmp/p08-binding-recovery-773f6c40-34a8-4be7-ba63-b503c611a868`. No entry executed during preparation. Actual command must be compared to this card before launch.

Rollback/disabled state: pending decision false, no private input; external entry refuses. After start only original bounded closeout/purge, no replay. No UI/browser/application changes; no implementation expansion.

Observable success initially HANDOFF_RETAINED with matching fingerprints and verified resource closeout; final completion requires private absence, not just retained identifiers. Failure consumes attempt and gives no execution candidate. Remaining: exact approval, actual recovery/cleanup/purge; then separate full qualification and same-job Sandbox payment/negative/replay evidence/owner acceptance. Responsible owner/credential/DB roles approve external scope; implementer performs checks and evidence. Accepted1A/1B/2A/2B4/8; R1 newly closed0/27;3A OPEN. **No scope deviation.**
