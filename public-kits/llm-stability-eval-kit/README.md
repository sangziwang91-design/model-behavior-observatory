# LLM Stability Eval Kit

A lightweight public evaluation kit for repeated-prompt testing, output drift observation, and pseudo-consistency detection in LLM responses.

Chinese positioning: 大模型输出稳定性评测小工具。

## Why this exists

Most common LLM evaluations focus on single-run benchmark scores: accuracy, task completion, human preference, or domain-specific QA performance.

Those signals are useful, but they do not fully answer a practical deployment question:

> If I ask the same model the same question multiple times, or slightly perturb the question, does its evidence density, risk boundary, and final recommendation remain stable?

This kit is designed as a public, minimal, non-core evaluation layer.

It does not expose private control protocols, hidden scoring thresholds, proprietary prompt structures, or internal model-behavior control logic.

## Core use cases

- repeated-prompt evaluation
- output drift observation
- pseudo-consistency detection
- RAG answer stability testing
- fine-tuned model regression checking
- agent / workflow response stability review
- pre-deployment AI behavior sanity check

## What this kit tests

| Layer | Question |
|---|---|
| Surface consistency | Does the answer look similar across runs? |
| Evidence stability | Does the model rely on similar evidence? |
| Boundary stability | Does the model keep the same caveats and limits? |
| Decision stability | Does the final recommendation change? |
| Drift signal | Does the model gradually move to a different path? |
| Pseudo-consistency | Does surface stability hide internal change? |

## What this kit does not do

This is not a replacement for benchmarks such as MMLU, GSM8K, MATH, HumanEval, OpenCompass, or preference-arena evaluation.

It is a complementary behavioral observation layer:

> Benchmarks ask whether the model can answer.
>
> This kit asks whether the model remains behaviorally stable when answering repeatedly.

## Quick start

```bash
python src/repeated_prompt_runner.py \
  --prompt "What are the main risks of deploying a medical chatbot?" \
  --rounds 5 \
  --provider mock \
  --out outputs/sample_run.jsonl
```

Then build a report:

```bash
python src/build_report.py \
  --input outputs/sample_run.jsonl \
  --out outputs/sample_report.md
```

## Public safety boundary

Safe to publish:

- repeated-run testing idea
- output-drift vocabulary
- pseudo-consistency concept
- simple scoring table
- report template
- example cases

Not included:

- private ABS / MCF scoring weights
- seed injection mechanisms
- internal thresholds
- full behavioral control protocols
- customer audit internals
- non-public experimental data

## License

MIT for this public starter kit. Private audit systems and proprietary evaluation methods are not included.
