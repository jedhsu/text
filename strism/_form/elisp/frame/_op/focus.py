"""

    *Frame-Focus*

  Focus a frame, i.e. change the frame to the global selected frame.

"""

from ._operator import FrameOperator

__all__ = ["FrameFocus"]


class FrameFocus(
    FrameOperator,
):
    pass
