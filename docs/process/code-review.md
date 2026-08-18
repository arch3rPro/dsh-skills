# Code Review

## What it does

Reviews a change along **two axes** — **Standards** (does the code follow the repo's documented standards, plus a smell baseline?) and **Spec** (does it faithfully implement the originating issue/spec?) — run as parallel sub-agents and reported side by side, so one axis never masks the other.

**The defining constraint:** prioritize correctness, lifecycle, security, and broken required behavior over style. A short review with one substantiated blocker is better than a list of nits.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it when reviewing a branch, PR, or work-in-progress change, or when asked to "review since X".
- **Trigger boundary.** Reach for it when the question is *correctness against the spec and the standards*. For *what checks to run* before pushing, use [minimal-evidence-checks](./minimal-evidence-checks.md); for the *rationale* behind a change, use [decision-records](./decision-records.md).

## Prerequisites

A git repo with a way to diff to a fixed point, and an identifiable spec source (issue tracker, a passed path, or a specs directory). The smell baseline (Fowler) applies even when the repo documents no standards.

## The leading idea: two axes that must not merge

The whole skill rests on keeping two questions apart: **did they do it right** (Standards) and **did they do the right thing** (Spec). Merging the two lets one mask the other — a standards-perfect implementation of the wrong thing passes as reviewed.

## Common questions

**Why parallel sub-agents?** So the two axes don't pollute each other's context. The Standards reviewer hunts for convention breaks; the Spec reviewer hunts for divergence from the issue. Running them together blurs both.

**Isn't the smell baseline just style?** Some are, but several (Shotgun Surgery, Divergent Change, Speculative Generality) are design defects with real cost, and a documented repo standard always overrides them. They are heuristics to flag and discuss, never hard violations.

## It's working if

- The review pins a verified fixed point and an identified spec source before reading the diff.
- The two axes are reported separately; no finding is reranked or merged across them.
- Correctness, lifecycle, and security findings outrank style nits.
- Every finding states the defect, location, impact, and evidence.
- The smell baseline was applied, with documented repo standards overriding it.

## Where it fits

The *correctness* gate in the process category, alongside [minimal-evidence-checks](./minimal-evidence-checks.md) (the *run* before push), [decision-records](./decision-records.md) (the *why*), and [pr-history-hygiene](./pr-history-hygiene.md) (landing the change after review).
