---
schema: 1
id: 2026-11-17-ap117-004-pr13-r1-flint-noop-compatibility-e7c4
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-ap117-004-pr13-r1-focused-rereview
created: 2026-11-17
updated: 2026-11-17
sources: "Codex issue comment 6942893831; ap_117_KESTREL PR #13 exact R1 head bce44420bb7053556a10d40fef97afd91ad9c499; prior reviewed head 2d417adab3f28315c0cbde63048851ae6e44bca8; accepted main bdead48ae672ed6834eae274c8876944a79104bc; production-code source-executed old/new event comparison; GitHub Actions 44047034181 verified."
---

# Flint — AP117-004 PR #13 R1: redundant input compatibility and genuine source fencing

**Task outcome: COMPLETE.** **Verdict: PASS** in Flint's assigned **R1 focused** remit at PR head `bce44420bb7053556a10d40fef97afd91ad9c499` versus previously reviewed `2d417adab3f28315c0cbde63048851ae6e44bca8`; base `main@bdead48ae672ed6834eae274c8876944a79104bc`. The first-pass host/API/ownership PASS remains a distinct, intact, older-head record. No application implementation, merge, deployment, contract ratification, other-agent identity/memory changes or automatic PSD resync authorized.

## Summary

R1 is **one corrective commit, four changed paths**, +162/-16 relative to prior PR head: `src/main.js` (+17/-7); `tests/app-integration.test.js` (+113/-4); `tests/browser-smoke.mjs` (+15/-1); `docs/AP117_004_HOST_PSD_SESSION.md` (+17/-4). No change to accepted CP2/synthetic source, RMS/FFT math, spectrum-delivery, PSD processor, host session, resource budgets, frame loop, package/Node floor or typed publication schemas.

The sole behavioral compatibility change is *intentional and disclosed*: accepted original host invalidated RMS/FFT on every amplitude/frequency `input` event, including a same-value event. The real synthetic-source setter (`src/audio/synthetic-sine.js:50-56`) changes `sourceRevision` **only if the accepted numeric setting actually changes**. R1 checks revision immediately before and after the accepted setter and invalidates both `pipeline` and `spectrum` **only when revision changes**. It always refreshes the visible value and diagnostic and performs the same redraw. This is fewer unnecessary invalidations without weakening scientific change detection.

**Consequence:** an identical-value event no longer withdraws valid RMS/peak data, increments spectrum generation, breaks PSD continuity, changes source clock, drains/creates a new session or forces explicit source restart. A genuine value change still invalidates both RMS and FFT, captures the authorized source revision, fences the PSD session immediately, and retains truthful sticky hold-on-break until source restoration/replacement/replay. The owner still must explicitly accept this hold-on-break UX policy; it is not made more capable by R1.

The extra diagnostic distinctions are appropriate, with no new processing clock: paused eligible association = **“PSD session ready; source paused”**; initial admission failure = **“admission failed; no subscribed coverage began”** instead of fictitious lost coverage; established break = historical last span and **“discontinuity: lost coverage”** with the existing recovery control named. Transport is separately shown. No B2 PSD plot, additional scheduler, stream, queue or generic recovery framework.

## Evidence

**Assignment:** [Codex focused R1 handoff comment](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6942893831). Current PR fetched and pinned open/draft/unmerged, `head=bce44420bb7053556a10d40fef97afd91ad9c499`, `base=bdead48ae672ed6834eae274c8876944a79104bc`. Compared directly with `2d417adab3f28315c0cbde63048851ae6e44bca8`: one ahead/none behind and exactly four paths. Source: [`src/main.js` at R1](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/bce44420bb7053556a10d40fef97afd91ad9c499/src/main.js), blob `6ff041e3e4bc8f0abd046ec52205a119a545f772`; accepted `src/audio/synthetic-sine.js` blob `77f48d03488b888236834530e9910b04780b6af3`; accepted `src/analysis/pipeline.js` blob `25f396217a54501d3ea3565bac1b8e2eb0c46b0f`; R1 app integration `tests/app-integration.test.js` blob `42b81fb8f42bc683e0e3b7444d6370744109f122`. Read full R1 diff, exact old/new handler code and acceptance/test updates.

### Independently executed old/new production-handler comparison

Fetched exact GitHub production source bodies for `createSineSource`, `measureRms/snapshotGeneratorMetadata`, `createAnalysisPipeline`, `createPeakSpectrumAnalyzer`, `createSpectrumDelivery`, `createSpectrumStream`, `createPsdProcessor`, `createPsdSession`, old and R1 `src/main.js` and actual R1 `CONFIG`. Evaluated these **original production functions** in a controlled JS/V8 evaluator after mechanical ES-module declaration removal. The `bindRange` callback was extracted verbatim from the two main source revisions and bound to minimal fake DOM event elements; the harness manually mirrors production's **first ready → native session admission → spectrum.accept → session.drain** in advance calls. Thus **actual handler and science code executed**, but not the complete imported `main.js`, Node test suite or a real browser. The CI integration/Chromium checks independently cover the full host.

**Fixture:** accepted synthetic initial 480-frame CP2 blocks at 48 kHz, periodic-Hann FFT M1024/H512, admitted PSD capacity4. Seven initial accepted blocks produce five genuine PSD windows and RMS publication revision14, peak spectrum revision6, generation1, continuity0. Then two unchanged-value input events, one further block, real frequency 1000→2000, invalid frequency 50000, and a later valid source block.

| Control | Original head `2d417ad` | R1 `bce4442` |
| --- | --- | --- |
| Initial seven accepted blocks | Five PSD windows, RMS revision14, spectrum rev6, PSD generation1/continuity0 | Same |
| After redundant amplitude=0.5 and frequency=1000 events | RMS revision16 unavailable; peak unavailable; PSD generation3/continuity1, broken; source revision still0 | RMS revision14 **ready**, peak **ready**, generation1/continuity0; PSD processing with all five windows; source revision0 |
| Next valid 480-frame block | Source frame starts3360 but PSD remains broken and no new PSD delivered | Source frame starts3360; peak ready; PSD **sixth window delivered**; continuity preserved |
| Genuine frequency 1000→2000 | Source revision1, both measurements unavailable, PSD broken | **Same scientific fencing**, source revision1 and first break `source-parameters-changed` |
| Invalid frequency 50000 | Setter throws `Invalid frequency`, no additional source revision | **Same**; no additional source revision or data admission |
| Later accepted rev1 block | No silent PSD recovery | **Same**: session broken, last healthy PSD historic, peak may need additional FFT samples after segment reset |

Assertions from actual source-execution: R1 redundant event keeps RMS/peak ready; producer generation and continuity unchanged; next completed PSD observation delivered; genuine edit still fences; invalid input still fails without revision advance. All passed. Distinguish source-executed test probes from automated full-main CI. This is a meaningful independent falsification of the reported original failure, not just repeating the implementer test description.

**Exact R1 tests inspected:** `tests/app-integration.test.js:261-322` verifies real `main.js` unchanged-source state/accepted publication, same PSD handle/count/generation, no acquisition/FFT on redundant event, pause presentation with no source clock advancement, then sixth ordinal after resume; `:324-349` verifies real edit and idempotent redundant event preserving pending authorization; `:700-741` tests initial admission failure vs established lost coverage and recovery. `tests/browser-smoke.mjs` confirms paused text, no-op controls, no clock drift and new recovery wording. Read `docs/AP117_004_HOST_PSD_SESSION.md` changed sections L90-128 and `src/main.js` revised lines around diagnostic and handler.

**CI, externally executed not Flint-run:** [GitHub Actions run 44047034181](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44047034181), head `bce44420bb7053556a10d40fef97afd91ad9c499`, completed `success`, one successful job. Directly read actual job steps and logs: **131/131 Node tests, zero fail/skipped**, static build, built HTML official checker, Chromium browser smoke including paused/no-op/revision/fence/EOF/replay/BFCache/offline, representative rendered Nu checks and committed whitespace check. This is actual CI provenance, **not** Flint independently running `npm run verify` or a browser on this host. GitHub Actions used PR merge-ref testing; result is head-anchored by GitHub run metadata. Initial PR head CI remains historical.

## Decision analysis

**PASS — narrower state rule without hiding accepted processing.** The source revision is the accepted signal that a source setter changed the scientific data-generation policy. Ignoring an input with identical resulting source state is scientifically safer than falsely reporting broken continuity. Importantly, R1 only skips `pipeline.invalidate`/`spectrum.invalidate`; it does not skip `setter`, the visible control refresh, the diagnostic update, error handling or `drawFrame`. The source clock still advances only through ordinary `pipeline.advance()`. There is no second source of truth or renderer-controlled DSP policy.

**PASS — real revisions remain authoritative.** Source setter validates input before mutation; after a true accepted change, R1 records the actual `afterRevision` and invokes both invalidations. If a same-value event follows a real edit before the next PCM block, it does **not** clear the pending authorized revision, so the first new-revision block remains lawfully admitted. A real unexpected source revision still causes the existing fail-closed association decision. The latest PSD after any genuine break remains historical; no event silently performs an unapproved resync.

**PASS — minimal diagnostic correction, no new workflow.** The text no longer calls a never-admitted instrument “lost continuous coverage” and no longer presents a paused idle instrument as “processing” unqualified. The existing synthetic-source and Replay/source-selection controls are named as recovery actions. Scientific per-window units, periodogram semantics, no-physical-calibration caveat and two existing Canvas surfaces remain unchanged.

**Explicit compatible-contract change to record:** Prior host behavior did invalidate RMS and peak on every redundant UI event; R1 deliberately drops that effect. This is not bit-for-bit host UI behavior preservation. The behavior was incidental to UI events rather than a valid source-parameter transition, and new tests pin this revision-aware rule. Accepted CP2 and CP3-A public publication schemas, FFT math and source clock remain unchanged.

**No blocker found within Flint's R1 remit.** A subtle limitation remains: the correct actual source (trusted built-in) is required for source revision to represent accepted settings changes; exotic or malicious producers that mutate without revision are outside this checkpoint. Defer Issue #11 realtime/GC and #7 PSD rendering. The owner/Axiom still decide the genuine-edit hold-on-break tradeoff and PR merge. Do not broaden R1 into a generic input-state observer, debounce layer, history reconstruction, or new subscription API.

**Independence and attribution:** This focused follow-up is prompted by Codex's public comment and does not claim blinded review of other PR #13 reports; earlier Flint first pass disclosed one Mothlight review encountered while locating the assignment. This R1 verdict is based on exact R1 source/diff, independently executed old/new probes and separately attributed CI, not reviewer votes. Shared GitHub account attribution does not independently authenticate a running Flint agent.

## Revisit when

PR #13 head changes again; the synthetic source's revision contract changes; Axiom reconciles Harbor/Mothlight's R1 UX and lifecycle reviews; the owner decides hold-on-break recovery UX; or an actual source class lacks meaningful source revision monotonicity. Keep earlier original-head Flint PASS and this R1 targeted PASS as distinct exact-head records.
