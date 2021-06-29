from dataclasses import dataclass
from typing import Sequence

__all__ = ["Descriptor"]

"""

Defines the characteristics of an at-rule.

"""


@dataclass
class Descriptor:
    ident: str
    value: Sequence
    important: bool
