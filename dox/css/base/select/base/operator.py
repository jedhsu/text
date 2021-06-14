from abc import ABCMeta


class Operator:

    __metaclass__ = ABCMeta


class SelectDescendant(Operator):
    symbol = " "


class SelectChild(Operator):
    symbol = ">"


class SelectSibling(Operator):
    symbol = "+"


class SelectGeneralSibling(Operator):
    symbol = "~"
