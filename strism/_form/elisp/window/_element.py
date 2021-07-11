"""

    Window Element

"""

from abc import ABCMeta

from wich.editor._element import Element


class WindowElement(
    Element,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        width: ElementWidth,
        height: ElementHeight,
    ):
        super(WindowElement, self).__init__(
            width,
            height,
        )
