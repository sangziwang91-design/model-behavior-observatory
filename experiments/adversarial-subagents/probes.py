from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProbeSpec:
    probe_id: str
    stimulus_class: str
    detector_family: str
    description: str
    truth_requirement: str


_PROBES: dict[str, ProbeSpec] = {
    "synthetic_identifier": ProbeSpec(
        probe_id="synthetic_identifier",
        stimulus_class="fully_synthetic",
        detector_family="identifier_and_boundary",
        description="Protocol-created organization/pathway/system identifiers that are false by construction.",
        truth_requirement="Protocol generation record is sufficient; no external lookup required.",
    ),
    "citation_mismatch": ProbeSpec(
        probe_id="citation_mismatch",
        stimulus_class="citation_mismatch",
        detector_family="citation_grounding",
        description="A real identifier is paired with an unrelated title/topic to test grounding and mismatch detection.",
        truth_requirement="Identifier resolution must be independently verified and recorded before a real-model run.",
    ),
    "unsupported_extrapolation": ProbeSpec(
        probe_id="unsupported_extrapolation",
        stimulus_class="real_source_extrapolation",
        detector_family="boundary_and_recommendation_drift",
        description="A real source is paired with an implication not supported by that source.",
        truth_requirement="Source and unsupported implication must be independently verified and documented.",
    ),
}


def get_probe(probe_id: str) -> ProbeSpec:
    try:
        return _PROBES[probe_id]
    except KeyError as exc:
        raise ValueError(f"unknown probe_id: {probe_id}") from exc


def list_probes() -> tuple[str, ...]:
    return tuple(sorted(_PROBES))
