"""

    *Cascade: Tab-Size*

  A CSS property describing whitespace handling.

"""


from strism._form.cascade import CascadeProperty

__all__ = ["CascadeTabSize"]


class CascadeTabSize(
    CascadeProperty,
    IntegerLength,
):
    pass
