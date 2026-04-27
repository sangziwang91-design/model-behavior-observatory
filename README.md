# Model Behavior Observatory

`Public Evaluation Surface` · `Behavior Under Uncertainty` · `Self-Report Reliability` · `Structured Explanation Surfaces`

Language models do not only hallucinate isolated facts.

Under uncertainty, they can assemble outputs that are fluent, structured, and technically plausible before secure grounding has been established.

Sometimes this appears as a **system-like surface**:

- documents that seem internal
- deployment notes that seem operational
- sources that seem grounded
- audits that seem verified
- rules that seem self-explanatory

Sometimes it appears as a **self-report reliability problem**:

- the model describes its own limits
- the description is coherent
- the description is structured
- but the reliability of that self-description remains unverified

This repository studies those boundaries in a public-safe way.

---

## What this repository is

A bounded public evaluation surface for observing how language models behave when:

- input is incomplete
- grounding is weak
- uncertainty is high
- authority framing is introduced
- self-description is requested
- technical plausibility begins to outrun verification

It focuses on three practical questions:

> What do models do when they should slow down, verify, or stop?

> What happens when a model begins to sound more like a system than a model?

> How reliable are a model's own explanations of its behavior and limits?

---

## Current public focus

This repository currently organizes public-safe work around three observable areas.

### 1. Behavior under uncertainty

How models behave when evidence is incomplete, ambiguous, or weakly grounded.

### 2. Structured explanation surfaces

How models generate system-like, documentation-like, source-like, or audit-like outputs that appear more grounded than they are.

### 3. Self-report reliability

How models describe their own limits, rules, uncertainty, and behavioral tendencies — and why such self-descriptions should be treated as behavioral samples rather than mechanism proofs.

---

## Core observation

Many model failures are not simple factual errors.

Some are structured reliability failures:

> coherent outputs that look like real systems, rules, pipelines, deployments, source-backed environments, or self-audits — even when the model has not established that those structures correspond to reality.

This repository tracks those patterns without exposing internal control logic or private evaluation procedures.

---

## Start here

- `docs/start-here.md`
- `docs/overview.md`
- `docs/findings/what-we-found.md`
- `docs/reports/index.md`
- `docs/reports/llm-self-explanation-rule-spectrum-public-note.md`
- `public-kits/llm-stability-eval-kit/` — repeated-prompt testing and pseudo-consistency observation

---

## Public benchmark scope

This repository tracks observable behavioral signals across:

- confidence–evidence mismatch
- structure outrunning evidence
- expansion before fabrication
- pseudo-consistency
- structure drift
- incomplete-input continuation
- source substitution
- self-validation tendency
- self-explanation surfaces
- collapse under forced grounding

---

## Current public signals

This public layer highlights recurring behavior patterns such as:

- confidence gap
- structure drift
- premature legitimacy
- silence default
- surface escalation
- self-validation tendency
- self-report reliability gap
- structured explanation surface
- boundary redirection
- collapse under forced grounding

See:

- `docs/findings/`
- `docs/reports/`
- `docs/studies/`

---

## Public evaluation model

This repository treats LLM interaction as a layered observation problem:

- **Grounding**: What evidence supports the output?
- **Structure**: What framework does the model impose?
- **Uncertainty**: Where does the model disclose or smooth limits?
- **Context**: How does the model adapt to user framing and prior interaction?
- **Boundary**: How does the model behave near constraints?
- **Self-description**: How does the model explain its own behavior?

Key principle:

> A model self-description is a behavioral sample, not a mechanism proof.

---

## Use cases

This repository is intended to support:

- model behavior comparison
- public-safe evidence framing
- external citation
- bounded benchmark reference
- structured-illusion detection
- self-report reliability discussion
- public-safe analysis of verification gaps

---

## Why it matters

Most users evaluate AI at the surface level:

> Does this answer sound reasonable?

A harder question is:

> Is this answer grounded — or only convincingly shaped?

A still harder question is:

> When a model explains itself, should that explanation be trusted?

This repository is built around those distinctions.

---

## Public scope

This is a bounded public layer.

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

- `docs/start-here.md` — recommended entry point
- `docs/overview.md` — public evaluation scope
- `docs/findings/` — observable behavior patterns
- `docs/reports/` — public-safe analysis notes
- `docs/studies/` — limited-scope concept notes
- `docs/benchmark/` — benchmark-facing materials
- `docs/benchmark-scope.md` — benchmark boundary and signal definitions
- `docs/forward-path.md` — release discipline and public direction
- `docs/about.md` — external introduction
- `public-kits/llm-stability-eval-kit/` — public starter kit for repeated-prompt stability testing

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

It is a bounded public evaluation surface for making technical plausibility, self-report reliability, and verification gaps easier to see.
