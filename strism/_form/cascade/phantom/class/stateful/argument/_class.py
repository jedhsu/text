"""

    *Cascade: Argument State-Phantom*

  A phantom class based on UI state.

"""

from .._class import CascadePhantomClass

from abc import ABCMeta


class CascadeStatefulPhantom(
    CascadePhantomClass,
):
    __metaclass__ = ABCMeta
