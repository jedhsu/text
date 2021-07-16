"""

    *Character-Key*

  An ordinary character key.

"""

from abc import ABCMeta

from dataclasses import dataclass

from .._key import BaseKey

__all__ = ["CharacterKey"]


@dataclass
class CharacterKey(
    BaseKey,
):
    __metaclass__ = ABCMeta
