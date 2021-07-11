from dataclasses import dataclass

from ..point import Point

__all__ = ["Line"]


@dataclass
class Line:
    a: Point
    b: Point

    def __len__(self) -> float:
        raise NotImplementedError
