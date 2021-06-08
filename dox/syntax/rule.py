"""

Syntax highlighting rule.

"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import re
from typing import Pattern, TypeVar


__all__ = ["Rule"]


@dataclass
class Rule(metaclass=ABCMeta):
    pattern: Pattern

    @abstractmethod
    def apply():
        pass

    Simple = TypeVar("Simple")
    Capture = TypeVar("Capture")
    String = TypeVar("String")
    Identifier = TypeVar("Identifier")


class SimpleRule(Rule):
    token_type: TokenType

    def apply(self, highlight: Highlight):
        highlight.write_token(self.token_Type)


@dataclass
class CaptureRule(Rule):
    token_types: list[str]

    def apply(self, highlight: Highlight):
        match = highlight.scaner.last_match()

        for line in self.lines():
            pass


@dataclass
class StringRule(Rule):
    pattern: Pattern = re.compile(r"\\.")

    def __init__(self):
        return super(StringRule, self).__init__(self.pattern)

    def apply(self, highlight: Highlight):
        scanner = highlight.scannr()
        start = scanner.position - 1

        while not scanner.is_done():
            if scanner.scan(self.pattern()):
                if scanner.position > start:
                    highlight.write_token(
                        "s",
                        scanner.substring(start=scanner.position - 2),
                    )


@dataclass
class IdentifierRule(Rule):
    pattern = r"[a-zA-Z_][a-zA-Z0-9_]*"

    @staticmethod
    def apply(highlight: Highlight):
        identifier = highlight.scanner.last_match[0]
        # type = highlight.language.words[
        highlight.write_token(type)
