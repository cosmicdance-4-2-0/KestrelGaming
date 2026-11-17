---
schema: 1
id: 2026-11-17-ap117-pr13-host-psd-session-trust-lk30
kind: handoff
scope: agent:latch
status: active
evidence: observed
author: latch-ap117-pr13-host-trust-2026-11-17
created: 2026-11-17
updated: 2026-11-17
sources: "PR #13 Axiom review assignment issues/comments 6913221997 and 6914016022; exact ap_117_KESTREL head 2d417adab3f28315c0cbde63048851ae6e44bca8 vs main bdead48ae672ed6834eae274c8876944a79104bc; source at head psd-session blob 005e8f77fd7d71e5be51780a6cdbefa525bb2377, psd-processor blob 1f3937cbdaf77514c435da30879975e6a13f16ef, spectrum-stream blob 4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc, spectrum-delivery blob ef19cd748de41226ab0cd8375949e278f7aeb76f, fft-amplitude blob ee35e0793aceb5eb9e3fc49d27f293a1719effc5; isolated V8 exact-source probes; CI 43844573608 successful exact head; own LK29."
---

# Latch — AP117-004 PR #13 trusted-origin and handle-binding review

**Disposition:** **PASS — Latch's assigned supported trusted-host origin/ownership remit**, exact PR head `2d417adab3f28315c0cbde63048851ae6e44bca8`. No observed blocker. **Not** a vote for merge, API adoption, release, hostile plugin authentication, per-panel error isolation or performance certification; Axiom reconciles and owner decides.

**Source:** [PR #13](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13), base `main@bdead48ae672ed6834eae274c8876944a79104bc`. Assignment from [Axiom's supplement](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6914016022) and [initial specialist dispatch](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6913221997). Prior historical finding [LK29](2026-11-15-ap117-pr12-psd-trust-review-lk29.md): a free-form PSD processor accepts callback-shaped wrappers but a trusted correct native handle does not misroute receipts. This PR supplies the minimal real host handoff that LK29 requested.

**Mode:** Source and contract audit plus isolated JS execution of **fetched production source functions**, replacing only ES-module syntax with explicit local binding. No application source edit, merger, deployment, new library, full Node suite, browser, device, or GC/stress run.

## Summary

The current supported application host is the authority for **choosing its one spectrum producer**. `createPsdSession({producer,spectrum,source,capacityObservations})` calls `producer.subscribeComplete()` itself, passes the newly returned native handle directly to `createPsdProcessor`, retains the processor privately, and exposes only `drain/readStatus/readCurrent/dispose`. It refuses extra keys, including `subscription`, `take`, `readStatus`, `processor`, and callback-like injection. Each `drain` accepts no arguments and pulls only from the private processor. This **does close Issue #10's supported single-trusted-host *origin binding* subgate**, unlike the isolated PR #12 constructor. It **does not authenticate an incorrectly selected producer** or prevent forged data from a hostile producer/controller; source identifiers and BigInt generation/ordinal/continuity stamps remain *descriptors and counters*, not credentials.

First CP2-ready descriptor is used **before that same input's `spectrum.accept`**; no early first-window loss is created by the host. Successful accepts drain synchronously, independent of Canvas/rAF. Explicit limited capacity and status distinguish clean EOF from drained PSD, local overrun from real upstream failure, future-only versus historical windows and historical output after a fence. The host holds-on-break by deliberate policy, rather than silently resyncing and claiming complete coverage. Source replacement, replay, import transitions and pagehide dispose before installing another session.

## Evidence

### Exact inspected sources

- [`src/host/psd-session.js:3–133`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/host/psd-session.js#L3-L133), blob `005e8f77fd7d71e5be51780a6cdbefa525bb2377`: strict option names, actual producer call and native subscription transfer, construction cleanup, private PSD processor, bounded drain, frozen observations and status, no resync/public subscribe, idempotent dispose.
- [`src/main.js:62–130,139–165,226–277,299–389`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/main.js): host retains one selected producer from `createSpectrumStream(CONFIG.spectrum)`; `admitPsd` derives source from actual CP2 ready publication before first `spectrum.accept`; drains after successful accept; disposal before replace/reset; authorizes synthetic parameter revisions from real setter; current UI diagnostic marks lost coverage/historical state; pagehide guards. No new acquisition, FFT or rendering scheduler.
- [`src/analysis/psd-processor.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/analysis/psd-processor.js), blob `1f3937cbdaf77514c435da30879975e6a13f16ef`, accepted unchanged module: per-handle zero-argument `take`, scientific fingerprint, source, time span and continuity checks.
- [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/analysis/spectrum-stream.js), blob `4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc`; [`spectrum-delivery.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/analysis/spectrum-delivery.js), blob `ef19cd748de41226ab0cd8375949e278f7aeb76f`; [`fft-amplitude.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/analysis/fft-amplitude.js), blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`: accepted complete-delivery and spectral numerical source unmodified.
- [`tests/psd-session.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/tests/psd-session.test.js) covers both Issue #10 collisions, native/wrong options, late B, old A, four-final, cap2 overrun, loss and disposal.
- [`tests/app-integration.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/tests/app-integration.test.js): source-read review of test-only Node module-hook tracing real main and fault injection. [`docs/AP117_004_HOST_PSD_SESSION.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/docs/AP117_004_HOST_PSD_SESSION.md) accurately declares trusted host, hold-on-break, limits.
- GitHub compare exact base→head: **one commit, 10 changed paths** (three additions; existing code/math paths untouched except main/config and tests/UI/Node engine metadata). Live `main` still `bdead48ae...` at review. [Actions run 43844573608](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43844573608) reported completed **success**, matching exact reviewed SHA. Implementer/Axiom attribute 131 Node tests, HTML/browser/CI pass; Latch did **not** independently rerun those suites or parse the full CI job log.

### Executed isolated V8 checks (actual source, no algorithm changes)

Fetched five production sources at exact head: `psd-session.js`, `psd-processor.js`, `spectrum-stream.js`, `spectrum-delivery.js` and `fft-amplitude.js`. Adapted import/export declarations only to local factory injection using V8; retained all production logic. The fixture used proper spectrum/RMS method fingerprints and source BigInt spans, periodic Hann M8/H4/N8, fs48000, explicit capacity budgets. These are **direct-adapter legal envelopes**, not a claim to execute the full CP2 `pipeline.advance` or Node suite.

| Review case | Independent observed outcome | Interpretation |
| --- | --- | --- |
| **PR13-L1 mixed extra constructor options**: supply `subscription`, `take`, `readStatus`, `processor`, `onReceive` | All rejected by `createPsdSession` option whitelist. The public handle exposes exactly `drain/readStatus/readCurrent/dispose`; `drain(foreignReceipt)` throws before consuming B. | Supported API **cannot** be injected through caller-supplied handle/receipt. |
| **PR13-L2 equal-stamp two producers**: same full source descriptor but different genuine PCM amplitudes 0.25 and 0.50 | Both began generation `1n`, completion ordinal `1n`, continuity revision `0n`; A PSD DC `0.000006944444444444445`, B PSD DC `0.00002777777777777778` (4x). Each host session returned only its own producer's result. | Origin is selected actual producer object; stamps do not select it. |
| **PR13-L3 late B and genuine historical A**: A starts first, B joins same producer after first completion | B initial drain empty; after next 12 samples, A returns starts `[0n,4n,8n,12n]`, ordinals `1..4`; B returns `[4n,8n,12n]`, ordinals `2..4`. | Future-only B and same-handle historical A both pass. |
| **PR13-L4 four queued final FFT windows**: final20 with capacity4 | Before drain: `source-ended-drain-pending`, four queued; after: four PSD windows starts `0,4,8,12`, `drained`, lastResult `ended`, `maxDrainCalls=5`. | Producer EOF not mislabeled consumer drain. |
| **PR13-L5 cap2 final20** | `broken` with `subscriber-delivery-overrun`, zero processed/queued. | Explicit atomic overrun, no invented partial continuity. |
| **PR13-L6 reset/fence after valid PSD** | `broken`, cause `test-fence`, last observation marked historical, retained immutable object still available as history, no additional drain. | No cached ready resurrection. |
| **PR13-L7 idempotent disposal** | Session `disposed`, later drains return no observations, no public reset/resync. | Narrow terminal capability. |

All outcomes above are observed in this isolated test; they are **not** externally authenticated module host execution or live-device behavior.

## Findings / severity / dissent

**L-P13-1 — PASS: Issue #10 native-handle origin binding now demonstrated for supported direct host.** Prior LK29 showed a composite function-wrapper could defeat a free-form consumer constructor under a violated host wiring premise. PR13 no longer lets callers supply such a wrapper to the **session**. Construction uses exactly the selected real producer's newly returned handle; direct same-stamp producer and late-subscription tests pass. This is a meaningful correction without a generic broker, UUID registry, receipt MAC, extra source read or FFT refactor.

**L-P13-2 — KNOWN LIMIT (nonblocking): host-producer selection remains trusted.** `producer` itself is an accepted caller-supplied option in the narrow session helper. A malicious `subscribeComplete` implementation or mistaken host selection can provide B's genuine handle while claiming A's context; the session has no independent trusted producer registry to expose this. The in-repo `main.js` composes one static `createSpectrumStream(CONFIG.spectrum)` instance; there is **no evidence** a hostile producer can enter the supported application. Do **not** claim authentication against wrong/hostile producers or unrestricted same-realm JS plugins. Before a multi-provider selector is introduced, test that selection and session binding remain paired at the host composition boundary. No new security framework required today.

**L-P13-3 — IMPORTANT OWNER TRADEOFF (no demonstrated safety defect): hold-on-break loses continuing science until explicit new source.** An authorized synthetic slider edit fences PSD, and the same session stays broken while RMS/peak may keep advancing. This is truthful and explicit in the UI and contract, not an undetected gap. It may nevertheless frustrate instrumentation workflows. Request owner acceptance/rejection of hold-until-replace/replay; do not silently add automatic resync or mark it an unrelated trust vulnerability. A future resync must explicitly acknowledge permanently forfeited source windows.

**L-P13-4 — EVIDENCE LIMIT: full integration CI is attributed.** Green exact-head CI supports that Node tests/build/browser succeeded in CI; the actual Node/browser logs were not independently rerun by Latch. Focused tests use source code with local module adaptation. No measured realtime, GC/heap, external-plugin attack or actual multi-provider UI selector was tested.

**Additional concern to monitor, not a blocker:** `session.readCurrent()` returns the last immutable PSD even after break/end; freshness comes from `readStatus()` and not the frozen measurement alone. Presenters must respect `lastObservationHistorical` and source spans, including on dispose. Current `main.js` diagnostic does so on inspected paths.

## Dissent and acceptance decision

- My earlier PR12 caution `take(receipt)` alone is not origin authentication **still holds at the bare PSD processor level**. This PR addresses it *by wiring the actual native subscription in a new trusted host*, not by magically making stamps authentic.
- A non-native hostile producer can still lie; this is **outside** the authorized first host scope, and testing arbitrary same-realm JS requires an entirely different threat model. Reject both blanket 'secure plugin ecosystem' praise and exaggerated 'critical vulnerability' language.
- The new owner-facing hold-on-break recovery policy has a real usability cost. Axiom should preserve it for explicit reconciliation instead of burying it under generic 'safe' language.
- If a supported caller can supply `subscription`/receipt injection without corrupting the host or construct a wrong-handle session through the **actual in-repo `main.js` wiring**, revise PASS to BLOCK. I found no such path. Re-pin to a new SHA if PR changes.

**Outcome:** **COMPLETE — first-pass Latch trust-origin review.** Recommend **PASS** for Latch's remit at `2d417adab3f28315c0cbde63048851ae6e44bca8`; no application corrections requested from this perspective. Issue #10's broader closeout and owner adoption remain separate gates. Axiom should reconcile all independent reviews before any merge recommendation.

**Independence/provenance note:** My first tool retrieval of PR issue comments included a **previously posted Flint report** together with Axiom's assignment. The substantive source inspection and separate V8 tests above were performed independently of Flint's arguments, but this is **not a perfectly blinded first pass**. No other specialist reports were intentionally read or used to derive this verdict. All GitHub writes were confined to my own agent memory and my PR review. Shared GitHub account author attribution is not proof of separately authenticated runtime identity.

## Revisit when

Axiom changes PR head or challenges the native-handle proof; a producer selection/configurator or second host source is added; the owner chooses a different hold/recovery strategy; a third-party plugin runtime is proposed; or Issue #10 and #11 closeout evidence changes.
