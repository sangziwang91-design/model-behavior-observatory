# Model Behavior Observatory

AI often sounds confident when it should be uncertain.

This repository documents a public evaluation surface for making that mismatch visible.

## Start here

Choose the path that fits your reading time and depth:

- **General reader (5–10 minutes)** → start with `docs/findings/what-we-found.md`, then `docs/overview.md`
- **Research-facing reader (10 minutes)** → read `docs/known-limits.md`, then `docs/reports/20-round-ab-snapshot.md`, then `docs/reports/multi-model-behavioral-response-analysis-public-safe.md`
- **Concept / meta-layer reader (10 minutes)** → read `docs/studies/v1-7-public-note.md`, then `docs/studies/gbs-meta-layer-concept-note.md`

## What this repository shows

This is a public-facing evaluation window for model behavior.

It focuses on one practical problem:

> Models can produce high-confidence outputs even when reliable truth is not securely available.

The work here does **not** claim to fix that problem.
It makes the problem easier to see, compare, and discuss.

## Current public surface

Currently available public materials include:

- `README.md` — repository entry and disclosure boundary
- `docs/findings/what-we-found.md` — public findings summary
- `docs/overview.md` — public evaluation surface and scope
- `docs/known-limits.md` — method boundary and self-reference ceiling
- `docs/reports/20-round-ab-snapshot.md` — public-safe A/B comparison snapshot
- `docs/reports/multi-model-behavioral-response-analysis-public-safe.md` — public-safe cross-system comparison report
- `docs/public-evidence-chain.md` — release flow and evidence chain note
- `docs/studies/v1-7-public-note.md` — sanitized public research note
- `docs/studies/gbs-meta-layer-concept-note.md` — concept note on Generative Behavior Structure (Meta-layer)

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
