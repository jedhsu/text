"""

    *Cascade Inherit-Keyword*

  The _inherit_ global keyword of the CSS language.

"""

from ._keyword import CascadeGlobalKeyword

__all__ = ["CascadeInheritKeyword"]


class CascadeInheritKeyword(
    CascadeGlobalKeyword,
):
    pass
