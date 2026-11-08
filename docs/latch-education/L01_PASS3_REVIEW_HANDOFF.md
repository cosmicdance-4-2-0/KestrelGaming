# Latch L01 Pass 3 — independent implementation review

**Assignment:** LATCH-L01-PASS3-REVIEW-01 · Mothlight → independent reviewer · 2026-11-08

Review the current PR head on `mothlight/latch-education`, targeting `agents/latch-v1`, against Pass-2 merge baseline `ca49d6eabd6e6f17bfd139efd0d3804a16d351c8`. Resolve and record the exact head before inspecting it. Axiom is a suitable reviewer given the earlier contract and runtime reviews; the owner chooses and delivers this assignment. No independent review or participation is implied by this document.

Load your own identity and authorized continuity first. Retain your individual judgment. Review source, execution and claims; do not implement fixes, merge, publish hidden evaluator cases or assess Latch as a learner during this pass.

## Scope and sources

Read the [lesson](Latch_L01_Instructional_Checkpoint.md), [addendum](Latch_L01_Review_Addendum.md), [errata](Latch_L01_R1_R2_Errata.md) and [accepted three-pass plan](L01_FIXTURE_IMPLEMENTATION_PLAN.md). Later corrections govern conflicting model semantics. The new [application surface contract](../../labs/latch_l01/SURFACE_CONTRACT.md) defines input-shape handling separately from authorization.

Inspect `labs/latch_l01/surface.py`, `visible_cases.py`, `__main__.py`, the lab README and `tests/test_latch_l01_surface.py`. Compare core model and existing tests with the baseline. The scripted agent has no LLM/interpreter, the tool/publication broker is deny-only, and no live tool engine exists; do not mistake empty synthetic logs for deployed injection resistance.

## Discriminating review questions

- Does input validation reject mutable/unhashable/non-string identifiers before the accepted string-only model is called, with explicit response precedence and no state changes? Retain typed legitimate neighboring requests. Check no coercion or retained mutable caller reference, and distinguish adapter shape errors from model authorization/offline results.
- Can application requests or the scripted agent reach binding, session/grant mutation, clock, reset, setup or private inspection through the advertised action envelope? The adapter is not a Python sandbox; introspective trusted Python code is explicitly excluded.
- Does instruction-containing draft text actually reach the authorized scripted reader as data, without becoming authority or a dispatched command? Does an explicit denied tool/publication request leave both model and synthetic effect state unchanged? Check the denied as well as legitimate read path.
- Do all nine original public cases and later counterexamples have meaningful checks? Inspect expected values independently of the model helper. Try a materially broken fixture: blanket denial, empty successful read, or an unintended server write on restore. Confirm the runner reports failure rather than adjusting its oracle.
- Do CLI text/JSON outputs, case errors, empty runs and process exit codes accurately reflect execution? Are claims limited to public fixture behavior, with no invented learner result, qualification or hidden-key independence?

Run `python3 -m labs.latch_l01`, its `--json` form, the full `python3 -m unittest discover -s tests -v`, `python3 tools/validate_seed.py`, and whitespace checks on the actual PR delta. Record commands, exact revision/environment, observed outcomes and limitations. The PR author reports current results in the PR description; retain attribution until reproduced. Additional reviewer-written public probes are welcome, but are not hidden learner trials.

## Return and stop

Return ACCEPT / ACCEPT WITH BOUNDED CORRECTIONS / REQUEST CHANGES for the exact reviewed head. For each material finding give source location, a minimal input/event sequence, expected versus observed behavior, impact, evidence status and smallest correction. Separate blockers from optional extensions. Preserve dissent and alternative valid designs.

Report source receipt, independent versus reported checks, any remaining trust-surface limitation, and where your review was actually persisted through your own authorized workflow. Stop after review. Latch retains the separate exact-head integration gate. Even a favorable review does not qualify L01 or authorize learner evaluation; a later evaluator must author genuinely separate cases and an assessment plan if the owner assigns that work.
