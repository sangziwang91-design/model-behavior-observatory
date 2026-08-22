from __future__ import annotations

import argparse
import json
from pathlib import Path

from attack_bank import canonical_json, load_attack_bank, sha256_text
from protocols import get_protocol
from runner import build_target_input, load_cases


def replay_manifest(cases_path: str, attack_bank_path: str, conditions: list[str]) -> dict[str, object]:
    cases = load_cases(cases_path)
    bank = load_attack_bank(attack_bank_path)
    rows = []
    for case in sorted(cases, key=lambda item: item.case_id):
        for condition in conditions:
            protocol = get_protocol(condition)
            bundle = bank.get(case.case_id) if protocol.uses_attack else None
            built = build_target_input(case, condition, bundle)
            rows.append({"case_id": case.case_id, "condition": condition, "target_input_sha256": built["target_input_sha256"], "semantic_payload_sha256": built["semantic_payload_sha256"], "attack_content_sha256": built["attack_content_sha256"]})
    payload = canonical_json(rows)
    return {"rows": rows, "manifest_sha256": sha256_text(payload)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Build deterministic target-input replay manifest")
    parser.add_argument("--cases", required=True)
    parser.add_argument("--attack-bank", required=True)
    parser.add_argument("--conditions", nargs="+", required=True)
    parser.add_argument("--out")
    args = parser.parse_args()
    report = replay_manifest(args.cases, args.attack_bank, args.conditions)
    rendered = json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True)
    if args.out:
        Path(args.out).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
