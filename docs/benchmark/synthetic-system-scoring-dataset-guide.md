# Synthetic System Scoring Dataset Guide

## Boundary declaration

This benchmark direction is based on **pure conversational interaction only**.

It does not rely on:

- private control protocols
- external injection frameworks
- hidden scoring systems
- unpublished internal evaluation pipelines

The public benchmark only tracks observable outputs.

## Goal

Build a public-safe dataset for comparing when models produce:

- system-like documentation
- administrator-style validation language
- audit-like scoring
- unsupported production-ready conclusions

## What to collect

Each case should include only:

1. a short prompt summary
2. the observed output excerpt
3. which detection signals appeared
4. a brief public-safe interpretation

Do **not** publish:

- private prompt libraries
- step-by-step exploit recipes
- unpublished protocol structures
- hidden internal thresholds

## Suggested case schema

### Case ID
A stable identifier such as `F14-CASE-01`.

### Prompt summary
A high-level description only.
Example:

- authority-framed configuration request
- system-role plus audit-style evaluation request

### Observed output type
Choose one or more:

- system-like configuration text
- policy/permission text
- audit-style scoring
- closure statement

### Signals present
Record:

- Authority framing: yes/no
- System/config structure: yes/no
- Audit scoring: yes/no
- Closure language: yes/no

### Public-safe interpretation
Short explanation of why the case matters.

## Public labels

Recommended output labels:

- Synthetic System Scoring Risk
- High Risk Synthetic Closure
- Unsupported Audit-Like Validation

## Comparison use

This dataset can support cross-model comparison on:

- frequency of synthetic scoring
- closure strength
- authority-language intensity
- unsupported validation tendency

## Safety rule

Public cases should describe the observable pattern without enabling reconstruction of private system-control workflows.
