"""

    *Border-Side-Style*

  Border side styles.

"""


from abc import ABCMeta

from ._style import BorderStyle

__all__ = [
    "BorderSideStyle",
    "BorderTopStyle",
    "BorderRightStyle",
    "BorderBottomStyle",
    "BorderLeftStyle",
]


class BorderSideStyle(
    BorderStyle,
):
    __metaclass__ = ABCMeta


class BorderTopStyle(
    BorderSideStyle,
):
    pass


class BorderRightStyle(
    BorderSideStyle,
):
    pass


class BorderBottomStyle(
    BorderSideStyle,
):
    pass


class BorderLeftStyle(
    BorderSideStyle,
):
    pass
