"""

    *Color*

  A measure of graphical color.

"""

from abc import ABCMeta


from .._graphical import GraphicalMeasure


__all__ = ["Color"]


class Color(
    GraphicalMeasure,
):
    __metaclass__ = ABCMeta
