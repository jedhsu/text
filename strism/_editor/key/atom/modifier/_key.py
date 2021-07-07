"""

    *Modifier-Key*

  A modifier key.

"""

from abc import ABCMeta

from typing import TypeVar

from .._key import Key

__all__ = ["ModifierKey"]


class ModifierKey(
    Key,
):
    __metaclass__ = ABCMeta

    Meta = TypeVar("Meta")
    Control = TypeVar("Control")
    Shift = TypeVar("Shift")
    Hyper = TypeVar("Hyper")
    Super = TypeVar("Super")
    Alt = TypeVar("Alt")
