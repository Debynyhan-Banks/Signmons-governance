# APP-013 / 3A / P08 — bounded access-fact observability proposal

**Status: owner decision requested; no implementation or external read authorized.** Section R1-W01 / APP-013 / 3A / P08. R09 safely stopped `ACCESS_UNKNOWN` after Cloud 13/13 and completion of the access domain. Mandatory read-only closeout/private-input purge verified. Backend receipt `f52b99f`. R09 is consumed/no retry. The current sanitized journal omits which already-allowlisted service, permission or key-absence fact caused UNKNOWN, so another full read without safe observation would be blind.

## Alternatives

1. **Recommended — local-only fixed access-fact observation.** In a fresh disabled copy of backend `31e25cd`, reuse the existing `cloud_observation` pattern for the access domain. After strict shape validation, retain only sorted names drawn from the six fixed service names and existing permission allowlist whose values are `UNKNOWN` or `DENIED`, fixed disabled-service names, and the fixed `keyAbsence` enum. Record counts and existing `rolesExact`/`bindingsAbsent` booleans. No raw response, URL, bearer, resource identifier, policy or dynamic account data. Keep classification and all reads unchanged. Test injected unknown/denied/disabled/present/qualified/malformed cases and journal privacy. No real provider read under this approval; a later operation needs separate exact owner approval.
2. **Defer for provider/account-owner investigation.** Keep P08 stopped with R09's verified containment. The current receipt does not identify a specific permission or service.
3. **Repeat R09 or broaden UNKNOWN into success.** Reject. R09 is consumed and unknown access does not qualify payment readiness.

## Finite Alternative 1 card

- **Source/criterion:** backend `31e25cd`, `evidence/APP-013/p08-service-state-projection-local-20261029/source/composed_qualification.py` at `classify_access`, `cloud_observation`, `Coordinator.run`, and its focused/model/launcher tests. Existing P08 current-state criterion requires exact enabled services, granted permissions, absent key and exact roles/bindings before the admitted job's 3A Sandbox payment path. Inspected gap: `ACCESS_UNKNOWN` has no safe fixed-fact identity in journal.
- **Expected files/interfaces:** one fresh disabled source/test/evidence copy. Add one bounded access observation to sanitized journal after shape validation, before access verdict; do not alter `read_access`, provider descriptors, acceptance, call ceilings, parser, cap, source/approval/window bindings, no-retry, closeout or private purge. Existing launcher stays unbound.
- **Data/identity/retention:** fakes only. Observation values must be selected from compile-time service/permission allowlists and fixed enums/booleans, with maximum lengths/counts checked. No raw body, exception, account/tenant/job/UUID, bearer or password in output. Existing retention/purge behavior remains.
- **Finite tests:** each service/permission unknown, denied and disabled; key denied/unknown/present/not found; roles/bindings drift; all-qualified, malformed/foreign names, duplicate/extra fields, journal privacy; unchanged positive/negative/concurrency/recovery/signal/deadline/closeout tests; predecessor regression, disposable PostgreSQL tests, source-lock/manifest, architecture, governance baseline/consistency/tests and both whitespace gates. Browser not applicable to backend metadata observation. Finish is local observability only, not live P08/3A acceptance.
- **Dependencies/owner/rollback:** Debynyhan Banks decides this local correction before implementation; implementer discards the fresh disabled copy on failure. Any later provider read requires a new exact card/window and separate approval. No provider state to roll back.
- **Exclusions:** no API enablement, IAM/secret/key/account/database business mutation, authentication/signing/token exchange, runtime restoration/deployment, Stripe/payment, booking/customer action, spending, merge or push.

**Impact:** no section/count, acceptance criterion, dependency, request ceiling or allowance change. R09 cannot be diagnosed retrospectively. **Proposed deviation only; none implemented.**

**Owner decision requested:** approve Alternative 1 for bounded local correction and isolated tests only, or defer.
