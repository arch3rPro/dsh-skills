# CLAUDE.md — dsh-skills

A set of coding-agent skills distilled from the engineering conventions of **DeepSeek Harness**. The project is **dsh-skills** (DeepSeek-Harness-Skills); the full name appears only in the README.

## Repository layout

```
skills/<category>/<name>/SKILL.md    the executable standard (any harness)
skills/<category>/<name>/agents/openai.yaml   Codex metadata + invocation policy
docs/<category>/<name>.md           human-facing docs page per skill
reference/                          read-only upstream clones — gitignored, never edited
.claude-plugin/plugin.json          Claude Code plugin manifest
.claude-plugin/marketplace.json     Claude Code marketplace (npx skills / plugin install)
scripts/link-skills.sh              symlink every skill into ~/.claude/skills and ~/.agents/skills
scripts/validate-skills.py          strict-validate every SKILL.md + openai.yaml (run before push)
.github/workflows/validate.yml      CI gate: runs the validator on every push/PR
```

Categories: `architecture/`, `testing/`, `documentation/`, `process/`.

## Standing orders

- Every skill is one `<category>/<name>` directory carrying `SKILL.md`, `agents/openai.yaml`, and a matching `docs/<category>/<name>.md` page. Add all three in one change.
- **Design from adaptability, not from the conversation.** Ground each skill's scope and rationale in *project adaptability* (when does the standard apply to a project — and when does it not?) and *agent adaptability* (when and how does the agent reach for it, and by what invocation).
- **Never transcribe conversation feedback into rules.** User feedback, this session's discussion, and reviewer commentary about a skill are *input about how to design* the skill — they are never themselves rules, standards, or phrases to paste into `SKILL.md`, `openai.yaml`, or docs pages. State the resulting engineering principle on its own merits, sourced from project and agent adaptability, with no echo of who said it or when.
- **Generalize.** Keep only conventions that transfer across projects; drop dsh-specific machinery (its plugin host, bilingual pairing, CI gates, vendoring). Frame an opinionated architecture choice as a *conditional* decision — state when it applies — never as a universal mandate.
- **Write for the agent.** Call the Skill tool with "writing-for-agents" (and its `SKILL-MECHANICS.md`) when authoring: leading words, steps with completion criteria, positive phrasing, single source of truth, no no-ops.
- **Invocation choice.** Default to *model-invoked* (agent reaches for it autonomously): omit `disable-model-invocation`, and keep `interface` only in `agents/openai.yaml`. A *user-invoked* skill sets `disable-model-invocation: true` and `policy.allow_implicit_invocation: false`. Keep the two files in sync — a skill is invoked the same way in every harness.
- **Keep one home per fact.** State a rule in exactly one skill; link elsewhere with a relative path. Use relative links inside `docs/`.
- **Reference repos are read-only.** Never edit or commit `reference/`; it exists only as extraction source material.
- Update `README.md` (index + status table) and `.claude-plugin/plugin.json` whenever a skill is added, renamed, or removed.

## Editing these instructions

`AGENTS.md` symlinks `CLAUDE.md`; edit the real file. Keep each rule self-contained; condense when clarity survives.
