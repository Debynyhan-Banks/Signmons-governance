# APP-013 / 3A — CT1 supplied-response composition specification

LOCAL SPECIFICATION ONLY. Authority: CT1 local proposal and approval c14934b. Source pins: backend account-containment-source-manifest.json (40 files); baseline1f8fa97. No executable reader, credential access or live packet is delivered by this specification.

## Data flow and exact interfaces

A future separately authorized operation would bind a new canonical operation UUID to historical operation bea4fe6b-2202-48ed-9df1-84a17d23fcd8, journal SHA256 7ea07c21fdc737f671a025de9b44980b2771ddbe9cfdd02cfdb26b9063c5323f and revocationIntentAt 2026-11-14T19:22:30.000Z. The historical safe journal bytes are an immutable reference, never execution authority.

Reuse qualification_launch.py sql_contract()[0] and NativeIO.sql for the single existing read-only account/session query. Pass its original serialized response as database={operationId,body}. Preserve explicit counts and exact row fields. Its operator UUID stays in process memory; the fixed production TARGET_SHA256 must match before using that UUID. Database sessions means only the existing query's matching pg_stat_activity connections, excluding its own PID.

Reuse firebase_https_contract(validatedUUID) and NativeIO.https: POST https://identitytoolkit.googleapis.com/v1/projects/signmons/accounts:lookup with localId array containing that UUID. Pass the original response as firebase={operationId,status,body}. CT1 parses the supplied REST fields, strictly decodes customAttributes and converts explicit validSince seconds to the existing exact_firebase timestamp interface. Missing fields are never defaulted. No second response or shared cutoff modification is permitted.

Call account_containment.validate(binding,database,firebase,historicalJournalBytes). Only fixed status/boolean flags and historicalAuthentication=UNKNOWN may be retained. The internal _payloads test seam is not a production API or authority source. Production validate pins the real target digest and historical journal. A confirmed value describes supplied observations; provenance/freshness and live custody must be established by a future approved composition. It does not prove historical authentication, global token invalidation or payment acceptance.

## Proposed finite future read budget — not authorized

Maximum three CLI reads: existing owner and project descriptors, then existing gcloud auth print-access-token descriptor. The last is an explicit credential read into memory and must be named in a future approval with SDK refresh/retry/cache effects. One account SQL read, one Firebase lookup, and one independent existing SQL session-closeout read. No credential persisted, raw response logged, account mutation, token revocation, identity activation, key action, payment, support contact or automatic retry.

The existing NativeIO boundaries provide descriptor checks, deadlines, response caps, TLS and process-close interfaces. They do not by themselves constitute an approved composed runner. Before any live packet: implementer must demonstrate exact executable invocation, one-attempt reservation, source/resource pins, owner/project identity, deadline and budget enforcement, memory-only token/password custody, interruption handling, independent closeout and purge through existing interfaces. No new runner is authorized by CT1. If an executable composition requires additional implementation, present that smallest bounded gap for decision first.

## Readiness record — local only

Inspected source baseline1f8fa97; checks/evidence dated2026-11-15. Actual SQL parser and exact account/Firebase validators are invoked in synthetic tests; timestamp, null/missing fields, strict JSON, foreign identity and operation isolation are covered. Source manifest pins transitive existing modules and immutable R47 journal/result. Local verification establishes parsing behavior only.

Current credentials, permissions, API response, account state, database sessions and Firebase revocation cutoff: UNKNOWN; owner/cloud/DB custodians own future external authority. Live deadlines, process composition, token custody and cleanup execution: NOT YET QUALIFIED; implementer owns completing the executable-readiness review without provider calls. No attendance requested. Next observable result is an exact composition feasibility/readiness review, or the smallest demonstrated implementation gap. Current containment and R47 historical authentication remain UNKNOWN.

Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1 newly closed0/27. No scope deviation beyond approved CT1.
