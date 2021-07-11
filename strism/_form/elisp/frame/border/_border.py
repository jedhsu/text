"""

    Frame Border

"""

from abc import ABCMeta
from dataclasses import dataclass

__all__ = [
    "FrameBorder",
]


@dataclass
class FrameBorder:
    __metaclass__ = ABCMeta
