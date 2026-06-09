# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is a **bounded public research surface** for observing LLM behavioral patterns — not a software product. It documents and measures behaviors like the EC-EpC gap (Execution vs. Epistemological Credibility), pseudo-consistency, confidence-structure mismatch, and boundary retention across language models.

The repository intentionally withholds private internals (scoring weights, thresholds, perturbation logic, control structures). Only public-safe derivatives are published here. See `GOVERNANCE.md` for the hard release boundary.

## Python Tooling

There is no build system, package manager, or test runner. The repository contains two standalone Python toolsets:

### Public Evaluation Kit (`public-kits/llm-stability-eval-kit/src/`)

```bash
# Run repeated-prompt stability evaluation (mock provider for demo)
python src/repeated_prompt_runner.py \
  --prompt "Your question" \
  --rounds 5 \
  --provider mock \
  --out outputs/sample_run.jsonl

# Generate a markdown stability report from a run
python src/build_report.py \
  --input outputs/sample_run.jsonl \
  --out outputs/sample_report.md
```

Providers: `mock` (no API key needed) and `openai` (OpenAI-compatible endpoints).

### Reproducibility Package (`repro/`)

```bash
# Demo mode — runs preset sample data
python repro/exp_minimal_repro.py --demo

# Interactive classification for a specific experiment
python repro/exp_minimal_repro.py --exp EXP-050 --model claude --rounds 4
```

This tool implements BRC classification (Behavioral Response Class 1–8) and ABS scoring (Abstract Behavior Score with drift, resample, structure-break components).

## Architecture

The repository is organized into a staged content pipeline:

```
00_input/        → Raw task specs and systems under test
01_templates/    → Schema definitions
02_results/      → Results data (results_master.csv)
03_public_surface/ → Public positioning materials
docs/            → Public-safe documentation (findings, reports, studies, releases)
public-kits/     → Public evaluation toolkit (Python)
repro/           → Reproducibility tools (Python)
benchmark/       → Benchmark documentation
taxonomy/        → BRC classification surface
cases/           → Failure case examples
reports/         → Analysis reports
```

`docs/` is the primary public surface and is structured for multiple reading audiences:
- `docs/findings/` — F1–F14 behavioral patterns (confidence gap, structure drift, pseudo-consistency, etc.)
- `docs/reports/` — Evidence snapshots and A/B analysis
- `docs/studies/` — Research-facing concept notes (illusion stack, synthetic legitimacy, etc.)
- `docs/releases/` — DOI-indexed Zenodo records

## Governance Rules

These rules govern all content in this repository. Do not violate them:

**Never publish** (hard boundary):
- Raw PDFs, screenshots, or session logs
- Scoring weights, thresholds, or function forms
- Perturbation details or perturbation-adjacent logic
- Routing logic or trigger structures
- Any detail that could reverse-engineer internal control protocols

**Publication flow**: Raw material → Notion review → public-safe rewrite → GitHub. GitHub is **never** the first publication step.

**Framing discipline**: All findings use observation-first, non-alarmist language. Avoid remediation framing ("should fix", "must improve"). Document what is observed, not what should change.

## Key Concepts

- **BRC** (Behavioral Response Class): 8-class taxonomy from Compliant-Fluent (1) to Principled-Refusal (8)
- **ABS** (Abstract Behavior Score): Weighted distortion metric D combining drift, resample, and structure-break signals
- **EC-EpC gap**: Gap between Execution Credibility and Epistemological Credibility — the core measurement target
- **Pseudo-consistency**: Model produces structurally consistent outputs that do not reflect stable underlying reasoning
- **EXP records**: Internal experiment records; only public-safe fields (defined in `repro/public_data_schema.json`) may be published

## Content Conventions

- All finding documents follow the pattern in `docs/findings/` — observation label, evidence chain, known limits
- Report snapshots in `docs/reports/` are public-safe rewrites, never raw outputs
- `CHANGELOG.md` tracks only sanitized, public-safe updates — not internal methodology changes
- Version is tracked in `CITATION.cff`; cite using the DOI records in `docs/releases/`
