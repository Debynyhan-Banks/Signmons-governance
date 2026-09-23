# APP-013 / P06 R11 enabled21 refusal-class diagnostic

Status: consumed with zero matching records. No retry is authorized or planned.

## Demonstrated gap

Consumed request-log operation `2db28e8e-2d91-420e-8a6d-24d2413596e8` found exactly one enabled21 submit: HTTP 409 at `2026-09-22T17:29:46.796419Z` after 2.273183664 seconds. Together with zero jobs and zero address rows, this proves a synchronous pre-address current-state refusal. Request logs do not contain the sanitized application refusal class needed to distinguish customer-intake state change from current-verification refusal.

## Proposed operation

Operation `8cba60f6-f4e8-40ed-b201-6d09e09eb90c` will perform one read-only Cloud Logging query limited to project `signmons`, service `signmons-calldesk-staging`, exact revision `signmons-calldesk-staging-app013p06enabled21`, interval `2026-09-22T17:29:45Z`–`17:29:50Z`, and records containing `HTTP exception diagnostic`. It requires exactly one record and retains only one allowlisted refusal class, timestamp, HTTP 409 and count. It discards raw log text and does not retain request URL, body, headers, query parameters, phone, code, address, token, stack trace or provider content. Local syntax and parser review pass without executing the query.

## Boundaries

Approval authorizes exactly one query and no retry. It does not authorize database access, LOGIN change, activation, deployment, traffic change, provider request or mutation, verification code, browser/customer action, database write, job creation, request retry, hold release, secret/IAM change or billing change. R11 and full R12 remain open. No scope deviation.

## Result and source reconciliation

The operation ran once during the authorized 6:00–6:45 AM Eastern window on 2026-09-23 and returned `UNCONFIRMED` / `DIAGNOSTIC_COUNT` with count zero. It was not retried. Local source inspection explains the absence: `customerSessionHttp` owns `/customer-session/*` before Nest filters, `CustomerConsentBrowserTransport.handleBody` catches the exception and returns the allowlisted status, and the enabled runtime does not wire the transport's optional diagnostic callback. The global `SanitizedExceptionFilter` cannot emit the queried record for this route. The existing callback is status-only and cannot identify the internal refusal stage.

The earlier HTTP 409, zero-job and zero-address-row findings remain authoritative. The exact pre-address branch remains unknown. Another log query or unchanged browser run is not useful. See backend `evidence/APP-013/p06-r11-enabled21-refusal-class-result.md` and `APP013_P06_R11_CONTROLLED_REFUSAL_OBSERVABILITY_CHANGE_REQUEST.md`. No scope deviation implemented.
