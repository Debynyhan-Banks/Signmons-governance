# APP-013 / 3A / P08 — IAM Role etag output-contract correction proposal

Status: ALTERNATIVE 1 OWNER APPROVED FOR LOCAL CORRECTION AND ISOLATED TESTS. R1-W01 / APP-013 / 3A remains unchanged.

Owner decision: Debynyhan Banks approved Alternative 1 in the governed conversation on October 28, 2026, against this document's pre-decision SHA256 `86329f669cad87d075513cf0178e3f297035c374a34fcd761ab09203b0d73f12`. Approval covers only the five local steps below. It does not authorize a provider call, retry or new external operation.

## Demonstrated gap

Fresh approved operation `9725da4a-51e7-439d-aa79-fe48c62229dc` ran once at 6:30 p.m. Eastern. All three allowed CLI reads and the one exact IAM FULL-view HTTPS read completed. The strict parser stopped with sanitized reason `ROLE_SHAPE`; private inputs are absent, raw output/bearer were not retained and provider mutation was impossible. Backend evidence: `evidence/APP-013/p08-role-inventory-r02-stop-20261028/`.

The existing parser allows `name`, `title`, `description`, `includedPermissions`, `stage` and `deleted`. Google's documented IAM `Role` response also includes `etag`: <https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles>. The provider response is unavailable by design, so the smallest evidence-backed correction is to accept documented nondecision `etag` only, validate that it is a string when present and discard it before classification/evidence. Unknown fields must continue to fail closed.

## Alternative 1 — recommended local correction

In a fresh disabled copy of the evidence-contained qualifier only:

1. add optional `etag` to the exact allowed response-field set;
2. require a present `etag` to be a string and discard it before role classification, candidate hashing and saved evidence;
3. retain all existing role-name, permission, stage/deleted, page, redirect, host/path/query, bearer/raw-output, deadline, signal, one-attempt and private-input controls;
4. add positive coverage for documented `etag`, negative coverage for non-string `etag` and continued refusal of an unknown field;
5. run the full isolated qualifier suite and required repository gates.

No provider call, retry or new operation is included. After local proof, a later exact read-only operation requires a fresh ID, window and separate owner approval.

## Alternative 2 — stop

Leave exact role candidates unknown and keep Stage A access resolution blocked.

## Boundaries and impact

This proposal does not authorize an API/service enable, IAM role or binding action, Firebase action, signing/token exchange, API-key action, database/identity/secret/tag/runtime action, deployment, Stripe/payment, customer action or spending. It adds no section, acceptance criterion or dependency and does not resolve the separate exchange-key incompatibility.

Owner decision requested: approve Alternative 1 for local correction and isolated tests only, or choose Alternative 2. Accepted counts remain unchanged. **No scope deviation.**
