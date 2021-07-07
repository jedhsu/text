"""

    *Font*

  A face type describing glyph appearance.

"""

from abc import ABCMeta

from .._face import Face


class Font(
    Face,
):
    __metaclass__ = ABCMeta
