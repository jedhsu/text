"""

    *Character-Key*

  An ordinary character key.

"""

from dataclasses import dataclass

from .._key import BaseKey

__all__ = ["CharacterKey"]


@dataclass
class CharacterKey(
    BaseKey,
):
    pass
