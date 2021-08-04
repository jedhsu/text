"""

    *Inner-Frame-Shape*

"""

from ._shape import Shape

from wich.measure.distance.graphical import Pixel

__all__ = ["InnerFrameSahep"]


class InnerFrameShape(
    Shape,
):
    def __init__(
        self,
        width: Pixel,
        height: Pixel,
    ):
        super(InnerFrameShape, self).__init__(
            width,
            height,
        )
