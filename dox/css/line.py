from dataclasses import dataclass


@dataclass
class Line:
    __break: property
    clamp: property

    height: property
    height_step: property
