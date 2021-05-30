"""

Syntax highlighting rule.

"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class Rule(metaclass=ABCMeta):
    pass


@dataclass
class SimpleRule(Rule):
    token_type: TokenType

    @abstractmethod
    def apply(self):
        pass


@dataclass
class CaptureRule(Rule):
    pass


@dataclass
class StringRule(Rule):
    pass


@dataclass
class IdentifierRule(Rule):
    pass
