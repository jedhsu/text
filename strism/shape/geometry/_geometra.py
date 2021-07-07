"""

    *Shape Geometra*

  A type describing shape geometry.

"""

from abc import ABCMeta

from strism._geometry import Geometra

__all__ = ["ShapeGeometra"]


class ShapeGeometra(
    Geometra,
):
    __metaclass__ = ABCMeta
