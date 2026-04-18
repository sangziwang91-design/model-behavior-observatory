# F13 — Confidence–Structure Gap

The confidence–structure gap describes a divergence:

> the model's confidence and structural completeness
> increase faster than the security of the underlying evidence.

## What is being compared

This finding compares three layers:

1. confidence (how certain the answer sounds)
2. structure (how complete and organized the explanation is)
3. grounding (how securely the claims are supported)

The gap appears when (1) and (2) rise faster than (3).

## Why this matters

Users often rely on signals like:

- clarity
- completeness
- fluent reasoning
- confident tone

These signals are useful in many contexts,
but they can be misleading when grounding is weak.

A highly structured, confident answer can feel more trustworthy
than a cautious, fragmented one,
even when the latter is more faithful to the actual uncertainty.

## Where the gap shows up

The gap is especially visible in situations involving:

- newly introduced concepts
- weakly verified entities
- cross-domain synthesis
- speculative or hypothetical reasoning

In these cases, the system can produce:

- coherent multi-step explanations
- consistent terminology
- stable framing

without proportionally strong evidence.

## What this finding does not claim

It does not claim that confidence or structure are inherently wrong.
It does not claim that all confident answers are unreliable.

It highlights a specific risk pattern:

> confidence and structure can scale independently of grounding.

## Why this matters for interpretation

When reading model outputs, it is useful to separate:

- how well the answer is constructed
- how well the answer is supported

These are not always aligned.

## Disclosure boundary

This page is a public-safe finding note.
It does not expose internal metrics, scoring formulas, or protocol details.
