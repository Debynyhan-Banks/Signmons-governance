# APP-013 / 3A / P08 — KQ3 corrected key-only qualification

Prepared, not approved. This is one new qualification using the completed ET1 correction. For KQ3, no operation root, credential read, provider call, sign-in or timed password prompt has started. TR19 successfully verified owner credential coverage beyond 2:15 p.m. and independently closed. Its approval authorized sign-in, not the key actions below. Owner reachability through 2:20 p.m. is already confirmed.

## Purpose, source and exact resources

Section 3A still requires the admitted job's authentic Sandbox payment and matching application gate evidence, including negative/replay safety (`APP013_REMAINING_EXECUTION_CONTRACT.md:62` and the existing DATA_CONTRACTS.md payment contracts). KQ3 resolves the key prerequisite before application authentication. It stops at an inert sink and cannot complete authentication or payment.

Current source including ET1 and TR19 evidence: `d2acad66cf6b9b7006b4b5867c92e9b3b194375b`; test evidence: `e20c5e28c7f23c759e3232a5886600a26a56666c`. Operator SHA256: `d178de94e373be00517f252de0cfde6e7bd5d07309100242037a528731428c71`. The exact source guard, native/qualification manifests, SDK/runtime, dependencies and dynamic configuration were checked at 2026-11-14T18:32:44.382257+00:00; the guard passed in 0.537921 seconds under its 8-second local bound. The actual scope validator passed. Current source matches the 647 passing ET1 tests; those runtime suites were not rerun for this documentation-only preparation.

Project `signmons`; existing owner `debynyhan@signmons.com`; private project-number digest pinned in scope. New operation `8be45e96-ac92-4b7a-86fe-0739366f619c`; key `signmons-p08-8be45e96ac924b7a86fe0739366f619c`; display marker `Signmons P08 8be45e96-ac92-4b7a-86fe-0739366f619c`; only restriction `apiTargets:[{service:identitytoolkit.googleapis.com}]`.

Scope hash: `0b2f616b40acdb9a30ccbfd72a38839d0439e258598dc9cdee1f01fae5eeda26`. New scope filename: `APP013_P08_KQ1_KEY_BOUNDARY_SCOPE_00000003.json`; future approval filename: `APP013_P08_KQ1_KEY_BOUNDARY_APPROVAL_00000003.json`. The existing operator retains its KQ1 action identifier. Here `00000003` is a numeric qualification revision, not a calendar date: its existing interface accepts eight digits and independently validates the exact UTC window. No code or validator was changed. Original KQ1 and KQ2 scope/approval/result files and their committed evidence remain unchanged; both operations are consumed and cannot be replayed. KQ2 preparation verified this unchanged numeric-revision filename interface through the actual approval parser, including refusal of false external authority. KQ3 uses revision 3; no execution hook was invoked during preparation.

## One attempt and independent cleanup, if approved

1. Recheck the exact committed decision, source, runtime, configuration, command, current time and absent operation root, then start the existing independent purge guard. Main performs two fixed owner/project CLI reads and one bounded read of the matching owner's credential cache. Credential coverage must extend past 2:05 p.m. Eastern. Any failed gate stops before key creation. No new sign-in is included.
2. Read the existing API Keys service state and exact typed key absence. Create the one restricted key only if those gates pass; allow at most five paced create-operation polls. Use the actual corrected native metadata/authentication boundary: exact resource, UID, marker, restrictions and retained creation provenance must validate; only the current etag may be atomically refreshed. Validate post-create and authentication metadata, then read keyString at most once. An inert sink records KEY_BOUNDARY_REACHED, with no account login or token issuance. Raw keyString and its in-memory hash are discarded, never persisted or printed. Diagnostic etag flags still compare against the original creation version.
3. Run independent cleanup under the same exact approval, including after main failure. If creation was not attempted, it needs no second owner/cache check. Otherwise it performs its own two owner/project CLI reads and one cache read, recovers only retained successful-create/LRO provenance, and validates the exact same UID/resource/marker/restrictions/create window. The already implemented KD boundary may adopt that proven key's freshly validated current etag for one conditional DELETE. At most five deletion polls and a reserved final authoritative metadata readback follow. This current-etag adoption is explicitly included in the requested decision. There is no unconditional deletion or mutation retry.
4. Close owned processes, purge private operation files and retain safe status, counts, match flags and ownership hash. Lost provenance, provider failure or abrupt process death can leave explicit containment UNKNOWN. Private purge alone does not prove provider/process containment. The cloud custodian owns any residual requiring a separate exact decision; this packet cannot extend itself or reset its budget.

## Limits, window and spending

Maximum **4 owner/project CLI reads, 2 credential-cache reads, 25 HTTPS requests** (11 main, 14 cleanup), **one create and one conditional delete**. Main includes service/absence/create/up to five create polls/post-create/authentication metadata/keyString. Cleanup includes up to six retained-operation recovery reads and at most eight KD requests. Cache/HTTPS requests and in-phase source checks are bounded to eight seconds; owned CLI calls to 30 seconds. The initial local source verification uses its existing per-command bounds, not the in-phase aggregate timer.

The SDK exception permits existing-owner credential refresh, internal authentication retries and cache writes only for those fixed CLI reads. Internal SDK request count is UNKNOWN. No token export, automatic operation retry, manual password input or new browser sign-in is included.

Saturday **November 14, 2026, Eastern time**:

- Launch before **1:50 p.m.**; main provider work ends **1:56 p.m.**
- Main process closure has ten seconds within the cleanup reserve.
- Cleanup mutations/polls stop **2:02:50 p.m.**; final metadata reads stop **2:03:50 p.m.**
- Owned-process cleanup ends **2:04 p.m.**; private purge ends **2:05 p.m.**
- Early completion closes immediately. Your confirmed reachability through 2:20 p.m. covers completion by **2:05 p.m.**; no Terminal attendance is required.

The 480-second cleanup reserve retains the reviewed bound for unchanged fixed calls/pacing/source checks plus process/final-read margin. A further 60 seconds is reserved for purge. Actual requests remain gated by time and shared durable counters. Additional spending allowance is **$0**; no billing change, paid-service activation or compute deployment. This is an authorization limit, not a provider-side instantaneous billing cap.

## Readiness and finite checklist

The source-bound prerequisite record is `APP013_P08_KQ3_KEY_BOUNDARY_READINESS_20261114.json`. Its source/configuration/actual-command checks are current local evidence. The unchanged approval parser's false-authority refusal was verified during KQ2 preparation and is retained as historical interface evidence. ET1's 647-test verification covers actual parsing/serialization, missing/null values, precise creation-time/ownership/restrictions checks, conditional races, no retries, concurrency, interruption, recovery, private retention and independent cleanup. Independent runtime review found no additional locally discoverable prerequisite. Independent final packet review and documentation checks are recorded in that readiness file before approval is requested.

TR19 observed credential validity beyond **2:15 p.m.** at 1:30:14 p.m.; its process/configuration/receipt closeout was independently verified and committed at `d2acad6`. KQ3 private purge by 2:05 p.m. fits that observed horizon. The included phase owner/project/cache checks still gate all key work. API availability, effective create/read/delete permissions and usable keyString behavior remain **UNKNOWN**; these are qualification targets. Metadata alone is not proof of usable access. KQ2 stopped before any key-API request; renewal does not prove its historical cause or guarantee this attempt. If a credential gate fails, stop and close without retry.

Preparation checklist: preserve old KQ1 evidence; bind new operation/source/resources/window; verify actual source/configuration/scope/command interfaces; reconcile exact-byte test evidence; obtain independent review and required checks. Execution checklist, still pending: exact owner approval (attendance already confirmed); one live qualification; independent containment and private/process closeout; immutable safe result and handoff. Implementer owns preparation/supervision/evidence; owner and credential/cloud custodian own external authority and any unresolved containment.

No external SQL/Neon, account authentication, Handoff, runtime deployment, IAM/secret changes, Stripe, real charge, refund, booking or customer contact is authorized. No rollback of a deployed application is involved; before approval the path remains disabled. After approval the only authorized containment mutation is conditional deletion of this one proven temporary key, with UNKNOWN retained if it cannot be proved.

## Actual command and decision

After exact approval is recorded in a new governance commit, only the commit placeholder is replaced. The scope and approval filenames are fixed. The actual CLI refuses missing, uncommitted, mismatched or false authority. Preparation does not invoke this command.

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B -c 'import runpy,sys;path=sys.argv.pop(1);sys.path.insert(0,sys.argv.pop(1));sys.argv[0]=path;runpy.run_path(path,run_name="__main__")' '/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery/evidence/APP-013/p08-connected-packet-20261110/kq1_key_boundary.py' '/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery/evidence/APP-013/p08-connected-packet-20261110' --run '<FULL_GOVERNANCE_APPROVAL_COMMIT>' APP013_P08_KQ1_KEY_BOUNDARY_SCOPE_00000003.json APP013_P08_KQ1_KEY_BOUNDARY_APPROVAL_00000003.json
```

The independent cleanup and local purge command vectors are recorded in readiness for the same exact committed decision. No separate replay authority follows from them. Before launch, compare actual command/source/resources/configuration/authority/time against this record; any mismatch blocks launch.

Decision requested: approve KQ3's one restricted-key create/keyString qualification, validated current-etag handling, same-UID conditional removal, bounded SDK/cache exception, spending limits and independent cleanup/private purge; retain the already-confirmed reachability through completion by 2:05 p.m. No Terminal confirmation or password is required.

Next observable result: KEY_BOUNDARY_REACHED or one safe key-stage failure, followed by authoritative key status and safe closeout/residuals. This is not authentication proof or payment acceptance. Accepted 1A/1B/2A/2B remain **4/8**; **3A OPEN**; R1 newly closed **0/27**. **No scope deviation.**
