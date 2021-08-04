"""

    Window Divider

  A window divider.

"""


from wich.editor._element.shape import ElementWidth
from wich.editor._element.shape import ElementHeight

from .._element import WindowElement

__all__ = [
    "WindowDivider",
]


class WindowDivider(
    WindowElement,
):
    def __init__(
        self,
        width: ElementWidth,
        height: ElementHeight,
    ):
        super(WindowDivider, self).__init__(
            width,
            height,
        )
