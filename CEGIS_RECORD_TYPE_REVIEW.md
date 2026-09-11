# APP-013 county record-type review — 2026-09-11

## Decision

No positive county allowlist is qualified yet. Keep acceptance disabled. Building and Unit, Condo, Office or Suite are relevant physical-site candidates; Site Visit and Photogrammetry are candidate collection methods, not documented accuracy guarantees. This narrows the earlier conditional qualification: metadata plus matching county/road fields are insufficient for live acceptance without source-owner clarification and operational evidence.

## Verified evidence

Read-only public layer metadata and an aggregate query were inspected; no individual address, customer data, credentials, Google request or paid service was used.

Current metadata defines seven point types and eight collection methods. It supplies category labels but no quantitative accuracy or per-method acceptance guarantees. County has a default value, so county text alone is not proof. Published VALIDATIONSTATUS 0 means no calculation/validation pending and no error; 2 means validation pending with no calculation required and no error. Pending validation does not prove a record is incorrect, but also cannot be represented as completed validation.

The aggregate filter was status='Current' AND country='US' AND stateabbreviation='OH' AND county='Cuyahoga'. Grouping by pointtype,capturemeth,VALIDATIONSTATUS and counting OBJECTID returned 52 groups totaling 115,395 records, all status 2, without a reported transfer-limit truncation. Candidate category counts:

| Point type | Capture method | Count |
| --- | --- | ---: |
| Building | Site Visit | 1,898 |
| Building | Photogrammetry | 7,034 |
| Unit, Condo, Office or Suite | Site Visit | 282 |
| Unit, Condo, Office or Suite | Photogrammetry | 320 |

These 9,534 candidate records are not qualified matches, not a customer-coverage sample and not a success-rate estimate. The aggregate also contains legacy/out-of-domain values such as Address and Unaddressed. Do not silently map these to Building. Null, Parcel, Mile Post, Utility Asset, Other and Unknown cannot pass the proposed physical-building rule. Do not infer that all valid homes outside the candidate set are outside coverage.

## Required clarification (draft only, not sent)

The county's official IT page lists gis@cuyahogacounty.us for GIS/REST questions. Ask:

1. Is this the supported public service for current physical service-address county membership, or is there a better maintained endpoint?
2. Why do all queried current records report validation required? What consumer-facing quality gate is appropriate, and what validation rules are actually run?
3. What location accuracy and review process do Site Visit/Photogrammetry and the Building/Unit categories represent? How should legacy/null values be interpreted?
4. Is linked-road agreement adequate near boundaries, including long driveways and buildings across a road's county boundary? Which authoritative boundary/parcel source and uncertainty rule should a consumer use?
5. What reuse/retention terms, update cadence, operational request limits and outage expectations apply to a small commercial application?

Do not send this draft without separate approval. Do not pay for an alternative or change provider automatically. A numerical buffer or metadata label cannot replace missing accuracy evidence. A future independently qualified source may resolve this blocker without a county response, but requires its own evidence and cost review.

## Next safe work

County acceptance remains UNKNOWN. The owner decision needed for this source is permission to send the above inquiry, not approval of unfamiliar GIS codes. While waiting, a separately approved bounded section can continue Google input/result semantic matching with mocks; it must not bypass county or admission gates. Routine customer verification remains an automation goal; this source review has not demonstrated acceptable automation coverage.

## Reproduction and validation

Fetch the layer metadata with f=pjson and inspect the pointtype, capturemeth and VALIDATIONSTATUS domains. Query layer 0/query using the filter/grouping above, outStatistics count(OBJECTID) as record_count, returnGeometry=false and f=json. Verify errors/transfer limits, sum every returned group and compare published domains. Do not request individual address rows.

Documentation only: governance consistency, execution-placement tests and git diff check are the applicable gates. No runtime/UI/dependency/schema changes; application tests/build/browser QA not rerun and previous results are not new evidence. APP-013 remains 50% recorded scope / 0 of 12 accepted; no pilot acceptance or overall estimate.

Sources reviewed:

- https://gis.cuyahogacounty.gov/server/rest/services/NCGIDE/Addressing_Sites_Streets/FeatureServer/0
- https://gis.cuyahogacounty.gov/server/rest/services/NCGIDE/Addressing_Sites_Streets/FeatureServer/0/query
- https://gis.cuyahogacounty.us/docs/nams/datadictionary.htm (dated July 31, 2024; corroborated category labels against current metadata)
- https://www.cuyahogacounty.gov/information-technology
