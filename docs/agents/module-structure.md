# Module structure

Every work-module matches the pattern set by `notes/year-1-freshman/4-mathematics-euclid/01-euclid-elements-book-1/`. Treat that folder as the reference implementation — the Great Books analogue of the physics repo's `01-algebra`.

## Required files per work-module

- `README.md` — one-paragraph framing; the local curriculum citation (label any externally verified quotation); edition used; companion readings (backward and forward); objective checkboxes; exit criteria; time estimate. Use `templates/work-readme-template.md`.
- `notes.md` — structure of the work, passage-cited summary, key terms, puzzles, connections, first-read summary. Use `templates/reading-notes-template.md`.
- `discussion.md` — at least five pre-read questions (at least one an objection), each with type, where-in-the-text, and what-would-count-as-an-answer; post-read answers with passage support; cross-curriculum connections; thesis-thread line. Use `templates/discussion-template.md`.
- `reflection.md` — dated 2–4 sentence entry plus thesis-thread line. Appended, not overwritten, on re-reads.

## Mathematics and Natural-Science modules additionally have

- `problems.md` — propositions, constructions, or calculations to demonstrate, cited to the primary text (Euclid I.47, *Almagest* V.3, *Principia* I.II.6). Use `templates/math-demonstration-template.md`.
- `solutions.md` — every demonstration fully worked. Each solution ends with an explicit **"Check."** step (limiting case, special case, sanity of magnitudes or units). Mirrors the physics repo discipline.
- `notebooks/` — only where computation or plotting genuinely helps (Ptolemy epicycles, Kepler's area law, Apollonius conics, Archimedes quadrature, Boethius tone ratios, Lobachevski models, Einstein's numerical examples).

## Latin modules additionally have

- `exercises.md` — morphology drills, parsing, Latin-to-English and English-to-Latin translation, with a separate answer key in `solutions.md`. Use `templates/latin-exercise-template.md`.

## Subject folder (one level up from modules) also has

- `README.md` — subject overview, reading order, prereqs from earlier years, cross-track connections, and links to each module folder.

## Writing style

- Concise. One idea per paragraph. No throat-clearing, no summaries of summaries.
- **Every claim about a text has a citation** in the work's standard reference system — Bekker column for Aristotle; Stephanus page for Plato; book-chapter-verse for Scripture; part-question-article for the *Summa*; book-proposition for Euclid and Apollonius; line number for poetry and drama; page number in the cited edition only as a last resort.
- Derive every mathematical or logical result. Never assert a demonstration without giving it or pointing to where it is given.
- Quote sparingly and always grammatically integrated into your sentence.
- At least one "puzzles and questions raised while reading" note per `notes.md`.
- Every `discussion.md` ends with a thesis-thread line, either confirming no connection or naming the candidate question added to `thesis/question-candidates.md`.

## Objective bullets

Use verbs that name a concrete, testable skill.

Good:

- [ ] Reconstruct the three-part argument for the immortality of the soul in *Phaedo* 78b–84b.
- [ ] Demonstrate Euclid *Elements* I.47 from the definitions and postulates of Book I, on paper.
- [ ] Parse and translate the opening paragraph of *Summa Theologiae* I.1.1, identifying every declension and conjugation.
- [ ] State the strongest objection to Aristotle's account of natural slavery in *Politics* I and reply to it from within Aristotle's own framework.

Bad:

- [ ] Understand the *Phaedo*.
- [ ] Read Euclid Book I.
- [ ] Be familiar with Aristotle's *Politics*.

## Cross-references

- In `notes.md`, add a "Connections" section linking backward and (tentatively) forward, using full relative paths to other module folders.
- In the subject `README.md`, link backward under "Companion readings" with paths to earlier-year or earlier-subject modules.
- A work that is read in more than one year (Aristotle *Physics* in Sophomore Philosophy and Senior Philosophy; Newton *Principia* in Junior and Senior Natural Science; Kant *Critique of Pure Reason* in Junior and Senior Seminar; Mendel *Plant Hybridization* in Freshman and Senior Natural Science) gets one module per occurrence, and each module cross-links to the other.

## Evidence and assessments

Tutor-authored scaffolds are preparation. Preserve learner notes and answers; label teaching notes explicitly when authorship is uncertain. Add `learner-work.md` for actual attempts, feedback, assistance, timing, and next tasks. Keep `reflection.md` for the learner’s own dated reflections.

Each README defines the exit task, time limit, aids, and pass rubric before assessment. Preserve the existing Euclid Book I 60-minute gate. Keep prompt files free of worked answers and link a separate key. Authoring a key does not count as learner demonstration. Apply the completion gate in [tutoring.md](tutoring.md).
