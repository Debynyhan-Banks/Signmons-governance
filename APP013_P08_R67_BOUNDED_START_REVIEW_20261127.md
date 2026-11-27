# R67 / TR40 — one bounded start-time decision

**PROPOSED; NOT APPROVED OR LAUNCHED.** APP-013 / 3A / P08. Source `fef39a05cd7e83b54e74a6774716c2b9ab5a4286`. This is a timing/authority amendment and replacement opening proposal, not a backend implementation change. R66/TR39 is EXPIRED_UNSTARTED: the first clock check on receipt of approval was6:33:53a.m.Eastern, after sign-in6:28 and recovery6:30. No attempt, provider call, credential input or payment occurred; nine owned paths were absent and the hash-matched unapproved executor was removed. Original R66 approval cannot launch R67.

## Demonstrated gap, alternatives and proposed decision

The short fixed launch window expired while the owner was replying, before any action. Repeating another three-minute approval deadline creates the same risk. Waiting for a later fixed appointment is possible, but does not remove that timing dependency. Proposed alternative: authorize **one constants-only binding of the start and dependent deadlines after this approval**, inside the exact bounded interval below. No changing resource pins, source, action limits, identities, success checks, cleanup reserves or approval stages. No new subsystem, acceptance section, dependency, runtime code or automatic retry.

The template `APP013_P08_R67_TIMING_TEMPLATE_20261127.json` fixes fresh operation IDs, current source/manifest/resource/identity hashes, database, account hash and all limits. Its SHA-256 is `83bf802d24393b9d3615f5d15f6585c8e86030791b6cdbc27289287da1b9a1a2`. Only the reviewed absolute time fields and the hashes necessarily derived from those fields may be bound after approval. The unchanged Chrome-first executor and short-file Terminal dispatcher may receive the corresponding R67/TR40/date/source/attendance/decision-reference constants only.

## Exact one-time timing rule — November27, America/New_York

Let **S** be the later of6:45a.m. and the next whole minute at least120seconds after the actual binding clock. Require **S no later than7:15a.m.** Binding may happen only after this exact owner approval, once. If that formula exceeds7:15, stop; this does not authorize another replacement or extension. Practically the reply must arrive before7:13a.m. to leave the required binding lead time. All times are UTC-backed; the rule is not based on a guessed chat timestamp.

Before any external action, record S and every derived absolute deadline, compare all non-time fields to the template, run the existing source/recovery/sign-in/native/timing preflights, and commit the binding and exact decision records. Owner explicitly delegates this one constants-only binding and commitment of decisions representing this approval; it is not assistant self-approval. Publish the resulting exact timetable in chat. Once committed, S cannot slide again. No new automated enforcement is claimed for this operator gate; existing runtime validators enforce the bound absolute decisions.

| Stage | Fixed offset from S | Latest possible Eastern bound |
| --- | --- | --- |
| TR40 sign-in | Start at/after S, strictly before S+3min; at most300seconds | Before7:18a.m. |
| TR40 independent cleanup | S+10min; one conditional8second cache check requires coverage strictly beyond S+60min | Cleanup7:25; coverage beyond8:15 |
| R67 recovery | Dispatch before S+5min; reads end S+9; session cleanup S+14 | Dispatch7:20; reads7:24; cleanup7:29 |
| Qualification, separately approved later | Confirmation/commit before S+12; reads S+17; cleanup S+22 | Approval7:27; reads7:32; cleanup7:37 |
| Native, separately approved later | Manual confirmation/commit/dispatch before S+14 | Before7:29 |
| Payment/work/cleanup/purge | Payment S+46; work S+47; cleanup S+58; private purge S+60 | 8:01 /8:02 /8:13 /8:15 |
| Owner attendance | Stay75minutes from S | Latest8:30a.m. |

Sign-in and recovery remain one attempt. Credentials must cover the bound purge time, not the maximum time if an earlier S is selected. All native660second cleanup,120second purge and3600second custody limits remain unchanged. Native's earlier manual dispatch gate remains stricter than its program cutoff. The exact bound packet must pass existing admission again before launch.

## Opening scope authorized only if the owner approves this proposal

1. **TR40 sign-in:** one `/opt/homebrew/bin/gcloud auth login debynyhan@signmons.com --force --no-activate --brief --quiet --verbosity=none`; same seven scopes: openid; https://www.googleapis.com/auth/userinfo.email; https://www.googleapis.com/auth/cloud-platform; https://www.googleapis.com/auth/appengine.admin; https://www.googleapis.com/auth/sqlservice.login; https://www.googleapis.com/auth/compute; https://www.googleapis.com/auth/accounts.reauth. Owner signs in personally. Same approved Chrome-first child environment, not exclusive routing; existing SDK refresh/internal-authentication-retry/persistent-cache exception, with internal request count UNKNOWN. One conditional eight-second existing cache-validity read only after exit0, unchanged configuration and owned-process/group absence. Token immediately discarded; safe status retained. Persistent SDK cache remains after independent cleanup. No operator retry, alternate account or exported credential.
2. **R67 recovery, conditional on successful coverage/cleanup:** maximum2owner/project CLI reads and3read-only SQL queries, existing SDK exception, normal and independent session cleanup and private purge. Hidden input order: Neon database password, then existing pinned we_ destination ID. No sk_test_ key requested at recovery.
3. **R67-only later Terminal delegation:** owner enters the entire displayed APPROVE QUALIFICATION or APPROVE SANDBOX phrase including both number/letter groups. Assistant independently verifies the exact review/confirmation and commits it before release. No stale confirmation, status-as-approval or assistant-entered phrase.
4. **Guarded browser opening:** one existing Chrome incognito opening only after later native approval and the actual attended-payment stage; manual $99 test Checkout. No advance payment approval.

Later qualification remains a separate exact decision: at most27CLI,20HTTPS,4SQL and1credential-cache read, stated SDK exception and independent cleanup. Later native scope remains separate: reviewed exact temporary runtime identity, numeric-secret, IAM, owned restricted key, test-account, database-role, candidate-tag and existing Sandbox-webhook actions; caps196CLI,100HTTPS,60SQL,6child processes,200child requests; stated SDK exception; guarded opening/manual Sandbox Checkout; independent cleanup/purge. These limits are disclosed here, **not authorized in advance**. AP1 reporting and BR2 identity readbacks remain current.

$0 additional spending allowance is not a hard cloud-billing cap; existing liabilities remain unchanged. No real charge, refund, booking, customer/support contact, production deployment, new infrastructure or automatic retry. Cleanup may require another hidden Neon administrator-password entry. Never enter private values into chat.

## Readiness, checklist and responsibilities

| Prerequisite | Source/evidence | Result and responsible role |
| --- | --- | --- |
| Exact source/configuration and provider output boundaries | Existing current/committed manifest guards, qualification/native source, AP1 completion | Current source/43SDK guards PASS; prior249selected tests reused, not rerun / implementer |
| Dynamic resource and private custody binding | Actual BindingRecoveryCapability.prepare and packet.construct_values/native_envelope/Capability at both earliest/latest S with synthetic private fields and inert authority | PASS; no actual private input or attempt / implementer |
| Deadlines, admission, settling and reserves | Actual Coordinator require_child_entry and settle_bindings at S+14min minus1second, then480setup+45identity+420settling | Both endpoints leave976seconds above960reserve; no request dispatched / implementer |
| One attempt, concurrency, interruptions, closeout and purge | Unchanged existing interfaces and AP1 regressions; final exact S must rerun real preflights | Local proof reused; six prospective roots absent, no executor/authority bound / implementer |
| Sign-in template/browser/SDK | Committed approved Chrome-first template73686cddb7f5f70332155432d82f2d87c325c4a95a4a0bd1c8b717a00866084d and R66 actual preflight; constants-only TR40 binding allowed only after approval | Prior same-source local proof; exact bound preflight required before launch / implementer |
| Current external prerequisites | No current credential/cache/provider/SQL read | UNKNOWN / owner and cloud/database/Stripe custodians |
| Customer finish | Existing same-job signed-event/application-gate acceptance criterion in APP013_REMAINING_EXECUTION_CONTRACT.md §3A | NOT DEMONSTRATED / product owner and implementer |

Completed: expired-unstarted closeout; explicit timing-amendment review; fixed non-time template/fresh IDs; current source/SDK checks; actual earliest/latest recovery/native/admission proof; local temporary-root cleanup. Remaining: this owner amendment/opening decision plus75minute availability/no-overlap; bind/verify/commit S and exact artifacts once; sign-in/coverage/cleanup; recovery; later exact qualification and native decisions; same-job payment/event/gate; independent closeout; owner acceptance. First observable external result is sign-in coverage/closeout, not presumed payment success.

No provider, credential-cache, real SQL, browser, payment or database-fixture action occurred during preparation. No runtime source changed. Exact provider state/effective access/API/key compatibility, identity convergence, authentication and payment remain UNKNOWN; fixtures cannot establish them. Source-bound timing readiness is qualification-only, not execution-ready.

On decline/expiry leave all actions unbound; remove only any exact owned preparation artifacts. On failure retain corrected AP1 stage/code and cleanup evidence; do not replay a full attempt merely to rediscover an aggregate label. Accepted1A/1B/2A/2B remain4/8,3A OPEN,R1newlyclosed0/27. **Explicit prospective deviation:** owner delegates one constants-only timing binding within6:45–7:15a.m. instead of approving already-fixed timestamps. Not implemented or used; all other scope/limits are unchanged.
