"""

    *Line*

  A string with line geometry.

"""

from dataclasses import dataclass

from ..string import String


@dataclass
class Line(
    String,
):
    geometry: LineGeometry
