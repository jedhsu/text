"""

    *Border-Top Color*

  The color of the top border.

"""

from ._side import BorderSideColor

__all__ = ["BorderTopColor"]


class BorderTopColor(
    BorderSideColor,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        return super(BorderTopColor, self).__init__(
            *args,
            **kwargs,
        )
