"""

    Tenth

  The tenth fractional measure.

"""

from ._fractional import DecimalFractional

__all__ = [
    "Tenth",
]


class Tenth(
    DecimalFractional,
):
    denominator = 10
