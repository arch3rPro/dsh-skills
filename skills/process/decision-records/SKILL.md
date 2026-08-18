---
name: decision-records
description: Record design decisions as Architecture Decision Records (ADRs) so the why survives — with a classification, a lifecycle, and a mandatory alternatives-considered section. Use when making or proposing a non-trivial design decision, when reviewing a change that affects architecture, contracts, processes, or formats, or when deciding whether to archive a past decision. Applies to any project that wants its decision rationale to outlive the people who made it.
---

# Decision Records

An **Architecture Decision Record (ADR)** captures the *why* and *what we gave up* behind a design decision — the parts code and docs cannot carry. This skill covers where records live, when to write one, and the in-file structure. It applies to any project that wants its rationale to outlive the change.

**The defining constraint:** an ADR records a *decision* — the alternatives it beat and the consequences it accepted — not a transcript of how the decision was reached. A decision without its rejected alternatives invites re-litigation.

## Layout and lifecycle

Every record has two axes:

- **Lifecycle** — its status, which changes over time:
  - **proposed** — not yet built (or only partly); the plan and open questions live here.
  - **accepted / implemented** — the decision shipped; the file describes shipped reality in the **present tense** and is kept current with what actually shipped (facts — paths, names, structure — not the decision itself).
  - **rejected** — considered and declined; keep it only while its rationale prevents a tempting, meaningful mistake.
- **Class** — the *kind* of decision (feature, bug-fix, simplification, architecture, process, testing). Pick the class folder that matches.

A record moves between lifecycle folders as its status changes; the move updates the status line and the body's form in the same change.

## When to write one

Write (or update) an ADR when a change is **non-trivial**: it alters behavior, architecture, a contract shared across files or modules, process or tooling, testing strategy, an on-disk/wire/config format, or another decision a maintainer may reasonably revisit. A purely mechanical or local edit with no behavior/contract/structure change is exempt.

**Never edit a record into a different decision.** Supersede it with a new one and keep both cross-linked, unless the old one is fully superseded and can be consolidated into the new owner.

## The in-file structure

Every record opens with the decision's **problem** — written to stand without the solution. What follows depends on the lifecycle:

- **proposed**: `Problem → Proposal → (bespoke) → Alternatives considered → Acceptance criteria → Risks`. Proposal may speak in future tense — plans, migration steps, and open questions belong here.
- **accepted/implemented**: `Problem → Decision → (bespoke) → Alternatives considered → Consequences`. Decision describes shipped reality in the present tense; *Consequences* records what the trade-off cost **and** bought. No future-tense spec language ("should", migration plans, acceptance checklists).
- **rejected**: the proposal, frozen; the verdict lives on the status line.

**Alternatives considered is mandatory.** Every record carries it: each genuine alternative and why it lost, one bold-led paragraph per alternative or a subsection per contested one. A decision recorded without what it beat invites re-litigation.

## Archiving

Archive an accepted decision when it is complete and its rationale is unlikely to guide future work. Keep it active while its alternatives, ownership boundary, negative guarantee, or reintroduction condition remains useful. Archive by *semantic value*, never by word count, age, or a target quota. Once archived, a record is frozen — never edit it, and never treat it as authority for current behavior.

## Workflow

1. **Decide if a record is owed.** Non-trivial decision → yes. Mechanical edit → no.
2. **Choose lifecycle and class** to match the decision's current status and kind.
3. **Write the problem** first, so it stands without the solution.
4. **Record the decision** in the form matching its lifecycle; state present-tense reality if it has shipped.
5. **Enumerate the alternatives** — every genuine one and why it lost.
6. **Record the consequences** — what the trade-off cost and bought.
7. **Audit for supersession** — does a new decision make an old one obsolete? Consolidate or cross-link.

## Completion criteria

- Every non-trivial decision has (or updates) a record in the matching lifecycle and class.
- The record opens with a problem that stands alone, and carries the lifecycle-appropriate body.
- **Alternatives considered** is present and names every genuine alternative and why it lost.
- An accepted record states present-tense reality and is kept current with what shipped.
- Archived records are frozen and never treated as current authority.
