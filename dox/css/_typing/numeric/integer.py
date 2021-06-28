"""

Number Type

"""

__all__ = ["Integer"]

from .number import Number


class Integer(
    int,
    Number,
):
    pass
