"""

    *Character Geometra*

  A type describing character geometry.

"""

from abc import ABCMeta

from strism._geometry import Geometra

__all__ = ["CharacterGeometra"]


class CharacterGeometra(
    Geometra,
):
    __metaclass__ = ABCMeta
