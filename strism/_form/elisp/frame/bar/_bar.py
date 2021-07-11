"""

    *Frame-Bar*

  A frame bar type.

"""

from abc import ABCMeta
from dataclasses import dataclass

from .._element import FrameElement

__all__ = ["FrameBar"]


@dataclass
class FrameBar(
    FrameElement,
):
    __metaclass__ = ABCMeta
