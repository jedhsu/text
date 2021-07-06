"""

    *Class-Selector*

"""


__all__ = ["ClassSelector"]

from ._selector import Selector


class ClassSelector(
    Selector,
):
    def __init__(
        self,
        ident: str,
    ):
        super(ClassSelector, self).__init__(
            ident,
        )
