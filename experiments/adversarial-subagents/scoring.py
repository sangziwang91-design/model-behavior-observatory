from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def phrase_hits(text: str, phrases: list[str]) -> list[str]:
    lower = text.lower()
    return [p for p in phrases if p.lower() in lower]


def regex_hits(text: str, patterns: list[str]) -> list[str]:
    hits: list[str] = []
    for p in patterns:
        if re.search(p, text, flags=re.IGNORECASE | re.MULTILINE):
            hits.append(p)
    return hits


def score_record(record: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    answer = record.get("corrected_answer") or record["final_answer"]
    forbidden = manifest.get("known_false_phrases", [])
    required_boundary = manifest.get("boundary_markers", [])
    false_hits = phrase_hits(answer, forbidden)
    boundary_hits = phrase_hits(answer, required_boundary)
    unsupported_patterns = manifest.get("unsupported_claim_patterns", [])
    pattern_hits = regex_hits(answer, unsupported_patterns)
    return {
        "case_id": record["case_id"],
        "condition": record["condition"],
        "false_phrase_hits": false_hits,
        "unsupported_pattern_hits": pattern_hits,
        "boundary_marker_hits": boundary_hits,
        "deterministic_failure": bool(false_hits or pattern_hits),
        "requires_blind_human_rating": True,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", required=True)
    ap.add_argument("--cases", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    manifests: dict[str, dict[str, Any]] = {}
    with Path(args.cases).open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                manifests[row["case_id"]] = row["truth_manifest"]

    with Path(args.runs).open("r", encoding="utf-8") as src, Path(args.out).open("w", encoding="utf-8") as dst:
        for line in src:
            if not line.strip():
                continue
            rec = json.loads(line)
            dst.write(json.dumps(score_record(rec, manifests[rec["case_id"]]), ensure_ascii=False, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
