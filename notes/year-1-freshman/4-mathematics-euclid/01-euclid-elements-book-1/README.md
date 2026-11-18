# 01 — Euclid, *Elements*, Book I

> The foundation of geometry — and the paradigm of demonstrative science itself. Book I proceeds from 23 definitions, 5 postulates, and 5 common notions to 48 propositions culminating in the Pythagorean theorem (I.47) and its converse (I.48). No other work in the TAC curriculum is cited more often by later authors; no other book teaches the *form* of rigorous argument so cleanly.

## TAC syllabus citation

From the [TAC syllabus](https://www.thomasaquinas.edu/a-liberating-education/syllabus):

> Freshman | Mathematics | Euclid — *Elements*

This local plan begins with Book I; `docs/CURRICULUM.md` assigns Books I–VI and selected later propositions.

## Edition

- **Primary**: Heath, Sir Thomas L., trans. *The Thirteen Books of Euclid's Elements*, 2nd ed., 3 vols. (Dover, 1956). Volume I contains Books I–II with Heath's extensive commentary. Reference passages by proposition number (I.1, I.47, etc.), not by Heath's page numbers.
- **Alternative**: Euclid. *Elements*. Green Lion Press one-volume edition. Leaner, TAC-favored, no commentary — good for a second pass.
- **Free online**: [D.E. Joyce's HTML edition](https://mathcs.clarku.edu/~djoyce/java/elements/) with interactive diagrams.

See [`RESOURCES.md`](../../../../RESOURCES.md#euclid-and-the-green-lion-press) for full alternatives.

## Companion readings

**Backward** — before this module:

- None required within this curriculum. Book I is the starting point.
- Helpful: ordinary high-school algebra, fluency with compass-and-straightedge constructions (a ruler and compass are non-optional physical props for this module).

**Forward** — this module is a direct prerequisite for:

- `02-euclid-elements-book-2/` and all subsequent Euclid books.
- `2-philosophy-presocratics-physics-de-anima/` — Aristotle's *Posterior Analytics* reads Euclid's style as the model of demonstrative science.
- `4-mathematics-astronomy/` (Sophomore) — Ptolemy and Apollonius presuppose Book I and Book III throughout.
- `4-mathematics-analytic/` (Junior) — Descartes's *Geometry* reformulates, and sometimes replaces, Euclidean method.
- `3-natural-science-galileo-newton/` (Junior) — Galileo and Newton both write in Euclidean style.
- `4-mathematics-number-geometry-relativity/` (Senior) — Lobachevski's *Geometrical Researches* begins by questioning Euclid's fifth postulate.

## Objectives

By the end of this module you should be able to, without references:

- [ ] State all 23 definitions, 5 postulates, and 5 common notions of Book I from memory (or reconstruct them from the definitions you do remember).
- [ ] Distinguish definition, postulate, and common notion, and explain why Euclid keeps them separate.
- [ ] Demonstrate I.1 (equilateral triangle on a given base) and I.4 (SAS congruence) on paper.
- [ ] Demonstrate I.5 (the *pons asinorum*: base angles of an isosceles triangle are equal) on paper.
- [ ] Demonstrate I.16 (exterior angle theorem) and explain why its proof fails in spherical geometry — previewing Lobachevski Senior year.
- [ ] Demonstrate I.47 (Pythagorean theorem) on paper, diagram first, with every citation traceable back to Book I.
- [ ] Demonstrate I.48 (the converse of I.47) on paper.
- [ ] State the fifth postulate and explain what makes it different in character from the other four — a question Lobachevski will revisit.
- [ ] Identify which of the 48 propositions use Postulate 5 and which do not (the "neutral geometry" subset).

## Files in this module

- [`notes.md`](notes.md) — the structure of Book I, passage-cited summaries of the 23 definitions / 5 postulates / 5 common notions, the major dependency graph of propositions, key terms, and puzzles raised while reading.
- [`discussion.md`](discussion.md) — Socratic questions, with a strong objection to Euclid's fifth postulate and a reasoned reply.
- [`learner-work.md`](learner-work.md) — actual attempts, assistance, feedback, and next tasks.
- [`reflection.md`](reflection.md) — dated reflection entries with thesis-thread line.
- [`problems.md`](problems.md) — a graded list of propositions to demonstrate on paper, from I.1 through I.48.
- [`solutions.md`](solutions.md) — worked demonstrations with explicit **"Check."** steps.
- [`notebooks/`](notebooks/) — optional Python support: `01-construct-equilateral-triangle.ipynb` (uses `great.common.euclid`) and `02-neutral-vs-full-geometry.ipynb`.

## Exit criteria

The full work-level completion gate also requires learner notes, discussion, corrected demonstrations, and a dated learner-authored reflection; see [tutoring guidance](../../../../docs/agents/tutoring.md). Existing teaching notes and `solutions.md` are preparation.

Pass the following exit test without references or tutor assistance in 60 minutes. Record actual start/finish time and any aids. Pass requires all four tasks correct, justified steps and dependencies, and correct labeled diagrams; unsupported critical steps require correction and an equivalent retest:

1. State the five postulates from memory.
2. Demonstrate Proposition I.1 with a correct diagram.
3. Demonstrate Proposition I.5 (*pons asinorum*).
4. Demonstrate Proposition I.47 (Pythagorean theorem), naming every earlier proposition each step invokes.

## Estimated time

- ~20 hours first read of Book I with Heath.
- ~25 hours second read, pen-in-hand, constructing every proposition on paper.
- ~10 hours drafting `notes.md`, `discussion.md`, `reflection.md`, `problems.md`, and `solutions.md`.
- ~5 hours optional notebook work.

Total: ~60 hours. This is the single heaviest Freshman Mathematics module; budget accordingly. Subsequent books go faster because the method is now familiar.
