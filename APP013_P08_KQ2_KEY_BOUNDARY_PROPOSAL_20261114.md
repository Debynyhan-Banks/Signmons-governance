# APP-013 / 3A / P08 — KQ2 corrected key-only qualification

Prepared, not approved. This is one new qualification using the completed ET1 correction. No operation root, credential read, provider call, sign-in or timed password prompt has started. The owner's ET1 local approval and request to proceed authorize this preparation, not the external actions below.

## Purpose, source and exact resources

Section 3A still requires the admitted job's authentic Sandbox payment and matching application gate evidence, including negative/replay safety (`APP013_REMAINING_EXECUTION_CONTRACT.md:62` and the existing DATA_CONTRACTS.md payment contracts). KQ2 resolves the key prerequisite before application authentication. It stops at an inert sink and cannot complete authentication or payment.

ET1 source: `4173ec0b3b8bf3dc81d607275a427101615a4c35`; test evidence: `e20c5e28c7f23c759e3232a5886600a26a56666c`. Operator SHA256: `d178de94e373be00517f252de0cfde6e7bd5d07309100242037a528731428c71`. The exact source guard, native/qualification manifests, SDK/runtime, dependencies and dynamic configuration were checked at 2026-11-14T18:09:48.734701+00:00; the guard passed in 0.508513 seconds under its 8-second local bound. The actual scope validator passed. Current source matches the 647 passing ET1 tests; those runtime suites were not rerun for this documentation-only preparation.

Project `signmons`; existing owner `debynyhan@signmons.com`; private project-number digest pinned in scope. New operation `82ab0998-1d08-4405-91d7-3dcac62c6e67`; key `signmons-p08-82ab09981d08440591d73dcac62c6e67`; display marker `Signmons P08 82ab0998-1d08-4405-91d7-3dcac62c6e67`; only restriction `apiTargets:[{service:identitytoolkit.googleapis.com}]`.

Scope hash: `9bf8b781603709a3bc2fc5e3a31e42a1599a5c62839e23f65b8111eab65933e7`. New scope filename: `APP013_P08_KQ1_KEY_BOUNDARY_SCOPE_00000002.json`; future approval filename: `APP013_P08_KQ1_KEY_BOUNDARY_APPROVAL_00000002.json`. The existing operator retains its KQ1 action identifier. Here `00000002` is a numeric qualification revision, not a calendar date: its existing interface accepts eight digits and independently validates the exact UTC window. No code or validator was changed. Original KQ1 scope/approval/result files and their committed evidence remain unchanged; that operation is consumed and cannot be replayed. The actual approval parser accepted the new filename form and rejected a synthetic draft with external authority false; no execution hook was invoked.

## One attempt and independent cleanup, if approved

1. Recheck the exact committed decision, source, runtime, configuration, command, current time and absent operation root, then start the existing independent purge guard. Main performs two fixed owner/project CLI reads and one bounded read of the matching owner's credential cache. Credential coverage must extend past 1:45 p.m. Eastern. Any failed gate stops before key creation. No new sign-in is included.
2. Read the existing API Keys service state and exact typed key absence. Create the one restricted key only if those gates pass; allow at most five paced create-operation polls. Use the actual corrected native metadata/authentication boundary: exact resource, UID, marker, restrictions and retained creation provenance must validate; only the current etag may be atomically refreshed. Validate post-create and authentication metadata, then read keyString at most once. An inert sink records KEY_BOUNDARY_REACHED, with no account login or token issuance. Raw keyString and its in-memory hash are discarded, never persisted or printed. Diagnostic etag flags still compare against the original creation version.
3. Run independent cleanup under the same exact approval, including after main failure. If creation was not attempted, it needs no second owner/cache check. Otherwise it performs its own two owner/project CLI reads and one cache read, recovers only retained successful-create/LRO provenance, and validates the exact same UID/resource/marker/restrictions/create window. The already implemented KD boundary may adopt that proven key's freshly validated current etag for one conditional DELETE. At most five deletion polls and a reserved final authoritative metadata readback follow. This current-etag adoption is explicitly included in the requested decision. There is no unconditional deletion or mutation retry.
4. Close owned processes, purge private operation files and retain safe status, counts, match flags and ownership hash. Lost provenance, provider failure or abrupt process death can leave explicit containment UNKNOWN. Private purge alone does not prove provider/process containment. The cloud custodian owns any residual requiring a separate exact decision; this packet cannot extend itself or reset its budget.

## Limits, window and spending

Maximum **4 owner/project CLI reads, 2 credential-cache reads, 25 HTTPS requests** (11 main, 14 cleanup), **one create and one conditional delete**. Main includes service/absence/create/up to five create polls/post-create/authentication metadata/keyString. Cleanup includes up to six retained-operation recovery reads and at most eight KD requests. Cache/HTTPS requests and in-phase source checks are bounded to eight seconds; owned CLI calls to 30 seconds. The initial local source verification uses its existing per-command bounds, not the in-phase aggregate timer.

The SDK exception permits existing-owner credential refresh, internal authentication retries and cache writes only for those fixed CLI reads. Internal SDK request count is UNKNOWN. No token export, automatic operation retry, manual password input or new browser sign-in is included.

Saturday **November 14, 2026, Eastern time**:

- Launch before **1:30 p.m.**; main provider work ends **1:36 p.m.**
- Main process closure has ten seconds within the cleanup reserve.
- Cleanup mutations/polls stop **1:42:50 p.m.**; final metadata reads stop **1:43:50 p.m.**
- Owned-process cleanup ends **1:44 p.m.**; private purge ends **1:45 p.m.**
- Early completion closes immediately. Remain reachable through completion, no later than **1:45 p.m.**; no Terminal attendance is required.

The 480-second cleanup reserve retains the reviewed bound for unchanged fixed calls/pacing/source checks plus process/final-read margin. A further 60 seconds is reserved for purge. Actual requests remain gated by time and shared durable counters. Additional spending allowance is **$0**; no billing change, paid-service activation or compute deployment. This is an authorization limit, not a provider-side instantaneous billing cap.

## Readiness and finite checklist

The source-bound prerequisite record is `APP013_P08_KQ2_KEY_BOUNDARY_READINESS_20261114.json`. Its source/configuration/actual-command and negative-authority checks are current local evidence. ET1's 647-test verification covers actual parsing/serialization, missing/null values, precise creation-time/ownership/restrictions checks, conditional races, no retries, concurrency, interruption, recovery, private retention and independent cleanup. Independent runtime review found no additional locally discoverable prerequisite. Independent final packet review and documentation checks are recorded in that readiness file before approval is requested.

Current credentials, API availability, effective create/read/delete permissions and usable keyString behavior remain **UNKNOWN**; resolving them within the bounded lifecycle is the purpose of this qualification. Metadata alone is not proof of usable access. If credential coverage fails, stop and close; any later renewal requires a separately prepared sign-in decision.

Preparation checklist: preserve old KQ1 evidence; bind new operation/source/resources/window; verify actual source/configuration/scope/command interfaces; reconcile exact-byte test evidence; obtain independent review and required checks. Execution checklist, still pending: exact owner approval and availability; one live qualification; independent containment and private/process closeout; immutable safe result and handoff. Implementer owns preparation/supervision/evidence; owner and credential/cloud custodian own external authority and any unresolved containment.

No external SQL/Neon, account authentication, Handoff, runtime deployment, IAM/secret changes, Stripe, real charge, refund, booking or customer contact is authorized. No rollback of a deployed application is involved; before approval the path remains disabled. After approval the only authorized containment mutation is conditional deletion of this one proven temporary key, with UNKNOWN retained if it cannot be proved.

## Actual command and decision

After exact approval is recorded in a new governance commit, only the commit placeholder is replaced. The scope and approval filenames are fixed. The actual CLI refuses missing, uncommitted, mismatched or false authority. Preparation does not invoke this command.

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B -c 'import runpy,sys;path=sys.argv.pop(1);sys.path.insert(0,sys.argv.pop(1));sys.argv[0]=path;runpy.run_path(path,run_name="__main__")' '/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery/evidence/APP-013/p08-connected-packet-20261110/kq1_key_boundary.py' '/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery/evidence/APP-013/p08-connected-packet-20261110' --run '<FULL_GOVERNANCE_APPROVAL_COMMIT>' APP013_P08_KQ1_KEY_BOUNDARY_SCOPE_00000002.json APP013_P08_KQ1_KEY_BOUNDARY_APPROVAL_00000002.json
```

The independent cleanup and local purge command vectors are recorded in readiness for the same exact committed decision. No separate replay authority follows from them. Before launch, compare actual command/source/resources/configuration/authority/time against this record; any mismatch blocks launch.

Decision requested: approve KQ2's one restricted-key create/keyString qualification, validated current-etag handling, same-UID conditional removal, bounded SDK/cache exception, spending limits and independent cleanup/private purge; remain reachable through completion by 1:45 p.m. No Terminal confirmation or password is required.

Next observable result: KEY_BOUNDARY_REACHED or one safe key-stage failure, followed by authoritative key status and safe closeout/residuals. This is not authentication proof or payment acceptance. Accepted 1A/1B/2A/2B remain **4/8**; **3A OPEN**; R1 newly closed **0/27**. **No scope deviation.**
