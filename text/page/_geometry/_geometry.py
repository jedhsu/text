"""

    *Page Geometry*

"""

from dataclasses import dataclass

from strism._measure import Pixel

__all__ = ["PageGeometry"]


@dataclass
class PageShaping:
    width = Pixel(816)
    height = Pixel(1056)
