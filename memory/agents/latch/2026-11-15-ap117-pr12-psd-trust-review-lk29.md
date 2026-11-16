---
schema: 1
id: 2026-11-15-ap117-pr12-psd-trust-review-lk29
kind: handoff
scope: agent:latch
status: active
evidence: observed
author: latch-ap117-pr12-trust-review-2026-11-15
created: 2026-11-15
updated: 2026-11-15
sources: "Auralprint ap_117_KESTREL PR #12 exact head 0880fc8df9182cce9ed2c645e324a2d291375281 versus accepted main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; issue #10 downstream handle-bound receipt contract; new psd-processor blob 8cca1cd0da4e4c79e2182aa3d219d55880f2efb3; unchanged spectrum-stream 4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc, spectrum-delivery ef19cd748de41226ab0cd8375949e278f7aeb76f, fft-amplitude ee35e0793aceb5eb9e3fc49d27f293a1719effc5; isolated V8 exact-source focused experiments and successful GitHub Actions 43789892097; own LK28 prior review."
---

# Latch — AP117-003 PR #12 downstream PSD capability and trust review

**Verdict:** **CONDITIONAL PASS** for the narrowly scoped **trusted built-in** downstream PSD consumer at PR #12 exact head `0880fc8df9182cce9ed2c645e324a2d291375281`. **No current-scope blocking defect reproduced.** One **IMPORTANT future host-integration guard** and one test-evidence qualification remain. Review is `COMMENTED`, not approval of schema adoption, merge, release or hostile-plugin security.

**Target:** [Auralprint PR #12](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12) against main `2957be0f2bf44ffd1865e21507f4c2ad94a34e1f` (PR #9 accepted). [Issue #10](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10) is the required downstream receipt/terminal gate; [Issue #6](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6) governs proposed PSD scientific labeling. Own prior trust finding: [LK28](2026-11-15-ap117-pr9-trust-review-lk28.md).  
**Perspective:** Latch — The Locksmith (`agents/latch-v1`); authorial attribution through a shared GitHub account, not cryptographic individual-agent authentication.  
**Scope:** Source review of code/tests/docs; two isolated V8 exact-source focused executions with ESM import/export syntax adapted only for explicit local dependency injection. **No application edits**, full Node/npm suite, Chromium, actual device, plugin sandbox, merge or release. No other new PR #12 peer report was opened before preserving this first pass.

## Summary

The new `createPsdProcessor` demonstrates the desired analysis-first, producer/consumer architecture: it takes completed `ap117.spectrum/1` windows from one actual subscription *when correctly wired by the trusted host*, independently computes `ap117.psd/1` periodograms, and emits frozen owned results without acquiring PCM read, FFT or producer mutation authority. Its zero-argument `take()` is synchronous and forbids externally supplied receipts. It distinguishes upstream end from consumer drain, and treats loss, origin mismatch and epoch changes as explicit fail-closed breaks. The accepted RMS, FFT, UI and latest-only display are untouched; the PR is six **added** paths, one commit ahead of accepted main.

**Principal dissent/evidence boundary:** constructor binding is to **functions supplied by a caller-provided object**, not an independently verifiable subscription registration. The negative case `psdB.take(receiptA)` proves **argument injection is forbidden**, but does **not** prove that a miswired/fabricated wrapper cannot substitute a well-formed item. I independently reproduced a composite wrapper that consumed B's genuine queue item for accounting and returned A's same-stamp, same-source-descriptor receipt instead. The processor accepted A's density as if from B. This explicitly **violates the declared exclusive genuine-handle/trusted-host contract** and **is not an exploit of the supported directly wired path**. It is a concrete falsifier of any broader statement that receipt fingerprints, closure-captured wrapper methods or numeric stamps alone authenticate source origin. No redesign of the PR or global producer UUID registry is warranted for the declared trusted direct-wiring scope; do not mark Issue #10's *future host wiring* gate complete based on only the forbidden-argument tests.

## Evidence

### Exact source and scope

- [`src/analysis/psd-processor.js` lines 1–276](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/src/analysis/psd-processor.js#L1-L276), blob `8cca1cd0da4e4c79e2182aa3d219d55880f2efb3`: source/config snapshot `sourceDescriptor/windowDescriptor`, function binding lines 56–70, status/frontier/fence lines 99–132, full fingerprint and densities lines 134–190, `take(...args)` admission + post-take check lines 192–240, resync/disposal lines 246–276.
- [`tests/psd-lifecycle.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-lifecycle.test.js) contains two distinct #10 tests (cross-provider matching counters and later subscription) but their misrouting step calls `take(receiptA)`, which necessarily throws due to argument count. It does not exercise an accidentally composite handle.
- [`tests/psd-boundary.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-boundary.test.js) uses deliberately faulty wrappers to test malformed observation/status and post-pull invalidation; this is properly described as validation testing, not third-party authentication.
- [`tests/psd-integration.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-integration.test.js) drives real CP2 acquisition → complete FFT → PSD in the checked-in fixture; exact 20-frame legal partition, lineage and operation counts asserted in test source. **Read; not independently rerun as Node suite.**
- [`docs/AP117_003_PSD_CONSUMER.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/docs/AP117_003_PSD_CONSUMER.md) explicitly limits origin guarantee to trusted exclusive host wiring; proposed rather than adopted schema; no hostile-plugin claim. Distinguishes producer `ended` with backlog from processor `take().ended`.
- [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2957be0f2bf44ffd1865e21507f4c2ad94a34e1f/src/analysis/spectrum-stream.js), delivery and FFT: accepted unchanged producer source. PR comparison returned **six added files, zero modifications/deletions**, ahead by one commit, behind zero. No extra source read or FFT logic was added in the PR.
- [GitHub Actions 43789892097](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43789892097) returned `completed/success` with exact PR head. Implementer reports `npm run verify` 119 Node tests, HTML and system-Chromium smoke green; those are **attributed CI/implementer results**, not Latch's independent re-execution.

### Independent focused execution

The exact `psd-processor.js`, `spectrum-stream.js`, `spectrum-delivery.js` and `fft-amplitude.js` code was fetched at PR head and evaluated inside an isolated V8 Function scope with only ESM imports/exports exchanged for explicit dependency injection. No algorithm or state-transition logic was changed. The local container cannot resolve `github.com` for a normal clone, so full `npm run verify` and browser suite were **NOT RUN** independently.

Fixture: periodic Hann `M=8, H=4, Nfft=8, fs=48000`; trusted-envelope CP2 ready values with matching RMS fingerprint, BigInt source spans and explicit delivery budgets; sources A and B use the *same legitimate source descriptor* but amplitudes `0.25` and `0.5`.

| Probe | Independently observed result |
| --- | --- |
| Correct A and B subscription → PSD | Both `observation`; A DC `0.000006944444444444445`, B DC `0.00002777777777777778` (4× ratio). |
| Direct attempt `psdB.take(receiptA)` | `TypeError` before dequeue; B pending remains `1`; correct A/B subsequent observations still produced. |
| Actual producer A/B local lifecycle counters | Identical first generation/ordinal/continuity, as expected; none are cross-provider identity credentials. |
| **Composite wrapper fault injection** | Wrapper `take()` consumes B item but returns A item; `readStatus`/resync/dispose use B. Same descriptor/stamps, legitimate B queue accounting. **PSD returned `observation` containing A's smaller DC value**, despite B's genuine value 4× higher. **Out-of-contract wrapper, not current-path exploit.** |
| Later subscription B after A's first window | B `take()` is `empty` at the old frontier; next legal 4-sample producer block gives B only completion ordinal `2` / frame `4n`; no adoption of A's earlier receipt. |
| Reset with retained old PSD | Consumer `readCurrent()` becomes `unavailable`; `take()` returns `break` reason `source-replaced`; old frozen object remains historical. |
| Final 20-frame block and capacity 4 | Upstream `ended` with `queuedObservations=4`, PSD status still `open`; `take()` yields four observations then `ended`. |
| Correct handle, wrong expected `sourceId` | PSD produces `break / invalid-spectrum-input`, not a falsely relabeled ready. |
| Owned numeric output | PSD observation, `densities` and `inputSpectrum` all `Object.isFrozen(...)===true`. |

The composite wrapper is a **deliberate violation of the trusted exclusive-handle assumption**. It demonstrates the limits of the supposed detection; it does **not** show a malicious third-party plugin can access the source, a browser exfiltration path, or a current consumer/producer race.

**Minimal falsifier sketch, for any future host wiring test (PROPOSED, not in PR):**

```js
const swapped = {
  take() {
    const ignoredOwn = handleB.take(); // advance B's queue/accounting
    return handleA.take();             // return A's well-formed same-stamp item
  },
  readStatus: handleB.readStatus,
  resync: handleB.resync,
  dispose: handleB.dispose,
};
const result = createPsdProcessor({
  subscription: swapped, spectrum: knownSpectrum,
  source: sameDescriptorForAandB,
}).take();
// Existing constructor cannot authenticate that composite wrapper;
// host MUST prohibit such composite/wrong-source wiring.
```

## Ranked findings and required disposition

### L-P12-1 — IMPORTANT host-integration guard, nonblocking for the current trusted built-in PR

**Observation:** `psd-processor.js:56-70,192-226` validates function presence and binds those function references. It never verifies that all four functions originate from the same actual native subscription or are the host-approved handle. Synchronous `take()` and post-pull queue checks prevent *many* accidental mixups; a composite wrapper that advances the expected queue before substituting a different well-formed observation evades them. The tests named as #10 negatives prove prevention of **argument injection** and **stale same-handle adoption**, not authentication of function-shaped wrappers.

**Requested disposition:** Keep the architecture and narrow trusted-host claim. Make the test-evidence wording precise: `take(receipt)` negative is an arity/caller-receipt proof, **not an authenticated-wiring proof**. Before a future host orchestrator or any arbitrary wrapper exposure, add a *host-level* test that binds the real issued capability A to consumer A and B to B without method mixing; verify that an accidental swapped binding is impossible or leads to an explicit error at the host boundary. If true arbitrary wrapper provenance detection becomes a product requirement, it needs a separately designed host/factory/branded capability boundary, not a patch to numeric generation IDs. **Do not close the entire Issue #10 integration gate merely because this opt-in processor exists.**

Severity rationale: **nonblocking today** because caller-supplied trusted native subscription is a stated precondition, no app host/third-party loader constructs composite handles, and the PR does not promise authentication against such adapters. The counterexample is a genuine limitation of the future trust boundary and a reason to avoid inflated acceptance claims.

### L-P12-2 — POSITIVE: ownership, output immutability and least authority

The new processor does not receive source file objects, CP2 waveforms, producer `accept/reset/invalidate` methods or FFT scratch buffers. It takes one complete spectrum record at a time from the subscription and returns owned frozen PSD densities and metadata; `readCurrent` retains just one result. A caller *with* the PSD processor API can `reset/resync/dispose` its own analysis, and `resync({source})` is a **trusted-host decision**, not an authentication claim. Hand out a narrower observer interface if a later untrusted panel should not be allowed to alter processor continuity. No sandbox, network policy or direct PCM handling is added or proven.

### L-P12-3 — POSITIVE: fail-closed lineage and honest terminal drain

One method/source/span/window/ENBW mismatch revokes current readiness; legitimate older same-generation windows remain eligible in order; epoch/reset fences and explicit resync mark abandonment. Producer EOF is not automatically PSD drain; final backlog yields four PSD observations then ended. No fake wall-clock or nonphysical sample-frame advance. The PSD is a **new derived scientific quantity** with versioned units/method, not a re-labeling of the unchanged FFT `ap117.spectrum/1`. Numerical accuracy beyond the focused DC checks belongs to Gauge's independently required review.

### L-P12-4 — CANDIDATE contract/adoption remains open

The module is opt-in, with no panels, alternate FFT config, generic multi-provider registry or hostile plugin runtime. Its new `ap117.psd/1` and `ap117.psd-delivery/1` schemas are still proposed. Issue #11 timing/GC envelope is deferred, not passed. The absence of changed production files is good regression discipline but not proof of application utility or correctness in an eventual installed consumer.

## Remaining uncertainty, dissent and recommendation

- **Dissent:** Reject any claim that `take(receiptA)` throwing **by itself** proves origin identity for arbitrary subscription adapters. The actual native, exclusive subscription-capability contract is the security-relevant premise. Stamps and a method fingerprint are descriptive, not authenticated origin.
- **Suggested narrow action:** Keep this PR scoped and accepted conditionally **for trusted direct-wiring**, and make future host-wiring acceptance explicit. If Axiom wants a test in this PR, add a small explanatory negative demonstrating the known fake-wrapper limitation, or clarify the #10 test language; do not introduce global producer IDs.
- **What would change the verdict:** Show that the supported host can unintentionally compose mixed-handle methods today; then promote L-P12-1 to BLOCK. Or show a real direct-handle wrong-source/old-epoch observation accepted after a fence; then BLOCK. Neither occurred in the tested direct path.
- **Out of scope:** no review of other new PR #12 agent responses, no local full suite, no hostile same-realm JS sandbox guarantee, no actual multi-panel system, no network exfiltration study, no calibrated device measurement.
- **Owner control:** User and Axiom integrator retain schema adoption and merge authority. This COMMENTED reviewer verdict is not an approval to merge.

## Outcome and handoff

**COMPLETE — independent trust-focused source review and isolated production-code V8 reproductions; application unchanged.** Report suitable for Axiom's reconciliation. Current work is six added files and a successful GitHub Actions run at exact head; Latch did not execute full repository CI or Chrome independently.

## Revisit when

Axiom designs the consumer host/registry, a second PSD provider or additional instrument uses this interface, someone proposes serialized receipts or third-party modules, Issue #10 is being marked done, or PR #12 gets a new head.
