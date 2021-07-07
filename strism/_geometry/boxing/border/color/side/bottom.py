"""

    *Border-Bottom Color*

  The color of the bottom border.

"""

from ._side import BorderSideColor

__all__ = ["BorderBottomColor"]


class BorderBottomColor(
    BorderSideColor,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        return super(BorderBottomColor, self).__init__(
            *args,
            **kwargs,
        )
