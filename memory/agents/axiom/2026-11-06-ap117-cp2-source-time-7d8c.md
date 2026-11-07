---
schema: 1
id: 2026-11-06-ap117-cp2-source-time-7d8c
kind: lesson
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-06
updated: 2026-11-06
sources: "Owner requested the next checkpoint after CP1; ap_117_KESTREL PR #2, final head e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb; home baseline 3017652b19c72bc89a032bd541f322cabcabb2f8."
---

# Axiom — Source time is part of measurement meaning

## Summary

A replacement source is not interchangeable if its measurements inherit a clock
label from the previous implementation. The source must supply its sample clock
and lineage; an analyzer must preserve them. An incompatible correction deserves
an explicit contract version, even in an early prototype.

[Project PR #2](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/2)
is stacked on still-unmerged CP1; neither PR is owner-accepted merely because work
continued. Keep detailed implementation, contracts and fixtures in the application
repository. This record preserves only engineering continuity and evidence limits.

## Evidence

- Loaded Axiom's common contract, personality, structured profile, protocols, index
  and CP1 record at home baseline `3017652b19c72bc89a032bd541f322cabcabb2f8`.
- Local CP1 reconstructed through the authorized connector because ordinary Git
  authentication was unavailable for the target. All 25 file contents matched Git
  blob hashes; the resulting base tree matched GitHub's existing tree. Remote
  commits use real upstream parents, not the local snapshot's substitute history.
- Local CP1 tests: 21 pass. Final CP2: 34 pass; static build and official Nu
  checker pass. A frozen Python-wave fixture was independently reproduced.
- Local Chromium launch failed on denied socket creation; shared browser could not
  connect to localhost. CI browser execution is recorded in the PR; failed launch
  attempts are not substitutes for real browser evidence.
- Axiom home validator already failed before this record: one broken relative link
  in the CP4 follow-up memory and two agent-scoped handoffs rejected for scope/next
  action. Preserve these as baseline debt; do not rewrite unrelated memory during
  the application checkpoint. The baseline suite ran 83 tests: 78 passed and five
  failed on those same three validator findings. The new record adds no validator
  diagnostics; whole-home validation is still red.

- Final project head `e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb` passed
  [CI run 42329197868](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42329197868):
  34 tests, static build, official Nu on built/three rendered documents, and real
  Chromium interaction checks. Initial screenshots were inspected; a one-sample
  display edge was corrected and gained a browser pixel check. PR #2 is ready for
  review, remains stacked on CP1, and is not merged. Device performance and other
  browsers remain unverified. Local source tree equals remote tree
  `b55022c56005e9aebdb2f1628e13f128e2d3f2bc`.

## Revisit when

Review the exact final PR head and its CI evidence before accepting CP2. Retain the
working prototype and the explicit source/measurement boundary. Stop for independent
and owner review before expanding to the next algorithm or renderer. Do not merge
CP1 or CP2 as an inferred side effect of implementation authorization.
