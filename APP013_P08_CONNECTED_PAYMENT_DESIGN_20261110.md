# APP-013 / 3A / P08 — connected integration design inspection

Owner approved local proposal159b9e7 with “i approve”. Backend7d844ec,governance159b9e7. No runtime edits. Pre-change frozen baseline/complete consistency PASS. This is a design inspection,not a completed implementation card or readiness claim.

## Reuse map and locally resolved constraints

- Existing native_child.mjs calls boundClients and CoordinatorAuthSequence. The latter activates the exact app/Firebase identity,issues the token,authenticates,clears token,then closes. A payment phase must run while that same token/session exists and return to the existing independent cleanup;no second authentication lifecycle.
- Handoff.invoke_child currently caps child work at30seconds,captures stdout and requires an exact six-field authentication result. A human Checkout phase needs an explicitly bounded attended interval and a private local-browser bootstrap channel;printing bootstrap/token into a public result is excluded. Parent timeout/child process termination and independent cleanup must remain authoritative.
- Handoff._merge_child only accepts authClient's fixed field set and rejects parent drift. Payment state therefore needs an explicitly validated owned journal extension and source-manifest migration,not arbitrary extra journal keys. private_inventory currently owns only envelope/receipt as private files. Any qualification-to-native transfer must be registered with that same bounded custody/cleanup owner before another qualification is scheduled.
- operator-bridge.mjs already contains the attended browser UI,status/events/detail/bind/create/recover allowlist,stable request key,Origin/CSRF/size/deadline controls and private-session clear. Reuse this UI/API flow. Its plan points at the correct focused backend and same job/tenant/origin/account hash.
- normalizeDatabase supports controlled-v2 policy but assumes a CLOSED role and ACTIVE operator;that whole historical parser cannot be replayed unchanged after runtime restoration. Reuse its existing supported payment-policy profile and exact business checks at an explicitly declared phase;never fabricate roleClosed or actor status to satisfy it. Current full active/retired role validators stay required.
- Current native transports permit auth hosts and only GET dispatch detail. Payment routes,webhook lifecycle transport,typed response handling and finite counts require explicit versioned authority,not widening host access generically.
- No new application fee/routing/schema logic is needed. Existing job-policy binder,payment requests/recovery,Stripe Checkout provider and signed webhook handlers are the connected application seams. Existing role/account/amount/foreign-event/concurrency tests will be reused,with real local SQL/TLS and desktop/mobile browser composition proof.

## Material unresolved provider contract

Historical stripe-destination.json and stripe-final-readback.json establish only destination name,disabled status,Sandbox mode,connected-account scope,event hash and URL matching at October22. The retained screenshot shows the same name/URL/Disabled/No event deliveries found;it does not display object ID/type. No endpoint API family is proven by these artifacts. Current Q12 intentionally did not query Stripe destination metadata.

Official Stripe contracts differ: v1 webhook endpoints use POST /v1/webhook_endpoints/{id} with disabled; v2 event destinations use POST /v2/core/event_destinations/{id}/disable. The Dashboard label Event destinations alone does not select an API contract. Do not guess a v1 object from that label,create a replacement,change API version or implement both families speculatively.

Sources inspected November10: https://docs.stripe.com/api/webhook_endpoints/update and https://docs.stripe.com/api/v2/core/event-destinations/disable . These are public documentation reads,not account reads or provider qualification. They do not prove the existing object's kind or usable access.

Decision needed: permit the single existing-destination read-only browser inspection described in APP013_P08_STRIPE_DESTINATION_INSPECTION_20261110.md. It resolves actual object/API family and visible fixed contract for the connected card. If the UI does not expose enough evidence,report UNKNOWN and the exact missing field;do not silently escalate to API/secret reads.

## Next observable finish and boundaries

Local integration approval remains valid. After the provider contract is identified,implementer completes exact file/interface/task/test/call/time/retention/cleanup card BEFORE coding,then completes the already-approved local integration. No additional local-scope approval is requested. No implementation-ready claim until unresolved contract is resolved. No new recovery,qualification,password prompt or scheduled45minute session. Q12 successful historical observation and purge remain unchanged;its candidate is not retimed.

Completed source/interface/cleanup gap inspection. Remaining external fact:existing Stripe destination object/API family,owner/provider administrator. Remaining local deliverables:connected card,implementation,tests,exact separate live proposal. Remaining3A actual Sandbox/payment/webhook/failure-recovery/owner acceptance;accepted4/8,R1newlyclosed0/27. No scope deviation from approved local integration;external inspection proposed separately.
