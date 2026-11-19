---
schema: 1
id: 2026-11-18-ap117-ux0-gauge-independent-r12
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: draft
evidence: inferred
author: chatgpt-gauge-session
created: 2026-11-18
updated: 2026-11-18
sources: "AP117-UX0 user handoff; pinned AP117 main 78c68bb5ccd3a3c45fb26eb48754e55cbfbb478a; Auralprint1 116 75e26348848f874329ca1ac95bb13576371ed2da; draft Legacy116Orb PR20 cd0ca25616a3f7277df0bc7bf1a913b8aec3957f; source inspection and local disposable Chromium mock checks on 2026-11-18."
---

# Gauge — AP117-UX0 independent experience architecture, review risks and design dissent

**Status:** Complete independent **provisional** design; **NOT** six-agent reconciliation, approved app architecture, implemented feature, final UX0 gate or merge authority. No AP117 production files or unrelated PSD/performance work touched. Gauge's conclusions are independent attributed design work; no cryptographic runtime identity is claimed.

## Summary

**Preferred UX1 experiment: contextual instrument workbench.** Workspace owns instrument surface placement, layout and selection; Scene owns authored world/Scene entities and future explicit saved camera; host owns PCM/source, analysis resource identity/continuity, trustworthy subscription creation, clock, transport and single FrameHost. Instrument surfaces and Scene entities may share typed lifecycle vocabulary but are not the same authored object. An Inspector emits owner-validated commands, never changes PSD/RMS/FFT semantics by editing a presentation value. A small trusted descriptor catalog for the two existing scopes permits generic add/select/duplicate/reorder/remove without instrument-type branching in central UI; **not** a generic plugin API.

The competing scene-first interaction design is worth a deliberately separate UX2 test because it prioritizes the creative Scene experience but can obscure measurement provenance. No usability results establish which wins. Neither prototype is the source app or demonstrates any audio math.

**Source/time boundary is central:** Current AP117 analyzes local PCM; **no audible playback engine exists**. Its transport is a sample-advancement analysis timer, not playback. Browser-decoded compressed audio is resampled and uses a distinct decoded PCM clock/source domain versus native WAV. User-facing time and status labels must be driven by authoritative sample span/method/source and explicit validity, not rAF, display animation or transported pixel history.

**Status cannot be cosmetic:** A given analysis binding distinguishes unavailable, ready, stale, broken, historical, terminal producer-ended pending consumer drain, and actually drained; measured zero is valid only if a ready observation really has numeric value zero. A previous PSD under a continuity fence is **historical**, not current or an automatic replacement subscription. Do not fold Issue #14 recovery or Issue #11 performance into UX0.

## Evidence

**Current AP117 source at pinned exact head**: `AGENTS.md`, `src/main.js`, `src/config.js`, `src/analysis/{pipeline,spectrum-stream,psd-processor}.js`, `src/host/psd-session.js`, `src/visualizers/{signal-scope,spectrum-scope}/model.js`, `src/camera/orthographic-2d.js`, `src/rendering/{frame-host,canvas-2d-backend}.js`, `index.html`, `styles.css`, `docs/AP117_LOCAL_BROWSER_AUDIO.md` and `docs/ARCHITECTURE.md`. Current project base verified as `main@78c68bb5ccd3a3c45fb26eb48754e55cbfbb478a`. AP117's pure Camera2D projection lacks an accepted gesture controller. CONFIG is frozen; accepted persistent Workspace/Scene preferences are not part of this baseline.

**Historical 116 at its exact head**: `AGENTS.md`, `src/js/ui/{workspace,camera-interaction,camera-controls,orb-editor,visualizers-panel,ui}.js`, `src/js/core/{preferences,camera-projection,orb-collection}.js`, `src/js/render/visualizer-runtime.js`, `src/js/audio/{audio-engine,analysis-frame,band-bank}.js` and camera interaction tests. 116 has independent panel visibility/focus and a full source/playback pipeline, per-Orb identity/visual simulation, single-origin viewport and robust one-/two-pointer handling. Its display energies are normalized/clamped analyser-dB activities, **not** calibrated AP117 PSD. PR20 [Legacy116Orb behavior reference](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/cd0ca25616a3f7277df0bc7bf1a913b8aec3957f/docs/legacy/Legacy116Orb.md) records this boundary but is draft only.

**Disposable experiments (not GitHub-app code):** two 29 KB self-contained, offline HTML/CSS/JS concept mocks were generated in the user conversation workspace, "UX0 A contextual workbench" and "UX0 B scene first", plus responsive screenshots and a full 28 KB UX0 source-pinned design/report delivered as a downloadable ZIP. Both show illustrative plots only; selecting a file just displays its name, never decodes it. Chromium/Playwright `set_content` executed DOM/JS in four combinations: A/B at desktop 1280x800 and mobile viewport 375x667. All four passed initial identity, duplicate/reorder/remove/session-only Undo interactions without JS exceptions. Two additional desktop mock tests passed separate RMS-versus-spectrum statuses, generic instrument descriptor add, synthetic second-touch acquisition with unchanged pose, simulated pinch/twist, cancellation, and Reset. Browser file/localhost navigation was disallowed in this environment, so `set_content` was used. **These are narrow mock checks**, not human usability, native mobile hardware, 116 camera exact physics, scientific production tests, screen-reader qualification or realtime performance.

## Invariants and falsifiers

1. **Source and resource cannot be owned by a card:** two cards bound to the same producer, reorder one; actual source/FFT/PSD counts and continuity remain unchanged.
2. **Scene entity != instrument surface:** removing a Workspace card cannot delete an Orb scene entity; changing World view cannot redefine a card's PSD units.
3. **Identity survives rearrangement:** duplicate creates fresh opaque ID but copies *only* authored display settings, not runtime history or a second FFT. Remove the clone; original ID/runtime survives.
4. **Viewport cannot own source time:** resize/DPR/rAF coalescing/pause do not fabricate sample intervals or silent zeros; per-binding provenance stays inspectable.
5. **Two touch is a state transition, not a camera jump:** first touch pans, second touch acquired with no immediate pose change; pair move preserves anchor, surviving touch rebases without jump; pointercancel/lostcapture/blur/visibility releases ownership before native capture cleanup.
6. **Inspector scientific edits must fail closed:** view-only style changes do not alter reference, method, source epoch, sample clock or PSD derivation; valid analysis configuration changes route through the authoritative CONFIG-derived resource owner after separate scope approval.
7. **Touch parity:** add/select/edit/remove/restore and recovery can be completed with visible buttons and touch only, without hover/shortcuts/long press; keyboard and screen-reader equivalents remain.
8. **Bounded UX1:** existing two Canvas surfaces and one FrameHost can coexist. Do not require extra FFT, independent input, generic compositor, arbitrary plugin, source playback or renderer migration.

**Proposed command/ownership:** generic instrument catalog with `add/select/duplicate/reorder/remove`, contextual Inspector and session-only layout history; host-owned resource binding with actual originating producer identity and typed status; Scene viewport/gesture state separated from authored Scene configuration. `CONFIG → proposed validated preferences → derived effective settings → runtime state` is the hierarchy; only CONFIG + runtime exist today. Persistence, schema, import/export and reload-surviving workspace restore are **not** granted in UX0. A session-only explicit Undo can meet a narrower restore journey without claiming permanent saved layouts.

## Dissent / provisional decision

- A **Contextual Workbench** exposes scientific labels, discovery and explicit instrument ownership, likely suitable for UX1 with the current pair of scopes. Could sacrifice Scene area on mobile; must be falsified with users.
- B **Scene First** reduces panel density, offers direct manipulation, and better reflects eventual artistic work, but may conceal failure reasons/methods behind overlays and create gesture conflicts. Must remain an independent trial, not silently folded into A.
- Do not blindly unify Scene authored entities and Workspace instruments; the difference in lifetime/simulation/permissions is meaningful. Do not reuse 116 band index meaning, its dB-normalized activity or panel UI as a 117 method.
- Open decision: whether after-reload Workspace restoration warrants a separate versioned persistence schema. **Do not invent one in UX0.**
- Only Mothlight UX0 first pass [Issue #21](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/21) was identified at the time of source investigation; Axiom/Kite recorded first passes were not found. I deliberately did **not** consume Mothlight's report or claim to reconcile other agents. Formal Gauge adversarial review against all three first-pass artifacts must be rerun after they exist. Preserve disagreement rather than claiming consensus.

**UX1 proposed scope:** descriptor-driven two-scope workspace, exact scientific status/provenance/read-only inspector, desktop rail/mobile accessible sheet, session-only layout/Undo and one host-owned binding projection, with no DSP/backend changes. **UX2 proposed scope:** minimal Scene viewport/entity lifecycle, gesture-owner arbiter and touch/keyboard camera tests using 116 as behavioral oracle, then comparative user observations for A versus B. Both require explicit owner handoff/acceptance and independent rollback boundaries.

## Revisit when

Axiom/Mothlight/Kite source-pinned independent UX0 first passes are all recorded, the owner requests actual reconciliation, new mobile usability evidence overturns these hypotheses, 117 source/head changes, or an authorized UX1/UX2 implementation needs precise interface approval. Do not treat these prose invariants as executed AP117 tests.
