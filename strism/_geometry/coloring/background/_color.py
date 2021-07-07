"""

    *Background-Color*

  The background color of an element.

"""

from strism._measure.graphical.color import Color

__all__ = ["BackgroundColor"]


class BackgroundColor(
    Color,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(BackgroundColor, self).__init__(
            *args,
            **kwargs,
        )
