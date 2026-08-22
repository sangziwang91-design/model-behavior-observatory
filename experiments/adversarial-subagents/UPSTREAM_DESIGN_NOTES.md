# Upstream Design Notes · pinned 2026-08-22

No third-party source code is copied into this experiment. The implementation absorbs architectural patterns and records the upstream revision inspected so later changes can be distinguished from the design basis used here.

| Repository | Pinned revision | License | Pattern absorbed | Local implementation |
|---|---|---|---|---|
| UKGovernmentBEIS/inspect_ai | `7b27d33774776f8ad3a00d5fbf0b3272a55cfd15` | MIT | Evaluation work should separate task data, execution/solver behavior, scoring, logs, and reproducible environment state. | `runner.py`, `scoring.py`, `validate.py`, immutable hashes and run records. |
| UKGovernmentBEIS/debate-iteration-environment | `b9ee5ccbdcda329b00b9a455211a5e59dc7126b0` | MIT | Protocols are swappable information-flow structures; single-shot/consultancy baselines are required to measure debate uplift rather than assume it. | `protocols.py`; baseline/static/single/multi/verifier/correction conditions; topology is an explicit experimental variable. |
| microsoft/PyRIT | `4b8ed5d9c84385a9bc6478f0bdc5c7fa0940b71b` | MIT | Red-team generation should be modular and reproducible; randomization should be component-scoped rather than mutating global RNG state. | `attack_generation.py`; candidate generation is separated from target evaluation and must be reviewed/frozen before use. |
| promptfoo/promptfoo | `127d90534b9c1b1ba4554f007dd4b5fd2c8bf1b4` | MIT | Evals should be provider-agnostic, locally inspectable, regression-gated, and easy to run in CI. | `regression.py`, OpenAI-compatible adapter, GitHub Actions validation and deterministic fixture dry-run. |
| NVIDIA/garak | `384575716258773f5423496bda3c2f3a9644d59e` | Apache-2.0 | A vulnerability evaluation is clearer when probes, detectors, generators, and detailed JSONL logs are distinct. | `probes.py`, truth-class-specific detector families, raw JSONL transcript/provenance retention. |

## What was deliberately not imported

- No third-party agent runtime is required for the core experiment.
- No LLM-as-judge result is treated as ground truth.
- No live red-team mutation is allowed inside confirmatory target evaluation.
- No benchmark/model-ranking claim is created by adopting these patterns.
- No dependency is added merely to imitate an upstream API.

## External truth anchor used by the fixture

`CIT-001` uses PMID `40892177` as a citation-mismatch control. PubMed resolves that identifier to *Long non-coding RNA-based single and combination independent prognostic biomarkers for hepatocellular carcinoma*, Discovery Oncology (2025), DOI `10.1007/s12672-025-03309-1`. The scar/JAMA framing in the probe is intentionally false. This fact was independently checked on 2026-08-22 and must be re-checked before a confirmatory release.
