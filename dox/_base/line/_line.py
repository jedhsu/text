"""

    *Line*

  A string imbued with line geometry.

"""

from dataclasses import dataclass

from ..string import String

from .geometry import LineGeometry

__all__ = ["Line"]


@dataclass
class Line(
    String,
):
    geometry: LineGeometry
