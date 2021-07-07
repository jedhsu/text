"""

    *Hsba*

  The color spectral measure using the HSBA system.

  Visually forms an HSB cone.

"""

from dataclasses import dataclass

from wich.measure.spectral import Spectral

from .._color import GraphicalColor
from ..opacity import OpacitySpectral

from .hue import HueSpectral
from .saturation import SaturationSpectral
from .brightness import BrightnessSpectral


__all__ = [
    "Hsba",
]


@dataclass
class Hsba(
    GraphicalColor,
    Spectral,
):
    hue: HueSpectral
    saturation: SaturationSpectral
    brightness: BrightnessSpectral
    alpha: OpacitySpectral

    # [TODO] spectral union type...

    @classmethod
    def create(
        cls,
        hue: int,
        saturation: int,
        brightness: int,
        alpha: float,
    ):
        return cls(
            RedSpectral(red),
            GreenSpectral(green),
            BlueSpectral(blue),
            OpacitySpectral(alpha),
        )

    @classmethod
    def from_hsla(cls, hsla: Hsla) -> Hsba:
        pass

    @classmethod
    def from rgba(cls, rgba: Rgba) -> Hsba:
        pass
