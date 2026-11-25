# ED1 — specific webhook comparison reporting completed locally

APP-013 / 3A / P08. Backend implementation commit `5ea6fcb3bc897c195fb2311af9d5ddb75c958e13` completes the bounded ED1 correction described in proposal `77358d1` and `APP013_P08_ED1_LOCAL_DECISION_20261125.md`. **No scope deviation beyond the prepared ED1 correction.** No provider request, credential read, sign-in, endpoint change or payment occurred.

## Result

The existing one-request checker can now report eight fixed comparisons: object type, endpoint identity, Sandbox mode, URL, API version, exact enabled events, recognized status and disabled status. Each value is only MATCH, MISMATCH or TYPE_INVALID. It retains no raw endpoint values, secret, URL, event list, provider-derived hash or exception text.

Detailed reporting requires the explicit `--endpoint-once --field-report` option and OBSERVE input. DISABLE and VERIFY with that option refuse before dispatch. Ordinary calls retain their exact seven-key result, preserving the existing containment consumer. The same pure comparison function feeds the native endpoint predicate; optional status semantics, initial-disabled requirement, identity/pin checks and exact event-list equality remain intact. Reordered events pass; duplicates and missing/extra events fail.

The acceptance/refusal set is unchanged for decoded provider JSON and validated configuration pins. One malformed-input nuance is explicit: an event object with a non-callable `toString` previously threw TypeError while sorting; it now reports TYPE_INVALID and remains refused with PAYMENT_ENDPOINT_DRIFT. No rejected endpoint becomes accepted. Existing JSON.parse duplicate-member semantics remain unchanged.

## Verification and evidence

- 132 focused Node tests passed through the native/payment and key-check boundaries.
- 21 native transport tests, 52 key-correction Python tests, 151 native Python tests and 59 containment tests passed: **415 affected tests total**.
- Initial restricted loopback/process/TLS fixture failures are retained. Identical suites passed with the required local fixture permissions; no source or assertion was weakened to obtain those passing runs. The disposable TLS fixture confirmed its server was reaped and its temporary directory removed.
- All 25 governance tests, frozen baseline, full cross-repository consistency, backend governance wrapper, architecture and whitespace checks passed.
- Nine current manifests retain the same entry sets. 299 file references and three manifest-digest references verify; existing committed source guards pass against `5ea6fcb`. Historical receipts and R58's retained evidence hashes are unchanged.
- Independent review found no blocking issue and verified nine synthetic legacy CLI-to-containment-consumer combinations. Ordinary results remain seven keys; the old consumer still rejects extra fields, which is why reporting is explicit opt-in.

Evidence: backend `evidence/APP-013/p08-connected-packet-20261110/ed1-local-20261125/verification.json`, test logs, current manifest verification and committed-source-guard receipt. The change touches four existing source/test files plus nine derived current manifests. Owner AGENTS.md changes and unrelated historical artifacts are preserved. No application build, schema, hosted UI or browser behavior changed; production build, deployment, real database and actual-browser gates are not claimed as new evidence.

## Remaining work and next result

R58 is consumed and remains stopped before authentication or Checkout. Its exact mismatched field is **UNKNOWN**; ED1 does not reconstruct the discarded response. Current endpoint configuration and disabled status remain unverified.

The implementer next prepares the smallest source-bound, separately approved observation using this existing one-GET checker and hidden existing Sandbox inputs. A full connected workflow is not needed merely to identify the failing endpoint comparison. The Stripe custodian owns authorization for that observation and any subsequent configuration decision. No existing recovery, containment or R58 authority may be reused, and no new external operation is authorized here.

Remaining 3A acceptance is unchanged: the same admitted job's $99 Sandbox payment, authentic matching signed event, application gate clearance and owner acceptance. Accepted 1A/1B/2A/2B remain **4/8**; 3A OPEN; R1 newly closed **0/27**. Local implementation and testing are complete; live diagnosis and payment acceptance remain pending.
