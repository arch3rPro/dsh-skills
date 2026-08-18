# PR History Hygiene

## What it does

Discipline for the lifecycle of a pull request, from preparation through landing — how to split work, rewrite history safely, label, and land a stack of dependent PRs. It applies to any git workflow with pull requests; the platform-specific bits generalize to whatever the repo uses.

**The defining constraint:** history is rewritten only when **lease-protected** — a force-push that aborts if the remote has moved — and never with raw force. Everything else follows from protecting other people's work and the review record.

## When to reach for it

- **Invocation mode.** Model-invoked: the agent reaches for it when preparing, rewriting, labeling, merging, or stacking pull requests.
- **Trigger boundary.** Reach for it when the question is *how to move a change through the PR lifecycle*. For *what to review* in the change, use [code-review](./code-review.md); for *what checks to run* before pushing, use [minimal-evidence-checks](./minimal-evidence-checks.md).

## Prerequisites

A git workflow with pull requests. The stacked-PR portion assumes the platform has a native stack feature and that all branches live in one repository.

## The leading idea: lease protection

The whole skill rests on one rule: **a history rewrite is safe only when it cannot silently destroy a concurrent update.** Lease-protected force-push aborts if the remote moved; raw force-push does not. Everything else — re-auditing review state after a rewrite, splitting work, stacking — protects the same two things: other people's work and the integrity of the review record.

## Common questions

**Is rebasing allowed after review?** Yes. A history rewrite is allowed after review, but it invalidates commit-OID assumptions — so you must re-fetch the live heads and re-audit review threads, approvals, mergeability, and checks afterward. Pre-rewrite hashes are not current evidence.

**Why land a stack through the native feature and not per-PR merges?** Manual merging and retargeting reproduces stack semantics badly — it can reorder, break bases, and leave dependents pointing at merged heads. The native stack feature owns the ordering, retargeting, and merge state; you just submit the whole range and verify it landed.

## It's working if

- Every PR is one coherent change; unrelated work is split.
- Every history rewrite is lease-protected; raw force-push never occurred.
- Review threads, approvals, mergeability, and checks were re-audited after any rewrite.
- Labels: one kind plus all material areas.
- A stack landed through the native stack feature, every selected PR reported merged, and branches were deleted only after merged-state verification.

## Where it fits

The *landing* skill in the process category, closing the loop after [code-review](./code-review.md) (correctness) and [minimal-evidence-checks](./minimal-evidence-checks.md) (the run before push). It pairs with [decision-records](./decision-records.md) when a change's rationale should survive in the history.
