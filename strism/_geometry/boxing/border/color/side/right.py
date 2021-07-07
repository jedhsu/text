"""

    *Border-Right Color*

  The color of the right border.

"""

from ._side import BorderSideColor

__all__ = ["BorderRightColor"]


class BorderRightColor(
    BorderSideColor,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        return super(BorderRightColor, self).__init__(
            *args,
            **kwargs,
        )
