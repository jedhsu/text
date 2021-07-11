"""

    *Element Maximum-Dimension*

"""

from abc import ABCMeta

from .._bound import ElementShapeBound

__all__ = ["ElementMaximumDimension"]


class ElementMaximumDimension(
    ElementShapeBound,
):
    __metaclass__ = ABCMeta
