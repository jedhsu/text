"""

    *Cascade: White-Space*

  A CSS property describing whitespace handling.

"""

from enum import Enum

from strism._form.cascade import CascadeProperty

__all__ = ["CascadeWhiteSpace"]


class CascadeWhiteSpace(
    Enum,
    CascadeProperty,
):
    Normal = "normal"
    Nowrap = "nowrap"
    PreLine = "pre-line"
