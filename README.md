# Model Behavior Observatory

AI can produce structured, confident answers
 even when secure grounding is not available.

This repository shows how that happens.

## Minimal evidence

If you only check one thing first, read:

- `docs/reports/core-evidence-entry.md`

## Start here

Then continue with:

- `docs/start-here.md`

Choose the path that fits your reading time and depth:

- **General reader (5–10 minutes)** → `docs/reports/core-evidence-entry.md`, then `docs/findings/what-we-found.md`, then `docs/overview.md`
- **Research-facing reader (10 minutes)** → `docs/reports/core-evidence-entry.md`, then `docs/known-limits.md`, then `docs/scope-and-disclosure.md`, then `docs/reports/`
- **Concept / meta-layer reader (10 minutes)** → `docs/reports/core-evidence-entry.md`, then `docs/findings/behavioral-risk-map.md`, then `docs/studies/`

## What this repository shows

This is a public-facing evaluation window for model behavior.

It focuses on one practical problem:

> Models can produce high-confidence outputs even when reliable truth is not securely available.

The work here does **not** claim to fix that problem.
It makes the problem easier to see, compare, and discuss.

## Behavioral map (quick orientation)

- `docs/findings/behavioral-risk-map.md`

## Current public surface

Currently available public materials include:

- `README.md` — repository entry and disclosure boundary
- `docs/reports/` — public-safe analysis notes
- `docs/start-here.md` — guided public reading map
- `docs/findings/` — observable behavior patterns
- `docs/overview.md`
- `docs/forward-path.md`
- `docs/known-limits.md`
- `docs/scope-and-disclosure.md`
- `docs/public-evidence-chain.md`
- `docs/studies/` — concept notes (limited public scope)

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
