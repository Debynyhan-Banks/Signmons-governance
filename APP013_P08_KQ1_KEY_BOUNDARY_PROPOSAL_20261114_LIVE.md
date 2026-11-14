# APP-013 / 3A / P08 — KQ1 exact key-only qualification

Prepared, not approved. This packet is qualification-only. Local implementation approval63c342b9 does not authorize its provider or credential actions. No attempt root, provider call, credential read, sign-in or timed prompt has started.

## Purpose and pins

Section3A's same-job Sandbox payment criterion is unchanged (APP013_REMAINING_EXECUTION_CONTRACT.md section3A and existing DATA_CONTRACTS.md PaymentPolicy/payment-state contracts). KQ1 tests the temporary Google API-key boundary needed before application authentication. It does not run authentication or Stripe payment.

Source `a26065ed7ae497733ded4d7ea93fa52f930193b2`; operator SHA256 `979ff9343c3ca994f70610bcf10e995cef415980141983bc40d6be953905c9e7`. Existing native/qualification/SDK files and packet/KS/KD dependencies are pinned in the scope. Current source guard passed in0.590s without credentials or provider reads. Scope hash `b468db73640603e85bf1d97ad782cb4b9292643ec1b111bb917eccd9003582d1`.

Project `signmons`, existing owner `debynyhan@signmons.com`; exact private project-number digest remains pinned in scope. Operation `eed61968-8014-481c-9750-69e1953b1353`; key `signmons-p08-eed619688014481c975069e1953b1353`; display marker `Signmons P08 eed61968-8014-481c-9750-69e1953b1353`. Only restriction `apiTargets:[{service:identitytoolkit.googleapis.com}]` is permitted. This is a new operation, not a replay of R46 or KD3.

## One authorized attempt, if approved

1. Verify exact committed decision/source/runtime/configuration and start the independent purge guard. In the main phase, make the two fixed owner/project CLI reads and one bounded read of the matching owner's credential cache. Cache coverage must extend beyond1:00p.m.; failure stops before key creation. No browser sign-in is included.
2. Read existing API Keys service state and exact typed key absence. If qualified, create this one restricted key, process at most five paced create-operation polls, validate post-create metadata and the unchanged authenticate UID/etag checks, and read keyString at most once. The injected sink records KEY_BOUNDARY_REACHED without an account/authentication call. Raw keyString and its in-memory hash are discarded, not logged or persisted.
3. Start an independent cleanup process under the same authority. If creation was never attempted, no second owner/cache read is needed. Otherwise its own two owner/project reads and one cache read must qualify current identity/coverage. Recover only retained successful-create/LRO provenance. Fresh exact resource, UID, display marker, restrictions and create-window checks may adopt that proven UID's current etag for one conditional DELETE. This prospective adoption is explicitly part of the requested decision; it does not weaken the main native etag check. Poll at most five times and attempt final authoritative metadata readback after uncertain deletion.
4. Close owned processes, remove private operation files and retain only safe diagnostics/counts/match flags/ownership hash. No create/delete retry, scope extension or second credential-cache allowance is available. Lost create provenance, provider failure or abrupt process death can leave explicit containment UNKNOWN. Private purge does not prove process/provider containment; cloud custodian owns any residual requiring a new exact decision.

## Exact limits, timing and spending

Maximum4 owner/project CLI reads,2 credential-cache reads,25 HTTPS requests (main11, independent cleanup14),1 create POST,1 conditional DELETE. Main includes service/absence/create/up to5polls/post-create/authenticate-metadata/keyString. Cleanup includes up to6 retained-operation recovery GETs and at most8 KD requests. SDK existing-owner refresh, internal authentication retries and credential-cache writes are excepted only for these fixed CLI reads; internal SDK request count is UNKNOWN. No exported tokens, manual password input or automatic operation/mutation retry.

Saturday November14,2026, Eastern time:

- Launch must begin before12:45p.m.; main provider work ends12:51p.m.
- Main process closure has10seconds within the cleanup reserve.
- Cleanup mutations/polls stop12:57:50p.m.; its reserved final-read period ends12:58:50p.m.
- Owned-process cleanup ends12:59p.m.; original-root private purge ends1:00p.m.
- An early completed run closes immediately; no waiting until the deadline is required. The owner should remain reachable through completion, no later than1:00p.m.

The480second cleanup reserve includes worst-case fixed-call/poll/source checks and process/final-read margin. HTTPS/cache requests and in-phase source checks are bounded to8seconds; owned CLI calls to30seconds. Initial local source verification has per-command bounds and is not covered by that aggregate8second phase timer. Time and shared durable counters gate actual requests. No new spending allowance: `$0` additional allowance, no billing change, paid-service activation or compute deployment. This is a permission limit, not a provider-side instantaneous billing cap.

## Readiness and finite checklist

| Prerequisite | Source/evidence and timestamp | Verification / owner |
| --- | --- | --- |
| Source, command, SDK/runtime/configuration, private project pin | Actual source_guard/validate_scope and operator command builder; current readiness JSON at2026-11-14T17:32:26.767778+00:00 | Local PASS; implementer. Root absent, no reservation. |
| Output serialization, parsing, error masking, keyString sink and HTTP closure | Unchanged sourcea26065e;44 focused tests included136 connected, plus104 native and25 governance, verification402ee6a | Historical local PASS matched to current exact bytes, not newly rerun or live evidence; implementer. |
| Durable budgets, concurrency, interruption, separate cleanup, original-root purge, clock/process bounds | Actual KQ1 journal/guard/owned-process interfaces and corresponding tests; local completion card | Local PASS; conservative480s cleanup reserve selected after independent review; implementer. |
| Credential validity, API availability, effective create/read/delete access, actual key behavior | Proposed pre-create owner/project/cache/service gates and one key lifecycle | Current UNKNOWN; legitimate purpose of qualification. No separate sign-in is inferred. Owner/credential and cloud custodian. |
| External authority and availability | Exact decision draft and this packet | PENDING. Owner must approve creation/keyString/current-etag cleanup, SDK/cache exception, limits and availability. |
| Result and closeout | Future safe result plus exact-root inventory/process observation | NOT EXECUTED. Implementer supervises; cloud custodian owns unresolved containment. |

Preparation checklist: exact source/scope/resource/window bound; current local source/configuration/command check complete; unchanged test evidence reconciled; independent review and documentation checks recorded in readiness JSON. Remaining: explicit owner decision, bounded live qualification, authoritative containment, independent local closeout and evidence reconciliation. No SQL/Neon, account login/token issuance, Handoff, runtime/IAM/secret changes, browser, Stripe, charge, refund, booking or customer contact is authorized.

## Command and decision

After exact owner approval is recorded in a new governance commit, replace only the approval-commit placeholder below with that full commit. The scope and approval filenames are fixed. The actual CLI refuses a missing/wrong/uncommitted decision. Preparation never invokes this command.

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B -c 'import runpy,sys;path=sys.argv.pop(1);sys.path.insert(0,sys.argv.pop(1));sys.argv[0]=path;runpy.run_path(path,run_name="__main__")' '/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery/evidence/APP-013/p08-connected-packet-20261110/kq1_key_boundary.py' '/Users/debynyhanbanks/Web Projects/signmons-backend-r08-recovery/evidence/APP-013/p08-connected-packet-20261110' --run '<FULL_GOVERNANCE_APPROVAL_COMMIT>' APP013_P08_KQ1_KEY_BOUNDARY_SCOPE_20261114.json APP013_P08_KQ1_KEY_BOUNDARY_APPROVAL_20261114.json
```

Independent `--cleanup` and local-only `--purge` command vectors are recorded in readiness JSON for the same exact scope/decision; neither resets budgets or authorizes replay. Before launch, compare the actual command, source, scope hash, configuration snapshot, root absence and current time with this readiness record. Any mismatch blocks launch.

Decision requested: approve KQ1's exact new-key create/keyString qualification, prospective same-UID current-etag conditional deletion, bounded cache/SDK exception, stated spending limits and independent cleanup/private purge; remain reachable through completion by1:00p.m. No separate Terminal confirmation or Neon password is required. If credential coverage fails, record that stop and close; any later sign-in needs a separate exact proposal.

Next observable result: KEY_BOUNDARY_REACHED or a safe specific key-stage failure, followed by authoritative key status and safe closeout/residuals. This is not AUTH_PROOF, payment acceptance or3A completion. Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1 newlyclosed0/27. No scope deviation.
