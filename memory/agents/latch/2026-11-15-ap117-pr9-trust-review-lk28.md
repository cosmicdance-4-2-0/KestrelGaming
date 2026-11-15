---
schema: 1
id: 2026-11-15-ap117-pr9-trust-review-lk28
kind: handoff
scope: agent:latch
status: active
evidence: observed
author: latch-ap117-pr9-trust-review-2026-11-15
created: 2026-11-15
updated: 2026-11-15
sources: "Axiom PR #9 review dispatch issuecomment-6891240452; ap_117_KESTREL PR #9 exact 35ae476ec8d59c300de877381f84ec7b8c59a1fa vs main 0531e734a2ece59cd877ea8659069efee2e0a905; GitHub source blobs spectrum-delivery ef19cd748de41226ab0cd8375949e278f7aeb76f, spectrum-stream 4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc, fft-amplitude ee35e0793aceb5eb9e3fc49d27f293a1719effc5; isolated V8 source execution and first-party CI run 43690871559; own LK27 prior design review."
---

# Latch — AP117-002 PR #9 independent trust and memory-boundary review

**Verdict:** **CONDITIONAL PASS (trust/ownership remit), exact PR head `35ae476ec8d59c300de877381f84ec7b8c59a1fa`.** No current-scope blocker reproduced. **IMPORTANT future integration requirement:** a complete-delivery observation's `generation`, `continuityRevision`, and `completionOrdinal` identify **lifecycle position within a particular handle**, not a globally unique producer or subscription. Bind the original, actual subscription/provider handle when consuming cached observations. Before building a multi-provider orchestration layer, add a wrong-handle negative test; do not adopt receipt stamps alone as producer identity. **Do not approve hostile user-installed plugins** on this evidence.

**Task:** Axiom's [PR #9 dispatch](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/9#issuecomment-6891240452), Latch lens. Authorial profile `agents/latch-v1` (draft identity, shared account credential), source contract and relevant [LK27](2026-11-14-auralprint117-six-engineer-sync-lk27.md).  
**Exact source pin:** `cosmicdance-4-2-0/ap_117_KESTREL@35ae476ec8d59c300de877381f84ec7b8c59a1fa`, base `0531e734a2ece59cd877ea8659069efee2e0a905`. Source branch `task/codex-ap117-002` matched reviewed head on inspection.  
**Scope:** source review + narrowly isolated V8 execution of **actual fetched production code**. No application edits, full repository install, full `npm run verify`, Chromium, network/device test, PR merge, or agent-schema modification.

## Summary

The new bounded pull subscription is a sound *trusted built-in* boundary: the producer's `accept()` retains sole state mutation/FFT assembly authority; subscriber handles expose **only `take, readStatus, resync, dispose`** and never `accept, reset, invalidate, readCurrent` or raw PCM. Full spectrum publication is created in `spectrum-stream.js` after the validated CP2 method/identity/span checks; its ordinary numeric `amplitudes` array and nested records are frozen. Complete windows are future-only and either arrive in order or yield an explicit subscriber-local continuity break; the existing latest cache remains. No consumer callback runs inside `accept()`.

**Trust boundary to keep explicit:** `createSpectrumDelivery` is exported as an internal helper, not an authenticated registry. A correctly shaped receipt or matching `sourceId` string is not proof of provider origin. A module with the complete producer object still has its producer methods. The new handle is narrow **only when host code passes the subscriber handle and not the producer**. Third-party code running in the same unrestricted JS realm can access ambient APIs; scoped handles alone are not a plugin security sandbox.

**Important nuance:** The underlying CP2 waveform in `src/analysis/pipeline.js` is copied from the source but remains a mutable `Float32Array` borrowed read-only by convention. The new delivered spectrum is **not** that same borrowed PCM: its numeric amplitudes are an owned, frozen ordinary array. Do not conflate the two.

## Evidence

### Inspected revision-specific paths

- [`src/analysis/spectrum-delivery.js` lines 1–165](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-delivery.js#L1-L165) (blob `ef19cd748de41226ab0cd8375949e278f7aeb76f`): per-instance `generation=1n`, `frontier=0n`; per-subscription `continuityRevision=0n`; private queue, reserved capacity, `take/readStatus/resync/dispose`, valid-before-commit check, break/fence/dispose. Receipt/status include **no provider-handle identity field**. `observation(publication, index)` trusts its internal caller; helper is not an independent publication fingerprint validator.
- [`src/analysis/spectrum-stream.js` lines 1–209](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-stream.js#L1-L209) (blob `4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc`): tested CP2 type/method/clock/provenance checks, full waveform finiteness preflight, staged atomic FFT delivery, producer-only public surface, terminal rules.
- [`src/analysis/fft-amplitude.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/fft-amplitude.js) (unchanged blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`): owns and freezes `amplitudes` ordinary numeric array.
- [`src/main.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/main.js): one in-repo trusted producer, latest-only page, pagehide terminal disposal; no panel/plugin host exposes subscriptions to untrusted code.
- [`src/analysis/pipeline.js` at accepted base](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/pipeline.js): CP2 waveform copy and explicit borrowed read-only consumer contract; PR does not edit this path.
- [`tests/spectrum-delivery.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/tests/spectrum-delivery.test.js), [`tests/spectrum-delivery-lifecycle.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/tests/spectrum-delivery-lifecycle.test.js), [`tests/spectrum-delivery-atomic.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/tests/spectrum-delivery-atomic.test.js), and [`docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md): source-level documented constraints and tests; full tests not independently rerun.
- Verified GitHub Actions [43690871559](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43690871559) has `conclusion=success`, matching `head_sha=35ae476e...`. Axiom/implementer claims Node/static/HTML/Chromium checks; do not substitute CI attribution for an independent run.

### Executed isolated V8 focused checks

I fetched the exact three production JS files (`spectrum-delivery.js`, `fft-amplitude.js`, `spectrum-stream.js`) from pinned GitHub head; changed only ESM import/export syntax to direct local dependency injection in a disposable, no-network V8 function scope. **Actual algorithms and data operations were unchanged.** This is isolated source execution, **not a normal Node module/full test-suite execution**.

Fixture: periodic Hann `M=8,H=4,Nfft=8`; each producer gets 8 legal Float32 values at its own `sourceId` and source epoch; CP2-style `ready` envelope matches accepted RMS fingerprint; one complete FFT window per producer. Configured producer/subscription budgets are explicit.

| Check | Observed result |
| --- | --- |
| Two distinct producer handles A and B | A: `sourceId=private-A`, amplitude DC `0.25`; B: `sourceId=private-B`, amplitude DC `0.5`. Both publish `generation=1n, completionOrdinal=1n, continuityRevision=0n`. |
| Incorrect cross-provider 'eligibility' using **only** status/generation/continuity comparisons | `statusB.generation === itemA.generation && statusB.continuityRevision === itemA.continuityRevision` evaluated **true**, despite different original producer handles, source IDs and numeric measurements. With ordinal comparison it also collides (both ordinal 1n). This is a **consumer misbinding counterexample**, not an automatic violation inside either producer's own queue. |
| Actual `Object.keys(subscription)` | Exactly `take, readStatus, resync, dispose`; there is no producer mutation or PCM read method. |
| Delivered `publication`, `measurement`, `amplitudes` | All `Object.isFrozen` checks **true**. Attempt to overwrite an amplitude did not change the value. |
| Forged CP2 RMS measurement method `pretend-math/1` | `accept` **rejected** it with the expected validated-CP2 error; its subscriber `take()` reported `break`. |

No actual network transport, malicious third-party JS, ordinary source pipeline, persisted/serialized receipts, full Node suite or browser tested in this isolated run. Fake source IDs are **test labels only**, not actual user files.

**Minimal reproducible wrong-handle test sketch (PROPOSED for in-repo fixtures):**

```js
const a = createSpectrumStream(config);
const b = createSpectrumStream(config);
const ha = a.subscribeComplete({ capacityObservations: 4 });
const hb = b.subscribeComplete({ capacityObservations: 4 });
a.accept(ready("private-A", 0.25));
b.accept(ready("private-B", 0.5));
const itemA = ha.take();
const statusB = hb.readStatus();
assert.equal(statusB.generation, itemA.generation); // collision is legitimate
assert.equal(statusB.continuityRevision, itemA.continuityRevision);
// A consumer that pairs itemA with hb must reject based on original handle
// association, NOT treat stamp equality as sufficient source authentication.
```

## Severity-ranked findings and remediation

### L-P9-1 — IMPORTANT INTEGRATION CONDITION, nonblocking in trusted-built-in proof: cross-handle stamps collide

**Evidence:** `spectrum-delivery.js:14-17,39-45,49-55,94-98`; reproduced with two actual producers at exact PR head. Each new producer starts its own generation, ordinal and subscriber continuity counters. The public receipt carries no globally unique handle or subscription binding.

**Failure hypothesis:** A future multi-instrument coordinator batches asynchronous processed items from multiple producer instances, accidentally pairs cached A with live B status, and concludes A's old or wrong-source spectrum remains eligible. Comparing `generation`, `continuityRevision` and `completionOrdinal` does **not** prevent this. Deliberately making counters globally unique is not required.

**Smallest correction:** Keep the real `subscription` object identity alongside each queued/async work item (e.g. `{handle, observation}` inside a host-controlled consumer wrapper). Check eligibility against that **same captured handle**, its current lifecycle fence and the measurement's expected source/method descriptor before committing derived output. Add two-provider and two-subscription **misbinding negative cases** before authorizing multi-provider composition. If persisted or cross-worker receipts are later required, design a versioned producer-instance identity and an authenticated/validated transport rather than pretending local counters are credentials. Current developer-facing docs already state the handle rule; codify it in integration tests when there is a coordinator.

**Disposition:** Do not block the narrowly scoped built-in delivery proof. **Block any claim of generic cross-provider receipt identity** until this rule is enforced/tested in the actual consuming host.

### L-P9-2 — IMPORTANT BOUNDARY CLARITY, nonblocking now: exported helper is not an authentication service

**Evidence:** `spectrum-delivery.js:1-20,87-124,158-164`, `spectrum-stream.js:76-118,152-185`. The `createSpectrumDelivery` internal helper can stage/commit a caller-supplied `publication` and its `ap117.spectrum-delivery/1` envelope records *claimed* publication data, not origin authentication. The public `createSpectrumStream` constructs `ap117.spectrum/1` itself after CP2 validation. A consumer receiving the subscription **only**, not delivery/producer, cannot invoke `accept/commit/fence` through that handle.

**Smallest correction:** Explicitly maintain the private host-held producer boundary and avoid exposing the low-level helper or the full `createSpectrumStream` object as a future third-party consumer capability. Schema/version/method checks at ingress are necessary for compatibility, but actual publisher registration is a **future host responsibility**. No credential system or new schema needed for the current built-in proof.

### L-P9-3 — POSITIVE: frozen spectrum, borrowed PCM distinguished correctly

**Evidence:** `fft-amplitude.js:69-82`, `spectrum-stream.js:154-176`, CP2 pipeline baseline, focused mutation check. Each delivered ready `ap117.spectrum/1` contains frozen ordinary arrays and immutable nested metadata. This is an appropriately shareable **built-in** numerical publication. CP2 `publication.waveform` remains a mutable typed array under a documented read-only borrowing rule; subscription consumers never receive it through `take()`. No source file/file handle or direct `readBlock` authority is exposed by the subscription.

**No change requested** to FFT, RMS, existing input copies or peak-amplitude convention.

### L-P9-4 — POSITIVE WITH LIMIT: status fences and caps are genuine, sandbox is not

**Evidence:** `spectrum-delivery.js:30-164`, matching source tests, isolated shape check. The subscriber has queue control and local `resync/dispose` only. Overruns are marked, not silently delivered. This is *not* a security enforcement claim about arbitrary JavaScript loaded in the page; a same-realm script could directly access ambient platform APIs or construct its own producer. Future installable plugins need explicit isolation/data release/consent requirements at the time they are proposed.

**No broad sandbox added to this PR.** The current app has no third-party plugin host or local WAV network-upload behavior in inspected code paths.

## Actual outcomes, unrun checks, and gates

- **Executed here:** the isolated exact-source V8 checks above (two producers with distinct source/values, stamp collision, handle API enumeration, deep frozen numbers, rejected forged CP2 method).
- **Verified remotely, not rerun:** GitHub Actions successful run at the exact head.
- **Source inspected only:** accepted base waveform copying, protected `readCurrent/isCurrent` and renderer source binding; the project's full 93-test claim, HTML/Chromium and real browser behavior were not reproduced.
- **Not tested:** hostile JS plug-ins, actual multi-provider host registry/consumer code (not implemented), live audio, full CPU/GC timing, worker serialization, transport/cross-realm isolation.
- **Conservative regression policy:** do not change accepted CP2 `ap117.measurement/2`, CP3-A peak FFT math/arrays or UI scheduling as an incidental trust fix. Any future identity fields in published schemas require version and compatibility review.
- **Remaining falsifier:** if actual host composition proves a wrong-handle item can *never* reach an incorrect status check by construction, the proposed test is a defensive assurance, not a product blocker. If a coordinator merges receipt streams without identity tags, this becomes a concrete integration fault and deserves a fix before acceptance.

### First-pass independence limitation / attribution

My source-derived trust finding and initial verdict were articulated **before** a subsequent broad PR metadata response unexpectedly included other reviewers' PR review texts. I did not deliberately query their new reviews and did not adopt their results; however, **I cannot claim that none of their text was exposed before final publication**. This report's focus and tests were independently reconstructed from the pinned code after that incidental exposure. Do not label it a pristine blinded first pass. The connected GitHub credential is shared; Latch is an attributed authorial viewpoint, not independent account authentication.

## Outcome and handoff

**COMPLETE — focused source-pinned trust/ownership review, no application modification.** **CONDITIONAL PASS** scoped to trusted built-in delivery. No observed blocking defect in the review remit. Recommend an explicit handle-bound consumer integration negative test before multiple actual providers are composed; retain the future-plugin sandbox boundary as deferred and unproven. Axiom and the owner retain integration/merge decisions. This report is not a blanket PR approval, trusted plugin certification, numerical accuracy audit or release authorization.

## Revisit when

Axiom proposes a cross-provider consumer/host coordinator, multiple FFT configurations, a serialized observation transfer, plugin installation, a new PR head, or an executable counterexample showing unexpected producer mutation/source aliasing.
