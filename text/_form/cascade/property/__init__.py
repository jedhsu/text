"""

    *form . css . prop*

  Css property syntax forms types.

"""

from ._property import CascadeProperty
from ._property import CascadeValues
from .shorthand import CascadeShorthandProperty

__all__ = [
    "CssProperty",
    "Values",
    "CssShorthandProperty",
]
