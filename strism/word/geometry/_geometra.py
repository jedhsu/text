"""

    *Word Geometra*

  A type describing word geometry.

"""

from strism._geometry import Geometra

from abc import ABCMeta

__all__ = ["WordGeometra"]


class WordGeometra(
    Geometra,
):
    __metaclass__ = ABCMeta
