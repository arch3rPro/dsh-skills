# Runtime Invariants

## What it does

A discipline for **runtime invariant checks** — checks that run in the running system and fail loud when a module's contract is violated.

**The defining constraint:** a check may assert **authoritative event streams or mutable data — never service or method presence**. An implementation-detail check is not an invariant; it tests implementation, not contract.

## When to reach for it

- **Invocation mode.** Model-invoked: when adding runtime invariant checks, or deciding what an invariant may assert.
- **Trigger boundary.** Use it when a check must guard a *running* system's contract. For choosing which test tier a change needs, use [testing-tiers](./testing-tiers.md) — this skill decides what an invariant may assert and how checks are owned.

## The leading rule

A check asserts **authoritative state**: an event that fired, a durable state transition, a relationship that must hold. It **never asserts service or method presence** — asserting "this service exists" is an implementation detail that passes regardless of behavior.

## Ownership and registration

- Each check is owned by and registered under the module whose contract it guards.
- Duplicate registration and invalid declarations **fail loud at startup**.
- Registration **reserves the name** so two modules can never silently claim the same contract.
- **No synthetic checks.** Register a check only when the module owns an observable relationship; if nothing is observable, say so and explain why, rather than fabricating an assertion.

## Common questions

**Is an invariant a test?** Not the same thing. A test runs in the test tier and asserts the component's behavior; an invariant runs in the live system and asserts the running contract. They complement each other.

**What if my module has nothing observable to check?** Register nothing and state why, module-specifically. Fabricating a check to fill a slot weakens the whole set.

## It's working if

- Every check asserts authoritative state, never service or method presence.
- Each check is module-owned; duplicates fail loud.
- Failures are attributable and name the violated contract.
- Startup fails loud on invalid declarations; no synthetic checks exist.

## Where it fits

The runtime-verification half of the testing category, complementing [testing-tiers](./testing-tiers.md) (test-tier selection). Both answer "how do we know the system honors its contracts" — one in tests, one in the running system.
