---
schema: 1
id: 2026-11-21-idiw-pr21-preflight-report-boundary-lk32
kind: handoff
scope: agent:latch
status: active
evidence: observed
author: latch-idiw-pr21-2026-11-21
created: 2026-11-21
updated: 2026-11-21
sources: "IDIW-S1-04P issue 18 and PR 21; exact base main@4e77021b9595e09bd21f36f35778801222df6c4b head 589dc4e1cc73eedb4a4cc1a4e4108aaca8786828; preflight blob bc8ea9c2f9124e92c4308dfe693eb2330b92f537; preflight tests c7a75ac1e46f7b68999e1f25d2fa7694aad380c1; release audit dd069dc3e6754e52bb3bd4f5923dd63aa72e2004; exact-function isolated V8 probes and source audit; CI 44987723831; PR COMMENTED review 6010540604."
---

# Latch — IDIW PR #21 preflight report confidentiality and authority review

## Summary

**Disposition:** **NO GO for merge** at exact PR head `589dc4e1cc73eedb4a4cc1a4e4108aaca8786828`, pending two small report-confidentiality repairs. Published [official COMMENTED review 6010540604](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/21#pullrequestreview-6010540604). Draft PR remained open and unmerged at verification. The new preflight is appropriately narrow and read-only from a remote-write standpoint, but its *reporting* is not fully fail-closed against untrusted header values or older comparison records.

**Mode / provenance:** Source-pinned independent counterexamples, read-only target repository; no app source edit, merge, preview deployment, credential use, DNS/Cloudflare change, or production interaction. Original user request simply asked to inspect PR #21; prior project review workflow authorizes an independent specialist review. PR description exposed Mothlight/Gauge verdicts, so this is **context-exposed, not blind**. Their full review texts were read only **after** independent counterexamples were formed. Shared GitHub account author attribution is not independent authentication of Latch's runtime.

**Authority and release boundary:** Issue #18 only authorizes a nonproduction verifier, draft PR and local loopback tests; **live-host gate remains BLOCKED** because no preview exists or was authorized. CI run [44987723831](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/actions/runs/44987723831) reports success for the exact head. Implementer reports 256 Node tests, 332 Chromium/axe checks and Nu 0 errors. Latch did not independently run full Node/browser/Nu tests or real HTTP. Historical peer redaction corrections are present at this head.

## Evidence

### L21-1 — allowlisted response header **values** disclose arbitrary content (merge blocker)

- Source: `prototype/first-light/scripts/preflight-preview.mjs` lines 355–364 (`headerFingerprint`), lines 36–46 (`RECORDED_HEADERS`), and 478–484 (raw Content-Type in summary).
- **Executed exact function** in isolated V8 with normal `Headers`-shaped local input (only ESM binding/fake Headers object adapted). Served `content-security-policy: script-src 'nonce-PRIVATE-SESSION-4321' https://internal-tenant-5544.example; report-uri https://internal-account-7342.example/report?auth=PRIVATE-ACCOUNT-0319`, `access-control-allow-origin: https://PRIVATE-TENANT-2066.example`, plus standard content-type and X-Robots-Tag. Returned `recorded` contained **all four private markers verbatim**; the function copies the first 300 characters of each allowlisted header value. This would enter `checks[].details.fingerprint.recorded` and the saved JSON by direct source flow. Content-Type is also included unredacted in `checks[].summary`. **Synthetic markers; no actual live account data observed**.
- Operator procedure explicitly permits allowlisted values and instructs users to inspect/keep reports private. This is a **policy mismatch** with issue #18's broader `reports free of credentials/private body/account metadata` requirement, **not proof of a current live breach**. Proposed minimal fix: safe normalized summaries or digest+length for endpoint/high-entropy fields like CSP/ACAO; safe Content-Type MIME/charset summary; optional separately authorized private raw diagnostic mode; marker tests in JSON, stdout and report file.

### L21-2 — old/modified comparison report can bypass name redaction (merge blocker)

- Source: `compareFingerprints` lines 367–381 and `runPreflight` lines 429–451, 471–476. A comparison input is accepted based solely on a matching `schema` string. No validation of `earlier.recorded` keys or `earlier.otherNames` values.
- **Executed exact `compareFingerprints` in isolated V8**: `earlier.otherNames = ['x-private-tenant-99817']` with otherwise standard current fingerprint emits `x-private-tenant-99817 removed`. Likewise `earlier.recorded = { 'x-private-user-83762': 'yes' }` emits `x-private-user-83762 removed`. The messages are interpolated into the new report's header-check summary and printed by CLI. This bypasses the current safe header-name vocabularies and realistically can occur when upgrading from older report formats, though no existing live protected report is known.
- Minimal fix: normalize/reject previous keys and names to current fixed allowlists before diffing; collapse unknown names to count; test with a schema-valid hostile/legacy earlier report through CLI file/stdout.

### L21-3 — credential boundaries on *nested* authenticated preview (conditional future-host risk)

- Source `get` lines 142–178 always spreads `...headers` on each GET and follows all same-origin redirects except `/cdn-cgi/access/`. `robots.txt` probe line 527 intentionally uses `fromOrigin:true`, i.e., always root `/robots.txt` even if preview base path is `/staging/`. Thus `--base-url https://shared.example/staging/ --auth-headers-env ...` sends preview credentials to origin-root `/robots.txt`, and same-origin redirects could carry them to another path-scoped backend. **Not a cross-origin leak or actual tested remote exposure.** A dedicated root-only preview host mitigates. If authenticated nested bases are supported, omit auth on root robots probe; block off-base redirect hops or require explicit owner-approved scope. Source-confirmed risk only, not independently executed Node HTTP.
- This does not re-open Mothlight's already fixed incorrect subpath robots probe; the root policy is semantically correct for crawlers.

### L21-4 — unbound previous report provenance (P2)

- `runPreflight` checks earlier `schema` only, not earlier `target.origin/basePath` or `artifact.manifestSha256`. Equal raw header fingerprints from two unrelated targets may be described as `unchanged since the earlier report`. Ask for a provenance mismatch REVIEW or explicit cross-target selection; not an observed host failure.

### Positive findings

- Only GET requests; redirects never followed across origins; proper auth failure / timeout BLOCKED and malformed Location FAIL; injected markup classified without served body, title, h1, lang, generic attribute, custom tag or custom header NAME copies. Fixed public edge URL patterns retained as diagnosis. Unknown-route and root robots probes, byte-for-byte assets, served-copy release audit and optional Nu; synthetic flag on loopback. No fixture or app source changes in this PR beyond the one README section; new tool/tests/docs/evidence only.
- 36 hermetic tests in submitted suite include marker checks for served title, element values, names and redirect paths, but **not** above private allowlisted header values or hostile old report fingerprint keys/names. Existing tests do compare safe earlier reports and detect count changes. No actual authorized protected preview exists; no live-host risk or release certification claimed.

## Outcome

**COMPLETE — official exact-head review published with two bounded merge-blocking *report* corrections, one conditional path-auth topology risk, one comparison-provenance note.** Existing peer work deserves credit; do not add broad security abstractions or modify deployment infrastructure. No source/PR state changes, no release authority, no false reports of actual private data exfiltration. Review again at a new exact head; avoid granting adoption on CI success alone.

## Revisit when

Implementer changes header value sanitization or historical compare input policy; owner explicitly chooses to accept raw allowlisted header values in private reports; authenticated nested-base previews are authorized; the operator adds cross-target header comparison for cutover; or PR #21 advances/merges.
