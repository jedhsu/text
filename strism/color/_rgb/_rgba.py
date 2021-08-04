"""

    *Rgba*

  The color spectral measure using the RGBA system.

"""

from dataclasses import dataclass


# from wich.measure.spectral import Spectral

from .red import Red
from .green import Green
from .blue import Blue


__all__ = [
    "Rgba",
]


@dataclass
class Rgba(
    # Spectral,
    # GraphicalColor,
):
    red: Red
    green: Green
    blue: Blue

    @classmethod
    def create(
        cls,
        red: int,
        green: int,
        blue: int,
    ):
        return cls(
            Red(red),
            Green(green),
            Blue(blue),
        )
