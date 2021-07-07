from dataclasses import dataclass
from enum import Enum
from io import StringIO
from typing import Optional


@dataclass
class _Highlight:
    is_xml: bool
    lexer: type
    language: Language

    _buffer: StringIO  # [TODO] what is this
    in_macro: bool = False


class _Compute_(_Highlight):
    @staticmethod
    def compute_line_length(line: str) -> int:
        pass


class _Write_(_Highlight):
    def write_char(self, char: int):
        # just copy the structure lol
        if "less_than":
            self._buffer.write("&lt;")

    def write_text(self, text: str):
        pass

    def write_token(self, type: TokenType, text=Optional[str]):
        pass


class _Format_:
    pass


class Highlights:
    pass
