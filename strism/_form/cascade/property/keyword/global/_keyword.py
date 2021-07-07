"""

    *Cascade Global-Keyword*

  The global keyword syntax form of the CSS language.

"""

from abc import ABCMeta

from .._keyword import CascadeKeyword

__all__ = ["CascadeGlobalKeyword"]


class CascadeGlobalKeyword(
    CascadeKeyword,
):
    __metaclass__ = ABCMeta
