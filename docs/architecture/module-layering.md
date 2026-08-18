# Module Layering

## What it does

**Knows and enforces the dependency graph** of a multi-module or multi-package codebase — surfacing circular dependencies and enforcing the intended layering with tooling instead of memory.

**The defining constraint:** derive the graph from the **canonical dependency signal** (a package manifest's peer dependencies, a module's declared imports), and enforce intended direction with tooling in the check gate.

## When to reach for it

- **Invocation mode.** Model-invoked: when a codebase has many modules or packages and layering is a real concern.
- **Trigger boundary.** Use it when dependency relationships are non-trivial — multiple packages, a plugin ecosystem, or a layered architecture. A single small module does not need a graph. For deciding when a capability deserves its own seam, use [extension-points-and-seams](./extension-points-and-seams.md).

## The leading rule

The graph comes from the **canonical dependency signal**, not ad hoc inspection — so it is reproducible and always matches the code. Enforce the intended direction with tooling, so a violation fails rather than silently drifting.

## Common questions

**Why derive from the canonical signal?** A hand-maintained graph drifts. Deriving from the declared dependencies keeps it reproducible and current; the graph is a projection of the code, not a separate document.

**What does a circular dependency mean?** No clear layer boundary — a signal to re-examine ownership before layering can be enforced cleanly.

## It's working if

- Edges are derived from the canonical dependency signal.
- Intended layering is explicit; circular dependencies are surfaced.
- Layering is enforced by tooling in the check gate.
- The graph is a documented artifact and the single home for dependency facts.

## Where it fits

The structure half of the architecture category, alongside [extension-points-and-seams](./extension-points-and-seams.md) (when a capability gets its own seam) and [code-conventions](./code-conventions.md). It turns "which module may depend on which" from tribal knowledge into an enforced, documented fact.
