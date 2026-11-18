# Agent setup and maintenance

Shared instructions live in [AGENTS.md](../../AGENTS.md), [PROFILE.md](PROFILE.md), and the topical guides here. Canonical workflows live in [`.agents/skills/`](../../.agents/skills/). Cursor rules point to these guides; `CLAUDE.md` imports `AGENTS.md` and `.claude/skills/` links to the canonical skill folders. No guidance loads from another learning repository.

Open this repository root in your assistant and ask it to read `AGENTS.md`, the profile, current progress, and the target module. This local layout follows the physics project's portable configuration and [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills). Reload project configuration or start a fresh session if new skills are not visible. File validation confirms structure, not what a running client has loaded.

Available workflows: `discussion-session`, `diagnose-prereqs`, `grade-solution`, `grade-composition`, `author-module`, and `thesis-advisor`. Ask naturally, for example: “Continue Euclid Book I from the latest learner log.”

Run `python3 tools/agent_config.py check` after editing configuration. It checks canonical skills, adapters, relative Claude links, required documents, and local Markdown links in the agent configuration. Each repository owns its files; adapt shared improvements deliberately rather than requiring byte-for-byte equality across curricula.

For ChatGPT without repository access, follow [CHATGPT-START.md](CHATGPT-START.md). Export a fresh packet with:

```sh
python3 tools/agent_config.py export --skill discussion-session --module notes/year-1-freshman/4-mathematics-euclid/01-euclid-elements-book-1 > /tmp/great-books-study.md
```

The export includes current guidance, progress, and selected module context. Separate answer keys are excluded. Inspect the packet before sharing it; linked primary texts still need to be supplied or opened separately.
