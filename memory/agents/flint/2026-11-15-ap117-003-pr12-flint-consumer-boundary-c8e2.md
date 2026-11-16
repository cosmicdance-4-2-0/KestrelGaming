---
schema: 1
id: 2026-11-15-ap117-003-pr12-flint-consumer-boundary-c8e2
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-ap117-003-pr12-independent-review
created: 2026-11-15
updated: 2026-11-15
sources: "AP117 PR12 head 0880fc8df9182cce9ed2c645e324a2d291375281 vs main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; Axiom issue comment 6907662478; exact source + tests + handoff + GitHub Actions 43789892097; Flint independent source-executed controlled V8 probes."
---

# Flint — AP117-003 PR #12: PSD consumer API, ownership and minimum admission bounds

**Independent verdict: CONDITIONAL PASS in Flint's assigned minimality/API/ownership remit at exactly `0880fc8df9182cce9ed2c645e324a2d291375281`.** Recommend one narrow constructor validation alignment before treating `ap117.psd/1`/the public API as a stable adopted contract. No observed false PSD, accepted CP2/CP3-A regression or complete-window delivery loss in exercised legal cases. **Read-only application review:** no change to the Auralprint PR, merge, deployment, contract ratification or another agent's profile. The independent findings were recorded before consulting any other new PR #12 agent reviews. Shared GitHub account signing is provenance attribution, not agent-runtime authentication.

## Summary

PR #12 adds a single synchronous **subscription-bound PSD transformer** rather than a second acquisition path, FFT, scheduler, generic broker or GUI feature. The accepted spectrum stream and latest display are unchanged. The six new paths are `src/analysis/psd-processor.js`, `tests/psd-boundary.test.js`, `tests/psd-integration.test.js`, `tests/psd-lifecycle.test.js`, `tests/psd-math.test.js`, and `docs/AP117_003_PSD_CONSUMER.md`; all 1,312 added lines, zero deletions, no existing production file changed. The one new production file is 276 lines. Status/provenance ownership remains understandable and reversible.

The second versioned schema `ap117.psd-delivery/1` is justified as a *different kind of thing* from `ap117.psd/1`: one is transport/continuity control, the other a scientific observation. This is not a universal registry or duplicated DSP state. No custom framework is recommended.

### Required bounded correction: align PSD constructor definition with accepted FFT limits

**Severity: MINOR-to-IMPORTANT contract-integrity / construction bounds; non-demonstrated numerical defect.**

**Path:** `src/analysis/psd-processor.js:18-31` `windowDescriptor`. It uses the literal ceiling `n > 2 ** 30` instead of the accepted producer's `maxFftFrames`, even though the processor's caller passes `spectrumConfiguration` including that configured ceiling. `src/analysis/fft-amplitude.js:6-13` requires `fftFrames <= maxFftFrames`, and `src/config.js` sets `maxFftFrames=16384`.

**Independently executed counterexample:** configure `windowFrames=8, hopFrames=4, fftFrames=32768, window="periodic-hann", maxFftFrames=16384`. Supply the constructor an otherwise valid disposable trusted-interface test handle/status (not pretending this is a genuine spectrum producer). **Actual output:** `createPsdProcessor` **accepts** and constructs the window descriptor; `createSpectrumStream` on the identical config rejects `Invalid bounded radix-2 spectrum definition`. If larger M is supplied, the PSD constructor also spends its unbounded-by-CONFIG O(M) summation work before discovering no actual accepted spectrum can match. The 2^30 literal is a second magic admission policy.

**Smallest correction:** require the `maxFftFrames` field to satisfy the already-accepted FFT definition, and `n <= maxFftFrames`; remove the 2^30 alternative. Validate these **before** iterating M window weights. This does not require a new shared validation package or alter PSD math. Alternatively explicitly document a different permitted processor range with an independently justified use case and O(M) construction budget, but current trusted built-in host provides none.

**Requested negative regression:** mismatched `Nfft=32768,maxFftFrames=16384` rejects synchronously with a clear `RangeError`, as does missing/invalid `maxFftFrames`; valid default and valid optional zero-pad configurations still pass. This closes the duplicated CONFIG admission contract without changing accepted functionality.

**Significance:** This is not evidence that legal CP3-A inputs produce wrong PSD. The trusted host will normally construct both objects from the same valid config; I therefore do **not** call this a functional BLOCK on the current headless proof. The owner should decide whether to fix this before ratifying the proposed public contract; my recommendation is yes.

## Evidence

**Pinned PR:** [AP117-003 #12](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12), head `0880fc8df9182cce9ed2c645e324a2d291375281`, base/accepted live main `2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`. Axiom dispatched six reviews in [PR #12 issue comment 6907662478](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#issuecomment-6907662478). I examined that common dispatch **but did not read another engineer's new PR #12 review** before recording this first-pass report.

**Exact files inspected:** `src/analysis/psd-processor.js` blob `8cca1cd0da4e4c79e2182aa3d219d55880f2efb3`, complete 277 lines; `docs/AP117_003_PSD_CONSUMER.md` blob `aa46ec26ac95044cfe0759b15efce64ae6fb1f7c`; all four new tests at exact PR head: `psd-boundary` blob `1b14bd04f206dbd5113aa870a0638cc510c256fd`, `psd-lifecycle` blob `abf439ef4e1fea87346ca9d708406110ea2f2bf9`, `psd-integration` blob `c6c6d059210ae3ac95e4e90b3aece5805de5a242`, and `psd-math` (complete fetched in review). Read `AGENTS.md` blob `52b35815987bec8424e37418a819d9557762aafb`, accepted `fft-amplitude.js` blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`, `spectrum-stream.js` blob `4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc`, and `spectrum-delivery.js` blob `ef19cd748de41226ab0cd8375949e278f7aeb76f`. Read Issue #6, #10 and deferred #11 gate bodies. Own Flint Kestrel `AGENT.md`, `PROFILE.json`, current index, memory protocol loaded from `agents/flint-v1@87fd168a737d02e9ff0ffd11e8df5c8fd743166c`.

**CI independently verified through GitHub:** [Actions run 43789892097](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43789892097) `head_sha=0880fc8...`, completed/success. Read job step report and job log: **119 passing Node tests, zero failed**, 1,312 direct-DFT bins with reported max numerical error 1.5585406229479126e-19, weighted Parseval error 1.5265566588595902e-16; static build, HTML checks, Chromium smoke all completed. This is **CI-observed** under GitHub Actions, not independently executing the full Node/browser suite on this host. Browser smoke exercises the existing page, **not** a production GUI PSD panel.

**Independent source-executed controls:** fetched exact original JS function bodies via GitHub and executed in a fresh V8 evaluator after mechanical `export/import` removal. No production logic was manually replicated in those components, but this is **not** Node module-loader, compiled web bundle, full repository suite or browser test.

- **Real producer→subscriber→processor final20:** M8/H4/N8, accepted Hann, `x[n]=(n+1)/32`, final true; producer status already `ended` with four queued windows, PSD processor status `open`. Four actual `take()` calls returned source starts 0,4,8,12 and independently advancing PSD revisions 2–5, exact valid copied DC densities; fifth `take()` returned `ended(end-of-source)`. No lost final observation and latest spectrum revision remains 5.
- **Capacity 2, four-window batch:** processor reported `break/subscriber-delivery-overrun`, `failureScope=subscriber-delivery`, upstream completion frontier 4; resync returned open with unavailable PSD (no fabricated history).
- **Forbidden external receipt:** `psd.take({status:"observation"})` threw before dequeuing; subsequent no-argument take returned the genuine own-handle item. PSD `densities` were frozen and **not the same array** as accepted spectrum amplitudes.
- **Constructor mismatch:** 32768 above accepted configured max 16384 accepted by PSD constructor, rejected by accepted spectrum producer.
- **Randomized genuine source controls:** **300 independent legal provider/subscriber/PSD runs**, varied M from 4–127, arbitrary H within M, unpadded/padded radix-2 N, rectangular/Hann, 10 source batches per run, 5,038 actual derived observations. All processed without an unexplained `break`; stream stalls/overrun were avoided through capacity-safe per-batch selection and draining. A first deliberately unconstrained fuzz run did encounter expected cap64 overflow under H2 and a 190-frame batch; this is **correct explicit overrun**, not an unexpected contract defect.

**Limits:** no full local npm suite, GUI/browser PSD integration, actual host-miswired handle, hardware/GC timing, hostile same-realm sandbox or independent every-bin DFT recomputation were run by Flint; source + CI evidence is attributed appropriately.

## Ownership, complexity, and compatibility evaluation

**Pass — true capability-bound pulling.** `psd-processor.js:54-69` captures the supplied subscription's `take/readStatus/resync/dispose` operations. There is no public `accept(receipt)` and `take(...args)` throws before any underlying `take()` when arguments are supplied (`:192-196`). This closes the accidental cross-subscription receipt API; it does **not** cryptographically bind a caller-provided handle to a particular producer or prove the trusted host selected the intended source. That authority belongs to host wiring. Same-realm hostile injected wrappers are explicitly outside scope.

**Pass — output ownership and mathematical adapter.** `:134-190` copies/validates the complete recognized `ap117.spectrum/1` fingerprint, expected source and window geometry, finite owned bins, exact BigInt source span, bin spacing, S1/U/gain/ENBW, and monotonically progressed spectrum lineage. Density transform is one O(K) loop; output has a **new frozen numeric array** and frozen span/window/input lineage. No FFT, PCM `readBlock()`, large hidden output queue, renderer polling or independent render clock. The repeated Hann weight formula at the *boundary* is a deliberate independent check of an accepted algorithm: do not turn it into a generic DSP registry merely to save ~10 lines. Keep explicit method/version compatibility so new FFT normalization cannot silently change PSD meaning.

**Pass — two type identities have different owners.** `ap117.psd/1` is a spectral *measurement* and `ap117.psd-delivery/1` is the consumer *status/transport*. The processor's one retained current PSD is separate from the upstream subscription backlog. Two schemas are proportionate; a third generic bus schema is not.

**Pass — currentness and history.** `:99-128,192-263` checks actual handle state before and after synchronous pull; historic same-generation queued spectra are processed despite no longer being the latest spectrum `revision`. Local reset, invalid data or upstream fence makes readiness unavailable until explicit frontier `resync()`. Producer `ended` does not mean PSD has drained; `take().ended` does. Earlier ready PSD objects are true *historical values* after break, not licenses to claim continuous current coverage.

**Pass with deferred trust caveat:** The individual numeric `generation/continuityRevision` fields cannot distinguish two different producer instances with the same source descriptor. This PR's **caller-supplied handle** is the only authority; the code refuses receipt injection but cannot independently verify a wrongly supplied, perfectly legal live handle. A trusted host must retain the actual handle from `intendedProducer.subscribeComplete()` and transfer exclusive ownership. The issue #10 test protects receipt-misrouting but is **not** a proof against miswired construction; if/when a host attaches a PSD panel, use a positive constructor wiring test comparing intended producer and handle provenance without adding global UUIDs or hostile-plugin security claims.

**API naming note (nonblocking):** `psd.reset(cause)` intentionally creates a sticky local unavailable state, unlike `spectrum.reset()` which reinitializes source assembly. The doc explicitly states that `psd.resync()` is required to resume. That distinction must remain prominent in exported documentation; a rename is not necessary absent actual caller confusion.

**Complexity:** Constructor O(M) computes/calibrates one window definition; per `take` O(K) density transform, plus bounded upstream queue's existing O(C) removal. Caller-owned output retention is excluded from processor budget. The current code has no extra PCM/FFT path and is defensibly single-purpose. The out-of-CONFIG 2^30 validation range remains the only narrow avoidable scope inconsistency identified in this remit.

## Severity and owner recommendations

1. **MINOR/IMPORTANT** — `psd-processor.js:18-31`: enforce upstream `maxFftFrames` before window-calibration loop; one small guard and regression. Re-review this changed head. No numerical defect demonstrated under valid actual producer configurations.
2. **NONBLOCKING future host integration** — protect construction-time actual-handle provenance and exclusive ownership in the first host wiring checkpoint. Do not claim that rejecting receipt arguments proves host construction can never bind the wrong valid subscription.
3. **DEFERRED** — Issue #11 operating envelope, browser/real hardware timing, GC allocation ceilings, B2 visualizer, multi-provider broker/scheduler, Welch/history, new DSP method and UI are outside this pure headless PSD proof.

**Dissent:** I reject an abstraction split for PSD/transport solely to avoid two schema labels: the separate labels preserve a meaningful measurement-versus-delivery distinction. I also reject comparing PSD integral to unweighted CP2 RMS² as a mandatory equality; the correctly documented integral is window-weighted mean-square. Do not force independently configured PSD windows through this same-window adapter. A second source/FFT is warranted only if a future mathematical policy actually differs.

**Owner-facing disposition:** **CONDITIONAL PASS**, proceed to Axiom's six-engineer reconciliation. Fix the constructor admission mismatch before adopting the public API, or document an explicit rationale to defer it. Maintain the source-pinned head; no approval transfers automatically to a changed PR. The owner holds merge authority.

## Revisit when

Codex revises the PR head to align config admission, Axiom completes independent six-agent reconciliation, the first actual host/PSD panel implements exclusive handle wiring, or measured operating-envelope evidence demands a different bounded consumer strategy. Retain this first-pass dissent and its exact test limits.
