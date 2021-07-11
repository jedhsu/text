"""

    Layout Parameters

"""

from dataclasses import dataclass

__all__ = [
    "LayoutParameters",
]


@dataclass
class LayoutParameters:
    outer_border_width: Pixel
    inner_border_width: Pixel

    vertical_scroll_bars
    horizontal_scroll_bars

    scroll_bar_width
    scroll_bar_height

    left_fringe
    right_fringe

    right_divider_width
    bottom_divider_width
