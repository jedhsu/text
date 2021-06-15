from abc import ABCMeta
from dataclasses import dataclass


class Keyword:
    __metaclass__ = ABCMeta

    pass


class GlobalKeyword(Keyword):
    pass


class Inherit(GlobalKeyword):
    pass


class Initial(GlobalKeyword):
    pass


class Unset(GlobalKeyword):
    pass


# @dataclass
# class Initial:
#     initial: property
#     letter: property
#     letter_align: property
