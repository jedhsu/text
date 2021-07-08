from dataclasses import dataclass

from .pixel import Pixel

__all__ = ["PageGeometry"]


@dataclass
class PageGeometry:
    width = Pixel(816)
    height = Pixel(1056)
