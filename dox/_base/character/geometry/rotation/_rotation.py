"""

    *Character Rotation*

  The position character along the rotation axis.

"""

from typing import Literal

from .._geometric import CharacterGeometric

from .css import CssTextOrientation

__all__ = ["CharacterRotation"]


class CharacterRotation(
    CssTextOrientation,
    CharacterGeometric,
):
    def __init__(
        self,
        val: Literal[
            "mixed",
            "upright",
            "sideways",
        ],
    ):
        pass
