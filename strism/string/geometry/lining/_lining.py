"""

    *String Lining*

  String lining graphically decorates a string with a line.

"""

from enum import Enum

from .._geometra import StringGeometra

__all__ = ["StringLining"]


class StringLining(
    Enum,
    StringGeometra,
):
    Underline = "Underline"
    Overline = "Overline"
    LineThrough = "LineThrough"
    Blink = "Blink"
