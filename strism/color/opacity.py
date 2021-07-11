"""

    *Opacity*

  The spectral measure for opacity.

"""


from wich._measure.scaling import Percent
from wich._measure.spectral import Spectral

__all__ = ["OpacitySpectral"]


class Opacity(
    Percent,
    Spectral[0, 1],
):
    def __init__(
        self,
        value: float,
    ):
        super(Opacity, self).__init__(
            value,
        )
