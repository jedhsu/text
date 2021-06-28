"""

Number Type

"""

from abc import ABCMeta

__all__ = ["Number"]

from .._type import Type

# [TODO] just subtpye float for now, make sure this is precise later


class Number(
    Type,
):
    __metaclass__ = ABCMeta
