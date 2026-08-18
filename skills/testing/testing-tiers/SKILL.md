---
name: testing-tiers
description: Choose the right test tier for a change and keep the suite meaningful — unit, integration, real-entry-path, end-to-end, and snapshot tiers; test the real entry path rather than a hand-built harness; verify the world rather than the component's self-report; prefer the real implementation over a mock; and treat line coverage as necessary, never sufficient. Use when writing, planning, or reviewing tests, deciding what a change needs to be tested, or when a suite is green but the product is broken.
---

# Testing Tiers

A decision discipline for keeping a test suite green **and** meaningful. A green suite that proves nothing is worse than a failing one you trust — this skill keeps the two apart. It applies to any project with tests; the tier names below generalize across frameworks (the concrete names like "vitest" or "jest" are placeholders for whatever the project uses).

**The defining constraint:** tests must exercise the **real entry path** and **verify the world**, not the component's self-report. A mock-heavy unit suite can be 100% green while the shipped behavior is broken — the failure mode this skill exists to prevent.

## The tiers, and when each applies

Pick the shallowest tier that would actually fail for the change's regression:

| Tier | What it proves | Applies when |
| --- | --- | --- |
| **Unit** | A function/class behaves per its contract | The behavior is confined to one module |
| **Integration** | Several modules cooperate | A shared contract or wiring changes |
| **Real entry path** | The shipped entry (loader, binary, server, worker) actually works | A product-visible plugin, entrypoint, or composition changes |
| **End-to-end** | The assembled system works against a real external boundary | The change touches provider, network, or cross-system behavior |
| **Snapshot** | External contract / presentation output stays stable | Model-, protocol-, or human-visible output changes |

Match evidence to the surface: focused unit tests for behavior, snapshots for model or user-visible output, real-entry-path tests for shipped entrypoints, and e2e for provider behavior. Never default to the full suite for a narrow change — run the smallest set that covers the diff, and let CI own exhaustive coverage.

## Test the real entry path

A product-visible change requires a **non-unit, real-composition test** — boot the actual loader / binary / server / worker through its real entry point. A hand-built harness that calls the component directly proves plumbing, not that the shipped entry works. Two traps:

- **A guard only guards if the regression actually fails it.** For a plugin without injection, a loader smoke can stay green when a default export replaces the required named exports — add an explicit assertion that the invalid form is absent, and prove it: introduce the regression, watch it go red, revert.
- **"Real entry path" means the published artifact.** A package `bin` runs the built output under plain runtime, not through a source-mode shim that masks resolution or swallow-failure bugs.

## Verify the world, not the self-report

An e2e assertion re-runs the command or re-reads the file **externally**; asserting on the component's own output lets a cheating component pass. Assert untouched files are byte-identical. Tests own their resources: create the harness in the test, dispose in teardown even on failure or retry.

## Prefer the real implementation over a mock

Mock only the expensive or non-deterministic boundary — an external API, the network, the clock. Keep everything downstream real. A hand-rolled stand-in proves the bridge moves bytes, not that the shipping behavior behaves as asserted. When you must mock the model or API, use a scripted stand-in with the **real** downstream code.

## Coverage is necessary, never sufficient

Line coverage proves lines ran, not that the feature works as shipped. An uncovered line is often dead code the gate is flagging for deletion — delete it rather than bolt on a test for it. Treat a coverage bar as a floor, and put the real verification burden on behavioral tests that would fail for the intended regression.

## Tests describe behavior, not correctness

Tests pin behavior. When behavior intentionally changes, the tests change with it — do not preserve a "correct" test for obsolete behavior, and explain the behavior change in the change description.

## Workflow

1. **Name the surface.** What changed: a module, a contract, an entrypoint, a provider boundary, or visible output?
2. **Pick the shallowest tier** from the table that would fail for the change's regression.
3. **Route it through the real entry path** if it is product-visible; mock only the external/nondeterministic boundary.
4. **Write the assertion against the world** — external state, a re-run, a re-read — not the component's report.
5. **Run the smallest set** that covers the change; don't reflexively run the full suite.

## Completion criteria

- Every product-visible change has a real-entry-path test, not a hand-built harness.
- Every assertion verifies external state or a re-run/re-read, not the component's self-report.
- Mocks exist only at expensive or non-deterministic boundaries; everything downstream is real.
- The shallowest tier that would catch the regression is the one used; the full suite is CI's job.
- Behavior changes updated their tests in the same change.
