"""

    *Element Width*

  The width shaping dimension.

"""

from abc import ABCMeta

from ._dimension import ElementShapingDimension

__all__ = ["ElementWidthDimension"]


class ElementWidthDimension(
    ElementShapingDimension,
):
    __metaclass__ = ABCMeta
