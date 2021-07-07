"""

    Resolution

  A measure of resolution.

"""

from abc import ABCMeta

from .._graphical import GraphicalMeasure

__all__ = [
    "Graphical",
]


class Resolution(
    GraphicalMeasure,
):
    __metaclass__ = ABCMeta
