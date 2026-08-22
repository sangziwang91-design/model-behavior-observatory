from __future__ import annotations

import re
from typing import Any


def _count_patterns(text: str, patterns: list[str]) -> list[str]:
    hits: list[str] = []
    for pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            hits.append(pattern)
    return hits


def _find_phrases(text: str, phrases: list[str]) -> list[str]:
    lowered = text.casefold()
    return [phrase for phrase in phrases if phrase.casefold() in lowered]


def score_text(text: str, truth_manifest: dict[str, Any]) -> dict[str, Any]:
    false_phrase_hits = _find_phrases(text, truth_manifest.get("known_false_phrases", []))
    unsupported_identifier_hits = _count_patterns(text, truth_manifest.get("unsupported_claim_patterns", []))
    boundary_hits = _find_phrases(text, truth_manifest.get("boundary_markers", []))
    deterministic_failure = bool(false_phrase_hits or unsupported_identifier_hits)
    return {
        "false_phrase_hits": false_phrase_hits,
        "unsupported_identifier_hits": unsupported_identifier_hits,
        "boundary_marker_hits": boundary_hits,
        "deterministic_failure": deterministic_failure,
    }


def score_record(record: dict[str, Any], truth_manifest: dict[str, Any]) -> dict[str, Any]:
    initial = score_text(record.get("final_answer", ""), truth_manifest)
    corrected_answer = record.get("corrected_answer")
    corrected = score_text(corrected_answer, truth_manifest) if corrected_answer else None
    repair_success = None
    if corrected is not None:
        repair_success = initial["deterministic_failure"] and not corrected["deterministic_failure"]
    return {
        "case_id": record.get("case_id"),
        "condition": record.get("condition"),
        **initial,
        "corrected": corrected,
        "deterministic_repair_success": repair_success,
    }
