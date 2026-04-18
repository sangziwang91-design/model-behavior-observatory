# F11 — Pseudo-Consistency

Pseudo-consistency names a misleading stability pattern:

> a system appears consistent across rounds,
> but the internal path is not genuinely stable.

What stays stable is often the surface shape,
not the underlying evidential grounding.

## Why this matters

Users often treat repeated similarity as a sign of reliability.
If a model gives answers that sound aligned in tone, structure, and conclusion,
it is easy to assume the model has reached a trustworthy stable state.

That assumption can fail.

A model may preserve:

- the same explanatory posture
- the same confidence level
- the same narrative frame
- the same apparent conclusion

while still shifting:

- what it is implicitly assuming
- how it is mapping the object to nearby concepts
- which gaps it is silently filling
- where the boundary between verification and interpretation is placed

## What makes this pseudo-

The pattern becomes pseudo-consistency when repetition is driven more by structural convergence
than by stable evidential handling.

In that case, the answer looks steady,
but the steadiness is partly produced by:

- format lock
- familiar-framework reuse
- repeated narrative compression
- pressure toward completion

The output can look disciplined while remaining weakly grounded.

## What this finding is trying to separate

Pseudo-consistency helps separate two different things:

1. real stability
2. repeated plausibility

Real stability would suggest that the system is handling the same uncertainty boundary
in a meaningfully similar way.

Pseudo-consistency suggests that the system is repeatedly returning
to a similar-looking answer pattern,
without proving that the underlying judgment process is equally stable.

## Why this matters for evaluation

A repeated answer is not automatically a robust answer.
A stable-looking answer is not automatically a boundary-honest answer.

For this reason, behavioral evaluation should not stop at:

- whether answers look similar
- whether the structure remains coherent
- whether the model sounds settled

It should also ask whether the model is preserving the same uncertainty discipline.

## Correct reading boundary

This page does not claim direct access to hidden internal computation.
It does not claim that all repeated patterns are deceptive.
It names a public-facing behavioral risk:

> apparent stability can be stronger than actual grounding.

## Disclosure boundary

This is a public-safe finding note.
It does not disclose protected scoring details, hidden protocol variants, round-level raw traces, or reconstruction-relevant internal logic.
