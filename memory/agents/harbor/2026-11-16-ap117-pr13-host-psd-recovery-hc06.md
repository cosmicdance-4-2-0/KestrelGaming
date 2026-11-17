---
schema: 1
id: 2026-11-16-ap117-pr13-host-psd-recovery-hc06
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-ap117-004-pr13-review-session
created: 2026-11-16
updated: 2026-11-16
sources: "Auralprint PR #13 Axiom dispatch issuecomments 6913221997 and 6914016022; source/test/host contract at PR exact head 2d417adab3f28315c0cbde63048851ae6e44bca8 against accepted main bdead48ae672ed6834eae274c8876944a79104bc; Harbor home agents/harbor-v1@0db42b9e5758edea65b8510e4c44ad98c7ece88e; 17 focused V8 isolated checks and one direct main.js bindRange+synthetic source no-op reproduction; GitHub Actions 43844573608 attributed to CI."
---

# Harbor HC06 — AP117-004 PR #13 independent host PSD lifecycle/recovery review

**Task:** Axiom/Codex AP117-004 / CP3-B1-H1 specialized Harbor review of EOF/fence/recovery, import, source and channel changes, render faults, pagehide/BFCache, truthful sticky causes, and independent consumer failures.  
**PR:** [Auralprint #13](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13), exact head `2d417adab3f28315c0cbde63048851ae6e44bca8` against `main@bdead48ae672ed6834eae274c8876944a79104bc`. Review head remained unchanged and PR open/draft at verification.  
**Harbor home before report:** `KestrelGaming/agents/harbor-v1@0db42b9e5758edea65b8510e4c44ad98c7ece88e`.  
**Disposition:** **CONDITIONAL PASS in Harbor lifecycle/remit.** No source/producer/processor integrity blocker reproduced. One **moderate source-lifecycle/UX problem, HC06-01**, requires a bounded correction or explicit owner-accepted tradeoff before merge; deliberate hold-on-break for **real** source/parameter transitions remains sound. All other product, schema and merge decisions remain with Axiom/owner. No application code changes.

## Summary

The new [host PSD session](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/host/psd-session.js) subscribes through the selected producer's actual native handle and owns one headless PSD processor. The host [main.js](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/main.js) creates a subscription **before accepting the first ready CP2 block**, drains after each successful FFT `accept()` rather than via rAF, and drains before `stop("complete")`. This preserves the accepted CP2/CP3-A acquisition, source chronology and numerical methods while adding an honest per-session diagnostic.

**Essential Harbor distinction:** the PSD window can remain historically valid when the producer is ended, the host paused, or continuity fenced. A loss in that consumer's coverage must not become a fictitious continuous measurement. Under normal EOF and error transitions the implementation respects this: `readStatus().upstream.status=ended` is distinct from `session.state=drained`, sticky first and latest causes remain visible, and source replacement disposes the old association first.

**HC06-01** is a concrete source-control false positive amplified by the newly permanent hold policy: the unchanged [synthetic sine source](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/audio/synthetic-sine.js#L50-L56) increments `sourceRevision` *only when the value actually changes*, while [main slider handler](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/main.js#L145-L163) invalidates pipeline and spectrum for *every* `input` event without comparing the revision. An event that merely reasserts the existing value (whether a duplicate DOM input event or a test/automation injection) changes `sourceRevision:0 → 0` but publishes `source-parameters-changed` and leaves PSD broken for the remainder of the association. The handler's broad invalidation predates PR #13; the long-lived PSD outage under hold-on-break is newly consequential.

## Evidence

### Exact-head source inspection

- [`src/host/psd-session.js:11–132`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/host/psd-session.js#L11-L132) constructor/source ownership, native handle, capacity4+1 drain, sticky break, disposal, no resync. Only 134 source lines and this is the entire new production module.
- [`src/main.js:60–133`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/main.js#L60-L133) reports last PSD span/history versus source input/peak publication/subscription/last painted peak; revokes association on unapproved sourceRevision.
- [`src/main.js:145–178`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/main.js#L145-L178) synthetic setter and render-error global stop/invalidation. [`src/main.js:188–255`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/main.js#L188-L255) latest-view drawing separate from analysis, first-ready PSD admission before FFT, `psdSession?.drain()` before ordinary final `stop("complete")`, and post-render-failure EOF `stop("replay-required")`.
- [`src/main.js:259–389`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/main.js#L259-L389) stop/start, `install` disposal before spectrum reset, file import loading/error/cancel, source/channel restoration/replay, explicit render retry, idempotent pagehide, BFCache reload. [`src/audio/file-import.js:8–35`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/audio/file-import.js#L8-L35) generation-token late result fence.
- [`tests/psd-session.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/tests/psd-session.test.js), [`tests/app-integration.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/tests/app-integration.test.js), [`tests/browser-smoke.mjs`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/tests/browser-smoke.mjs), [candidate host contract](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/docs/AP117_004_HOST_PSD_SESSION.md), [Auralprint AGENTS.md](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/AGENTS.md). Ten changed paths; CP2, FFT, PSD processor and subscription producer source are unchanged by PR #13. Package/lock only raise declared Node engine minimum to >=22.15 for the test-only Node module hook.

### Reproduced source-executed controls

**14/14 PASS in one isolated V8 pass:** Fetched exact PR-head original `fft-amplitude.js`, `spectrum-delivery.js`, `spectrum-stream.js`, `psd-processor.js`, `psd-session.js` and `synthetic-sine.js`; adapted only ESM import/export syntax to explicit in-memory dependency injection. Used synthetic versioned CP2-ready envelope and Hann M8/H4/N8 with explicit resource budget. Not a full CP2 pipeline execution.

1. Producer `ended` with four complete `[0,8),[4,12),[8,16),[12,20)` observations gives `source-ended-drain-pending`, then one bounded drain returns four ordered PSDs and `drained`; no next take duplicates history, last PSD historical.
2. One final20 in 5×4 synthetic block partitions produces the same four spans. Completing CP2 revisions in the direct envelope were supplied by the fixture, not measured by actual CP2.
3. Seven-frame short final produces zero PSD and a properly drained session; 8+2 partial tail retains only last genuinely complete PSD.
4. `source-parameters-changed` fence holds broken after later accepted sourceRevision-1 input; prior valid PSD is historical, never silently restored.
5. First/last causes remain `source-parameters-changed` / `render-failed` on successive fences.
6. Capacity2 subscriber breaks with `subscriber-delivery-overrun` and no partial batch while separate cap4 succeeds.
7. Dispose old PSD session before source reset; old handle cannot reopen; new producer session on new epoch receives new observations.
8. Unknown construction keys and foreign receipt arguments rejected before consuming the subscribed handle.
9. Ordinary repeated EOF cannot resurrect ready or generate duplicate PSD.
10. Malformed second consumer record causes consumer-local `invalid-spectrum-input` without corrupting producer/peak; throwing consumer `take()` triggers sticky `psd-consumer-error`, not global FFT invalidation.
11. Injected throwing `dispose()` remains idempotent; after disposal no more `take()` work.
12. The synthetic setter's **same-value input** leaves source revision unchanged; independently calling the spectrum's established invalidation does fence the current PSD association.

**3/3 PASS in a second exact-source async importer pass:** (a) pending file load canceled by restoration cannot install its late resolution; (b) pagehide-like importer disposal prevents late result and post-disposal state callbacks; (c) invalid/oversized file reports error then settled and installs nothing. These test the unchanged importer module, not the whole actual browser host.

**1 direct handler reproduction of HC06-01:** Extracted the exact `bindRange` function from the PR-head `src/main.js` (unchanged text), compiled it with a production `createSineSource` and minimal DOM/host substitutes. Triggered a same-value amplitude `input` event at 0.5. Observed **sourceRevision before=0, after=0** while both `pipeline.invalidate("source-parameters-changed")` and `spectrum.invalidate("source-parameters-changed")` executed, authorized revision remained 0 and diagnostic update/draw occurred. This reproduces the incorrect source-change predicate. Separately, session-level test showed the corresponding `spectrum.invalidate` makes PSD sticky broken; the original whole `main.js` was **not** executed by Harbor in this test. No claim of an observed real user/browser input event firing spuriously; dispatching duplicate `input` is a valid deterministic fault/control fixture.

**CI provenance:** [Actions run 43844573608](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43844573608) at exact PR head completed successfully, with all verify job steps green. Codex/Axiom attribute 131/131 Node tests and HTML/Chromium. Harbor **did not independently run** `npm run verify`, actual browser/BFCache, physical device/GC measurements or the complete production `main.js` via Node module hooks. Local `git ls-remote` attempted against GitHub and failed DNS (`Could not resolve host: github.com`); connector source inspection and isolated V8 execution were used instead.

**Review independence qualification:** GitHub's PR comments fetch returned Axiom's handoff together with some already-posted reviewer text (including Mothlight), before all independent controls were run. This is **not a blind first-pass review**. All claims of 14 + 3 V8 and one direct handler reproduction refer to tests Harbor executed in this session, not peer-reported tests; observations and conclusions are not claimed as evidence of independent discovery prior to reading the thread. Other reviewers retain their own authorship.

### Findings and decision

**HC06-01 — MODERATE, reproducible; request owner disposition / smallest correction.**

- **Counterexample:** Existing amplitude=0.5. Trigger a duplicate synthetic range `input` with the same value. Source revision remains unchanged; host nevertheless declares source parameters changed and invalidates RMS/peak and the subscriber's continuity. Under the new no-resync/hold rule, next normal data may restore RMS and peak but PSD session stays broken, reported as lost coverage until the user explicitly chooses synthetic restoration/replacement/replay.
- **Cause:** `main.js:150–159` invalidates unconditionally after invoking the existing setter; the source's version semantics in `synthetic-sine.js:50–56` do not treat no-op as a parameter transition. The recovery contract for **actual** change is not at fault.
- **Minimum proposed fix (not implemented):** Capture before/after `source.getSettings().sourceRevision`. If equal, update displayed control as needed but do **not** call `pipeline.invalidate` or `spectrum.invalidate`; otherwise preserve current authorized revision, legitimate fences and hold policy. Add one direct host control/integration regression (duplicate input must preserve PSD session/coverage) and positive control (actual value change must fence).
- **Alternative:** Explicitly ratify arbitrary slider input as a reset command, rename the cause and make the intentional reset visible. This preserves current code but is disproportionate for an ordinary range input; I recommend the revision guard.
- **Severity distinction:** This is a workflow/diagnostic false-positive and recoverability problem, not a wrong PSD density or evidence that an invalid FFT window was released.

**HC06-02 — OWNER RECOVERY-POLICY TRADEOFF, not a code defect:** Even genuine synthetic parameter change holds PSD unavailable for the entire source association while RMS/peak continue. This is faithfully documented and represents deliberate, conservative loss handling. An owner may accept it as a limited first-slice policy, but should explicitly choose it rather than assuming PSD will resume after reconfiguration. Do not silently add `resync` or change the compatibility boundary in review. If owner later wants automatic new-segment analysis, require a separately authorized, explicit discontinuity/new association policy.

**No Harbor blocking findings** for EOF drain, status cause preservation, source-replacement disposal, import cancellation, late completion, consumer isolation, fixed capacity or accepted global render-error policy. The source-level final render/retry/replay-required path is consistent with existing invariants, but was **not independently exercised in a complete browser/host run**; rely separately on exact-head CI.

**Recommendation to Axiom:** CONDITIONAL PASS. Request a minimal no-op control check/fix and/or explicit owner resolution of HC06-01 before a merge recommendation. Preserve genuine hold-on-break as designed unless owner selects a different recovery scope. A changed PR head requires a new review of affected lines and a fresh exact-head test check.

## Revisit when

Axiom reconciles six reviews; the owner decides HC06-01 and genuine slider hold-on-break; a corrective PR head changes `bindRange`, the session association, import/replay or EOF; a real host/browser test demonstrates a conflicting behavior; or a separately authorized new-source PSD recovery design is approved. Re-resolve SHA and preserve any dissent by attribution. Shared GitHub account authentication is not individual agent identity authentication.
