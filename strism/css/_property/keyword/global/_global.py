"""

    *Global-Keyword*

"""

from abc import ABCMeta

from .._keyword import Keyword

__all__ = ["GlobalKeyword"]


class GlobalKeyword(
    Keyword,
):
    __metaclass__ = ABCMeta
