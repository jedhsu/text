from abc import ABCMeta

from dataclasses import dataclass

from ._type import Type
from ._unit import UnitMeasure


# [TODO] subclass Dimension?


@dataclass
class Frequency:
    ident = Ident("frequency-percentage")

    frequency: type
    unit: type


class UnitFrequency(
    UnitMeasure,
):
    __metaclass__ = ABCMeta


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
