from dataclasses import dataclass

from ._type import Type
from ._unit import UnitMeasure


@dataclass
class Frequency:
    frequency: type
    percentage: type


class UnitFrequency(
    UnitMeasure,
):
    pass


class Hertz(
    UnitFrequency,
    Type,
):
    ident = Ident("Hz")


class KiloHertz(
    UnitFrequency,
    Type,
):
    ident = Ident("kHz")
