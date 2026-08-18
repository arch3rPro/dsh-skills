---
name: extension-points-and-seams
description: Design for swappable capabilities — when a capability may have multiple implementations or consumers, separate it into contract / implementation / consumer so they vary independently, and route new behavior through documented extension points instead of patching a core. Use when designing a new capability, deciding whether to split an interface, or adding behavior to an existing system. Out of scope (no seam needed) when a capability has a single fixed implementation and consumer.
---

# Extension Points and Seams

This skill scopes itself by **project fit**: it answers *when* a capability warrants a seam and *how* to build one. It applies to **swappable** capabilities. A capability with a single fixed implementation and a single consumer is outside its scope — for those a seam is needless indirection, and the honest design choice is to keep it a single unit.

**The defining constraint:** a **seam** is the place where a *swappable* capability lives — the contract, the implementation, and the consumer are separated so they can vary independently. If nothing can plausibly vary, there is no seam to build.

## Decide: does this capability warrant a seam?

Build a seam only when at least one of these is true:

- **Multiple implementations are real or imminent** — a second backend, provider, or adapter is already planned or shipped (local vs remote, mock vs real, one vendor vs another).
- **Multiple consumers exist** — more than one caller uses the capability, and they must not each couple to one implementation.

If there is one conceivable implementation and one consumer, keep it a single unit. Split **only when a second implementation or consumer appears** — never preemptively. The seam's whole value is independent variation; without variation there is nothing to buy.

## The three roles

A seam has three distinct concerns that change at different rates:

1. **Contract** — the interface that names the capability: the operations, the vocabulary types, the guarantees. It depends only on what the contract needs; it imports no implementation.
2. **Implementation** — a concrete provider that fulfills the contract. Multiple implementations are siblings against the same contract.
3. **Consumer** — what actually uses the capability. It programs against the contract and never imports a specific implementation's types.

Keep the three in separate units when they evolve independently; fold them together when they are genuinely one concern. A capability with one implementation and one consumer that happens to be a plugin host may fold contract and consumer — the split is a function of *independent variation*, not of being a plugin.

## Design the contract for all current consumers

The contract is shaped by **every** current consumer, not dictated by the loudest one. Keep implementation-, provider-, or consumer-specific behavior out of the contract — a consumer's special need lives in the consumer, not in the interface. The inverse smell is equally bad: a public method on a generic service whose only caller is one internal consumer is an unnecessary API expansion — hand that consumer a private closure instead of widening the contract.

## Attach behavior to extension points, not by patching the core

New behavior attaches to a **documented extension point** — a place the design names as open for contribution. If you find yourself modifying the core to add a feature that could ride an existing extension point, stop and route it through the point. When no extension point fits, adding one is a design decision, not a shortcut.

## Registrations are reversible

Contributions through a seam are effects with disposers — a listener, provider, or slot registers through a path that returns how to undo it, so reload and teardown unwind predictably. A seam whose registrations cannot be undone is a leak.

## Workflow

1. **Ask the variation question.** Could this capability plausibly have a second implementation or a second consumer? If no — and nothing is imminent — do not build a seam. Document the single choice instead.
2. **Name the three roles.** If a seam is warranted, write the contract first: operations, vocabulary types, guarantees. Then place implementations and consumers against it.
3. **Check the contract is consumer-neutral.** No one consumer's behavior has leaked in; no public method exists solely for one internal caller.
4. **Verify reversibility.** Every registration returns a disposer.

## Completion criteria

- The decision to build (or not build) a seam is explicit, and the "no seam" case is documented rather than absent.
- If a seam exists, contract / implementation / consumer are separated to the degree they vary independently.
- The contract serves every current consumer; no consumer-specific behavior leaked in; no single-caller public API expansion exists.
- New behavior rides documented extension points, not core edits.
- Every registration through the seam is reversible.
