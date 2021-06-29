"""

Dimension

"""

from abc import ABCMeta
from dataclasses import dataclass

__all__ = ["Dimension"]

from .numeric import Number
from ._unit import UnitMeasure


@dataclass
class Dimension:
    __metaclass__ = ABCMeta

    number: Number
    unit: UnitMeasure
