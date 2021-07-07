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

"""

[SVG]

"""

# [TODO] prob just directly subclass (SvgFilterElement)


class Blend(FilterElement, SvgElement):
    pass


class ColorMatrix(FilterElement, SvgElement):
    pass


class ComponentTransfer(FilterElement, SvgElement):
    pass


class Composite(FilterElement, SvgElement):
    pass


class ConvolveMatrix(FilterElement, SvgElement):
    pass


class DiffuseLighting(FilterElement, SvgElement):
    pass


class DisplacementMap(FilterElement, SvgElement):
    pass


class DistantLight(FilterElement, SvgElement):
    pass


class DropShadow(FilterElement, SvgElement):
    pass


class Flood(FilterElement, SvgElement):
    pass


class FuncA(FilterElement, SvgElement):
    pass


class FuncB(FilterElement, SvgElement):
    pass


class FuncG(FilterElement, SvgElement):
    pass


class FuncR(FilterElement, SvgElement):
    pass


class GaussianBlur(FilterElement, SvgElement):
    pass


class Image(FilterElement, SvgElement):
    pass


class Merge(FilterElement, SvgElement):
    pass


class MergeNode(FilterElement, SvgElement):
    pass


class Morphology(FilterElement, SvgElement):
    pass


class Offset(FilterElement, SvgElement):
    pass


class PointLight(FilterElement, SvgElement):
    pass


class SpecularLighting(FilterElement, SvgElement):
    pass


class SpotLight(FilterElement, SvgElement):
    pass


class Tile(FilterElement, SvgElement):
    pass


class Turbulence(FilterElement, SvgElement):
    pass


# <filter>
# <foreignObject>
