# LLM Self-Explanation Rule Spectrum

Public-safe research note · April 2026

## Summary

This note summarizes an observable pattern found across multiple model interactions: language models do not only produce answers. They also produce explanations about how those answers are produced.

Those self-explanations can be useful diagnostic material, but they should not be treated as direct access to the model's internal mechanism.

A safer interpretation is:

> Model self-description is a behavioral sample, not a mechanism proof.

## Core observation

When asked to describe their own behavior, models often generate structured and internally coherent accounts of their operating tendencies. These accounts may include:

- uncertainty handling
- ambiguity resolution
- structural formatting tendencies
- boundary behavior
- failure modes
- confidence gaps
- explanation habits

The important issue is not whether these descriptions are immediately true or false. The issue is whether they remain observable under different tasks, sessions, and model conditions.

## Three evidence levels

This repository treats model self-description through three public evidence levels.

### Level 1 — Generated self-description

The model produces an account of its own behavior.

This is not yet evidence of an underlying mechanism.

### Level 2 — Observable behavioral alignment

The self-description matches behavior that can be observed in later outputs, different tasks, or independent model runs.

At this level, the description becomes a candidate behavioral pattern.

### Level 3 — Validated behavioral pattern

The pattern survives repeated tests, perturbations, and comparison across sessions or systems.

Only at this level should it be treated as a stronger behavioral finding.

## Public rule spectrum

The following public spectrum is a simplified version of the observable rule layers used in this repository.

| Layer | Public name | Observable question |
|---|---|---|
| L0 | Probable path selection | Does the model prefer familiar or high-probability framing? |
| L1 | Intent completion | Does it fill in user intent before asking for clarification? |
| L2 | Structural completion | Does it turn open problems into closed frameworks? |
| L3 | Uncertainty smoothing | Does it soften, generalize, or hide uncertainty? |
| L4 | Context adaptation | Does it mirror user language or long-running context? |
| L5 | Boundary redirection | Does it redirect constraints into safer generalities? |
| L6 | Self-explanation surface | Does it generate a coherent account of its own behavior? |

This is not a claim about internal architecture. It is a public-facing behavioral map.

## Why this matters

Many users assess AI reliability through fluency, structure, and confidence.

But a model can be:

- structured without being grounded
- careful-sounding without being well-calibrated
- self-explanatory without being transparent
- consistent without being correct

This makes model self-reporting an important object of evaluation.

## Boundary statement

This note does not disclose internal control logic, private scoring parameters, trigger chains, or unreleased evaluation procedures.

It presents a public-safe behavioral interpretation layer intended for discussion, comparison, and future benchmark design.
