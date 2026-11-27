# AP1 clarified local proposal — distinguish the reproduced failures

PROPOSED; NOT IMPLEMENTED. This addendum and APP013_P08_AP1_AUTH_PAYMENT_BOUNDARY_PROPOSAL_20261127.md together form the owner review. Where they differ, this addendum controls. Source remains4e29a9114245990fd69712749505e5b069d9ca70. Section APP-013 / 3A / P08 and all acceptance criteria remain unchanged. No Terminal attendance or timed approval window is needed.

## Concrete finding

The newly run existing helper test_entry.JournalContractIntegrationTests.ec1_completed reproduces two distinct synthetic causes through actual child, journal, parent and independent closeout: an invalid token role claim and runtime HTTP403. Both retain exactly TOKEN_INTENT / ADAPTER_REFUSED_OR_UNKNOWN, authenticated false, no payment, null child result digest and AUTH_OUTCOME_UNKNOWN. Both passed all existing helper assertions and purged their synthetic inputs. APP013_P08_R65_LOCAL_AMBIGUITY_REVIEW_20261127.json records the results and timestamp. All12original R65 receipt hashes remain unchanged. No provider, credential, database fixture or browser activity occurred.

The original AP1 proposal separates runtime authentication from payment handoff but does not distinguish these two reproduced pre-payment failures. It therefore needs the following bounded additions before implementation, not another full run to rediscover the same aggregate label.

## Exact clarified implementation scope

Retain the original six source/test files and optional post-authentication payment hook. In the existing recovery-sequence.mjs only:

1. Preserve TOKEN_INTENT for issuance. After a nonempty token is returned and before calling clients.authenticate, persist RUNTIME_AUTH_INTENT in the existing phase field.
2. Extend the existing fixed safeCode allowlist by exactly four already-generated source codes: TOKEN_CLAIMS_DRIFT, TOKEN_TIME, AUTH_RUNTIME_REFUSED and EXACT_JOB_READBACK. They come from unchanged client.mjs and its existing operator-bridge reader; no provider text or exception message is retained. All other unrecognized errors remain ADAPTER_REFUSED_OR_UNKNOWN.
3. Preserve the original AP1 distinction: after original runtime authentication returns, save AUTHENTICATED/authenticated=true; only then enter PAYMENT_HANDOFF_INTENT and invoke the optional existing payment composition. Do not infer payment or parent proof from these phases.
4. In bound_handoff.py allow exactly the two new finite phases, RUNTIME_AUTH_INTENT and PAYMENT_HANDOFF_INTENT. Do not add fields or broaden diagnostic-value acceptance.

The six files remain recovery-sequence.mjs, bound_handoff.py, test_bound.mjs, test_bound.py, native_child.mjs and test_entry.py at the paths and hashes in the original proposal. No edit to client.mjs, operator-bridge.mjs, transport, provider descriptors, acceptance predicate, product app, database or SDK is proposed.

A current transitive-hash inspection found one omitted derived dependency: p08-connected-packet-20261110/vm2-source-manifest.json. The scope is therefore the original eight manifests PLUS that ninth existing manifest, derived hashes only. This is disclosed before approval/implementation to avoid another mid-implementation scope stop. All original historical locks/receipts remain immutable.

## Observable local finish and tests

Reuse the original AP1 positive, negative, privacy, deadline, concurrent/merge/lost-output, recovery and full selected regression checklist, explicitly excluding PostgreSQL fixtures. Add assertions through the existing same child/journal/parent boundary that the two reproduced cases now differ truthfully:

- Invalid role claim: RUNTIME_AUTH_INTENT / TOKEN_CLAIMS_DRIFT; authenticated false, no payment or parent proof.
- Runtime403: RUNTIME_AUTH_INTENT / AUTH_RUNTIME_REFUSED; authenticated false, no payment or parent proof. The code identifies runtime refusal, not its provider-side cause or HTTP401 versus403.
- Existing token expiry and mismatched-job tests retain TOKEN_TIME and EXACT_JOB_READBACK respectively; generic/private canary errors remain fixed UNKNOWN and cannot leak strings.
- Issuance failures retain existing SIGN/KEY_READ/EXCHANGE diagnostics; successful runtime authentication followed by payment-handoff refusal retains authenticated=true and PAYMENT_HANDOFF_INTENT, without payment acceptance or manufactured proof digest.

No-hook callers retain behavior and outcomes, with the deliberately approved additional diagnostic phase. This supersedes the original proposal's byte-equivalent-control-flow wording; phase persistence itself necessarily changes journal versions. Test exact current sequence/concurrency transitions rather than silently weakening assertions. Existing request counts, one-attempt rules, deadlines, cleanup, private purge, parent proof/readbacks and all payment/event/gate checks stay unchanged.

Required verification: direct Node/Python tests, applicable full native and connected packet suites, current and committed source checks, architecture, frozen baseline, complete consistency,25governance tests and both whitespace checks. Do not rerun prior tests merely to inflate counts. No real credential/provider/SQL/browser/payment action, retry, deployment or new attended session follows from local approval.

This will fix the demonstrated loss of failure distinctions; it is not a claim to fix R65's unknown provider/runtime cause or prove that the next live payment will succeed. R65's original result cannot be reconstructed from a synthetic case. Future readiness must use the corrected evidence without relabeling history.

Completed now: current-source and receipt review, two-case local reproduction, original proposal review and complete nine-manifest dependency check. Remaining after owner decision: implement only the described six-file/nine-manifest changes, prove distinctions and unchanged cleanup/proof behavior, then record review-ready evidence. Implementer owns local work; owner decides the semantic/diagnostic scope, and all external custodians retain separate authority. Rollback: restore these six sources and nine manifests together; no operation is running. Accepted4/8;3A OPEN;R1 newly closed0/27; no completion percentage or ETA inferred.

Prospective scope clarification only; no implementation deviation. Requested decision: approve AP1 together with this addendum, six existing source/test files and nine derived manifests, local synthetic checks only.
