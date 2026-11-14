# APP-013 / 3A / P08 — TR19 owner credential renewal

PREPARED, NOT APPROVED. KQ2 is consumed and closed: two owner/project CLI checks completed, one cache allowance was reserved, no explicit key-API request or key mutation occurred, private files were purged and operation processes are absent. The generic retained failure does not prove token expiry, insufficient horizon alone, or successful token acquisition. TR19 re-establishes owner credential coverage; it cannot prove KQ2's historical cause or guarantee a later key qualification.

Current backend source/evidence HEAD: `1dabb8f9195ee68b9150f6f4e32d0b951b049a4a`. Renewal checks all tracked APP-013 evidence, so this exact HEAD is used rather than runtime-only ET1 source `4173ec0`. Section 3A's same-admitted-job Sandbox payment and matching application-gate criterion remains unchanged (`APP013_REMAINING_EXECUTION_CONTRACT.md:62` and existing DATA_CONTRACTS.md payment identity/mode/account/amount/currency rules). This is a credential prerequisite only. Accepted 1A/1B/2A/2B remain 4/8; 3A OPEN; R1 newly closed 0/27.

## Exact operation and authorization effects

Invoke once:

```sh
/opt/homebrew/bin/gcloud auth login debynyhan@signmons.com --force --no-activate --brief --quiet --verbosity=none
```

Use installed SDK 583.0.0 and pinned Python 3.14.2. The owner selects **debynyhan@signmons.com**, then personally completes the Google browser/MFA/consent flow. No password, authorization code or authorization URL is copied into chat or logs. No second invocation, manual-code fallback, ADC update, impersonation, credential import, alternate account/configuration or custom scope is included.

The existing command requests these seven standard scopes:

- `openid`
- `https://www.googleapis.com/auth/userinfo.email`
- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/appengine.admin`
- `https://www.googleapis.com/auth/sqlservice.login`
- `https://www.googleapis.com/auth/compute`
- `https://www.googleapis.com/auth/accounts.reauth`

Existing grants are not read. The explicit SDK exception covers OAuth/browser/callback traffic, internal authentication retries and persistent credential/token/cache metadata maintenance. Internal authentication request count is UNKNOWN. Browser/SDK credentials remain after closure; sign-out, revocation and cache erasure are not included. No provider-resource probe, external SQL, IAM/key change, Stripe/payment, deployment, charge/refund, customer action or additional spending is authorized.

## Exact window, conditional validation and cleanup

Saturday **November 14, 2026, Eastern time**: launch strictly before **1:40 p.m.** (`18:40Z`); one sign-in is bounded to **300 seconds**; independent closure ends by **1:47 p.m.** (`18:47Z`). Only exit 0, verified owned leader/group absence and unchanged exact account/project configuration permit one reserved **eight-second** call to the existing `read_cached_token`, requiring validity strictly beyond **2:15 p.m.** (`19:15Z`). This is a target to verify, not a promised credential lifetime. Immediately discard the token; retain only a safe enum, never the token, actual expiry, raw cache data or token hashes. No separate advance cache/CV read is needed or authorized.

Failure to cover the future horizon does not prove the token is already expired. No retry or repair follows failure. The owner is asked to be ready for browser sign-in and remain reachable through **2:20 p.m.** for a possible separately approved follow-up; no later key/payment action is authorized by this proposal. A future packet must fit the observed credential horizon, its applicable cleanup reserve and its own exact approval.

Reuse the reviewed one-shot TR18/TR17 procedure and `packet.renewal_preflight`. Reservation: `owner-signin-20261114-tr19`; exclusive 0700 receipt directory: `evidence/APP-013/p08-narrow-access-check-local-20261101/renewals/20261114-tr19/`; 0600 safe receipts and a nonblocking lock. The compatibility decision remains `APPROVE_TR1_CREDENTIAL_RENEWAL_SDK_RETRY_CACHE_AND_CLEANUP`, bound to this proposal hash, exact source, reservation and window. Only a committed `APP013_P08_TR19_DECISION_20261114.json` can authorize execution. A review draft or placeholder cannot.

Reject ambient credential/proxy/configuration overrides. Use DEVNULL for process stdin/stdout/stderr and the existing reviewed SDK environment, which disables file/HTTP logging, prompts and usage reporting. Directly own one process group, with monotonic and wall-clock bounds. On timeout/interruption, terminate/reap only the still-owned group using bounded TERM/KILL, then independently verify leader/group absence. Never guess a PID or close unrelated browser windows. UNKNOWN closure remains UNKNOWN and blocks the conditional cache check. Remove the owned temporary executor after closure or abandonment; retain only safe attempt/result/verification receipts. Browser credentials remain under the owner's custody.

## Source, readiness and finite checklist

The reviewed TR18 executor is recovered with its receipt-recorded SHA256 and inspected before use. Only operation labels, current source, exact attendance/window bindings and the eventual approval-commit reference change; preserve the deferred-signal spawn/registration guard and all process/cache/cleanup logic. No new runtime implementation or subsystem is proposed. The placeholder prevents pre-approval execution. The prepared executor hash and binding-only comparison are recorded in `APP013_P08_TR19_SOURCE_READINESS_20261114.json` before approval is requested.

| Prerequisite / responsible owner | Actual interface and evidence | Required readiness result |
| --- | --- | --- |
| Source, output contracts, SDK and runtime / implementer | Actual `packet.renewal_preflight`; current and committed qualification/native/dependency graph; 51 SDK files plus nine additional sign-in SDK files | Fresh local preflight and exact SDK hash comparisons; no token/provider read or operation reservation |
| Configuration and identity / implementer and credential custodian | Existing `config_snapshot`, override rejection, exact command and seven scope definitions | Current local configuration PASS; browser identity/consent and new credential coverage remain UNKNOWN until execution |
| Deadline, no retry, concurrency and interruption recovery / implementer | Existing one-attempt reservation, nonblocking lock, deferred-signal ownership registration, 300-second process bound and conditional eight-second cache check | Source/command/authority/window comparison before launch; leader/group closure before cache read; no automatic extension |
| Retention and closeout / implementer and credential custodian | DEVNULL, persistent SDK cache exception, discarded token, 0600 safe receipts and removal of the owned executor | Safe result, unchanged exact configuration and independent receipt/process closure by 1:47 p.m. |
| Approval and attendance / owner | This exact proposal and false-authority review draft; prior TR18/KQ2 consumed | Exact sign-in/scopes/cache/cleanup approval, browser readiness and reachability through 2:20 p.m. |

Finite tasks: prepare source/scope and recovered executor; verify actual local preflight/SDK/command and binding-only reuse; obtain independent review and required documentation checks; obtain exact approval; compare current source/clock/authority; reserve once and invoke once; conditionally check credential horizon; independently close processes/configuration/receipt custody; save safe result and remove executor. No Terminal or Neon password prompt is part of TR19.

Preparation checks: backend governance baseline, architecture and whitespace; governance frozen baseline, consistency, 25 governance tests and whitespace; actual local renewal preflight and nine additional SDK hash comparisons. Existing ET1 tests match the unchanged runtime; they are not reported as newly run for this preparation. Effective provider access and connected payment state remain UNKNOWN.

Observable finish: `VALID_THROUGH_CUTOFF` with independently verified closure, or a safe unqualified result without retry. Before exact approval the operation is disabled and unreserved. After an attempt, preserve its receipt and do not replay; no token revocation or external rollback is inferred. **No scope deviation.**
