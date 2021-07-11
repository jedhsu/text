"""

    *Stick*

  A string imbued with plane geometry.

"""

from dataclasses import dataclass

from ..string import String

from .geometry import StickGeometry

__all__ = ["Stick"]


@dataclass
class Stick(
    String,
):
    geometry: StickGeometry
