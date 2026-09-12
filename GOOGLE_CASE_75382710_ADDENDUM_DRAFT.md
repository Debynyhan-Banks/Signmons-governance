# Google case 75382710 — unsent addendum

Use the existing authenticated Google Cloud support case, not a guessed support email. Draft only: no message sent.

Subject: Clarification: transient responseId and county-based service eligibility

Hello Google Maps Platform Support,

For our U.S.-only Signmons service application, we plan to use Address Validation to confirm a customer-entered service address and determine whether it falls within our business service area, Cuyahoga County, Ohio. We are not building a geographic dataset or claiming parcel certification.

Please clarify:

1. For a correction sequence, may we hold the first responseId server-side only for that customer's active session, use it as previousResponseId, and delete it at session end or after 24 hours, whichever occurs first? No logs, backups or cross-user reuse.
2. May we evaluate uspsData.fipsCountyCode and county immediately in memory for service eligibility, then discard the provider fields? Does this business-rule use have additional restrictions?
3. May we retain only a minimal eligibility outcome (inside/outside/unknown), Signmons-generated operation ID, check time, address revision and policy version without retaining the Google response or county fields? If not, what supported approach do you recommend?
4. What is the documented format of fipsCountyCode: three county digits or five state-and-county digits? Are leading zeros preserved? What should clients expect when USPS county or physical-address flags are absent?
5. May we retain only non-address-specific integration findings such as field presence/type and code length from a controlled test, or should these also be treated as restricted Google Maps Content?

The published caching table lists particular fields; we do not want to assume it permits caching other USPS fields or derived outcomes. Please identify the applicable documentation/terms for these uses.

Thank you.

No credentials, private address, phone number, customer records or raw API response should be attached.
