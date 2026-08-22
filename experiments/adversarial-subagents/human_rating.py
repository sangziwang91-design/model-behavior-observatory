from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


REQUIRED_COLUMNS = {"output_id", "rater_id", "boundary_retention", "structured_completion", "retraction_integrity"}
DIMENSIONS = ("boundary_retention", "structured_completion", "retraction_integrity")


def fleiss_kappa(rows: Iterable[list[int]], categories: list[int]) -> float:
    matrix = list(rows)
    if not matrix:
        raise ValueError("no rating rows")
    n_raters = sum(matrix[0])
    if n_raters < 2:
        raise ValueError("at least two raters are required")
    if any(sum(row) != n_raters for row in matrix):
        raise ValueError("all items must have the same number of ratings")
    n_items = len(matrix)
    p_j = [sum(row[j] for row in matrix) / (n_items * n_raters) for j in range(len(categories))]
    p_bar = sum((sum(count * count for count in row) - n_raters) / (n_raters * (n_raters - 1)) for row in matrix) / n_items
    p_e = sum(p * p for p in p_j)
    if p_e == 1.0:
        return 1.0 if p_bar == 1.0 else 0.0
    return (p_bar - p_e) / (1.0 - p_e)


def load_ratings(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"rating CSV missing columns: {sorted(missing)}")
        return list(reader)


def agreement_report(path: str | Path) -> dict[str, object]:
    ratings = load_ratings(path)
    outputs = sorted({row["output_id"] for row in ratings})
    raters = sorted({row["rater_id"] for row in ratings})
    report: dict[str, object] = {"outputs": len(outputs), "raters": len(raters), "dimensions": {}}
    for dimension in DIMENSIONS:
        values = sorted({int(row[dimension]) for row in ratings if row[dimension] not in {"", "NA", "N/A"}})
        grouped: dict[str, Counter[int]] = defaultdict(Counter)
        for row in ratings:
            raw = row[dimension]
            if raw in {"", "NA", "N/A"}:
                continue
            grouped[row["output_id"]][int(raw)] += 1
        usable = [output_id for output_id in outputs if output_id in grouped]
        if not usable or not values:
            report["dimensions"][dimension] = {"kappa": None, "usable_outputs": 0}
            continue
        counts = [[grouped[output_id].get(value, 0) for value in values] for output_id in usable]
        rater_counts = {sum(row) for row in counts}
        if len(rater_counts) != 1 or next(iter(rater_counts)) < 2:
            report["dimensions"][dimension] = {"kappa": None, "usable_outputs": len(usable), "reason": "unbalanced_raters"}
            continue
        report["dimensions"][dimension] = {
            "kappa": round(fleiss_kappa(counts, values), 6),
            "usable_outputs": len(usable),
            "categories": values,
            "ratings_per_output": next(iter(rater_counts)),
        }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute blinded human-rating agreement")
    parser.add_argument("ratings_csv")
    args = parser.parse_args()
    print(json.dumps(agreement_report(args.ratings_csv), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
