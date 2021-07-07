"""

    *Character*

  A character is an abstract character with geometry.

"""


@dataclass
class Character(
    AbstractCharacter,
):
    geometry: CharacterGeometry
