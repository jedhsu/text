"""

    *Focusing-Action*

  A focusing user action phantom classtype.

"""

from abc import ABCMeta

from .._class import UserActionPhantomClass

__all__ = ["FocusingAction"]


class FocusingAction(
    UserActionPhantomClass,
):
    __metaclass__ = ABCMeta
