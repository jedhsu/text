"""

    *Element Width*

"""

from strism._geoshape import Pixel

from ._dimension import Dimension

__all__ = ["ElementWidth"]


class ElementWidth(
    Pixel,
    Dimension,
):
    def __init__(
        self,
        width: int,
    ):
        super(ElementWidth, self).__init__(
            width,
        )
