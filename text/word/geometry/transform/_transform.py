"""

    *Word Transform*

  A transform type on word geometry.

"""

from abc import ABCMeta

from .._geometra import WordGeometra

__all__ = ["WordTransform"]


class WordTransform(
    WordGeometra,
):
    __metaclass__ = ABCMeta
