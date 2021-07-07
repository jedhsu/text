"""

    *Character-Weight*

  Describes the character density.

  More precisely, measures covered space per character area.

"""

from enum import Enum

__all__ = ["CharacterWeight"]


class CharacterWeight(Enum):
    Light = "Light"
    Normal = "Normal"
    Bold = "Bold"

    # relative
    Lighter = "Lighter"
    Bolder = "Bolder"

    _100 = "100"
    _200 = "200"
    _300 = "300"
    _400 = "400"
    _500 = "500"
    _600 = "600"
    _700 = "700"
    _800 = "800"
    _900 = "900"


# [TODO] think about optimal init design


class FontWeight:
    pass
