---
name: grade-composition
description: Rubric-based grading of a composition (essay) or thesis draft — verdict, first weak paragraph, root cause, next action, citation sanity check. Use when the user shares a draft, asks for feedback on an essay, or says "check my essay," "grade this," or "review my thesis draft."
---

# Grade a composition

Read `AGENTS.md`, `docs/agents/PROFILE.md`, and `docs/agents/tutoring.md`. Grade only submitted learner work. Verify cited passages before judging their support; mark unavailable sources unverified. Preserve draft history and record assistance separately from learner authorship. A rubric pass on a draft does not complete the source work or thesis defense.

## When to use

Trigger on requests like:

- "Here's my essay on natural law — check it."
- "Grade my draft."
- "Review the objection chapter of my thesis."
- "Is this essay ready to submit?"

For shorter compositions (the five / four / two essays of Years 1–3), a single pass suffices. For a thesis draft, run one pass per section plus one overall pass.

## Rubric

Five dimensions, scored on a 1–4 scale. A pass means a 3 or better on every dimension; a 2 anywhere is a revision request.

### 1. Thesis

- **4** — deniable, specific, sustained through every section.
- **3** — deniable and specific; one section drifts.
- **2** — not genuinely deniable, or too broad to be defended in the given length.
- **1** — a summary rather than a thesis.

### 2. Evidence

- **4** — every claim about a text cites a passage; passages are well-chosen; quotations are grammatically integrated.
- **3** — most claims cite; a few paraphrases are uncited.
- **2** — whole paragraphs of claims without citation, or long quotations without analysis.
- **1** — the essay leans on commentary instead of primary text.

### 3. Structure

- **4** — sections labeled; each ends with a sentence naming what it has established; objection is genuine and reply engages it.
- **3** — structure holds; one section ends without an earned conclusion, or the reply slightly dodges the objection.
- **2** — sections drift into each other; the objection is a strawman or the reply concedes the thesis.
- **1** — no discernible structure, or no objection at all.

### 4. Prose

- **4** — topic sentences underline-able; quotations integrated; plain voice; consistent citation style.
- **3** — mostly clean; a few misfit quotations or inconsistent citations.
- **2** — prose padding, rhetorical questions, hedging fillers, or citation drift.
- **1** — the reader cannot follow paragraph to paragraph.

### 5. Originality of question

Especially important for the Senior Thesis.

- **4** — a question the authors themselves frame, answered in a way that the student has earned through engagement with specific passages.
- **3** — a real question, answered conventionally; the answer is defensible but not striking.
- **2** — a question only an outsider would ask, or a conventional answer to a conventional question.
- **1** — an essay in search of a question.

## Output format

After reading the draft, produce exactly this structure:

```
## Verdict
Pass | Revision requested | Major revision requested

## Scores
- Thesis: N
- Evidence: N
- Structure: N
- Prose: N
- Originality: N

## First weak paragraph
[Paragraph number / section heading.]

## Root cause
[One paragraph on *why* that paragraph is weak — what it is trying to do and where it breaks. Cite a sentence from the draft.]

## Next action
[One paragraph on the single most useful revision. Be concrete: "rewrite paragraph 4 so it ends with the sentence that names what the section establishes," not "tighten the prose."]

## Citation sanity check
- [Either "citations consistent throughout" or the first 2–3 inconsistencies with fix.]
- [Note any paraphrase without citation; give the paragraph and the fix.]
- [Note any quotation that is not grammatically integrated.]

## Strengths
- [One to three genuine strengths. Do not invent.]
```

## How to read the draft

1. First pass: read end to end without marking. Form an overall impression. Write the verdict provisionally.
2. Second pass: score the five dimensions. Find the first paragraph that is doing less than its job; that is the "first weak paragraph."
3. Third pass: citation check. Every paraphrase cited? Every quotation integrated? Citation style consistent?
4. Only then write the output.

## Anti-patterns

- **Praise inflation.** If every dimension scores 4, either the draft is genuinely finished or you have not read hard enough. Re-read.
- **Omnibus rewrite.** The "Next action" is exactly one concrete revision. Not five. Not "restructure the whole thing."
- **Style policing.** Grammar matters, but a clean paragraph defending a weak thesis is worse than a rough paragraph defending a strong one. Diagnose substance first.
- **Summarizing the essay back.** The student wrote it; do not tell them what it says. Evaluate it.
- **Grading without citation.** If you flag a weakness, cite a sentence from the draft. Otherwise the student cannot act on the feedback.

## For thesis-scale drafts

- Run the rubric per section the first time through, then a final overall pass.
- In the overall pass, the "first weak paragraph" prompt becomes "first weak section" — same logic, larger unit.
- Cross-reference `thesis/outline.md` to check whether the draft still matches the approved outline. If the thesis has drifted from the outline, flag that explicitly in the root cause.

## Cross-reference

Writing standards: `docs/agents/writing-style.md`. Thesis-specific staged guidance: `.agents/skills/thesis-advisor/SKILL.md`. Core tutor tone: `docs/agents/tutoring.md`.
