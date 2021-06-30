"""

Box Model

"""

from dataclasses import dataclass


class BoxDecorationBreak:
    Slice = "slice"
    Clone = "clone"


@dataclass
class Box:
    decoration_break: BoxDecorationBreak
    sizing: type
