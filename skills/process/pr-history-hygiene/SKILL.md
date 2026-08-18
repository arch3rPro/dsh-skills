---
name: pr-history-hygiene
description: Keep pull-request history deliberate and safe — split independent changes, rewrite with lease-protected force-push (never raw force), apply one kind label plus all material area labels, and land a stack of dependent PRs through the platform's native stack feature rather than manually merging and retargeting. Use when preparing, rewriting, labeling, merging, or stacking pull requests.
---

# PR History Hygiene

Discipline for the lifecycle of a pull request, from preparation through landing. It covers how to split work, how to rewrite history safely, how to label, and how to land a stack of dependent PRs. It applies to any git workflow with pull requests; the platform-specific bits (stacking, labels) generalize to whatever the repo uses.

**The defining constraint:** history is rewritten only when it is **lease-protected** — a force-push that aborts if the remote has moved — and never with raw force. Everything else follows from protecting other people's work and the review record.

## Choose the history deliberately

- **Split independent changes.** Each PR is one coherent change; do not bundle unrelated work. When a bug is found in a PR you already published, fix the introducing PR before propagating the fix to dependents.
- **Pick the merge strategy per change.** After review, an ordinary branch may merge forward or rebase. A history rewrite is allowed after review, but it invalidates every commit-OID assumption — re-audit review threads, approvals, mergeability, and checks afterward.

## Rewrite safely — never raw force

Before any history rewrite:

1. Fetch the current remote branch and record its exact head.
2. Publish with a **lease-protected force-push** (e.g. `--force-with-lease=<branch>:<observed-head>`) so a concurrent update aborts the push instead of being overwritten.
3. **Raw `--force` is never allowed** — it silently destroys a concurrent update.
4. After the push, re-fetch the live heads and re-audit unresolved review threads, approvals, and checks. Commit hashes and inline-comment anchors from before the rewrite are not current evidence.

## Label deliberately

Apply one primary label that classifies the change's kind, and every material area label that the change touches. A label is *material* when the change substantively affects that area; do not over-tag with every area a file happens to live in.

## Land a stack through the platform's native stack

A **stack** is a set of dependent PRs where each bases on the one below it (A ← B ← C, each targeting the previous). Land them through the platform's **native stack feature**, not by manually merging and retargeting individual PRs.

- Verify every head branch lives in the same repository (native stacks require it), and that every dependent PR is a member of one official stack in bottom-to-top order.
- Link missing same-author members into the official stack; ask before linking when authors differ.
- Submit the whole stack, or an explicitly bounded prefix, through the stack's merge command. Do not pass per-PR delete flags, manually retarget dependents, or issue per-PR merges.
- Verify every selected PR reports **merged** (a queued request is not a completed landing), then delete branches only in a separate pass after merged-state verification.
- If the stack needs a refreshed base, prefer a native cascading rebase or an incremental merge-forward, validating each rewritten layer and re-auditing before merging.

## Workflow

1. **Split** — each PR is one coherent change; fix the introducing PR before propagation.
2. **Rewrite** — if a history rewrite is warranted, lease-protect it and re-audit after.
3. **Label** — one kind label plus every material area label.
4. **Land** — a standalone PR merges normally; a stack goes through the native stack feature, bottom-up, verified to merged.

## Completion criteria

- Every PR is one coherent change; unrelated work is split.
- Every history rewrite is lease-protected; raw force-push never occurred.
- Review threads, approvals, mergeability, and checks were re-audited after any rewrite.
- Labels: one kind plus all material areas.
- A stack landed through the native stack feature, every selected PR reported merged, and branches were deleted only after merged-state verification.
