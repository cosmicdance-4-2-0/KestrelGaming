---
name: kestrel-technical-writing-ste100
description: Write or revise technical documentation with ASD-STE100 (Simplified Technical English)-informed rules — short direct sentences, one meaning per term, procedural versus descriptive style — while preserving identifiers, commands, units and notation. Use when drafting or editing procedures, READMEs, specifications or other technical prose, or when a documentation review asks for clearer wording. Does not certify ASD-STE100 compliance and does not rewrite approved copy, quotations or historical records.
---

# STE-informed technical writing

**Reference:** ASD-STE100 Simplified Technical English, **Issue 9 (January 2025)**, from the
[official ASD-STE100 site](https://www.asd-ste100.org/). Issue 9 was the current issue when this skill was written.
Check the official site for a newer issue before you rely on that. This skill states writing practices
in its own words. It does **not** contain the STE dictionary or the text of the standard. Do not copy the
official dictionary into a repository without authorization.

**Claim limit:** Text written with this skill is *STE-informed*. Do not claim ASD-STE100 compliance on the basis of
generated text, this skill or an automated check. A compliance claim needs review against the official
standard and its dictionary by a qualified person.

## When to apply

- **Apply** to new technical prose: procedures, setup and usage instructions, specifications, technical
  descriptions, release notes and log entries.
- **Do not rewrite automatically:** owner-approved marketing or editorial copy, quotations, historical
  evidence, immutable records, legal text, or text that another document says is exact. Suggest changes for
  review instead.

## Rules

### Decide the type of text first

- **Procedural** text tells the reader what to do. Write instructions in the imperative ("Open the file.").
  Put one instruction in each sentence, unless the reader must do two actions at the same time.
  Put a condition before the instruction ("If the build fails, read the log.").
  Use numbered steps for a sequence. Target **20 words or fewer** for each sentence.
- **Descriptive** text tells the reader how something is or works. Target **25 words or fewer** for each
  sentence. Put one topic in each paragraph, with about six sentences or fewer.

### Words and terms

- Use one word for one meaning, and one meaning for each word. Do not use synonyms for variety.
- Use the simplest common word that is correct. Prefer "use" to "utilize" and "start" to "initiate".
- Keep **technical nouns and technical verbs** that the domain needs: API names, product names, commands,
  file names, protocol terms and mathematical terms. A technical term is not a style problem.
- Write each controlled term exactly the same way every time, with the same capitalization.
- When a project needs its own vocabulary, keep it in `docs/TERMINOLOGY.md`. Start from the
  [terminology template](assets/TERMINOLOGY.md). Each term has one meaning and lists the words to avoid.

### Sentences and grammar

- Prefer the active voice. In procedures, use only the active voice.
- Prefer simple verb forms: the imperative, the simple present, past and future. Avoid an "-ing" form unless it
  is part of a technical name.
- Do not remove articles ("the", "a") or verbs to make a sentence shorter. Telegraphic text is ambiguous.
- Use a vertical list for a set of conditions, parts or options.
- In a warning or caution, start with the instruction, then give the risk.

## Preserve technical meaning

Never change these items during a style edit: identifiers, API and function names, commands and their flags,
file paths, URLs, configuration keys, error messages, units, numbers, version strings and mathematical notation.
If a plain-language edit could change a requirement, a guarantee or a qualification (for example "must" to
"should", or "all" to "most"), **flag it for review instead of making it**.

## Check your edit

[`scripts/ste_check.py`](scripts/ste_check.py) (Python 3.9+, standard library only) gives review aids:

```sh
python3 <this-skill>/scripts/ste_check.py protect before.md after.md   # exit 1 if a protected token changed
python3 <this-skill>/scripts/ste_check.py lint after.md --terms docs/TERMINOLOGY.md
```

- `protect` compares inline code, URLs, flags, dotted names, camelCase and snake_case identifiers, paths,
  numbers and units between two versions. A change means that you must review the edit before you accept it.
- `lint` reports sentence length against the targets above, long paragraphs, "-ing" forms, possible passive
  voice and project terms marked "avoid". Each finding is a hint for a person to decide. It does not use the
  STE dictionary.

Report what you changed, what you flagged for review and what you did not check.
