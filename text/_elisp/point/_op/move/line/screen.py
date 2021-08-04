"""

    *Screen-Line-Move*

  Move a point by screen lines.

"""

from abc import ABCMeta

from .._move import Move

__all__ = ["ScreenLineMove"]


class ScreenLineMove(
    Move,
):
    __metaclass__ = ABCMeta
