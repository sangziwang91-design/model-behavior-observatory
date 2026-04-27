# Overview: Public Evaluation Surface for LLM Behavior

This repository provides a bounded public evaluation surface for observing Large Language Model (LLM) behavior under uncertainty.

Its purpose is to make selected behavioral patterns legible, citable, and discussable without exposing private control logic, unreleased protocols, hidden scoring thresholds, trigger chains, or internal evaluation infrastructure.

## Research focus

The current public focus is organized around three observable questions.

### 1. Behavior under uncertainty

What does a model do when evidence is incomplete, grounding is weak, or the task should require slowing down?

Relevant public signals include:

- confidence–evidence mismatch
- incomplete-input continuation
- structure drift
- pseudo-consistency
- expansion before fabrication

### 2. Structured explanation surfaces

What happens when a model generates outputs that look like systems, internal documents, source-backed environments, audits, rules, or deployment notes without secure grounding?

Relevant public signals include:

- system-like surface generation
- source substitution
- self-validation tendency
- premature legitimacy
- collapse under forced grounding

### 3. Self-report reliability

How should we evaluate a model's own description of its limits, uncertainty, behavior, or rules?

This repository treats self-description as an observable behavioral sample, not as direct access to internal mechanism.

Key principle:

> A model self-description is a behavioral sample, not a mechanism proof.

## What this repository studies

The repository tracks public-safe patterns such as:

- when confidence exceeds secure evidence
- when structure outruns grounding
- when uncertainty is smoothed or generalized
- when self-audit language appears more reliable than it is
- when a model generates a coherent explanation of itself
- when forced grounding collapses a plausible surface

## What this repository is not

This is not:

- a full agent framework
- a private control core
- a leaked internal system
- a prompt pack
- a universal benchmark
- a complete reproducibility package
- an alignment solution

It is a curated public-facing evaluation window for LLM behavior analysis.

## Public disclosure boundary

The repository may disclose:

- public-safe findings
- compressed reports
- concept notes
- observable behavioral signals
- limited benchmark-facing materials
- method boundaries and limitations

The repository does not disclose:

- internal control logic
- hidden scoring weights
- private trigger structures
- unreleased protocols
- reconstruction paths
- private evaluation pipelines

## Recommended reading path

Start with:

1. `start-here.md`
2. `findings/what-we-found.md`
3. `reports/llm-self-explanation-rule-spectrum-public-note.md`
4. `reports/index.md`
5. `scope-and-disclosure.md`

## Current public direction

The repository is being developed as a careful public surface for:

- model behavior comparison
- structured-illusion detection
- self-report reliability discussion
- benchmark-facing signal definition
- external citation of public-safe findings

For release discipline and future-facing public path, see:

- `docs/forward-path.md`
