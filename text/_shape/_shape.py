"""

    *Element Shape*

"""

from dataclasses import dataclass

from strism._geoshape import Pixel

__all__ = ["ElementShape"]


@dataclass
class ElementShape:
    width: Pixel
    height: Pixel

    @classmethod
    def create(
        cls,
        width: int,
        height: int,
    ):
        return cls(
            Pixel(width),
            Pixel(height),
        )
