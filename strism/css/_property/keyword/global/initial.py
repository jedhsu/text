"""

    *Initial-Keyword*

"""

from abc import ABCMeta

from .._keyword import Keyword

__all__ = ["InitialKeyword"]


class InitialKeyword(
    Keyword,
):
    __metaclass__ = ABCMeta
