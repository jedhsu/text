from dataclasses import dataclass

from ...measure import Length
from ..base import Dimensions, Element, End, Start


class Block:
    color: type
    style: type
    width: type

    start: Start
    end: End


class BorderStyle:
    Solid = "Solid"
    Dashed = "Dashed"
    Dotted = "Dotted"
    Groove = "Groove"
    Ridge = "Ridge"
    Double = "Double"
    Inset = "Inset"
    Outset = "Outset"


@dataclass
class BorderWidthKeyword:
    Thin = "thin"
    Medium = "medium"
    Thick = "thick"


class BorderWidth(Length, BorderWidthKeyword):
    pass


class BorderDimensions(Dimensions):
    pass


class BorderCornerRounding:
    """
    border-radius

    """


@dataclass
class Border(Block):
    dimensions: Dimensions

    style: BorderStyle
    color: type
    width: type
    radius: type  # border corner rounding

    collapse: type
    spacing: type


class TopBorder:
    style: BorderStyle


# [TODO] etc...


class Borders:
    """
    Border that is comprised of four parts.

    Two ways of building border.

    """

    top: TopBorder
    right: RightBorder
    bottom: BottomBorder
    left: LeftBorder


class BorderRadius:
    pass


@dataclass
class BorderCorners:
    top_left: BorderRadius
    top_right: BorderRadius
    bottom_left: BorderRadius
    bottom_right: BorderRadius


class Inline(Element):
    start: Element
    end: Element


class Radius:
    start_start: property
    start_end: property
    end_start: property
    end_end: property


@dataclass
class Image:
    outset: type
    repeat: type
    slice: type
    source: type
    width: type
