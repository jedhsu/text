"""

    *Select*

  Select elements.

"""

from dataclasses import dataclass
from abc import ABCMeta

__all__ = ["Select"]


@dataclass
class Select:
    __metaclass__ = ABCMeta

    ident: str
