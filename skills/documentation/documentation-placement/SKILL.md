---
name: documentation-placement
description: Decide where documentation belongs so each fact has exactly one home — classify documents as tutorial or reference, place each fact in the tier that owns it and link everywhere else, and keep budgets as guardrails rather than reduction targets. Use when writing, moving, restructuring, or auditing documentation, or deciding where a fact should be documented.
---

# Documentation Placement

A discipline for arranging documentation so a reader can find a fact exactly once. The core rule is **one home per fact**: each fact lives in the tier whose job it is, and everywhere else it is a link. This skill tells you where a fact belongs, how deep to go, and how to classify a document. It applies to any repo with documentation.

**The defining constraint:** the authoring order is *locate → set detail → classify → relocate descendant detail → link*. You decide where a fact lives before you write it, not after.

## The tier taxonomy: one home per fact

Documents form a hierarchy of tiers, each with a job. Place a fact in the tier whose job it is; elsewhere, link there.

| Tier | Job | Does NOT belong there |
| --- | --- | --- |
| **Standing orders** (top-level agent instructions) | Rules an agent needs in context every session, one to three lines each, linking its home | Stories, worked examples, anything restated from a linked home |
| **Architecture map** | Ordered map of the system — composition, core pieces, flows, extension points | Type definitions, per-module detail, decision rationale |
| **Reference** (one page per module/subsystem) | Type definitions, semantics, generated API | Behavior narration |
| **Decision records** | Active decisions — the why, what was given up, required verification | Migration plans, spec-speak once the decision has shipped |
| **How-tos / cookbook** | Step-by-step guides with numbered verify steps | Design rationale |
| **Package/module README** | The per-module consumer contract: config, semantics, limitations, extension points | JSDoc restatement, generated-catalog restatement |
| **Generated reference** | Exhaustive sources regenerated from source | Hand edits — change the generator instead |

Placement in one sentence: bugs → incident records; rationale → decision records; procedures → how-tos; type definitions → reference pages; package contracts → READMEs; standing orders → the top-level agent instructions.

## Classify tutorial vs reference

Every in-scope document is one of two forms:

- **Tutorial** — follows an ordered path to an outcome; introduces only what each step needs; orders concepts by prerequisite and difficulty.
- **Reference** — defines a lookup scope and current behavior; supports lookup without sequential reading.

Classify from intended use, not the title. Separate substantial mixed forms; label a section when one part is small. A tutorial's reader is classified (beginner/intermediate/advanced) before writing, so prerequisites precede dependent concepts.

## Progressive detail: describe your subject, link your children

A document's subject and tree position fix its scope. Describe its own subject at appropriate detail; summarize direct children only by purpose, responsibility, and high-level behavior; link to the owning descendant for lower-level detail. Document type does not widen this scope — a reference may be exhaustive only about its own subject.

## Budgets are guardrails, not reduction targets

If the repo sets word budgets, treat them as ceilings with headroom, not targets to hit. When a budget gate goes red: **relocate** content that belongs in another tier (leave a one-line link), then **condense** content that belongs here but can be shorter, and only then **raise** the ceiling when the words genuinely need the space — justify the change. A too-low budget is a bug in the budget, not the document.

## Never hand-edit generated content

Generated references, catalogs, and snapshots are never hand-edited. If a fact belongs there, change the generator's source and regenerate. A paired or derived artifact updates through its owner, never by hand.

## Workflow

1. **Locate the document** in the repo and navigation trees; state its subject and identify its direct children.
2. **Set the permitted detail** — full for its subject, summary for children, links for descendants.
3. **Classify** it as tutorial or reference from intended use.
4. **For a tutorial**, order concepts by prerequisite and difficulty; move optional advanced material later or to a reference.
5. **Relocate descendant-owned detail** and replace lower-level explanations with links to their owners.
6. **Audit for the slop checklist**: the same rule in more than one home, narrated history, hand-restated catalogs, reasoning transcripts, and status annotations.

## Completion criteria

- Every fact has one home; duplicates are links.
- Each document is classified (tutorial or reference) from intended use.
- Detail is progressive: full for its own subject, summarized for children, linked for descendants.
- Generated content is regenerated from source, never hand-edited.
- Budgets are treated as guardrails with headroom, not reduction targets.
