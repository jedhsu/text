# basic shape type

# needs more org

from dataclasses import dataclass
from typing import Callable


@dataclass
class Shape:
    shape: type

    image_threshold: property

    margin: property

    outside: property


@dataclass
class Shapes:
    circle_: Callable
    ellipse_: Callable


polygon: property

path_: Callable
rect_: Callable
