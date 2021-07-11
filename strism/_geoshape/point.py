"""

    *Point*   (x: Pixel, y: Pixel)

  A pair of coordinates describing position.

"""

from __future__ import annotations
from dataclasses import dataclass

from .pixel import Pixel


__all__ = ["Point"]


@dataclass
class Point:
    x: Pixel
    y: Pixel

    @classmethod
    def create(
        cls,
        x: int,
        y: int,
    ):
        return cls(
            Pixel(x),
            Pixel(y),
        )

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(
        self,
        pt: Point,
    ):
        return Point.create(
            self.x + pt.x,
            self.y + pt.y,
        )

    def __sub__(
        self,
        pt: Point,
    ):
        return Point.create(
            self.x - pt.x,
            self.y - pt.y,
        )
