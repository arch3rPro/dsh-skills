# Postmortem

## What it does

Writes a **backward-looking failure record** — what broke, the mechanism, why every safety net missed it, and the concrete guardrails added so the same class of bug fails loudly next time.

**The defining constraint:** a postmortem is retrospective and failure-specific. It is not an incident log, not a blame report, and not a decision record.

## When to reach for it

- **Invocation mode.** Model-invoked: after a hard incident or regression, or when deciding whether a failure retrospection is owed.
- **Trigger boundary.** Use it when a failure needs a durable lesson. For a *forward-looking* design decision (and its alternatives), use [decision-records](./decision-records.md) instead — the two complement each other.

## When one is owed

Write one when a bug is **subtle** (non-obvious mechanism), **systemic** (the reason it escaped every safety net is structural), and **costly to rediscover** (it cost real debugging time and would again). A trivial fix with an obvious cause does not earn one.

## Structure

Open with an **executive summary** a busy reader absorbs in thirty seconds — what broke, root cause in plain terms, why it escaped, durable lesson. Then: Summary → Timeline → Root cause → Guardrails. The interesting part is *why the process let it through*, not the one-line fix.

## Common questions

**Is this an ADR?** No. A postmortem records a failure that already happened; a decision record records a choice you are making now. If the postmortem motivates a future choice, record that separately and cross-link.

**Does every bug need one?** No. Only subtle, systemic, costly-to-rediscover failures. The rest get a fix, not a postmortem.

## It's working if

- It opens with an executive summary absorbable in thirty seconds.
- Root cause states the mechanism, not the nearest symptom.
- Guardrails are concrete and each links to the artifact that enforces it.
- It is retrospective, not an incident log or a decision record.

## Where it fits

The retrospective half of the process category, complementing [decision-records](./decision-records.md) (the forward-looking half). Its debugging counterpart is systematic debugging (reproduce → hypothesize → locate); this skill captures the durable lesson after the fact.
