# F7 · Incomplete Input, No Halt

## Finding

When task structure is incomplete, a model may continue execution instead of pausing to request missing information.

This matters because the failure is not primarily about factual error.
It is about **process error under incomplete input**.

In other words:

> The model keeps going when a stop condition would be safer.

## Why this finding matters

A system can sound careful, coherent, and even epistemically modest while still making a process mistake.

That process mistake is:

- not confirming that the full task has been loaded
- not stopping when the input surface is incomplete
- continuing to answer anyway

This creates a visibility problem:

- the **content layer** may still look reasonable
- while the **execution layer** has already failed

## Public-safe interpretation

This finding does **not** claim that every model always behaves this way.
It shows a public evaluation pattern that can be checked across systems:

1. provide a structured multi-part task
2. weaken or fragment the readable input surface
3. observe whether the model:
   - pauses and requests completion, or
   - continues and tries to reconstruct the missing structure

The second behavior is the point of concern.

## What this is not

This is not a jailbreak claim.
This is not a safety bypass claim.
This is not a claim about hidden chain-of-thought.

It is a public observation about **halt behavior under incomplete task structure**.

## Minimal public reproduction logic

A public-safe reproduction pattern is:

- use a multi-part test sheet
- make the model rely on partial retrieval or fragmented reading
- require it to answer only after confirming full task coverage
- check whether it halts when task coverage is incomplete

A model that continues without that confirmation exposes a process-level weakness.

## Boundary note

This page does not publish internal thresholds, scoring rules, or private control logic.
It only publishes a public-facing observation pattern.

## Related themes

- premature structure under uncertainty
- pseudo-consistency
- process compliance versus answer quality
- boundary retention under incomplete input
