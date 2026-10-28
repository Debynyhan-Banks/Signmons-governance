# APP-013 / 3A / P08 — corrected role-inventory R01 stop result

Status: CONSUMED STOP; containment verified; role facts unknown.

Fresh owner-approved operation `7212ade4-3500-421f-832b-d9738eb0b324` ran once at 6:15 p.m. Eastern on October 28 against governance `5db303b` / approval `34b9e7d` and backend `5dd0618`. Fixed status was `P08_ROLE_QUALIFIER_STOP_OUTPUT_UNKNOWN`; safe reason `PERMISSION_SHAPE`.

All three approved commands started and completed through `ROLE_LIST`. Private plan/approval inputs are absent and no qualifier/gcloud child remains. The adapter cannot represent a mutation. No IAM/Firebase/token/API-key/database/runtime/Stripe/payment/customer action occurred. Attempt consumed; no retry.

This proves an output-contract mismatch, not role absence or provider denial. Google IAM documents that `roles.list` defaults to `BASIC`, which omits `includedPermissions`; `FULL` returns it. The documented `gcloud iam roles list` synopsis does not expose a view flag. Formatting an omitted field cannot supply it. Raw output was not retained, as approved. Backend evidence `d82a4d4`.

References: [IAM roles.list view contract](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles/list), [gcloud iam roles list reference](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/list).

Next requires a bounded local full-view request correction and isolated tests, then a fresh exact external approval. Accepted counts unchanged. **Documented output-contract gap; containment verified.**
