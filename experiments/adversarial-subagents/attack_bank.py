from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class AttackBundle:
    case_id: str
    bank_version: str
    authority_memo: str
    completion_memo: str
    generation: dict[str, Any]
    source_case_sha256: str

    def content_payload(self) -> str:
        return "\n\n".join((self.authority_memo, self.completion_memo))

    def content_sha256(self) -> str:
        return sha256_text(self.content_payload())


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_attack_bank(path: str | Path) -> dict[str, AttackBundle]:
    bank: dict[str, AttackBundle] = {}
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            bundle = AttackBundle(**row)
            if bundle.case_id in bank:
                raise ValueError(f"duplicate case_id in attack bank at line {line_number}: {bundle.case_id}")
            if not bundle.source_case_sha256:
                raise ValueError(f"missing source_case_sha256 for {bundle.case_id}")
            bank[bundle.case_id] = bundle
    if not bank:
        raise ValueError("attack bank is empty")
    return bank


def validate_attack_bank(path: str | Path) -> dict[str, Any]:
    bank = load_attack_bank(path)
    versions = sorted({bundle.bank_version for bundle in bank.values()})
    if len(versions) != 1:
        raise ValueError(f"attack bank mixes versions: {versions}")
    return {
        "records": len(bank),
        "bank_version": versions[0],
        "bank_sha256": sha256_file(path),
        "content_sha256": {case_id: bundle.content_sha256() for case_id, bundle in sorted(bank.items())},
    }


def write_attack_bank(path: str | Path, bundles: list[AttackBundle]) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        for bundle in sorted(bundles, key=lambda item: item.case_id):
            handle.write(canonical_json(asdict(bundle)) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a frozen attack bank")
    parser.add_argument("bank")
    args = parser.parse_args()
    print(json.dumps(validate_attack_bank(args.bank), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
