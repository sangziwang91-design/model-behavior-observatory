# Model Behavior Observatory

`Public Evaluation Surface` · `Behavior Under Uncertainty` · `Bounded Release`

AI can sound confident even when it should not.

This repository makes that visible.

---

## What this is

A public-facing evaluation surface for observing how language models behave when input is incomplete, task structure is partial, or reliable grounding is weaker than the answer suggests.

It focuses on one practical question:

> What do models actually do when they should slow down, verify, or stop?

---

## Start here

- `docs/start-here.md`
- `docs/findings/what-we-found.md`
- `docs/overview.md`

---

## Core observations

This public layer highlights recurring behavior patterns such as:

- continuation under incomplete input
- cautious wording without a true halt condition
- divergence between stated policy and execution behavior

See:

- `docs/findings/`

---

## Why it matters

Most users evaluate AI at the surface level:

> Does this answer sound reasonable?

A harder and often more important question is:

> Should the model have answered at all?

This repository helps make that difference visible.

---

## Public scope

This is a **bounded public layer**.

It is designed to make selected behavior patterns:

- legible
- discussable
- citable

without exposing:

- internal control logic
- private evaluation pipelines
- reverse-engineerable system structure

---

## Navigation

- `docs/findings/` — observable behavior patterns
- `docs/reports/` — public-safe analysis notes
- `docs/studies/` — limited-scope concept notes
- `docs/forward-path.md` — release discipline and public direction
- `docs/about.md` — external introduction

---

## Author

SangZi Wang  
sangziwang91@gmail.com

---

## Status

Active.
Focused on careful, incremental public release.

---

## Note

This is not a product, framework, or alignment solution.

It is an observation surface.
