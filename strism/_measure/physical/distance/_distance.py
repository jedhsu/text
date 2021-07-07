"""

    Physical Distance

  A measure of physical distance.

"""

from abc import ABCMeta

from wich.measure.distance import Distance

from .._measure import PhysicalMeasure

__all__ = [
    "PhysicalDistance",
]


class PhysicalDistance(
    PhysicalMeasure,
    Distance,
):
    __metaclass__ = ABCMeta
