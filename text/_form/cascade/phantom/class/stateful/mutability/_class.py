"""

    *Mutability*

  A type describing mutability state of an element.

"""

from abc import ABCMeta

from .._class import CascadeStatefulPhantom


class Mutability(
    CascadeStatefulPhantom,
):
    __metaclass__ = ABCMeta
