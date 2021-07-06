"""

    *Shorthand-Property*

"""

from ._property import Property
from .values import Values

__all__ = ["ShorthandProperty"]


class ShorthandProperty(
    Property,
):
    def __init__(
        self,
        values: Values,
    ):
        super(ShorthandProperty, self).__init__(
            values,
        )
