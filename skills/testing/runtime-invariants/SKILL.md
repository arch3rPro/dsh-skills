---
name: runtime-invariants
status: beta
description: "Assert only authoritative state at runtime — authoritative event streams or mutable data, never service or method presence — with each check owned by the module it guards and failing loud at startup. Use when adding runtime invariant checks, or deciding what an invariant may assert. It complements testing-tiers, which picks the test tier."
---

# Runtime Invariants

A discipline for **runtime invariant checks** — checks that run in the running system and fail loud when a package's contract is violated. It is distinct from [testing-tiers](./testing-tiers.md), which decides which test tier a change needs; this skill decides *what an invariant may assert* and how checks are owned and registered.

**The defining constraint:** a check may assert **authoritative event streams or mutable data — never service or method presence**. An implementation-detail check ("this service exists", "this method was called") is not an invariant; it tests implementation, not contract.

## What an invariant may assert

An invariant guards a *contract the running system owns* — an event that was produced, a durable state transition that occurred, a relationship that must hold. It asserts:

- an **authoritative event stream** (this event fired in this order, with this content);
- **mutable data** (this invariant over the store holds after this operation).

It never asserts service or method **presence** — whether a capability is wired up — because that is an implementation detail, not a contract. Asserting presence turns the check into a synthetic test that passes regardless of behavior.

## Ownership and registration

- **Each check is owned by the module whose contract it guards.** The check registers under the module's exact name; a duplicate registration fails loud rather than silently overwriting.
- **Fail loud at startup.** An invalid, blank, or duplicate check declaration throws at startup instead of being skipped, so misconfiguration is visible immediately.
- **Reserve the name.** Registration reserves the module's name even when filters keep the check inactive, so two modules can never silently claim the same contract.
- **No synthetic checks.** Register a check only when the module owns an observable event or mutable-data relationship. If nothing is observable, say so and explain, module-specifically, why nothing is checkable — do not fabricate an assertion to fill a slot.

## Workflow

1. **Identify the contract** the module owns — an event stream or mutable-data relationship.
2. **Decide the assertion** — what must hold, stated as authoritative state, never as service/method presence.
3. **Register the check** under the module's exact name; a duplicate fails loud.
4. **Make failures loud** — a violation reports the owning module and the violated contract.
5. **If nothing is observable**, register an explicit note explaining why, rather than a synthetic check.

## Completion criteria

- Every check asserts authoritative state (events or mutable data), never service or method presence.
- Each check is owned by and registered under the module it guards; duplicates fail loud.
- Failures are attributable to the owning module and name the violated contract.
- Startup fails loud on invalid, blank, or duplicate declarations.
- No synthetic checks; a module with nothing observable says so explicitly.
