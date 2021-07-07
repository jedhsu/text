"""

    Graphical Distance

  A graphical distance measure.

"""

from abc import ABCMeta


from wich.measure.distance import Distance

from .._graphical import GraphicalMeasure


__all__ = [
    "GraphicalDistance",
]


class GraphicalDistance(
    GraphicalMeasure,
    Distance,
):
    __metaclass__ = ABCMeta
