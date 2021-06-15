from dataclasses import dataclass


@dataclass
class Resolution(float):
    resolution: type


@dataclass
class ResolutionUnits:
    x = "#x"


class DotsPerInch:
    dpi = "#dpi"


class DotsPerCentimeter:
    dpcm = "#dpcm"


class DotsPerPixelUnit:
    dppx = "#dppx"
