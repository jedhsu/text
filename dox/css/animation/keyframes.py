from dataclasses import dataclass

from ..base import AtRule


@dataclass
class KeyFrames(AtRule):
    name: type

    from_: Offset
    to: Offset

    percentage: type
