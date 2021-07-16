"""

    *Key*

  A sequence of key atoms.

"""

from abc import ABCMeta
from dataclasses import dataclass

from typing import Optional
from typing import Sequence

from .atom import KeyAtom
from .binding import KeyBinding

__all__ = ["Key"]


@dataclass
class Key:
    __metaclass__ = ABCMeta

    parts: Sequence[KeyAtom]
    binding: Optional[KeyBinding]

    @classmethod
    def create(
        cls,
        *part: KeyAtom,
        binding: Optional[KeyBinding] = None,
    ):
        return cls(
            [*part],
            binding,
        )
