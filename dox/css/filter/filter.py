"""

Graphical effects.

"""

from dataclasses import dataclass
from typing import Callable


@dataclass
class Filter:
    filter: property

    filter_function: type


class FilterFunction:
    brightness_: Callable
    saturate_: Callable

    contrast_: Callable
    grayscale_: Callable

    sepia_: Callable

    drop_shadow_: Callable

    hue_rotate_: Callable

    invert_: Callable

    opacity_: Callable

    blur_: Callable


# @dataclass
# class Opacity:
#     opacity: property
#     opacity_: Callable
