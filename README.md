# the-great-books

A self-study repository that reproduces the **Thomas Aquinas College** Great Books curriculum — four years of theology, philosophy, natural science, mathematics, language (Latin), music, and seminar, taught by primary sources and Socratic discussion rather than textbooks and lectures. The authoritative blueprint is [`docs/CURRICULUM.md`](docs/CURRICULUM.md).

## Goals

1. Read the Great Books cover-to-cover, in the order and grouping TAC uses, so that each work illuminates the next.
2. Learn to discuss — examine a text, pose a question, hear an objection, reply with evidence from the page.
3. Write — five essays Freshman year, four Sophomore, two longer Junior, a Senior Thesis defended before a committee.

A **thesis-thread** runs through all four years: candidate questions are logged from the first seminar; one is refined and answered in the Senior Thesis.

## Repository layout

```
the-great-books/
  docs/CURRICULUM.md                # source-of-truth blueprint (TAC syllabus, year × subject)
  STUDY_PLAN.md                     # year-by-year pacing (TAC 4-yr and comfortable 8-yr tracks)
  PROGRESS.md                       # one checkbox per work / book
  RESOURCES.md                      # editions, translations, online texts, commentaries, Latin resources
  templates/                        # module / composition / thesis / Latin / math-demonstration templates
  great/common/                     # lightweight Python helpers for math / astronomy / music modules
  AGENTS.md                         # shared tutor instructions and evidence policy
  docs/agents/                      # learning profile and canonical rules
  .agents/skills/                   # canonical learning workflows
  .cursor/                          # thin contextual rule adapters
  tools/agent_config.py             # configuration checks and study handoff export
  notes/
    year-1-freshman/
    year-2-sophomore/
    year-3-junior/
    year-4-senior/
  compositions/
    year-1/   # five essays
    year-2/   # four essays
    year-3/   # two longer essays
  thesis/                           # Senior Thesis — question-candidates, notes, bibliography, drafts, defense
```

Each subject folder holds numbered work-modules (one module per primary text or tightly linked cluster):

```
<subject>/
  README.md                         # overview, reading order, prereqs across subjects
  01-<work-or-cluster>/
    README.md                       # framing, TAC syllabus citation, edition, objectives, exit criteria
    notes.md                        # reading notes: structure, passages, puzzles, vocabulary
    discussion.md                   # Socratic questions with passage citations
    reflection.md                   # learner-authored reflection + thesis-thread hook
    learner-work.md                 # attempts, assistance, feedback, next task
    # mathematics + natural-science additionally:
    problems.md
    solutions.md
    notebooks/
    # Latin additionally:
    exercises.md                    # prompts; keep answer keys separate
  02-<work-or-cluster>/
  ...
```

## Getting set up

Most of the repo is plain markdown — open it in any editor and start reading. For the handful of Mathematics / Natural Science / Music modules that benefit from computation (Ptolemy, Kepler, Apollonius, Archimedes, Boethius on tone ratios, Lobachevski, Einstein), there is a small Python toolchain.

Prerequisites: [`uv`](https://github.com/astral-sh/uv) and Python 3.12 (`uv` will install it if missing).

```bash
uv sync                     # install dependencies into .venv
uv run jupyter lab          # launch JupyterLab for the math/astronomy/music notebooks
```

You do not need Python to read, take notes on, discuss, or write about any seminar, theology, philosophy, or language work.

## Study workflow

1. Pick the next unchecked work in [`PROGRESS.md`](PROGRESS.md) for the subject track you are working on this week.
2. Skim the matching section of [`docs/CURRICULUM.md`](docs/CURRICULUM.md) and the subject `README.md` under `notes/year-.../<subject>/` for reading order and companion readings.
3. Read the primary edition from [`RESOURCES.md`](RESOURCES.md) once to follow the argument; read it again pen-in-hand for passages.
4. Copy `templates/reading-notes-template.md` → `notes/year-.../<subject>/NN-<work>/notes.md` and write structure, passages, puzzles, vocabulary.
5. Copy `templates/discussion-template.md` → `discussion.md` and draft at least five substantive questions, at least one of which is an objection to the author's position. Then cite passages from the text that answer or complicate each one.
6. For mathematics or natural-science works, copy `templates/math-demonstration-template.md` → `problems.md` and demonstrate the propositions on paper (or in a notebook when geometry/calculation benefits from it).
7. Copy `templates/reflection-template.md` → `reflection.md` and write 2–4 sentences on what changed in your understanding, plus a "thesis-thread" line if this reading suggested or refined a candidate question in [`thesis/question-candidates.md`](thesis/question-candidates.md).
8. Complete the module’s stated unaided exit task under its timing, aid, and rubric conditions. Record your actual attempts, corrections, assistance, and timing in `learner-work.md`. Check [`PROGRESS.md`](PROGRESS.md) only when the [completion gate](docs/agents/tutoring.md#completion-gate) is evidenced. Tutor-written notes and keys are preparation.

## Years at a glance

| Year | Focus | Subjects |
|------|-------|----------|
| 1 Freshman | Greek origins: poetry, philosophy, mathematics, life-sciences | Bible, Plato+*Organon*, Life Sciences, Euclid, Latin I, Greek Seminar |
| 2 Sophomore | Fathers, Aristotle's natural philosophy, chemistry, astronomy, Roman and medieval seminar | Augustine+Anselm, *Physics*+*De Anima*, Chemistry, Astronomy (Ptolemy–Kepler), Latin II, Roman-to-Dante Seminar |
| 3 Junior | Summa I, *Ethics* and *Politics*, new science, analytic geometry, music, early-modern seminar | Summa I, *NE*+*Politics*, Descartes–Galileo–Newton, Viète–Descartes–Archimedes, Music, Early-Modern Seminar |
| 4 Senior | Summa II, metaphysics, light+life, foundations of mathematics, modernity, Senior Thesis | Summa II, *Metaphysics*+*On Being and Essence*, Light+EM+Life, Dedekind–Lobachevski–Einstein, Modern Seminar, Senior Thesis |

See [`STUDY_PLAN.md`](STUDY_PLAN.md) for hour estimates and the week-by-week pacing.

## Tutor configuration

[AGENTS.md](AGENTS.md) and [the learning profile](docs/agents/PROFILE.md) provide a shared entry point. [Tutoring guidance](docs/agents/tutoring.md) defines interactive teaching, staged hints, evidence, and completion. [Agent setup](docs/agents/README.md) explains Cursor adapters, Claude links, and study handoffs.

Canonical workflows live in [`.agents/skills/`](.agents/skills/):

- `discussion-session`: close reading, demonstration, or parsing, one question at a time.
- `diagnose-prereqs`: route specific prerequisite gaps without claiming module completion.
- `grade-solution`: inspect a proof, interpretation, parsing, or other short attempt.
- `grade-composition`: review an essay or thesis draft against the existing rubric.
- `author-module`: prepare prompts and separate keys with a concrete exit task.
- `thesis-advisor`: develop learner-owned questions through the four-year thesis thread.

Run `python3 tools/agent_config.py check` after configuration changes. To begin, ask “Continue from the current session in PROGRESS.md.” No weekly study budget has been selected yet; the first session uses a small part of the existing Euclid Book I module.

## Source

All reading lists and titles are drawn from the publicly posted [Thomas Aquinas College syllabus](https://www.thomasaquinas.edu/a-liberating-education/syllabus).

## License

MIT for the scaffolding, notes, templates, and tooling. All primary texts referenced here belong to their authors / translators / publishers; this repo does not redistribute them.
