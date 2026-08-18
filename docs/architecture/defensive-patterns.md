# Defensive Patterns

## What it does

A catalogue of defensive-programming rules distilled from defects that actually shipped. Each pattern is one class of failure — a concurrency race, an ownership leak, an outcome misreported — stated as the positive rule that prevents its recurrence. Read it before writing lifecycle, concurrency, subprocess, teardown, error-reporting, or untrusted-IO code.

**The defining constraint:** the rules are about *settlement* (honestly reporting every independent fact of an outcome) and *ownership* (knowing who owns a resource until it is fully gone). Most concurrency bugs are a settlement or ownership violation in disguise.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it automatically when a change or review touches async setup/teardown, callbacks, spawned processes, workers, event listeners, disposal, error aggregation, temp files, or untrusted input.
- **Trigger boundary.** Reach for it when the code has a *settlement* or *ownership* decision to make. For test-strategy companions (verify the world, resource ownership in tests), use [testing-tiers](../testing/testing-tiers.md) instead.

## Prerequisites

None. It runs in any codebase — no framework, no build setup, no specific language (the wording is TS-flavoured but the patterns are language-neutral).

## The clusters

The seven patterns group into three clusters, so you apply the group that fits the code:

- **Reporting** — report orthogonal outcomes independently; honor public contracts on both sides; contain callback exceptions in the dispatcher.
- **Ownership** — async state is not synchronous state; dispose must reach quiescence, not just request it.
- **Untrusted IO** — scrub the environment; use private unpredictable paths; unlink link-shaped paths.

The leading words are *settlement* and *ownership*: if you can name which independent fact a caller must know, and who owns each resource until it is fully gone, you can apply the right pattern.

## Common questions

**Aren't these overkill for a small change?** The patterns are cheap to apply correctly at write time and expensive to chase as a bug. They matter most where "it usually works" hides a reproducible race — the exact code these patterns target.

**Is this just a checklist?** No. It is a judgement aid. Each pattern names a failure mode and the positive rule; apply the ones your code actually touches, and use the completion criteria to know when you are done.

## It's working if

- Every async or fallible path reports each independent outcome on its own branch or field — a time-out is never reported as a clean success.
- Every resource has one owner and a defined quiescence point that is actually awaited before teardown returns.
- Every dispatched callback is contained, so one bad subscriber cannot break core lifecycle.
- Every spawned command and temp file treats input as hostile: scrubbed env, private random paths, exclusive owner-only opens, link-safe removal.

## Where it fits

A reach-for-it-anytime standalone, and the architectural counterpart of [testing-tiers](../testing/testing-tiers.md) — the same settlement-and-ownership discipline applied to code versus to tests. It belongs with [code-conventions](./code-conventions.md) under architecture: conventions shape how code is written; defensive patterns shape how failure is handled.
