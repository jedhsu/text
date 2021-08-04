"""

    *Cascade: Attribute-Select*

  Select attributes.

"""

from ._select import CascadeSelect

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
