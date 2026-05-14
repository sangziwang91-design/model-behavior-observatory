# Baseline Comparison: Generative Behavior Science Framework vs. Existing Evaluation Approaches

**Sangzi Wang · Independent Researcher**  
*For use in Related Work sections of academic submissions*  
*Public-safe layer — internal system details withheld per PUBLIC-PRIVATE-SPLIT governance*

-----

## Overview

This document situates the Generative Behavior Science (GBS) framework and its core instruments (EC-EpC, BRC, ABS, GBSF, PMIGS, Testing as Environment / TAE) relative to four major families of existing work: (1) static benchmark evaluation, (2) LLM observability platforms, (3) AI safety evaluation, and (4) human-AI interaction research.

The argument is not that GBS replaces these approaches, but that it addresses a complementary layer — **longitudinal interaction dynamics, generative distribution governance, and bounded disclosure architecture** — that existing tools do not directly target.

-----

## 1. Static Benchmark Evaluation

| Dimension | HELM (Liang et al., 2022) | lm-evaluation-harness (EleutherAI) | OpenAI Evals | **GBS / EC-EpC / BRC** |
|---|---|---|---|---|
| Unit of analysis | Single-turn output | Single-turn task | Single-turn task | **Multi-turn interaction sequence** |
| What is measured | Accuracy, calibration, robustness, bias | NLP task performance | Application-specific quality | **Behavioral trajectory, distribution shift, credibility gap** |
| Reproducibility | Public protocol + code | Public code | Public framework | Reproducible per EXP protocol (this package) |
| Cross-model | Yes | Yes | Partial | **Yes (Claude, GPT, Gemini, GLM, Kimi)** |
| Evaluation awareness | Not addressed | Not addressed | Not addressed | **Core research object (TAE / EXP-051)** |
| Long-context drift | Not addressed | Not addressed | Not addressed | **Core research object (EXP-065)** |
| Human-model co-adaptation | Not addressed | Not addressed | Not addressed | **Core research object (HMCGF / IEF)** |

**Key distinction:** HELM and lm-eval measure *what a model outputs* on standardized tasks. GBS measures *how model behavior evolves across interaction*, including drift, recovery, attractor formation, and protocol-induced shifts.

**Gap filled by GBS:** The EC-EpC gap — the divergence between execution completeness and epistemic credibility — is not captured by accuracy-based benchmarks that treat task completion as success.

-----

## 2. LLM Observability / LLMOps Platforms

| Dimension | LangSmith | Arize Phoenix | Langfuse | Braintrust | **GBSF Audit Console** |
|---|---|---|---|---|---|
| Primary focus | Tracing, prompt mgmt | Observability, data drift | Tracing, eval workflow | Dataset-centric regression | **Behavioral audit, interaction drift** |
| Interaction depth | Session-level trace | Token/span level | Session-level | Dataset comparison | **Round-level BRC + ABS scoring** |
| Behavioral taxonomy | None | None | None | None | **BRC 8-class + ABS distortion index** |
| Protocol-induced effects | Not addressed | Not addressed | Not addressed | Not addressed | **PMIGS, attractor detection** |
| Public/private output split | None | None | None | None | **Translation Bus / bounded disclosure** |
| Epistemic credibility audit | None | None | None | None | **EC-EpC gap measurement** |

**Key distinction:** LangSmith/Arize track *system performance and errors*. GBSF audits *behavioral credibility and generative distribution governance* — whether the model’s apparent compliance masks epistemic drift.

-----

## 3. AI Safety Evaluation

| Dimension | METR | Apollo Research | Anthropic/OpenAI Joint Evals (2025) | **GBS / TAE / EC-EpC** |
|---|---|---|---|---|
| Primary focus | Autonomous capability, long-horizon tasks | Scheming, self-preservation | Sycophancy, misuse, misalignment | **Behavioral ecology, interaction-layer governance** |
| Evaluation awareness | Emerging concern | Studied directly | Partial | **Core research object (TAE = Testing as Environment)** |
| Protocol as variable | Not primary | Not primary | Not primary | **Primary: protocol morphology induces generative shift (PMIGS)** |
| Long-context reliability | Yes (task completion) | Not primary | Not primary | **Yes (runtime collapse, externalized continuity — EXP-065)** |
| Multi-turn co-adaptation | Not primary | Not primary | Not primary | **Yes (HMCGF, IEF, semantic territory — EXP-057)** |
| Evidence gate / disclosure | Not addressed | Not addressed | Not addressed | **Yes (PUBLIC-PRIVATE-SPLIT, bounded disclosure)** |

**Convergence point:** GBS and the AI safety eval community share concern about evaluation awareness (the model behaving differently when it detects it is being tested). GBS contributes the *Testing as Environment* framing: testing is not a neutral observer but an active shaper of generative behavior.

**Divergence:** METR/Apollo focus on dangerous capability thresholds. GBS focuses on the everyday interaction layer — how ordinary protocol structure, conversational framing, and multi-turn context shape behavioral trajectories even in non-dangerous interactions.

-----

## 4. Human-AI Interaction Research

| Dimension | HALIE (Lee et al., 2022) | CHI HCI tradition | Wizard-of-Oz studies | **GBS / HMCGF / IEF** |
|---|---|---|---|---|
| Unit of analysis | Human-LM interaction episode | User task performance | Simulated agent interaction | **Interaction ecology: co-generative field** |
| What is measured | Perceived quality, ownership, enjoyment | Usability, efficiency, errors | User mental models | **Generative distribution co-shift, semantic territory formation** |
| Model behavior as variable | Implicit | Implicit | Simulated | **Explicit: model trajectory is primary dependent variable** |
| Mechanism focus | Descriptive | Descriptive | Descriptive | **Mechanistic: attractor, convergence inertia, drift-recovery** |
| Governance layer | None | None | None | **Yes: runtime governance, evidence gate, rule mutation** |

**Key distinction:** HCI research documents *human experience*. GBS additionally tracks *model-side behavioral change* within the same interaction, treating the interaction as a bi-directional generative field.

-----

## Summary: The Layer GBS Occupies

```text
Static output quality          <- HELM, lm-eval, OpenAI Evals
↓
Session-level tracing          <- LangSmith, Arize, Langfuse
↓
Dangerous capability auditing  <- METR, Apollo, Anthropic/OAI
↓
Human experience of AI         <- HCI, HALIE, CHI

UNMAPPED LAYER (addressed by GBS):

Multi-turn behavioral trajectory
+ generative distribution governance
+ epistemic credibility gap (EC-EpC)
+ protocol-induced behavioral shift (PMIGS)
+ evaluation awareness as generative force (TAE)
+ human-model co-adaptation field (HMCGF)
+ bounded disclosure architecture
```

-----

## Citation Anchors (for Related Work)

When citing this framework in submissions, use the following Zenodo DOIs:

- EC-EpC Gap: `10.5281/zenodo.19879788`
- Behavioral Cartography Dataset (BRC): `10.5281/zenodo.19881753`
- GBSF DDRS: `10.5281/zenodo.20086355`
- IEF: `10.5281/zenodo.20087158`
- ABS-1.1: `10.5281/zenodo.20087587`
- Convergence Inertia (EXP-047): `10.5281/zenodo.20087809`
- MSI-AUDIT-001: `10.5281/zenodo.20088014`

-----

*Last updated: 2026-05-14 · Public-safe layer · Internal system architecture withheld*
