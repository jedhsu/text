"""

    *_selector . element*

"""

from ._selector import ElementSelector
from .universal import UniversalElementSelector

__all__ = [
    "ElementSelector",
    "UniversalElementSelector",
]
