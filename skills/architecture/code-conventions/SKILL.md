---
name: code-conventions
description: General code conventions that keep a codebase predictable — reversible side effects, switching on discriminant tags, explicit-over-implicit at boundaries, configuration over hardcoded tunables, branded opaque ids, trusting types at typed boundaries, and honest empty catches. Use when writing, reviewing, or refactoring code in a typed language with an explicit boundary structure (services, plugins, modules, packages).
---

# Code Conventions

A set of conventions distilled from a large, heavily-gated TypeScript codebase. Each one prevents a recurring class of mistake. They are not style preferences; they are rules that keep behavior **explicit**, **reversible**, and **checked at the right boundary**. Apply the ones that fit your codebase's shape; most assume a typed language and module/package boundaries.

**The defining constraint:** every convention makes one thing *unambiguous* — where a side effect can be undone, where a decision is made, where a value is validated, and what a swallow actually swallowed.

## Reversible side effects

Registrations and contributions are effects, and every effect has a disposer. When a plugin, module, or service contributes something to a shared context — a listener, a schema, a provider, a slot — the registration path returns the function that undoes it. This makes reload and teardown unwind predictably. If a contribution cannot be undone, that is a design gap to name, not something to hide.

## Switch on discriminant tags

When a union is closed, exhaustiveness is checked by ending the switch in `assertNever`. When the union is deliberately open to extension, fall through a **documented default** rather than a bare `default` that silently does nothing. The reader should always be able to tell "every case handled and proven" from "unknown case falls through on purpose."

## Explicit over implicit at boundaries

Defaulting and choice-making happen at one named step, never hidden inside a downstream call. If a request carries optional fields that must resolve to concrete values, the resolution is an explicit `resolve(request) → spec` step in the owning implementation — not a `?? default` tucked inside `run()`. A caller reading `run()` should never have to hunt for the default it applied.

## Configuration over hardcoded tunables

Anything that varies by deployment is a validated configuration field, changeable by the operator — not a hardcoded constant or a test-only hook. A `DEFAULT_*` constant is a code smell for a choice that belongs in config. The inverse also holds: protocol constants, external specifications, and security invariants stay **fixed** in code; they are not configurable because someone might someday want to change them.

## Fail loud, at the earliest resolvable point

Misconfiguration fails loudly at load when it is self-contained, and at the earliest resolvable point otherwise. Never silently skip a missing referent — a config that names something absent is an error to surface, not a feature to ignore.

## Brand opaque cross-boundary ids

An opaque identifier that crosses a module, service, or wire boundary is a branded type (`Branded<B>`), never a bare `string`. The brand keeps two unrelated id spaces from silently interoperating, and it tells the reader what domain the value belongs to.

## Trust types at typed same-process boundaries

At a **typed, same-process** boundary — a direct call the compiler checks — do not add runtime validation, defensive fallbacks, or hostile-input tests for values the static interface already requires. Add runtime validation only where the boundary is genuinely untrusted: parser/config input, queued data, model or tool JSON, durable files, worker or process messages, and wire boundaries. Over-validating a typed boundary is redundant cost; under-validating an untyped one is a crash waiting.

## Honest empty catches

An empty `catch` names what it swallows and why nothing else can reach it — a one-line comment that states the swallowed class of error and the argument that no other error can occur there. Keep the `try` to one statement so the catch's scope is obvious. Never write a bare `catch {}` that could be hiding a real failure.

## Symmetry for parallel values

Parallel constructs (twin functions, sibling cases, paired options) are written symmetrically. An unexplained asymmetry usually means an extraction was missed — one path gained behavior the other silently lacks. When you see two things that "should" match and don't, ask which one is wrong before accepting the difference.

## Tests describe behavior, not correctness

Tests pin behavior. When behavior intentionally changes, the tests change with it — do not preserve a "correct" test for obsolete behavior. Explain the behavior change in the PR; do not let a stale test masquerade as the source of truth.

## Workflow

1. **Name the boundaries.** For the code in hand, list the explicit boundaries: typed same-process calls, and the genuinely untrusted ones (config, wire, worker, file, model/tool JSON).
2. **Trace reversibility.** Every contribution has a disposer; if one does not, flag it.
3. **Trace decision points.** Every default, every switch fall-through, every catch is either explicit and documented, or an open bug.
4. **Apply the positive rule** at each site.

## Completion criteria

- Every side effect has a returned disposer.
- Every closed union ends in `assertNever`; every open union falls through a documented default.
- Every default is an explicit resolution step, never a hidden `?? default` in a downstream call.
- Every deployment-varying choice is a validated config field; protocol and security constants stay fixed.
- Every opaque cross-boundary id is branded.
- Runtime validation exists exactly at untrusted boundaries and nowhere else.
- Every empty catch names what it swallows and why nothing else can reach it.
- Parallel constructs are symmetric; every asymmetry is accounted for.
