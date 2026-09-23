# APP-013/P06 R11 enabled22 refusal-stage diagnostic

Status: consumed once during the owner-approved September 23, 8:00–8:30 AM Eastern window. One sanitized refusal-stage record returned. No retry.

## Exact bounded operation

One read-only Cloud Logging query in project `signmons`, resource type `cloud_run_revision`, service `signmons-calldesk-staging`, exact revision `signmons-calldesk-staging-app013p06enabled22`, historical interval `2026-09-23T11:47:00Z` inclusive through `2026-09-23T11:51:10Z` exclusive, restricted to `CONTROLLED_INTAKE_REFUSAL`. Limit 20 records, ascending time, one invocation, no automatic retry. This interval surrounds the locally saved Ready result (11:47:26Z) and verified closeout (11:51:02Z); filesystem save times bound the search and are not request timestamps. Proposed query execution window: September 23, 8:00–8:30 AM Eastern.

Filter:

```text
resource.type="cloud_run_revision"
resource.labels.project_id="signmons"
resource.labels.service_name="signmons-calldesk-staging"
resource.labels.revision_name="signmons-calldesk-staging-app013p06enabled22"
timestamp>="2026-09-23T11:47:00Z"
timestamp<"2026-09-23T11:51:10Z"
"CONTROLLED_INTAKE_REFUSAL"
```

Retain only timestamp, operation `submit`, status 409, counts, and exactly one of `INTAKE_STATE_CHANGED`, `LIFE_SAFETY_REFUSAL`, `CURRENT_VERIFICATION_UNAVAILABLE`. Parse the exact fixed marker from `src/communications/controlled-intake-refusal.ts`; discard raw text and all other fields. Keep raw response only in process memory, never display or persist it. Zero/multiple stages, malformed records or a saturated limit are inconclusive, not permission to infer a cause or rerun.

This image newly wires the fixed marker into the controlled browser transport. A marker identifies a refusal stage; it does not independently prove job count, provider outcome or a complete root cause. Use the observed stage to narrow existing local source analysis before proposing any repair. Do not schedule another browser attempt merely because the query finishes.

## Authorization boundary

One query only. No database access, LOGIN, activation, deployment, traffic change, provider request or mutation, verification code, browser/customer action, database write, job creation, request retry, hold release, secret/IAM or billing change. No new packet or capacity increase. Current runtime is already verified closed. Preparation is local documentation only; execution requires owner approval of this query/window. No scope deviation.

## Result and source mapping

The one approved query returned exactly one fixed marker at `2026-09-23T11:50:24.943550Z`: operation `submit`, HTTP 409, stage `CURRENT_VERIFICATION_UNAVAILABLE`. No raw log was displayed or retained. No other query or external action was performed.

Local source review maps this stage to the verification service and its final consumption checks. It covers current phone-proof eligibility, submission/session/policy checks, and post-address observation/final-commit checks; the caller also assigns it to otherwise untagged 409s from that promise. Therefore this marker alone does not prove phone expiry, address failure, exhausted capacity, a specific database mismatch, or no committed job. It does not justify another browser attempt or a higher ceiling. The deployed session is closed and the exact request stays preserved.

Next is bounded local source/fixture analysis of these existing checks; if current private state is indispensable, prepare one consolidated decision before any additional read. Do not implement a speculative fix, expand logging, or schedule another live run on the basis of this coarse stage. P06 remains 12/14 with R11/full R12 open. No scope deviation.
