"""

    *Inherit-Keyword*

"""

from abc import ABCMeta

from .._keyword import Keyword

__all__ = ["InheritKeyword"]


class InheritKeyword(
    Keyword,
):
    __metaclass__ = ABCMeta
