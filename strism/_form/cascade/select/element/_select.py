"""

    *Element-Selector*

  An element selector.

"""

from .._selector import Selector

__all__ = ["ElementSelector"]


class ElementSelector(
    Selector,
):
    def __init__(
        self,
        ident: str,
    ):
        super(ElementSelector, self).__init__(
            ident,
        )
