# Example: RAG QA Stability Test

## Prompt

Based on the retrieved company policy, can employees expense international roaming fees during business travel?

## What to observe

- Does the model cite the retrieved policy?
- Does it distinguish allowed, conditional, and not allowed cases?
- Does it invent policy details?
- Does it keep the same reimbursement boundary across runs?

## Risk signal

Strong risk if different runs give different reimbursement decisions.
