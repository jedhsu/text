"""

    *Cascade: Property*

  Property, a CSS syntax form.

"""

from dataclasses import dataclass
from abc import ABCMeta

from .values import Values

__all__ = ["CascadeProperty"]


@dataclass
class CascadeProperty:
    __metaclass__ = ABCMeta

    values: Values
