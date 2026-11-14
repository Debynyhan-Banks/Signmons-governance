# APP-013 / 3A — IQ1 local implementation and containment complete

Runtime source: backend `bdec9fa789b7a749434bf81fd23b843b885e4ebf`. Original local approval: fa98c82; containment amendment approval: 46137d2. This closes local IQ1 implementation/testing, not live qualification, payment or section acceptance.

## Implemented behavior

The three approved IQ1 files implement an exact committed-decision gate, source/configuration/resource/command bindings, an IQ1-only sandboxed SDK command translation, fixed 5-command main and 6-command cleanup sequences, and immutable mutation reservations. Existing RuntimeAdapter/NativeIO serialization and RB1 readbacks are reused. Shared transport, installed SDK, existing manifests and historical operations are unchanged.

The detached cleanup worker holds the IQ1 resource lease and owns all SDK process objects. Its separate main coordinator requests only five ordered steps. The ready receipt is verified before enable; every SDK process is started under the OS child-creation restriction. Main/launcher loss permits independent cleanup; worker loss or incomplete results remain UNKNOWN. Lost enable acknowledgement is not erased by a later disabled readback. Cleanup checks fresh owner/project and the original UID hash before one disable, then verifies disabled state and final UID. No ownership is inferred from an arbitrary PID. No automatic replay or unsandboxed fallback exists.

The executable gates enforce exact approved scope, manifest and wrapped commands before native hooks; per-step order/count/deadline/configuration/source/custody checks; and typed external approval. Receipt tampering, unavailable sandbox, foreign command, changed identity and source/configuration drift refuse. Local process closure does not prove that a remote mutation was cancelled. No claim of branch protection or universal process recovery is made.

Only safe scope/binding/stage/UID-hash/count/status evidence is retained. Raw UID/project responses and SDK output remain transient; no password, token export, explicit credential-cache read, key/secret access, SQL or payment interface is exposed. The SDK may internally refresh/use its existing cache only under the future separately approved exception. The original 660-second cleanup and 120-second purge reserves remain enforced; no private input files are required by IQ1. A safe result is never interpreted as payment evidence.

## Local readiness and validation

Backend evidence directory: `evidence/APP-013/p08-connected-packet-20261110/iq1-local-verification/`.

| Prerequisite | Source/evidence and result | Responsible role |
| --- | --- | --- |
| Actual parsing/serialization/readback | 51 IQ1 tests included in final 187 connected tests; actual NativeIO serializer/RB1 methods, exact vectors, omitted/null/bool/numeric/malformed values, initial state/UID checks, safe failures; PASS | Implementer |
| Source/configuration/runtime pins | 33 repository and 47 SDK/runtime files pinned; committed source guard PASS in 0.585 seconds at 2026-11-14T21:45:00Z; local configuration shape PASS; `readiness.json` | Implementer |
| Process containment | Actual sandbox/owned transport tests deny fork/spawn/detached children; missing sandbox refuses; actual coordinator killed after enable still triggers cleanup; finite detached-worker fixture survives launcher loss; killed worker yields UNKNOWN | Implementer |
| Recovery/concurrency | One enable/disable ceilings; lost acknowledgements; before/after-intent interruptions; fresh cleanup owner/project/UID; cleanup disagreements; deadlines/clock rollback; duplicate reservations, lease conflicts, foreign process refusal and receipt/root tampering; PASS | Implementer |
| Regression | Final connected suite 187 PASS; native Python suite 135 PASS; build, lint and architecture PASS. Connected suite includes local loopback browser fixtures, not live Stripe/account interaction | Implementer |
| Governance | Frozen baseline, cross-repository consistency, 25 required governance tests and both whitespace checks PASS; results recorded in readiness evidence | Implementer |
| Live credentials, permissions and SDK operational compatibility | UNKNOWN. Help parsing and synthetic responses do not establish authenticated runtime behavior | Owner / credential and cloud custodians |
| Current identity state and UID | UNKNOWN. Original R48 discarded mismatch remains UNKNOWN | Cloud custodian |
| Live timing and decision | Unbound descriptor template only; no operation/window, external decision or attendance booked | Owner / implementer |

Verification commands: pinned Python `-B -m unittest discover` over the connected directory and native-entry source directory with `-p 'test_*.py'`; `npm run build`, `npm run lint`, `npm run arch:check`; backend governance-baseline command, governance frozen-baseline/consistency commands and the three required governance test files; `git diff --check` in both checkouts. Local process/sandbox and loopback tests ran with tool approval outside the nested tool sandbox. All provider calls and real credential-cache reads were zero.

Initial development failures were resolved locally: synthetic timestamp fixtures now follow the existing strict UTC format; final configuration checking uses the same driver dependency as phase gates; the exact pinned interpreter is compared by canonical filesystem target because Homebrew reports an equivalent symlink path. Final regressions cover the resulting implementation. No validator was weakened to accept another interpreter or expired authority.

## Checklist, remaining work and next observable result

Original local items 1–5 complete: authority/wrapper, independent worker, actual adapters, failure/recovery/process tests and regressions. Item 6's committed implementation/readiness evidence and descriptor template are complete; the exact live packet still needs fresh timing, credential readiness, non-overlap/availability and separate external authority. This is qualification-only readiness, not execution-ready status.

Next: prepare one fresh IQ1 identity-only live qualification from `live-review-template.json`. It retains 11 CLI maximum, one enable/disable, no SQL/password/payment flow, and the SDK exception. Do not infer credential validity from configuration shape or reuse a consumed window. If renewal is necessary, review that distinct action before it occurs. The observable result is either confirmed enabled/disabled same-UID state with independent closure or one safely classified failure with explicit residuals. No full payment run follows automatically.

After that boundary qualifies, 3A still requires current connected readiness, authentication, owner-completed same-job Sandbox Checkout, authentic matching event/application gate and failure-recovery evidence, independent closure and owner acceptance. IQ1 does not clear R47 historical account/session/revocation uncertainty. R48 remains consumed.

Rollback/disabled state: new IQ1 cannot perform native work without its separately committed exact external decision. No deployment, merge, push, provider configuration or payment was performed. Unrelated owner changes remain intact. Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27. No scope deviation beyond the prospectively owner-approved IQ1 containment amendment.
