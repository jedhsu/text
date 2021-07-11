"""

    *Key-Atom*

  An atomic key, a single key event.

"""

from dataclasses import dataclass

from typing import Optional


from .base import BaseKey
from .modifier import ModifierKey

__all__ = ["KeyAtom"]


@dataclass
class KeyAtom:
    base: BaseKey
    modifier: Optional[ModifierKey]

    @classmethod
    def create(
        cls,
        base: BaseKey,
        modifier: Optional[ModifierKey] = None,
    ):
        return cls(
            base,
            modifier,
        )
