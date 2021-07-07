"""

    *Shape Orienting*

  A type describing shape orientation.

"""

from abc import ABCMeta

from .._geometra import ShapeGeometra

__all__ = ["ShapeOrienting"]


class ShapeOrienting(
    ShapeGeometra,
):
    __metaclass__ = ABCMeta
