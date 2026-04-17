# Scope and Disclosure

This repository is intentionally partial.

Not everything is published, and that is a design decision.

## Why some details are withheld

The order of reasons matters:

### 1. Reproducibility boundary

A protocol can be described without making every implementation detail replicable.

Full disclosure of internal structure often leads to shallow replication rather than meaningful verification.

The goal here is **understandable observation**, not copyable internals.

### 2. Misuse risk

If the full injection structure, trigger design, and internal thresholds are exposed, the same tools can be used to:

- induce misleading outputs deliberately
- simulate credibility without evidence
- game evaluation setups

The protocol is meant to reveal these behaviors, not to amplify them.

### 3. Commercial protection

The work behind this repository includes systems that are not intended to be open-sourced in full.

This is not hidden. It is stated openly so readers can interpret the boundary correctly.

## What is still transparent

Even with these limits, the following are fully visible:

- the problem framing (confidence vs reliability)
- the observation protocol (public version)
- the scoring dimensions and scenario structure
- the observed patterns and aggregate results
- the known limits of the method itself

## How to read this repository correctly

Treat this as a **behavior observation surface**.

Not as:

- a complete system
- a universal benchmark
- a final authority on model correctness

The goal is to make a specific class of behavior visible in a way that others can examine, question, and build on.
