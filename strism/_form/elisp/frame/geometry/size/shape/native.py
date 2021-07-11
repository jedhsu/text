from ._shape import Shape


__all__ = [
    "Shape",
]


class NativeFrameShape(
    Shape,
):
    def __init__(
        self,
        width: Pixel,
        height: Pixel,
    ):
        super(FrameShape, self).__init__(
            width,
            height,
        )
