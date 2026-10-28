# APP-013 / 3A / P08 — CLI failure observability local result

Status: LOCAL CORRECTION PASSED; EXTERNAL RETRY NOT AUTHORIZED. R1-W01 / APP-013 / 3A remains open.

Owner-approved Alternative 1 is complete at backend `0714c39`, based on governance approval `1fdddd0`. The disabled evidence helper now assigns every CLI call a fixed stage and classifies nonzero subprocess stderr in memory into only `AUTH`, `PERMISSION_DENIED`, `BILLING_OR_SERVICE_DISABLED`, `NOT_FOUND`, `INVALID_ARGUMENT`, `TRANSPORT`, `TIMEOUT` or `UNKNOWN`. Sanitized result evidence contains the stage and category only; raw stdout/stderr, account identifiers, bearer values and provider bodies remain unretained.

The 22-case fake subprocess/HTTP matrix passes, including actual `subprocess.run` serialization, all eight categories, unknown/private-message suppression, malformed-successful-output stage capture and the previously established exact calls, denial, collision, partial/lost ownership, signal, cutoff, concurrency, closeout and private-input purge controls. Source SHA256 is `7e5cbd4e6f68f42314bac2d12cd07cda33ed016986db646a61668d465871f430`. Architecture, frozen baseline, cross-repository consistency, 25 governance safeguards and whitespace checks pass.

No credential was resolved and no subprocess against gcloud, network/provider read, role create, IAM change, account/database/token/runtime/Stripe/payment action, deployment or spending occurred. Next observable result is a separately approved fresh exact operation or owner deferral. Counts remain 1A/1B/2A/2B accepted (4/8); R1 newly closed 0/27, legacy 6/60, intelligence 0/13. **No scope deviation.**
