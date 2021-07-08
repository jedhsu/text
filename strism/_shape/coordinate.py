from __future__ import annotations
from dataclasses import dataclass

from .pixel import Pixel


__all__ = ["Coordinate"]


@dataclass
class Coordinate:
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
        coord: Coordinate,
    ):
        return Coordinate.create(
            self.x + coord.x,
            self.y + coord.y,
        )

    def __sub__(
        self,
        coord: Coordinate,
    ):
        return Coordinate.create(
            self.x + coord.x,
            self.y + coord.y,
        )

    def __mul__(
        self,
        coord: Coordinate,
    ):
        return Coordinate.create(
            self.x + coord.x,
            self.y + coord.y,
        )
