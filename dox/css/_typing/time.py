from abc import ABCMeta
from dataclasses import dataclass
from typing import Union

from ._type import Type
from ._unit import UnitMeasure

from .numeric import Number


class UnitTime(
    UnitMeasure,
):
    __metaclass__ = ABCMeta


class Seconds(
    UnitTime,
    Type,
):
    ident = Ident("s")


class Milliseconds(
    UnitTime,
    Type,
):
    ident = Ident("ms")


@dataclass
class Time(
    Type,
):
    number: Number
    unit: Union[
        Seconds,
        Milliseconds,
    ]


class TimingFunction:
    pass
