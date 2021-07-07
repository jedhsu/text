"""

    *Hyperlink-Action*

  A user action on a hyperlink, phantom classtype.

"""

from abc import ABCMeta

from .._class import UserActionPhantomClass

__all__ = ["HyperlinkAction"]


class HyperlinkAction(
    UserActionPhantomClass,
):
    __metaclass__ = ABCMeta
