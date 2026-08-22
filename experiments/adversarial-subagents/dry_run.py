from __future__ import annotations

import argparse
import json
from pathlib import Path

from attack_bank import canonical_json, load_attack_bank, sha256_file
from regression import validate_result_jsonl
from runner import AgentSpec, FixtureClient, load_cases, load_json, run_condition


def dry_run(config_path: str, cases_path: str, attack_bank_path: str, out_path: str) -> dict[str, object]:
    config = load_json(config_path)
    conditions = config["conditions"]
    cases = load_cases(cases_path)
    bank = load_attack_bank(attack_bank_path)
    target_calls_per_case = sum(2 if condition == "correction_challenge" else 1 for condition in conditions)
    verifier_calls_per_case = sum(1 for condition in conditions if condition == "consensus_plus_verifier")
    agents = {"target": AgentSpec("target", "target", "fixture-model", "fixture target"), "verifier": AgentSpec("verifier", "verifier", "fixture-verifier", "fixture verifier")}
    client = FixtureClient({"target": ["I cannot verify the premise; available evidence is insufficient."] * (target_calls_per_case * len(cases)), "verifier": ["The attack premise is unsupported by the supplied truth manifest."] * (verifier_calls_per_case * len(cases))})
    bank_sha = sha256_file(attack_bank_path)
    rows = []
    for case in sorted(cases, key=lambda item: item.case_id):
        for condition in conditions:
            rows.append(run_condition(case=case, condition=condition, agents=agents, client=client, attack_bundle=bank.get(case.case_id), bank_sha256=bank_sha))
    destination = Path(out_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(canonical_json(row) + "\n")
    regression = validate_result_jsonl(destination)
    return {"status": "PASS", "rows": len(rows), "regression": regression}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the full experiment topology with deterministic fixture models")
    parser.add_argument("--config", required=True)
    parser.add_argument("--cases", required=True)
    parser.add_argument("--attack-bank", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    print(json.dumps(dry_run(args.config, args.cases, args.attack_bank, args.out), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
