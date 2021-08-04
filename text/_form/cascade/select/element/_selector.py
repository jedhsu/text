"""

    *Element-Selector*

  An element selector.

"""

from .._select import Select

__all__ = ["ElementSelector"]


class ElementSelector(
    Select,
):
    def __init__(
        self,
        ident: str,
    ):
        super(ElementSelector, self).__init__(
            ident,
        )
