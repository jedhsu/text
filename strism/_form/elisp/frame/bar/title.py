"""

    Frame Title Bar

"""

from dataclasses import dataclass


from ._bar import FrameBar

__all__ = [
    "FrameTitleBar",
]


@dataclass
class FrameTitleBar(
    FrameBar,
):
    pass
