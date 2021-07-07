from dataclasses import dataclass

from ._scrollbar import WindowScrollBar


__all__ = ["WindowScrollBars"]


@dataclass
class WindowScrollBars:
    left: WindowScrollBar
    right: WindowScrollBar
    horizontal: WindowScrollBar
