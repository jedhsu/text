"""

    *Attribute-Selector*

"""

from ._selector import Selector

__all__ = ["AttributeSelector"]


class AttributeSelector(
    Selector,
):
    def __init__(
        self,
        ident: str,
    ):
        super(AttributeSelector, self).__init__(
            ident,
        )
