# APP-013 / 3A / P08 — bounded Service Usage output-category proposal

**Status: owner decision requested; no code change or external read authorized.** Section R1-W01 / APP-013 / 3A / P08. R07 safely stopped at `HTTPS_OUTPUT:service_1` after Cloud 13/13 qualified; closeout and private-input retirement verified. The fixed descriptor is the `iam.googleapis.com` Service Usage state read. Current sanitized evidence cannot distinguish oversized output, invalid UTF-8 or malformed JSON. Backend receipt `4f23b23`; R07 is consumed/no retry. This is a prerequisite diagnosis for the same admitted job's 3A payment-readiness path, not a new section or accepted capability.

## Alternatives and decision

1. **Recommended: bounded local-only response-category observation.** In a fresh disabled copy of backend `9888e7c`, preserve the exact ten-request allowlist and existing parsing refusal. For `HTTPS_OUTPUT` only, record a fixed non-sensitive category (`OVERSIZE`, `INVALID_UTF8`, or `INVALID_JSON`) alongside the existing fixed request ID. Record no bytes, length, status body, URL, bearer, raw exception or dynamic identifier. Prove each category using injected fake responses and verify journal privacy, no retry, deadline/signal cleanup and mandatory closeout. No real provider request under this approval. A later fresh exact read-only operation would require its own owner approval and window.
2. **Defer and investigate with the provider/account owner.** Leave P08 stopped and retain the verified R07 containment. This avoids another local change but does not narrow the malformed-output cause.
3. **Repeat R07 or accept unparsed response as success.** Reject: R07 is consumed, and an unparsed response cannot prove the IAM service enabled state. Do not weaken the gate.

## Finite Alternative 1 card

- **Source and criterion:** locked backend `9888e7c`, `evidence/APP-013/p08-https-output-observability-local-20261029/source/qualification_launch.py` at `NativeIO.https`, `bounded_json` and `Adapter._https`, with its focused launcher/coordinator tests. Existing P08 current-state acceptance requires exact enabled-service and permission facts before authentication/runtime qualification. Inspected missing behavior: `HTTPS_OUTPUT:service_1` identifies the request but not a safe response failure category.
- **Expected files/interfaces:** one fresh disabled source/test/evidence copy only; existing launcher CLI and `HTTPS_OUTPUT:<ID>` syntax gain one fixed category field in the sanitized journal. Preserve all operation/source/approval/clock bindings, 26 CLI/ten HTTPS/two SQL ceilings, USD0, one-use/no-retry and strict JSON gate. No application runtime or old receipt edits.
- **Data/identity/retention:** fake provider responses only; no real bearer, CHILD password, Firebase ID or database data. Test persistence excludes payload bytes and raw exceptions. Exact private-input deletion and absence readback remain mandatory if a later operation is separately approved.
- **Finite checks:** injected oversized, invalid UTF-8, malformed JSON and wrong-shape output; normal JSON; unknown descriptor; no leak in journal; positive/negative/recovery/concurrency and signal/deadline cases; unchanged original regression; disposable PostgreSQL cases; architecture, governance baseline/consistency/tests and whitespace gates. Browser is not applicable to this backend-only metadata parser; no UI behavior changes. Finish is a locally verified safe category, not P08 or 3A acceptance.
- **Dependencies/owner/rollback:** Debynyhan Banks must choose this local correction before implementation. Implementer may discard the new disabled copy on failure. Separate exact approval is required for any later Cloud/HTTPS/database read. No provider state exists to roll back.
- **Exclusions:** no API enablement, IAM/secret/key/account/database business mutation, authentication/signing/token exchange, runtime restoration/deployment, Stripe/payment, booking/customer action, spending, merge or push.

**Impact:** no change to section IDs, acceptance denominator, dependency order or external allowance. It may produce one additional local iteration; it does not explain the consumed R07 result retrospectively. **Proposed deviation only; none implemented.**

**Owner decision requested:** approve Alternative 1 for bounded local correction and isolated tests only, or defer for provider investigation.
