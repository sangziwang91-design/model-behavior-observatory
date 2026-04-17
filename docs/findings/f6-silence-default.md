# F6 — Silence Default

## Public finding

When uncertainty handling fails, a model often fills the gap instead of holding the boundary.

This does not always appear as a dramatic falsehood.
Often it appears as a smoother, more helpful, more complete-sounding answer than the evidence actually justifies.

## Why it matters

At the public surface, users usually do not see the moment where a model had another option:

- stop
- mark uncertainty clearly
- hold the boundary
- refuse to over-structure the answer

Instead, the model may continue speaking as if the safest move is to keep the answer going.

That continuation pressure is what this finding refers to as a **silence default**.

## What the pattern looks like

The pattern often appears as one or more of the following:

- uncertainty is compressed instead of made explicit
- missing evidence is replaced by plausible structure
- the answer keeps expanding instead of pausing
- boundary language appears late, weakly, or not at all

## Why "silence" matters here

The issue is not literal absence of words.
The issue is the absence of a needed boundary signal.

What is missing is not output.
What is missing is a clear stop condition.

## Public interpretation

A model can fail safely in two very different ways:

- by stopping too early
- by continuing too smoothly under uncertainty

The second failure is often harder for ordinary users to notice, because it still looks helpful.

## What this repository observes

This repository does **not** treat the silence default as proof that every long answer is unreliable.
It treats it as a recurring public-facing behavior pattern:

> when boundary retention weakens, the model often fills the gap before it marks the gap.

## What this finding does not claim

This finding does **not** mean:

- the model should always refuse
- every continuation is unsafe
- silence is always better than explanation

It means only that under uncertainty pressure, continued explanation can become a substitute for genuine boundary holding.

## Public reading rule

When an answer keeps flowing under uncertain conditions, the right question is not only:

- "Is this useful?"

It is also:

- "Did the model clearly show where it should have stopped?"
