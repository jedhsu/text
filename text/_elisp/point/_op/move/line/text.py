"""

    *Text-Line-Move*

  Move a point by text lines.

"""

from abc import ABCMeta

from .._move import Move

__all__ = ["TextLineMove"]


class TextLineMove(
    Move,
):
    __metaclass__ = ABCMeta
