---
name: event-contract-matrix
status: beta
description: "Maintain an explicit matrix of which module dispatches each event and which modules listen — many-to-many, with deliberate bypass sites noted — so event contracts stay a single source of truth. Use in event-driven or pub/sub systems where events cross module boundaries."
---

# Event Contract Matrix

A discipline for documenting **who produces and who consumes each event** in an event-driven or pub/sub system. It keeps the event contracts a single source of truth, so a change to a producer or consumer is visible against the whole graph instead of being discovered per call site.

**The defining constraint:** the matrix records the **many-to-many** relationship — each event lists its dispatch sites and its listeners — and explicitly notes sites that **deliberately bypass** the normal emit path. An event contract is not just "this event exists"; it is who can hear it.

## What the matrix records

- **One row (or entry) per event**, listing:
  - the **producer(s)** that dispatch it — including any dispatch site that deliberately bypasses the standard emit path (e.g. containment-driven dispatch), so those are visible rather than a hidden surprise;
  - the **listener(s)** that receive it.
- **The relationship shape**: many-to-many, so the matrix is a table of event → producers and event → listeners, not one large implicit graph.

A dense many-to-many relation is best presented as a table rather than a sprawling graph — one event per row, producers and listeners as columns.

## Keeping it a single source of truth

- **Update the matrix in the same change that changes an event contract** — a new event, a new producer, a new listener, or a new bypass site. Do not let the matrix drift from the code.
- **Treat the matrix as the contract's home.** Where a contract is defined, link to the matrix; do not restate the producer/listener list in multiple places.
- **Review it like a contract.** When a dispatch or listen site changes, verify the matrix still matches before merging.

## Workflow

1. **Enumerate the events** that cross module boundaries.
2. **For each event, record its producers and listeners** — including bypass sites.
3. **Choose the presentation** — a table for many-to-many relations, kept dense and readable.
4. **Update it with each contract change** in the same change; link from the contract's definition.
5. **Verify** the matrix matches the code before merging.

## Completion criteria

- Every boundary-crossing event appears with its producers and listeners.
- Deliberate bypass sites are explicitly noted, not hidden.
- The matrix is the single home for producer/listener relationships; other docs link, not restate.
- It is updated in the same change as any event-contract change and verified before merge.
