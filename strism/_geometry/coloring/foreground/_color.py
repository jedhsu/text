"""

    *Foreground-Color*

  The color of the element foreground.

"""

from strism._measure.graphical.color import Color

__all__ = ["ForegroundColor"]


class ForegroundColor(
    Color,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(ForegroundColor, self).__init__(
            *args,
            **kwargs,
        )
