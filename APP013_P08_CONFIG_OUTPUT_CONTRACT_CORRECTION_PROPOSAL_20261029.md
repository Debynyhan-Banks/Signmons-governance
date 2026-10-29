# APP-013 / 3A / P08 — gcloud config output-contract correction proposal

Status: **Alternative 1 approved for local correction and testing only**. Debynyhan Banks replied “i approve” after review of this proposal at governance commit `3c69b16`. R1-W01 / APP-013 / 3A / P08 remains active.

## Demonstrated gap

Approved operation R02 `56e8b2e6-58ec-46fc-9ba0-c4cbc74918ac` ran once at 8:47:57 a.m. Eastern and stopped at `CONFIG_OUTPUT`. The controller had completed its exact 26 gcloud metadata reads, had made zero HTTPS requests and zero qualification SQL statements, and then completed one closeout-only SQL statement. Journal closeout is `QUALIFIED`, residuals are empty and the private plan/binding are absent. The attempt is consumed and no retry is authorized.

The local parser currently requires the projected config object to have exactly top-level `core` and `auth`, then requires `auth` to be empty. Installed primary `gcloud config list --help` states that the command lists set properties unless `--all` is used. An unset projected `auth` section may therefore be omitted. The sanitized attempt did not retain raw config output, so the exact observed shape is not claimed.

## Alternatives

1. **Recommended — narrow safe-shape normalization.** In the disabled qualification source only, accept exactly `{"core":{"project":"signmons"}}` or the existing `{"core":{"project":"signmons"},"auth":{}}` as override-absent. Continue rejecting every nonempty `auth`, wrong/missing project, extra top-level/core field, scalar/list/malformed/oversized value and credential environment override. Add a fixed safe shape classification to future sanitized evidence, plus positive/negative fake tests. Run the existing 30-case qualification suite, disposable PostgreSQL proof and unchanged role/restoration/access/authentication regressions. No external read follows automatically.
2. Replace the single projection with multiple config-property commands. This changes the exact 26-command contract and expands the external surface; reject for this correction.
3. Defer. P08 remains stopped at current-state qualification and no payment demonstration can proceed.

## Finite card and boundaries

- Approved section/criterion: existing 3A entry qualification for the admitted same job; no acceptance criterion or denominator changes.
- Source/evidence: backend `1125d17`; `qualification_launch.py` config parser; sanitized R02 result under `evidence/APP-013/p08-composed-qualification-r02-stop-20261029`.
- Files/interfaces: the evidence-contained launcher, its focused tests/manifest/result and sanitized governance result only.
- Checklist: add the two exact safe shapes; reject all other shapes; prove environment overrides still refuse; prove no output values enter evidence; run focused, PostgreSQL, locked regression, baseline, architecture and whitespace gates; record result; stop before any new operation.
- Tests: omitted-empty-section positive, explicit-empty positive, nonempty-auth, wrong/missing project, extra keys, malformed/oversized, signal/deadline/closeout and unchanged full locked suites.
- Retention/identity/state: no raw config output retained; no credential/provider/account/database state change; R02 receipts remain immutable.
- Exclusions: no gcloud/provider read, retry, database/Firebase read, IAM/service/key/account/token/runtime/Stripe/payment action, deployment, spending, merge or push.
- Rollback/disabled state: revert only the local evidence-source commit; native execution remains impossible without a new exact plan and separate approval.
- Observable finish: exact safe-shape tests and all gates pass with a sanitized local result. This does not complete P08 or 3A.

Owner decision: Alternative 1 is approved for local correction and testing only. This decision does not authorize another external operation. Accepted milestones remain 4/8; newly closed R1 0/27, legacy 6/60, intelligence 0/13. **Demonstrated output-contract drift disclosed; approved local correction only.**
