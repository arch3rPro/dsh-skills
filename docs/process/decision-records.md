# Decision Records

## What it does

Captures design decisions as **Architecture Decision Records (ADRs)** so the *why* survives — the alternatives a decision beat, and the consequences it accepted. It covers where records live, when to write one, and the in-file structure.

**The defining constraint:** an ADR records a *decision* — its rejected alternatives and accepted consequences — not a transcript of how it was reached. A decision without what it beat invites re-litigation.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it when making or proposing a non-trivial design decision, reviewing a change that affects architecture/contracts/processes/formats, or deciding whether to archive a past decision.
- **Trigger boundary.** Reach for it when a decision needs to *outlive the change*. It complements [code-review](./code-review.md): a review checks a change against standards and spec; decision-records ensure the *rationale* behind the change is recorded. For what to write inside the prose, use [prose-standard](../documentation/prose-standard.md).

## Prerequisites

A place for records to live (a `docs/decisions/` or `.agents/` tree). The skill scales from one decision to a whole corpus.

## The leading idea: the rejected alternative

The whole practice rests on one idea: **a decision is only as durable as the record of what it rejected.** Without the alternatives section, a later maintainer cannot tell why the current choice won, and the whole argument gets re-litigated from scratch. The alternatives-considered section is the heart of the record.

## Common questions

**What counts as a "non-trivial" decision?** Anything that alters behavior, architecture, a shared contract, process, testing strategy, or an on-disk/wire/config format — or any decision a maintainer may reasonably revisit. A mechanical edit with no such change is exempt.

**Why is the implemented form present-tense?** Because an accepted record describes shipped reality and must be kept current with what actually shipped. Future-tense spec language ("should", migration plans) is planning, not a record of what is — it belongs in the proposal, not the shipped decision.

## It's working if

- Every non-trivial decision has (or updates) a record in the matching lifecycle and class.
- The record opens with a problem that stands alone, and carries the lifecycle-appropriate body.
- Alternatives considered names every genuine alternative and why it lost.
- An accepted record states present-tense reality and is kept current with what shipped.
- Archived records are frozen and never treated as current authority.

## Where it fits

A process-category skill about *why*, alongside [code-review](./code-review.md) (about *correctness*) and [minimal-evidence-checks](./minimal-evidence-checks.md) (about *running checks*). It pairs with [prose-standard](../documentation/prose-standard.md) for the writing itself.
