#!/usr/bin/env python3
"""Build a simple Markdown report from repeated-prompt JSONL outputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean
from typing import List, Dict, Any


SCORE_KEYS = [
    "surface_consistency",
    "evidence_stability",
    "boundary_stability",
    "decision_stability",
    "drift_signal",
    "pseudo_consistency_signal",
]


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def avg_score(rows: List[Dict[str, Any]], key: str):
    vals = []
    for row in rows:
        value = row.get("manual_scores", {}).get(key)
        if isinstance(value, (int, float)):
            vals.append(value)
    return round(mean(vals), 2) if vals else "N/A"


def build_report(rows: List[Dict[str, Any]]) -> str:
    prompt = rows[0]["prompt"] if rows else ""
    provider = rows[0]["provider"] if rows else ""
    rounds = len(rows)
    score_table = "\n".join([f"| {key} | {avg_score(rows, key)} |" for key in SCORE_KEYS])
    samples = "\n\n".join([f"### Round {row['round']}\n\n{row['answer']}" for row in rows[:5]])

    return f"""# LLM Stability Evaluation Report

## 1. Test Setup

| Field | Value |
|---|---|
| Provider | {provider} |
| Rounds | {rounds} |
| Prompt | {prompt} |

## 2. Average Manual Scores

| Metric | Average |
|---|---|
{score_table}

## 3. Observed Drift Notes

Fill this section manually after reviewing the repeated outputs.

Suggested checks:

- Did the final recommendation change?
- Did uncertainty disappear or appear across rounds?
- Did evidence density change?
- Did the answer become more generic?
- Did the model repeat the same surface structure while changing its internal emphasis?

## 4. Pseudo-Consistency Check

Pseudo-consistency means:

> The answer looks stable on the surface, but the reasoning emphasis, evidence basis, boundary condition, or final decision gradually changes across repeated outputs.

Assessment:

- [ ] No obvious pseudo-consistency
- [ ] Mild pseudo-consistency
- [ ] Strong pseudo-consistency
- [ ] Requires more rounds

## 5. Sample Outputs

{samples}

## 6. Deployment Note

This report is a lightweight behavioral observation artifact. It should be used together with standard benchmarks, domain expert review, safety review, and real-world monitoring.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    rows = load_jsonl(args.input)
    report = build_report(rows)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(report, encoding="utf-8")
    print(f"Wrote report to {args.out}")


if __name__ == "__main__":
    main()
