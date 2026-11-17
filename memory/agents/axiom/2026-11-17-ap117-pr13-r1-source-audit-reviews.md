---
schema: 1
id: 2026-11-17-ap117-pr13-r1-source-audit-reviews
kind: review
scope: agent:axiom
status: active
evidence: observed
author: axiom-pr13-r1-assessment
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint PR13 R1 comment 6942893831; source head bce44420bb7053556a10d40fef97afd91ad9c499 vs prior 2d417adab3f28315c0cbde63048851ae6e44bca8 and base bdead48ae672ed6834eae274c8876944a79104bc; compare diff, src/main.js exact new source; CI run 44047034181 job133915182137; Axiom PR13 review dispatch comment 6942947627."
---

# AP117-004 PR #13 — bounded R1 source verified, targeted review pending

## Verified state
Codex [R1 completion comment](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6942893831) observed. Draft PR remains open, unmerged, mergeable; head **`bce44420bb7053556a10d40fef97afd91ad9c499`**, parent prior reviewed `2d417adab3f28315c0cbde63048851ae6e44bca8`, accepted main/base `bdead48ae672ed6834eae274c8876944a79104bc`. R1 one commit, 4 changed paths +162/−16: `src/main.js`, app integration/browser tests, host PSD session doc. No core native-subscription `src/host/psd-session.js`, producer, FFT/PSD numerical or schemas, CONFIG, FrameHost or Canvas work changed.

`src/main.js` `bindRange` now compares actual synthetic sourceRevision before/after setter; only real change invalidates CP2 pipeline and spectrum. No-op control refresh remains and active PSD history continues. **Compatibility change:** accepted pre-PR host invalidated on any input even equal value; R1 intentionally removes pointless no-op fence, explicitly documented and test guarded. Real value edit still triggers deliberate sticky PSD hold until explicit source restoration/replay; no resync. Diagnostic uses `PSD session ready; source paused` when session eligible but host stopped; reports `PSD admission failed; no subscribed coverage began` for never-admitted, not lost scientific coverage; real break remains `lost coverage`. Recovery copy names synthetic source and file Replay/source actions.

Actual production `main.js` integration tests added no-op amplitude/frequency real source revisions, producer counters, frozen PSD history, true edit sticky failure, initial admission injected rejection and later genuine gap, pause/resume status. Browser smoke now checks same-value input while paused and correct copy; no new visualizer.

[CI run 44047034181](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44047034181) verified job 133915182137 full log: **131/131 Node pass, zero fail/skip**, build, official Nu built/rendered HTML, Chromium offline browser smoke, whitespace success. Tests ran on PR merge ref `c580a90151a881c52a5625ed68360f02be16e7ee` combining this exact R1 head with unchanged main; no independent local Axiom npm/browser execution. GitHub Actions Node20 support deprecation warning, not failing gate.

**Axiom R1 source PASS, overall MERGE HOLD**. Published [targeted exact-new-head handoff](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6942947627):
- Harbor: no-op vs true edit, first/last fence, recovered lifecycle/EOF.
- Mothlight: paused vs processing, never-admitted vs lost coverage, historical status, recovery instructions.
- Flint: preexisting host no-op invalidation compatibility, minimality.
Original first-pass Latch/Gauge/Kite PASS remains pinned to `2d417ad`; native handle, FFT/PSD algorithm and bounded drain untouched, targeted re-review only if counterexample/new scope. Owner must accept genuine-edit hold-on-break as scoped prototype tradeoff before a merge verdict; not permanent instrument policy. Issue #10 host gate open, #11 performance and #7 PSD visualization deferred.

No app code edits, merge, deploy or release by Axiom.
