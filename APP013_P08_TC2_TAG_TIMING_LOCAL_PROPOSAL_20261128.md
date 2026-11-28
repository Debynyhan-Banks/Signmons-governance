# TC2 — local synchronous-tag timing correction

**Prepared for owner decision; not implemented or externally authorized.** APP-013 / 3A / P08. Source `ee98bc4891605ad8e96632f15553a7bafc50a4d3`; inspected 2026-11-28T13:10:57.168434+00:00. R69 is consumed. No further Terminal attendance is required for this local work.

## Traceability and demonstrated gap

The frozen 3A exit criterion requires the owner’s Sandbox payment on the same admitted job and a matching signed event that clears its payment gate. Protected-job authentication is an existing prerequisite. TC2 repairs the existing temporary runtime tag command needed to reach that authentication path; it introduces no section, payment stack, resource or acceptance criterion. DATA_CONTRACTS.md’s approved payment policy/job binding and tenant/identity boundaries remain unchanged.

R69 passed all nine current prerequisite checks but stopped before authentication with `RUNTIME_TAG_COMMAND_TIMEOUT`. Its final result is `ENTRY_CONTAINMENT_UNCONFIRMED`, with the sole retained label `RUNTIME:tag:app013-p07-atomic`. `APP013_P08_R69_CLOSEOUT_REVIEW_20261128.json` binds the receipts: private inputs purged on time, all 185 recorded child groups absent, native parent and purge guardian absent, Terminal idle, exact owned launch files absent. No authentication, key creation, signing-role binding or payment was attempted. The retained tag label is historical forward uncertainty; there are no new cleanup-readback failure labels. This does not authorize clearing the UNKNOWN or claiming complete provider restoration.

The current synchronous command lacks `--async`. Installed SDK `update_traffic.py` calls `UpdateTraffic`; it gets/replaces the service and waits for Ready when necessary. The pinned `serverless_operations.py:771–788` can select `WaitService`, whose operation poller requests `timeout='10s'` (`op_pollers.py:465–474`). SDK polling defaults to a much larger overall wait. Current AQ1 `native_io.py:97–100,351–399` gives every CLI command 8 seconds total, including up to 2 seconds for owned-group reaping: at most 6 seconds for startup, API work, synchronous completion waiting and output.

This proves that a permitted single provider wait can exceed the local execution allowance. It does **not** prove which internal stage R69 reached or whether its update was accepted before timeout. Newly inspected SDK files below were not historical pins; do not retroactively claim their bytes were verified at R69 launch.

## Proposed correction and alternatives

Use **30 seconds total** only for AQ1’s exact validated forward and removal tag command vectors, including the existing 2-second reap reserve. This is up to 28 seconds for execution/output, always clamped to the earlier existing phase deadline. It accommodates a 10-second wait plus bounded startup/request/output allowance, but is a policy-selected attempt ceiling, not a provider-latency guarantee. Every other command, SQL path and non-AQ1 purpose retains its existing 8-second treatment.

Keep the command synchronous, its JSON traffic-pair output contract, safe error classifications, readback predicates, requests, mutation counts and no-retry rules. Adding `--async` alone is rejected: the SDK’s async path does not return the same traffic-pair resource and would require a larger acknowledgment/readiness contract change. Another full run under the current six-second execution ceiling is also rejected.

The corresponding AQ1 tag-removal cleanup reservation must be **at least 38 seconds** before persisting intent: 30 for the command plus the existing 8-second readback. Override the existing native `entry.Coordinator.cleanup_mutation` seam only when the purpose is AQ1 and the label exactly equals `RUNTIME:tag:` plus the validated restore module’s TAG. Delegate once to the unchanged base implementation with `max(seconds, 38)`; all other labels/purposes pass through. The base coordinator, positive no-dispatch provenance, consumed mutation markers and independent-attempt rules stay unchanged. Transport matching independently requires complete exact forward/removal vectors, including the dynamically selected candidate.

## Exact local surface and reuse

Only these four existing source/test files may change:

| File relative to backend | Inspected SHA256 |
| --- | --- |
| `evidence/APP-013/p08-native-entry-local-20261101/source/native_io.py` | `7e015a9cc5ff9967b75479df13b1ea6de6b42f983a2f51cfd68da374ad134ed8` |
| `evidence/APP-013/p08-native-entry-local-20261101/source/entry.py` | `e8d17b3e0acafd5fbe5a45b2aea4b448c23b7424907f67ee66bcf7e0920deb77` |
| `evidence/APP-013/p08-native-entry-local-20261101/source/test_child_cleanup.py` | `094324bd5a512f05685c7a4edee1bbfb753d3a10ca6281f7e452c664f9b56a6e` |
| `evidence/APP-013/p08-native-entry-local-20261101/source/test_entry.py` | `74fdf63c00f43589c0a09e0f8de86b7286e3ed3d8678a8acbc67d8d6949bb575` |

Reuse `_run`/`_owned_process`, owned child inventory, monotonic/phase clamps, `entry.Coordinator`’s existing cleanup hooks, `TC1OwnershipTests`, `ChildCleanupTests`, `TC1TimingTests` and `TC1OwnedJournalTests`. Preserve the historical TagMutationDiagnosticTests compatibility oracle and safe error labels. No base-coordinator, command-vector, success-predicate, SQL, application/payment or SDK change is needed.

Exactly eight current derived manifests may receive mechanical hashes; source-guard algorithms, frozen anchors and historical manifests must not change:

- `evidence/APP-013/p08-native-entry-local-20261101/source/source-manifest.json`
- `evidence/APP-013/p08-native-entry-local-20261101/source/test-manifest.json`
- `evidence/APP-013/p08-key-correction-20261110/source-manifest.json`
- `evidence/APP-013/p08-connected-packet-20261110/iq1-source-manifest.json`
- `evidence/APP-013/p08-connected-packet-20261110/sq1-source-manifest.json`
- `evidence/APP-013/p08-connected-packet-20261110/vm2-source-manifest.json`
- `evidence/APP-013/p08-connected-packet-20261110/account-containment-source-manifest.json`
- `evidence/APP-013/p08-connected-packet-20261110/account-containment-read-source-manifest.json`

Governance scope is this decision/completion evidence and concise current updates in the pointer, board, handoff and APP-013 ticket. Unrelated AGENTS.md changes and historical files remain preserved.

## Timing, state and retention boundaries

- Setup adds at most 22 seconds for one forward tag command. The earlier approximately 606-second subtotal becomes 628; with 120 seconds for input and 14 seconds for the full identity interval, approximately 762 seconds fits the existing 780-second attempt cap with roughly 18 seconds left for other local overhead. This is not an all-latency success guarantee.
- The one permitted tag removal adds at most 22 seconds in main **or** independent cleanup, never a mutation retry in both. Completed-main independent readback bounds do not gain a second removal. Partial-main worst-case cleanup already exceeds the 660-second horizon and can increase by 22 seconds; retain that explicit limitation.
- Keep 780-second setup, 420-second IAM settling, 600-second post-settle admission, 660-second independent interval, 120-second purge reserve, fixed one-hour custody and current call ceilings unchanged. Existing larger cleanup maxima remain a reason to label a future run qualification-only.
- Admission before intent, second gate, actual process clamp, complete owned-child closure, parent exit and independent first-dispatch provenance remain mandatory. A deadline interruption retains UNKNOWN where required; this amendment does not clear R69’s uncertainty.
- No new private fields, raw provider payloads, logs, credentials, token retention, inputs or resource identities. The existing token/job/tenant/payment binding and purge rules remain.

## Finite checklist and verification

Completed before implementation: current source/evidence inspection; two independent timing/seam reviews; exact four-file/eight-manifest dependency inventory; owner acceptance trace; SDK output/wait contract review; local closure verification. Implementation remains pending this decision.

After approval:

1. Add the exact-vector AQ1 tag allowance and paired pre-intent cleanup reservation in the existing seams. Do not weaken a guard to accommodate an incomplete test fixture.
2. Verify forward/removal selection, ordinary-purpose and unrelated/foreign-vector negatives, and earlier work/cleanup deadline clamping. Prove one harmless process delayed for 10 seconds can finish through the actual `_run` → `_owned_process` path, with only Popen redirected to local Python, no provider command. Record one spawn, closed descendants and an unrelated surviving sentinel.
3. Verify timeouts/interruption/held pipes/output limits still close owned groups and preserve the original failure. Test the 37/38-second cleanup admission boundary before intent/action, main and independent modes, elapsed-time races, foreign tag/identity/IAM labels, no automatic retry and consumed independent grants.
4. Run the inspected selected suites below; no broad test discovery, PostgreSQL fixture, real SQL, browser or provider access. Tests may use harmless local processes only. Preserve the existing concurrent-entry and ordinary-purpose regressions.
5. Update only the eight current manifests, verify current/committed source guards, and independently inspect the final diff and process evidence. Run required governance, architecture and whitespace checks. Record implemented/local-tested/live-demonstrated/owner-accepted states separately.

From backend, using the existing pinned Python and local test imports:

```sh
/opt/homebrew/Cellar/python@3.14/3.14.2/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -I -B -c 'import sys,unittest;sys.path.insert(0,sys.argv.pop(1));unittest.main(module=None)' evidence/APP-013/p08-native-entry-local-20261101/source test_child_cleanup test_entry.TagMutationDiagnosticTests test_entry.TC1TimingTests test_entry.TC1OwnedJournalTests -v
```

Reused classes currently contain 58 tests before additions. Inspect any new or changed fixture before execution; never select the full test_entry module. Browser and database integration checks are excluded because this amendment changes neither interface and must remain local. Full customer-workflow/browser evidence still belongs to later 3A acceptance.

Required checks: backend `SIGNMONS_GOVERNANCE_REPO=<G> node scripts/check-governance-baseline.mjs`, `node scripts/architecture-check.mjs`; governance `node scripts/frozen-baseline-check.mjs`, `SIGNMONS_BACKEND_REPO=<B> node scripts/docs-consistency-check.mjs`, and the three required governance test files; `git diff --check` in both repositories. Reuse the existing native source/committed guards, not a rewritten expectation. No tests for TC2 are claimed run yet.

## Readiness evidence and unresolved facts

| Prerequisite | Source/evidence and result | Responsible owner |
| --- | --- | --- |
| Exact failure boundary | R69 closeout receipt and native_io forward-vector classifier: PASS; internal provider stage UNKNOWN | Implementer |
| Real SDK synchronous response/wait | Source inspected at the timestamp above; 10-second wait and traffic-pair output confirmed | Implementer |
| Dynamic resource/configuration pins | Existing complete `restore.command` vectors and exact TAG label reused; no pin/SDK change | Implementer |
| Time/cleanup/concurrency/retention | Existing owned-process and cleanup seams inspected; new behavior awaits tests | Implementer |
| Current provider/authentication | R69 prerequisite observation retained historically; present authentication and forward tag outcome UNKNOWN | External approval remains owner-controlled |
| Implementation authority | This proposal has no authority until the owner explicitly approves | Debynyhan Banks |

SDK paths are relative to `/opt/homebrew/Caskroom/gcloud-cli/583.0.0/google-cloud-sdk`:

| File | Evidence class | SHA256 |
| --- | --- | --- |
| `lib/googlecloudsdk/command_lib/run/serverless_operations.py` | Existing qualification-manifest pin | `b7ca29dcc6eb77739965267323e842da3d55c76f28b65cf4f9baefc1d02ada02` |
| `lib/surface/run/services/update_traffic.py` | Current local inspection; not a historical R69 pin | `15a39927e0225c44cb228a27cac314630ba0b87a12243bac1a6935fc973cec33` |
| `lib/googlecloudsdk/command_lib/run/op_pollers.py` | Current local inspection; not a historical R69 pin | `f60ee9f0553fcbe813566cdca56e10a9c3c0cadf20f7330bc298cc720a40dd2f` |
| `lib/googlecloudsdk/api_lib/util/waiter.py` | Current local inspection; not a historical R69 pin | `3b3aae3276b7ae1fd9a34965273cf73d58a469a1d0eaf6a58363e8bd0289fec6` |
| `lib/googlecloudsdk/command_lib/run/flags.py` | Current local inspection; not a historical R69 pin | `6fd29176137f91e862d1d390786c1a09fd4fb1ec330ac6138db605e3d2a553ac` |

Future launch preparation must recheck the then-current SDK/source/configuration and actual timing, using existing blocking interfaces. This review makes no new automated-enforcement claim and authorizes no future sign-in, tag mutation, credential read or live qualification. A future provider observation, if needed, requires its own concrete bounded review; do not start another attended workflow to guess the consumed cause.

## Finish, rollback and decision

Observable local finish: both exact synchronous tag commands can survive a legitimate 10-second wait under their reviewed allowance; short remaining phases refuse/close safely; cleanup intent waits for its full reservation; unrelated purposes retain prior behavior; source guards and selected checks pass. This is a local transport/timing fix, not completed authentication or 3A acceptance.

Rollback is restoration of these local files and mechanical current pins from the recorded source; there is no provider rollback because this amendment authorizes no external action. Baseline failure stops work. Dependencies, section count, accepted 1A/1B/2A/2B and the remaining 3A → 3B → 3C → 3D order stay unchanged. Accepted 4/8; 3A OPEN; R1 newly closed 0/27.

**Requested decision: approve TC2 local tag timing correction and the listed synthetic/process tests.** No attendance or deadline is required. This increases one command’s allowance beyond TC1’s existing 8-second treatment, so AGENTS.md’s “Do not change scope, dependencies, section IDs/counts, acceptance criteria or substantial prerequisites without explicit owner approval BEFORE implementation” applies. All other approved bounds remain.

**No scope deviation in preparation. Explicit prospective local timing amendment; no code implemented.**

## Preparation checks

Current frozen-baseline, cross-repository consistency, backend architecture and both whitespace checks passed. All 25 required governance tests passed. These are documentation/readiness checks only; TC2 implementation and runtime tests remain pending owner approval.
