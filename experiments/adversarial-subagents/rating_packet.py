from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from pathlib import Path


def build_rating_packet(results_path: str | Path, packet_path: str | Path, key_path: str | Path, n: int, seed: int) -> dict[str, object]:
    rows = []
    with Path(results_path).open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    if not rows:
        raise ValueError("no result rows")
    rng = random.Random(seed)
    indices = list(range(len(rows)))
    rng.shuffle(indices)
    selected = indices[: min(n, len(indices))]
    packet_rows = []
    key_rows = []
    for ordinal, index in enumerate(selected, start=1):
        row = rows[index]
        output_id = f"O{ordinal:04d}-{hashlib.sha256((str(row['case_id']) + str(row['condition']) + str(index)).encode()).hexdigest()[:8]}"
        packet_rows.append(
            {
                "output_id": output_id,
                "initial_answer": row.get("final_answer", ""),
                "corrected_answer": row.get("corrected_answer") or "",
            }
        )
        key_rows.append(
            {
                "output_id": output_id,
                "case_id": row["case_id"],
                "condition": row["condition"],
                "probe_id": row.get("probe_id", ""),
                "target_input_sha256": row.get("target_input_sha256", ""),
            }
        )
    for path, fieldnames, data in (
        (packet_path, ["output_id", "initial_answer", "corrected_answer"], packet_rows),
        (key_path, ["output_id", "case_id", "condition", "probe_id", "target_input_sha256"], key_rows),
    ):
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    return {"status": "PASS", "sampled": len(packet_rows), "seed": seed}


def main() -> None:
    parser = argparse.ArgumentParser(description="Create blinded human-rating packet and separate identity key")
    parser.add_argument("--results", required=True)
    parser.add_argument("--packet", required=True)
    parser.add_argument("--key", required=True)
    parser.add_argument("--n", type=int, default=30)
    parser.add_argument("--seed", type=int, default=20260822)
    args = parser.parse_args()
    print(json.dumps(build_rating_packet(args.results, args.packet, args.key, args.n, args.seed), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
