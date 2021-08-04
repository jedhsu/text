"""

    *Letter Geometra*

  A type describing letter geometry.

"""

from abc import ABCMeta

from strism._geometry import Geometra

__all__ = ["LetterGeometra"]


class LetterGeometra(
    Geometra,
):
    __metaclass__ = ABCMeta
