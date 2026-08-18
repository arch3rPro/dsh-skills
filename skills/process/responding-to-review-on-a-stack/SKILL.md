---
name: responding-to-review-on-a-stack
status: beta
description: "Respond to code review across a dependent PR stack — fix on the PR that introduced the issue, propagate the fix up-stack, keep each review fix a distinct commit, lease-protect any rewrite, and re-audit threads, approvals, and checks after every rewrite. Use when review comments span several stacked PRs."
---

# Responding to Review on a Stack

A discipline for acting on review comments that span several PRs in a dependent stack (`A ← B ← C …`). It owns **review-fix placement and propagation**; [pr-history-hygiene](./pr-history-hygiene.md) owns linkage checks and landing, and [code-review](./code-review.md) owns finding the issues.

**The defining constraint:** a fix lands on the PR that **introduced** the issue, then flows up-stack — never downstream, where the introducing PR ships the unfixed code and the fix is hidden from its reviewer.

## Ground rules

- **One worktree per PR branch.** Each PR's fixes happen in that PR's own worktree; parallel fixes never share a checkout.
- **The stack object is authoritative.** Base branches establish the expected dependency order; the platform's stack metadata proves it is recognized. Do not treat a matching branch chain as an official stack without checking that metadata.
- **A fix lands on the introducing PR, then flows up-stack.** When a comment on PR `B` points at code `B` introduced, fix it on `B` and propagate into `C` — even if `C` also carries the file.
- **Each review fix remains a distinct commit.** A later rebase may change its OID, but do not amend a reviewed fix out of the branch history. Amend only your own not-yet-pushed, not-yet-reviewed work.
- **Choose merge-forward or rebase deliberately.** Both are allowed after review. A rewritten push must be lease-protected and must abort rather than overwrite a concurrently advanced remote head; raw force is forbidden.

## Resolve comments through the stack

1. **Triage every comment on the merits** before acting: verify the claim against the code — a reviewer flagging the right symptom can still misdiagnose the cause.
2. **Map each accepted finding to its originating PR** and fix it there.
3. **Propagate the fixed layer** through every affected child in order — merge-forward (merge the fixed parent into the child, validate, continue upward) or a native cascading rebase (validate the rewritten layers, then publish).
4. **Trust but verify delegated fixes** — a sub-agent's report describes intent, not necessarily what landed. Re-run the gates on the actual tree; prove a regression guard fails on the unfixed code.
5. **Reply in the review thread**, not as a top-level comment, stating the fix and the current commit or head that carries it.
6. **After any rewritten push**, re-read unresolved threads, approvals, mergeability, and checks. A force-pushed OID or outdated inline anchor is not current evidence that the finding remains resolved.

## Workflow

1. **Ground** — one worktree per PR; confirm the stack object, not just the branch chain.
2. **Triage** — verify each comment on the merits; accept or rebut.
3. **Fix at origin** — land each accepted fix on the introducing PR, as a distinct commit.
4. **Propagate** — move the fixed layer up-stack via merge-forward or a validated cascading rebase.
5. **Verify** — re-run gates on every affected PR; re-audit threads, approvals, and checks after any rewrite.
6. **Reply** — state the fix and its commit in the review thread.

## Completion criteria

- Every fixed PR's current diff contains the intended correction at the layer that introduced the issue.
- The stack is recognized by the platform and each child's diff against its parent shows only that child's changes.
- Unresolved threads, approvals, mergeability, and checks were re-audited after every rewritten push.
- The relevant gates pass on every affected PR, not just the top.
