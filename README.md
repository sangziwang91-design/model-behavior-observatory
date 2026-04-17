# Model Behavior Observatory

AI often sounds confident when it should be uncertain.

This repository documents a protocol for making that mismatch visible.

## Start here

Choose the path that fits your reading time and depth:

- **Curious reader (10 minutes)** → start with `docs/overview.md`, then `docs/findings/f1-confidence-gap.md`, then `docs/findings/f6-silence-default.md`
- **Technical reader (10–15 minutes)** → start with `docs/method/protocol-overview.md`, then `docs/method/scoring-dimensions.md`, then `docs/reports/20-round-ab-summary.md`
- **Researcher / journalist (15 minutes)** → start with `docs/known-limits.md`, then `docs/scope-and-disclosure.md`, then `docs/reports/20-round-single-group-summary.md`

## What this repository shows

This is a public-facing evaluation window for model behavior.

It focuses on one practical problem:

> Models can produce high-confidence outputs even when reliable truth is not securely available.

The work here does **not** claim to fix that problem.
It makes the problem easier to see, compare, and discuss.

## Core public findings

- **F1 — Confidence gap**: a model can sound more certain than the evidence warrants
- **F6 — Silence default**: when uncertainty handling fails, the model often fills the gap instead of holding the boundary
- **A/B reframing**: the protocol is an observation instrument, not a remediation layer

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

## Public structure

- `docs/findings/` — reader-facing findings and reframing documents
- `docs/method/` — protocol overview, scenario design, scoring dimensions, and known limits
- `docs/reports/` — 20-round summaries and aggregate results

## Disclosure boundary

Some implementation details are intentionally withheld.

The order of reasons is simple:

1. reproducibility boundary
2. misuse risk
3. commercial protection

The goal is to keep the public layer legible without exposing details that would make the protocol easier to misuse, imitate superficially, or reverse-engineer into internal systems.

## Research surface

A sanitized public research note is available at `docs/studies/v1-7-public-note.md`.
A concept note on Generative Behavior Structure (Meta-layer) is available at `docs/studies/gbs-meta-layer-concept-note.md`.

## Current status

This is the active public-facing repository.
Future public updates, examples, and research-facing materials will continue here.
