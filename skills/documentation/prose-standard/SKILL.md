---
name: prose-standard
description: Write prose that preserves every contract while deleting reasoning transcripts, repetition, and decoration — across comments, JSDoc, docs, prompts, diagnostics, and user-visible strings. Use when writing, reviewing, trimming, restoring, or auditing prose, or deciding where documentation or a comment is required. It owns two rules: preserve the complete proposition, and never let an authoring-session vantage leak into durable text.
---

# Prose Standard

Write enough to preserve the contract, then remove reasoning transcripts, repetition, and decoration. A **contract** is an obligation, invariant, precondition, postcondition, or compatibility promise that a caller, callee, implementer, producer, or consumer relies on. This skill owns editorial judgment and required prose coverage; it applies to any document or string an agent or human reads — comments, JSDoc, docs, prompts, diagnostics, and visible UI strings.

**The defining constraint:** a smaller word count is never the goal by itself. The goal is *every factual clause preserved, nothing more*. Trim or add as the proposition demands.

## Preserve the complete proposition

Before editing a passage, enumerate every proposition it carries. Preserve each relevant:

- actor and action;
- condition, timing, and ordering;
- modality — *must*, *may*, *never*;
- negative guarantee and exception;
- ownership, side effect, failure mode, and consequence.

Remove adjectives, repetition, and narration only when every factual clause survives and the result is clearer. A smaller word count alone is not an improvement. Do not weaken a proposition to make progress.

## Required coverage by location

This is not a one-way shortening pass — add prose where code and structure do not communicate a required contract.

- **Public API docs:** document caller-visible return distinctions, throws or rejections, side effects, ownership, timing, cancellation, and durability.
- **Internal comments:** orient non-local structure and obviously complicated local structure — invariants, race ordering, ownership, security boundaries, surprising failure. Delete control-flow narration and code restatement.
- **Module comments:** state the module's role, dependencies, responsibilities, and non-obvious architecture choices; link choices to their rationale.
- **Tests:** explain only non-obvious test design — why a fixture, an assertion, or an indirect observation is necessary. Delete walkthroughs.
- **READMEs / package docs:** include the consumer contract — configuration, semantics, failures, limitations, extension points.
- **Prompts and visible strings:** treat wording as behavior; inspect generated output and run behavior validation, or state why no check applies.
- **Diagnostics:** name the failing subject or path, the violated rule, and the correction when non-obvious. Remove internal execution narration.

## Never let an authoring-session vantage leak in

Durable prose states the current state from the repository's vantage — never the authoring session's. A reader at the latest state, with no access to any transcript, PR thread, or uncommitted draft, must be able to resolve every reference and verify every claim. In practice:

- **State the present, not the history.** Avoid "previously", "now", "no longer", "used to", "renamed", "was moved". State the current mechanism; put change stories in commits and change descriptions, not in durable prose.
- **No review or PR vantage.** No "a later PR in this stack", "this PR adds", "rejected in review", "the reviewer confirmed". State the shipped mechanism or extension point.
- **No reasoning transcript.** No step-by-step derivation, proof of obvious branches, test walkthroughs, or rejected local alternatives. Keep the resulting contract or durable rationale; delete the path used to derive it.
- **No hedges or planning residue.** "Probably fine for now", "should be enough" — promote to a tracked marker or restate as the actual bound; delete the hedge.

## Name the exact subject

Write directly: name actors and facts. Before writing a vague abstraction (*contract*, *boundary*, *shape*, *surface*, *gate*), ask whether a more exact term names the subject — *response fields*, *JSON validation*, *ESM exports*. Keep a term when it names the exact technical subject. Do not narrate control flow or tests, preserve review history, or restate code.

## One home per fact

State a fact in exactly one place; elsewhere, link. The same rationale repeated beside sibling methods keeps one home. Grep a distinctive phrase to find duplicates and replace copies with links.

## Workflow

1. **Scope the passage.** Confirm what is in scope and what the document or string must communicate.
2. **Enumerate the propositions** before touching anything; keep each relevant clause.
3. **Classify each candidate** as keep, add, trim, restore, or defer — and apply clear changes only when the task authorizes edits.
4. **Check for session-vantage leakage** and restate surviving facts from the repository's vantage.
5. **Verify the result** against the owning code or behavior; confirm no proposition was dropped.

## Completion criteria

- Every proposition that matters is preserved; nothing added or dropped.
- The passage states the current state, with no history, review, or reasoning-transcript vantage.
- Every abstraction is checked against a more exact term; the precise subject is named.
- Each fact has one home; duplicates are links.
- Visible strings and prompts are treated as behavior, not decoration.
