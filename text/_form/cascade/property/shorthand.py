"""

    *Cascade: Shorthand-Property*

"""

from ._property import CascadeProperty
from ._property import CascadeValues

__all__ = ["CascadeShorthandProperty"]


class CssShorthandProperty(
    CascadeProperty,
):
    def __init__(
        self,
        values: CascadeValues,
    ):
        super(CssShorthandProperty, self).__init__(
            values,
        )
