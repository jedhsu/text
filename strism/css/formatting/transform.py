from dataclasses import dataclass
from typing import Callable


@dataclass
class Transform:
    transform: property
    box: property
    origin: property
    style: property

    function: Callable


@dataclass
class Perspective:
    perspective: type
    perspective_: Callable

    origin: type


@dataclass
class Matrix:
    """
    Matrix transforms.

    """

    matrix_: Callable
    matrix_3d_: Callable


@dataclass
class Rotation:
    """
    Rotations.

    """

    rotate: type

    rotate_3d: type

    rotate_x: type
    rotate_y: type
    rotate_z: type


@dataclass
class Scaling:
    """
    Scaling (Resizing).

    """

    scale: type

    scale_: Callable

    scale_3d: property

    scale_X: property
    scale_Y: property
    scale_Z: property


@dataclass
class Skew:
    """
    Skew (Distort).

    """

    skew: type

    skew_X: type
    skew_Y: type


@dataclass
class Translate:
    """
    Translate.

    """

    translate: type

    translate_3d: property

    translate_x: property
    translate_y: property
    translate_z: property
