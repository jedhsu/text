"""

    *Angle*

  The "equator ring" of the bicone.

  Hue.

"""

from __future__ import annotations
from dataclasses import dataclass

from typing import Annotated

from .._color import Color

__all__ = ["Angle"]


@dataclass
class Angle(
    int,
    Annotated[Color, int],
):

    # def __prepare__(
    #     cls,
    #     bases,
    #     dict,
    #     value,
    # ):
    #     dict["value"] = value

    # def __new__(
    #     cls,
    #     value: int,
    # ):
    #     cls.value = value
    #     return cls

    def __init__(
        self,
        value: int,
    ):
        assert 0 <= value <= 360, ValueError
        super(Angle, self).__new__(
            int,
            value,
        )
