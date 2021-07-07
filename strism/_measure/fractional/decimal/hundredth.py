"""

    Hundredth

  The hundredth fractional measure.

"""

from ._fractional import DecimalFractional

__all__ = [
    "Hundredth",
]


class Hundredth(
    DecimalFractional,
):
    denominator = 100
