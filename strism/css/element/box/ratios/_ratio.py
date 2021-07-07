from abc import ABCMeta
from dataclasses import dataclass


@dataclass
class BoxRatio:
    __metaclass__ = ABCMeta

    x: float
    y: float
