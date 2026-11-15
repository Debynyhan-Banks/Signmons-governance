# APP-013 / 3A — CT1 current account containment validator

PROPOSED LOCAL CHANGE ONLY; not implemented or externally authorized. Baseline backend1f8fa97/runtime2f19eb8; governancefb63475. Gap proven by APP013_P08_POST_IQ8_READINESS_RECONCILIATION_20261115.md: generic Firebase revocation lower bound2026-10-26T13:17:28.538Z predates R47 revocationIntentAt2026-11-14T19:22:30.000Z. A generic passing result cannot reconcile current containment against that later intent. Historical AUTH_OUTCOME_UNKNOWN cannot be reconstructed by new reads.

## Exact local acceptance criterion

Add one pure, operation-bound validator for already-returned app/account, database-session and Firebase lookup responses. Return only fixed safe identity/disabled/claims/email-verification/session/revocation-bound flags and CURRENT_CONTAINMENT_CONFIRMED or CURRENT_CONTAINMENT_UNKNOWN. Confirmation requires exact existing account fingerprint/identity, explicit disabled app/Firebase states, expected claims, zero matching database sessions and validSince at least R47's second-precision revocation intent. A current confirmation must never rewrite R47 receipts or assert whether its historical authentication succeeded.

Do not change REVOCATION_LOWER_BOUND_MS, generic qualification acceptance, IQ8/BR1 behavior, native payment entry or installed SDK. Do not add an executable runner, provider client, generic diagnostic framework, API endpoint, private-input store or recovery subsystem. Local implementation ends at a tested validator and source-pinned read-composition specification. If existing read interfaces cannot safely supply the required data without broader work, stop with the exact gap rather than inventing new infrastructure.

## Reuse and inspected interfaces

- qualification_launch.py QUALIFICATION_SQL/sql_contract/read_database: exact one-account identity and TARGET_SHA256 fingerprint, disabled app status, tenant/job and matching pg_stat_activity session inventory. Its existing query recovers the UUID transiently; no owner UUID lookup is needed. Reuse existing parser through an inert one-response seam where practical, not a reconstructed partial business predicate.
- firebase_https_contract(uid): fixed projects/signmons accounts:lookup POST with one already-validated localId. NativeIO.https has descriptor allowlisting, response cap, no redirects/proxy and deadline handling. This is a read despite POST.
- read_firebase: existing REST field parsing/custom-claims/validSince shape semantics. Do not alter its global threshold. CT1 validates the same returned body against the explicitly bound R47 cutoff and also checks emailVerified using exact_firebase's conservative contract.
- native-closeout adapter.py exact_account/exact_firebase: exact target/status/claims and second-precision revocation comparison. Normalize only explicitly returned REST fields into the expected shape; never fabricate missing disabled/emailVerified/claims/revocation values. Reject unsupported timestamp ranges, malformed numbers/duplicates, foreign identity and missing fields. Use one received response, no second HTTP call.
- R47 journal/result: bind original operationbea4fe6b-2202-48ed-9df1-84a17d23fcd8, exact committed safe journal hash and revocationIntentAt. No raw UUID/password/token/provider body in output. New source pins refer to existing immutable evidence, not consumed authority.

Database-session flags refer only to the query's matching database connections, not every Firebase token/session. Revocation flags mean the returned cutoff meets the bound; they do not prove global access-token invalidation or historical authentication outcome.

## Section card and finite checklist

Section APP-013/3A; objective is the current-containment prerequisite to the same connected payment journey. New behavior requires the owner decision before coding. Expected files: p08-connected-packet-20261110/account_containment.py, test_account_containment.py, account-containment-source-manifest.json; safe local evidence/governance only. Existing modules are imported/reused without edits. No dependency installation, database migration or app/UI interface change.

1. Trace exact input schema and existing parser invocation, R47 committed evidence/timestamp, SQL session scope and REST-to-existing-validator conversion before edits. Pin source/evidence and record unresolved live facts.
2. Implement pure fixed-output validation with no native fallback and no credential acquisition; bind expected target fingerprint and historical revocation reference. No globals patched to change acceptance.
3. Test valid latest/equal-second timestamp; older October-only success rejected; one second stale; malformed/null/missing/huge timestamps; missing/invalid emailVerified/disabled/claims; wrong UID/tenant/account; duplicate/malformed/multi-user responses; wrong journal hash/operation/time; nonzero database sessions; raw-secret sentinels absent from all result/errors. A lost response remains UNKNOWN, never a mutation or retry instruction.
4. Exercise actual existing serializer/parsers with injected synthetic responses and no network/credentials. Verify independent calls cannot cross-bind inputs and no mutable global state leaks between operations. No browser change; reuse existing UI evidence, no invented UI acceptance.
5. Produce source-pinned read-composition specification using actual existing descriptors. Proposed future maximum: three CLI reads (owner, project, SDK access-token command), one read-only SQL account query, one Firebase lookup and one independent SQL session-closeout read. Token/password remain transient; no raw export to user/log/file. Exact launch/credential/window/cleanup review is separate. Do not issue a live packet if local process/custody or read-interface requirements remain unresolved.
6. Run focused validator tests, connected/native regressions as affected, source guard, architecture, frozen baseline/consistency/25governance tests and whitespace checks; preserve historical receipts and unrelated AGENTS/renewal work. Finish with source SHA, commands/results, safe evidence, UNKNOWNs and next observable result.

Concurrency/recovery: pure functions own no sessions or resources and do not mutate inputs; per-operation source/identity binding prevents cross-adoption. Future external composition must reserve once, enforce per-call budgets/cutoffs, own processes and perform independent closeout/private purge; local validator approval does not authorize or claim those live controls. Existing credential/password input and cleanup policies remain unchanged. No deadline or retention extension.

## Proposed later read scope — not authorized now

Use debynyhan@signmons.com and project signmons. Obtain current account UUID from the existing exact SQL query in memory; no separate retained private-identifier recovery session. A hidden Neon password prompt will be required only after full preparation and exact approval. The existing SDK token command is an explicit credential read/export into process memory, distinct from the earlier IQ8 no-token-export exception; later approval must name it, SDK refresh/cache effects and cleanup. No sign-in, account enable/disable, token revoke, key creation, runtime activation, payment or support action is part of the proposed read. If account/permissions/credentials are unavailable, stop and report; do not change them.

No live attendance requested now. All live state remains UNKNOWN beyond IQ8's historical observation. This validator cannot retroactively close R47's historical authentication outcome or establish readiness for a payment on its own.

## Decision, alternatives and finish

Alternatives: repeat generic qualification (insufficient timestamp coverage); change shared cutoff (affects unrelated consumers and loses explicit historical binding); replay R47 closeout (consumed authority/private inputs absent); invoke full payment child just to inspect accounts (unnecessary mutations/payment coupling). A pure bound validator plus existing reads is the smallest proposed local change.

Owner decision requested: approve CT1 local validator/tests and source-pinned composition specification only. Implementer owns finite completion; owner/cloud/DB custodians retain subsequent live authority; owner accepts3A only after authentic same-job payment evidence. Rollback/disabled state: validator remains unregistered/uninvoked by production or connected entry; no automatic runtime adoption. Accepted4/8;3A OPEN;R1 newly closed0/27;R47 immutable. Explicit prospective deviation: narrowly scoped current-containment validator; no deviation implemented.
