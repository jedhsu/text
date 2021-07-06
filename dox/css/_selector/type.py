"""

    *Type-Selector*

"""

from ._selector import Selector

__all__ = ["TypeSelector"]


class TypeSelector(
    Selector,
):
    def __init__(
        self,
        ident: str,
    ):
        super(TypeSelector, self).__init__(
            ident,
        )
