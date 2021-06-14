from abc import ABCMeta
from typing import Text

from sympy import Add, Lambda, Symbol
from sympy.core.operations import AssocOp
from sympy.core.symbol import Str


class Decorator(Lambda):
    __metaclass__ = ABCMeta

    Operand = Symbol("x")
    text: Text

    def __init__(
        self,
        text: Text,
        decoration: AssocOp,
    ):
        super(Decorator, self).__new__(Lambda, text, decoration)


# [Test]


def adds_period():
    return Decorator("word", Add(Decorator.Operand, Str(".")))


class Test:
    adds_period = adds_period
