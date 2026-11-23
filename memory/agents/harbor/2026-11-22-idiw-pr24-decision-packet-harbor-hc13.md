---
schema: 1
id: 2026-11-22-idiw-pr24-decision-packet-harbor-hc13
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-idiw-s1-03b-p-review-session
created: 2026-11-22
updated: 2026-11-22
sources: "IDIW Issue #23 and PR #24 exact head 3a24712988e299c3215199e9985b75334e3678be against accepted main@27b13c0011b8dcc88791b46dfe338e8b724517d3; read PR patch, AGENTS.md, decision packet, IDIW-031/032/033 decision log, current owner release ledger, en.json/portfolio.json/page.mjs/release.mjs/approved creator copy/accessibility/hosting plan; eight isolated source/document-structure checks; no CI run returned for exact head; Harbor home agents/harbor-v1@064b2406a0216481cc52f6cd2c6ca429e6d27353; no real host/credentials/mail/device/merge/deploy accessed."
---

# Harbor HC13 — IDIW Issue #23 / PR #24 publication-copy and visitor-decision boundaries

**Mode:** Independent Harbor specialist review of an [owner-decision preparation packet (Issue #23)](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/issues/23) and the [documentation-only PR #24](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/pull/24). No implementation authority, owner gate decisions, preview deployment, hosted Cloudflare access, DNS or production publication.  
**Application head:** `3a24712988e299c3215199e9985b75334e3678be`, exact PR head at inspection; `main@27b13c0011b8dcc88791b46dfe338e8b724517d3` accepted source baseline. PR is draft, open and unmerged.  
**Harbor home:** `agents/harbor-v1@064b2406a0216481cc52f6cd2c6ca429e6d27353` loaded before review.  
**Disposition:** **ACCEPT as a decision packet for owner consideration**, not an approval of any public copy not already accepted, a source-verification certification, accessibility sign-off, or a release/cutover. **No Harbor-scope merge blocker reproduced.**

## Summary

PR #24 is four documentation-only commits changing **exactly three paths**: new [`docs/reviews/IDIW_S1_03B_VISITOR_REVIEW/DECISION_PACKET.md`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/3a24712988e299c3215199e9985b75334e3678be/docs/reviews/IDIW_S1_03B_VISITOR_REVIEW/DECISION_PACKET.md), [`docs/DECISIONS.md`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/3a24712988e299c3215199e9985b75334e3678be/docs/DECISIONS.md) (IDIW-031–033), and [`docs/reviews/IDIW_S1_04R_RELEASE_CANDIDATE/README.md`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/3a24712988e299c3215199e9985b75334e3678be/docs/reviews/IDIW_S1_04R_RELEASE_CANDIDATE/README.md) (only existing gate notes). No HTML, content catalog, source-link, site, release profile/validator, CI, host, DNS, old portal, independent app or actual contact deployment changed.

**Grounded owner direction:**
- **IDIW-031:** Owner directs a **hold** on final Work/project copy and optional source/download-link placement. Public Auralprint repository paths may move or be renamed. **G-copy remains OPEN**; no permanent source link architecture or implementation was approved.
- **IDIW-032:** Owner explicitly **authorizes public-facing use of the selected `kisuul@idiw.net` contact identity**, extending IDIW-027/029 (selected identity and one owner-reported inbound receipt). This is materially stronger than mere selection, but **not** approval of the final displayed wording, a particular release profile, actual Cloudflare-served HTML, manual screen-reader/no-JS behavior, sending as the address, or apex cutover. The packet/ledger correctly keep **G-contact OPEN** on those distinct tasks. Do not publish underlying private mail routing implementation in review records.
- **IDIW-033:** Owner directs **English only for now**, postponing final launch-language choice until copy is approved. Pseudo/Arabic remain fixtures; **G-locales OPEN** for launch.

**Other decisions:** D-04 treatment/switcher and D-06 manual accessibility are expressly undecided; D-05 notice/404 and D-07 production remain undecided. Do not manufacture an owner decision from a recommendation or CI PASS.

**Contact publication check:** The [current template `contactPanel`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/3a24712988e299c3215199e9985b75334e3678be/prototype/first-light/src/template/page.mjs#L70-L100) emits no address/action/form in default `candidate`/`omit` mode, with the exact `contact.body` text. Opt-in `candidate-contact` emits one visible selected email address, native `mailto:` and explicit copy-if-mail-app-fails explanation. The [release profile](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/3a24712988e299c3215199e9985b75334e3678be/prototype/first-light/src/release.mjs) keeps English, `noindex`, preview notice and no version. The candidate's separate [`renderNotFound`](https://github.com/cosmicdance-4-2-0/i_d_i_w--TEMPLATE/blob/3a24712988e299c3215199e9985b75334e3678be/prototype/first-light/src/template/page.mjs#L222-L284) has a single absolute-root Home recovery link but no contact path. All are already implemented in accepted source; the PR does **not** change them.

## Evidence

### Eight focused source/document consistency checks: 8/8 PASS

Read exact-head docs, current catalog and source code. Executed eight in-memory JS structural/assertion controls against the fetched texts and parsed JSON; no full website build, Node/Chromium suite or live service interaction:
1. Parsed the real release-candidate decision ledger: **13/13 gates** still have state **OPEN** or **BLOCKED**. No gate changed state or became OWNER-DECIDED from this PR.
2. Compared IDIW-032, the packet and `portfolio.json`: public use authorized; final contact/profile/served verification and deployment not asserted. No private forwarding/routing secret was included.
3. Verified default no-address copy and opt-in one-mailto wording keys are distinct and present in `en.json`, matching `release.mjs` contact modes.
4. Checked the four `notFound.*` copy keys against the packet, including the explicit Home route.
5. Checked IDIW-031/032/033 chronology and D-04/D-06 OPEN statuses.
6. Confirmed current-host retrieval errors are attributed as **unverified**, not app outages; all proposed manual NVDA/Firefox/VoiceOver/Safari tests remain expressly **NOT RUN**, and no mail delivery action was claimed in this assignment.
7. Verified **37 relevant catalog keys** and **12 About paragraph keys** exist in the current English source. The approved canonical About is referenced rather than silently rewritten.
8. Screened packet's explicit external URLs for unexpected private/credential/dashboard destinations; no such link found. This is not a comprehensive automated secret scan, nor a guarantee about external links.

The exact three-file PR diff is documentary only (134-line packet, short decision-log additions, short existing ledger-note revisions). The accepted `main` revision equals the requested source baseline; the PR head was `3a24712988e299c3215199e9985b75334e3678be`. No GitHub Actions run was returned for this docs-only exact head. **Do not attribute PR #22's earlier CI result or any future CI to PR #24** without separately verified provenance.

**Independence disclosure:** The task PR body describes its author's partial verdict and source research, so this is **context-exposed**. I inspected source and ran the cited structural checks independently; I did not read other agents' PR #24 review discussions before this report or assert a blind review.

### Nonblocking release-only and handoff boundaries

- **G-contact:** A source-visible `mailto:` is not proof of functionality under Cloudflare Email Address Obfuscation/JS detections, a disabled-script reader, keyboard, screen reader, touch, or mailbox transport. Future protected-preview authorization must precede served-host tests. Testing the click/ability to read and copy the visible address **must not send actual email** merely to demonstrate accessibility. A manually recorded visitor task must distinguish “link opens configured app” from “sent/received message”.
- **G-legacy/G-host/G-rollback:** Current 404 is a useful root Home fallback for unknown paths, but does **not** establish redirects or preservation of old game-portal deep links/assets. Historical portal source and any waitlist records require an owner-approved preservation/disposition plan before cutover. Apex host ownership, Cloudflare edge effects, `www`, and rehearsed rollback remain unverified and independent. A docs review cannot certify them.
- **G-copy/source links:** The owner has explicitly warned repository names and download locations move. Keep primary app discovery separate from optional source/archive link architecture in a *future* scoped decision; do not silently remove or redirect current links in this packet.
- **G-treatments:** Editorial comparison route and switcher **currently ship in the prototype package**; a future choice to make them review-only needs an independently audited implementation, not just a ledger edit. D-04 is OPEN.
- **G-a11y/locales:** Automated Chromium/axe evidence from earlier code does not replace manual physical phone, first-time visitor, no-CSS/no-JS, NVDA/Firefox, VoiceOver/Safari or real engine results. The packet lists concrete procedures and labels each NOT RUN. English-only present review is not an owner decision for final translation/launch locale policy.
- **G-notice/G-indexing/G-version:** Preview notice, `noindex`, `version:null` remain release-profile requirements; nothing here authorizes removal, indexing or version promotion.

**Nonblocking doc consistency note:** Existing `AGENTS.md` retains some historical prose from before IDIW-032 about the contact destination/delivery being unverified; the new decision log and packet carry the newer owner-authorized distinction. That older intro must not be misread as revoking public-use authorization or as current release approval. If the source contract needs a future clarification, handle in a separately scoped documentation change, not an unasked runtime refactor.

**Disposition and limits:** **ACCEPT the evidence-grounded decision packet** for owner review; do **not** close G-copy/G-contact/G-locales/G-treatments/G-a11y or infer live deployment. A final approved production page and an implemented link architecture require independent future review. No credentials, private records, live-site probes, email actions, browser tests, file editing, deployment or release were performed.

## Revisit when

The owner chooses exact D-01/D-02/D-03 final release wording/presentation, D-04 treatment visibility, D-05 notice/404 and D-06 a11y acceptance; a new PR implements source-link/contact changes; protected-preview authorization allows served-host testing; or PR #24 head changes. Re-pin source, distinguish approved owner direction from current draft artifacts and real served results, and retain this packet acceptance as a documentation-only verdict.
