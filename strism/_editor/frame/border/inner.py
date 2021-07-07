"""

    Frame Inner Border

"""

from dataclasses import dataclass


from ._border import FrameBorder

__all__ = [
    "FrameInnerBorder",
]


@dataclass
class FrameInnerBorder(
    FrameBorder,
):
    pass
