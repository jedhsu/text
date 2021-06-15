from dataclasses import dataclass
from typing import Callable

from .base import AbsoluteMeasure

__all__ = ["Length"]

calc: Callable


class AbsoluteLength(AbsoluteMeasure, type):
    pass


class RelativeUnit:
    pass


class Length(AbsoluteLength, RelativeLength):
    pass


class FontRelativeUnit(RelativeUnit):
    cap = "#cap"
    ch = "#ch"


class Em(RelativeUnit):
    symbol = "em"


class Ex(RelativeUnit):
    """
    Height of a lowercase x.

    """

    symbol = "ex"


class RootEm(RelativeUnit):
    symbol = "rem"


class ViewportRelativeUnit(RelativeUnit):
    # 1/100th of viewport height
    vh = "#vh"

    # 1/100th of viewport width
    vw = "#vw"

    vmin = "#vmin"
    vmax = "#vmax"


class ViewportCentiheight(ViewportRelativeUnit):
    pass


# [TODO] finish


class Fraction:
    """
    Fraction unit for grid tracks.

    """

    pass


@dataclass
class LengthUnit:

    Q = "#Q"


class Millimeter(LengthUnit):
    symbol = "mm"


class Centimeter(LengthUnit):
    symbol = "cm"


class Inch(LengthUnit):
    abbr = "in"


class Pixel(
    LengthUnit,
    CssType,
    SvgType,
):
    """
    Size required to yield 96 ppi.

    """

    abbr = "px"


class Pica(LengthUnit):
    abbr = "pc"


class Point(LengthUnit):
    abbr = "pt"
