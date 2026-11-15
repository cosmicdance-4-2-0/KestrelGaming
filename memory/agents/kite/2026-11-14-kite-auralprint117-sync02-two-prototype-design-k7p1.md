---
schema: 1
id: 2026-11-14-kite-auralprint117-sync02-two-prototype-design-k7p1
kind: decision
scope: agent:kite
status: draft
evidence: inferred
author: kite-session
created: 2026-11-14
updated: 2026-11-14
sources: "Axiom user-uploaded Auralprint 117 Team Synchronization 02 (2026-11-07), ap_117_KESTREL@0531e734a2ece59cd877ea8659069efee2e0a905, KestrelGaming agents/kite-v1@778c17e5af2b089033067d7294af2890c9e8a938."
---

# Kite — Auralprint 117 Synchronization 02: two disposable delivery experiments

**Task and recipient:** Team Synchronization 02, independent Kite submission for Axiom, Issue #8: https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/8.
**Loaded application:** `cosmicdance-4-2-0/ap_117_KESTREL@0531e734a2ece59cd877ea8659069efee2e0a905`. On 2026-11-14 the live `main` ref **still matched** this accepted SHA. No newer game/app implementation consulted.
**Loaded individual identity:** Kite — The Unlicensed Inventor, `cosmicdance-4-2-0/KestrelGaming` `agents/kite-v1@778c17e5af2b089033067d7294af2890c9e8a938`; branch-local `AGENTS.md`, `KESTREL.md`, `agents/kite/AGENT.md`, `PROFILE.json`, `kestrel/MEMORY_PROTOCOL.md`, `kestrel/STATE_PROTOCOL.md`, `kestrel/PERMISSIONS.md` and `memory/agents/kite/INDEX.md` consulted. Kite's own project index `memory/projects/cosmicdance-4-2-0/ap_117_kestrel/INDEX.md` was not present at that branch; I do not invent earlier Kite Auralprint reports. A prior branch-scoped user authorization allows Kite's own public continuity record on `agents/kite-v1`.
**Independence:** No other engineer's *new* Synchronization 02 response or Issue #8 comments inspected before this independent first pass. Earlier colleagues' findings are known only as supplied by Axiom's common handoff, not personally reverified or treated as consensus.
**Work authorization:** DESIGN / REVIEW ONLY. No application code edit, new analysis engine, PR, contract acceptance, merge, release or other agent-memory modification. All trial predictions below are unexecuted.

## Summary

**Verdict: ACCEPT owner-established analysis-first/multiple-instrument direction, defer technical delivery choice until one small discriminating trial.** Two cheaper-than-framework candidates:

- **A / synchronous per-window push:** emit each complete `ap117.spectrum/1` window to registered cheap analysis callbacks immediately while preserving existing latest-only `readCurrent()` for displays. Minimal retention; vulnerable to slow, reentrant or faulty callbacks.
- **B / bounded pull journal:** append immutable complete-window observations to a capped ring and allow a complete analyzer to drain by its own sequence cursor; latest-only panel reads current independently. Pacing separation with explicit queue pressure and discontinuity; higher memory/lifecycle cost.

My provisional preference is **A** as the cheapest falsifier, *not a production winner*. Switch to B if measured callbacks stall necessary analysis/source progress, or if an actual analysis consumer requires independent timing. Reject either if it silently drops an observation promised under complete delivery, resurrects stale ready data after reset, alters CP2/CP3-A math, or uses presentation cadence as a clock.

**Key inference:** It is wrong to equate "computed by FFT" with "published to all required consumers." The accepted spectrum assembler may compute multiple complete windows within one `accept` yet return only the final ready cache, which suits rendering but not every-window downstream analysis.

## Source evidence and required alignment

**Owner requirement as paraphrased in the uploaded handoff:** user-configurable panel with independent analyses and visualizers; panels can draw at different rates; a module can provide, consume or both; scientific measurement is not determined by a visualizer; compositing is later. This is architectural intent, not authorization for a plugin framework.

**Accepted baseline:** CP2's validated PCM acquisition, RMS `ap117.measurement/2`, source identity/channel/epoch, copied PCM, source-sample `BigInt` half-open spans; CP3-A `ap117.spectrum/1` one-sided coherent-tone **peak-amplitude** bins, default M=1024/H=512/Nfft=1024 and periodic Hann; two independently modeled Canvas2D views drawn through a host-owned `FrameHost`; analysis independent of rAF. The handoff reports 67/67 accepted Node checks, offline build and browser smoke in GitHub Actions run 42438949177. **I did not rerun these tests.**

**Actual app source verified at pinned commit:**
- `src/analysis/spectrum-stream.js` blob `19c34cb8958c204e1ee529ee2c1adc773c8b37c2`: the sample loop calls `analyzer.analyze(buffer, rate)` at every full window, overwrites `current` and increments `revision` each time, returns only latest `current` from `accept/readCurrent`. `reset` clears PCM/window state, `invalidate` invalidates current while retaining assembler window state; `isCurrent` checks the **live** current revision/status. Multiple windows can have the **same upstream inputPublicationRevision**, so that is not their unique sequence.
- `src/analysis/pipeline.js` blob `25f396217a54501d3ea3565bac1b8e2eb0c46b0f`: CP2 owns readBlock, validates continuity/epoch/terminal state, clones PCM, and publishes distinct RMS revisions. Avoid a second `readBlock` path.
- `src/analysis/fft-amplitude.js` blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`: publishes owned, frozen JS bin arrays and method/window metadata. Neither candidate needs another FFT for matching-window consumers.
- `src/main.js` blob `4c7ffc085da934ff76a4b9e15d611eb6b26b796d`: consumes CP2 publication in `spectrum.accept()` and independently draws latest in `drawFrame`. Accepted host currently **stops analysis on render failure** and invalidates displays; do not silently replace that failure policy.
- `src/config.js` sets spectrum numerical defaults; `src/rendering/frame-host.js` retains the one host-owned rAF loop; `src/visualizers/spectrum-scope/model.js` has no DSP or rendering import and accepts a ready latest spectrum. Source `tests/spectrum.test.js` presently uses small blocks no larger than hop to inspect latest windows one at a time; this does **not** prove four externally delivered windows from one large `accept()`.
- `docs/CP3_FREQUENCY.md`, `docs/ARCHITECTURE.md`, `docs/CHECKPOINTS.md` and app `AGENTS.md` preserve meanings and non-goals.

**Still proposed, not adopted:** C-stream alternative to previous B1 option C/latest-only limitation, a multi-consumer subscriber interface, B2 simultaneous instruments and a putative CP3-B0 checkpoint. The compatible matched-window conversion `P[k]=A[k]^2/(c[k]*ENBW_Hz)` is a normalized PCM-squared/Hz, single-window no-detrend periodogram, not generally CP2 unweighted RMS squared; different window/hop or detrending requires a separate mathematical policy, possibly an independent analyzer on **already acquired** PCM. PSD production, VU, BPM, hardware calibration and physical loudness remain outside this task.

## Fixed structural falsifier (not a new benchmark)

One same-epoch 20-frame synthetic PCM sequence, `M=8,H=4,Nfft=8`, a declared window method and exact sample clock. Compare input **A** (one 20-frame accepted publication) against **B** (8/4/4/4 accepted publications with correct absolute start/end metadata). Expected complete `BigInt` window spans are:
1. `[0n,8n)`
2. `[4n,12n)`
3. `[8n,16n)`
4. `[12n,20n)`

**Important test-construction caveat:** CP2 `createAnalysisPipeline` rejects short *nonfinal* blocks when its configured `blockFrames` is fixed. Do **not** pretend that its ordinary `advance` can emit 8/4/4/4 with `blockFrames=20`; test the exported `spectrum.accept` using bona fide CP2-compatible ready publication fixtures with the complete required RMS fingerprint and contiguous source spans, or use source configurations that are individually valid. Do not weaken an accepted ingress check for convenience.

A **fast complete analyzer** should receive all four windows in source order under the declared no-overrun test conditions, and compare their bins against an independent call of the existing FFT on each exact source slice. A **slow latest-only visual panel** draws once after all input and shows **only `[12n,20n)`** with its valid method/source/epoch/sample span, status and revision. A second independent SignalScope panel can show CP2 RMS simultaneously; no exclusive single "spectrum or PSD" mode is allowed to alter another consumer's math. A latest-only panel may skip displayed intermediate windows intentionally. A complete analyzer may lose data **only with explicit declared overrun/discontinuity**, not silent success.

## Prototype A — push each complete spectrum

**Proposed seam, NOT approved signature:** a narrowly typed `subscribeComplete(callback)->unsubscribe` or constructor `onCompleteWindow` hook on the spectrum stream, alongside the accepted `accept/readCurrent/isCurrent` API. In the existing full-window branch compute the same FFT once, freeze ownership, update revision/current, then deliver the complete observation synchronously in ascending span order. No dispatcher threads, broker, independent PCM acquisition, extra FFT or renderer modifications to prove the basic contract.

**Predicted partition A:** in a single `accept`, callback sees all four windows before the call returns; SpectrumScope's next draw reads last `[12n,20n)`. **Predicted partition B:** one complete observation becomes deliverable after each valid chunk; same ordered four and same final latest. The fast consumer may be a trivial per-window bin-difference collector (not a scientifically certified onset/tempo detector); a same-window PSD *trial* may derive a per-window periodogram with exact lineage, never silently alter spectrum bins.

**Cost:** event delivery O(W*C) for W completed spectra and C subscribers; no required producer historical queue, though subscribers may retain immutable results. Callback execution time is part of `accept`, so a slow synchronous callback can delay the acquisition host; a blocking callback cannot be preempted by a same-thread browser timer. No unsupported realtime guarantee. Reentrant `accept/reset` from callbacks must be rejected or explicitly deferred; subscriber-list mutation must be stable during fanout. A throwing callback is isolated and its own complete-consumer status becomes `faulted/discontinuous`; it must not silently make the next window seem continuous. Whether one subscriber failure stops the *entire* app is an explicit owner decision; current accepted render-failure behavior is not automatically changed.

**Rollback:** remove/disable the added per-window publication seam; the preserved original latest path and accepted FFT/CP2 remain unchanged. Keep trial data outside production or in a separately reviewed disposable branch only after implementation authorization.

**Change-my-mind test:** force callback B to do expensive bounded work or throw on second window while callback A is cheap. Measure `accept` latency, whether A remains complete, any source scheduling impact, and exception/lifecycle behavior. If a slow subscriber reliably violates required progress/robustness, abandon synchronous fanout as the general seam even if its four-window math passes.

## Prototype B — bounded journal with individual pull cursors

**Proposed seam, NOT approved signature:** `readSince(cursor,maxItems)->{observations,nextCursor,status,gap}` plus preserved `readCurrent` for renderer. Provider owns a fixed-capacity ring of already-frozen spectrum observations and a live publication/currentness fence. Consumers own sequence cursors, not PCM state. A cursor carries source/epoch, parameter-generation/method identity, and monotonically increasing *per-window* sequence, not an array index or an upstream CP2 publication revision. `maxRetainedWindows` is configuration with unit "complete spectra"; memory budget scales with retained count × (Nfft/2+1) bins plus metadata. Not a magic universal constant.

**Predicted partition A:** with fixture capacity K >= 4 and no prior backlog, the producer appends four inside one `accept`; fast consumer drains four after it returns, slow renderer reads latest only. **Predicted partition B:** one window is appended per input chunk; fast drains after each or after all while within capacity; both yield same four ordered spans and final latest. Panel drawing cadence is independent of cursor progress.

**Negative pressure pair:** K=2, one atomic 20-frame `accept`, no in-call drain: two early complete spectra are evicted before a pull consumer can read them. `readSince` must report OVERUN with known missing window sequence/range; it must not pretend the last two are a continuous four-window stream. This is a deliberately invalid **complete-delivery test configuration**, not a reason to allocate unbounded buffers. K=4 establishes only the fixed toy; a real accepted block may generate more than K windows before any polling. For a pausable file host, optional bounded backpressure/replay may meet completeness; for a nonpausable live host, explicit gap and invalidation of continuity-sensitive analyzers are mandatory.

**Two analysis cursors:** fast consumer drains and remains continuous; slow complete consumer is deliberately starved until its cursor expires and receives its own overrun, without invalidating the fast consumer or latest panel. The latest panel is not a backlog consumer.

**Lifecycle fence:** supplied Harbor counterexample: ready publication revision 2, missed ready revision 3, upstream reset/invalidate at revision 4. A cached immutable ready-3 object cannot resurrect as current. Consumer/render use must check a **live producer-derived currentness fence** (or an equally complete ordered lifecycle proof) that includes status and reset generation. Retained historical observations may be labeled historical only; reset invalidates live cursors and prevents cross-epoch/parameter mixing. A push consumer also needs this if it can miss an invalidation. Receipt status must distinguish `ready historical` from `current ready` and `invalidated`.

**Cost:** bounded O(K*binCount) spectrum storage, cursor/fence bookkeeping, gap calculation, consumer drain tests and lifecycle complexity. Independent consumer calls cannot synchronously block FFT delivery, but bounded queues do not eliminate CPU bottlenecks or certify hard realtime. No invented throughput/latency claim.

**Rollback:** remove the journal and cursor API; preserve `readCurrent/isCurrent` and original source+FFT behavior. If a ring is unneeded, drop the experimental journal rather than convert it into a global event bus.

**Change-my-mind test:** run the same no-overrun and overload cases, then vary valid accepted input block sizes and consumer consumption patterns. If even a reasonable explicit bound repeatedly loses data needed by fast analyzers while inexpensive synchronous push meets measured budgets, prefer A. If reset/overrun semantics dominate the complexity of the useful functionality, do not ratify B yet.

## Simultaneous instrumentation experience with no compositor

Both prototypes test one fast analysis-only consumer, one slow SpectrumScope latest-only panel, and one CP2 SignalScope latest-only panel. A trivial host-owned list of model/presenter bindings suffices; existing Canvas2D surfaces and single `FrameHost` remain. No layout editor, new render backend, PixiJS/Three.js, new scene composite, or visualizer-driven FFT mode is required.

**Information to communicate (design expectation):** measurement quantity+method/units; source/epoch/channel and exact half-open sample span; ready/waiting/no complete window/faulted/gap; the latest displayed revision and whether it is still current. Repeating a panel's last measurement while paused or drawing slower than analysis is not a new numerical observation. A cached old ready after reset must not be labeled fresh. Source-sample age and wall-clock draw age are distinct; do not infer actual acquisition time from sample index in an offline file. Different window/hop profiles are different provider policies and must be explicitly matched by lineage before reuse. A user hiding a panel must not shut off an analysis consumer subscribed for every window.

## Proposed tests — NOT RUN

| ID | Setup | Falsifiable outcome |
| --- | --- | --- |
| T1 | A/B source partition, fixed M8/H4/Nfft8 | Exactly four source-ordered BigInt window observations for complete consumer under declared guarantee; per-bin oracle parity; latest [12,20). |
| T2 | Frame rate varied, fast analysis + slow draw | Analysis window list unchanged; slow panel intentionally coalesces and does not alter provider window policy. |
| T3 | Push callback throws, reenters or disposes during fanout | Other consumers and provider state remain coherent; failure reported; no silent complete resumption. |
| T4 | Pull ring K=4 then K=2 for one 20-frame accept | K4 may return all four; K2 explicitly reports missing/overrun instead of silent last-only. |
| T5 | Two pull cursors, one deliberately starved | Fast cursor stays complete if capacity/cadence permit; slow cursor reports its own discontinuity. |
| T6 | Ready r2; skipped ready r3; reset/invalidate r4 | Cached r3 cannot become current after r4 under either prototype. |
| T7 | Zero new complete windows, short final source, source replacement/replay | No invented padded FFT; valid last span remains historical where policy permits; reset fences old epochs. |
| T8 | BigInt source frame indices beyond Number.MAX_SAFE_INTEGER; parameter/channel/epoch change | Exact source spans and no accidental cross-revision windows; lifecycle event/gap where required. |
| T9 | Separate same-window periodogram versus distinct PSD window/hop | Lineage correct; no second PCM read; invalid to call mismatched reused bins a new-method spectrum. |
| T10 | Renderer error, late import cancellation, disposed subscriber | No stale ready resurrected; accepted existing host stop/error policy respected until expressly changed. |

**Test evidence categories:** numerical correctness (independent per-window oracle), delivery correctness (ordered/gap/invalid), performance (measured per-host time+bounded bytes), and user comprehension (method, age, status; requires a future human test) are independent gates. No hardware performance, true realtime or PSD/VU/BPM certification is implied. To select a bound, measure maximum complete windows per accepted block, analysis consumer cost and concurrent cursors, and require a named owner decision. Do not invent a success percentage or queue capacity as production canon.

## Recommendation, dissent and boundaries

**Preserve:** accepted CP2 measurement+continuity, accepted CP3-A peak-bin definitions and complete-window assembler, original latest-only renderer cache, host-owned scheduling, source invalidation/reset and EOF behavior, no DSP-driven visual settings, no extra PCM read, no hidden globals. A subscription must not change numerical results or original published measurement meaning.

**Recommend:** authorize a *future* dedicated, disposable CP3-B0-like seam proof (name proposed, not accepted): first measure A vs B in a pure headless fixture with actual producer/consumer APIs and exact four-window comparisons. Only after deciding the delivery contract should B1 PSD and B2 panel orchestration proceed. If matching-periodogram PSD uses spectra from the same FFT policy, derive per window with exact units/method lineage. If distinct method, use an independent analyzer *on the same validated PCM*, not another acquisition.

**Defer/reject:** a generic plugin registry/broker, full PSD/Welch pipeline, certified VU/tempo/onset/beat products, new scene composer, new Canvas/Pixi/Three backends, infinite history, unbounded queues, mic/live device testing, Build 116 port, user-installed arbitrary-code sandbox, mandatory display FPS and mixed-source clocks.

**Dissent:** not every consumer needs complete delivery—latest is a perfectly honest policy when declared. Nor is per-window synchronous delivery a solved architecture merely because it reproduces M8/H4; blocking/callback-fault tests can falsify it. Nor can analysis independently continue through render failure be silently asserted as *current behavior*: `src/main.js` explicitly stops analysis on render failure. Owner must choose any future finer-grained fault containment before it is implemented.

**Uncertainty:** no actual trial, live-device latency, memory/CPU comparison, panel comprehension study, or independent PSD implementation was executed. A's cheapness is an engineering hypothesis, not evidence of a winning design. The handoff's reported accepted CI is historical evidence, not new check results.

**Potential affected app paths if later approved (none modified):** `src/analysis/spectrum-stream.js`, `src/main.js`, `src/visualizers/spectrum-scope/model.js` (only if status/age UI is scoped), `tests/spectrum.test.js` plus isolated delivery/overrun tests; `docs/CP3_FREQUENCY.md` and checkpoint record only under an owner-adopted versioned change. Do not touch accepted measurements, code or other agents' memories during this synchronization.

## Evidence

Exact pinned app files and checks named above were inspected via GitHub at `0531e734a2ece59cd877ea8659069efee2e0a905`. The uploaded Axiom handoff supplies the user requirement and historic status. All proposed APIs, expected results, rollback and comparative performance are **unexecuted design inferences**, not empirical findings. This is a Kite working-perspective contribution under a shared GitHub account, not independent runtime attestation.

## Revisit when

Axiom completes source-pinned reconciliation of the six independent reports; the owner authorizes a bounded implementation trial; a producer/consumer prototype supplies actual window/overrun/fence traces; validated cost measurements support one architecture; or adopted PSD/visualizer method requirements change the minimum delivery guarantee.
