from dataclasses import dataclass

clamp_: Callable  # relaed to min an max oper


@dataclass
class Line:
    __break: property
    clamp: property

    height: property
    height_step: property
