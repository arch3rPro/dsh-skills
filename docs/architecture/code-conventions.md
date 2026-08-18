# Code Conventions

## What it does

A set of conventions, distilled from a large heavily-gated codebase, that keep behavior explicit, reversible, and checked at the right boundary. Each one prevents a recurring class of mistake: reversible side effects, switching on discriminant tags, explicit-over-implicit defaulting, configuration over hardcoded tunables, branded opaque ids, trusting types at typed boundaries, and honest empty catches.

**The defining constraint:** every convention makes one thing unambiguous — where a side effect can be undone, where a decision is made, where a value is validated, and what a swallow actually swallowed.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it automatically when writing, reviewing, or refactoring code that touches side effects, defaults, unions, config values, or cross-boundary ids.
- **Trigger boundary.** For the bug-class rules about failure handling and ownership, use [defensive-patterns](./defensive-patterns.md) — conventions shape how code is *written*; defensive patterns shape how failure is *handled*. For when a capability warrants an interface/implementation split, use [extension-points-and-seams](./extension-points-and-seams.md).

## Prerequisites

A typed language with an explicit boundary structure (modules, packages, services) makes most of these conventions natural. In an untyped or single-file codebase, apply the ones that still fit — reversibility, explicit defaulting, honest catches — and set aside the type-dependent ones (branded ids, `assertNever`, trust-at-typed-boundaries).

## The two anchors

Two leading ideas hold the whole set together:

- **Reversibility** — every contribution to a shared context can be undone, so reload and teardown unwind predictably.
- **Explicitness** — every default, fall-through, and swallow is a named decision, never a silent `?? default` or a bare `catch {}`.

If a change you are reviewing violates one of these anchors, it has violated at least one convention.

## Common questions

**Aren't these TS-specific?** They were written in TypeScript, but only branded ids, `assertNever`, and trust-at-typed-boundaries depend on types. The rest — reversible effects, explicit defaulting, config-over-hardcoding, honest catches, symmetry — transfer to any language.

**Is "trust types at typed boundaries" an invitation to skip validation?** No — it is about *where*. At a typed same-process call, the compiler is the guard; adding redundant runtime checks there is noise. At an untyped boundary (config, wire, worker, file), the guard is missing, and that is exactly where validation belongs.

## It's working if

- Every side effect has a returned disposer, and teardown can unwind it.
- Every closed union ends in `assertNever`; every open union falls through a documented default.
- Defaults are explicit resolution steps, not hidden `?? default` inside `run()`.
- Deployment-varying choices are config fields; protocol and security constants stay fixed.
- Opaque cross-boundary ids are branded.
- Runtime validation exists exactly at untrusted boundaries and nowhere else.
- No bare `catch {}` exists — every empty catch names what it swallows and why nothing else can reach it.

## Where it fits

A reach-for-it-anytime standalone under architecture. It is the *writing* half of the architecture discipline; [defensive-patterns](./defensive-patterns.md) is the *failure-handling* half, and [extension-points-and-seams](./extension-points-and-seams.md) is the *structure* half (when to introduce an interface/implementation split).
