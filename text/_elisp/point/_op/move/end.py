"""

    *End-Move*

  Move a point to the end of the buffer.

"""

from abc import ABCMeta

from ._move import Move


class EndMove(
    Move,
):
    __metaclass__ = ABCMeta
