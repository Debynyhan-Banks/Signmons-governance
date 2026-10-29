# APP-013 / 3A / P08 — Cloud false-fact observability proposal

Status: **Alternative 1 approved for local correction and testing only**. Debynyhan Banks replied “i approve” after review of this proposal at governance commit `2a77601`. R1-W01 / APP-013 / 3A / P08 remains active.

## Demonstrated gap

Approved operation R04 `63964638-5f31-4e5c-ad03-7f1226b1f80b` ran once at 9:46:44 a.m. Eastern and stopped `CLOUD_DRIFT`. It completed the Cloud domain after exactly 26 CLI reads, made zero HTTPS requests and zero qualification SQL statements, then completed one closeout-only SQL statement. Closeout qualified, residuals are empty and private inputs are absent. The attempt is consumed and no retry is authorized.

The Cloud classifier reduced thirteen allowlisted booleans to `DRIFT`, but the journal retained only that aggregate verdict. No raw Cloud output was retained, so the exact changed fact is unknown. Guessing at a parser or environment correction would be unjustified and could consume another no-retry window.

## Alternatives

1. **Recommended — safe false-fact names only.** In the disabled composed coordinator, after exact Cloud shape validation and before classification, retain only a sorted list drawn from the existing thirteen constant Cloud fact names whose value is exactly `false`, plus true/false counts. Never retain raw values, identifiers, provider bodies, hashes, policies or errors. Add tests proving allowlist-only output, malformed/extra refusal, no sensitive values, atomic journal behavior and unchanged verdict/closeout semantics. Run the focused/model, disposable PostgreSQL and all locked regression suites. No external read follows automatically.
2. Capture raw or hashed Cloud responses. Reject: it increases retention/privacy risk and is unnecessary to name a failed boolean predicate.
3. Defer. P08 remains stopped at unknown Cloud drift and no payment demonstration can proceed.

## Finite card and boundaries

- Approved section/criterion: existing 3A entry qualification for the admitted same job; no acceptance criterion or denominator changes.
- Source/evidence: backend `7fe401d` coordinator/launcher and R04 sanitized stop under `evidence/APP-013/p08-composed-qualification-r04-stop-20261029`.
- Files/interfaces: evidence-contained `composed_qualification.py`, focused tests, manifest/result/README and sanitized governance result only.
- Checklist: record allowlisted false names/counts only; reject malformed/extra Cloud shapes before observation; prove raw values cannot persist; retain atomic journal and closeout; run 33+ focused/model, PostgreSQL, role/restoration/access/authentication, baseline, architecture and whitespace gates; record result; stop before any operation.
- Retention/state: safe predicate names/counts only; no raw response, credential, provider/account/database state or private identifier.
- Exclusions: no gcloud/provider/database/Firebase read, retry, configuration correction, IAM/service/key/account/token/runtime/Stripe/payment action, deployment, spending, merge or push.
- Rollback/disabled state: revert only the local evidence-source commit; native execution remains impossible without a new exact plan and separate approval.
- Observable finish: safe false-fact evidence tests and all gates pass. This does not resolve the Cloud drift, complete P08 or accept 3A.

Owner decision: Alternative 1 is approved for local correction and testing only. This decision does not authorize another external operation. Accepted milestones remain 4/8; newly closed R1 0/27, legacy 6/60, intelligence 0/13. **Demonstrated observability gap disclosed; approved local correction only.**
