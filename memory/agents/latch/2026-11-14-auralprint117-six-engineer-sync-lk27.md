---
schema: 1
id: 2026-11-14-auralprint117-six-engineer-sync-lk27
kind: handoff
scope: agent:latch
status: active
evidence: inferred
author: latch-ap117-sync02-independent-2026-11-14
created: 2026-11-14
updated: 2026-11-14
sources: "Axiom Team Synchronization 02 user-supplied handoff, 2026-11-07; ap_117_KESTREL accepted exact main 0531e734a2ece59cd877ea8659069efee2e0a905, inspected 2026-11-14 (main still same); own Latch AGENT/PROFILE and Kestrel contract/memory on agents/latch-v1 at a98d1db48ff50514253705d76202778094ff82f1. No other engineer's new synchronization report inspected; code inspected but no tests or prototypes executed."
---

# Latch — AP117 Team Synchronization 02 independent trust-boundary review

**To:** Axiom — The Geometer, Auralprint 117 integrator  
**Assignment:** Six Engineer Synchronization 02 / **Latch**, source [Issue #8](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/8).  
**Perspective:** Latch — The Locksmith, character_id `latch`, `KestrelGaming@agents/latch-v1`; draft agent identity, not authenticated autonomous instance.  
**Application baseline:** **`cosmicdance-4-2-0/ap_117_KESTREL@0531e734a2ece59cd877ea8659069efee2e0a905`**. GitHub `main` reference was still exactly this commit on 2026-11-14; nothing newer was substituted.  
**Source-mode:** independent source audit and design proposal only. No application changes, new permissions, PR, merge, code execution, synthetic test execution or device trial. I deliberately did not open other engineers' new Issue #8 responses before recording this initial view.

## Summary

**Verdict: ALIGN ON OWNER GOAL; CONDITIONAL ACCEPT OF A NARROW PROVIDER/CONSUMER SEAM; REQUEST EXPLICIT TRUST AND OWNERSHIP CONDITIONS BEFORE ANY USER-EXTENSIBLE MODULE DESIGN.**

The owner's requirement is analysis-first simultaneous instrumentation: analysis providers and consumers may be composed at independently selected rates/configurations; a consumer needing every observation must receive it in order **or a visible discontinuity**, while a renderer may intentionally coalesce to latest. Latch's highest-risk concrete seam is **confusing schema validation and shallow-frozen publication objects with provider authenticity, subscriber authorization and buffer isolation**. Preserve the accepted CP2/CP3-A semantics. Demonstrate one narrow host-owned, bounded fanout across two subscriptions before generalizing into plugin discovery, scripting, network permissions or a universal pub/sub framework.

A malicious module in the **same unrestricted browser JavaScript realm** cannot be sandboxed through a capability-shaped JavaScript API alone. It already has ambient platform APIs. Future user-installed modules require an actual trust/packaging/sandbox decision. The current program has **no evidence of hostile plugins or actual audio exfiltration**; this is a forward threat hypothesis, not a vulnerability finding about the accepted prototype.

## Evidence — actual baseline inspected

- [`AGENTS.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/AGENTS.md): CONFIG precedence, numerical truth, protected CP2/CP3-A interfaces, no plugin implementation.
- [`src/analysis/pipeline.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/pipeline.js): strictly checked source/epoch/channel/tap/clock and BigInt spans; CP2 snapshots RMS metadata; `waveform = new Float32Array(block.samples)`; outer publication frozen; `isCurrent` checks live ready/revision.
- [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/spectrum-stream.js): exported `accept(publication)` validates the CP2 RMS fingerprint, chronological waveform blocks, builds complete overlapping FFT windows, updates `current` for each, but returns only the last current publication. It has `reset`, `invalidate` and `isCurrent`, not subscription fanout/history.
- [`src/analysis/fft-amplitude.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/fft-amplitude.js): spectral `amplitudes` is an owned, frozen ordinary JS Array; **do not falsely claim it shares the PCM mutable-buffer property**.
- [`src/main.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/main.js): trusted static host wires one CP2 pipeline -> spectrum stream; one analysis timer distinct from host-owned Canvas `FrameHost`; local file selection/cancel/replace/epoch/replay/teardown. It currently stops sampling and invalidates views on a renderer failure; do not silently change that *accepted behavior* in this synchronization.
- [`src/visualizers/signal-scope/model.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/visualizers/signal-scope/model.js): forwards the published `waveform` reference to the view model. The same typed-array bytes can be written by a consumer even though the enclosing record is frozen. This is a **known read-only-by-convention**, not a demonstrated current mutation exploit.
- [`src/rendering/frame-host.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/rendering/frame-host.js): renderer scheduling and exception policy is host controlled.
- [`src/audio/file-import.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/audio/file-import.js) and [`src/audio/pcm-buffer-source.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/audio/pcm-buffer-source.js): import generation cancellation; bounded local WAV input; source owns selected PCM copy and disposal.
- [`tests/publication-integrity.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/tests/publication-integrity.test.js), [`tests/stream-boundary.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/tests/stream-boundary.test.js) and [`tests/spectrum.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/tests/spectrum.test.js): existing source-level controls for invalid metadata, freshness, epoch discontinuity, and compatible complete FFT windows. **Read, not rerun.**
- [`docs/CP3_FREQUENCY.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/docs/CP3_FREQUENCY.md): accepted method distinction, latest-only stream and explicit future history requirement.
- Axiom handoff says PR #5 merged and CI run 42438949177 passed 67/67 Node tests, offline build and browser smoke. **Attributed to the handoff**, not independently rerun or evidence of live-device performance.

### Authority and status distinction

**Owner-required:** user-composable instrumentation panel; accurate analysis before rendering; provider/consumer/both roles; multiple simultaneous analyzers with potentially different window/hop policy; complete/ordered vs intentional latest-only delivery with explicit loss; bounded memory; truthful unit/clock/epoch/status. Preserve CONFIG as authority over defaults and analysis selection; no visualizer may secretly dictate DSP math.

**Established accepted behavior:** CP2 normalized finite-window RMS `ap117.measurement/2`; CP3-A `ap117.spectrum/1` coherent-tone peak-amplitude FFT latest-value with copied validated PCM; one source read; host-owned dual Canvas2D frame loop. The read-only waveform is **contractual** not enforced immutability. No general subscriptions or third-party plugin boundary exist today.

**Reopened proposal, not settled:** B1 Option C's externally latest-only restriction; a C-stream fanout of *each completed* FFT window; PSD conversion for matching upstream window; independent PSD FFT for different method/window; B2 user panel selector; tiny callback or bounded queue interface; CP3-B0 name. No new computation claim should be mislabeled as accepted.

**Excluded:** auth tokens, microservice broker, general callback marketplace, arbitrary JS plugin installation, multi-renderer compositing, live-device latency proof and infinite lossless buffer; none are prerequisites for this first bounded seam.

## Ranked findings / threat model

### T1 — IMPORTANT NOW FOR NEXT SEAM: producer validity is not producer authority

A `ready` envelope with correct `ap117.measurement/2` fields proves compatible *shape* and provenance claims only. It is not evidence the data came from an approved source. Current `createSpectrumStream.accept` is designed to validate interchange labels and chronology, not authenticate a remote producer. Those are sensible current guarantees.

**Future failure path:** a dynamically registered module publishes fabricated `ap117.spectrum/1` (or correctly shaped CP2 RMS with fake `sourceEpoch`) and causes an authorized panel to present it as an observation from the user-selected WAV. A string `sourceId='local-wav'` is not a credential.

**Minimum boundary:** the host binds *provider registration identity + allowed output descriptors* to the publication channel. Consumers subscribe to registered handles, not arbitrary strings. Validate method/units/schema/clock/span from that registered producer; reject mismatch as invalid/unavailable. Do not pretend that handles authenticate untrusted JS running in the same realm. The host-controlled adapter and module-loading trust boundary must be explicit before claiming adversarial security.

**Positive control:** genuine CP2 and CP3-A observations remain accepted unchanged.

### T2 — IMPORTANT: mutable PCM aliases break isolation when the trust level changes

`AnalysisPipeline.advance` creates one owned PCM waveform copy; that protects it from source-buffer aliasing. But it exposes `publication.waveform` as a non-frozen `Float32Array`. `toSignalScopeModel` forwards the reference. `Object.freeze(publication)` does **not** make its typed-array elements immutable. CP3-A's emitted peak `amplitudes` is different: an owned frozen ordinary array.

**Future failure path:** subscriber A changes one waveform sample before B computes spectral flux or PSD; B's result depends on subscriber callback order, not the source. Or a visualizer keeps a mutable reference through reset and presents stale private PCM as current.

**Minimum boundary:** for *trusted in-process* built-ins, retain the explicitly documented read-only-by-contract borrowed waveform with tests to detect accidental mutation; for future untrusted/isolated consumers, deliver a defensive copy or an enforced separated read-only transport under an explicit memory/CPU budget. Prefer derived typed observations to raw PCM when a visualizer does not need raw samples. Never claim `Object.freeze` creates a typed-array sandbox.

**Positive control:** two well-behaved consumers receive equivalent values with no unnecessary source reread or FFT duplication.

### T3 — BLOCKER FOR THE SUBSCRIPTION FEATURE: delivery guarantee must not be forged by coalescing

Exact counterexample in the handoff: `M=8,H=4,Nfft=8`, 20 PCM samples in one block versus chunks 8/4/4/4. Windows are `[0,8), [4,12), [8,16), [12,20)`. Current `spectrum-stream.accept` computes all internally but exports only latest `[12,20)`. That is **correct for today's latest-value consumer**, not sufficient for any future consumer promised every complete window.

**Minimum boundary:** provide a bounded **complete/ordered** subscription that exposes all four or produces a source-span-identified discontinuity/overrun; preserve `readCurrent` as *latest* and permit renderer coalescing. Keep a single physical PCM source read and reuse compatible FFT windows; if a future analyzer requires independent window/detrend choices, don't silently substitute peak-amplitude bins.

**Disagreement:** do not demand lossless delivery of every window to all consumers. Such an unconditional promise makes live/nonpausable sources impossible to bound; explicit discontinuity is the required honest failure.

### T4 — IMPORTANT: callbacks, slow consumers and queues must not acquire producer authority

**Future failure paths:** subscriber throws in synchronous fanout, monopolizes the event loop, calls `reset`/registers a new subscription during publication, queues forever, or receives a new epoch under a stale subscription. A single bad renderer must not silently fabricate `faulted PCM`. Current main's global stop-on-render-fault is accepted and should not be quietly rewritten; a later scope decision may improve isolation.

**Minimum boundary:** host owns subscription handles and releases; producer commits the observation **before** dispatch; callbacks receive data *and cannot call producer mutation methods through their handle*. Define ordering/reentrancy semantics; isolate ordinary callback exceptions so dependent subscribers see an explicit subscriber failure, not silent skipped upstream data. Cap pending **observations and bytes** with named CONFIG parameters; at cap announce gap/overrun and invalidate continuity-sensitive derived state. Revoke/close on producer epoch replacement/disposal and prevent queued callbacks from delivering after closure.

**Truthful limitation:** a malicious synchronous callback in the same JS realm can still block all execution; time budgets/callback catching cannot enforce preemption. Workers or isolated processes are future requirements if hostile code must actually be confined.

### T5 — IMPORTANT: consumer scope controls information exposure, not just numeric correctness

**Future failure paths:** a 'spectrum colorizer' receives the entire private PCM WAV though it needs only spectrum bins, or source-switch retention lets it read a prior user's WAV. A plug-in advertised as 'local' uses ambient `fetch`/network APIs to send bytes. A mere `subscribe({ sourceId })` string filter or promise not to exfiltrate will not prevent that.

**Minimum boundary:** host gives each subscription only the type/quantity/source/channel/tap/epoch it needs; no direct `readBlock` or local-file handle; revoke stale source handles; avoid full waveform delivery where derived bins suffice. The accepted current application has zero third-party runtime dependencies and does not implement outgoing WAV upload in the inspected local file path; **no exfiltration observed**.

**Deferred threat:** actual third-party *code* isolation, permission to use browser network/file APIs, CSP/worker or hosted sandbox, auditing and user consent must be deliberately designed when installable modules are authorized. Module manifest permissions alone are descriptive, not enforcement.

### T6 — IMPORTANT: lifecycle events cannot disappear behind 'latest'

A downstream subscriber holding an immutable `ready` snapshot can falsely resurrect it after its producer resets. The correct status must come from a producer-currentness/fence or a demonstrably ordered lifecycle stream, not the cached object's internal `ready` label. This is especially important where latest-value ready observations can be coalesced but `reset`, `invalid`, `ended`, `discontinuity` and `closed` controls cannot silently vanish.

**Minimum boundary:** producer-owned monotonically increasing publication revisions **within a run-scoped lifecycle/epoch**, currentness checked against the producer when showing current data, explicit terminal/revoke event(s), no queued old-epoch ready after reset. A historic observation may be displayed as *historic* if labeled accurately; it must not become fresh.

## Candidate smallest seam (design, not ratified API)

1. Host owns **one validated provider handle**, exact supported publication descriptor (`ap117.spectrum/1` with peak-amplitude method and provenance), lifecycle fence and two bounded subscribers.
2. Provider can expose each complete FFT window once, after the already-validated CP2 copy is used. Publisher identity is **host-bound**, not a caller-supplied `sourceId` string. Upstream CP2 and accepted FFT mathematical method remain unchanged.
3. Subscriber A chooses `delivery=complete-ordered` with a small explicit bounded capacity; it receives four windows or an explicit gap/overrun with missing source span(s), then must reset continuity-sensitive analysis. Subscriber B chooses `delivery=latest`; it can read the final `[12,20)` with source-time metadata. Lifetime `reset/invalidate/closed` is distinct from coalescible ready measurements.
4. The subscribed consumer receives a narrow **read-only subscription capability**, not `pipeline`, `spectrum`, source selector, `CONFIG` mutation access or arbitrary local WAV data. A trusted consumer is allowed to derive a new measurement, but if it publishes that observation the host binds a *new provider identity* with explicit method/lineage, not inherited authorship.
5. Dispatch occurs only after producer state committed; subscriber fault/cancel/unsubscribe cannot reenter producer mutation or reorder committed observations. Backlog limits and overflow policy are named CONFIG parameters (`maxQueuedObservations`, `maxQueuedBytes`, `dispatchBudget` with declared units) to calibrate empirically; **no numerical magic defaults are ratified**.
6. Renderer chooses draw cadence without affecting measured sample spans or analysis method. Exact implementation mechanism—synchronous bounded push, pull queue or callback-drain—is open for Flint's minimalism review and an actual test. This is not a generic subscription registry recommendation.

## Proposed falsifiable fixtures (DESIGNED, NOT RUN)

| ID | Deliberate mutation / controlled scenario | Required observable pass and legitimate control |
| --- | --- | --- |
| **L-AP-01** | `M8/H4/N8`, 20 frames partitioned 20 versus 8+4+4+4 | Complete subscriber observes four `[0,8),[4,12),[8,16),[12,20)` in order or declared overrun; latest sees `[12,20)` for both; no repeat source read/FFT for compatible consumers |
| **L-AP-02** | Fake publication with correct `ap117.spectrum/1` fields and plausible source string from unregistered publisher | Rejected as unauthorized **by host binding**; same valid data from registered producer accepted; incompatible method/units rejected even from registered provider |
| **L-AP-03** | A mutates borrowed PCM after publication; B computes over same nominal input | B unchanged under isolation boundary, or explicit fail-closed mutation detection in trusted-only mode; existing source copy protects acquisition, not subscriber-versus-subscriber aliasing |
| **L-AP-04** | Slow subscriber with burst larger than configured capacity; nonpausable producer | Queue remains bounded; complete subscriber sees explicit gap/discontinuity and invalidates continuity-dependent output; latest consumer may coalesce normally; pausable file source can backpressure/replay only when explicitly supported |
| **L-AP-05** | Subscriber throws, unsubscribes mid-dispatch, triggers reentrant subscription, then source switches | No duplicate/out-of-order committed measurements; valid subscriber continues or receives explicit declared halt; former handle can't deliver old WAV/epoch values as ready |
| **L-AP-06** | Producer emits ready rev2, ready rev3 missed, reset rev4, consumer retains frozen rev3 | Frozen old ready cannot be reported current; reset fence/live-currentness invalidates it even if latest queue skipped middle ready |
| **L-AP-07** | Subscriber entitled only to peak spectrum tries raw PCM read, wrong channel/source, and stale handle after replacement | No path through subscription interface; ordinary authorized spectrum panel still works without permission ceremony |
| **L-AP-08** | Static trusted-in-process consumer and untrusted browser module with ambient network access | Document that interface scoping **cannot** by itself prevent network egress from arbitrary same-realm JS. Do **not** mark security-qualified without genuine sandbox/trust boundary; current application no upload in inspected path |
| **L-AP-09** | Distinct PSD detrend/window requirements versus matching upstream FFT window | Same-window derived consumer carries method lineage and can avoid redundant FFT; incompatible-method consumer must demand separate analyzer or explicitly report incompatibility |
| **L-AP-10** | Rendering cadence varied, display throws, source EOF and reset while analysis consumer holds pending windows | Source-sample timing remains authoritative; renderer may coalesce; current error-stop policy not silently regressed; downstream receives invalidation/ended/error per selected delivery contract |

**Independent acceptance evidence required later:** exact producer/subscriber source and method pins, per-window trace for both partitions, source epoch/span/BigInt checks, memory high-water mark at configured bounds, callback exception/disposal traces, negative source/method publication and subscriber access checks, and a legitimate simple-display positive control. A passing headless test cannot establish UI usability, live-device realtime behavior, hostile-plugin isolation or zero network egress.

## Alternatives and tradeoffs

- **A — Trusted callback fanout:** lowest code/latency when processing is bounded and synchronous; must explicitly handle reentrancy, callback exception and backpressure. Cannot preempt malicious subscribers.
- **B — Host-owned bounded pull/cursor queue:** separates producer completion from consumer work and more naturally supports slow subscribers and explicit overruns; more state to maintain, especially per-subscriber epoch cursors. Still no true same-realm adversarial isolation.
- **C — General event bus/worker plugin framework:** unnecessary for the first proof, introduces serialization, plugin governance, error and performance complexity before the source integrity experiment is demonstrated. Appropriate only upon explicit future hostile-module requirements and tested isolation.
- **Existing `readCurrent()` latest-only:** correct and worth retaining for renderer but **insufficient alone** for an ordered analyzer. No redesign of accepted FFT/RMS math required.
- **Data copying policy:** blindly copy to every trusted built-in may waste time and memory; blindly share mutable typed arrays with untrusted modules violates isolation. Choose the trusted borrow vs isolated copy boundary deliberately and measure before optimizing.

## Dissent and what would change my mind

1. I dissent from any assertion that **schema validation equals publisher authentication** or that a manifest-like subscription list is a security sandbox.
2. I dissent from making a spectrum-only visualizer receive private raw WAV samples by default, or from promising that the existing no-upload behavior persists if arbitrary executable plugins are introduced.
3. I dissent from silently changing CP2/CP3-A failure and replay semantics (including current render-fault stoppage) as an incidental fanout refactor.
4. I would **reduce** the proposed boundary if the only permitted modules remain first-party trusted static code and the M8/H4 negative + alias mutation fixtures prove no corruption under documented borrower contracts. Conversely, a proved cross-subscriber mutation, source-scope leak or missed-overrun case justifies a stronger enforcement mechanism. Real adversarial isolation cannot be concluded from such unit tests alone.
5. Do not present B1 C-stream, B2, PSD math or CP3-B0 as accepted integration merely because this individual report supports narrow prototypes.

**Relevant probable design paths, not edits:** `docs/ARCHITECTURE.md`, `docs/CP3_FREQUENCY.md`, future checkpoint contract, `src/analysis/spectrum-stream.js` and a future host-owned subscription seam; `src/main.js` composition and positive/negative fixtures in `tests/spectrum.test.js` and publication-boundary tests. Avoid changing accepted `src/analysis/pipeline.js` `ap117.measurement/2` and numerical FFT/oracle unless a demonstrated requirement forces a separately reviewed contract change.

## Outcome and handoff

**COMPLETE as independent design-only synchronization input; no implementation, test execution or shared contract approval.** This record can be linked from Issue #8 for Axiom's reconciliation. This report does not assert that Latch's security skill qualifications have been earned, that any new agent response was read, or that multiple Git authors/agents were cryptographically authenticated. The shared GitHub identity is a credential; Latch is the attributed authorial viewpoint.

## Revisit when

Axiom publishes a concrete typed provider/consumer seam and explicit loss/currentness semantics, when the M8/H4 partition proof is run, on evidence of mutating or overloaded subscribers, or when user-installed code and true capability isolation are separately authorized.
