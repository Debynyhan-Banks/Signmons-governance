# APP-013 / 3A / P08 — IAM Role etag output-contract correction result

Status: LOCAL CORRECTION COMPLETE; NO EXTERNAL ACTION. R1-W01 / APP-013 / 3A remains unchanged.

Under owner approval `95b434f`, backend `fed5efb` implements only Alternative 1 from `APP013_P08_ROLE_ETAG_OUTPUT_CORRECTION_PROPOSAL_20261028.md`. Source SHA256 is `b164717be48a45e2c6be86d4c3968d636f028dded95af8d0597d580f9af8083b`.

The disabled evidence-contained qualifier now accepts optional IAM Role `etag` only when it is a string and discards it before normalization, definition hashing, classification and evidence. Non-string `etag` and unknown fields retain strict `ROLE_SHAPE` refusal. All request, bearer/raw-output, pagination, deadline, signal, one-attempt, private-input and restoration-contract controls remain.

Verification: 21/21 isolated tests, Python syntax, backend architecture, frozen baseline, cross-repository consistency, 25/25 governance safeguard tests and whitespace checks pass. Browser and database gates are inapplicable to this evidence-only parser correction. No provider command/request, retry, IAM action or other external action occurred.

Accepted milestones remain 1A/1B/2A/2B (4/8). R1 newly closed remains 0/27; legacy remains 6/60; intelligence remains 0/13. **No scope deviation.**
