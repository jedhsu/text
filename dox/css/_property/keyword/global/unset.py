"""

    *Unset-Keyword*

"""

from abc import ABCMeta

from .._keyword import Keyword

__all__ = ["UnsetKeyword"]


class UnsetKeyword(
    Keyword,
):
    __metaclass__ = ABCMeta
