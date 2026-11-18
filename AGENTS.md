# Great Books learning repository

These instructions apply to assistants working in this repository. Use ordinary maintenance workflows for repository changes and the learning workflows below when teaching.

## Start here

1. Read [the repository profile](docs/agents/PROFILE.md) for goals, sources, pacing, and the reference module.
2. Before teaching, read `PROGRESS.md`, the target module's `README.md`, and its latest learner work and reflection. Consult `docs/CURRICULUM.md`, `STUDY_PLAN.md`, and `RESOURCES.md` for scope, sequence, and editions.
3. Read [tutoring guidance](docs/agents/tutoring.md) for sessions, feedback, and completion; [module structure](docs/agents/module-structure.md) when authoring; [writing standards](docs/agents/writing-style.md) for essays/theses; and [math/code style](docs/agents/math-and-code-style.md) for demonstrations or computation.
4. Use the relevant workflow in `.agents/skills/`: `discussion-session`, `diagnose-prereqs`, `grade-solution`, `grade-composition`, `author-module`, or `thesis-advisor`. See [agent setup](docs/agents/README.md) for tool entry points and handoffs.

## Evidence and scope

- Scaffolds, tutor notes, worked solutions, and inspected sources are preparation, not learner achievement. Never invent reading, attempts, elapsed time, scores, reflections, or discussion answers.
- Check a work complete only with its required learner work, a passed stated unaided exit task, and a dated learner-authored reflection. Record evidence paths, timing, assistance, and gaps; partial sessions leave the work unchecked.
- Keep learner attempts and separate answer keys apart. Offer one hint at a time; honor explicit requests for explanations or worked answers and label that practice assisted. Give no coaching during an unaided assessment.
- Cite claims about primary texts by their standard reference. Distinguish the text, the translator/editor, and our interpretation. Verify unfamiliar passages and current external requirements before relying on them.
- Preserve existing learner work and thesis choices. A weak recall check schedules repair; it does not erase earlier valid completion evidence.
- Respect the agreed time budget. The four/eight-year tracks are estimates, not a chosen workload or a credential. Do not import the physics project's career plans or hours.
- Make focused changes and run relevant checks. Do not change global settings or other repositories as part of local maintenance.

## Configuration ownership

Canonical guidance lives here, in `docs/agents/`, and in `.agents/skills/`. Cursor rules are thin adapters; Claude skill folders are relative links to the same skills. This repository has no runtime dependency on the physics repository. Run `python3 tools/agent_config.py check` after configuration changes.
