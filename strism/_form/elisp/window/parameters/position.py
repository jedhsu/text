"""

    Position Window Parameters

"""

from typing import Literal
from dataclasses import dataclass

__all__ = [
    "BasicWindowParameters",
]


@dataclass
class BasicWindowParameters(
    PositionParameters,
):
    left: Pixel
    top: Pixel
    icon_left: Pixel
    icon_top: Pixel
    user_position: bool
