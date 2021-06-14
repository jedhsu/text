from dataclasses import dataclass
from typing import Callable


class ColorKeyword:
    pass


class Color:
    pass


@dataclass
class Hsl:
    hsl: property
    hsla_: Callable[[], [Hue, Saturation, Lightness, Opacity]]
