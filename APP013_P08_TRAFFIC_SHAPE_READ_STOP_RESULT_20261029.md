# APP-013 / 3A / P08 — traffic-shape read safe stop

Exact approved operation `581346e1-445f-48f1-909c-b86137a9c1a3` reserved at 2:45:08 p.m. Eastern on October 29, 2026 and returned `P08_TRAFFIC_SHAPE_DIAGNOSIS_STOPPED` / `CLI_REFUSED` on its first owner-list CLI command. The traffic command was never attempted; no traffic subcondition was learned. The saved journal has empty residuals; exact private plan and binding are absent with affirmative readback. No traffic change, payment or other mutation occurred. The single attempt is consumed and cannot be retried.

The local adapter currently collapses nonzero CLI exit, oversized output and process-launch failure to `CLI_REFUSED` while suppressing raw stderr. The executable path resolves locally, but current owner/provider status is UNKNOWN. No follow-on Cloud read is authorized. See backend commit `b5c5f4b`, `evidence/APP-013/p08-traffic-shape-read-stop-20261029`.

Next owner decision is `APP013_P08_TRAFFIC_CLI_FAILURE_CLASSIFICATION_PROPOSAL_20261029.md`, a local-only safe error-category correction. A fresh external read would still require a new exact card and approval. Accepted 4/8; newly closed R1 0/27, legacy 6/60, intelligence 0/13; P08 and 3A remain open. **Unintended CLI stop disclosed; no scope deviation implemented.**
