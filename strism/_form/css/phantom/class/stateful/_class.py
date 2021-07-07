"""

    *Stateful Phantom-Class*

  A phantom class based on UI state.

"""

from .._class import PhantomClass

from abc import ABCMeta


class StatefulPhantomClass(
    PhantomClass,
):
    __metaclass__ = ABCMeta
