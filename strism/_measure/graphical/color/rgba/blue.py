"""

    Blue Spectral

  The spectral measure for blue.

"""

from wich.measure.spectral import Spectral
from wich.literal.integer import Integer

__all__ = [
    "BlueSpectral",
]


class BlueSpectral(
    Integer,
    Spectral,
):
    def __init__(
        self,
        spectral: int,
    ):
        super(BlueSpectral, self).__init__(
            spectral,
        )
