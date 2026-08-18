---
name: defensive-patterns
description: Defensive-programming patterns to apply when writing or reviewing lifecycle, concurrency, subprocess, teardown, error-reporting, or untrusted-IO code. Use when a change touches async setup or teardown, callbacks, spawned processes, workers, event listeners, disposal, error aggregation, temp files, or anything receiving untrusted input — and when reviewing a PR that touches any of those.
---

# Defensive Patterns

A catalogue of bug-class rules distilled from defects that actually shipped. Each pattern is one class of failure, stated as the rule that prevents its recurrence. Read this before writing lifecycle, concurrency, subprocess, teardown, or error-reporting code — these are the places where "it usually works" hides a reproducible race.

**The defining constraint:** these rules are about *settlement* — the honest, complete reporting of an outcome — and *ownership* — knowing who owns a resource until it is fully gone. Most concurrency bugs are a settlement or ownership violation in disguise.

This is guidance, not a script. Each pattern names a failure mode and the positive rule that avoids it; apply the ones your code touches. Patterns cluster into two groups — **reporting** and **ownership** — with one **untrusted-IO** trio.

## Reporting — tell the whole truth about an outcome

### Report orthogonal outcomes independently

A result can be several things at once. A process can time out **and** exit 0 because it trapped the signal; a call can fail **and** leave valid partial state. Surface each independent fact (`timedOut`, `signal`, `exitCode`) on its own field or branch — never nest one flag's report inside another's branch, or a caller reads a cut-short run as a clean success. When two facts can both be true, the code that reports only one is lying.

### Honor public contracts on BOTH sides

When an implementation receives several representations of one outcome, **normalize them before returning through the public API**. If a provider may signal failure by throwing *or* by emitting an error token, the public runtime exposes model-request failures as exactly one form; middleware and caller defects remain thrown. Consumers must never guess whether a caught exception came from the provider, a wrapper, or their own assembly. Document the normalized contract where the type is defined, and exercise every source form through the real consumer.

### Contain callback exceptions in the dispatcher

A user-supplied listener that throws must not reject the promise it runs inside, and must not starve the listeners after it. Wrap the dispatch loop in try/catch and log. One bad subscriber never breaks core lifecycle.

## Ownership — know who owns a resource until it is fully gone

### Async state is not synchronous state

A background job's completion races turn boundaries; a close fires for both EOF and disposal; several queued operations may share one `running` interval. Never treat a status flag or an idle signal as the result of one specific operation — cancellation or disposal can discard unstarted items. A caller that truly owns a run must define its interval explicitly (for example, from its durable receipt through the next whole-agent idle) and describe any selected output as interval-wide, not causally attributed to one input. The guard cuts both ways: if the awaited transition can never occur, the wait hangs, so handle the "nothing to wait for" branch explicitly.

### Dispose must reach quiescence, not just request it

A teardown that issues kills or aborts but returns before the work stops leaves orphans. Make cleanup async and await the children's exit (kill → await the done signal). Close listener and notification registries **before** killing, so late completions stay silent. A dispose that returns before the work has actually stopped has not disposed anything.

## Untrusted IO — never give hostile input the ambient world

### Scrub the environment

Spawned commands get a scrubbed environment: drop anything matching `*KEY*`, `*SECRET*`, `*TOKEN*`, `*PASSWORD*` so harness credentials cannot leak into output, `env`, or spill files.

### Use private, unpredictable paths

Temp and spill files use a private (0700) directory, random names, and exclusive owner-only opens (`'wx'`, `0o600`). Predictable world-readable paths invite symlink races and disclosure.

### Unlink link-shaped paths

A path that may be a symlink or junction is removed by checking `isSymbolicLink()` then `unlink` — unlink deletes only the link and refuses a real directory, so it never follows the link into its target. Recursive deletion can descend through a junction into its target; reserve recursive removal for known real directories.

## Workflow

1. **Scope the exposure.** For the code in hand, name which patterns apply: lifecycle/teardown → ownership group; error aggregation → reporting group; anything spawning or writing files → untrusted-IO trio.
2. **Trace settlement.** For every async or fallible path, ask: *what are all the independent facts a caller needs to know, and is each reported without being nested in another?*
3. **Trace ownership.** For every resource created, name the owner and the exact point it is fully gone. If a status can be read before the work is done, the ownership rule is violated.
4. **Apply the positive rule, not a workaround.** Each pattern is stated as what *to do*; if you catch yourself reasoning "it's fine because only we call this", the defensive posture is lost.

## Completion criteria

- Every async/fallible path reports each independent outcome on its own branch or field.
- Every resource has one owner and a defined quiescence point that is awaited.
- Every dispatched callback is contained so one subscriber cannot break the rest.
- Every spawned command and temp file treats its input as hostile: scrubbed env, private random paths, exclusive owner-only opens, link-safe removal.

## Companion: verify the world, not the self-report

When these patterns guard a behavior you also test, assert externally: re-run the command or re-read the file rather than trusting a status the code reported. A "success" reported by the very component being tested is not evidence. Tests own their resources too — create in the test, dispose in `afterEach`, even on failure or retry.
