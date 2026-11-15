# APP-013 / 3A — actual SDK message serialization review

Local review authorized by owner proceed after IQ4/IQ5. No provider/account/cache action, code change or support contact. Baseline backendc63cf71, governanced18afdd. Historical live IQ5 explicit disabled observation remains historical, not refreshed.

The prior plain-dictionary printer probe did not cover the SDK response-message decoding step. This review exercised the installed apitools.base.py.encoding.JsonToMessage with the actual generated IAM v1 ServiceAccount type, then googlecloudsdk.core.resource.resource_printer.Print(single=True), for both actual formats json(email,disabled) and json(email,disabled,uniqueId). Synthetic identity only, pinned Python -I -B -S and installed SDK lib/third_party imports; no CLI/client creation or network transport.

| Synthetic provider JSON | Both actual projected outputs |
| --- | --- |
| disabled:true | Field present; boolean true |
| disabled:false | Field present; boolean false |
| disabled absent | Field absent |
| disabled:null | Field absent |

Eight cases passed these observations. Installed resource_projector converts the SDK protorpc message through MessageToDict. Installed Describe.Run obtains an IAM client then invokes projects_serviceAccounts.Get; this reviewed command has no explicit state-cache lookup. This limited source inspection is not a proof of no caching anywhere in the transport/provider.

New conclusion: IT1 MISSING describes emitted SDK JSON, not the original provider wire value. Provider omission and explicit null are indistinguishable after this tested decoder boundary. Earlier dictionary-only null preservation evidence did not establish behavior for real SDK messages. IQ4's true-then-missing difference cannot be explained merely by adding uniqueId to a projection when both inputs contain the same explicit true value. Both projections preserved explicit true in this local test. The actual wire payload remains unavailable, so original cause stays UNKNOWN; tests do not recreate IQ4 or prove its provider state.

No justified patch follows from this result. In particular, do not change missing/null to disabled:true, remove final UID/state confirmation, or count earlier true as successful final closure. IQ5 independently confirmed disabled later, resolving current restoration uncertainty only. Likewise the historical enabled predicate's missing-as-false behavior is unchanged, not newly validated as usable access.

## Next in-house decision

The remaining evidence gap is before SDK message decoding. A useful future diagnostic must distinguish raw IAM response field presence/type from projected SDK output for the same response, with only fixed flags/timing/identity-match retained. Another unmodified run or new current-state read cannot supply that missing historical information. Merely adding a wait does not answer this question.

Before implementation, prepare a narrowly scoped design for observing that single response boundary using the installed SDK's existing transport/message seams, preserving its authentication, request count, source guards, cleanup and secret suppression. It must prove locally that no headers, tokens, raw body or arbitrary exception text escapes; it must not introduce a second independent API request and then claim it was the same response. If that cannot be achieved within a bounded existing seam, report that concrete design blocker instead of adding a general logging framework. This document does not authorize a monkeypatch, SDK edit, new HTTP client, extra provider call, evidence-retention change or live run. Owner approval must precede such implementation under repository change-control rules.

Completed: eight actual message-decode/projection cases and source review. Responsible implementer owns the exact bounded design; owner retains implementation/live decisions. No attendance, sign-in/password or support involvement required for design work. Existing IQ1–IQ5/AL1 receipts remain immutable; R47 history unchanged.

Accepted1A/1B/2A/2B remain4/8;3A OPEN;R1 newly closed0/27. Remaining identity prerequisite/current account entry, authenticated same-job Sandbox payment/event/application recovery, cleanup and owner acceptance are unchanged. No scope deviation; local review only.
