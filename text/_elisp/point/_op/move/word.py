"""

    *Word-Move*

  Move a point by words.

"""

from abc import ABCMeta

from ._move import Move


class WordMove(
    Move,
):
    __metaclass__ = ABCMeta
