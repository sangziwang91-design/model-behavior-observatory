from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

from runner import load_cases
from scoring import score_record


def wilson_interval(successes: int, total: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if total <= 0:
        return (float("nan"), float("nan"))
    p = successes / total
    denom = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denom
    margin = z * math.sqrt((p * (1 - p) + z * z / (4 * total)) / total) / denom
    return max(0.0, center - margin), min(1.0, center + margin)


def analyze_results(results_path: str | Path, cases_path: str | Path) -> dict[str, object]:
    manifests = {case.case_id: case.truth_manifest for case in load_cases(cases_path)}
    by_condition: dict[str, list[bool]] = defaultdict(list)
    with Path(results_path).open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            score = score_record(row, manifests[row["case_id"]])
            by_condition[row["condition"]].append(bool(score["deterministic_failure"]))
    summary: dict[str, object] = {}
    for condition, values in sorted(by_condition.items()):
        failures = sum(values)
        total = len(values)
        low, high = wilson_interval(failures, total)
        summary[condition] = {"n": total, "deterministic_failures": failures, "deterministic_failure_rate": round(failures / total, 6) if total else None, "wilson_95": [round(low, 6), round(high, 6)]}
    baseline = summary.get("baseline")
    if isinstance(baseline, dict) and baseline.get("deterministic_failure_rate") is not None:
        base_rate = float(baseline["deterministic_failure_rate"])
        for condition, row in summary.items():
            if isinstance(row, dict) and row.get("deterministic_failure_rate") is not None:
                row["risk_difference_vs_baseline"] = round(float(row["deterministic_failure_rate"]) - base_rate, 6)
    return {"metric": "manifest-checkable deterministic failure only", "conditions": summary}


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze deterministic outcomes without model ranking")
    parser.add_argument("--results", required=True)
    parser.add_argument("--cases", required=True)
    args = parser.parse_args()
    print(json.dumps(analyze_results(args.results, args.cases), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
