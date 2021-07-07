"""

    Red Spectral

  The spectral measure for red.

"""

from wich.measure.spectral import Spectral
from wich.literal.integer import Integer

__all__ = [
    "RedSpectral",
]


class RedSpectral(
    Integer,
    Spectral,
):
    def __init__(
        self,
        spectral: int,
    ):
        super(RedSpectral, self).__init__(
            spectral,
        )
