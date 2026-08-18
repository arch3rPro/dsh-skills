---
name: code-review
description: Review a change along two axes — Standards (does the code follow the repo's documented standards, plus a smell baseline?) and Spec (does it faithfully implement the originating issue/spec?) — run as parallel sub-agents and reported side by side, prioritizing correctness, lifecycle, and security over style. Use when reviewing a branch, PR, or work-in-progress change, or when asked to "review since X".
---

# Code Review

A **two-axis** review of the diff between a fixed point and the current head:

- **Standards** — does the code conform to the repo's documented coding standards?
- **Spec** — does the code faithfully implement the originating issue / spec?

Run both axes as **parallel sub-agents** so they don't pollute each other's context, then aggregate. **This is guidance, not a complete checklist** — verify the live base and head before reviewing, and read enough surrounding code to understand the design.

**The defining constraint:** prioritize correctness, lifecycle, security, and broken required behavior over style. A short review with one substantiated blocker is better than a list of nits.

## Why two axes

A change can pass one axis and fail the other:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**

Reporting them separately stops one axis from masking the other. Do not merge or rerank findings across axes.

## Process

### 1. Pin the fixed point and the spec source

Capture the diff against the merge-base of the supplied fixed point (commit, branch, tag). Find the originating spec in order: issue references in commit messages → a path the user passed → a spec file under the repo's docs/specs directory. If there is no spec, the Spec axis reports "no spec available" and skips.

### 2. Identify the standards sources

Anything the repo documents about how code should be written (a `CODING_STANDARDS.md`, `CONTRIBUTING.md`, `AGENTS.md`). On top of that, always carry the **smell baseline** below, which applies even when the repo documents nothing:

- **The repo overrides.** A documented repo standard wins; where it endorses something the baseline flags, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic, never a hard violation; skip anything tooling already enforces.

**The smell baseline** (each reads *what it is* → *how to fix*): Mysterious Name; Duplicated Code; Feature Envy; Data Clumps; Primitive Obsession; Repeated Switches; Shotgun Surgery; Divergent Change; Speculative Generality; Message Chains; Middle Man; Refused Bequest.

### 3. Spawn both sub-agents in parallel

- **Standards sub-agent:** the diff, the standards-source files, and the full smell baseline (it has no other access). Ask for, per file/hunk: (a) violations of a documented standard, citing the standard; (b) baseline smells, named and quoted. Distinguish hard violations from judgement calls; skip what tooling enforces. Cap the report.
- **Spec sub-agent:** the diff and the spec. Ask for: (a) requirements missing or partial; (b) behavior not asked for (scope creep); (c) implemented-but-wrong requirements, each quoting the spec line.

### 4. Aggregate

Present the two reports under separate headings, verbatim or lightly cleaned. End with a one-line summary per axis: finding count and worst issue within each axis — never a single winner across axes.

## Review focus (apply during the read)

- **Intent and interface contracts:** trace both sides of every changed interface — errors, cancellation, ownership, disposal.
- **Lifecycle and concurrency:** races before publication, cancellation during awaits, independent error reporting, callback containment, complete detach cleanup, quiescent disposal.
- **Consumer fit:** trace every consumer; flag consumer-specific behavior leaking into an interface, and the inverse (a public method with one internal caller — prefer a private closure).
- **Scope and necessity:** map each abstraction, state machine, option, and compatibility path to a current contract and consumer; challenge speculative generality.
- **Configuration evidence:** ask what evidence supports each default, public operation set, and format; require an explicit choice or deferral where evidence is absent.
- **Enforcement:** follow every denial path to the operation that executes it; test alternate callers that can bypass a schema, facade, wrapper, or listener order.
- **Bounds:** enforce limits where the complete result is known; probe tiny/exact limits, oversized chunks, and multibyte text.
- **Real entry path:** tests exercise the shipped entry (loader, binary, worker), not a hand-mounted harness.
- **Test strength:** assertions fail on the intended regression and verify external state, not a restatement of the implementation.

## Reporting findings

State the defect, location, impact, and evidence. Place a localized defect inline on the tightest diff range; use a review-level comment for cross-cutting architecture or scope. Separate blockers from suggestions, and omit issues already enforced by a green gate.
