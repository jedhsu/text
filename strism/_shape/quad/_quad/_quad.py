from dataclasses import dataclass

from strism._shape import Pixel
from strism._shape import Shape

__all__ = ["Shape"]


@dataclass
class Quad(
    Shape,
):
    height: Pixel
    width: Pixel
