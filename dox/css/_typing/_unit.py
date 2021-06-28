"""

Unit

Type class representing a unit of measure.

"""

from abc import ABCMeta

__all__ = ["UnitMeasure"]

from ._type import Type


class UnitMeasure(
    Type,
):
    __metaclass__ = ABCMeta
