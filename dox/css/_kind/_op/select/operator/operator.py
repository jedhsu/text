from abc import ABCMeta


class Operator:

    __metaclass__ = ABCMeta


class SelectSibling(Operator):
    symbol = "+"


class SelectGeneralSibling(Operator):
    symbol = "~"
