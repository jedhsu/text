from dataclasses import dataclass


@dataclass
class Angle:
    angle: type
    angle_percentage: type


@dataclass
class AngleUnits:
    deg = "#deg"
    grad = "#grad"
    rad = "#rad"
    turn = "#turn"
