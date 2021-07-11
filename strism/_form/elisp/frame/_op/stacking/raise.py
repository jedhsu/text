"""

    *Frame-Raise*

  Raise the frame on the z-index.

"""

from ._operator import FrameStackingOperator

__all__ = ["FrameRaise"]


class FrameRaise(
    FrameStackingOperator,
):
    pass
