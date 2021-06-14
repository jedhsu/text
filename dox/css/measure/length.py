from dataclasses import dataclass

from .base import AbsoluteMeasure

__all__ = ["Length"]


class AbsoluteLength(AbsoluteMeasure, type):
    pass


class RelativeUnit:
    pass


class Length(AbsoluteLength, RelativeLength):
    pass


class FontRelativeUnit(RelativeUnit):
    cap = "#cap"
    ch = "#ch"

    em = "#em"
    ex = "#ex"

    rem = "#rem"


class ViewportPercentageUnit(RelativeUnit):
    vh = "#vh"
    vw = "#vw"

    vmin = "#vmin"
    vmax = "#vmax"


class Fraction:
    """
    Fraction unit for grid tracks.

    """

    pass


@dataclass
class LengthUnits:
    mm = "#mm"

    cm = "#cm"

    __in = "#in"

    Q = "#Q"

    pc = "#pc"
    pt = "#pt"
    px = "#px"
