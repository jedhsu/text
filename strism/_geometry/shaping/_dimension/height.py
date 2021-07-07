"""

    *ElementHeight*

  The height shaping dimension.

"""

from abc import ABCMeta

from ._dimension import ElementShapingDimension

__all__ = ["ElementHeightDimension"]


class ElementHeightDimension(
    ElementShapingDimension,
):
    __metaclass__ = ABCMeta
