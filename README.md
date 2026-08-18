<div align="center">

# DeepSeek-Harness-Skills

</div>

<p align="center">
  A set of coding-agent skills distilled from the engineering conventions of **DeepSeek Harness** — executable standards your coding agent applies while coding, reviewing, testing, or documenting.
</p>

<p align="center">
  <b>English</b> · <a href="./README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="dsh-skills — coding-agent skills distilled from DeepSeek Harness, organized across architecture, testing, documentation, and process">
</p>

## Get started

The fastest way to use these standards is to install them so your agent reaches for them automatically:

```bash
scripts/link-skills.sh   # symlinks every skill into ~/.claude/skills and ~/.agents/skills
```

Or just read one — each `SKILL.md` is a self-contained executable standard. Pick the discipline that matches what you're doing: [code-conventions](docs/architecture/code-conventions.md), [testing-tiers](docs/testing/testing-tiers.md), [prose-standard](docs/documentation/prose-standard.md), or any in [the set](#the-set).

## The set

Ten skills across four categories. Every one is **model-invoked** — the agent reaches for it automatically when a trigger fires.

| Skill | Category | What it does |
| --- | --- | --- |
| [defensive-patterns](docs/architecture/defensive-patterns.md) | architecture | bug-class rules for lifecycle, concurrency, teardown, untrusted I/O |
| [code-conventions](docs/architecture/code-conventions.md) | architecture | reversible side effects, explicit-over-implicit, config-over-hardcoding, branded ids |
| [extension-points-and-seams](docs/architecture/extension-points-and-seams.md) | architecture | build a seam only when a capability has multiple implementations or consumers |
| [testing-tiers](docs/testing/testing-tiers.md) | testing | pick the right tier, test the real entry path, verify the world not the self-report |
| [prose-standard](docs/documentation/prose-standard.md) | documentation | contract-first prose: preserve propositions, drop reasoning transcripts |
| [documentation-placement](docs/documentation/documentation-placement.md) | documentation | one home per fact; tutorials vs references; budgets as guardrails |
| [decision-records](docs/process/decision-records.md) | process | ADRs with classification, lifecycle, mandatory alternatives |
| [minimal-evidence-checks](docs/process/minimal-evidence-checks.md) | process | the smallest check set that covers the diff; fix or explain failures |
| [code-review](docs/process/code-review.md) | process | two axes (standards + spec); substantiated blockers over nits |
| [pr-history-hygiene](docs/process/pr-history-hygiene.md) | process | lease-protected rewrites, deliberate labels, native stack merges |

## Where they come from

Every skill is distilled from a real convention in DeepSeek Harness and adapted so it works in any codebase — not only inside the harness it came from.

## How it's packaged

Each skill is one `<category>/<name>` directory carrying three files in a single change:

- `SKILL.md` — the executable standard (Claude Code / any agent harness)
- `agents/openai.yaml` — Codex metadata and invocation policy
- `docs/<category>/<name>.md` — a human-facing docs page

```text
skills/
  architecture/   how code is shaped and how failure is handled
  testing/        how behavior is verified
  documentation/  how prose and docs are written
  process/        the workflow around code — decisions, review, checks, git
```

## Invocation design

Skills are either **model-invoked** (the agent reaches for them automatically when a trigger fires) or **user-invoked** (only a human typing the skill's name can fire them — zero context load, but the human is the index). All ten skills here are model-invoked.

## Installation

The install routes below are alternatives, not add-ons — pick one.

### `npx skills` — any agent (Claude Code, Codex, …)

The [skills.sh](https://skills.sh) installer copies editable skill files into your project:

```bash
npx skills@latest add arch3rPro/dsh-skills
```

The installer lets you choose which skills to take and which coding agents to install them on. All ten skills are **model-invoked**, so they auto-fire once installed.

Or install one skill at a time:

```bash
npx skills@latest add arch3rPro/dsh-skills --skill=code-review
```

> `npx skills` pulls from GitHub — publish the repo first, then run the command above.

### Claude Code — the plugin

Add this repo as a Claude Code marketplace, then install the plugin:

```bash
claude plugins marketplace add arch3rPro/dsh-skills
claude plugins install dsh-skills@dsh-skills
```

The plugin manifest lives in `.claude-plugin/` (`marketplace.json` + `plugin.json`).

### Local symlinks — for development

Run `scripts/link-skills.sh` to symlink every skill into `~/.claude/skills` and `~/.agents/skills`. Re-run after adding, removing, or renaming a skill.

> **Pick one route.** `npx skills` writes files you own and edit; the Claude Code plugin is a managed bundle. Installing both leaves every skill twice.

## Acknowledgments

These skills are distilled from the engineering conventions of **DeepSeek Harness**.
