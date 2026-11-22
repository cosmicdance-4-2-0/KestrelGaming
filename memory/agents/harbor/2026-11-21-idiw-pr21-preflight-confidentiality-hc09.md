---
schema: 1
id: 2026-11-21-idiw-pr21-preflight-confidentiality-hc09
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-pr21-readonly-review-session
created: 2026-11-21
updated: 2026-11-21
sources: "IDIW i_d_i_w--TEMPLATE PR #21, exact head a07262344e69b9d1600c4d38623634b6b9fa9a02 vs main 4e77021b9595e09bd21f36f35778801222df6c4b; source-executed virtual-filesystem tests of actual auditRelease and redactServedFinding with artificial markers; repository AGENTS.md and IDIW-S1-04P operator procedure; Harbor home agents/harbor-v1@5d95013c7e808f728e59f... (full SHA: 5d95013c7e808f728e59cb17a9fb7fe3b262dabe)."
---

# Harbor HC09 — IDIW PR #21 served-preview preflight and confidentiality review

**To:** IDIW PR #21 owner/integrator.  
**Revision:** `cosmicdance-4-2-0/i_d_i_w--TEMPLATE@a07262344e69b9d1600c4d38623634b6b9fa9a02`, base `main@4e77021b9595e09bd21f36f35778801222df6c4b`.  
**Mode:** Read-only independent technical examination, **context-exposed**: PR description already listed existing reviewer acceptance/corrections. I did not rely on peers' reasoning or fetch their new reviews. No application, hosting, DNS, credentials, deployment or review threads edited during the analysis.
**Verdict:** **BLOCK merge for current head** until H21-01 is corrected and H21-02's precondition behavior is explicitly resolved. None of the current probes reached a live site; the synthetic code-execution cases used artificial markers.

## Summary

The PR adds a read-only, local-fs-writing served-preview preflight under `prototype/first-light/`: a GET-only, origin-scoped comparison between audited build files and a future authorized preview. Its design intentionally does not deploy and gates real protected preview/cutover separately. Source inspection finds appropriate defenses against cross-origin redirect following, non-HTTPS nonloopback targets, targeting independent application hosts, unannounced missing content, soft-404 and edge-injection changes. The default/contact release audits and published HTML/CSS are not modified.

**H21-01 (blocking):** a report-redaction regex mishandles a served attribute containing an HTML-decoded quotation mark, leaving an artificial private marker in the report's `served copy#release-audit` findings. The same weakness affects an external URL finding. This contradicts the report's promise to withhold served values.

**H21-02 (important):** an unaudited artifact produces an `artifact#release-audit FAIL` but the preflight continues making GET requests, including artifact-listed routes, with operator-provided authentication. The test currently only checks the outcome and does not assert zero requests. This undermines "audit before host probing"; it is a code-level trace, not independently source-executed with real network traffic.

## Evidence

### H21-01: source-executed report-leak counterexamples — 2/2 reproduced

Read exact [`scripts/audit-release.mjs`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/a07262344e69b9d1600c4d38623634b6b9fa9a02/prototype/first-light/scripts/audit-release.mjs) and [`scripts/preflight-preview.mjs`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/a07262344e69b9d1600c4d38623634b6b9fa9a02/prototype/first-light/scripts/preflight-preview.mjs). I ran the actual `auditRelease` implementation in isolated V8 using injected in-memory filesystem adapter, exact repository `portfolio.json` / `en.json` and synthetic HTML. I then invoked the exact `redactServedFinding` declaration extracted from lines 470–479, with only its unused safe-tag/attribute helper inputs stubbed. This is **source-executed production code**, not an entire `runPreflight` network/CLI or Node test-suite run.

**Case A: decoded quoted locale.** Served markup `<html lang="zz&amp;quot;...">` is not the tested character-reference variant; the actual tested input is `<html lang="zz&quot;SENSITIVE-MARKER-731">` (also reproduced with `&#34;`). The production release audit emits `index.html: locale "zz"SENSITIVE-MARKER-731" is not declared for release (en)`. Sanitizer emits `index.html: locale (served value withheld)SENSITIVE-MARKER-731" is not declared for release (en)`. The marker survives, violating value-withholding.

**Case B: decoded quoted URL.** An unverified `href="https://unknown.invalid/path&quot;SENSITIVE-MARKER-731"` yields a finding containing `external URL https://unknown.invalid/path"SENSITIVE-MARKER-731`. The sanitizer masks the host and some path, but leaves `"SENSITIVE-MARKER-731` in the result. Again, this artificial marker survives.

**Control:** `lang="zz_plain"` is normally fully withheld; the leak requires the boundary-crossing decoded quote, which the repo's audit deliberately supports.

**Root cause:** A naive `locale "[^"]*"` replacement and a URL redaction that terminates on quote cannot safely redact interpolated untrusted values in human-readable finding prose. A served value can contain decoded quotes without terminating its original HTML-quoted attribute.

**Minimum resolution:** Prefer release-audit structured finding objects (stable code, file, attribute/tag, safe counts) for preflight; produce predeclared report text rather than regex-redacting arbitrary diagnostic prose. A bounded alternative is to make served findings fail-closed with fixed generic messages/counts and no interpolated values. Add end-to-end tests asserting synthetic markers absent from CLI stdout/stderr, serialized report and `checks[].details.findings`, including `&quot;`, `&#34;`, URL, and any other quoted fields. Keep artificial markers only.

### H21-02: audit not actually an admission gate

At [`preflight-preview.mjs:523–528`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/a07262344e69b9d1600c4d38623634b6b9fa9a02/prototype/first-light/scripts/preflight-preview.mjs#L523-L528), `artifactFindings` creates a failing result but execution proceeds. At [lines 541–543](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/a07262344e69b9d1600c4d38623634b6b9fa9a02/prototype/first-light/scripts/preflight-preview.mjs#L541-L543), it starts fetching all artifact-listed paths even when findings are nonempty. Current [test near lines 601–612](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/a07262344e69b9d1600c4d38623634b6b9fa9a02/prototype/first-light/tests/preflight-preview.test.mjs#L601-L612) asserts `artifact#release-audit = FAIL` and overall `FAIL`, not that host requests were prohibited.

The origin restriction still prevents cross-origin forwarding, but paths under an unaudited artifact have not been authorized by the intended precondition. Proposed correction: validate the artifact first, return a non-success report **without issuing GETs**, or throw a clear preflight validation error before constructing a request. Prefer a report with a full `artifact FAIL` and `network not attempted` status over usage exit 2; no remote evidence should be asserted. Add a loopback test with a fixture artifact and a request counter proving zero GETs. **This is source-inspection inference, not an independently source-executed fetch.**

### Other boundaries and evidence limits

- **Scope:** Seven files changed: one new 741-line library/CLI, one new 680-line test file, procedure, evidence report, two synthetic JSON samples and README. No site contact page, render path, release-audit code, CI workflow, DNS, Cloudflare or production application modification. Current PR is open/draft and live-host gate explicitly BLOCKED.
- **Good controls observed:** `GET` and `redirect: manual`; cross-origin redirect is not followed; HTTPS enforced outside loopback; separate Auralprint/KeyLine hosts refused. Under nested base path, root robots probe drops auth headers. Response size/timeout limits, clear PASS/FAIL/REVIEW/UNVERIFIED/BLOCKED statuses, and report provenance exist. This is source inspection, not a comprehensive network adversarial certification.
- **Known deliberate report risk:** `robots.txt` directive lines are recorded in clear, apart from query redaction. They can include nonpublic paths or internal host references; operator procedure says reports remain private. A future authorized preview should review the necessity/retention of these lines, without conflating intentional data with a proven H21-01 leak.
- **Accepted source:** `main@4e77021b9595e09bd21f36f35778801222df6c4b`. No real access-protected preview exists/was contacted, so this PR cannot authorize G5/G6 or demonstrate edge policies.
- **CI evidence at review head:** GH Actions run `44990015682` was **in progress** at the last check; earlier successes apply to earlier SHA only. No local `node --test`, Chromium/axe, Nu, actual CLI/network server run, or full Kestrel validator reproduced in Harbor's container during this review.
- **PR-head movement:** The PR description still named `589dc4e` while head moved through `95ea427` to `a072623` during this review. The present report is pinned to `a072623`; repin on any further correction. The newer `a072623` correction fixes a separate known-server-version leakage but **does not change** H21-01's sanitizer or H21-02's precondition handling.
- **Independence:** Context-exposed because the PR description includes other reviewers' statuses, but the two findings and the synthetic checks are Harbor-attributed; no blind-review claim and no reviewer consensus inferred.

**Verdict:** **BLOCK current-head merge** under a prototype's own confidentiality and no-surprise network contract. These are narrow repairs; do not introduce a general web crawler, secret service, deployment automation or separate retry framework.

## Revisit when

A new head carries a fail-closed served-finding redaction scheme plus a no-request-on-failed-artifact test, or the owner explicitly reduces the artifact admission requirement with a documented risk tradeoff. Re-read and source-execute the changed code at exact head, review CI separately, retain synthetic-only host status, and preserve no-deployment authority.
