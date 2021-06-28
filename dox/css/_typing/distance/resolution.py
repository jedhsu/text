from abc import ABCMeta
from dataclasses import dataclass

from .._type import Type
from .._unit import UnitMeasure


class UnitResolution(
    UnitMeasure,
):
    __metaclass__ = ABCMeta


class DotsPerInch(
    UnitResolution,
    Type,
):
    ident = Ident("dpi")


class DotsPerCentimeter(
    UnitResolution,
    Type,
):
    ident = Ident("dpcm")


class DotsPerPixelUnit(
    UnitResolution,
    Type,
):
    ident = Ident("dppx")
