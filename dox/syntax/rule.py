"""

Syntax highlighting rule.

"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import re
from typing import Pattern

from .highlight import Highlight


@dataclass
class Rule(metaclass=ABCMeta):
    pattern: Pattern

    @abstractmethod
    def apply():
        pass


class SimpleRule(Rule):
    token_type: TokenType

    def apply(self, highlight: Highlight):
        highlight.write_token(self.token_Type)


@dataclass
class CaptureRule(Rule):
    pass


@dataclass
class StringRule(Rule):
    pass


@dataclass
class IdentifierRule(Rule):
    pass
