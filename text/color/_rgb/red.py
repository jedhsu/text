"""

    *Red*

  The spectral measure for red.

"""

__all__ = ["Red"]

from ._primary import PrimaryColor


class Red(
    PrimaryColor,
):
    def __init__(
        self,
        val: int,
    ):
        super(Red, self).__init__(
            val,
        )
