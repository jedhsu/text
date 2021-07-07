"""

    *String Texture*

  A type describing the texture of strings.

"""

from abc import ABCMeta

from .._geometry import StringGeometry

__all__ = ["StringTexture"]


class StringTexture(
    StringGeometry,
):
    __metaclass__ = ABCMeta
