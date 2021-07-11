"""

    *Frame-Lower*

  Lower the frame on the z-index.

"""

from ._operator import FrameStackingOperator

__all__ = ["FrameLower"]


class FrameLower(
    FrameStackingOperator,
):
    pass
