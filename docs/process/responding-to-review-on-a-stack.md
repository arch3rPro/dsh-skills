# Responding to Review on a Stack

## What it does

Acts on review comments that span several PRs in a dependent stack (`A ← B ← C …`). It owns **review-fix placement and propagation**.

**The defining constraint:** a fix lands on the PR that **introduced** the issue, then flows up-stack — never downstream, where the introducing PR ships the unfixed code and the fix is hidden from its reviewer.

## When to reach for it

- **Invocation mode.** Model-invoked: when review comments span several stacked PRs.
- **Trigger boundary.** This skill owns the review-response; [pr-history-hygiene](./pr-history-hygiene.md) owns linkage checks and landing, and [code-review](./code-review.md) owns finding the issues.

## Ground rules

- One worktree per PR branch; the platform's stack object (not the branch chain) is authoritative.
- A fix lands on the **introducing** PR, then flows up-stack.
- Each review fix stays a distinct commit; amend only your own unpushed, unreviewed work.
- Rewrites are lease-protected; raw force is forbidden.

## Resolving comments

1. Triage every comment on the merits — a reviewer flagging the right symptom can still misdiagnose the cause.
2. Map each accepted finding to its originating PR and fix it there.
3. Propagate up-stack by merge-forward or a validated cascading rebase.
4. Trust but verify delegated fixes — re-run gates on the actual tree; prove a guard fails on unfixed code.
5. Reply in the review thread, stating the fix and the commit that carries it.
6. After any rewritten push, re-audit threads, approvals, mergeability, and checks.

## Common questions

**Why not fix the top PR?** Because the introducing PR ships the unfixed code and hides the fix from its reviewer. Fix at origin, then propagate.

**Is rebasing allowed after review?** Yes, but the rewrite must be lease-protected, and you must re-audit threads, approvals, and checks afterward — a force-pushed OID is not current evidence.

## It's working if

- Every fixed PR's current diff carries the correction at the introducing layer.
- The stack is platform-recognized; each child's diff against its parent shows only that child's changes.
- Threads, approvals, mergeability, and checks were re-audited after every rewrite.
- Gates pass on every affected PR, not just the top.

## Where it fits

The review-response half of the process category, between [code-review](./code-review.md) (finding issues) and [pr-history-hygiene](./pr-history-hygiene.md) (landing the stack).
