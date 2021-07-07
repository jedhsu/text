"""

    Rgba

  The color spectral measure using the RGBA system.

"""

from dataclasses import dataclass


from wich.measure.spectral import Spectral

from .._color import GraphicalColor
from ..opacity import OpacitySpectral

from .red import RedSpectral
from .green import GreenSpectral
from .blue import BlueSpectral


__all__ = [
    "Rgba",
]


@dataclass
class Rgba(
    Spectral,
    GraphicalColor,
):
    red: RedSpectral
    green: GreenSpectral
    blue: BlueSpectral
    alpha: OpacitySpectral

    @classmethod
    def create(
        cls,
        red: int,
        green: int,
        blue: int,
        alpha: float,
    ):
        return cls(
            RedSpectral(red),
            GreenSpectral(green),
            BlueSpectral(blue),
            OpacitySpectral(alpha),
        )
