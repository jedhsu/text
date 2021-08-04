"""

    *Prefix*

  A prefix.

"""

from abc import ABCMeta

from typing import TypeVar

__all__ = ["Prefix"]


class Prefix:
    __metaclass__ = ABCMeta

    Meta = TypeVar("Meta")
    Control = TypeVar("Control")
    Shift = TypeVar("Shift")
    Hyper = TypeVar("Hyper")
    Super = TypeVar("Super")
    Alt = TypeVar("Alt")
