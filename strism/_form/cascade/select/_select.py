"""

    *Cascade: Select*

  Select elements in the CSS syntax.

"""

from dataclasses import dataclass
from abc import ABCMeta

__all__ = ["CascadeSelect"]


@dataclass
class CascadeSelect:
    __metaclass__ = ABCMeta

    ident: str
