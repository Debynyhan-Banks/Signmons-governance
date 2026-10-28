# APP-013 / 3A / P08 — same-day immutable operation renewal proposal

Status: PROPOSED; owner decision pending. R1-W01 / APP-013 / 3A / P08. Current backend source `4511b63487890f9bc437600225cc8c4f70fb634b`; current governance approval `3011370833bf76b16b75a36e07150c420cf6093a`. Local correction and isolated-test authority only if approved. No credential resolution, Google/provider request or change, API enablement, diagnostic, database/account/runtime action, Stripe/payment, deployment, spending, private plan or external operation is included.

## Approved section and connected finish

The approved section is APP-013 / 3A. Its unchanged acceptance criterion is an authentic same-job Stripe Sandbox payment and matching signed settlement for admitted job `9180bef4-561d-47a0-869f-925e6a3dfd96`. Stage A establishes the narrow current access facts required before Stage B/authentication can safely reach that connected payment path. This correction does not add a section, feature, acceptance criterion, dependency or denominator.

## Demonstrated gap

The October 28 Stage A attempt is consumed and its operation document must remain immutable. The corrected October 29 operation is approved but unstarted. The source-locked plan builder and launcher both accept only `APP013_P08_STAGE_A_OPERATION_YYYYMMDD.md`, leaving no unique valid filename for a fresh, separately approved October 28 operation. Using the October 29 filename for an October 28 window would misstate the operation date; rewriting the consumed October 28 document would violate immutable evidence.

This is a deterministic local filename-contract gap. It does not demonstrate a provider, billing, permission or product defect. No October 29 private plan has been created and no external request has occurred under that approval.

## Alternatives and recommendation

1. **Recommended: allow one explicit same-day renewal suffix while enforcing the filename date against the operation window.** Accept the existing unsuffixed form and `APP013_P08_STAGE_A_OPERATION_YYYYMMDD_RNN.md`, where `NN` is `01` through `99`. The first fresh October 28 renewal would be `_R01`.
2. Wait for the approved October 29 operation. This requires no local change but adds an unnecessary overnight delay.
3. Rewrite or reuse the consumed October 28 document. Refused because it would break immutable evidence and no-retry boundaries.
4. Put an October 28 window in the October 29 filename. Refused because the filename would no longer truthfully identify the operation date.

Alternative 1 is recommended. It preserves all existing document SHA, Git commit, owner decision, operation/decision UUID, source manifest, exact window, no-retry, private-plan and closeout checks.

## Exact local implementation card

Source SHA: backend `4511b63487890f9bc437600225cc8c4f70fb634b`. Reuse the evidence-only `launch_binding.py`, `plan_builder.py`, their 27 focused tests and the unchanged Stage A/access/restoration/authentication suites. The inspected missing behavior is the two exact unsuffixed filename regular expressions in those evidence-only sources.

In a fresh disabled evidence directory only:

- accept the legacy unsuffixed filename and an optional `_RNN` suffix with exactly two digits;
- require renewal numbers `01` through `99`; refuse `R00`, one/three digit forms, extra suffixes, path separators and alternate prefixes;
- parse the document date and require it to equal the `America/New_York` calendar date of `window.start`;
- require cutoff, work end, cleanup end and purge end to remain on that same Eastern calendar date;
- keep the existing one-hour maximum, ordered window, exact Git document read, SHA256, APPROVED owner decision, operation/decision IDs, source/manifest pins, project fingerprint, private permissions, one-use, purge and no-retry gates unchanged;
- make the plan builder and launcher consume one shared filename/date parser so their contracts cannot diverge;
- prove both the legacy unsuffixed document and `_R01` through the actual disposable-Git document to private-plan to unchanged validation path;
- prove date mismatch, cross-midnight window and malformed renewal filenames stop before private output;
- retain collision, race, signal, rollback, stale/foreign commit, hash drift and purge tests;
- prove native execution stays unbound and no gcloud, OAuth, HTTPS, credential-cache or provider adapter is invoked.

Expected files are confined to a new evidence directory containing copied disabled source, focused tests, source manifest, initial/final logs, verification and limitations. Existing consumed evidence, product source, operation documents and approvals remain unchanged.

## Verification, finish and rollback

Run the focused filename/date cases, then the existing 11 builder, 16 launcher, 24 Stage A, 40 access-model, 31 restoration and 60 authentication tests. Run backend architecture/cross-repository baseline/whitespace and governance frozen-baseline/consistency/25 safeguard/whitespace checks. Preserve initial failures without weakening assertions.

Observable finish is a disabled local builder/launcher copy that accepts an immutable `_R01` document only when its Eastern date matches the exact window. Native remains unbound. Rollback is deletion/reversion of the new evidence-only directory. A same-day external operation still requires a separately committed exact document and separate owner execution approval. That future approval must explicitly supersede and cancel the unstarted October 29 operation before any same-day attempt, preventing two live authorities.

## Dependencies, owners and exclusions

Debynyhan Banks decides this local correction. The implementer owns exact parser/date/test coverage. A later exact same-day document/approval owns its window, external requests and cancellation of the October 29 authority. Google owns provider behavior, which is untouched here.

Excluded: changing the 3A acceptance criterion; changing Stage A requests, retention, allowance or resource scope; rewriting consumed evidence; preparing a private plan; credentials/cache, gcloud, OAuth/bearer/HTTPS; API/IAM/key/account/database/runtime/Firebase/Stripe/payment/customer action; deployment, merge/push or spending.

Accepted 1A/1B/2A/2B, 4/8 walkthrough; 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. **Explicit same-day operational filename prerequisite proposed before implementation; no implemented scope deviation.**

## Owner decision

Debynyhan Banks replied “i approve” to the bounded same-day renewal correction and local tests against governance commit `867797572ebcad15d55fa9c0a3333a5914a51a21`. This authorizes only the disabled local implementation and verification described above. It does not authorize a private plan, credentials, provider requests, the proposed 5:30–6:00 p.m. operation, cancellation of the October 29 operation or any external action.
