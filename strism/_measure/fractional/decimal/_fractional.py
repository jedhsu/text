"""

    Decimal Fractional

  The base 10 fractional measure.

"""

from abc import ABCMeta

from .._fractional import Fractional


class DecimalFractional(
    Fractional,
):
    __metaclass__ = ABCMeta
