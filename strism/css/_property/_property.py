"""

    *Property*

  A property type.
"""

from dataclasses import dataclass
from abc import ABCMeta

from .values import Values

__all__ = ["Property"]


@dataclass
class Property:
    __metaclass__ = ABCMeta

    values: Values
