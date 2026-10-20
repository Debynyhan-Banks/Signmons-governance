# APP-013/P06 R11 correction-continuation zero-traffic readiness proposal

Status: decision-ready. No database, Cloud Run, Twilio, address-provider, browser or customer action occurred during preparation.

## Section and acceptance traceability

Section: existing APP-013/2B, P06-R11. The unchanged criterion is one protected journey that obtains current phone and eligible-address evidence, preserves the reviewed draft and creates exactly one job only through controlled admission. The new immutable image contains the locally verified cross-instance correction continuation. This proposal advances only deployment/readiness evidence; it cannot accept R11 or authorize a journey.

Source/image: archive SHA-256 `48ea0a9bb31c439a1fa5f1f8e543c4ecc582edfb21a9e8e741ca2d652b7911e1`; Cloud Build `44569641-ba52-4302-bb02-e4194006c979`; image `us-east5-docker.pkg.dev/signmons/signmons/signmons-calldesk-backend:p06-r11-cont-48ea0a9bb31c`; immutable digest `sha256:69ef032639e5dcfa2bcaaa5d88d0e438ec62903f08cb44fc5572af1209e332d3`.

## Liability reconciliation before deployment

The last direct-child read-only receipt was the pre-enabled39 baseline: 17 phone holds / USD8.50 and nine address operations / USD0.90. Enabled39 then completed the approved phone step and reached address correction before terminal `ADDRESS_CORRECTION_STATE_UNAVAILABLE`. Its decision records that the approved 18th phone hold / USD0.50 deviation was exercised. The correction screen also implies one initial address operation, but no post-enabled39 aggregate receipt exists.

Therefore **17/USD8.50 is stale and must not be used as current state**. Expected state for a new read-only refresh is 18 phone holds / USD9.00 and 10 address operations / USD1.00 at both account and tenant, invalid rows zero, approvals inactive, runtime role `NOLOGIN`, connection limit zero and sessions zero. This is an evidence-derived expectation, not a substitute for the refresh. Any mismatch stops before mutation and returns to owner review.

The owner separately reports a current Twilio cash balance of USD8.38. That balance is not the same as internal retained-liability ceilings and has not been independently read. This proposal performs no Twilio metadata read, request, code, message or transaction, so it spends none of that balance.

## Alternative 1 — one zero-traffic readiness deployment

After explicit owner approval of this alternative, the USD2 Cloud/runtime operational allowance and a future 60-minute Eastern window:

1. Prepare a fresh one-use controller with new plan/operation identities, exact image/digest, target `signmons-calldesk-staging-app013p06enabled40`, fixed normal revision `signmons-calldesk-staging-app013dbrot2`, exact window and mandatory closeout. Target/tag absence and current normal routing remain fresh preflight facts, not assumptions.
2. The owner enters the saved child `neondb_owner` password through hidden input. Run exactly one direct-child `REPEATABLE READ READ ONLY` transaction for fixed liability aggregates plus approval/runtime-role/session classifications. Read no customer, request, job, phone, address or provider payload. Roll back and close. Require exactly 18/USD9.00 phone, 10/USD1.00 address at account and tenant, invalid zero and fully closed runtime; otherwise stop.
3. Run a read-only Cloud preflight: service `signmons-calldesk-staging` in `us-east5`; normal traffic 100% on `app013dbrot2`; enabled tag absent; enabled40 absent; exact image digest present; controlled-material version1 and child-database version2 enabled; current runtime identity and service limits unchanged. Do not inspect Twilio.
4. Build an execution-disabled runtime envelope from the fresh receipt. Bind phone account ceiling to exactly the refreshed retained amount and address account/tenant ceilings to exactly the refreshed retained amount, leaving no new provider-operation headroom. Retain the schema-required browser `starts:1` value, but zero traffic, no route request and exhausted provider ceilings prevent its use. The envelope exists only to prove startup/readiness, never to serve a journey.
5. Open only the limited child runtime role, activate the exact short-lived runtime approval and deploy exactly one revision `app013p06enabled40` with the immutable image, `--no-traffic`, temporary `p06-intake-enabled` tag, all six non-target flags literal `false`, and explicit secrets `CONTROLLED_INTAKE_SECRETS_JSON=signmons-staging-controlled-intake-material:1` plus `DATABASE_URL=signmons-staging-p06-child-database-url:2`.
6. Require Ready condition true, exact image digest, exact flags/secrets/runtime envelope, target traffic zero and normal traffic still 100% on `app013dbrot2`. Make no HTTP request to the candidate route and run no browser journey.
7. Immediately revoke approvals, remove the enabled tag, restore child runtime `NOLOGIN` / connection limit zero / sessions zero, confirm the envelope expired or inactive, and read back normal traffic unchanged. Closeout runs after every success, stop or uncertainty. Preserve one sanitized result; no automatic retry.

Observable finish: one ready zero-traffic revision with exact image/config evidence followed by verified closed state, or one preserved safe stop followed by verified closed state. Either result leaves the image/revision unused and changes no acceptance count.

## Alternative 2 — pause

Keep the image unused. Perform no database or Cloud Run action and spend no Twilio or Cloud runtime allowance.

## Data, cost, recovery and exclusions

Private database input remains hidden and unsaved. The fixed read-only refresh returns counts, micros and boolean classifications only. Activation/revocation writes only bounded approval/runtime-role state required for startup and closes it in the same operation. Cloud Run writes one zero-traffic revision and temporary tag; the tag is removed during closeout. No source build or IAM grant is required.

Requested allowance: USD2 for Cloud Run deployment/runtime only, an operational limit rather than a provider-enforced billing cap. Twilio allowance: USD0. Address-provider allowance: USD0. Phone/address operation headroom: zero. No actual Twilio balance read is authorized.

Positive checks: exact liability/closed-runtime refresh, exact Cloud baseline/image/secrets, one ready zero-traffic revision, normal routing unchanged and terminal closed state. Negative/recovery checks: wrong password/target/count/image/secret/tag/routing/window stops; activation or deployment uncertainty triggers closeout; readiness mismatch permits no second deployment; cleanup ambiguity blocks every later action.

Excluded: Twilio account access, provider metadata, phone START/CHECK/resend, SMS/code/message, address-provider call, browser request, customer/job action, traffic shift, payment/booking/dispatch, schema/migration, secret payload/version change, IAM change, build, hold release/reset/exclusion, ceiling increase, deployment retry and live acceptance.

Owner decision: approve Alternative1, the expected 18/USD9.00 phone and 10/USD1.00 address refresh gates, one zero-traffic enabled40 deployment, bounded child-database activation/closeout, USD2 Cloud/runtime allowance, USD0 Twilio/address allowance, no retry and a future 60-minute Eastern window; or choose Alternative2.

P06 remains12/14; R11/fullR12 remain open; accepted milestones remain3/8. No scope deviation.

## Approved package — October 11

The owner approved Alternative1, the exact18/USD9.00 phone and10/USD1.00 address read-only gates, one enabled40 zero-traffic deployment, bounded child-database activation/closeout, USD2 Cloud/runtime allowance, USD0 Twilio/address allowance and no retry for10:00–11:00a.m.Eastern.

Fresh plan `845f222d-f3c5-48d8-b2d6-4947bc1afea9`, packet `9cfe5009-477d-40a8-834b-28542dcf1c78`, eight operation identities and exact window bindings are installed at `/private/tmp/r11-correction-readiness-20261011-1000`. The immutable image/archive/build bindings pass. The execution source is an extracted copy of the reviewed archive; its build passes. Packet review binds runtime digest `0ea5538607f389a4e1bca5ab9e698293b9b81efe1a86043e76f46c2b8b5e9297` and phone digest `101651f598590220d37802ee0faed377d6ddc7bd8a7f76be579f5c958f9e2eda`.

The package check proves one deploy command, `--no-traffic`, enabled40, no candidate fetch, no Twilio command, exact18/9,000,000 and10/1,000,000 gates and no existing action markers. All26 controller containment tests pass. The one-command private coordinator prompts once for the saved child password, opens the bounded role, waits for the15-minute runtime window, deploys/readies once, then closes immediately; run failure still attempts closeout. No action has begun. Owner invokes the exact command once at or after10:00a.m. and before the package's start reserve is exhausted. Any stop or uncertainty consumes the package; do not rerun.

No scope deviation.

## Executed readiness outcome

Fresh corrected plan `5574d146-58d5-4340-aa2c-0e28d488f426` / packet `af8bcc76-a04b-4e40-a703-9d24c200a99b` completed once. Exact read-only baseline matched18/USD9.00 phone and11/USD1.10 address. Activation/readback passed, enabled40 became `READY_NO_TRAFFIC` from immutable image `sha256:69ef0326…32d3`, target traffic remained0 and normal traffic remained100% on `app013dbrot2`.

Mandatory closeout returned `CLOSED` with failures empty. Approval revocation/readback passed, the enabled tag was removed, runtime role closeout passed and no session remained. Independent Cloud metadata confirms enabled40 is the exact image, container healthy/Ready and retired after tag removal; only `app013-bounds` receives100% traffic. No HTTP candidate request, browser journey, Twilio/address-provider call or customer/job action occurred. The package is consumed; never rerun.

Zero-traffic readiness is complete. R11 remains open because the customer journey was intentionally excluded. The embedded runtime envelope is expired, so enabled40 cannot be reused for a later journey; a fresh time-bound revision is required. P06 remains12/14; R11/fullR12 remain open; accepted milestones remain3/8. No scope deviation.
