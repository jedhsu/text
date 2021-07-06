"""

    *Selector*

  A type of selector.

"""

from dataclasses import dataclass
from abc import ABCMeta

__all__ = ["Selector"]


@dataclass
class Selector:
    __metaclass__ = ABCMeta

    ident: str
