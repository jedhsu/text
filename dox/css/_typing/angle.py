from abc import ABCMeta
from dataclasses import dataclass
from typing import Union

from ._type import Type
from ._unit import UnitMeasure


class UnitAngle(
    UnitMeasure,
):
    __metaclass__ = ABCMeta


class Degrees(
    UnitAngle,
    Type,
):
    ident = Ident("deg")


class Gradians(
    UnitAngle,
    Type,
):
    ident = Ident("grad")


class Radians(
    UnitAngle,
    Type,
):
    ident = Ident("rad")


class Turns(
    UnitAngle,
    Type,
):
    ident = Ident("turn")


@dataclass
class Angle:
    number: Number
    unit: Union[
        Degrees,
        Gradians,
        Radians,
        Turns,
    ]
