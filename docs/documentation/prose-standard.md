# Prose Standard

## What it does

Writes prose that preserves every contract while deleting reasoning transcripts, repetition, and decoration — across comments, JSDoc, docs, prompts, diagnostics, and user-visible strings. It owns two rules: **preserve the complete proposition** (never drop a factual clause to get shorter), and **never let an authoring-session vantage leak into durable text** (no "used to", no PR vantage, no reasoning transcripts, no hedges).

**The defining constraint:** a smaller word count is never the goal by itself. The goal is every factual clause preserved, nothing more.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it when writing, reviewing, trimming, restoring, or auditing prose, or deciding where a comment or doc is required.
- **Trigger boundary.** Reach for it whenever prose is the deliverable. For *where* a fact belongs in the doc hierarchy and how deep to go, use [documentation-placement](./documentation-placement.md) — prose-standard is the *writing* discipline, documentation-placement is the *placement* discipline.

## Prerequisites

None. It runs on any passage in any project — a single comment or a whole documentation corpus.

## The two anchors

Two leading ideas hold the whole set together:

- **The complete proposition** — before editing, enumerate every factual clause (actor, condition, modality, negative guarantee, consequence) and preserve each one.
- **The session vantage** — durable prose speaks from the repository's state, never from the authoring session's. A reader with no transcript or PR thread must be able to resolve every reference.

## Common questions

**Does "trim" mean make it shorter?** Only as a side effect. The rule is *preserve every proposition, remove the rest*. If shortening drops a true fact or flips an obligation into an endorsement, it failed — restore the proposition.

**What about "used to" phrases that are technically true?** Resolvable is not enough on current-state surfaces. "The old connection drains before the new one accepts" is runtime lifecycle (fine); "the migration used to run at startup" is change history (move to the change description).

## It's working if

- Every proposition that matters is preserved; nothing added or dropped.
- The passage states the current state, with no history, review, or reasoning-transcript vantage.
- Every abstraction is checked against a more exact term; the precise subject is named.
- Each fact has one home; duplicates are links.
- Visible strings and prompts are treated as behavior, not decoration.

## Where it fits

The *writing* half of the documentation discipline, alongside [documentation-placement](./documentation-placement.md) (the *placement* half). Both are reach-for-it-anytime standalones.
