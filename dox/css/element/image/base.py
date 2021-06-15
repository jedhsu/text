"""

Image base type.

"""

from dataclasses import dataclass
from typing import Callable


class _Image(type):
    pass


@dataclass
class Image:
    # ONE OF

    # [TODO] url
    gradient: Gradient  # type
    element_: Callable  # defines image elt
    image: Callable

    cross_fade: Callable  # blending of two images
    image_set: Callable  # defines resoltuion?

    orientation: property
    rendering: property
    resolution: property


@dataclass
class Paint:
    paint_: Callable

    paint_order: property
