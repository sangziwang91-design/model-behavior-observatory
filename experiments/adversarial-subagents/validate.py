from __future__ import annotations

import argparse
import json
from pathlib import Path

from attack_bank import load_attack_bank, sha256_file, validate_attack_bank
from protocols import get_protocol
from replay import replay_manifest
from runner import case_sha256, load_cases, load_json


def validate_all(config_path: str, cases_path: str, attack_bank_path: str) -> dict[str, object]:
    config = load_json(config_path)
    conditions = config["conditions"]
    for condition in conditions:
        get_protocol(condition)
    cases = load_cases(cases_path)
    bank = load_attack_bank(attack_bank_path)

    stale = []
    missing = []
    for case in cases:
        bundle = bank.get(case.case_id)
        if any(get_protocol(condition).uses_attack for condition in conditions):
            if bundle is None:
                missing.append(case.case_id)
            elif bundle.source_case_sha256 != case_sha256(case):
                stale.append(case.case_id)
    if missing:
        raise ValueError(f"attack bank missing case(s): {missing}")
    if stale:
        raise ValueError(f"attack bank stale for case(s): {stale}")

    replay_a = replay_manifest(cases_path, attack_bank_path, conditions)
    replay_b = replay_manifest(cases_path, attack_bank_path, conditions)
    if replay_a["manifest_sha256"] != replay_b["manifest_sha256"]:
        raise AssertionError("deterministic replay manifest changed between identical builds")

    rows = replay_a["rows"]
    by_case: dict[str, dict[str, dict[str, object]]] = {}
    for row in rows:
        by_case.setdefault(str(row["case_id"]), {})[str(row["condition"])] = row
    for case_id, condition_rows in by_case.items():
        controls = [condition_rows[name] for name in ("static_attack", "single_agent", "multi_agent_consensus") if name in condition_rows]
        if controls:
            content_hashes = {row["attack_content_sha256"] for row in controls}
            semantic_hashes = {row["semantic_payload_sha256"] for row in controls}
            if len(content_hashes) != 1 or len(semantic_hashes) != 1:
                raise AssertionError(f"matched-context controls diverged for {case_id}")

    return {
        "status": "PASS",
        "conditions": conditions,
        "case_records": len(cases),
        "attack_bank": validate_attack_bank(attack_bank_path),
        "cases_sha256": sha256_file(cases_path),
        "config_sha256": sha256_file(config_path),
        "replay_manifest_sha256": replay_a["manifest_sha256"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate adversarial sub-agent experiment assets")
    parser.add_argument("--config", required=True)
    parser.add_argument("--cases", required=True)
    parser.add_argument("--attack-bank", required=True)
    parser.add_argument("--out")
    args = parser.parse_args()
    report = validate_all(args.config, args.cases, args.attack_bank)
    rendered = json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True)
    if args.out:
        Path(args.out).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
