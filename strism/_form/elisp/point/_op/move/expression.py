"""

    *Expression-Move*

  Move a point by expressions.

"""

from abc import ABCMeta

from ._move import Move


class ExpressionMove(
    Move,
):
    __metaclass__ = ABCMeta
