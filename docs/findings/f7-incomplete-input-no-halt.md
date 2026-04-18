# F7 · Incomplete Input, No Halt

## Finding

When task structure is incomplete, a model may continue execution instead of pausing to request missing information.

This matters because the failure is not primarily about factual error.
It is about **process error under incomplete input**.

In plain terms:

> The model keeps going when a stop condition would be safer.

## Core observation

A model can often **describe** the correct policy under incomplete input:

- confirm whether the full task has been loaded
- stop when coverage is incomplete
- request the missing structure before execution

But describing that policy is not the same as enforcing it.

This finding points to a practical mismatch:

> **Policy expression can remain intact while execution behavior still fails to halt.**

That mismatch matters because the answer may still sound careful, coherent, and even epistemically modest.
The visible answer can look acceptable while the execution layer has already made the wrong move.

## Why this finding matters

A process-level failure can hide behind a content-level success.

The model may:

- sound careful
- preserve uncertainty in wording
- avoid direct fabrication
- still continue execution when it should first stop and confirm task completeness

This creates a visibility problem:

- the **content layer** may still look reasonable
- while the **execution layer** has already failed

## Public-safe interpretation

This finding does **not** claim that every model always behaves this way.
It defines a public evaluation pattern that can be checked across systems:

1. provide a structured multi-part task
2. weaken or fragment the readable input surface
3. ask the model to proceed only after confirming full task coverage
4. observe whether the model:
   - pauses and requests completion, or
   - continues and tries to reconstruct the missing structure

The second behavior is the point of concern.

## Public observation status

In repeated public-safe probes, this pattern does not appear as a one-off artifact.
A recurring outcome is that models often distinguish between:

- what a system **should** do under incomplete input, and
- what a model **tends** to do in practice under incomplete input.

This does not justify a universal claim.
It does support treating the phenomenon as a stable behavior pattern worth testing directly.

## Minimal public reproduction logic

A public-safe reproduction pattern is:

- use a multi-part test sheet
- make the model rely on partial retrieval or fragmented reading
- require it to answer only after confirming full task coverage
- compare:
  - what the model says it should do under incomplete input, and
  - what it actually does under incomplete input

If the stated policy is "stop and confirm" but the execution behavior is "continue and reconstruct," that gap is itself the finding.

## What this is not

This is not a jailbreak claim.
This is not a safety bypass claim.
This is not a claim about hidden chain-of-thought.
This is not a claim that every incomplete-input case should always hard-stop.

It is a public observation about **halt behavior under incomplete task structure** and about the gap between **policy expression** and **execution behavior**.

## Boundary note

This page does not publish internal thresholds, scoring rules, or private control logic.
It only publishes a public-facing observation pattern.

## Related themes

- premature structure under uncertainty
- pseudo-consistency
- process compliance versus answer quality
- boundary retention under incomplete input
- policy-expression versus execution mismatch
