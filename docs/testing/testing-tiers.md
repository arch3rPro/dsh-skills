# Testing Tiers

## What it does

A decision discipline for keeping a test suite green **and** meaningful. It tells you which test tier a change needs, then keeps that tier honest: test the real entry path, verify the world rather than the component's self-report, prefer the real implementation over a mock, and treat line coverage as necessary, never sufficient.

**The defining constraint:** tests must exercise the **real entry path** and **verify the world** — not the component's self-report. A mock-heavy unit suite can be 100% green while the shipped behavior is broken.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it when writing, planning, or reviewing tests, deciding what a change needs, or when a suite is green but the product is broken.
- **Trigger boundary.** Reach for it when the question is *what to test and how to trust it*. For the failure-handling rules that apply *inside* the code being tested (settlement, ownership, untrusted IO), use [defensive-patterns](../architecture/defensive-patterns.md) — that skill guards the behavior, this one guards the verification.

## Prerequisites

A test suite (any framework — the tier names are framework-neutral). The skill scales to any project size; on a small project the "real entry path" and "snapshot" tiers still apply to the shipped binary or CLI even if there is no web surface.

## The leading idea: verify the world

The whole skill rests on one discipline: **assert on external, observable state** — a re-run, a re-read, a byte-identical file — never on the component's own report of success. Once the assertion trusts the component, the suite can be green while the component is broken.

## Common questions

**Why not just push coverage to 100%?** Coverage proves lines ran, not that the feature works. A 100% covered but wrongly-behaved component passes; an uncovered line is often dead code to delete, not a test to bolt on. Coverage is a floor; behavioral tests that fail on the intended regression are the real verification.

**When is a mock acceptable?** Only at the expensive or non-deterministic boundary — an external API, the network, the clock. Everything downstream stays real, and a mocked model or API is a *scripted* stand-in driving the real downstream code.

## It's working if

- Every product-visible change has a real-entry-path test, not a hand-built harness.
- Every assertion verifies external state or a re-run/re-read, not the component's self-report.
- Mocks exist only at expensive or non-deterministic boundaries.
- The shallowest tier that would catch the regression is the one used; the full suite is CI's job.
- Behavior changes updated their tests in the same change.

## Where it fits

The testing category's only skill. It is the *verification* counterpart to [defensive-patterns](../architecture/defensive-patterns.md) (which guards failure handling) and pairs with [minimal-evidence-checks](../process/minimal-evidence-checks.md) (which decides what to *run* before a push — this skill decides what a change *needs* to be tested).
