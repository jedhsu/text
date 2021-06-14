from dataclasses import dataclass


@dataclass
class Resolution(float):
    resolution: type


@dataclass
class ResolutionUnits:
    x = "#x"

    dpcm = "#dpcm"
    dpi = "#dpi"
    dppx = "#dppx"
