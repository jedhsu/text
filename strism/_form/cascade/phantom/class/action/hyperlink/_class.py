"""

    *Cascade: Hyperlink Action-Phantom*

  A user action on a hyperlink, phantom classtype.

"""

from abc import ABCMeta

from .._class import CascadeActionPhantom

__all__ = ["CascadeHyperlinkActionPhantom"]


class CascadeHyperlinkActionPhantom(
    CascadeActionPhantom,
):
    __metaclass__ = ABCMeta
