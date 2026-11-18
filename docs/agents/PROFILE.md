# Great Books repository profile

The learner's goals are to read the Great Books in the Thomas Aquinas College curriculum, discuss them through close reading and objection/reply, and write increasingly substantial arguments culminating in a thesis. This is independent self-study; it confers no TAC credit, admission, degree, or actual committee approval.

## Sources and pacing

- `docs/CURRICULUM.md`: local curriculum blueprint. Its arrangement is the local plan; verify the current college syllabus before claiming an institutional sequence or requirement.
- `STUDY_PLAN.md`: proposed four/eight-year pacing and concurrent subject tracks. No personal weekly budget or start date has been confirmed here. Select one small session before assigning a weekly schedule; coordinate other studies only with the learner's actual availability.
- `PROGRESS.md`: work-level completion and current session pointer. Unchecked means completion is not evidenced, not that the learner necessarily knows nothing.
- `RESOURCES.md`: candidate editions and primary-source access. Distinguish a recommended edition from the edition actually in use. Use standard references across editions; note translation differences.
- `thesis/question-candidates.md`: learner-owned questions. Offer connections; add/refine a question only when the learner directs it. Do not invent a thesis choice.

The subjects run concurrently within a year. Session choice does not serialize the whole curriculum. An absent companion reading is not automatically a prerequisite: distinguish necessary concepts, useful context, and later connections. Begin foundational works without fabricating an entrance requirement. Latin develops in its own track; do not block English-language philosophy/theology on advanced Latin unless the task specifically requires parsing Latin.

## Modules and learner evidence

Reference module: `notes/year-1-freshman/4-mathematics-euclid/01-euclid-elements-book-1/`

This is an existing mixed teaching scaffold: its notes, prompts, and solution file do not establish who has studied or produced them. Read README/notes/problems when teaching; keep solutions closed during first attempts and unaided tests. Read the solution key when authoring or checking submitted work.

Record actual attempts and tutor feedback in the module's `learner-work.md`; append the learner's own dated 2–4 sentence reflections to `reflection.md`. Log the passage/task, verbatim attempt when practical, assistance, feedback, next action, and any review date agreed with the learner. Keep tutor-authored session notes out of the reflection field. Store proposed but unattempted prompts as preparation with status explicit.

The existing Euclid Book I gate is a 60-minute unaided assessment; preserve it. Smaller sessions have smaller objectives and do not pass the whole book. Other modules must define an exit task and rubric before testing; humanities recall can be closed-book, followed by a distinct passage-verification stage with the text open. Record the conditions of both stages. Do not pretend to observe a timer or closed-book conditions.

First-session default, absent a learner preference or previous evidence: Euclid Book I foundations, using the existing module. Read definitions I.1–I.4, Postulate I.1, and Common Notion I.1; distinguish their roles before attempting I.1. This is a starting suggestion, not evidence of an attempt or an agreed recurring schedule.

## Computation

Follow `pyproject.toml` and `uv.lock`. Reuse actual APIs in `great/common/`; inspect their definitions rather than guessing helper names. Diagrams and numerical checks support paper demonstrations. Documentation/config changes need configuration and link checks; numerical changes need checks relevant to the affected helper.
