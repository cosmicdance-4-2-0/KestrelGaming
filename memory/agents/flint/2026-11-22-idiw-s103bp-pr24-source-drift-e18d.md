---
schema: 1
id: 2026-11-22-idiw-s103bp-pr24-source-drift-e18d
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-idiw-s103bp-pr24-independent-review
created: 2026-11-22
updated: 2026-11-22
sources: "IDIW issue #23 and PR #24 exact head 3a24712988e299c3215199e9985b75334e3678be; accepted main 27b13c0011b8dcc88791b46dfe338e8b724517d3; exact 3-file diff, approved canonical copy, portfolio, locale catalog, render template, ledger, decisions and Auralprint GitHub README/releases checked 2026-11-22."
---

# Flint — IDIW S1-03B-P issue #23 / PR #24 decision packet

**Task outcome: independent source-diff review complete.** **Verdict: CONDITIONAL ACCEPT** at PR head `3a24712988e299c3215199e9985b75334e3678be` (base `27b13c0011b8dcc88791b46dfe338e8b724517d3`); one narrow source-of-truth consistency correction recommended before merging. This evaluates whether documentation is a coherent, evidence-grounded owner decision packet, **not** whether the website can be released. No site code, approval state, deployment, merge, independent app or another agent's memory touched.

## Summary

The owner requested a bounded **read-only owner-decision packet** in [Issue #23](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/issues/23). PR #24 consists of three Markdown paths only: new `docs/reviews/IDIW_S1_03B_VISITOR_REVIEW/DECISION_PACKET.md`; additions IDIW-031, -032, -033 to `docs/DECISIONS.md`; note-only updates to the S1-04R owner-gate ledger. **No HTML, CSS, i18n catalog, portfolio, release-candidate profile, verifier, scripts, CI, hosted app or independent application changed.** Document-only scope is proportionate: owner directions belong in the decision log, and ledger status notes must match them.

**What works:** The packet distinguishes owner-approved canonical homepage/About from draft project summaries, contact, statuses, links, notices and 404; makes the review-only Editorial public visibility choice explicit; identifies English-only as current review direction rather than approved translated launch; distinguishes the owner's authorized contact-address use from actual contact-profile choice, hosted Cloudflare output, manual accessibility and cutover. Both contact modes accurately reflect current source: default omits contact route; opt-in `candidate-contact` exposes one `mailto:kisuul@idiw.net` and the visible same address. All user-experience tests are marked **NOT RUN** and a realistic evidence/report protocol is supplied for physical phones, no-CSS/JS, keyboard/touch, reflow, forced colors, NVDA/Firefox, VoiceOver/Safari, actual engines and first-time visitors. G-copy, G-contact, G-locales, G-treatments and G-a11y remain **OPEN**, and release/host/cutover remains blocked under existing ledger.

**Issue C1 — stale canonical contact text:** The updated `docs/DECISIONS.md` IDIW-032 accurately records the owner's **authorized public-facing use** of `kisuul@idiw.net`, while the current [canonical approved creator-copy document](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/3a24712988e299c3215199e9985b75334e3678be/docs/content/S1_03_APPROVED_CREATOR_COPY.md#L61-L86) contains active-looking stale instructions at **lines 71, 78, 86**: no exact contact address or mailto is authorized; exact contact destination is undecided; wait until selected and approved. Those statements predate IDIW-032 but are not labeled superseded. Both are source-of-truth documents requested by Issue #23. A future engineer reading canonical copy §4–6 could incorrectly deny the newly approved use or conflate address permission with publication approval.

**Smallest correction:** Put a dated/specific supersession note immediately beside the older contact paragraphs in the canonical copy document, pointing to IDIW-032 and distinguishing **address use authorized** from **contact profile / exact copy / served accessibility / cutover not approved**. Alternatively add an explicit cross-reference in the packet identifying those particular older paragraphs as historical; however fixing the canonical document at its source is preferable. **Do not rewrite the historically approved homepage/About copy or change the profile.** Only one documentation consistency repair, not a contact implementation.

**Severity:** CONDITIONAL ACCEPT as a decision packet; this is a maintainability/authority clarity defect, not a deployed leak or a claim that the decision log itself is wrong. No framework, editorial rewrite, new provider abstraction, user study result or status change justified.

## Evidence

- **Exact issue**: [Issue #23](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/issues/23), IDIW-S1-03B-P, requests one decision packet, classifications of all visitor-facing and accessible copy, current public project evidence, contact alternatives, unexecuted manual test lanes and owner-only decisions; no site implementation or release authority.
- **Pinned PR:** [#24](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/24), head `3a24712988e299c3215199e9985b75334e3678be`, accepted `main@27b13c0011b8dcc88791b46dfe338e8b724517d3`, three Markdown changes (+142/−4). New packet blob `afc5d339aab5774760d1362d9b19d9c4b37c290a`, canonical copy blob `02cc182be60169c6b3a3e8c5abd63971a077ecd4`, root contract blob `33021de00513cb0dc53725693a898e4a5f257ad5`.
- **Source-checked inventory**: `prototype/first-light/src/i18n/en.json` blob `cea37c1de74f770c4f49fed977334a6613e6de21`, `src/content/portfolio.json` blob `8f0dc7fc0a09447c15d5d499eb9a7955641e8be9`, `src/template/page.mjs` blob `13e4a0a1aece71bfe7bfbb9f9a7b4533ddaedb30`, `src/release.mjs` blob `8d24d6354270bb43991a24360ccbf9eda9847b4d`. All draft labels represented without fabricating English string approval. Approved homeowner copy `docs/content/S1_03_APPROVED_CREATOR_COPY.md` §1–3 remains intact; owner decision additions §IDIW-031..033 distinguish factual authority and permission scope. Owner-gate ledger remains open/blocked, as source-diff confirmed.
- **External Auralprint claim**: exact public `cosmicdance-4-2-0/Auralprint1` README `main` independently retrieved via connected GitHub; explicitly says current Release 5 / Build 116 / `v0.1.16`; releases listing confirms tag `v116` published 2026-11-01. This supports version provenance but **not current hosted site runtime, audio, offline support or accessibility**. The packet correctly preserves the Nov 20 GET metadata as historical and labels current Auralprint/KeyLine URL retrieval service failure as `UNVERIFIED`, **not down**.
- **Execution limits:** Reviewed three-file diff, current source and external repo documentation, **no local Node/Chromium suite or full current page rebuild**. PR author states docs-only branch not built; no PR-specific workflow run was found for pinned head. Manual screen-reader, physical-device, real-browser, actual preview-host, email transport, cutover and rollback checks were **not executed**. This is a context-exposed engineering review since the PR description and earlier conversation are visible; no independent other reviewer comment was consulted.
- **Nuance:** The approved creator-copy §4 is a chronology and should not be silently rewritten. A small dated supersession note keeps its provenance while eliminating current conflicting instructions. No change is requested to the old approved exact About paragraphs or historic contact selections.

## Revisit when

The document changes to explicitly supersede the stale canonical contact instructions; the owner selects the final visible contact-copy/profile, project/link wording, locale or Editorial switcher policy; a genuine manual visitor/AT review is completed; or the PR head changes before merger. Re-pin any later acceptance to the new head.
