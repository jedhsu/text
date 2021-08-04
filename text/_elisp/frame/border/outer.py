"""

    Frame Outer Border

"""

from dataclasses import dataclass


from ._border import FrameBorder

__all__ = [
    "FrameOuterBorder",
]


@dataclass
class FrameOuterBorder(
    FrameBorder,
):
    pass
