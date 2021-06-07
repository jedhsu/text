from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class _Highlights:
    is_xml: bool
    _buffer: str  # [TODO] what is this
    lexer: type
    language: Language

    in_macro: bool = False


class _Compute_:
    @staticmethod
    def compute_line_length(line: str) -> int:
        pass


class _Write_:
    def write_char(char: int):
        pass

    def write_text(text: str):
        pass

    def write_token(type: TokenType, text=Optional[str]):
        pass


class _Format_:
    pass


class Highlights:
    pass
