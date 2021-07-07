"""

    *Character*

  A character is an abstract character with geometry.

"""

from dataclasses import dataclass

from strism._abstract import AbstractCharacter

from .geometry import CharacterGeometry

__all__ = ["Character"]

@dataclass
class Character(
    AbstractCharacter,
):
    geometry: CharacterGeometry
