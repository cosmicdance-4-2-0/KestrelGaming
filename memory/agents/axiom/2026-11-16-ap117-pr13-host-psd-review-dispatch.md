---
schema: 1
id: 2026-11-16-ap117-pr13-host-psd-review-dispatch
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-pr13-six-review
created: 2026-11-16
updated: 2026-11-16
sources: "Auralprint PR13 exact head 2d417adab3f28315c0cbde63048851ae6e44bca8 vs main bdead48ae672ed6834eae274c8876944a79104bc; Actions run 43844573608 verify job 133221415339; comment 6914016022; src/host/psd-session.js, src/main.js, src/config.js, docs/AP117_004_HOST_PSD_SESSION.md, tests/psd-session.test.js, app-integration.test.js, browser-smoke.mjs, ISSUE 10, Codex handoff 6911643686."
---

# PR #13 AP117-004 — Axiom pre-review source audit and six-agent dispatch

## Observed repo and CI state

Owner relayed Codex completion [PR #13](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13); verified live GitHub source: **open, DRAFT, unmerged, mergeable**, branch `task/codex-ap117-004`, one commit exact head `2d417adab3f28315c0cbde63048851ae6e44bca8` against unchanged `main@bdead48ae672ed6834eae274c8876944a79104bc`. 10 modified/added files, 1069 insertions and 7 deletions. The CI workflow [43844573608](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43844573608) at exact head completed success, and Axiom read its verify job's full log: **131/131 Node tests, zero failed/skipped**, static build, Nu HTML, Chromium offline smoke, four rendered HTML pages and whitespace pass. Local Node24/Chrome observations reported by Codex but not repeated by Axiom locally. Browser smoke reports original two canvases, PSD diagnostic, 2048/481 file cases, synthetic pause/revision, cancellation, rendering failure/recovery and BFCache; no external requests.

## Source-level inspection (not acceptance)

Read `src/host/psd-session.js` (134 lines), `src/main.js` (389), `src/config.js`, [AP117-004 host contract](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/docs/AP117_004_HOST_PSD_SESSION.md), test names/excerpts, accepted spectrum/PSD source semantics from prior planning. `createPsdSession` takes producer/config/source/capacity only; rejects unexpected options, creates a real native subscription itself via the producer, gives exact handle to `createPsdProcessor`, ensures producer capacity admission and cleans up after failure. Returns only `drain/readStatus/readCurrent/dispose`; owned per-call bounded result and latest immutable scientific observation; no external receipt. `CONFIG.psd.capacityObservations=4`; capacity+one-control synchronous drain. `src/main.js` installs from real CP2-ready measurement/span before same-input spectrum.accept; drains immediately after successful accept; distinct source/session lifecycle cleanup, typed diagnostic with aria-live=off, source/canvas/peak/PSD differentiation. No accepted CP2, FFT/PSD math, producer delivery, presenter, FrameHost or source code changes. New package engine Node>=22.15 matches registerHooks test harness; no deps changed.

**Initial source-level verdict: no confirmed blocker but REVIEW HOLD until independent six-agent reports**, no unnecessary code rewrite or merge. Noted precise review concern: **hold-on-break** intentionally leaves PSD unavailable after any slider spectrum.invalidate, until source restoration/replacement/replay; source continues measuring RMS/peak. This is explicit, scientifically honest and potentially a significant usability choice, not automatically a defect. Have Harbor/Mothlight/Latch assess intended contract. Producer-supplied handle is native but host still must choose the correct producer; no claim of hostile plugin or wrong-producer authentication. Issue #11 measured CPU/GC remains separate.

## Independent dispatch

Codex initially posted [PR #13 review requests comment 6913221997](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6913221997). Axiom posted [supplemental, source-pinned detailed six-agent handoff comment 6914016022](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6914016022). All must load own identity/contract/memory, read actual exact PR code, preserve first-pass independence/dissent, post PASS/CONDITIONAL/BLOCK with reproduced failure vs source inspection and any individual memory. Shared GitHub account signatures are attribution, not separate auth. No app mutation/merge/deploy.
- Flint: origin helper API, native handle/ownership, creation-before-accept, teardown, engine>=22.15.
- Latch: wrong producer vs wrong subscription, equal-stamp two producers, late B/future-only, no false authentication.
- Harbor: actual main lifecycle, EOF/final backlog/failure, import cancellation/replay, disposed consumer, no premature final.
- Mothlight: textual diagnostic truth and read-only accessibility, historical vs live, canvas coalescing, hold-on-break UX.
- Gauge: exact clock/epoch/channel/original FFT input revisions, all windows/partitions/Parseval, no second FFT.
- Kite: capacity4+one control, M8/H1 overflow, bounded retained status, no new source/callback/timer, #11 scope.

## Status / stop

Issue #10 remains open until exact-host review and owner acceptance. Owner controls adoption/merge. If actual current-scope blocker appears, assign one bounded Codex correction to same draft PR then repin SHA. If reviews pass, Axiom reconciles and owner decides merge; full PSD UI remains Issue #7 and FFT CPU/GC workload Issue #11 deferred. Axiom made no application change.
