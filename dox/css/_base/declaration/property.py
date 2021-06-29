"""

Property

"""

from typing import Sequence
from dataclasses import dataclass
from abc import ABCMeta

__all__ = ["Property"]


@dataclass
class Property:
    __metaclass__ = ABCMeta
    values: Sequence[str]


class ShorthandProperty(Property):
    pass
