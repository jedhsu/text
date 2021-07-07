"""

    *Frame-Stacking-Operator*

  Operate the frame in a stacking z-index context.

"""
from abc import ABCMeta

from .._operator import FrameOperator

__all__ = [
    "FrameStackingOperator",
]


class FrameStackingOperator(
    FrameOperator,
):
    __metaclass__ = ABCMeta
