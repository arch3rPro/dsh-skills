# Event Contract Matrix

## What it does

Documents **who produces and who consumes each event** in an event-driven or pub/sub system, as a single source of truth.

**The defining constraint:** the matrix records the **many-to-many** relationship — each event lists its dispatch sites and its listeners — and explicitly notes sites that **deliberately bypass** the normal emit path.

## When to reach for it

- **Invocation mode.** Model-invoked: in an event-driven or pub/sub system where events cross module boundaries.
- **Trigger boundary.** Use it when an event contract needs a documented home. For where a fact belongs in the doc hierarchy generally, use [documentation-placement](./documentation-placement.md); this skill is the concrete event-contract artifact.

## The leading rule

An event contract is not "this event exists"; it is **who can hear it**. Recording producers and listeners — including bypass sites — makes a change to either side visible against the whole graph instead of being discovered per call site.

## Keeping it a single source of truth

- Update the matrix **in the same change** as an event-contract change.
- Make it the contract's home; other docs link, not restate.
- Review it like a contract before merging.

## Common questions

**Table or graph?** For many-to-many relations, a table — one event per row, producers and listeners as columns — is denser and more readable than one sprawling graph.

**Why note bypass sites?** A site that deliberately skips the standard emit path is a hidden surprise if undocumented; listing it keeps the contract honest.

## It's working if

- Every boundary-crossing event lists its producers and listeners.
- Deliberate bypass sites are explicit.
- The matrix is the single home; other docs link.
- It updates with each contract change and is verified before merge.

## Where it fits

The contract-documentation half of the documentation category, alongside [documentation-placement](./documentation-placement.md) (where a fact belongs) and [prose-standard](./prose-standard.md) (how to write it). This is a concrete artifact for event-driven systems.
