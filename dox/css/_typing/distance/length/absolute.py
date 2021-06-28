from abc import ABCMeta
from dataclasses import dataclass


class AbsoluteLength(
    Type,
):
    pass


@dataclass
class UnitLength(
    Unit,
):
    ident: Ident  # [TODO] flesh out id selector


class Inches(
    UnitLength,
    Type,
):
    ident = Ident("in")


class Centimeters(
    UnitLength,
    Type,
):
    ident = Ident("cm")


class Millimeters(
    UnitLength,
    Type,
):
    ident = Ident("mm")


class QuarterMillimeters(
    UnitLength,
    Type,
):
    ident = Ident("q")


class Pixels(
    UnitLength,
    Type,
):
    """
    Size required to yield 96 ppi.

    """

    ident = Ident("px")


class Picas(
    UnitLength,
    Type,
):
    ident = Ident("pc")


class Points(
    UnitLength,
    Type,
):
    ident = Ident("pt")
