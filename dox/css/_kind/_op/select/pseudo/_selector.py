"""

    *Pseudo-Selector*

"""

from .._selector import Selector


class PseudoSelector(
    Selector,
):
    def __init__(
        self,
        ident: str,
    ):
        super(PseudoSelector, self).__init__(
            ident,
        )
