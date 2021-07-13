"""

    *Planar*

  A type with planar geometry.

"""

from abc import ABCMeta

__all__ = ["Planar"]


class Planar(
    Geometric,
):
    __metaclass__ = ABCMeta
