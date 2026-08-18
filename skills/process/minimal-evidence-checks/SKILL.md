---
name: minimal-evidence-checks
description: Run the smallest set of checks that covers an outgoing change before pushing, committing, or claiming checks pass — select evidence by the surface the diff touches, never reflexively run the full suite, and fix or explain a failure rather than pushing and hoping CI differs. Use before push, force-push, marking ready for review, or claiming checks pass.
---

# Minimal Evidence Checks

A discipline for running the **relevant** local evidence before a push, without reflexively running the full repository suite. It applies to any repo with checks and a CI system: CI owns exhaustive coverage and the platform matrix; you own the narrow evidence that the outgoing diff would fail.

**The defining constraint:** match the evidence to the surface. Every behavior change needs the narrowest available check that would fail for its regression — nothing more, and nothing less. Repeating a passing check merely because a commit follows is waste.

## Inspect the outgoing change first

Before selecting checks, know the complete scope of what changed:

1. Confirm the checkout and branch.
2. Determine the base (the merge target, branch parent, or remote head) and inspect the diff against it.
3. Account for staged, unstaged, and untracked paths separately.

After a base merge or retarget, re-inspect the combined scope and reassess which checks it can affect.

## Select evidence by surface

There is no universal baseline. Choose the narrowest check that would fail for the change's regression:

| Surface | Relevant evidence |
| --- | --- |
| **Behavior in one module** | The focused test file or test name for that module |
| **A shared contract** | That module's tests plus the adjacent modules that consume it |
| **Docs, decisions, comments** | The documentation/formatting check; full lint when the workflow requires it |
| **Model-, UI-, or user-visible output** | The focused snapshot or scenario that owns that output |
| **Packaging, exports, build config, entrypoints** | The build, hygiene checks, and the owning built-artifact smoke |
| **External provider or cross-system behavior** | The relevant end-to-end target when credentials are available |

Do not manually repeat a passing check just because commit or push follows — in particular, do not re-run a typecheck immediately before pushing if a pre-push hook already runs it.

## Focus coverage on the affected source

Test selection and coverage measurement are separate concerns. When coverage matters, name both the owning tests and the source whose coverage those tests must prove. If the owning tests are unclear, discover candidates from the dependency graph, then inspect them before treating the run as evidence. Never narrow the coverage scope or lower thresholds merely to hide an uncovered affected file.

## Full rehearsal only when it earns it

Run the complete local approximation only when explicitly requested, while diagnosing a CI failure, or when the change spans the repo so broadly that no narrower set is credible. Otherwise the smallest set is the discipline.

## Handle failures

If a relevant check fails before an ordinary push, **stop and fix or explain the blocker**. Do not push and hope CI differs. If a failure looks environment-specific, prove it: record the exact command, the failing test, and the platform-specific mismatch; confirm the non-platform evidence; and prefer fixing cross-platform nondeterminism when the check is required.

## Protect history-rewriting pushes

Rebasing is allowed for your own feature branches. Before a history rewrite:

- Fetch the current remote branch and record its exact head.
- Publish with **lease-protected force-push** (e.g. `--force-with-lease=<branch>:<observed-head>`) so a concurrent update aborts the push. **Raw force-push is never allowed.**
- After any rewritten push, re-fetch the live heads and re-audit review threads, approvals, mergeability, and checks — commit hashes from before the rewrite are not current evidence.

## Workflow

1. **Inspect the outgoing change** against a verified base; know the full scope.
2. **Select the smallest evidence set** that covers the surfaces the diff touches.
3. **Run it once.** Do not repeat a passing check for commit or push.
4. **Fix or explain any failure** before pushing.
5. **For a history rewrite**, use lease-protected force-push and re-verify after.

## Completion criteria

- The outgoing diff's scope is inspected against a verified base, not guessed.
- Every surface the diff touches has its narrowest check; nothing broader than needed was run.
- A passing check was not repeated merely because commit or push followed.
- A failing relevant check was fixed or explained before the push — never pushed on hope.
- Any history rewrite used lease protection; heads and review state were re-audited after.
