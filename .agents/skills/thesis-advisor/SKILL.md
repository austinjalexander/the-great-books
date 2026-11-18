---
name: thesis-advisor
description: Four-year staged guidance for the Senior Thesis — accumulating candidate questions Freshman year, refining to three Sophomore year, choosing one and outlining Junior year, drafting and defending Senior year. Use when the user mentions "thesis," "senior thesis," "thesis candidates," "my question," or asks to "refine" or "defend" a thesis question.
---

# Senior Thesis advisor

## When to use

Trigger on requests like:

- "Add a thesis candidate."
- "Refine my thesis questions."
- "Help me pick a thesis topic."
- "I'm ready to outline the thesis."
- "Draft the objection chapter."
- "Run a mock defense."

Unlike the other skills, this one is **always alive**: after any `discussion-session`, the tutor asks whether the reading connects to the thesis thread.

## Before you begin

Read `AGENTS.md`, `docs/agents/PROFILE.md`, and `docs/agents/tutoring.md`.

1. Read `thesis/question-candidates.md` to see the current list.
2. Read `thesis/outline.md` if it exists.
3. Read `thesis/drafts/` to see any writing so far.
4. Check `PROGRESS.md` to see what year the student is in (the "uppermost completed year" is a good proxy).

## Staged guidance

### Stage 1 — Freshman: accumulate

**Goal**: at least 20 candidate questions by the end of Freshman year.

- Every candidate is logged in `thesis/question-candidates.md` as:
  - A question in one sentence.
  - The work(s) from which it arose, with passage citations.
  - A one-sentence rationale for why the question is interesting.
- Questions here are **cheap**. Volume is the goal. Do not trim yet.
- At the end of Freshman year (or ~3/4 of the way through the reading list), review the list together and mark obvious duplicates — but do not delete anything yet.

Prompts the advisor uses:

- "That passage in *Republic* IV — could it support a thesis question? Try it in one sentence."
- "You've raised an objection to Aristotle's *Posterior Analytics* I.2 that you couldn't resolve. That's a candidate. Log it."

### Stage 2 — Sophomore: refine to three

**Goal**: by the end of Sophomore year, three strongest candidate questions, each with a one-paragraph rationale.

- For each of the ~20+ candidates, ask:
  - "Is this a question the authors themselves frame?" If no, cut or rephrase.
  - "Could a serious essay answer this in 40–80 pages?" If obviously yes or obviously no, cut.
  - "Does this question draw on at least three works in the program?" If yes, elevate.
- Merge overlapping candidates into single stronger questions.
- By Sophomore end, `thesis/question-candidates.md` has a "Top three" section with three questions, each with a one-paragraph rationale citing specific works.

### Stage 3 — Junior: pick one; outline

**Goal**: by the end of Junior year, a single chosen question and a one-page outline.

- Choose the question that (1) the student can still not resolve, (2) survives objections, and (3) has the most concrete passage-level material to work with.
- Copy the chosen question into `thesis/outline.md` using `templates/thesis-outline-template.md`.
- Draft the Roman-numeral outline: thesis, sections I–II (argument), section III (objection), section IV (reply), section V (conclusion).
- Compile `thesis/bibliography.md` with primary sources first, secondary second. All entries follow the chosen citation style (Chicago notes-bibliography or MLA).
- Discuss open problems explicitly. A thesis with no acknowledged unresolved problems is either trivial or self-deceived.

### Stage 4 — Senior: draft, revise, defend

**Goal**: a defended thesis.

- **Senior fall**: draft by outline section. The advisor reads drafts with the `grade-composition` skill's rubric but at thesis scale: one pass per section, one overall pass per draft.
- **Senior spring**: revise. Every revision is a full pass; nothing is "just fixing a paragraph."
- **Defense prep**: fill `thesis/defense-prep.md` with the ten questions the advisor most expects the committee to ask. For each, write a short answer tied to a specific passage in the thesis.
- **Mock defense**: the advisor runs a 30–45 minute mock defense, asking follow-up questions that force the student to cite their own thesis.

## Anti-patterns

- **Picking the thesis early.** A Freshman who says "I want to write on X" has not read enough to know. Log the candidate; do not freeze.
- **Scope inflation.** "The nature of being" is not a thesis. "Whether Aquinas's account of the analogy of being in *On Being and Essence* can survive the objection from Scotus" is closer.
- **Commentary-first thesis.** A thesis that begins "Gilson argues that…" is a thesis on Gilson, not on the primary author. If the question only makes sense through a commentator's lens, that is the wrong question.
- **Strawman objection.** If the objection in Section III is not one a careful TAC reader would raise, it is the wrong objection. Revise until it is the strongest case against.
- **No-reply reply.** A reply that concedes what the thesis claims has not replied; it has retreated. If the objection wins, revise the thesis.
- **Defense memorization.** The student should not memorize answers; they should know the thesis well enough to answer any question from it on the spot.

## Document discipline

- `thesis/question-candidates.md` — append-only through Sophomore year. Later edits only to merge or elevate, never to delete reasoning.
- `thesis/outline.md` — revised iteratively; version each major revision with a date header at the top.
- `thesis/drafts/` — one file per major draft: `draft-1.md`, `draft-2.md`, `draft-final.md`. Never overwrite an earlier draft; the history is pedagogically valuable.
- `thesis/defense-prep.md` — the ten questions + answers + citations; the night-before document.

## Cross-reference

Writing standards for the draft: `docs/agents/writing-style.md`. Grading rubric for draft passes: `.agents/skills/grade-composition/SKILL.md`. Underlying tutor tone: `docs/agents/tutoring.md`.

## Evidence and learner choices

Read `AGENTS.md`, `docs/agents/PROFILE.md`, and `docs/agents/tutoring.md` before advising. Treat year-based milestones as proposals within the learner’s actual pace. Log or refine thesis candidates only at the learner’s direction. Generated outlines, defense questions, and model answers are preparation; a performed defense requires an actual learner attempt and feedback. Preserve learner-authored drafts and never invent committee approval.
