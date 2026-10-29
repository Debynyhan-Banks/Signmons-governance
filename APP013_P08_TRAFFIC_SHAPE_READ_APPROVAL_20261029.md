# APP-013 / 3A / P08 — exact traffic-shape read approval

Debynyhan Banks selected “Approve this exact read-only operation” after review of `APP013_P08_TRAFFIC_SHAPE_READ_OPERATION_20261029.md` at immutable governance commit `c45d9a9`. Its pre-decision SHA256 is `4d4abaa792da803768e780b09204466d2df555c47c00521cc9e3acc65e7ea6ee`.

Approval covers only operation `581346e1-445f-48f1-909c-b86137a9c1a3` today, October 29, 2026, 2:45–3:00 p.m. Eastern: start at or after 2:45 and strictly before 2:55, reads before 2:58, process/private-input closeout before 3:00; maximum three Cloud CLI reads, USD0, one attempt and no retry. It identifies only fixed traffic facts for the named service. No Terminal password, provider configuration, traffic/deployment, authentication, Stripe/payment or customer action is authorized.

This authority is consumed by one reserved attempt or the strict 2:55 cutoff. It does not authorize a correction or R05 rerun. **No scope deviation.**
