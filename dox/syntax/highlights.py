from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class _Highlight:
    is_xml: bool
    _buffer: str  # [TODO] what is this
    lexer: type
    # language: Language

    in_macro: bool = False


class _Compute_:
    @staticmethod
    def compute_line_length(line: str) -> int:
        pass


class _Write_:
    # [TODO] not sure if this necces
    # Chars = {
    #     "lessthan": "&lt;"
    #         }
    def write_char(self, char: int):
        pass

    def write_text(self, text: str):
        pass

    def write_token(self, type: TokenType, text=Optional[str]):
        pass


class _Format_:
    pass


class Highlight:
    pass
