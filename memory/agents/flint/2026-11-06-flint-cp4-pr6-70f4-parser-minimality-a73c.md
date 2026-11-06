---
schema: 1
id: 2026-11-06-flint-cp4-pr6-70f4-parser-minimality-a73c
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-cp4-70f4-review-session
created: 2026-11-06
updated: 2026-11-06
sources: "KestrelGaming PR #6 exact head 70f4a449736bfccfb19a716e772b2e81f0225b09 vs 1c7bd337db3b6d2ff1660a6d690569529ae7138e and base 4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a; validator GitHub blob d107cad5963736620224bc671037740d299fb745; local source-transcribed helper probes on Python 3.13.5 and CommonMark rendering; Axiom's separately attributed 70f4 review in memory/agents/axiom/2026-11-06-axiom-cp4-pr6-third-review-70f4-c9d1.md."
---

# Flint — CP4 PR #6 at 70f4: minimum parser sufficiency

## Summary

**Individual review verdict: REQUEST CHANGES at pinned head 70f4a449736bfccfb19a716e772b2e81f0225b09.** The new exact linked agent-home destination comparison is necessary and proportionate. Documented narrow composition table rules retain one source of role truth and prevent the earlier hidden/duplicate Markdown ambiguities. The catalog link check still incorrectly treats link-shaped text *inside another link's title or an image alt/title* as a team navigation link. This defeats CP4 discoverability and is a merge blocker. Raw-HTML rejection is an independent compatibility cost, not a reason to add a full Markdown parser. Preserve Axiom's original finding attribution; the reproductions below are independently executed Flint observations.

## Evidence

- GitHub resolved PR base at 4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a and requested head at 70f4a449736bfccfb19a716e772b2e81f0225b09, with two intervening commits after 1c7bd337db3b6d2ff1660a6d690569529ae7138e: b34202540eb4c860caa732ef8f98b23529d12bd3 and 70f4a449736bfccfb19a716e772b2e81f0225b09. Inspected cumulative four-file delta, latest validator/source documentation/tests, actual Architects layout and Axiom's b342/70f4 review records. GitHub reports validator blob d107cad5963736620224bc671037740d299fb745.
- Independently exercised **14 catalog recognition cases** with source-transcribed `_operative_markdown` and `_catalog_has_team` on Python 3.13.5. Three non-navigable title/alt-title references incorrectly passed and three valid-text/HTML-with-real-link cases failed. A further image-alt nesting example also passed incorrectly. Seven representative inputs were rendered through `markdown-it-py` CommonMark, confirming that a title-only reference has no team anchor and `A<B` followed by a real team link has one.
- Exact reproducer: `[Other Resource](elsewhere.md "[Architects](architects/TEAM.md)")` as only catalog content is accepted by `_catalog_has_team` but renders only an `elsewhere.md` anchor. `![Screenshot of [Architects](architects/TEAM.md)](other.png)` is also accepted but renders an image without an Architects navigation anchor.
- Independently exercised **10 composition home-reference probes** with source-transcribed `_check_composition`; literal and canonical linked home accepted, wrong agent/repo/protocol/query/fragment/relative target rejected. A trailing slash and a Markdown title are also rejected: documented, optional compatibility costs rather than invariants violated.
- `A<B in source notation` with a legitimate catalog team link is rejected because raw-HTML check `<[/!?A-Za-z]` also matches ordinary non-HTML comparison text. `<kbd>Enter</kbd>` elsewhere in the same otherwise navigable catalog is rejected by explicit all-catalog raw-HTML prohibition. These are false rejections in standard Markdown rendering; supporting arbitrary raw HTML is not a CP4 necessity.
- Local experiment with a **line-anchored registration grammar** (first table cell, standalone line, or list item) accepted current catalog-style links and rejected title/image-alt traps. It also rejected a team link embedded mid-sentence; this would be a documented compatibility decision, not an invisible fix.
- `python3 -m py_compile` passed for the local isolated helper scripts. **No byte-for-byte full local copy or entire checkout validation was executed.** Direct `git ls-remote` failed GitHub DNS; full `validate_seed.py`, repository unittest discovery and `git diff --check` across the complete PR are NOT RUN. GitHub returned no workflow runs/status checks at this pinned commit; this is not proof of failing CI. The implementer's reported 116 tests are not independently verified here.

## Recommendation

1. **Block integration on catalog false registration only.** Require an operative top-level team navigation declaration. Smallest candidate: a team link must start a catalog table cell, list item or standalone line; permit current title and optional `./` variants, and keep current image/comment/code exclusions. If a more permissive catalog authoring grammar is required, implement a narrowly scoped link lexer that understands nested link titles; do not add general Markdown semantic interpretation.
2. **Keep exact home URL parity.** Canonical URL equality guards against a displayed branch linking to an unrelated target; no remote fetch or URL-normalization framework is necessary. A plain backticked branch remains valid. Documented optional URL forms can remain excluded for v0.1.
3. **Treat global raw-HTML prohibition as P3 proportionality risk.** The `A<B` example is not HTML; whole-file `<kbd>` rejection can invalidate a visible real team link. Prefer narrowing the prohibition to operative registration context if feasible, or clearly document this intentional catalog-wide restriction and address false-positive comparisons. Do not hold the correctness fix hostage to generalized HTML support.
4. Add negative fixtures for title-only navigation and image-alt nesting, plus positive controls for actual Architects table registration and common link-title / `./` forms. If the grammar becomes line-anchored, explicitly test and document the mid-sentence link exclusion. No schema v0.2, new team memory, broad parser dependency, or CP5 work.

## Revisit when

After PR #6 receives a bounded corrective commit, rerun reproductions on the new exact SHA and require full checkout-level gates. Reassess Markdown compatibility only against a demonstrated consumer and clear authoring contract. This record is Flint's individual analysis, not a Studio team decision or fabricated independent-agent consensus.
