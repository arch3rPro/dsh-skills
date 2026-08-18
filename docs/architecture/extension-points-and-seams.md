# Extension Points and Seams

## What it does

Design guidance for **swappable** capabilities. When a capability may have multiple implementations or consumers, it separates the capability into three roles — **contract**, **implementation**, **consumer** — so they can vary independently, and routes new behavior through documented extension points instead of patching a core. It scopes itself by project fit: a capability with a single fixed implementation and consumer is outside its scope.

**The defining constraint:** a seam is the place where a *swappable* capability lives. If nothing can plausibly vary — one implementation, one consumer, nothing imminent — there is no seam to build, and adding one is needless indirection.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it when designing a new capability, deciding whether to split an interface, or adding behavior to an existing system.
- **Trigger boundary.** Reach for it when the question is *structure* — should this become an interface/implementation split? For how the code inside a unit is written (reversible effects, explicit defaults), use [code-conventions](./code-conventions.md) instead. This skill only decides *whether* and *how* to create the seam.

## Project fit

The skill applies when a capability varies; it does not apply to single-fixed capabilities. A second implementation or consumer — real or imminent — is the signal to build a seam. Without one, the honest design choice is a single unit, documented rather than skipped.

## The leading idea: independent variation

The whole skill rests on one question: **does this capability vary independently from its consumers?** The three-role split buys one thing — independent variation. When you cannot name a real second implementation or second consumer, you cannot name what the split buys, so you should not split.

## Common questions

**When do I fold the three roles together?** When they change as one concern. The split is a function of independent variation, not of being a plugin — a plugin host can fold contract and consumer when there is genuinely one of each.

## It's working if

- The "no seam" decision is made explicitly and documented, not skipped.
- When a seam exists, contract / implementation / consumer are separated to the degree they vary.
- No consumer-specific behavior leaked into the contract, and no single-caller public API expansion exists.
- New behavior rides documented extension points, not core edits.
- Every registration through the seam is reversible.

## Where it fits

The *structure* half of the architecture discipline, alongside [code-conventions](./code-conventions.md) (how code is written) and [defensive-patterns](./defensive-patterns.md) (how failure is handled). It is a reach-for-it-anytime design judgement.
