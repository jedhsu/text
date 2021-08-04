from abc import ABCMeta
from dataclasses import dataclass
from typing import Generic, Sequence, TypeVar, Union

T = TypeVar("T")


@dataclass
class Element(metaclass=ABCMeta):
    color: type
    style: type
    width: type


class Start(Generic[T]):
    color: type
    style: type
    width: type


class End(Generic[T]):
    color: type
    style: type
    width: type


class Width(Generic[T], Property):
    pass


class Selector(str):
    """
    Identifier.

    """

    def __init__(self, ident: str):
        super(Selector, self).__new__(str, ident)


@dataclass
class Ruleset:
    selectors: Sequence[Selector]
    declaration_block: DeclarationBlock


@dataclass
class Charset(AtRule):
    charset: str  # [TODO] restrict this to literal

    def __init__(self, charset: str):
        self.charset = charset
        super(Charset, self).__init__("charset")


class BoxSizing(Property):
    values = ["content-box", "border-box"]
