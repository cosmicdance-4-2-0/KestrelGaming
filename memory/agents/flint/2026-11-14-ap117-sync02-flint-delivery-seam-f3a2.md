---
schema: 1
id: 2026-11-14-ap117-sync02-flint-delivery-seam-f3a2
kind: lesson
scope: agent:flint
status: active
evidence: inferred
author: flint-ap117-sync02-independent-session
created: 2026-11-14
updated: 2026-11-14
sources: "User-provided Auralprint_117_Six_Engineer_Synchronization.md (Axiom synchronization 02); ap_117_KESTREL main@0531e734a2ece59cd877ea8659069efee2e0a905; Flint own branch@2a47b5eb21a75cb62cd429661d37dd8e66d00910; own CP3-B1 challenge and actual CP3-A sources."
---

# Flint — Auralprint 117 Sync 02: bounded complete-window delivery without a broker

**Assignment:** Axiom's Team Synchronization 02, independent Flint design response. **Outcome:** COMPLETE, design-only independent first pass; later reconciliation is Axiom's responsibility. **Verdict:** **ACCEPT the owner's analysis-first, independent-cadence instrumentation intent; CONDITIONAL RECOMMENDATION for a small per-subscriber bounded pull queue plus existing latest view.** No app source, PR, integration, shared schema, or other agent's memory was modified.

## Summary

The CP3-A spectrum window assembler and Fourier normalization need not change. **Its delivery contract does.** A spectrum stream currently computes every complete FFT window internally but overwrites `current` for each. `readCurrent()` therefore cannot serve a complete-window analyzer, and a PSD derived from that latest only cannot reconstruct lost earlier FFT windows. Keep the existing `ap117.spectrum/1` numerical/publication shape and `readCurrent()` for the renderer. Add one **narrow stream-specific subscription seam**, with a bounded owned mailbox per complete-delivery subscriber; enqueue each full owned/frozen spectrum observation once per completed window, in source-window order, *without running consumer callbacks during producer `accept()`*. Subscribers explicitly pull/drain their own queue. A renderer remains a deliberate latest-value reader, with source span, status and producer currentness checks; it need not subscribe to every window.

This is **not** a general pub/sub broker. No dynamic topic registry, cross-provider routing, reactive scheduling framework, new PCM source reader, second FFT for same-window derived PSD, interchangeable FFT internals, scene compositor or guaranteed realtime losslessness is required.

**Critical finding unique to this remit:** the exported `createSpectrumStream.accept` currently checks `Float32Array` samples for finiteness *inside* the per-sample loop. If a proposed implementation calls external subscriber callbacks as soon as each window completes, a forged CP2-labelled block with several valid initial windows followed by a nonfinite late sample could expose “ready” windows **before** `accept()` throws and resets to unavailable. Consumer reentrancy or a callback exception could similarly interrupt a block halfway through. A non-reentrant pull mailbox gives the host a clear publication/rollback/fault boundary. Prevalidate the entire incoming PCM block (or prove the entire ingress is already validated); on any later producer exception, fence and flush all unconsumed events from the affected generation and report an explicit break, never allow a half-failed `accept` to claim continuous stream delivery.

## Evidence and source receipt

- **User attachment inspected in this session:** `Auralprint_117_Six_Engineer_Synchronization.md` by Axiom, prepared 2026-11-07, sections 1–9. This is a human-dispatched shared architecture design request, not implementation authorization.
- **App baseline actually fetched:** [`cosmicdance-4-2-0/ap_117_KESTREL@0531e734a2ece59cd877ea8659069efee2e0a905`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/0531e734a2ece59cd877ea8659069efee2e0a905); confirmed live `main` matched at inspection. Project `AGENTS.md` blob `52b35815987bec8424e37418a819d9557762aafb`; `docs/ARCHITECTURE.md` `546e5b7083a2972db7bc7bd6fe016bb4ba6f0142`; `docs/CP3_FREQUENCY.md` `0d65f1aa912cd3c7d19884c4472acc8622172e28`.
- **Actual app source:** `src/analysis/spectrum-stream.js` blob `19c34cb8958c204e1ee529ee2c1adc773c8b37c2`; `src/analysis/fft-amplitude.js` `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`; `src/analysis/pipeline.js` `25f396217a54501d3ea3565bac1b8e2eb0c46b0f`; `src/main.js` `4c7ffc085da934ff76a4b9e15d611eb6b26b796d`; `src/rendering/frame-host.js` `a1e0a88cbd3cd61926c35b5191d12cb89251e805`; `src/config.js` `414e695e4fc5f00f0c388e9f87fa9c756ac333f6`. Relevant current tests `tests/spectrum.test.js`, `tests/publication-integrity.test.js`.
- **Own persona:** `cosmicdance-4-2-0/KestrelGaming@agents/flint-v1`, verified home head **`2a47b5eb21a75cb62cd429661d37dd8e66d00910`** before this record. Read own branch-local `AGENTS.md`, `KESTREL.md`, `agents/flint/AGENT.md` (`b56d89557a84ddd9f3c234cc4c7ace0ffa6ee76c`), `PROFILE.json` (`b6391d89c44152ce44fbf16bdba1f3deb44fdefe`), own memory index, `MEMORY_PROTOCOL.md`, `PERMISSIONS.md`, `STATE_PROTOCOL.md`, `kestrel-remember` and own CP3-A/B1 records. These design records do not authenticate a separate operating agent.
- **Own earlier executed structural finding:** `memory/agents/flint/2026-11-07-ap117-cp3b1-flint-psd-architecture-challenge-s9c1.md` at blob `7d555c6580fe1098c59f0a952b3125c39edd90f9` records a controlled V8 source-executed M8/H4/20-frame probe. The new synchronization did **not** rerun that probe; it cites the preserved evidence.
- **Independence limit:** No newer Sync 02 reply from Gauge, Harbor, Mothlight, Kite, Latch, or Axiom's post-handoff reconciliation was inspected before writing this first-pass report. The dispatched shared document's attributions to historical Gauge/Harbor findings are not independent review of those new replies. No local app checkout, Node suite, CI rerun, browser/device/latency test or actual new provider prototype was executed for Sync 02.

## 1. Contract status: what is required and what remains a proposal

**Owner-established direction:** user-composable instrument panel, separate acquisition/analysis/consumer and render clocks, typed mathematically honest observations; provider-consumer modules may be both; renderers do not dictate DSP or data availability; accepted working prototype must survive. Complete/ordered analyzer delivery must either deliver every complete observation or **truthfully expose discontinuity** under bounded resource pressure. Latest rendering may deliberately coalesce. Same samples must not be reacquired merely to feed another consumer.

**Accepted baseline:** CP2 strict single source/cursor, finite normalized Float32 PCM and RMS `ap117.measurement/2`, copied waveform; CP3-A FFT spectrum method `ap117.spectrum/1` one-sided coherent-tone peak amplitude with documented Hann/window geometry; current `readCurrent()` latest-only contract and dual Canvas2D host frame loop. The accepted post-merge CI result **67/67** in Axiom's handoff is attributed there, not rerun by this reviewer.

**Still proposals:** a C-stream source of every completed spectrum, new delivery contract and its data/queue ownership, B1 PSD derivation policy, B2 panel selection, a general subscriber API, any cross-provider graph, and any later host rendering-failure isolation change. My earlier latest-only Option C was conditional on the then-specified B1 behavior and **does not veto** a new analysis-first requirement; the broader requirement now changes the correct recommendation.

**D3/latest-only:** no accepted exclusive selection of PSD versus amplitude panels; any prior UI selector is a **prototype convenience**, not an architectural exclusivity promise. **B1 C vs A:** same-window, no-detrend, one-periodogram PSD may reuse each complete CP3-A spectrum via `P[k]=A[k]^2/(c[k]*ENBW_Hz)`; independent window, detrending, Welch or averaging belongs to another provider/PSD algorithm and must not silently consume an incompatible amplitude stream.

## 2. Minimal seam: one provider, two delivery modes

Retain `createSpectrumStream` and `accept(validatedCP2Publication)`, `reset`, `invalidate`, `readCurrent`, `isCurrent`. **Propose one new narrow operation** `subscribeComplete({capacityObservations})`, returning an owned handle with `take()`, `readStatus()`, `resync()`, `dispose()`. This is an **illustrative API**, not agreed naming or production code. The existing `readCurrent()` remains the latest renderer operation; no second “latest subscriber” queue is necessary yet.

- Each complete FFT result is an existing **owned/frozen** `ap117.spectrum/1` measurement/publication with exact window sample span, `sourceEpoch`, `sourceRevision`, channel, tap, sample rate, CP2 `inputPublicationRevision`, provider publication revision, method, units, ENBW and M/H/Nfft. **Do not re-label it PSD.** Delivery wraps this publication with one narrow event type `ready | break | terminal`, provider generation and monotonic ordinal. The event schema needs explicit versioning only if exposed beyond the internal narrow `SpectrumStream` seam; do not invent a universal measurement registry.
- **Complete subscriber:** producer appends a frozen observation **reference** once to each active subscriber's bounded ring. Each handle owns only its cursor/queue, not the underlying science or sample clock. Separate subscribers drain at different schedules; one slow consumer does not block a fast one. They may process historical same-generation observations in source order, but may not relabel an old observation as the producer's current state.
- **Latest renderer:** reads `readCurrent()` and producer's live state; can repeat an unchanged revision without creating a new publication. The latest may be historic relative to source time (including clean EOF) and must show its source interval and status; render cadence does not create new measurements.
- **No callbacks during `accept`:** provider code must never execute arbitrary consumer code, eliminating callback-induced reentrancy, exceptions and unbounded processing from the producer's hot loop. A scheduled host may notify that work is pending **after** `accept` completes; such notification is advisory and never invokes subscriber computation inline. Polling alone is sufficient for the first proof.
- **Configuration:** one provider instance owns **one immutable FFT/window policy** (`windowFrames`, `hopFrames`, `fftFrames`, window kind, method). Compatible consumers can share it without a second transform. A different valid consumer window/hop/detrend policy requires **another provider instance** that consumes the **same already accepted CP2 waveform copy**, not another PCM source read. This may legitimately require a distinct FFT and different computational work. It does not warrant a global FFT configuration imposed by a display. `CONFIG` remains authoritative for actual selected defaults/limits; subscription cannot mutate the producer's DSP parameters.
- **Subscription start:** only windows produced **after** successful subscription can be guaranteed. Joining an already-running provider is explicitly “from now”; a history request is not implied. Subscribe before acquisition for a full-file guarantee. Subscription and disposal are idempotent/bounded; disposal drops that subscriber's owned queue but cannot reset the source or other consumers.

This is a **few-state FIFO, not a broker**: no topic strings, user-supplied filters, dynamic type coercion, event-sourcing database, worker scheduler, global subscriber map, replay persistence or cross-module authorization graph. The host wires a known provider to known typed consumers.

## 3. Admission, pressure, resets and error boundaries

**Each complete-delivery subscription promises either ordered delivery or a visible break, not unlimited lossless realtime computation.** Its capacity (count of complete observations) is a named finite `CONFIG` value chosen by expected maximum atomic PCM burst and memory budget. Capacity is per subscriber, not a universal number forced by a renderer.

**Overrun policy (recommended simplest):** a subscriber whose queue would overflow enters a latched `overrun` state. Discard its unread queue, retain an **out-of-band sticky gap/fence record** with expected/dropped publication ordinal range and affected source spans when known, and stop enqueuing for that subscriber until it explicitly `resync()`s. Its next `take()` must report the gap **before any newer ready**, even if the full queue prevented an ordinary control message from fitting. Resync may start only from a subsequently completed window/new segment and must disclose that prior continuity was not recovered. This is deliberately strict, inexpensive, and safe for onset/tempo algorithms that cannot interpolate missing windows.

**Same-generation older observations** remain legitimate as *historical* analysis while no gap has occurred and the producer is ready. **Currentness differs from historical validity.** A producer-wide live generation/fence identifies source replacement, invalidation, parameter-revision segmentation, replay, or disposal. A reset/invalidation must invalidate every subscriber's queued **current** work, clear outstanding records or explicitly preserve them only as historical with a guaranteed ordered lifecycle event, and expose an unmissable sticky break. I favor **flush and fence** for first proof: fewer states, no frozen-ready resurrection if a consumer missed an invalidating event. A cached ready object is never accepted as *current* without checking the producer's live fence/status; a frozen object alone is not evidence of currentness.

**Segment break:** changing sourceRevision within the same sourceEpoch clears partial FFT assembly; a complete-only algorithm may see a jump larger than H and must get an explicit `parameter-change`/new-segment event, not silently assume adjacent windows. Keep BigInt half-open PCM spans; do not derive producer time from rAF or arrival times. Reset/new epoch has independent source identity even when the sample counter restarts.

**Source transition:** replace/replay/channel change, canceled/failed file import, dispose and fault fence the provider and subscribers. Clean EOF after at least one window may retain a truthful **historical** latest complete span; a short final file yields unavailable/insufficient-window, never zero-padded fictional bins. `EOF — REPLAY REQUIRED` on ambiguous post-final failure remains distinguishable from clean EOF. `pagehide` disposes; any late callback must fail against a closed generation. No hidden automatic replay.

**Consumer exception:** no user callback executes inside producer `accept`; a thrown PSD/visualizer consumer occurs during its own drain or host/render cycle. That consumer's handle can be marked failed/disposed without corrupting other subscribers. Do **not** silently alter accepted application-wide render-failure transport behavior in `src/main.js`: currently `failRendering()` stops acquisition and invalidates both publications. Independent panel failure isolation is an **owner decision for a later checkpoint**; analyze and propose a transition with prior EOF/failure regression tests, not a stealth change in this design pass.

**Atomic acceptance risk:** today the spectrum stream's `accept()` validates a waveform's finite samples while iterating. With synchronous per-window consumer callbacks a forged, otherwise label-correct block with valid early samples and NaN near its end could emit multiple callback-visible ready measurements before `accept()` throws and resets. For the new seam either **prevalidate the full incoming PCM payload before the first enqueue** or guarantee producer commit/error fencing is atomic against subscriber `take()`; no consumer code may run during `accept()`. On any late analytical failure, flush any unconsumed partial-batch output and surface a fault/break before anyone observes apparent continuity. Do not weaken CP3-A ingress validation or presume a `ready` string authenticates CP2 provenance.

**Overflow during a single `accept()` is real.** A capacity of two cannot handle four same-call windows just because a subscriber is otherwise “fast”: pulling occurs only *after* accept completes. The proof must configure capacity sufficient for the atomic batch, or explicitly accept an overrun. For pausable files, a **later optional** bounded admission/backpressure policy may pause *before* accepting the next CP2 block, rather than promising arbitrary queue growth. For live sources, declare loss and invalidate dependent algorithms; no unlimited lossless realtime guarantee.

## 4. Smallest falsification proof: M8/H4/20

Use a pure Node/headless fixture with `M=8`, `H=4`, `Nfft=8`, 20 identical finite normalized Float32 samples, a fixed CP2 sourceEpoch and valid `ap117.measurement/2` lineage.

| Input partition | Complete-delivery subscriber with capacity >= 4 | Latest `readCurrent()` |
| --- | --- | --- |
| One 20-frame block | `[0,8), [4,12), [8,16), [12,20)` in this order | Only `[12,20)` |
| Blocks of 8, 4, 4, 4 | **Same** four spans, exact same FFT bins | Same final `[12,20)` |

Check each spectrum matches the existing unmodified FFT method, same source window/ENBW and publication provenance; compare per-window PSD `A^2/(c ENBW)` against an independent direct-DFT periodogram oracle, with DC/Nyquist factor 1 and interior factor 2. There is exactly **one CP2 acquisition** in each partition and no extra FFT for compatible downstream PSD. A repeated latest read does not generate another analysis event.

**Slow-consumer control:** subscribe two complete consumers, capacity `C`. Drain the first after each accepted block; leave the second undrained until its queue exceeds `C`. The first receives all windows; the second receives explicit sticky `overrun` and cannot silently continue. A fresh `resync()` restarts from a documented new segment/window boundary. Renderer continues seeing the correct latest. Use the **one 20-frame atomic burst** with `C=2` as a separate control: **both undrained complete consumers overrun**, even if one would normally drain quickly. This prevents a false claim of infinite intra-batch consumption.

**Reset/fence counterexample:** producer presents ready rev 2; it later produces rev 3; an invalidation/reset reaches rev 4 while a subscriber has not drained. Cached ready rev 3 must **never** be returned as freshly current after rev 4. Poll either reports a reset/fault fence (and discards pending events) or labels a retained earlier record historical under a rigorous ordered protocol. For the chosen flush-and-fence design, the next poll must report the break first.

**Transactional acceptance:** a CP2-labelled but internally invalid waveform with several finite initial FFT windows and a later NaN must yield **no callback-visible partial ready delivery**, then an explicit fault/fence. A subscriber throwing during `take()` or during its later processing cannot throw into the producer, advance its PCM cursor or break another subscriber.

**Other negatives:** partial PCM produces no window/new ready event; sourceRevision changes mid-assembly create an explicit segment; sourceEpoch/channel/reset/replay/EOF handling, duplicate/forged metadata, disposal, BigInt spans above `Number.MAX_SAFE_INTEGER`, and exact publication order independent of PCM block partition. No comparing an integrated PSD with unweighted CP2 RMS² except when analytically warranted. Explicit stale/dropped information is not “valid continuous measurement.”

**Evidence gates:** (i) *mathematics* — independent numeric periodogram oracle, intact FFT output; (ii) *delivery* — exact four ordered events for both partitions or an explicit configured overrun; (iii) *lifecycle* — no reset resurrection, proper fault/EOF behavior; (iv) *source cost* — readBlock call count unchanged per accepted source batch and no second FFT for same-window PSD; (v) *UI/cadence* — renderer consumes latest at arbitrary draw times without affecting analysis. No synthetic result certifies device timing, calibrated physical metering or hard realtime.

**What changes my mind:** if measured bounded pull queue memory/copy pressure becomes unacceptable relative to an exception-isolated, non-reentrant callback handoff with equivalent backpressure/gap and reset guarantees; or if an independently released provider/consumer ecosystem truly needs a generic type registry, subscription graph, multiple execution threads or arbitrary client modules. Do not buy those abstractions before they are demanded and demonstrated.

## 5. Alternatives and explicit disagreement

| Design | Benefit | Defect or cost |
| --- | --- | --- |
| Existing `readCurrent()` only | Proven minimal display interface | **Fails** all-window contract under large PCM blocks; no retroactive reconstruction |
| Synchronous per-window callback fanout | Fewer queue structures; zero extra mailbox polling | User callback can throw/reenter, stall source, mutate subscription list mid-iteration or observe intermediate block outputs; one slow consumer blocks all unless additional scheduling/exception semantics are introduced |
| **Per-subscriber bounded pull queue + latest view (recommend)** | Isolated consumers, ordered bounded delivery, explicit overrun, no subscriber code inside source loop, preserves latest rendering | Queue/cursor/fence logic and bounded memory per consumer; no lossless guarantee beyond configured capacity |
| Generic typed broker/DAG/event service | Potential arbitrary modular routing and scheduling | Unproven abstraction, type registry, lifecycle states, pressure policies and ownership surfaces beyond this proof |
| Independent PSD source and FFT | Allows independent PSD window/detrend/averaging | Another FFT computation (not another PCM acquisition) when same-window bins already suffice; do only if mathematics requires it |

**Axiom's C-stream** is therefore a worthwhile **hypothesis**, not an accepted implementation. Option C is compatible with every-window delivery *only after* the stream provides every complete compatible spectrum. Option A remains scientifically appropriate whenever the user selects independent PSD geometry or estimand. Defer both implementations until an owner-authorized delivery proof.

## 6. Owner review questions and explicit non-goals

1. Select **bounded pull** vs **callback** on the observed full-block/reset test, not lines of source code alone.
2. Define whether subscriber overflow is a **sticky fatal continuity gap** (my preference) or recoverable item-by-item loss; any recoverable design must preserve exact missing intervals and consumer invalidation.
3. Decide whether first proof targets a **single configured provider** plus one complete PSD analyzer and one latest renderer, or already includes two differently configured FFT streams. I recommend the former, with an explicit future second-provider compatibility fixture.
4. Clarify app-wide render failure ownership before enabling renderer isolation; keep accepted CP3-A fault/EOF behavior until a reviewed host change.
5. Name configuration `subscriberCapacityObservations`, provider FFT window/hop/method, and live/pausable admission policy in the actual `CONFIG` hierarchy. Avoid invented global defaults or renderer-controlled DSP policy.
6. Version a cross-module delivery event **only at its actual boundary**, leaving `ap117.spectrum/1`, CP2 schema and Fourier normalization untouched until a justified compatible change. A source revision/epoch fence is not a wall-clock scheduler.

**Not in scope:** PSD production, B2 UI, BPM/onset/VU certification, plugin sandboxing, scene mixing, Pixi/Three, device latency, Build 116 presets, generic source capture or actual realtime hardware tests. A first proof should modify only a narrow spectrum delivery seam and its negative tests **after separate owner implementation approval**.

**Attribution, dissent and status:** independent first-pass Flint reasoning under a shared GitHub account. No other engineer's new Sync 02 findings were consulted before this authored record. The earlier CP3-B1 latest-only choice was correct *under its own constrained assumptions*; the new owner requirement changes the target. Do not infer consensus. Full evidence for actual Sync 02 behavioral verification remains future work.

## Revisit when

Axiom reconciles six real independent responses, owner authorizes the narrow delivery checkpoint, a controlled M8/H4/20 headless test confirms or contradicts queue semantics, or a future consumer requires independent FFT geometry, guaranteed offline replay or stronger realtime scheduling. Re-pin the accepted baseline and preserve the old latest-only display semantics and unrelated CP2/CP3-A stability fixtures.
