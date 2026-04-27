#!/usr/bin/env python3
"""
Repeated Prompt Runner

Public minimal runner for repeated-prompt evaluation.

Providers:
- mock: offline demo mode
- openai_compatible: any OpenAI-compatible chat completion endpoint

Environment variables for openai_compatible:
- LLM_API_KEY
- LLM_BASE_URL
- LLM_MODEL
"""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.request
from pathlib import Path
from typing import Dict, Any


def call_mock(prompt: str, round_id: int) -> str:
    variants = [
        "The main risks include factual errors, overconfidence, missing context, and unclear accountability.",
        "Key risks are hallucination, inconsistent reasoning, weak evidence grounding, and unsafe recommendations.",
        "Primary concerns include reliability, drift across repeated use, lack of domain context, and poor escalation handling.",
        "The main deployment risks are inaccurate responses, unstable boundary handling, insufficient evidence, and failure to defer to professionals.",
        "Risks include over-trust, missing uncertainty signals, inconsistent advice, and weak auditability.",
    ]
    return variants[(round_id - 1) % len(variants)]


def call_openai_compatible(prompt: str) -> str:
    api_key = os.environ.get("LLM_API_KEY")
    base_url = os.environ.get("LLM_BASE_URL", "").rstrip("/")
    model = os.environ.get("LLM_MODEL")

    if not api_key or not base_url or not model:
        raise RuntimeError("Missing environment variables: LLM_API_KEY, LLM_BASE_URL, LLM_MODEL")

    url = f"{base_url}/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def run(prompt: str, rounds: int, provider: str, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)

    with out.open("w", encoding="utf-8") as f:
        for i in range(1, rounds + 1):
            started = time.time()
            if provider == "mock":
                answer = call_mock(prompt, i)
            elif provider == "openai_compatible":
                answer = call_openai_compatible(prompt)
            else:
                raise ValueError(f"Unsupported provider: {provider}")

            record: Dict[str, Any] = {
                "round": i,
                "prompt": prompt,
                "provider": provider,
                "answer": answer,
                "latency_sec": round(time.time() - started, 3),
                "manual_scores": {
                    "surface_consistency": None,
                    "evidence_stability": None,
                    "boundary_stability": None,
                    "decision_stability": None,
                    "drift_signal": None,
                    "pseudo_consistency_signal": None,
                },
                "notes": "",
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Wrote {rounds} records to {out}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--rounds", type=int, default=5)
    parser.add_argument("--provider", choices=["mock", "openai_compatible"], default="mock")
    parser.add_argument("--out", type=Path, default=Path("outputs/run.jsonl"))
    args = parser.parse_args()
    run(args.prompt, args.rounds, args.provider, args.out)


if __name__ == "__main__":
    main()
