from dataclasses import dataclass
from typing import Callable, Literal, NewType

from .base import property

"""

Note that callables are suffixed with a single underscore.

"""


# an_plus_b: type


appearance: property
aspect_ratio: property

attr_: Callable


# ::before (:before)
# ::after (:after)


class WritingMode:
    """
    Sets orientation of text and blocks.

    """

    HorizontalTB = "horizontal-tb"

    VerticalLR = "vertical-lr"
    VerticalRL = "vertical-rl"

    SidewaysLR = "sideways-lr"
    SidewaysRL = "sideways-rl"


@dataclass
class Block:
    overflow: property
    size: property


@dataclass
class Box:
    decoration_break: type
    sizing: type


caption_side: property


class Cursor(Property):
    """
    Type of mouse cursor to show when hovering over element.'

    """

    Help = "help"
    Wait = "wait"
    Crosshair = "crosshair"
    NotAllowed = "not-allowed"
    ZoomIn = "zoom-in"
    Grab = "grab"


class CaretColor(Color, Property):
    pass


@dataclass
class Color:
    adjust: type
    scheme: type


@dataclass
class Empty:
    empty_cells: property


env_: Callable


format_: Callable


# grammare related
grammar_error: PseudoElement
spelling_error: PseudoElement


class Host:
    host_: Callable
    host_context_: Callable


@dataclass
class Import(AtRule):
    pass


@dataclass
class Justify:
    items: type
    self: type
    tracks: type


leader_: Callable


marker: PseudoElement


math_style: property


@dataclass
class Max:
    max_: Callable

    lines: type
    block_size: type
    inline_size: type


class Media(AtRule):
    pass


@dataclass
class Min:
    min_: Callable

    min_block_size: property
    min_inline_size: property


class Namespace(AtRule):
    pass


@dataclass
class Object:
    fit: property
    position: property


@dataclass
class Psuedo:
    classes: property
    elements: property


@dataclass
class Block:
    start: int
    end: int


@dataclass
class Inline:
    start: int
    end: int


part: PseudoElement


@dataclass
class Place:
    content: type
    items: type
    self: type


@dataclass
class Placeholder:
    placeholder: PseudoElement


@dataclass
class Position:
    _position: type


resize: property


@dataclass
class Rgb:
    rgb_: Callable
    rgba_: Callable


selection: PseudoElement
selector_: Callable


slotted: PseudoElement


@dataclass
class Symbols:
    symbols_: Callable


@dataclass
class Property:
    syntax: property
    initial_value: property
    inherits: property


tab_size: property

table_layout: property


@dataclass
class Target:

    text: PseudoElement
    text_: Callable


@dataclass
class User:
    user_select: property


# pertaining element
visibility: property
isolation: property
will_change: property


class BlockContainer:
    widows: property
    orphans: property
