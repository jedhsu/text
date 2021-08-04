"""

    *String Protocol*

  A type describing a geometric protocol for strings.

"""

from abc import ABCMeta

from .._geometra import StringGeometra

__all__ = ["StringProtocol"]


class StringProtocol(
    StringGeometra,
):
    __metaclass__ = ABCMeta
