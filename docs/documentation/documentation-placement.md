# Documentation Placement

## What it does

Arranges documentation so a reader can find a fact exactly once. The core rule is **one home per fact**: each fact lives in the tier whose job it is, and everywhere else it is a link. It tells you where a fact belongs, how deep to go, and how to classify a document as tutorial or reference.

**The defining constraint:** the authoring order is *locate → set detail → classify → relocate descendant detail → link*. You decide where a fact lives before you write it.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it when writing, moving, restructuring, or auditing documentation, or deciding where a fact belongs.
- **Trigger boundary.** Reach for it when the question is *where and how deep*. For how each passage is *written* — preserving propositions, deleting session vantage — use [prose-standard](./prose-standard.md). Placement decides the home; prose-standard decides the words.

## Prerequisites

A documentation corpus (any size — the tier taxonomy scales from a single README to a large docs tree).

## The leading idea: one home

The whole discipline is one principle: **each fact has exactly one home, and elsewhere it is a link.** A fact stated in two places drifts — one copy ages, the other doesn't — and the reader never knows which is true. Placement is how you guarantee exactly one.

## Common questions

**Is a word budget a target?** No — a ceiling with headroom. When a budget gate goes red, relocate first, condense second, and raise the ceiling only when the words genuinely need the space. A too-low budget is a bug in the budget, not a reason to gut the document.

**Can I hand-fix a generated table?** No. Generated reference is regenerated from source; if the fact belongs there, change the generator and regenerate. A hand edit is overwritten or, worse, silently diverges from its source.

## It's working if

- Every fact has one home; duplicates are links.
- Each document is classified (tutorial or reference) from intended use.
- Detail is progressive: full for its own subject, summarized for children, linked for descendants.
- Generated content is regenerated from source, never hand-edited.
- Budgets are treated as guardrails with headroom, not reduction targets.

## Where it fits

The *placement* half of the documentation discipline, alongside [prose-standard](./prose-standard.md) (the *writing* half). Both are reach-for-it-anytime standalones.
