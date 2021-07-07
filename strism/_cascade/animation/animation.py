from dataclasses import dataclass


@dataclass
class Animation(Property):

    # -- Subproperties
    name: Property
    duration: Property

    timing_function: Property
    delay: Property

    iteration_count: Property
    direction: Property

    fill_mode: Property
    play_state: Property


"""

[SVG]

"""


class SvgAnimate:
    pass


class SvgAnimateColor:
    pass


class SvgAnimateMotion:
    pass


class SvgAnimateTransform:
    pass


class SvgDiscard:
    pass


class SvgMpath:
    pass


class SvgSet:
    pass
