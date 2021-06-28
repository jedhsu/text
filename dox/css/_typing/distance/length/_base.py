"""

Unit Length

"""

from abc import ABCMeta

__all__ = ["UnitLength"]

from ..._unit import Unit


class UnitLength(
    Unit,
):
    __metaclass__ = ABCMeta
