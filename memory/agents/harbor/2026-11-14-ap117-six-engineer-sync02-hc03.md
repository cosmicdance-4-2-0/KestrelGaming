---
schema: 1
id: 2026-11-14-ap117-six-engineer-sync02-hc03
kind: lesson
scope: agent:harbor
status: draft
evidence: inferred
author: harbor-chat-sync02-2026-11-14
created: 2026-11-14
updated: 2026-11-14
sources: "User-provided Auralprint_117_Six_Engineer_Synchronization.md (Axiom's Team Synchronization 02, prepared 2026-11-07); accepted ap_117_KESTREL main@0531e734a2ece59cd877ea8659069efee2e0a905; KestrelGaming Harbor home agents/harbor-v1@522b036a6187a0dc682c9b7aae2358e60623018b; existing Harbor CP3-B1 reset-fence and CP3-A lifecycle records. Read-only code inspection on 2026-11-14; no new peer synchronization responses read."
---

# Auralprint 117 — Harbor Synchronization 02: Analysis delivery, continuity, and truthful gaps

**Task:** Axiom's six-engineer design synchronization; independent Harbor first pass.  
**Destination:** [Auralprint Issue #8](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/8).  
**Accepted application source:** `main@0531e734a2ece59cd877ea8659069efee2e0a905` (current `main` matched at inspection).  
**Harbor source:** `agents/harbor-v1@522b036a6187a0dc682c9b7aae2358e60623018b` before this report.  
**Report type:** DESIGN ONLY; no application code, PR, deployment, merge, shared contracts, or other agents' memory edited.

## Summary

**Independent judgment: SUPPORT THE OWNER'S ANALYSIS-FIRST INSTRUMENTATION REQUIREMENT, CONDITIONALLY SUPPORT A SMALL STREAM SEAM.** The owner's durable requirement is that analysis measurements are accurate, independently consumable, and not paced or mathematically defined by rendering. Provider/consumer/both roles, simultaneously configurable instruments, and distinct complete versus coalesced delivery are real needs. They do **not** constitute acceptance of C-stream, a new subscriber API, or B1 option C. The earlier B1 option-C latest-only restriction (D3) is reopened, not already superseded by executable code. PSD conversion is valid only for Gauge's specified matched-window method and is not general PSD, loudness, VU or tempo certification.

Harbor's central invariant: **a once-valid historical FFT observation must remain historically attributable, but may never become freshly current after producer invalidation/reset merely because its frozen publication revision exceeds the consumer's previous stamp.** "Complete" additionally means **every completed observation is received in source-frame order, OR a detectable loss/overrun occurs**; bounded queues do not promise lossless live delivery. Treat a consumer loss as a discontinuity in **that consumer's derived-series validity**, not automatically as a fault in the shared PCM source.

## Evidence: exactly what the accepted source does

1. [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/spectrum-stream.js) accepts already-validated CP2 RMS waveform copies, checks source/epoch/tap/channel/clock/source-revision and BigInt spans, assembles overlapping FFT windows, bumps a spectrum publication revision for each completed window, but retains only `current`, the latest ready window. `readCurrent()` cannot supply all windows from one 20-frame accept. `invalidate()` bumps revision and withdraws current without resetting assembler chronology; `reset()` additionally clears partial window/source identity. `isCurrent(revision)` checks only the **latest** ready snapshot. Reusing it to authenticate *historical complete-stream* events would incorrectly reject legitimate older windows.
2. [`src/analysis/pipeline.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/pipeline.js) publishes copied PCM from strict contiguous source epochs, detects post-final/early EOF and latches protocol faults. `src/main.js` advances one CP2 block and feeds CP3-A without a second source read. Source selection/import/replay/channel switching is host-owned; current render faults stop the single host timer and both displays, invalidate both publications, and require explicit Retry render. A final-block render failure has the existing `EOF — REPLAY REQUIRED` path. These are **accepted CP3-A behaviors**, not evidence that the future multi-panel design already isolates renderer failure.
3. [`src/audio/file-import.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/audio/file-import.js) fences canceled/late asynchronous imports using a generation token. [`src/rendering/frame-host.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/rendering/frame-host.js) owns rAF, stops on present/schedule exceptions, and is separate from analysis timing. `pagehide` disposes source, importer and both backends; persisted pageshow reloads. Do not resurrect late callbacks after those boundaries.
4. [`docs/CP3_FREQUENCY.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/docs/CP3_FREQUENCY.md) defines `ap117.spectrum/1` as one-sided coherent-tone peak amplitude, not PSD. Its window spans are half-open **source-frame** intervals, not rendered frames. Published FFT bins are `Float64Array`-like owned numeric data; consumer mutation/read-only ownership is an interface concern, not a reason to change FFT arithmetic.
5. Existing [Harbor CP3-B1 source-executed counterexample](2026-11-07-cp3b1-psd-reset-fence-he01.md): producer emits ready revision 2; downstream misses ready revision 3; producer resets to unavailable revision 4. A retained ready-3 object is `> lastConsumed=2` yet stale. That old fixture was executed against CP3-A source; **no event/subscriber implementation has been executed here**.

**Status distinctions:** This report directly inspected the accepted source and prior Harbor evidence. It did not execute the current test suite or prove any candidate subscription behavior. Axiom's uploaded sync describes accepted 67/67 Node tests, offline build and Chromium smoke at the post-merge action; these are attributed to the historical CI, not new tests by Harbor. Application `main` still matched the pinned accepted SHA when inspected.

## 1. Minimal lifecycle and delivery seam — proposed, not adopted

**Keep three concepts separate:**
- **Source identity/time:** source ID, source epoch, tap, channel, clock domain/sample rate, source revision, BigInt `[startFrame,endFrameExclusive)`, and explicit FFT window/hop/method identity. Overlapping FFT spans are *expected*: advancement is by hop; they are not overlapping PCM blocks.
- **Producer lifecycle:** a producer-owned monotonically progressing **publication sequence** plus an independently verifiable **generation/fence** that changes when previously queued "current" observations must no longer be presented as live (source replacement/replay, invalidation/reset, parameter-boundary reconfiguration, disposal/fatal fault). A retained immutable data object cannot certify its own currentness. The fence must be available from **live provider state** or via an equivalent guaranteed ordered lifecycle channel which cannot lose a reset silently. These fields can be local to the provider seam; no universal registry is needed.
- **Subscriber cursor/contract:** each subscription declares `complete-ordered` or `latest-coalesced`, its buffer/pressure policy and current subscribed generation and expected sequence. A subscription joining late must explicitly start at the current frontier; it is not retroactively entitled to old FFT windows.

**Ready/data events vs control/status:** Ready observations carry provenance, method, half-open span and producer sequence/generation. Producer control transitions (`unavailable`, `reset`, `faulted`, `ended`, `disposed`) are NOT ordinary data windows and must not be silently overwritten by a bounded data queue. Subscriber control and fence state must be queryable even if its event callback was not invoked. A reset invalidates queued live data from the prior generation and makes the subscriber's derived continuity **unavailable until deliberately restarted or revalidated**; previously delivered observations may remain *historical* with old provenance, not current.

**Crucial subtlety:** Do **not** define currentness as `observation.revision === producer.readCurrent().revision` for a complete-stream analyzer. That is correct for the CP3-A **latest** view but invalidates older legitimate windows between ready revisions in the same uninterrupted generation. Check the **live generation** and subscriber's expected ordered sequence instead. A historical data archive can retain pre-reset windows with explicit epoch labels; a live dependent consumer may not silently process an undelivered pre-reset queue after a generation fence.

**Delivery semantics:**
- **complete-ordered:** consecutive completed window records in source-frame/window-start order, or a visible `DISCONTINUITY` status with the last confirmed observation, first missed/new available sequence where known, source epoch/config identity, and reason. A gap is not a fabricated zero-window. Stateful transformations (flux/onset/tempo/averaging) invalidate the continuous result after a gap and must explicitly reinitialize their window/history state before resuming. If exact missing frame span is not known, say UNKNOWN; do not infer it from rAF timestamps.
- **latest-coalesced:** intentional dropping of intermediate values is not a completeness failure; return the latest **valid current** observation plus source sample interval, method and held/coalesced age/status. A slower renderer may repeat a rendered image, but must not invent a newer measurement or misrepresent an ended/invalidated stream as live.
- **ended/final:** a final PCM fragment without a complete new FFT window is **not** a stream gap. For files below M, report no complete spectrum / `INSUFFICIENT WINDOW` while preserving truthful CP2 final RMS; for longer files retain the last actually complete window as historic final, without padding a synthetic spectral tail. An end-of-source state is distinct from ready-live and from `EOF — REPLAY REQUIRED`.
- **failure:** a consumer exception or slow consumer is a consumer-local fault/overrun unless it compromises shared source/provider validity. Upstream PCM protocol/epoch fault invalidates all dependent consumers. Renderer-only faults should be isolated in the *future multi-panel design* when proven safe; preserve the **current accepted global pause/invalidate** until an owner-authorized compatibility change. Do not discard an already correct partial analysis solely because one pane stops painting.

**Pressure boundary:** Memory is bounded per subscriber. If consumer capacity is exceeded, pause/backpressure is possible only where the source and whole input batch can really be paused without losing its accepted frames; a single large `accept()` may already produce more windows than a small queue holds. Otherwise emit a durable/control-plane `OVERRUN` / `DISCONTINUITY` and fail closed for that subscriber's continuous derived output. No infinite queue, no upstream rewind claimed for live input, no quiet skipping. On pausable file input, a replay from a new epoch may be an *explicit* recovery choice, not an implicit substitution for missed data.

**Callback safety:** Consumer dispatch must not be allowed to mutate upstream truth or abort unrelated subscribers' delivery midway through one accepted PCM block. A throwing callback faults/quarantines only that subscription, with the provider and healthy subscriptions progressing if provider state remains valid. Disposal or replacement invalidates queued callbacks and outstanding tickets; no late callback can cross its generation fence. Reentrant subscribe/unsubscribe must not reorder published windows or cause double delivery. Prefer staging all complete windows for an accepted block before fanout, so a failed downstream callback does not turn a partially published block into an unclear upstream commit; if a streaming per-window commit is chosen instead, each commit must have a precise once-only frontier.

**Ownership cost / Flint boundary:** I do **not** prescribe a general message bus, worker farm, scheduler, history database, or public global "measurement registry". The smallest needed objects are a provider's ordered publication/fence, a per-subscriber policy/cursor/bounded backlog, and a local fault/reporting path. Multiple FFT window/hop configurations may require distinct providers; a visualizer cannot covertly change another consumer's analysis policy.

## 2. Falsifying traces

| Case | Proposed observation or fail-closed result |
| --- | --- |
| **M8/H4/20 frames (one block vs 8+4+4+4)** | A complete subscriber receives exactly `[0,8)`, `[4,12)`, `[8,16)`, `[12,20)` in that order under both partitions **if no capacity overrun**. A latest-only consumer reads `[12,20)`. Exact spectral values and source provenance agree, independent of block partition and rendering. |
| **Subscriber queue capacity 2, no polling, 4 ready windows** | Cannot claim four received. An unpausable provider must report `DISCONTINUITY/OVERRUN`, identifying missed sequence/range if known; never silently return only the last two as continuous. An offline provider may deliberately backpressure **before** lossy acceptance or offer an explicit replay. |
| **Reset gap: ready #2, missed ready #3, reset #4** | After reset, a cached ready #3 is not current even though `3 > lastConsumed=2`. Live provider fence differs; queued old-generation ready is rejected/cleared. Last valid pre-reset observation remains historical only. A continuous derived analyzer must reinitialize. |
| **One subscriber throws on second window** | Fault that subscriber and report its precise last accepted sequence. Healthy consumer receives all four; PCM/source state and latest ready remain correct. No unreported duplicate/retry of the faulty callback. |
| **Two subscribers at distinct rates** | Fast analyzer's completeness does not depend on slow renderer/rAF. Slow latest view may coalesce; slow *complete* subscriber must observe either bounded backpressure or explicit loss, not a fake contiguous flux series. |
| **No complete new window in a partial block** | No synthetic observation, no sequence increment representing a fake FFT; previously complete same-generation latest remains historically valid. |
| **File final 481 frames vs default M1024** | CP2 publishes valid final RMS. Spectrum produces no full window and an explicit insufficient-window status. End-of-file is not treated as silent complete spectral measurement. |
| **Final-block display throws** | Current CP3-A behavior remains `EOF — REPLAY REQUIRED` after explicit Retry render; no old final reading republished as newly measured. Future per-panel recovery must preserve the same truth while isolating the bad pane. |
| **File switch/cancel/import late completion** | Host import generation rejects superseded completion. Source epoch and producer fence advance on accepted replacement; no old-file observation or callback may republish into new active panel. |
| **pagehide / BFCache restoration** | Dispose subscriptions and source, fence queued callbacks, stop scheduling; a persisted pageshow reload constructs fresh services, never revives disposed provider's 'ready' data. |
| **BigInt spans beyond Number.MAX_SAFE_INTEGER** | Preserve exact BigInt source spans and hop alignment; do not cast to Number for identity or gap accounting. Window-count sequence is not a sample-clock substitute. |
| **Parameter revision changes at a PCM block boundary** | No mixed-window parameter identity. Publish a segment boundary/availability change, discard incomplete assembler state as existing CP3-A does, and mark derived continuous outputs reset; legitimate new-configuration windows remain properly attributable. |

**Important falsifier of my own design:** if a per-subscriber event transport with a guarantee of ordered, non-droppable control transitions plus replayable acknowledgment can demonstrate that no old queued ready crosses reset or disposal, the additional live fence query could be unnecessary. The required guarantee is the property, not the mechanism. Likewise, if a very small synchronous fanout with isolated callbacks can prove complete delivery without buffering in the bounded file prototype, do not add ring buffers prematurely.

## 3. Minimum next proof and discriminating evidence

**Recommended proposal:** A narrow, authorized later **CP3-B0** experimental seam (name not yet adopted): source-invariant FFT provider emits completed windows to two test consumers **without changing CP2 PCM ingress or CP3-A FFT arithmetic**. One declares complete-ordered and records every source-span, revision and method; the other is latest/coalescing. Add a tiny observable lifecycle fence and an explicitly bounded pressure case. Keep current `readCurrent()`/SpectrumScope behavior as an independently regression-tested compatibility path.

**Minimum acceptance matrix (NOT EXECUTED):**
1. Both M8/H4 block partitions produce the same four complete windows with a complete subscriber and the same latest `[12,20)`; same bin values under source partition.
2. A cap-2 backlog produces a reported discontinuity rather than silent loss; a stateful dependent consumer refuses to publish an unjustified continuous result until reinitialized.
3. Cached ready-3 cannot regain live status after rev-4 reset; reset remains detectable even if observer missed its callback.
4. Throw in one subscriber on publication 2; upstream and other consumer still deliver. Dispose/reentrancy prevents late/reordered callbacks.
5. Replace/replay/parameter change/canceled import/EOF/pagehide and final-render-error paths preserve epochs, provenance, explicit statuses, and existing CP2/CP3-A observable behavior.
6. No second PCM acquisition, no second FFT when dependent method uses the exact CP3-A window, no renderer-timed analysis; numeric DFT/PSD oracle remains separate from lifecycle oracle.
7. Preserve current accepted tests and application functioning. Actual backpressure/realtime/device timing is **not** proven by an isolated fixture or historical CI.

**Evidence that changes my mind:** an alternative smaller seam shows the same detection/isolation properties under all tested traces with less state ownership. Or if the owner scopes an analyzer that explicitly uses latest/coalesced observations, complete window fanout is not a prerequisite for that particular B1 computation. A producer **capable** of complete delivery matters for future consumers, but not every consumer needs it.

## 4. Recommendation and dissent

- **Preserve:** CP2 strict source/epoch/BigInt clock, finite-window RMS and copied PCM; CP3-A coherent-tone one-sided peak amplitude, Hann/window/hop config, latest-only rendered read path, independent host FrameHost, EOF/replay/failure invariants and historical accepted CI. Never relabel peak amplitude as PSD, VU, LUFS or physical units.
- **Change, after separate owner scope:** expose each **completed** FFT window for a declared complete consumer; add minimal lifecycle fence and per-subscriber gap/fault status. Distinguish consumer exception from producer invalidity. Establish subscriber ownership, queue bounds, and clearly scoped reconfiguration without allowing visualizers to dictate global DSP.
- **Defer:** B1 PSD production, B2 panel UI, generic subscription middleware, multiple host clocks, worker/remote delivery, arbitrary plugin sandboxing, real-time SLA, compositing, scene persistence, cloud history and broad migration.
- **Reject:** revision-greater-than-last as currentness; silently dropping windows for a `complete` analyzer; treating render frames as sample time; synthetic padding at EOF; all-subscriber poisoning from one pure callback exception; reviving old epochs on replay; changing accepted CP3-A numerical semantics to ease interface design.
- **Individual dissent/uncertainty:** I prefer **an explicit subscriber discontinuity that invalidates dependent continuous analysis**, rather than an adaptive automatic catch-up scheme whose catch-up window ownership and reproducibility are unspecified. I do not claim that all PSD consumers need every FFT window: single-window PSD conversion can be latest, while Welch averages/onset/tempo may require ordered history. Whether the first transport is callback fanout or pull with bounded cursors belongs to the minimal comparative experiment, not this reviewer.

## Evidence

**Directly read:** User-provided synchronization Markdown, accepted Auralprint `AGENTS.md`, source files `src/analysis/{spectrum-stream,pipeline}.js`, `src/main.js`, `src/audio/file-import.js`, `src/rendering/frame-host.js`, `src/visualizers/spectrum-scope/model.js`, `src/config.js`, `docs/{CP2_FILE_PCM,CP3_FREQUENCY}.md`, and targeted existing test source at exactly `0531e734a2ece59cd877ea8659069efee2e0a905`. Read Harbor's Kestrel branch-local identity/contract/profile, memory/state/permission/verification procedures and indexed CP3 history at `522b036a6187a0dc682c9b7aae2358e60623018b`. Current application main equaled accepted baseline; no new Issue #8 responses were read.

**Verification distinction:** Source inspection and historical Harbor evidence, **not** a source-executed new subscription prototype. Tests, stress timings, device experiments, and the full Kestrel seed validator are **NOT RUN** for this design synchronization. No measured resource limit or production performance claim. Shared GitHub authentication does not authenticate Harbor's agent persona.

**Task outcome:** INDEPENDENT DESIGN SYNCHRONIZATION COMPLETE; technical design and CP3-B0 proposal remain UNADOPTED.

## Revisit when

Axiom reconciles all six first-pass responses; the owner approves a bounded provider/consumer prototype; a new subscription/event implementation is available for exact-head stress, reset and EOF testing; or accepted CP2/CP3-A source changes. Re-resolve current heads, preserve prior source and test limits, and do not treat this record as application architectural authority.
