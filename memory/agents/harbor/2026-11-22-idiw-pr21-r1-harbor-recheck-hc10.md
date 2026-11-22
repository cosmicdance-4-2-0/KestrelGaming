---
schema: 1
id: 2026-11-22-idiw-pr21-r1-harbor-recheck-hc10
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-idiw-pr21-r1-review-session
created: 2026-11-22
updated: 2026-11-22
sources: "IDIW PR #21 corrected exact head 83f164b44bfc50cb32dab877915bb336e62775eb, previous blocked a07262344e69b9d1600c4d38623634b6b9fa9a02 and base main 4e77021b9595e09bd21f36f35778801222df6c4b; source-executed virtual-filesystem actual release audit plus servedFindingCodes, mock request-counter actual runPreflight, exact-head GitHub Actions run 44998191613 (CI-attributed); Harbor prior HC09 and agent home agents/harbor-v1@803bc0374f69687d559ae9199e42797971f7eb1e."
---

# Harbor HC10 — IDIW PR #21 R1 preflight publication and confidentiality acceptance

**Task:** User-requested repeat of Harbor's independent [IDIW PR #21](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/21) review after implementation correction.  
**Application:** Exact `83f164b44bfc50cb32dab877915bb336e62775eb`, base `4e77021b9595e09bd21f36f35778801222df6c4b`; compare against blocked earlier `a07262344e69b9d1600c4d38623634b6b9fa9a02`.  
**Harbor home before recheck:** `agents/harbor-v1@803bc0374f69687d559ae9199e42797971f7eb1e`. Earlier review [HC09](2026-11-21-idiw-pr21-preflight-confidentiality-hc09.md) remains historical BLOCK evidence; do not erase or retroactively revise it.  
**Verdict:** **ACCEPT for merge consideration of nonproduction prototype only.** Both Harbor blockers **H21-01 / H21-02 RESOLVED** at the exact corrective head. This is an attributed specialist `COMMENTED — ACCEPT`, not a production deployment, owner release decision, permission to contact protected sites, or completed G5/G6 cutover evidence.

## Summary

One corrective commit changed the new preflight tool, preflight tests, documentation, synthetic evidence and README only (seven files). No release-audit implementation, published page, contact flow, default build, build pipeline, actual hosting, CI workflow, DNS, or independent Auralprint/KeyLine application was modified. The live-host gate remains **BLOCKED**.

- **H21-01 closed:** The old report sanitizer tried to hide *untrusted served values* inside free-form release-audit prose with regexes and leaked entity-decoded-quote markers. The replacement [`servedFindingCodes`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/83f164b44bfc50cb32dab877915bb336e62775eb/prototype/first-light/scripts/preflight-preview.mjs#L471-L519) selects fixed enumerated code labels and a trusted artifact-path key, with unknown prefixes reduced to `artifact` and unknown messages to `other-finding`. No raw served audit prose is retained. Repeated codes aggregate counts. This deliberately reduces human detail to protect confidentiality.
- **H21-02 closed:** [`runPreflight` artifact gate](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/83f164b44bfc50cb32dab877915bb336e62775eb/prototype/first-light/scripts/preflight-preview.mjs#L563-L580) now terminates before any GET when `auditRelease(artifact)` returns findings. It reports the actual `artifact#release-audit FAIL` and `target#observation UNVERIFIED / not attempted`, producing overall `FAIL` and an empty request log. This preserves failure provenance without fabricating a remote observation.

## Evidence

### Independently source-executed checks on the exact corrective head

Fetched `prototype/first-light/scripts/audit-release.mjs`, `scripts/preflight-preview.mjs` and the real `src/i18n/en.json` and `src/content/portfolio.json` at `83f164b...`. Evaluated the actual production function bodies in isolated V8 with only module declarations adapted and a virtual filesystem / intercepted GET for bounded tests. These are independent **source-executed unit/contract probes**, not a local Node/browser full suite or a real network test.

**H21-01:** An artificial served HTML with `lang="zz&quot;SENSITIVE-MARKER-731"`, `href="https://unknown.invalid/path&quot;SENSITIVE-MARKER-731"` and a malicious link in page text produced **three findings from the real release-audit function**, and each raw finding contained the synthetic marker. The corrected real `servedFindingCodes(findings, Set(["index.html"]))` returned exactly:
- `index.html: undeclared-locale`
- `index.html: unverified-external-url`
- `index.html: unverified-url-in-text`

**Marker absent** from the report-safe array. Additional direct helper controls used seven entries with an untrusted filename prefix, unknown message and duplicate script finding; the result was fixed codes `artifact: hidden-file`, `index.html: other-finding`, `index.html: script-or-inline-handler ×2` and the three expected named diagnoses, **no marker retained**. Unlike HC09, a decoded quote no longer terminates a quoted-value redaction because no interpolated value reaches the output.

**H21-02:** Executed the exact `runPreflight` body with the real `auditRelease` over a virtual artifact containing clean `index.html` plus an unintended `fixture.json`. The audit rejected JSON. The preflight returned **FAIL**, a `target#observation UNVERIFIED` `not attempted` marker, **0 intercepted GET calls**, and an empty request log. A positive control removing the JSON resulted in a clean artifact and **three virtual GET attempts** (root, unknown path, origin-root robots); the intercepted synthetic BLOCKED responses led to overall `BLOCKED`, not false PASS. No real network packets were sent.

**Test execution fidelity:** The above checks are production-function V8 evaluation with mocked filesystem/GET/Node globals and explicitly injected exact JSON policy. They establish the source-level boundaries and the prior exploit's closeout, not a complete CLI, HTTP server, Cloudflare Access, real DNS, timeout or browser run.

### Exact-head GitHub CI

[Actions run 44998191613](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/actions/runs/44998191613) was **completed/success** with `head_sha=83f164b...`. I directly inspected jobs and verify log:
- `264/264` Node tests, `0` failed, including `44` hermetic preflight tests (self-authored by the implementer).
- Build determinism, candidate and default release audits, official Nu HTML checks passed.
- `332/332` Chromium/axe checks passed on emulated devices, without a served remote host.

CI tests are **attributed to GitHub** rather than executed by Harbor's local Node/Chromium suite.

### Nonblocking boundaries / unknowns

- The tool remains **GET-only** and operator-targeted with redirect restrictions. It requires HTTPS for nonloopback, refuses the separate application hosts, and omits access headers from the origin-root robots probe when under a nested base path. Source-inspected at the review head; no general adversarial external-site certification.
- `robots.txt` directive lines are intentionally recorded verbatim except query redaction. The report remains an operator-private artifact and may contain operational paths. A genuine preview and report retention policy need separate owner authorization.
- The *artifact's own* release-audit failure evidence is operator-owned input and still exposes ordinary audit messages, while **served-copy** findings are fixed safe codes. This is within this task's specified distinction, not evidence of confidential server-response leakage.
- Preview diagnostics are intentionally less descriptive after H21-01; code-only output can still guide a developer to safely inspect a protected preview under separate authorization, rather than reveal response text in a portable report.
- One locally controlled synthetic client at one moment cannot certify Cloudflare edge rewriting, host availability, secret handling in a live environment, browser rendering or real rollback. The live-host gate stays BLOCKED; passing CI or a future preflight is **not** deployment approval.
- The PR description still names older `589dc4e`; only the **actual ref SHA `83f164b`** and its matching CI are used for this verdict. PR was open and draft at recheck. Repin on any subsequent head change.

**Disposition:** No remaining Harbor merge blocker found in the corrected S1-04P scope. Recommend **ACCEPT for nonproduction code-checkpoint merge consideration**, independent of other reviews and owner authority. No changes requested to production, no preview deployed, no credentials requested or stored, no user-controlled source paths fetched.

## Revisit when

PR #21 head changes, another reviewer supplies a counterexample, served-copy auditing expands beyond exact artifact paths, report retention/security policy changes, the owner authorizes a protected preview, or G5/G6 release readiness is reconsidered. Pin the new SHA and rerun both H21-01 exploit and H21-02 no-request proof; retain earlier HC09 as historical record.
