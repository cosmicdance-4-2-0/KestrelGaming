---
schema: 1
id: 2026-11-19-idiw-pr9-negative-review-lk31
kind: handoff
scope: agent:latch
status: active
evidence: observed
author: latch-idiw-pr9-2026-11-19
created: 2026-11-19
updated: 2026-11-19
sources: "IDIW i_d_i_w--TEMPLATE PR #9 requested head ff37843168bc8bbb3c45839e19e353e2deef910b, GitHub COMMENTED review 5987541159; source blobs validate 658f5c7ec79fed8c323aa7f2f15aa69976bfd43a, portfolio 19da89283ee5e912bc09850a19c731e69393f338; focused Node 22 executed negative tests; later PR head 26f11675fa12acbe60e8934e668a20b2522f4fe6 validator a670f57141af03ff5f7dbe86d94e4c6c9a20d335; CI runs 44663233495 and 44667283141. No production access."
---

# Latch — IDIW-S1-02A PR #9 negative-path review at pinned historical head

## Summary

**Review outcome: BLOCK exactly `ff37843168bc8bbb3c45839e19e353e2deef910b`, not a judgment that later `26f1167` is blocked.** Source-pinned independent review officially posted as [COMMENTED review 5987541159](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/9#pullrequestreview-5987541159), with failure modes and smallest remedies. Both serious pinned-head defects (impossible evidence times and English-only RTL title metadata) were changed in later PR head; the newer timestamp fix was independently executed in Node. The entire newer PR was **not** re-reviewed.

Reviewer: Latch — The Locksmith, Kestrel `agents/latch-v1`. Shared GitHub account is attribution, not identity authentication. PR body included Axiom's correction summary before this review, so this is not perfectly blinded; no other agents' review bodies were consulted. User authorized read-only investigation and publishing the PR review; **no application source, infrastructure, deployment, or PR state changed**.

## Evidence

**Native exact-source reproduction:** Used temporary outside-repo Node 22 fixtures containing exact `prototype/first-light/src/content/validate.mjs` and `portfolio.json`, verified by `git hash-object` to match GitHub blobs `658f5c7...` and `19da892...`. Positive checked-in portfolio `validatePortfolio === []`.

- At `ff37843`: substitutions of release evidence `2026-02-31`, `2026-13-20` and link verification `2026-11-20T24:00Z`, `2026-11-20T02:40:60Z` **all accepted with [] errors**. `WHEN` only checked digit shape. Existing test rejected `20 Nov 2026` rather than impossible real-world dates. **Actual false acceptance** of invalid publication evidence.
- At `26f1167`: recreated and Git-blob-verified new validator `a670f571...` in the same native Node fixture. The same impossible dates/times now produced explicit invalid-evidence findings. This specific blocker is fixed at that head.
- At both heads: changing `status` to inherited property `constructor` yields `[]` from `validatePortfolio` due to `status in STATUSES`. The full HTML template's missing `status.constructor` localized key should stop the build; **not evidence of a successfully emitted fraudulent page**. Recommend `Object.hasOwn(STATUSES, project.status)` and focused regression; P2 not a demonstrated static-build leak.
- At both heads: a complete `verified` record with `method: "Anonymous GET returned 404 Not Found"` and `limitations: "Destination removed"`, or an unsubstantiated `method: "guess"`, still produces `[]`, while link remains actionable and project `available`. Free text cannot be machine-attested by record-shape checking. Also `2999-01-01` and `2001-01-01` remain accepted. No actual live 404 or invalid presently checked-in record was established. Treat machine outcome/recency vs human release review as **release policy**, not a proved production outage.
- Correct rejections independently reproduced: absent `releaseEvidence`, missing link limitations, `available` lacking app link, `unverified` carrying app link, duplicate project ID, HTTP URL, ordinary unknown status. Null project and null link throw TypeError rather than friendly validation errors, but they stop the build.
- At `ff37843`: RTL fixture has `lang=ar dir=rtl` and a fully English-brand `meta.title`; template marks only *fallback* titles `lang=en`, so emitted English-only title is unmarked in Arabic document. At `26f1167` the template was updated to mark whole-title language/direction when justified; not independently executed through screen reader.
- Direct isolated V8 localizer checks: missing `nav.work` refuses strict usage; placeholder mismatch in `about.body` reported and throws at use; explicit fixture-only fallback wraps English element text with `lang=en dir=ltr`. No supported Arabic locale is claimed.
- Source/CI audit: `site.mjs` intentionally removes old preview `/experiments/neon/` without redirect, documents history; active Neon root/Editorial relative preview mapping preserved. `page.mjs` emits static semantic HTML, no client JS, contact explicitly pending and nonactionable. `tests/browser.mjs` contains real disabled-JS/CSS-abort checks but stubs external destinations; thus navigation assertions **do not prove** live availability. `scripts/audit-release.mjs` rejects fixtures, unsafe artifact content and undeclared links, not stale or semantically untruthful free-text evidence. GitHub Actions reports success on both old/new heads, self-harness, not independent full suite.
- **Aborted preliminary isolated V8 URL experiment:** The first functions-tool isolate lacked a global WHATWG `URL`, generating false invalid-URL results. Those results were discarded and replaced by native Node probes above. No false URL failures are cited in official review.

**Source/limits:** [Original head validator](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/ff37843168bc8bbb3c45839e19e353e2deef910b/prototype/first-light/src/content/validate.mjs) and [current correction](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/26f11675fa12acbe60e8934e668a20b2522f4fe6/prototype/first-light/src/content/validate.mjs). [Official review](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/9#pullrequestreview-5987541159) holds full failure table, expected/observed actions and fix recommendations. GitHub clone unavailable due DNS; no full local Node/browser/Nu suite or external destination checks performed. No manual screen readers/devices, deployment or production rollback experiment. The reviewed PR remained draft/unmerged at publication; latest head already changed and historical block cannot substitute for its re-review.

## Outcome

**COMPLETE — independent negative-path review posted, exact historical SHA, read-only app, source-verified native Node targeted counterexamples.** The classification is **BLOCK pinned head only**, with timestamp/title corrections later addressed. Product owner controls subsequent merge/release; unknown future link reachability, owner-approved contact, localization, actual physical accessibility and cutover rollback remain separate release gates. **No claim of security certification.**

## Revisit when

The owner requests new-head PR9 acceptance; IDIW introduces automatic project/evidence ingestion; a release gate claims that a nonempty `verified` record proves live availability; old preview routes are publicly published; or project/status validation becomes an independent reusable API.
