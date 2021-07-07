"""

    Hundredth

  The tenth fractional measure.

"""

from ._fractional import DecimalFractional

__all__ = [
    "Half",
]


class Tenth(
    DecimalFractional,
):
    denominator = 10

