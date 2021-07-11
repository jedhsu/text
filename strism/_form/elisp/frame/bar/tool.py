"""

    Frame Tool Bar

"""

from dataclasses import dataclass


from ._bar import FrameBar

__all__ = [
    "FrameToolBar",
]


@dataclass
class FrameToolBar(
    FrameBar,
):
    pass
