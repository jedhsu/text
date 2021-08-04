"""

    *Shape Geometry Protocol*

  A protocol describing shape geometry.

"""

from abc import ABCMeta

from .._geometra import ShapeGeometra

__all__ = ["ShapeGeometryProtocol"]


class ShapeGeometryProtocol(
    ShapeGeometra,
):
    __metaclass__ = ABCMeta
