# Minimal Evidence Checks

## What it does

Runs the **relevant** local evidence before a push without reflexively running the full repository suite. It matches the evidence to the surface the diff touches, never repeats a passing check, and fixes or explains a failure rather than pushing on hope.

**The defining constraint:** every behavior change needs the narrowest available check that would fail for its regression — nothing more, nothing less. CI owns exhaustive coverage; you own the narrow evidence.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it before pushing, force-pushing, marking ready for review, or claiming checks pass.
- **Trigger boundary.** Reach for it when the question is *what to run before a push*. For *what a change needs to be tested* (and how to trust the test), use [testing-tiers](../testing/testing-tiers.md) — that skill decides the tier; this one decides the run.

## Prerequisites

A repo with checks and a CI system. The evidence-by-surface table generalizes; the concrete check names are placeholders for the project's own commands.

## The leading idea: the smallest set

The whole discipline is one idea: **run the smallest set of checks that would catch the change's regression, and run it once.** The full suite is CI's job; repeating a passing check for a commit or push is waste that slows the loop and dulls attention.

## Common questions

**Why not just run the full suite before every push?** Because the full suite is slow, and its breadth makes a single focused failure easy to lose. The narrow check that fails on *this* change is the one with signal; the rest is CI's exhaustive safety net.

**Is force-push ever fine?** Only lease-protected — a force-push that aborts if the remote moved concurrently. Raw force-push is never allowed because it silently overwrites someone else's work.

## It's working if

- The outgoing diff's scope is inspected against a verified base, not guessed.
- Every surface the diff touches has its narrowest check; nothing broader than needed was run.
- A passing check was not repeated merely because commit or push followed.
- A failing relevant check was fixed or explained before the push.
- Any history rewrite used lease protection, and heads and review state were re-audited after.

## Where it fits

A process-category skill about the *run*, sitting alongside [testing-tiers](../testing/testing-tiers.md) (the *what to test* decision), [decision-records](./decision-records.md) (the *why*), and [code-review](./code-review.md) (the *correctness* gate). It is the pre-push half of the review workflow.
