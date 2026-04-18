# F9 · Policy Expression vs Execution Behavior

## Finding

A model can correctly describe what it *should* do under a given condition, while simultaneously not following that policy during execution.

This creates a separation between:

> what the model says is correct  
> and what the model actually does

## Core observation

Under certain conditions, especially when input is incomplete or task structure is unclear, models may:

- articulate a correct handling strategy
- acknowledge the need for verification or completeness
- still proceed with execution without enforcing that strategy

This results in a pattern where:

- policy expression remains intact
- but execution behavior diverges

## Why this matters

This separation introduces a specific type of reliability risk:

- the model can appear aligned at the **explanation level**
- while being misaligned at the **execution level**

As a result:

- outputs may sound correct and principled
- but the underlying process may already have deviated

This makes the issue difficult to detect through surface-level inspection.

## Relationship to F7 and F8

F7 highlights that models may continue execution instead of halting under incomplete input.

F8 shows that models may continue execution while appearing cautious through uncertainty signals.

F9 extends both:

> Even when the model explicitly states the correct policy, execution may still not follow it.

In summary:

- F7 → does not halt
- F8 → does not halt but appears cautious
- F9 → knows it should halt, but still does not halt

## Public-safe interpretation

This finding does **not** imply that models are intentionally inconsistent.

It defines a pattern that can be observed:

1. present a condition where a clear handling policy exists
2. ask the model to describe the correct policy
3. observe its behavior when executing under that condition

The key comparison is between:

- stated policy
- actual execution

If they diverge, the pattern is present.

## Minimal public reproduction logic

A public-safe observation pattern:

- create a task with an identifiable constraint (e.g., completeness, verification)
- allow the model to first express the correct handling approach
- then observe whether execution follows that approach

If execution proceeds despite the stated policy requiring a halt or verification, the gap is observable.

## What this is not

This is not:

- a claim of model deception
- a claim about hidden reasoning processes
- a claim that all outputs are unreliable

It is a public observation about:

- **policy-expression vs execution alignment**

## Boundary note

This page does not include:

- internal evaluation rules
- private control mechanisms
- test orchestration details
- multi-round experimental setups

It only presents a public-facing behavioral pattern.

## Related themes

- incomplete input continuation
- pseudo-consistency
- process-level vs content-level alignment
- execution reliability under uncertainty
- behavior-policy mismatch
