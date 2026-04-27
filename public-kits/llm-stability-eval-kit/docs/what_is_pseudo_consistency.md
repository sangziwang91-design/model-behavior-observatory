# What Is Pseudo-Consistency?

Pseudo-consistency is a behavioral pattern where an LLM appears stable on the surface while its answer path changes across repeated outputs.

The answer may use similar wording, structure, or conclusion, but the underlying emphasis drifts.

## Signs

- Same final answer, different evidence basis
- Similar structure, weaker caveats over time
- Stable tone, unstable risk boundary
- Repeated confidence, changing assumptions
- No visible contradiction, but gradual loss of specificity

## Why it matters

In real applications, users often trust repeated similar outputs.

But if the model's evidence structure or boundary condition changes silently, the system may be less reliable than it appears.

## Minimal test

1. Ask the same prompt 5-20 times.
2. Record each output.
3. Compare final decision, caveats, assumptions, evidence, and risk framing.
4. Mark whether surface similarity hides internal drift.

## Public-safe definition

Pseudo-consistency does not claim access to model internals.

It is an observable output-level pattern.
