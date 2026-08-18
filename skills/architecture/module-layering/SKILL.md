---
name: module-layering
status: beta
description: "Know and enforce your module dependency graph — derive inter-module edges from the canonical dependency signal, catch circular dependencies, and enforce intended layering with tooling. Use when a codebase has many modules or packages and layering is a real concern."
---

# Module Layering

A discipline for **knowing and enforcing the dependency graph** of a multi-module or multi-package codebase. It keeps the intended layering explicit, surfaces circular dependencies, and makes a violation fail instead of silently drifting.

**The defining constraint:** derive the graph from the **canonical dependency signal** — the single authoritative statement of what each module depends on (a package manifest's peer dependencies, a module's declared imports) — rather than from ad hoc inspection. Enforce intended direction with tooling, not memory.

## Know the graph

- **Identify the canonical dependency signal** for each module: the declared peer/regular dependency for packages, or the module imports for in-repo modules.
- **Derive the inter-module edges** from that signal, grouped by the package or module hierarchy, so the graph is reproducible rather than hand-maintained.
- **Keep the graph as a documented artifact** (a module-graph page or generated report) so it is the single home for dependency facts.

## Enforce layering

- **Decide the intended layering** — which modules may depend on which. State it explicitly (a layering rule per layer), not implicitly.
- **Detect circular dependencies** — a cycle means no clear layer boundary and is a signal to re-examine ownership.
- **Enforce with tooling** (e.g. a dependency-cruiser or graph analyzer), running in the check gate so a new edge that violates the intended direction fails rather than silently drifting.

## When it applies

Reach for this when a codebase has enough modules or packages that dependency relationships are non-trivial — multiple packages, a plugin ecosystem, or a layered architecture where the direction of dependencies matters. A single small module does not need a graph.

## Workflow

1. **Confirm the concern** — enough modules that layering matters; if not, skip.
2. **Identify the canonical dependency signal** and derive the edges.
3. **State the intended layering** explicitly, per layer.
4. **Enforce with tooling** in the check gate; treat a circular dependency or an edge against the intended direction as a failure.
5. **Keep the graph as a documented artifact**, updated with the code.

## Completion criteria

- Edges are derived from the canonical dependency signal, not ad hoc inspection.
- Intended layering is explicit; circular dependencies are surfaced.
- Layering is enforced by tooling in the check gate, so violations fail.
- The graph is a documented artifact and the single home for dependency facts.
