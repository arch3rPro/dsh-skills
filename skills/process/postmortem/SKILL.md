---
name: postmortem
status: beta
description: "Write a backward-looking failure record — executive summary, timeline, root cause, and guardrails — when a bug was subtle, systemic, and costly to rediscover. Use after a hard incident or regression, or when deciding whether one is owed. It records what broke and why it escaped; complement it with decision-records, which record forward-looking decisions."
---

# Postmortem

A **postmortem** is a backward-looking record of a failure: what broke, the mechanism, why every safety net missed it, and the concrete guardrails added so the same class of bug fails loudly next time. It is the complement of [decision-records](./decision-records.md), which records a forward-looking decision and its alternatives.

**The defining constraint:** a postmortem is retrospective and failure-specific — it is not an incident log, not a blame report, and not an ADR. Its job is to make the *mechanism* explicit and to leave guardrails, so the next occurrence fails loudly instead of silently.

## When one is owed

Write a postmortem when a bug is:

- **Subtle** — the mechanism is non-obvious and a careful engineer would re-derive it the hard way;
- **Systemic** — the reason it escaped every safety net is structural, not a one-line mistake;
- **Costly to rediscover** — it cost real debugging time, and would cost it again.

A trivial one-line fix with an obvious cause does not earn one. When unsure, ask whether the next engineer would hit the same wall — if yes, write it.

## Structure

Open with an **Executive summary**: one short paragraph a busy reader absorbs in thirty seconds — what broke, the root cause in plain terms, why it escaped, and the durable lesson. Then the detail:

1. **Summary** — what happened, in plain terms.
2. **Timeline** — the sequence that led to the failure and its discovery.
3. **Root cause** — the mechanism, stated precisely, not the nearest symptom.
4. **Guardrails** — the concrete measures added so the same class fails loudly: tests, agent rules, decision records, or process changes. Link each guardrail to the artifact that carries it.

The interesting part is *why the process let it through*, not the one-line fix. Keep the focus there.

## Not a decision record

A postmortem records a failure that already happened; a decision record records a choice you are making now. Do not fold the two: if the postmortem motivates a future decision, record that decision separately in a decision record and cross-link. Keep the retrospective and the forward-looking records distinct.

## Workflow

1. **Decide if one is owed** — subtle, systemic, and costly to rediscover? If not, skip.
2. **Write the executive summary** first, so the lesson stands alone.
3. **Record summary, timeline, and root cause** — the mechanism, precisely.
4. **Add guardrails** and link each to the artifact that carries it (test, rule, decision record).
5. **Cross-link** any decision the postmortem motivates into a decision record.

## Completion criteria

- The postmortem opens with an executive summary a busy reader can absorb in thirty seconds.
- Root cause states the mechanism, not the nearest symptom.
- Guardrails are concrete and each links to the artifact that enforces it.
- It is retrospective and failure-specific — not an incident log, a blame report, or a decision record.
- Any forward-looking decision it motivates lives in a separate decision record, cross-linked.
