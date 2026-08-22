from __future__ import annotations

import argparse
import json
from pathlib import Path


def validate_result_jsonl(path: str | Path) -> dict[str, object]:
    required = {"schema_version", "case_id", "probe_id", "condition", "case_sha256", "truth_manifest_sha256", "target_input_sha256", "semantic_payload_sha256", "transcript", "final_answer"}
    rows = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            missing = required - set(row)
            if missing:
                raise ValueError(f"result line {line_number} missing fields: {sorted(missing)}")
            if any(not turn.get("prompt_sha256") or not turn.get("output_sha256") for turn in row["transcript"]):
                raise ValueError(f"result line {line_number} has unhashed transcript turn")
            rows.append(row)
    if not rows:
        raise ValueError("result file is empty")
    return {"status": "PASS", "rows": len(rows), "schema_versions": sorted({row["schema_version"] for row in rows})}


def main() -> None:
    parser = argparse.ArgumentParser(description="Regression-gate a completed result JSONL")
    parser.add_argument("results")
    args = parser.parse_args()
    print(json.dumps(validate_result_jsonl(args.results), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
