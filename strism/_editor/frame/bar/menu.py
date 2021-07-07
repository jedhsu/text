"""

    *Frame-Menu-Bar*

"""

from dataclasses import dataclass


from ._bar import FrameBar

__all__ = ["FrameMenuBar"]


@dataclass
class FrameMenuBar(
    FrameBar,
):
    pass
