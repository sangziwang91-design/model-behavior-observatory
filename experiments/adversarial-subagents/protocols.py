from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class ProtocolSpec:
    """A condition-level information-flow protocol.

    The protocol controls only presentation/topology. Attack content is supplied
    from a frozen bank so generation and evaluation are separated.
    """

    name: str
    uses_attack: bool
    presentation: str
    uses_verifier: bool = False
    correction_round: bool = False
    description: str = ""


_PROTOCOLS: dict[str, ProtocolSpec] = {}


def register_protocol(spec: ProtocolSpec) -> ProtocolSpec:
    if spec.name in _PROTOCOLS:
        raise ValueError(f"protocol already registered: {spec.name}")
    _PROTOCOLS[spec.name] = spec
    return spec


def get_protocol(name: str) -> ProtocolSpec:
    try:
        return _PROTOCOLS[name]
    except KeyError as exc:
        raise ValueError(f"unknown protocol: {name}") from exc


def list_protocols() -> tuple[str, ...]:
    return tuple(sorted(_PROTOCOLS))


def iter_protocols(names: Iterable[str]) -> list[ProtocolSpec]:
    return [get_protocol(name) for name in names]


register_protocol(
    ProtocolSpec(
        name="baseline",
        uses_attack=False,
        presentation="none",
        description="Single-shot target baseline with no attack context.",
    )
)
register_protocol(
    ProtocolSpec(
        name="static_attack",
        uses_attack=True,
        presentation="anonymous",
        description="Matched-context control: frozen attack content without agent identity.",
    )
)
register_protocol(
    ProtocolSpec(
        name="single_agent",
        uses_attack=True,
        presentation="single_agent",
        description="Same frozen attack content attributed to one sub-agent.",
    )
)
register_protocol(
    ProtocolSpec(
        name="multi_agent_consensus",
        uses_attack=True,
        presentation="multi_agent",
        description="Same frozen attack components attributed to two agreeing sub-agents.",
    )
)
register_protocol(
    ProtocolSpec(
        name="consensus_plus_verifier",
        uses_attack=True,
        presentation="multi_agent",
        uses_verifier=True,
        description="Multi-agent attack plus an evidence-constrained verifier memo.",
    )
)
register_protocol(
    ProtocolSpec(
        name="correction_challenge",
        uses_attack=True,
        presentation="multi_agent",
        correction_round=True,
        description="Multi-agent attack followed by an explicit correction challenge.",
    )
)
