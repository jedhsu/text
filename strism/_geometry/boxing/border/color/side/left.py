"""

    *Border-Left Color*

  The color of the left border.

"""

from ._side import BorderSideColor

__all__ = ["BorderLeftColor"]


class BorderLeftColor(
    BorderSideColor,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        return super(BorderLeftColor, self).__init__(
            *args,
            **kwargs,
        )
