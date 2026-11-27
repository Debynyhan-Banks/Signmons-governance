# BR2 — local call-budget amendment

PROPOSED; not implemented. This is the exact stop condition in the approved BR2 card: if the current192-call cap cannot cover the worst case and cleanup, stop for a separate decision. Local approval8c56d0f remains valid for the original implementation scope. No provider operation or new live authority exists.

## Demonstrated blocker

Two synthetic executions through the actual connected parent, runtime adapter, accounting, fake credential acquisition, fixture child and independent closeout are recorded in APP013_P08_BR2_BUDGET_BLOCKER_20261126.json:

- Immediate matches:191 CLI calls, one enable/one disable, final ENTRY_CLOSED, no residuals, private inputs absent.
- Two extra state observations after each acknowledged transition: both transitions reached a matching third observation, one enable/one disable remained, but accounting stopped at192 CLI calls. Final ENTRY_CONTAINMENT_UNCONFIRMED retained TRAFFIC_PRIVATE_PLANS because required remaining closeout reads could not fit. Private inputs were still purged. This was entirely synthetic, with zero provider/credential/database-fixture actions.

The currently demonstrated normal path plus the maximum four extra reads requires195 calls by calculation. The full195-call closed result has not yet been demonstrated; the192cap correctly prevented it. Increasing the prospective limit to196 preserves the original one-call headroom rather than consuming cleanup capacity. This is explicit finite read authority, not mutation retry or SDK retry expansion.

## Exact amendment requested

Authorize local source/tests only to change the future connected packet's CLI cap from192 to196, specifically for BR2's at most four additional identity observations. Retain100 HTTPS/60 SQL/6 child/200 child-request caps, all one-mutation/no-transport-retry rules, deadlines, ownership checks,420/960-second work reserves,660-second cleanup and120-second purge reserves, spending limitations and no automatic live action. Every future live packet must visibly disclose196 and receive fresh exact authority. Old consumed192-call packets/decisions stay immutable and unusable with changed source.

Extend the approved local file scope by two existing files under evidence/APP-013/p08-connected-packet-20261110: packet.py (exact prospective limit guard) and test_packet.py (guard/refusal coverage). The original entry.py/test_entry.py and the same eight derived manifests remain in scope. Inspection of original committed hash references found no additional current manifest dependency for these two packet files; this must be rechecked after implementation. No shared transport/authority/SDK/application change or new subsystem is authorized.

Tests must prove a successful assembled195-call worst-case path with independent closure under196, unchanged191-call immediate path, refusal under192, rejection of any cap other than the newly exact196 in packet construction, actual call reservation before dispatch, no fourth observation, no mutation retry, no cleanup reserve reduction, and all original BR2 negative/interruption/concurrency/persistence/source/privacy cases. Use synthetic fixtures and harmless local processes only; explicitly exclude PostgreSQL fixtures. Reuse the actual packet/timing interfaces. Run the original card's selected regressions and governance/source checks. If another material gap appears, stop instead of widening scope.

Alternatives: retain192 and allow at most one extra read globally (does not satisfy approved BR2 three-observation policy); drop required cleanup reads (rejected); repeat mutations or a full live attempt (rejected). No external billing or spending action follows from this local decision.

## Current working state and finish

Approved partial changes exist locally in entry.py and the eight current manifests; test_entry.py has not yet been edited. No backend implementation commit or live launch occurred. The initial eight-test diagnostic regression had six passes and two expected failures because historical assertions still require one read; these assertions and the new policy tests remain unfinished. Do not present BR2 as verified or execution-ready. The original source remains committed atfabd456. Unrelated AGENTS.md and renewal files remain untouched.

Rollback/disabled state: no operation is launched; if the amendment is declined, preserve or explicitly revert only the BR2-owned partial changes without touching unrelated work. Implementer owns the local amendment/tests and final source-bound readiness; owner owns this changed prospective call limit; future cloud/credential/payment decisions remain separate. No Terminal attendance or deadline is needed.

Observable finish remains the original BR2 local proof, now including adequate196-call capacity. This does not guarantee provider convergence, resolve R64's historical cause, or complete3A. Accepted milestones4/8;3A OPEN;R1 newly closed0/27. Explicit prospective scope deviation: four additional future CLI-read slots and two packet files, before implementation.
