"""

    *Direction-Phantom*

  A direction phantom-class type.

"""

from abc import ABCMeta

from typing import TypeVar

from .._class import PhantomClass


class DirectionPhantom(
    PhantomClass,
):
    __metaclass__ = ABCMeta

    Top = TypeVar("Top")
    Right = TypeVar("Right")
    Bottom = TypeVar("Bottom")
    Left = TypeVar("Left")
