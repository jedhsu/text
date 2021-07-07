"""

    Thousandth

  The thousandth fractional measure.

"""

from ._fractional import DecimalFractional

__all__ = [
    "Thousandth",
]


class Thousandth(
    DecimalFractional,
):
    denominator = 1000
