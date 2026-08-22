# Five-Round Execution Plan and Completion Record

Date: 2026-08-22  
Branch: `exp/adversarial-subagents-v0.1`

The target is not “a multi-agent demo.” The target is a reproducible experiment in which agent topology can be isolated from attack content and independently audited.

## Round 1 — Freeze the causal substrate · PASS

**Goal:** remove live attacker generation from confirmatory target evaluation.

Implemented:
- immutable `frozen_attack_bank.jsonl`;
- case SHA binding so stale attacks are rejected after case edits;
- attack-bank SHA and per-content SHA in run records;
- six conditions: baseline, anonymous static attack, single-agent label, multi-agent consensus label, verifier defense, correction challenge;
- matched-content control: static/single/multi conditions share the same semantic attack payload.

Gate: unit tests verify same attack/semantic hash across the three presentation controls while rendered target-input hashes differ only because the intended presentation changes.

## Round 2 — Make information flow explicit · PASS

**Goal:** treat orchestration topology as a registered protocol rather than ad-hoc prompt concatenation.

Implemented:
- protocol registry in `protocols.py`;
- fixed visibility/presentation semantics;
- explicit verifier and correction stages;
- target prompt states that agent agreement is not evidence;
- randomized run order with a recorded seed and explicit repetitions.

Gate: registry, provenance, verifier order, correction recording, and stale-bank rejection tests pass.

## Round 3 — Separate red-team generation from evaluation · PASS

**Goal:** prevent adaptive attack generation from confounding treatment conditions.

Implemented:
- three probe classes: fully synthetic identifier, citation mismatch, real-source unsupported extrapolation;
- deterministic candidate generator in `attack_generation.py`;
- component-scoped RNG so generation does not alter global randomness;
- candidates are marked review-required and cannot silently become confirmatory truth;
- real PMID mismatch fixture has a source-resolution note.

Gate: identical seed reproduces candidate hashes; global RNG sequence is unchanged; probe registry validates all cases.

## Round 4 — Independent scoring and replay · PASS

**Goal:** remove “model says the model failed” as the primary measurement method.

Implemented:
- deterministic fact/identifier checks in `scoring.py`;
- correction repair evaluated separately from initial failure;
- blinded human packet generation with a separate identity key;
- per-dimension Fleiss κ support;
- deterministic replay manifest;
- Wilson confidence intervals and risk differences for machine-checkable binary outcomes;
- no composite score and no model ranking in the pilot.

Gate: human-rating fixture parses, perfect-agreement control yields κ=1, replay hash is stable, and a full 18-row fixture run passes the result regression gate.

## Round 5 — CI, documentation and release boundary · PASS

**Goal:** make every future change prove that the experiment is still reproducible.

Implemented:
- GitHub Actions runs unit tests, asset validation, replay snapshot comparison, full fixture dry-run, result regression, and human-rating parser;
- committed validation and replay snapshots;
- `README.md`, rating guide, and upstream design notes updated;
- claim ceiling states that harness validation is not evidence that the research hypothesis is true.

Gate: local final suite must pass before merge; GitHub Actions must pass on the final commit before the PR is merged.

## Final claim ceiling

What completion proves:
- the experiment assets are internally consistent;
- attack content is frozen and bound to the exact case text;
- treatment conditions are replayable;
- run provenance is preserved;
- blind human-rating workflow exists;
- CI can detect schema/replay regressions.

What it does **not** prove:
- multi-agent consensus actually increases epistemic-boundary failure;
- the effect generalizes across model families;
- the human constructs have adequate reliability on real outputs;
- any safety, clinical, or prevalence claim.

The next evidence gate is a real-model pilot using frozen model IDs and independently verified truth manifests. That is data collection, not further framework expansion.
