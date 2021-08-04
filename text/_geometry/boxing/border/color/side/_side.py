"""

    *Border-Side Color*

  The color of a border-side.

"""

from abc import ABCMeta

from .._color import BorderColor

__all__ = ["BorderSideColor"]


class BorderSideColor(
    BorderColor,
):
    __metaclass__ = ABCMeta
