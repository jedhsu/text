"""

Syntax highlighting rule.

"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import re
from typing import Pattern

@dataclass

class Rule(metaclass=ABCMeta):
    pattern: Pattern



class SimpleRule(Rule):
    token_type: TokenType
    

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
