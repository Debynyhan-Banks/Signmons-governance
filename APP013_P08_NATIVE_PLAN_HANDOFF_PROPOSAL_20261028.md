# APP-013 / 3A / P08 — native private-plan handoff correction proposal

Status: PROPOSED; owner decision pending. R1-W01 / APP-013 / 3A / P08. Current approved operation document commit `4496069308e3bbc8c3f2f3205c3e4de5c6255a95`; backend source `d5aa8f93b4e4a7a2a320a4637871403e73f4955a`. Local correction and isolated-test authority only if approved. No credential/cache access, gcloud, provider request/change, private plan, API/IAM/key, database/account/runtime, Stripe/payment, deployment or spending is included.

## Demonstrated gap and stop

Final pre-execution source inspection found the deterministic builder's native entry point always returns `P08_PLAN_BUILDER_REFUSED_UNBOUND`. Its tested `build()` interface requires an already-known private project number. No retained private project-number input exists; prior private plans were correctly purged. The native launcher independently issues the approved three commands for owner, project and bearer.

Obtaining the project number with an extra command before invoking the native launcher would make four commands, exceeding the approved maximum three. Supplying unpinned scratch glue or scanning credential caches would bypass the approved source/hash contract. Therefore the approved 5:30 operation is not executable from its pinned source. No private plan, credentials, command or external request has occurred. The operation remains approved but unstarted; it must not be attempted unless a corrected, separately approved source/document replaces it.

This is an implementer preparation gap, not a Google/provider/payment result. Stage A, Stage B and 3A acceptance remain open.

## Alternatives and recommendation

1. **Recommended: add one source-locked native coordinator that reuses the same owner/project read for plan construction and launcher qualification.** It performs exactly three actual commands total: owner, project and bearer.
2. Issue an extra project command before the current launcher. Refused because it exceeds the exact approved command ceiling.
3. Use unpinned scratch code or scan local credential caches. Refused because it breaks source/approval/privacy traceability.
4. Wait and redesign later. Safe but needlessly delays Stage A.

## Exact local implementation card

In a fresh disabled evidence directory copied from backend `d5aa8f9`:

- add a native coordinator in the existing source-locked launcher/builder boundary;
- read current owner and exact project once through the existing `NativeCLI` allowlist before creating private output;
- validate project ID/number shape and canonical fingerprint in memory;
- build the exact committed approved document into one private plan;
- pass a cache-once CLI wrapper to the unchanged `execute()` path so owner/project qualification consumes the just-read outputs and only the bearer command reaches the native CLI afterward;
- prove exactly three actual CLI calls total and zero duplicate project read;
- never save or print the raw project number outside the private `0600` plan; purge that plan in `finally` with absence readback;
- preserve exact Git document SHA, operation/decision/source/window/retention/no-retry gates, deadlines, signals, child cleanup and sanitized result;
- refuse owner/project mismatch, malformed output, cache reuse, builder failure, launch refusal, result-write failure, purge failure and any fourth command truthfully;
- keep native execution disabled unless a committed approved exact operation binds the corrected source.

Run positive, negative, signal, timeout, race, cleanup and actual serialized-command tests plus all 186 current regressions, architecture, baseline, consistency, safeguards and whitespace. Native must remain unbound without an exact approved operation.

Observable finish is a source-locked tested three-command document-to-plan-to-launch handoff. It remains local only. A new exact same-day operation document/source pin and separate external approval are required. That future approval supersedes/cancels both current unstarted operations.

Excluded: provider access or mutation, credentials/cache, private plan, changing Stage A requests/retention/allowance, API Keys, IAM roles/grants, Firebase/database/runtime, Stripe/payment, deployment, merge/push or spending.

Accepted 1A/1B/2A/2B, 4/8 walkthrough; 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. **Unintended native handoff gap disclosed before credentials; explicit local correction proposed before implementation.**

## Owner decision

Debynyhan Banks replied “i approve” to the bounded native plan-handoff correction and local tests against governance commit `eb7da758cb9af322769b73e2c8e8bb0f20487587`. This authorizes only the disabled local source/test work above. It does not authorize credentials, a private live plan, provider commands/requests, cancellation or execution of an operation.

## Implemented local result

Backend `03fccb41f6f40dd77b966b6d76764ec0bd3d8448` completes the source-locked coordinator. PASS: 16 builder/coordinator, 18 launcher, 24 Stage A, 40 access-model, 31 restoration and 60 authentication tests, 189 total. Exactly three actual CLI calls, cache one-use, preflight closeout, full fake diagnostic path, private-plan purge, manifests, architecture, baseline and scratch absence passed. Two initial new-test failures corrected fake response shape and the legacy no-coordinator assertion without adding direct subprocess/HTTP code or weakening authority.

Exact corrected operation `APP013_P08_STAGE_A_OPERATION_20261028_R02.md` is proposed for 5:30–6:00 p.m. Eastern with a strict 5:45 cutoff. Separate approval is required and will supersede/cancel both older unstarted authorities. **No scope deviation within the owner-approved local correction.**
