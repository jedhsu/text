"""

    Fractional

  The fractional measure.

"""

from fractions import Fraction

from wich.literal.integer import Integer

__all__ = [
    "Fractional",
]


class Fractional(
    Fraction,
):
    denominator: Integer

    def __init__(
        self,
        denominator: int,
    ):
        pass
