"""

    *Focusing-Action*

  A focusing user action phantom classtype.

"""

from abc import ABCMeta

from .._class import CascadeActionPhantom

__all__ = ["FocusingAction"]


class FocusingAction(
    CascadeActionPhantom,
):
    __metaclass__ = ABCMeta
