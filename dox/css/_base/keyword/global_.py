from ._keyword import Keyword

__all__ = [
    "GlobalKeyword",
    "InheritKeyword",
    "InitialKeyword",
    "UnsetKeyword",
]


class GlobalKeyword(Keyword):
    pass


class InheritKeyword(GlobalKeyword):
    pass


class InitialKeyword(GlobalKeyword):
    pass


class UnsetKeyword(GlobalKeyword):
    pass
