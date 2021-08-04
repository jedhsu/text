"""

    Window Position Parameters

"""

from dataclasses import dataclass


@dataclass
class WindowPositionParameters:
    left: Union[Integer, Positive, Negative, Float]
    top
    icon_left
    icon_top
