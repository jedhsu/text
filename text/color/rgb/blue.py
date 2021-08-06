"""

    *Blue*

  The spectral measure for blue.

"""

__all__ = ["Blue"]

from ._primary import PrimaryColor


class Blue(
    PrimaryColor,
):
    def __init__(
        self,
        val: int,
    ):
        super(Blue, self).__init__(
            val,
        )
