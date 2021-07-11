"""

    *Outer-Frame-Shape*

"""

from ._shape import Shape


__all__ = [
    "OuterFrameShape",
]


class OuterFrameShape(
    Shape,
):
    def __init__(
        self,
        width: Pixel,
        height: Pixel,
    ):
        super(OuterFrameShape, self).__init__(
            width,
            height,
        )
