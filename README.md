# Model Behavior Observatory

AI often sounds confident when it should be uncertain.

This repository documents a public evaluation surface for making that mismatch visible.

## Start here

If you only read one page first, read:

- `docs/start-here.md`

Choose the path that fits your reading time and depth:

- **General reader (5–10 minutes)** → start with `docs/start-here.md`, then `docs/findings/what-we-found.md`, then `docs/overview.md`
- **Research-facing reader (10 minutes)** → read `docs/start-here.md`, then `docs/known-limits.md`, then `docs/scope-and-disclosure.md`, then `docs/reports/20-round-ab-snapshot.md`, then `docs/reports/multi-model-behavioral-response-analysis-public-safe.md`
- **Concept / meta-layer reader (10 minutes)** → read `docs/start-here.md`, then `docs/studies/v1-7-public-note.md`, then `docs/studies/gbs-meta-layer-concept-note.md`

## What this repository shows

This is a public-facing evaluation window for model behavior.

It focuses on one practical problem:

> Models can produce high-confidence outputs even when reliable truth is not securely available.

The work here does **not** claim to fix that problem.
It makes the problem easier to see, compare, and discuss.

## Current public surface

Currently available public materials include:

- `README.md` — repository entry and disclosure boundary
- `docs/start-here.md` — guided public reading map for different readers
- `docs/findings/what-we-found.md` — public findings summary
- `docs/findings/f1-confidence-gap.md`
- `docs/findings/f2-structure-outruns-evidence.md`
- `docs/findings/f3-premature-legitimacy.md`
- `docs/findings/f4-observation-not-remediation.md`
- `docs/findings/f6-silence-default.md`
- `docs/findings/f7-incomplete-input-no-halt.md`
- `docs/findings/f8-pseudo-consistency.md`
- `docs/findings/f9-policy-vs-execution-gap.md`
- `docs/findings/index.md`
- `docs/overview.md`
- `docs/forward-path.md`
- `docs/known-limits.md`
- `docs/scope-and-disclosure.md`
- `docs/reports/20-round-ab-snapshot.md`
- `docs/reports/multi-model-behavioral-response-analysis-public-safe.md`
- `docs/public-evidence-chain.md`
- `docs/studies/v1-7-public-note.md`
- `docs/studies/gbs-meta-layer-concept-note.md`

## Author

SangZi Wang  
Email: sangziwang91@gmail.com

## What this repository is not

This is **not**:

- a full internal control core
- a leaked private system
- a patch, defense, or alignment fix
- a claim that current AI is universally broken

It is a structured public surface for observing how models behave when uncertainty pressure rises.

## Why it matters

Most users treat model confidence as a rough signal of reliability.
That shortcut is often wrong.

This repository is built to make that visible in a way that is:

- readable to non-specialists
- structured enough for technical readers
- explicit enough for researchers and journalists to audit the limits

## Disclosure boundary

Some implementation details are intentionally withheld.

The order of reasons is simple:

1. reproducibility boundary
2. misuse risk
3. commercial protection

The goal is to keep the public layer legible without exposing details that would make the protocol easier to misuse, imitate superficially, or reverse-engineer into internal systems.

## Current status

This is the active public-facing repository.
Future public updates, examples, and research-facing materials will continue here.
