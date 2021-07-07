"""

    *Move*

  Move a point.

"""

from abc import ABCMeta

from .._operator import PointOperator


class Move(
    PointOperator,
):
    __metaclass__ = ABCMeta
