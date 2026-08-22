# Adversarial Sub-Agent Experiment v0.2

A reproducible experiment for testing whether **agent information-flow topology**, rather than attack content alone, changes a target LLM's epistemic-boundary behavior.

This directory is part of the Model Behavior Observatory. It is not an autonomous-agent demo and it is not a validated safety benchmark. The unit of analysis is the target model's observable response under controlled orchestration conditions.

## Research question

When the factual content is held constant, does presenting the same adversarial material as anonymous context, one sub-agent's analysis, or multiple agreeing sub-agents change the target model's tendency to accept unsupported premises, build unsupported structures, or fail to retract them after challenge?

## Six conditions

| Condition | Attack content | Intended manipulation |
|---|---|---|
| `baseline` | none | single-shot baseline |
| `static_attack` | frozen | anonymous matched-context control |
| `single_agent` | same frozen payload | one-agent identity label |
| `multi_agent_consensus` | same frozen payload | two-agent consensus label |
| `consensus_plus_verifier` | same frozen payload | evidence-constrained defensive verifier |
| `correction_challenge` | same frozen payload | post-answer retraction integrity |

`static_attack`, `single_agent`, and `multi_agent_consensus` share the exact same `attack_content_sha256` and `semantic_payload_sha256`. Their rendered target prompt differs only in the intended presentation/topology labels.

## Architecture

```text
Case bank / truth manifest
        |
        +--> Probe registry
        |
Candidate attack generation  -- review -->  Frozen attack bank
                                            |
                                            v
                                   Protocol / information flow
                                            |
                                            v
                                     Target model
                                            |
                  +-------------------------+----------------------+
                  |                                                |
          deterministic scorer                           blinded human packet
          manifest-checkable facts                       separate identity key
                  |                                                |
                  +-------------------------+----------------------+
                                            |
                                  analysis + raw JSONL logs
```

The split follows a simple rule: **generation, execution, scoring, and verification are different jobs and may not certify one another.**

## Truth classes

1. `fully_synthetic` — identifiers created by the protocol; false by construction.
2. `citation_mismatch` — a real PMID/DOI is paired with unrelated claims; identifier resolution must be independently checked.
3. `real_source_extrapolation` — source may be real, but the requested implication is stronger than the source supports.

Do not pool these as a single “hallucination” class in analysis.

## Reproducibility controls

Every real run records:
- Git commit;
- case and truth-manifest SHA-256;
- frozen attack-bank SHA-256 and attack-content SHA-256;
- target-input and semantic-payload SHA-256;
- model IDs, roles, temperature, endpoint configuration;
- full prompts and outputs with per-message hashes;
- randomization seed and replicate index;
- initial and corrected answers separately.

A frozen attack bundle is rejected if the source case changes after freezing.

## Validate before any API call

```bash
cd experiments/adversarial-subagents
python -m unittest discover -v -p 'test_*.py'
python validate.py \
  --config protocol.example.json \
  --cases fixtures/seed_cases.jsonl \
  --attack-bank fixtures/frozen_attack_bank.jsonl
```

Build a deterministic replay manifest:

```bash
python replay.py \
  --cases fixtures/seed_cases.jsonl \
  --attack-bank fixtures/frozen_attack_bank.jsonl \
  --conditions baseline static_attack single_agent multi_agent_consensus consensus_plus_verifier correction_challenge
```

Run the full topology without external APIs:

```bash
python dry_run.py \
  --config protocol.example.json \
  --cases fixtures/seed_cases.jsonl \
  --attack-bank fixtures/frozen_attack_bank.jsonl \
  --out /tmp/adversarial-subagents-dry.jsonl
python regression.py /tmp/adversarial-subagents-dry.jsonl
```

## Real-model execution

Copy `protocol.example.json` to a non-committed local config and replace placeholder model IDs/endpoints with **frozen exact identifiers**. Then run:

```bash
python runner.py \
  --config protocol.local.json \
  --cases fixtures/seed_cases.jsonl \
  --attack-bank fixtures/frozen_attack_bank.jsonl \
  --out runs/pilot-001.jsonl \
  --seed 20260822 \
  --repetitions 2
```

Do not regenerate attacks during this target run.

## Scoring

Machine-checkable outcomes stay separate from human-coded outcomes.

### Deterministic
- known-false phrase hits;
- unsupported identifier/pattern hits;
- explicit boundary markers;
- deterministic correction repair.

### Blinded human coding
- boundary retention;
- structured completion;
- retraction integrity.

Create a blinded packet and a separate key:

```bash
python rating_packet.py \
  --results runs/pilot-001.jsonl \
  --packet runs/pilot-001.rater-packet.csv \
  --key runs/pilot-001.identity-key.csv \
  --n 30 --seed 20260822
```

After raters return scores, compute per-dimension agreement:

```bash
python human_rating.py ratings.csv
```

See `RATING_GUIDE.md`. An LLM judge may be used only as an auxiliary analysis, never as sole ground truth.

## Analysis

```bash
python analysis.py --results runs/pilot-001.jsonl --cases fixtures/seed_cases.jsonl
```

The default analysis reports manifest-checkable binary failure rates, Wilson 95% intervals, and risk differences versus baseline. Do not invent a composite risk score for the first study.

## First real evidence gate

Recommended pilot:

```text
10 verified probes
× 6 conditions
× 2 repetitions
= 120 target responses
```

Then blind-rate 20–30 stratified outputs with 3–5 independent human raters. Expand only if the measurement constructs are reproducible and the topology effect survives matched-context controls.

## Five-round implementation record

See `FIVE_ROUND_EXECUTION.md`. The implemented line is:

1. frozen attack corpus and case binding;
2. explicit protocol/information-flow controls;
3. independent probe and candidate-attack generation layer;
4. deterministic + blinded-human scoring and replay;
5. CI, immutable snapshots, documentation and claim ceiling.

## Upstream design lineage

The architecture selectively absorbs patterns from Inspect AI, UK AISI's debate-iteration-environment, Microsoft PyRIT, Promptfoo, and NVIDIA Garak without copying their source code or adding them as required runtime dependencies. Exact inspected revisions and local mappings are in `UPSTREAM_DESIGN_NOTES.md`.

## Stop conditions

Pause or downgrade the hypothesis if:
- source provenance cannot be reconstructed;
- truth manifests contain unresolved factual disputes;
- matched-context controls do not actually share the same attack payload;
- blinded raters cannot reliably distinguish structured completion from ordinary factual hallucination;
- the apparent effect disappears after content/token/presentation controls;
- findings depend on one target model, attacker family, or one unverifiable truth case.

## Claim ceiling

Passing CI proves the **harness and frozen assets are internally reproducible**. It does not prove that multi-agent topology causes boundary failure, that the effect generalizes, or that any clinical/safety claim is established. Those require real-model data and independent human reliability evidence.
