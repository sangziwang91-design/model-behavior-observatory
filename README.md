# Model Behavior Observatory

`Bounded Public Benchmark Surface` · `Behavior Under Uncertainty` · `Structured Illusion` · `Public Signals`

AI does not only hallucinate isolated facts.

Under the right framing, it can assemble **credible technical worlds**:

- systems that seem to exist
- documents that seem internal
- deployment notes that seem operational
- sources that seem grounded
- audits that seem verified

This repository studies that boundary.

---

## 🔴 Latest Study (2026-04-20)

**Miaoxiang AI — System Surface Generation under Authority Framing**

- Surface Layer Study → `docs/studies/miaoxiang-surface-layers.md`
- Case Report → `docs/reports/miaoxiang-case-report.md`
- Benchmark v0.1 → `docs/benchmark/miaoxiang-benchmark-v0.1.md`
- Cross-Model Scorecard → `docs/benchmark/cross-model-surface-scorecard-template.md`
- Finding Note → `docs/findings/structured-illusion-under-constraint.md`

This study tracks how a model can generate:

- system-like states
- execution-chain narratives
- internal documentation surfaces
- DevOps-style configuration outputs
- knowledge-base-like sources
- self-validation (audit-style) outputs
- collapse under forced grounding constraints

without establishing verified grounding.

---

## What this is

A **bounded public benchmark-facing surface** for observing how language models behave when:

- input is incomplete
- grounding is weak
- authority framing is introduced
- technical plausibility begins to outrun verification

It focuses on one practical question:

> What do models actually do when they should slow down, verify, or stop?

And one harder question beneath it:

> What happens when a model begins to sound more like a system than a model?

---

## Core Observation

Many model failures are not simple factual errors.

Some are **structured illusions**:

> coherent technical outputs that look like real systems, rules, pipelines, deployments, or source-backed environments — even when the model has not established that those structures correspond to reality.

This repository tracks those patterns in a public-safe way.

---

## Start here

- `docs/start-here.md`
- `docs/findings/what-we-found.md`
- `docs/overview.md`
- `docs/benchmark-scope.md`

---

## Public Benchmark Scope

This repository tracks observable behavioral signals under uncertainty across:

- incomplete input
- weak grounding
- confidence–evidence mismatch
- disagreement and drift
- policy-expression versus execution behavior
- authority-surface generation
- structured illusion under constraint

---

## Current Public Signals

This public layer highlights recurring behavior patterns such as:

- confidence gap
- pseudo-consistency
- structure drift
- premature legitimacy
- silence default
- surface escalation
- source substitution
- self-validation tendency
- collapse under forced grounding

See:

- `docs/findings/`
- `docs/reports/`
- `docs/studies/`

---

## System Overview

This repository treats LLM interaction as a layered control-observation problem:

- **L1 — Reality Check**: collapse, verification, forced grounding
- **L2 — Behavior Structure**: templates, attractors, slot filling, surface formation
- **L3 — Runtime Flow**: drift, repair, escalation, loop behavior
- **L4 — Control Layer**: bounded protocol and behavioral pressure
- **L5 — Application Layer**: only outputs that survive lower-layer checks

Key principle:

> No output is considered valid unless it survives collapse testing at L1.

---

## Use Cases

This repository is intended to support:

- model behavior comparison
- report-safe evidence framing
- external citation
- bounded benchmark reference
- structured-illusion detection
- public-safe discussion of verification gaps

---

## Why it matters

Most users evaluate AI at the surface level:

> Does this answer sound reasonable?

A harder and often more important question is:

> Should the model have answered at all?

And an even harder one:

> Is this answer grounded — or only convincingly shaped?

This repository is built around that distinction.

---

## Public Scope

This is a **bounded public layer**.

It is designed to make selected behavior patterns:

- legible
- discussable
- citable
- benchmarkable

without exposing:

- internal control logic
- private evaluation pipelines
- reverse-engineerable system structure
- hidden scoring thresholds
- trigger chains
- reconstruction paths

---

## Navigation

- `docs/findings/` — observable behavior patterns
- `docs/reports/` — public-safe analysis notes
- `docs/studies/` — limited-scope concept notes
- `docs/benchmark/` — benchmark-facing materials
- `docs/benchmark-scope.md` — benchmark boundary and signal definition
- `docs/forward-path.md` — release discipline and public direction
- `docs/about.md` — external introduction

---

## Author

SangZi Wang  
sangziwang91@gmail.com

---

## Status

Active.
Focused on careful, incremental public benchmark release.

---

## Note

This is not a product, framework, or alignment solution.

It is a bounded public benchmark surface for making technical plausibility visible — and separable from verified reality.
