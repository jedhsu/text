"""

    *Linear*

  A type with linear geometry.

"""

from abc import ABCMeta

__all__ = ["Linear"]


class Linear(
    Geometric,
):
    __metaclass__ = ABCMeta
