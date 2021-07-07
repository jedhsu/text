"""

    *CSS Shorthand-Property*

"""

from ._property import CssProperty
from .values import Values

__all__ = ["CssShorthandProperty"]


class CssShorthandProperty(
    CssProperty,
):
    def __init__(
        self,
        values: Values,
    ):
        super(CssShorthandProperty, self).__init__(
            values,
        )
