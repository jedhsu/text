"""

    *Angle Spectrum*

  A spectrum of angle.

"""

from dataclasses import dataclass

from ._color import Angle

__all__ = ["AngleSpectrum"]


@dataclass
class AngleSpectrum:
    left: Angle
    right: Angle

    @classmethod
    def create(
        cls,
        left: Angle,
        right: Angle,
    ):
        assert left < right, ValueError
        return cls(
            left,
            right,
        )


class RedBlue(AngleSpectrum):
    """
    Standard red blue.
    """

    def __init__(self):
        super(RedBlue, self).__init__(
            Angle(0),
            Angle(240),
        )
