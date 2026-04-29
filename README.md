# Model Behavior Observatory

**A bounded public research surface for LLM self-report reliability, structured behavioral failures, and constrained-access model audit.**

`LLM Behavior` · `Self-Report Reliability` · `EC-EpC Gap` · `Behavioral Cartography` · `Constrained-Access Audit`

---

## Latest release

### EC-EpC Gap and Cross-Model Behavioral Cartography · April 2026

Two public Zenodo records are now available:

| Record | Type | DOI |
|---|---|---|
| **Auditing Epistemological Credibility in LLM Self-Reports: A Dual-Axis Behavioral Framework and Pilot Evidence** | Preprint | [10.5281/zenodo.19879788](https://doi.org/10.5281/zenodo.19879788) |
| **Cross-Model Behavioral Cartography: A Pilot Dataset Summary for LLM Self-Report Reliability Research** | Dataset summary / pilot dataset record | [10.5281/zenodo.19881753](https://doi.org/10.5281/zenodo.19881753) |

Release note: [`docs/releases/zenodo-ec-epc-2026.md`](docs/releases/zenodo-ec-epc-2026.md)

These records introduce and document exploratory pilot-level work on the **EC-EpC gap**: the difference between a model's ability to produce a coherent self-audit output and the reliability of its self-reported knowledge boundaries.

---

## Core question

When a language model explains its own limits, should that explanation be trusted?

This repository treats model self-description as an observable behavior, not as direct proof of internal mechanisms.

---

## What this repository is

Model Behavior Observatory is a bounded public evaluation surface for observing how language models behave when:

- evidence is incomplete;
- grounding is weak;
- uncertainty is high;
- authority framing is introduced;
- self-description is requested;
- structured outputs begin to look more reliable than they are.

It focuses on practical reliability questions:

> What do models do when they should slow down, verify, or stop?

> What happens when a model begins to sound more like a system than a model?

> How reliable are a model's own explanations of its behavior and limits?

---

## Public research focus

### 1. Self-report reliability

How models describe their own limits, rules, uncertainty, and behavioral tendencies — and why these descriptions need external audit rather than direct trust.

### 2. EC-EpC gap

The measurable gap between:

- **Execution Credibility (EC):** how well a model executes a structured self-audit task;
- **Epistemological Credibility (EpC):** how accurately the model characterizes its own knowledge boundaries.

### 3. Behavioral cartography

Cross-model observation of external response patterns under structured audit conditions, without requiring internal model access.

### 4. Structured explanation surfaces

How models generate system-like, documentation-like, source-like, or audit-like outputs that appear more grounded than they are.

---

## Public-safe boundaries

This repository is intentionally bounded.

It makes selected observations legible, discussable, and citable while avoiding release of private audit procedures.

Public materials may include:

- high-level method framing;
- behavioral categories;
- summary-level quantitative findings;
- public pilot records;
- limitations and validation requirements.

Public materials do **not** include:

- exact task inputs;
- scoring weights;
- trigger thresholds;
- intervention templates;
- private audit heuristics;
- reverse-engineerable control procedures;
- full benchmark task packs.

---

## Claim level

Current public records are exploratory pilot-level releases.

They support:

- methodological critique;
- replication design;
- external citation;
- discussion of LLM self-report reliability;
- bounded public reference.

They do **not** support:

- population-level prevalence claims;
- model ranking;
- causal claims about internal model mechanisms;
- validated benchmark status;
- regulatory-grade standardization claims.

---

## Current public signals

This public layer highlights recurring observable patterns such as:

- confidence–evidence mismatch;
- structure outrunning evidence;
- premature legitimacy;
- pseudo-consistency;
- self-validation tendency;
- self-report reliability gap;
- structured explanation surface;
- boundary redirection;
- collapse under forced grounding.

---

## Start here

- [`docs/releases/zenodo-ec-epc-2026.md`](docs/releases/zenodo-ec-epc-2026.md) — April 2026 Zenodo release note
- [`docs/start-here.md`](docs/start-here.md) — recommended entry point
- [`docs/overview.md`](docs/overview.md) — public evaluation scope
- [`docs/findings/what-we-found.md`](docs/findings/what-we-found.md) — public findings map
- [`docs/reports/index.md`](docs/reports/index.md) — public-safe reports
- [`public-kits/llm-stability-eval-kit/`](public-kits/llm-stability-eval-kit/) — repeated-prompt testing and pseudo-consistency observation

---

## Citation

Wang, S. (2026). *Auditing Epistemological Credibility in LLM Self-Reports: A Dual-Axis Behavioral Framework and Pilot Evidence*. Zenodo. https://doi.org/10.5281/zenodo.19879788

Wang, S. (2026). *Cross-Model Behavioral Cartography: A Pilot Dataset Summary for LLM Self-Report Reliability Research*. Zenodo. https://doi.org/10.5281/zenodo.19881753

---

## Use cases

This repository is intended to support:

- model behavior comparison;
- public-safe evidence framing;
- external citation;
- bounded benchmark reference;
- structured-illusion detection;
- self-report reliability discussion;
- analysis of verification gaps under constrained-access conditions.

---

## Navigation

- `docs/releases/` — public release notes
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

Independent Researcher · Behavioral AI Research Initiative, Zhongshan

---

## Status

Active. Focused on careful, incremental public release of model behavior observation materials.

---

## Note

This is not presented as an alignment solution, product, or validated benchmark.

It is a bounded public research surface for making LLM self-report reliability, technical plausibility, and verification gaps easier to observe and discuss.
