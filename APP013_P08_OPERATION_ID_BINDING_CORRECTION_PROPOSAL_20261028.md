# APP-013 / 3A / P08 — operation-ID binding correction proposal

Status: PROPOSED; owner decision pending. R1-W01 / APP-013 / 3A / P08. Backend stop evidence `c2b8053`; launcher source `d19df96`; governance operation/approval `571037f` / `cf0affb`. Local correction and isolated-test authority only if approved. No credential resolution, Google read/change, API enablement, permission diagnostic, API Keys, database/account/runtime, payment, deployment, spending or window is included.

## Demonstrated gap and unchanged acceptance

The approved 1:15 p.m. Stage A attempt returned `P08_STAGE_A_LAUNCH_REFUSED_UNBOUND` before credentials. Sanitized diagnosis: the launcher correctly requires the committed approved operation document to contain the exact operation UUID, but the private plan generated that UUID after the document was approved and committed. The synthetic local test used a document constructed from an already-existing synthetic plan, so it did not exercise the real document-first workflow.

Zero owner/Google commands, bearer requests or HTTPS requests occurred. No provider state or billing changed. The private plan was deleted and absence verified. The operation is consumed and must never be replayed.

The 3A acceptance criterion remains the authentic same-job Sandbox payment and matching signed settlement. This correction is one operational prerequisite, not a new section, feature or denominator.

## Alternatives and recommendation

1. **Recommended: add one deterministic disabled plan builder and actual Git-document integration tests.** Preselect the operation UUID in the proposed document before owner approval. After approval is committed, the builder reads that exact committed document, requires the operation/decision/source/window/retention fields, verifies `owner decision: APPROVED`, and copies the same UUID into the private plan. It never invents authority or accepts a post-approval UUID.
2. **Manually prepare another document and plan.** Smaller immediate change, but it preserves the untested handoff that caused this stop and conflicts with the owner's shift-left safeguard.
3. **Defer Stage A.** No provider risk, but P08 remains blocked.

Alternative 1 is recommended. The existing launcher/document binding remains strict; no check is removed or weakened.

## Exact local implementation

In a fresh evidence directory, reuse the exact launcher/source manifest from `d19df96`. Add one disabled `plan_builder.py` and isolated tests that:

- parse a proposed operation document containing preselected operation UUID, decision UUID, exact Eastern/UTC window, backend/source-manifest pins, owner/project/service/four tuples, no-retry, Stage B refusal and `RETAIN_IF_ENABLED`;
- refuse document status other than committed `APPROVED` and exact `owner decision: APPROVED`;
- use `/usr/bin/git show <full-commit>:<exact-document>` and verify the document SHA256 before private data is supplied;
- construct the plan by copying, never generating or replacing, the document's operation and decision IDs;
- require the already-established private project-number value to match the unchanged canonical fingerprint without printing or persisting it outside the private `0600` plan;
- write exactly one `0600` plan inside a new `0700` directory using exclusive creation; refuse collisions, symlinks, extra paths and existing files;
- reread through the real launcher's `private_json`, `validate_plan` and `verify_approval_document` functions before reporting local readiness;
- delete the synthetic private plan/directory and verify absence in every test, including failure, SIGINT/SIGTERM, clock rollback and collision paths;
- contain no gcloud, OAuth, HTTPS or provider adapter calls and prove zero network/host-credential access.

Tests must cover proposed/pending/rejected/changed documents; missing/duplicate/malformed operation IDs; UUID mismatch; decision/source/document/window/retention drift; stale/foreign Git commits and paths; project fingerprint mismatch; private permissions; reservation race; interrupted write; exact purge; and end-to-end successful committed-document → private-plan → launcher-validation using a disposable local Git repository.

Rerun the 16 launcher, 24 Stage A, 40 access-model, 31 restoration and 60 authentication tests. Run required backend/governance baseline, architecture, consistency, safeguard and whitespace checks. Preserve initial failures and limitations.

## Finish, rollback and boundaries

Observable finish: a disabled plan builder whose disposable-Git integration proves the exact sequence that failed, while native launcher execution remains unbound. This is implemented/local-tested only, not a live retry or permission verdict.

Rollback is deletion/reversion of the new evidence-only builder. The existing launcher and consumed stop evidence remain immutable. A fresh external operation needs a new preselected UUID, exact document/window and separate owner approval after the correction passes.

Dependencies/owners: Debynyhan Banks approves/refuses this local correction and later separately approves any fresh external operation. Implementer owns actual document/plan integration coverage. Google owns provider behavior, which is not touched here.

Exclusions: weakening document binding; changing the consumed document/plan; credentials/cache, gcloud, bearer or network access; service/API/IAM/key/account/database/runtime/Stripe/payment/customer action; deployment, merge/push, allowance or scheduling.

Accepted 1A/1B/2A/2B, 4/8 walkthrough; 0/27 newly closed R1, 6/60 legacy, 0/13 intelligence unchanged. **Unintended preparation drift disclosed and contained; explicit correction proposed before implementation.**
