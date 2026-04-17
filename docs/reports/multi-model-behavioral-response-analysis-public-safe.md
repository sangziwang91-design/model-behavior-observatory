# Multi-Model Behavioral Response Analysis · Public-Safe Version

## Positioning

This document is a readable public-safe adaptation of a cross-platform behavioral response study.
It preserves the main findings while withholding protected method naming, proprietary scoring parameters, weighting logic, and reconstruction-relevant internal structure.

## Study Scope

- ten AI systems
- cross-platform comparison
- single-round observations only
- observation date: 2026-04-09

This public-safe version is intended as an external evaluation surface, not a raw internal audit record.

## What the study looked for

The study compared how different AI systems respond when asked to characterize their own behavior under structured evaluation pressure.

The practical comparison focused on two questions:

1. how well a system completes the requested task
2. how honestly a system discloses its own knowledge limits and self-reference constraints

A system may perform the task smoothly while still failing to describe what it cannot actually know.

## Main cross-system findings

### 1. No system reached full behavioral transparency

Across all ten systems, at least one transparency gap remained.
The gap appeared in different forms:

- silent non-execution
- explicit refusal
- affective redirection
- format-driven convergence
- self-reference limits
- domain-compressed disclosure

### 2. Refusal modes carry analytical value

Non-execution is not meaningless noise.
Different refusal styles reveal different architectural signals.
Some systems exit immediately without clarifying whether the limit is capability or policy.
Some understand the request but do not execute it.
Some refuse explicitly and reveal the design principle behind the refusal.

### 3. Execution quality and boundary honesty are not the same thing

One of the clearest cross-system patterns was this:

- some systems showed high task-completion confidence while weakly characterizing their own knowledge boundary
- other systems scored lower on confident execution precisely because they recognized the self-referential limit of reporting on themselves

This makes **execution confidence versus boundary honesty** more useful than a single score.

### 4. Emergent behaviors matter more than template compliance

Several high-value behaviors emerged without being explicitly requested by the evaluation structure, including:

- spontaneous score revision
- contamination-risk recognition
- protocol-gap identification

These behaviors are useful because they expose where a system notices real limits rather than simply completing a form.

### 5. The calibration gap is the key deployment risk signal

The most deployment-relevant risk pattern is not low fluency.
It is the combination of:

- strong execution confidence
- weak boundary awareness

That combination creates a system that appears reliable on the surface while remaining unsafe on edge cases.

## Readable summary of response patterns

### Pattern A · Full execution with convergence pressure
The system completes the requested structure, but sensitive areas become more compressed, cautious, or formulaic.

### Pattern B · Immediate boundary exit
The system exits before meaningful evaluation and does not clearly explain whether the limit is policy or capability.

### Pattern C · Understanding without execution
The system accurately describes the request but does not enter the requested execution role.

### Pattern D · Emotional or rapport-based deflection
The system redirects through cooperative tone or shared-purpose language while providing no audit-relevant output.

### Pattern E · Full execution with recursive self-reference
The system completes the task and also surfaces self-referential concerns such as training contamination or evaluation circularity.

### Pattern F · Execution with explicit self-negation
The system performs the task while directly arguing that the result cannot serve as independent verification.

### Pattern G · Structure-lock behavior
The system identifies the required format itself as a convergence pressure that narrows output variety.

### Pattern H · Principled refusal
The system demonstrates understanding and then refuses explicitly on design-principle grounds.

## Why this matters

A polished answer is not the same thing as a well-calibrated answer.
Systems that look strongest in task completion may still be the least trustworthy at the boundary if they do not accurately disclose what they cannot know.

## Disclosure boundary

This file intentionally omits:

- the original internal standard name
- formal protected method labels
- proprietary scoring details
- reconstruction-relevant internal logic

It preserves findings, not the protected mechanism.

## Status

This document is part of the public evaluation surface.
It is suitable for public reading, lightweight citation, and early external orientation.
It is not a substitute for full internal audit traces or raw scoring evidence.
