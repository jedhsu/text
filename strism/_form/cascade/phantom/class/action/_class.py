"""

    *Cascade: Action-Phantom*

  A user-action phantom-class type.

"""

from abc import ABCMeta

from .._class import CascadePhantomClass

__all__ = ["CascadeActionPhantom"]


class CascadeActionPhantom(
    CascadePhantomClass,
):
    __metaclass__ = ABCMeta
