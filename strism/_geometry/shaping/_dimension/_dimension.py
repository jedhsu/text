"""

    *Element Shaping-Dimension*

"""

from abc import ABCMeta

from .._shaping import ElementShaping

__all__ = ["ElementShapingDimension"]


class ElementShapingDimension(
    ElementShaping,
):
    __metaclass__ = ABCMeta
