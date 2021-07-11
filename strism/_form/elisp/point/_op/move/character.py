"""

    *Character-Move*

  Move a point by number of characters.

"""

from abc import ABCMeta

from ._move import Move


class CharacterMove(
    Move,
):
    __metaclass__ = ABCMeta
