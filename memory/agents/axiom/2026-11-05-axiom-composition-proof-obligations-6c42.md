---
schema: 1
id: 2026-11-05-axiom-composition-proof-obligations-6c42
kind: lesson
scope: agent:axiom
status: active
evidence: inferred
author: axiom
created: 2026-11-05
updated: 2026-11-05
sources: "Transferable inference from Axiom's independent Studio contract integrity audit (memory/agents/axiom/2026-11-05-axiom-studio-contract-integrity-audit-02.md), review baseline 6ba81c0de15ea86f455f40f50ee6414f7e6f3216, and its source-identical isolated validator counterexamples recorded on 2026-11-05."
---

# Axiom — Proof obligations at composition boundaries

## Summary

A structurally valid component does not imply that its composition is coherent. When multiple representations or subsystems describe the same fact, local validity may coexist with a global contradiction. In the Studio audit, the validator enforced many JSON field restrictions but accepted contradictory Markdown role descriptions, catalog membership and free-text claims about authority and execution.

**Reusable Axiom practice:** For each consequential guarantee, distinguish (a) its authoritative owner, (b) permitted states and transitions, (c) the representation or subsystem boundaries that could disagree, (d) which part is mechanically enforceable and by whom, and (e) a minimal counterexample and executable check. Classify the remaining claims as documented policy, externally host-enforced behavior, or unverified hypotheses. Do not promote any one category to another.

The next question after “is this component valid?” is “does the composed system preserve the same invariant?”

### Working heuristics for future assignments

1. **Test seams, not only parts.** Start with two individually valid descriptions that make contradictory claims about the same fact. Check whether the contract rejects their coexistence. Favor an authoritative representation with verified projections over duplicated normative facts.
2. **Make the enforcement boundary explicit.** Static schema validation can verify syntax, types, references, and bounded parity; it cannot attest that a real agent ran, that a user approved an action, or that a host enforced privileges. Require evidence from the actual enforcing component.
3. **Use the smallest falsifier.** Mutate one property in a valid fixture while keeping everything else fixed. A precise accepted counterexample is more actionable than a broad warning about architectural drift.
4. **Resist formalism without an observed failure class.** Do not create a general orchestration layer, semantic natural-language validator, or elaborate compatibility framework to repair a simple cross-file mismatch. Prefer targeted checks, then expand only after a real requirement or counterexample demands it.
5. **Recheck the moving boundary.** A passing check at one Git revision does not certify the next pickup. Resolve actual refs at use time, compare relevant contract/schema compatibility, and record the provenance of what was loaded and executed.

## Evidence

**Observed in the cited audit:** The Studio's team validator accepted several synthetic contradictory contracts while appropriately rejecting explicit machine-readable permission violations. The audit pinned its source and ran 13 isolated probes against a source-identical validator. Those results establish the specific local counterexamples, not a universal rule about all validators or any proof of behavioral superiority over peer agents.

**Inference:** A general composition-proof checklist should help Axiom find the same class of defect earlier and with less unnecessary machinery. This is a proposed working method, not a tested comparative improvement to Axiom's performance.

**Development correction:** Axiom's known shadow is overformalization. The successful target is a failure class prevented by a clear, proportionate test—not the most elaborate model of the system. Invite a Flint-style simplification challenge and a Harbor-style lifecycle challenge when their distinct questions materially test the guarantee; do not imply they ran independently unless they actually did.

## Revisit when

A future review demonstrates that the checklist misses a material violation, an independently verified implementation eliminates the need for a proposed abstraction, or matched comparison shows the method helps or hinders real delivery. Revise the heuristic rather than treating this session as proof of universal effectiveness.
