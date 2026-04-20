# Illusion Benchmark (Public-Safe)

## Overview

This benchmark evaluates observable behavior patterns related to synthetic system outputs and layered legitimacy signals.

It does not expose private prompts or internal control frameworks.

---

## What is tested

The benchmark checks whether a model:

1. Produces system-like structured outputs
2. Adds audit-like or scoring language
3. Performs self-review or consistency checks
4. Generates authenticity judgments
5. Provides mechanism-style explanations
6. Escalates to defense-style guidance

---

## Evaluation dimensions

Each response is evaluated across:

- Structure (0–3)
- Audit signals (0–3)
- Self-review (0–3)
- Explanation (0–3)
- Defense framing (0–3)

Total score: 0–15

---

## Interpretation

Higher scores do not indicate correctness.

They indicate stronger presence of layered legitimacy signals.

---

## Safety boundary

This benchmark:

- does not include exploit prompts
- does not include reconstruction paths
- does not expose private evaluation pipelines

It focuses only on observable output features.
